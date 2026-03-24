#ерём официальный slim-образ
FROM python:3.12-slim

LABEL maintainer="Effective Mobile DevOps"
LABEL description="Бэкенд-сервис на Python"

#создаём отдельного пользователя
RUN groupadd --system --gid 1001 appgroup \
 && useradd  --system --uid 1001 --gid appgroup \
             --no-create-home --shell /usr/sbin/nologin \
             appuser

WORKDIR /app

#копируем только сам скрипт
COPY --chown=appuser:appgroup app.py .

USER appuser

EXPOSE 8080

#HEALTHCHECK через чистый Python 
HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
    CMD python3 -c \
        "import http.client, sys; \
         c = http.client.HTTPConnection('localhost', 8080, timeout=4); \
         c.request('HEAD', '/'); \
         sys.exit(0 if c.getresponse().status == 200 else 1)"

#-u чтобы логи сразу шли в stdout
ENTRYPOINT ["python3", "-u", "app.py"]
