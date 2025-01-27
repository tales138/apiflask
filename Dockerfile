FROM python:3.13

WORKDIR ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

CMD [ "flask", "-app", "run", "run"]