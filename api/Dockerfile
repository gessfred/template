# TODO change to alpine
FROM ubuntu
RUN apt update -y && apt install -y python3 python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY *.py ./
COPY routers/ ./routers/
COPY tests/ ./tests/
ENTRYPOINT [ "uvicorn", "main:app" ]