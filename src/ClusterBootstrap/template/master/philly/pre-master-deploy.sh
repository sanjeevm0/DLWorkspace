sudo mkdir -p /etc/kubernetes
sudo mkdir -p /etc/kubernetes/manifests
sudo mkdir -p /etc/kubernetes/ssl/
sudo mkdir -p /etc/ssl/etcd
sudo mkdir -p /opt/addons/kube-addons
sudo rm -r /etc/kubernetes/manifests/*
sudo rm -r /etc/kubernetes/ssl/*
sudo rm -r /etc/ssl/etcd/*
sudo rm -r addons/kube-addons/*
sudo chown -R core /etc/kubernetes
sudo chown -R core /opt/addons/kube-addons
sudo docker rm -f $(docker ps -a | grep 'k8s_kube\|k8s_POD' | awk '{print $1}')
