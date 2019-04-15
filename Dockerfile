FROM circleci/python:3.6
ADD . /code
WORKDIR /code
RUN ls
RUN python3 -m venv env
RUN pip install -r requirements.txt
EXPOSE 5000:5000