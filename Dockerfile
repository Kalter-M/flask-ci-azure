FROM circleci/python:3.6

EXPOSE 5000:5000

ADD . /code
WORKDIR /code
RUN ls
CMD python3 -m venv venv
CMD . venv/bin/activate
CMD pip install -r requirements.txt
RUN ["python", "hello.py"]

