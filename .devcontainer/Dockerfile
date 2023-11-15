FROM python:3.12

RUN apt-get update && \
    apt-get upgrade --yes

WORKDIR /workspaces/testapi

RUN pip install --upgrade pip
RUN pip install pylint pycodestyle