FROM python:3.12.1

WORKDIR /apiflask

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

#EXPOSE 4000

#CMD [ "flask", "-app", "run", "run"]