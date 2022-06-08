FROM python:3.10

WORKDIR /utensils

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./utensils .

RUN sleep 1200

EXPOSE 5000
CMD ["python", "/utensils/main.py"]
