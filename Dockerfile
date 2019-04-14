FROM circleci/python:3.6

ADD . /code
WORKDIR /code
CMD ls
CMD python3 -m venv venv
CMD . venv/bin/activate
CMD pip install -r requirements.txt
CMD ["python", "hello.py"]

EXPOSE 5000:5000