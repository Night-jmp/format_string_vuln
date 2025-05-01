FROM ubuntu:latest

RUN apt update && apt install -y make gcc libc6 socat

EXPOSE 1337

COPY . /app
WORKDIR /app

ENV ADMIN_PASS=63324fd5a244c4397953ca9131222d5c

RUN make vuln

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./vuln,pty,stderr
