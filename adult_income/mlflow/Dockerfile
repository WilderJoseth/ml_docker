FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install mlflow
RUN chmod +x ./entrypoint.sh
CMD ["bash", "entrypoint.sh"]