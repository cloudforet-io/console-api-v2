FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV SPACEONE_PORT 50051
ENV SERVER_TYPE grpc
ENV PKG_DIR /tmp/pkg
ENV SRC_DIR /tmp/src
ENV CONF_DIR /etc/spaceone
ENV LOG_DIR /var/log/spaceone
ENV EXTENSION_NAME extension
ENV EXTENSION_SRC_DIR /opt/spaceone


COPY pkg/*.txt ${PKG_DIR}/

RUN pip install --upgrade pip && \
    pip install --upgrade -r ${PKG_DIR}/pip_requirements.txt

ARG CACHEBUST=1
RUN pip install --upgrade --pre spaceone-core spaceone-api

COPY src ${SRC_DIR}
WORKDIR ${SRC_DIR}
RUN python3 setup.py install && \
    rm -rf /tmp/*

EXPOSE ${SPACEONE_PORT}

ENTRYPOINT ["spaceone"]
CMD ["rest", "cloudforet.console_api_v2", "-m", "/opt"]
