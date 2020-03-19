FROM python:3.6-alpine as BASE

FROM BASE as BUILD

COPY requirements.txt /install/
RUN pip install -r /install/requirements.txt 

FROM python:3.6-alpine as PROD

WORKDIR /app

RUN addgroup -S app && \
    adduser -S -G app app && \
    chown -R app:app /app && \
    apk --update --no-cache add curl    

COPY . /app/

COPY --from=BUILD /usr/local/ /usr/local

USER app

# RUN APP
CMD python manage.py
