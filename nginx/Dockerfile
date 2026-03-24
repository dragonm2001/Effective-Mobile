FROM nginx:1.27-alpine

LABEL maintainer="Effective Mobile DevOps"
LABEL description="Nginx reverse proxy"

RUN rm -f /etc/nginx/conf.d/default.conf \
          /etc/nginx/conf.d/*.conf \
          /etc/nginx/nginx.conf

#кладём наш конфиг на место стандартного
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

#healthcheck стучимся на наш же /nginx-health эндпоинт
HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost/nginx-health || exit 1
