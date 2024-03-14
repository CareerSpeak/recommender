FROM python:3.9-alpine

RUN mkdir -p /home/python/recommend

WORKDIR /home/python/recommend

COPY requirements.txt ./

RUN apk update && apk add --no-cache py3-scikit-learn
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 65535

ENTRYPOINT [ "python"]

CMD [ "service.py" ]
