#!/usr/bin/python 
import sys
sys.path
sys.path.append('../../ClusterBootstrap')
sys.path.append('../../utils')

import utils
import yaml
import os
import DockerUtils

os.chdir(os.path.dirname(__file__))

config = yaml.load("config.yaml")
utils.render_template("Dockerfile.template", "./deploy/Dockerfile", config)

os.chdir("./deploy")
dockerBld = "docker build --build-arg NOCACHE=$(date +%s) -t " + config["k8s-bld"] + " ."
print dockerBld
os.system(dockerBld)

os.system("mkdir -p bin")
DockerUtils.copy_from_docker_image(config["k8s-bld"], "/hyperkube", "/bin/hyperkube")

os.chdir("../kubernetes")
dockerBld = "docker build -t " + config["k8s-pushto"] + " ."
print dockerBld
os.system(dockerBld)

dockerPush = "docker push " + config["k8s-pushto"]
print dockerPush
os.system(dockerPush)

