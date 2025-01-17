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
ENV SWAGGER_UI_DIR=/opt/swagger-ui
ENV PACKAGE_VERSION=$PACKAGE_VERSION

COPY pkg/pip_requirements.txt pip_requirements.txt

RUN pip install --upgrade pip && \
    pip install --upgrade -r pip_requirements.txt
RUN apt-get update && apt-get install -y git

RUN mkdir -p ${OPENAPI_JSON_DIR} ${SWAGGER_UI_DIR}
WORKDIR ${GIT_DIR}
RUN git clone --branch ${BRANCH_NAME} https://github.com/cloudforet-io/api.git
RUN cp -r api/dist/openapi/* ${OPENAPI_JSON_DIR}
RUN rm -rf ${GIT_DIR}

WORKDIR ${SWAGGER_UI_DIR}
RUN wget -q https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui-bundle.js \
    && wget -q https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui.css \
    && wget -q https://cdn.jsdelivr.net/npm/swagger-ui-dist/swagger-ui.css.map \
    && wget -q https://fastapi.tiangolo.com/img/favicon.png

COPY src ${SRC_DIR}
WORKDIR ${SRC_DIR}

RUN python3 setup.py install && rm -rf /tmp/*

RUN pip install --upgrade spaceone-api

EXPOSE ${SPACEONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["run", "rest-server", "cloudforet.console_api_v2", "-m", "/opt", "--host", "0.0.0.0"]
