#!/bin/bash 

sudo apt-get update 
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
        apt-utils \
        software-properties-common \
        build-essential \
        cmake \
        git \
        curl \
        wget \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        cpio \
        mkisofs \
        apt-transport-https \
        openssh-client \
        ca-certificates \
        vim \
        sudo \
        git-all \
        sshpass \
        bison \
        libcurl4-openssl-dev libssl-dev 

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-key fingerprint 0EBFCD88

# Install docker
echo "Docker Installation .... "
sudo apt-get update
sudo apt-get install docker-ce

echo "PIP installation .... "
sudo pip install --upgrade pip
sudo pip install setuptools 
sudo pip install pyyaml jinja2 flask flask.restful tzlocal pycurl

echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" | \
     sudo tee /etc/apt/sources.list.d/azure-cli.list

sudo apt-key adv --keyserver packages.microsoft.com --recv-keys 417A0893
sudo apt-get install apt-transport-https
sudo apt-get update && sudo apt-get install azure-cli



