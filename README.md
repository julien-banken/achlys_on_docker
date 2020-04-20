# Achlys on docker

## Installation

### Docker swarm

Step 1: Install docker

Step 2: Build the images with `build.sh` 

Step 3: Init the docker swarm on one machine

```
docker swarm init --advertise-addr <ip of the vm>
```

Step 4: Join the docker swarm on the other machines

```
docker swarm join --token <token> <ip of the vm>:<port>
```

Step 5: Deploy the stack:

```
docker stack deploy -c achlys.yml achlys_app
```

Remove the stack:

```
docker stack rm achlys_app
```

### Debugging

```
docker ps -a
docker exec -it <container id/name> /bin/bash
erl -sname remote_shell -remsh achlys0@node1 -setcookie MyCookie
```

## Tips

Fix ssh disconnection with the vm:

```
sudo dhclient enp0s8 -v
```

## Documentation

- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/#)