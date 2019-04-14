FROM circleci/python:3.6

ADD . /code
WORKDIR /code
RUN python3 -m venv env \
 source ./env/bin/activate
RUN pip install -r requirements.txt
CMD ["python", "hello.py"]

EXPOSE 5000:5000