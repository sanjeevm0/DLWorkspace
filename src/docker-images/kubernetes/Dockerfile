FROM ubuntu:16.04
MAINTAINER Sanjeev Mehrotra <sanjeevm0@hotmail.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        curl \
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

# Get Kubernetes
#RUN go get k8s.io/kubernetes
RUN mkdir /go/src/k8s.io
RUN git clone https://github.com/MSRCCS/kubernetes /go/src/k8s.io/kubernetes
RUN cd /go/src/k8s.io/kubernetes
RUN make

