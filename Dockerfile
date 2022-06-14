FROM python:3.10

WORKDIR /utensils

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./utensils .

EXPOSE 5000
CMD ["python", "/utensils/main.py"]
