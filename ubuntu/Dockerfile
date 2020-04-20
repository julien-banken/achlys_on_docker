FROM ubuntu:18.04

RUN apt-get update && apt-get install -y\ 
  git\
  curl\
  libssl-dev\
  make\
  automake\
  autoconf\
  libncurses5-dev\
  gcc\
  net-tools

# Install ASDF:

WORKDIR /root

ENV PATH="/root/bin:/root/.asdf/bin:/root/.asdf/shims:${PATH}"

RUN git clone --single-branch --branch v0.7.8 https://github.com/asdf-vm/asdf.git ~/.asdf && \
  echo '\n. $HOME/.asdf/asdf.sh' >> ~/.bashrc && \
  echo '\n. $HOME/.asdf/completions/asdf.bash' >> ~/.bashrc

RUN asdf update && \
  asdf plugin-add erlang && \
  asdf install erlang 22.0.4 && \
  asdf global erlang 22.0.4

# Install rebar3:

RUN mkdir /home/docker && \
  cd /home/docker && \
  git clone https://github.com/erlang/rebar3.git && \
  cd rebar3 && \
  ./bootstrap && \
  mkdir ~/bin && \
  cp rebar3 ~/bin/rebar3
