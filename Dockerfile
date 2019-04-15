FROM python:3.6

RUN mkdir /flask_ci
WORKDIR /flask_ci

COPY . /flask_ci
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python", "simpleapi.py"]