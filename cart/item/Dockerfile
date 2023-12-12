FROM python:3.10

WORKDIR /item

COPY ./requirements.txt /item/
RUN ls
RUN pip install --no-cache-dir --upgrade -r /item/requirements.txt

COPY ./app /item/app

EXPOSE 81

CMD ["/bin/sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port 81"]