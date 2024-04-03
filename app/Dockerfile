
FROM alpine
RUN apk add --update nodejs npm
RUN npm install --global serve
WORKDIR /app
COPY package.json /app
RUN npm install
COPY src ./src
COPY public/ ./public/
COPY *.config.js .
COPY index.html .
RUN NODE_OPTIONS=--openssl-legacy-provider npm run build
RUN ls dist/ && echo 'Build output [OK]'
RUN rm -rf node_modules/
COPY serve.sh .
RUN chmod u+wrx serve.sh
ENTRYPOINT ["./serve.sh"]
ENV HTTP_PORT 8080
EXPOSE 8080