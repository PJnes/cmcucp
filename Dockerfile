FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY cmcucp.py /app/cmcucp.py

ENTRYPOINT ["python", "/app/cmcucp.py"]