import argparse
import sys
import random

config = {
  'n': 5,
  'hostname': 'localhost',
  'prefix': 'achlys'
}

def get_node_list(n):
  nodes = []
  for i in range(n):
    nodes.append([])
  return nodes

def star_topology(n):
  nodes = get_node_list(n)
  for i in range(1, n):
    nodes[0].append(i)
  for i in range(1, n):
    nodes[i].append(0)
  print_structure(nodes)

def ring_topology(n):
  nodes = get_node_list(n)
  for i in range(n):
    nodes[i].append((i + n - 1) % n)
    nodes[i].append((i + 1) % n)
  print_structure(nodes)

def line_topology(n):
  nodes = get_node_list(n)
  for i in range(n - 1):
    nodes[i].append(i + 1)
    nodes[i + 1].append(i)
  print_structure(nodes)

def full_mesh_topology(n):
  nodes = get_node_list(n)
  for i in range(n):
    nodes[i] = [j for j in range(n) if j != i]
  print_structure(nodes)

def mesh_topology(n):
  nodes = get_node_list(n)
  visited = [0]
  for i in range(1, n):
    j = random.choice(visited)
    nodes[i].append(j)
    nodes[j].append(i)
    visited.append(i)
  print_structure(nodes)

def print_structure(nodes):
  separator = ' , '
  prefix = config['prefix']
  hostname = config['hostname']
  for i in range(len(nodes)):
    boards = separator.join([f'{prefix}{j}@{hostname}' for j in nodes[i]])
    print(f"({prefix}{i}@{hostname})[{boards}]")

if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('--n', help='Number of nodes')
  parser.add_argument('--hostname', help='Hostname of the node')
  parser.add_argument('--prefix', help='Prefix of the sname')
  parser.add_argument('--type', help='Structure of the network')

  args = parser.parse_args()

  if args.n:
    config['n'] = int(args.n)
  if args.hostname:
    config['hostname'] = args.hostname
  if args.prefix:
    config['prefix'] = args.prefix

  n = config['n']
  if args.type:
    if args.type == 'star':
      star_topology(n)
    elif args.type == 'ring':
      ring_topology(n)
    elif args.type == 'line':
      line_topology(n)
    elif args.type == 'mesh':
      mesh_topology(n)
    else:
      full_mesh_topology(n)
  else:
    full_mesh_topology(n)
