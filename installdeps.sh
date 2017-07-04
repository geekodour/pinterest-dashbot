#!/bin/bash
apt-get update
#apt-get install -y libfontconfig rabbitmq-server python3-pip git
apt-get install -y libfontconfig git
getPhantom(){
cd /usr/bin/
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xvf phantomjs-2.1.1-linux-x86_64.tar.bz2
cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs .
cd ~
}
getPhantom
#pip3 install virtualenv
git clone https://github.com/geekodour/pinterest-dashbot.git
installDeps(){
cd pinterest-dashbot/
pip3 install -r requirements.txt
}
installDeps
#genEnv(){
#cd pinterest-dashbot/
#virtualenv env
#. env/bin/activate
#pip install -r requirements.txt
#deactivate
#}
#genEnv
#setupRabbit(){
#rabbitmqctl add_user pin pinpin
#rabbitmqctl add_vhost pinvh
#rabbitmqctl set_user_tags pin pintag
#rabbitmqctl set_permissions -p pinvh pin ".*" ".*" ".*"
#}
#setupRabbit
