FROM alpine:3.3
MAINTAINER Harald Nezbeda <HNezbeda@anexia-it.com>

RUN apk add --update --no-cache build-base python-dev py-pip py-docutils && \
    pip install maildump && \
    apk del build-base && \
    rm -rf /var/cache/apk/* /root/.cache

EXPOSE 1080 1025

ENTRYPOINT [ "maildump", "-fn", "--db", "/maildump.db", "--smtp-ip", "0.0.0.0", "--http-ip", "0.0.0.0" ]
