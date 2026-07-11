FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y iputils-ping
RUN pip install psutil

CMD ["python", "system_check.py"]