FROM python:3

WORKDIR /usr/src/app/marvel

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV MONGO_DB_USERNAME=admin MONGO_DB_PWD=password

COPY . .
EXPOSE 5005 
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
#CMD [ "python3", "app.py" ]