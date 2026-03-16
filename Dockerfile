FROM python:3.14-slim-bookworm

# copies files and directories from current directory to WORKDIR
COPY . .

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./start.sh .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
