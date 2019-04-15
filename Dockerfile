FROM python:3.6

RUN mkdir /flask_ci
WORKDIR /flask_ci

COPY . /flask_ci

EXPOSE 5000:5000

CMD ["python", "simpleapi.py"]