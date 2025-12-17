FROM nginx:alpine

RUN rm -rf /etc/nginx/conf.d/*

COPY html/ /usr/share/nginx/html/

COPY nginx/ /etc/nginx/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]