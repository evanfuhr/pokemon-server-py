FROM python:3-alpine


# Setup dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# RUN apk add curl

# Setup app
EXPOSE 5000
COPY container_files .

CMD ["python", "./server.py"]

