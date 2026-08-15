FROM python:alpine

WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]

