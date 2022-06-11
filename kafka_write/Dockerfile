FROM python:3.9-slim

RUN pip install --upgrade pip
COPY requirements.txt /opt/app/requirements.txt
RUN python3 -m pip install -r /opt/app/requirements.txt
RUN pip install requests

COPY ./main.py /opt/app/main.py

ENTRYPOINT ["python", "-u", "/opt/app/main.py"]
