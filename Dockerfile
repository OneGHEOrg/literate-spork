FROM python:3.10

WORKDIR /utensils

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN echo "hello world"

COPY ./utensils .

EXPOSE 8080
CMD ["python", "/utensils/main.py"]
