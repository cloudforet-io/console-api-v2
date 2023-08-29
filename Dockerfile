FROM cloudforet/python-core:1.12
ARG PACKAGE_VERSION
ENV PYTHONUNBUFFERED 1
ENV SPACEONE_PORT 50051
ENV SRC_DIR /tmp/src
ENV CONF_DIR /etc/spaceone
ENV LOG_DIR /var/log/spaceone
ENV GIT_DIR /tmp/git
ENV EXTENSION_SWAGGER_DIR /opt/cloudforet/openapi
ENV PACKAGE_VERSION=$PACKAGE_VERSION

COPY pkg/pip_requirements.txt pip_requirements.txt

RUN pip install --upgrade -r pip_requirements.txt
RUN apt-get update && apt-get install -y git

RUN mkdir -p ${EXTENSION_SWAGGER_DIR}
WORKDIR ${GIT_DIR}
RUN git clone https://github.com/cloudforet-io/api.git
RUN cp api/dist/openapi/* ${EXTENSION_SWAGGER_DIR}

COPY src ${SRC_DIR}
WORKDIR ${SRC_DIR}

RUN python3 setup.py install && rm -rf /tmp/*

RUN pip install --upgrade spaceone-api

EXPOSE ${SPACEONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["rest", "cloudforet.console_api_v2", "-m", "/opt"]
