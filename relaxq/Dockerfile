from python:3
copy ./requirements.txt /app/
run pip install -r /app/requirements.txt
copy ./src/ /app/src/
workdir /app/src
env FLASK_APP=relaxq.py
cmd flask run --host=0.0.0.0
expose 5000
