FROM python:3.6

RUN mkdir /flask_ci
WORKDIR /flask_ci

COPY . /flask_ci
RUN sudo python3 -m venv venv
RUN sudo pip install -r requirements.txt
EXPOSE 5000:5000

CMD ["python", "simpleapi.py"]