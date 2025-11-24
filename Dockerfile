FROM cloudforet/python-core:2.0
ARG PACKAGE_VERSION
ARG BRANCH_NAME=master
ENV PYTHONUNBUFFERED=1
ENV SPACEONE_PORT=8000
ENV SRC_DIR=/tmp/src
ENV CONF_DIR=/etc/spaceone
ENV LOG_DIR=/var/log/spaceone
ENV GIT_DIR=/tmp/git
ENV OPENAPI_JSON_DIR=/opt/openapi
ENV PACKAGE_VERSION=$PACKAGE_VERSION

COPY pkg/pip_requirements.txt pip_requirements.txt

RUN pip install --upgrade pip && \
    pip install --upgrade -r pip_requirements.txt && \
    pip install --upgrade 'protobuf>=4.0.0,<6.0.0'

# Security: Install git with minimal dependencies and clean up apt cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p ${OPENAPI_JSON_DIR}
WORKDIR ${GIT_DIR}
RUN git clone --branch ${BRANCH_NAME} https://github.com/cloudforet-io/api.git
RUN cp -r api/dist/openapi/* ${OPENAPI_JSON_DIR}
RUN rm -rf ${GIT_DIR}

COPY src ${SRC_DIR}
WORKDIR ${SRC_DIR}

RUN python3 setup.py install && rm -rf /tmp/*

RUN pip install --upgrade spaceone-api

# Security: Create non-root user and set ownership
RUN useradd -m -u 1000 spaceone && \
    mkdir -p ${CONF_DIR} ${LOG_DIR} && \
    chown -R spaceone:spaceone ${SRC_DIR} ${CONF_DIR} ${LOG_DIR} ${OPENAPI_JSON_DIR} && \
    chown -R spaceone:spaceone /home/spaceone

USER spaceone

EXPOSE ${SPACEONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["run", "rest-server", "cloudforet.console_api_v2", "-m", "/opt"]
