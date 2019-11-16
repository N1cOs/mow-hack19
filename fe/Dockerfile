FROM node:12.13.0-alpine as builder

COPY . /app

WORKDIR /app

RUN npm install 

RUN npm run build

FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

COPY --from=builder /app/dist /usr/share/nginx/html