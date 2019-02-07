From mysql:latest
ENV MYSQL_ROOT_PASSWORD 1234
ENV MYSQL_DATABASE mydata
ENV MYSQL_USER ninja
ENV MYSQL_PASSWORD 1234
ADD script.sql /docker-entrypoint-initdb.d
EXPOSE 3306
CMD ["mysqld"]
