#!/usr/bin/env bash
# Add a custom HTTP header with Puppet

$nginx_config_content = "server {
   listen 80 default_server;
   listen [::]:80 default_server;
   
   root /var/www/html;
   index index.html;
   location /redirect_me {
      return 301 https://upschool.com/register;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }

   location / {
      add_header X-Served-By \$hostname;
      try_files \$uri \$uri/ =404;
   }
}"

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => $nginx_config_content,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
