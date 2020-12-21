FROM python:3.9

WORKDIR /opt/app

COPY . .
RUN pip3 install --upgrade pip -r requirements.txt
RUN find . -name __pycache__ -type d -delete

ENV TZ=Asia/Yekaterinburg
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python3", "-m", "src"]

