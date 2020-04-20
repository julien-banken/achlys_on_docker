#!/usr/bin/env python3

import docker

if __name__ == '__main__':
  client = docker.from_env()
  # print(client)
  # print(client.ping())
  print(client.containers.list())
  for container in client.containers.list():
    print("id={0}".format(container.id))
    print("name={0}".format(container.name))
    print("status={0}".format(container.status))
