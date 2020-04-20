FROM my-ubuntu

RUN cd /home/docker && \
  git clone --branch map-reduce https://github.com/nxanthos/achlys.git && \
  cd /home/docker/achlys && \
  rebar3 get-deps && \
  rebar3 do update, unlock, upgrade && \
  rebar3 compile