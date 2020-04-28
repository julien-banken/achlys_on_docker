#!/usr/bin/env python3

import docker
from graph import *

# achlys@<service name>

def get_service_name(k):
  return "achlys@node{0}".format(k)

def get_boards(neighbors):
  return ",".join([get_service_name(k) for k in neighbors])

def run(client, n):
  for (i, neighbors) in enumerate(full_mesh_topology(n)):
    
    service_name = get_service_name(i)
    boards = get_boards(neighbors)

    print("node: {0}".format(service_name))
    print("boards: {0}".format(boards))
    # https://docker-py.readthedocs.io/en/stable/user_guides/swarm_services.html
    
    # print(i)
    # print(neightbors)

if __name__ == '__main__':

  # https://docker-py.readthedocs.io/en/stable/user_guides/swarm_services.html
  
  # achlys_app
  
  client = docker.APIClient(base_url='unix://var/run/docker.sock')
  print(client)
  print(client.version())
  print(client.ping())

  # https://docker-py.readthedocs.io/en/stable/api.html
  # https://docker-py.readthedocs.io/en/stable/api.html#docker.types.ContainerSpec
  
  container_spec = docker.types.ContainerSpec(
    hostname='node3',
    image='achlys:latest',
    tty=True,
    command=[]
  )
  
  task_tmpl = docker.types.TaskTemplate(
    container_spec
  )

  service_id = client.create_service(
    task_tmpl,
    networks=['achlys_app_achlys-net'],
    name="node3"
  )

  # client.remove_service('node3')

  # for container in client.containers.list():
  #   print("id={0}".format(container.id))
  #   print("name={0}".format(container.name))
  #   print("status={0}".format(container.status))
  # run(15)
