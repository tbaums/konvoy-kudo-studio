FROM node:12-alpine
WORKDIR /app
COPY . .
RUN npm install --save
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]