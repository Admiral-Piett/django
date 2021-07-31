FROM python:3.9.1-alpine

ENV PYTHONPATH=/opt/svc

WORKDIR /opt/svc

COPY src/ ./
COPY tox.ini/ ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["pytest", "tests/unit/"]
#CMD ["python", "main.py"]
