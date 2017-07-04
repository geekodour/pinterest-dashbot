apt-get update
apt-get install libfontconfig rabbitmq-server python3-pip
getPhantom(){
cd /usr/bin/
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xvf phantomjs-2.1.1-linux-x86_64.tar.bz2
cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs .
}
getPhantom
pip3 install virtualenv
git clone https://github.com/geekodour/pinterest-dashbot.git
genEnv(){
cd pinterest-dashbot/
virtualenv env
pip install -r requirements.txt
}

