FROM ubuntu:16.04
MAINTAINER Sanjeev Mehrotra <sanjeevm0@hotmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        curl \
        apt-utils \
        ssh \
        wget

# Install Go
ENV GOVERSION=1.8.1
ENV GOOS=linux
ENV GOARCH=amd64
RUN wget --no-check-certificate https://storage.googleapis.com/golang/go$GOVERSION.$GOOS-$GOARCH.tar.gz
RUN echo go$GOVERSION.$GOOS-$GOARCH.tar.gz
RUN tar -C /usr/local -xzf go$GOVERSION.$GOOS-$GOARCH.tar.gz
RUN rm go$GOVERSION.$GOOS-$GOARCH.tar.gz
ENV PATH=$PATH:/usr/local/go/bin
RUN mkdir /go
RUN mkdir /go/src
ENV GOPATH=/go

# SSH Keys
COPY id_rsa /root/.ssh/id_rsa
RUN chmod 400 /root/.ssh/id_rsa

# Get Kubernetes
#RUN go get k8s.io/kubernetes
RUN mkdir /go/src/k8s.io
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
RUN git clone git@github.com:MSRCCS/kubernetes /go/src/k8s.io/kubernetes
WORKDIR /go/src/k8s.io/kubernetes
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
RUN apt-get install ca-certificates
RUN update-ca-certificates
RUN go get github.com/tools/godep
RUN git checkout release-1.5-multigpu
#RUN make

