FROM python:3.9-alpine3.15

RUN apk update && apk upgrade && apk --no-cache add curl unzip

RUN apk --no-cache add firefox-esr xvfb

RUN curl -sSL https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz | tar xz -C /usr/local/bin

ENV export=DISPLAY=:0

RUN Xvfb :0 -screen 0 1920x1080x16 &

WORKDIR /screen/

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY screenshot.py .

RUN chmod +x screenshot.py
CMD [ "python3", "screenshot.py" ]
