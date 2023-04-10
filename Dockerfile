FROM python:3.9-alpine3.13
LABEL maintainer="https://github.com/ywyder"

ENV PYTHONUNBUFFERED 1

# copy files to docker container and expose on port 8000
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
# create virtual env in docker, install requirements, create user (to not use the root to run the application)
RUN python -m venv /py && \ 
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ];  \
        then /py/bin/pip install -r /tmp/requirements.dev.txt;\
    fi && \ 
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
