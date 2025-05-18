FROM python:3.13-alpine AS base
ENV PYTHONUNBUFFERED=1 \
    TALKOPS_SOCKET=/tmp/talkops.sock \
    TALKOPS_STDERR=/tmp/talkops.stderr.log \
    TALKOPS_STDOUT=/tmp/talkops.stdout.log
RUN apk add --no-cache nodejs npm && \
    npm install -g pm2@6.0.6 talkops-client@1.0.0 && \
    mkdir /.cache && \
    mkdir /.local && \
    mkdir /.pm2 && \
    mkdir /app && \
    mkdir /data && \
    chown -R 1000:1000 /.cache /.local /.pm2 /app /data
WORKDIR /app

FROM base AS dev
USER 1000:1000
VOLUME [ "/app" ]
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["pm2-runtime", "ecosystem.config.cjs"]

FROM base
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src src
USER 1000:1000
CMD ["pm2-runtime", "ecosystem.config.cjs"]
