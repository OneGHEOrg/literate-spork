FROM python:3.10

RUN mkdir /utensils
WORKDIR /utensils
ADD . /utensils/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/utensils/main.py"]