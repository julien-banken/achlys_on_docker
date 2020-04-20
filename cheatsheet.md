# Cheat sheet

## Images

Show installed images:

```
docker images
```

Build an image:

```
docker build -t <tag> .
```

The dot indicates that the docker file is in the current directory.

Delete an image:

```
docker rmi <name>
```

Delete all images:

```
docker rmi -f $(docker images -a -q)
```

## Containers

Show running containers:

```
docker ps
```

Create a container:

```
docker run -d -p 80:80 --name achlys achlys
```

Start a container:

```
docker start <name>
```

Delete a container:

```
docker rm <tag>
```

Stop all containers:

```
docker stop $(docker ps -a -q)
```

Delete all containers:

```
docker rm $(docker ps -a -q)
```

Rename a container:

```
docker rename CONTAINER NEW_NAME
```

Show logs:

```
docker logs <name>
```

## Env variable

Show all environment variable

```
docker exec <name> env
```

Run container with an environment variable:

```
docker run -e VAR=VALUE ...
```

## Network

Create a network:

```
docker network create <network name>
```

Add a container to a network:

```
docker network connect <network name> <container name>
```

## Stack

Delete a stack:

```
docker stack rm <name>
```

Create a stack:

```
docker stack deploy -c scapp.yml scapp
```