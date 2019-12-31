FROM php:7.2-apache
RUN apt-get update && \
	docker-php-ext-install mysqli && \
	a2enmod rewrite && \
	service apache2 restart