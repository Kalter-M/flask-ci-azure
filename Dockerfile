FROM circleci/python:3.6
ADD . /code
WORKDIR /code
RUN ls
RUN sudo python3 -m venv venv
RUN sudo pip install -r requirements.txt
EXPOSE 5000:5000
CMD ["python", "tests.py"]
