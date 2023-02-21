FROM python:3.9

RUN pip install flask
RUN pip install flask-cors

COPY /dev /app

# CMD ["python3", "--version"]

RUN pwd

WORKDIR /app

CMD ["flask", "--app", "local_development.py", "--debug", "run", "--host=0.0.0.0", "--port=8000"]