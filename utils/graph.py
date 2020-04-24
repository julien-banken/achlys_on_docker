import random

def get_node_list(n):
  return [[] for _ in range(n)]

def star_topology(n):
  nodes = get_node_list(n)
  for i in range(1, n):
    nodes[0].append(i)
  for i in range(1, n):
    nodes[i].append(0)
  return nodes

def ring_topology(n):
  nodes = get_node_list(n)
  for i in range(n):
    nodes[i].append((i + n - 1) % n)
    nodes[i].append((i + 1) % n)
  return nodes

def line_topology(n):
  nodes = get_node_list(n)
  for i in range(n - 1):
    nodes[i].append(i + 1)
    nodes[i + 1].append(i)
  return nodes

def full_mesh_topology(n):
  nodes = []
  for i in range(n):
    nodes.append([j for j in range(n) if j != i])
  return nodes

def mesh_topology(n):
  nodes = get_node_list(n)
  visited = [0]
  for i in range(1, n):
    j = random.choice(visited)
    nodes[i].append(j)
    nodes[j].append(i)
    visited.append(i)
  return nodes
