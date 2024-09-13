FROM python:3.8-slim-buster

WORKDIR /src

ADD ./ /src

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 

CMD ["python", "main.py"]