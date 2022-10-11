FROM node:16-alpine

WORKDIR /app

#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
ENV CHOKIDAR_USEPOLLING=true

ADD . .

RUN npm install

RUN ls /app

#ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 5173

CMD ["npm", "run", "dev"]