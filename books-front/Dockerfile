FROM node:20 AS build

WORKDIR /usr/src/app

COPY . /usr/src/app

EXPOSE 8080

RUN npm install -g @angular/cli

RUN npm install

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "8080"]