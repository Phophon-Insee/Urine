FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

WORKDIR /app
# CMD ["uvicorn", "app.Urine:app", "--host", "0.0.0.0", "--port", "8000"]
RUN pip3 install numpy
RUN pip3 install tensorflow==2.4.0
RUN pip3 install pillow

EXPOSE 8000