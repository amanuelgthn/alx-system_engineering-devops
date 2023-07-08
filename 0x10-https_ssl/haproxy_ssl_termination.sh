#!/usr/bin/env bash
#terminating SSL on HAproxy
#Bash script that configures HAproxy so that it send traffic to web-01 and web-02,distributes requests using a roundrobin algorithm and the HAproxy server can be managed via an init script

balancer="\
frontend haproxy_balancer
    bind *:80
    mode http
    default_backend webserver

backend webservers
    balance roundrobin
    server 187642-web-01 54.90.59.65:80 check
    server 187642-web-02 18.235.248.54:80 
    
     location / {
        return 200 Holberton School;
    }
"
#Adding htpps load balancing to listen on port 443 on mode TCP
balance_https="\
frontend htpps_lb
    bind *:443 ssl crt /etc/haproxy/certs/$DOMAIN.pem
    reqadd X-Forwarded-Proto:\ https
    reqadd X-Holberton-School: 1
    default_backend webserver
"
# Update packages
apt-get -y update
apt-get -y upgrade

# install certbot/ SSL certificate installation
sudo apt-get install software-properties-common
sudo apt-get-repositry ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot

#get the certificate
sudo certbot certonly --standalone -d amanuelbikoradev.tech -d www.amanuelbikoradev.tech

# combine the fullchain.pem and privekey.pem which are created when the above get certificate, certbot certonly command is run, the certonly command uses the openssl command line to create these files
# save the keys to /etc/haproxy/certs folder
sudo mkdir -p /etc/haproxy/certs #createsa the folder if does not exist
DOMAIN='amanuelbikoradev.tech'
sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/letsencrypt/live/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs

#backup the default configuration file
mv etc/haproxy/haproxy.cfg{, _backup}


# Update packages
apt-get -y update
apt-get -y upgrade

# Add HAProxy PPA
apt-get -y install software-properties-common
add-apt-repository -y ppa:vbernat/haproxy-2.5
apt-get -y update

# Install HAProxy
apt-get -y install haproxy
cp -a /etc/haproxy/haproxy.cfg{,.orig}
echo "$balancer" >> /etc/haproxy/haproxy.cfg
echo :"$balance_https" >> /etc/haproxy/haproxy.cfg

systemctl restart haproxy



