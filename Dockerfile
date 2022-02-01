FROM python:3.10

RUN mkdir /utensils
COPY ./utensils/main.py /utensils
WORKDIR /utensils
ADD . /utensils/
RUN cd ..
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/utensils/main.py"]