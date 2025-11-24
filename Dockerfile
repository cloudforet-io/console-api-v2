# ========================================
# Stage 1: Builder
# ========================================
FROM cloudforet/python-core:2.0 as builder

ARG BRANCH_NAME=master
ENV GIT_DIR=/tmp/git
ENV OPENAPI_JSON_DIR=/opt/openapi
ENV BUILD_DIR=/tmp/build

# Install Build Dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Security Fix: protobuf CVE-2025-4565
# Step 1: Forcefully remove old protobuf files from base image
RUN pip install --no-cache-dir --upgrade pip && \
    rm -rf /usr/local/lib/python3.10/site-packages/google/protobuf* && \
    rm -rf /usr/local/lib/python3.10/site-packages/protobuf* && \
    find /usr/local/lib/python3.10/site-packages -type f -name "*protobuf*" -delete && \
    find /usr/local/lib/python3.10/site-packages -type d -name "*protobuf*" -exec rm -rf {} + 2>/dev/null || true

# Step 2: Install safe protobuf version (4.25.8 or later)
RUN pip install --no-cache-dir --ignore-installed --no-deps 'protobuf>=4.25.8,<5.0.0'

# Step 3: Reinstall dependent packages
RUN pip install --no-cache-dir --ignore-installed --no-deps \
    'googleapis-common-protos>=1.56.0' \
    'proto-plus>=1.22.0'

# Build Python wheels for faster installation
COPY pkg/pip_requirements.txt /tmp/pip_requirements.txt
RUN pip wheel --no-cache-dir --wheel-dir /tmp/wheels -r /tmp/pip_requirements.txt

# Clone OpenAPI Repository
RUN mkdir -p ${OPENAPI_JSON_DIR}
WORKDIR ${GIT_DIR}
RUN git clone --branch ${BRANCH_NAME} https://github.com/cloudforet-io/api.git && \
    cp -r api/dist/openapi/* ${OPENAPI_JSON_DIR} && \
    rm -rf ${GIT_DIR}

# Build Application
COPY src ${BUILD_DIR}/src
WORKDIR ${BUILD_DIR}/src
RUN python3 setup.py bdist_wheel -d /tmp/dist

# ========================================
# Stage 2: Runtime (Minimal & Secure)
# ========================================
FROM cloudforet/python-core:2.0

ARG PACKAGE_VERSION
ENV PYTHONUNBUFFERED=1
ENV SPACEONE_PORT=8000
ENV SRC_DIR=/opt/spaceone
ENV CONF_DIR=/etc/spaceone
ENV LOG_DIR=/var/log/spaceone
ENV OPENAPI_JSON_DIR=/opt/openapi
ENV PACKAGE_VERSION=$PACKAGE_VERSION

# Security Fix: protobuf CVE-2025-4565
# CRITICAL: Complete removal and reinstallation in runtime stage
RUN pip install --no-cache-dir --upgrade pip

# Step 1: Forcefully remove ALL protobuf files from system
RUN rm -rf /usr/local/lib/python3.10/site-packages/google/protobuf* && \
    rm -rf /usr/local/lib/python3.10/site-packages/protobuf* && \
    find /usr/local/lib/python3.10/site-packages -type f -name "*protobuf*" -delete && \
    find /usr/local/lib/python3.10/site-packages -type d -name "*protobuf*" -exec rm -rf {} + 2>/dev/null || true

# Step 2: Remove dist-info directories
RUN rm -rf /usr/local/lib/python3.10/site-packages/protobuf*.dist-info && \
    rm -rf /usr/local/lib/python3.10/site-packages/googleapis_common_protos*.dist-info && \
    rm -rf /usr/local/lib/python3.10/site-packages/proto_plus*.dist-info

# Step 3: Install safe protobuf 4.25.8 with NO dependencies check
RUN pip install --no-cache-dir --ignore-installed --no-deps 'protobuf>=4.25.8,<5.0.0'

# Step 4: Reinstall protobuf-dependent packages to work with 4.x
RUN pip install --no-cache-dir --ignore-installed --no-deps \
    'googleapis-common-protos>=1.56.0' \
    'proto-plus>=1.22.0'

# Verify protobuf installation
RUN python3 -c "import google.protobuf; print(f'✅ Protobuf version: {google.protobuf.__version__}')"

# Security Fix: System Package Updates
# Update critical system packages with security patches
RUN apt-get update && \
    apt-get upgrade -y \
    curl \
    libcurl4 \
    libgnutls30t64 \
    libsqlite3-0 \
    linux-libc-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Built Artifacts from Builder
COPY --from=builder /tmp/wheels /tmp/wheels
COPY --from=builder /tmp/dist/*.whl /tmp/
COPY --from=builder ${OPENAPI_JSON_DIR} ${OPENAPI_JSON_DIR}

# Install Application and Dependencies
RUN pip install --no-cache-dir --no-deps /tmp/wheels/*.whl && \
    pip install --no-cache-dir --no-deps /tmp/*.whl && \
    rm -rf /tmp/wheels /tmp/*.whl

# Reinstall spaceone-api with all dependencies (will use protobuf 4.x)
RUN pip install --no-cache-dir --upgrade spaceone-api

# Final verification
RUN python3 -c "import google.protobuf; v=google.protobuf.__version__; print(f'✅ Final protobuf: {v}'); \
    parts=list(map(int,v.split('.'))); \
    assert (parts[0]==4 and parts[1]>=25 and parts[2]>=8) or (parts[0]==5 and parts[1]>=29) or (parts[0]>=6), \
    'protobuf version must be >=4.25.8'"

# Security: Remove Unnecessary Build Packages
# Reduce attack surface by removing compiler toolchain
RUN apt-get update && \
    apt-get purge -y --auto-remove \
    gcc g++ binutils make 2>/dev/null || true && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Security: Create Non-root User
RUN useradd -m -u 1000 spaceone && \
    mkdir -p ${SRC_DIR} ${CONF_DIR} ${LOG_DIR} && \
    chown -R spaceone:spaceone ${SRC_DIR} ${CONF_DIR} ${LOG_DIR} ${OPENAPI_JSON_DIR} && \
    chown -R spaceone:spaceone /home/spaceone

USER spaceone
WORKDIR ${SRC_DIR}

EXPOSE ${SPACEONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["run", "rest-server", "cloudforet.console_api_v2", "-m", "/opt"]
