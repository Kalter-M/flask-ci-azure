FROM circleci/python:3.6



ADD . /code
COPY . /code
WORKDIR /code
RUN ls
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
EXPOSE 5000:5000