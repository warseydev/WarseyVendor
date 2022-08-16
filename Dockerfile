FROM ubuntu:latest
COPY src /usr/share/warseyvendor/

EXPOSE 6001

WORKDIR /usr/share/warseyvendor/

RUN apt update && apt install python3 python3-pip python3-dev curl gcc g++ -y

RUN pip3 install flask waitress flask_limiter flask_login pandas passlib

RUN mkdir /usr/share/warseyvendor/appdata && echo "{}" > /usr/share/warseyvendor/appdata/users.json && echo "{}" > /usr/share/warseyvendor/appdata/userpriv.json && mkdir /usr/share/warseyvendor/appdata/invitecodes

ENTRYPOINT python3 app.py