FROM python:3.12-slim AS base
ENV PYTHONUNBUFFERED=1
RUN useradd -u 1000 --create-home appuser && \
    mkdir /app && mkdir /data && \
    chown -R appuser:appuser /app /data /home/appuser
WORKDIR /app

FROM base AS dev
ENV ENV=development
RUN pip install --no-cache-dir watchdog
USER 1000:1000
VOLUME [ "/app" ]
ENTRYPOINT [ "./entrypoint.sh" ]
CMD ["watchmedo", "auto-restart", "--directory=.", "--pattern=*.py", "--recursive", "--", "python", "main.py" ]

FROM base
ENV ENV=production
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
COPY src src
USER 1000:1000
CMD ["python", "main.py"]
