FROM nginx:latest


RUN mkdir -p /nginx_proxy_cache

COPY ./docker/nginx/django.proxy /etc/nginx/conf.d
COPY ./docker/nginx/django.conf /etc/nginx/conf.d
