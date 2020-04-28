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

### Azure - docker-machine

Step 1: Install docker-machine

Step 2: Install Azure CLI

Step 3: Login to Azure

```
az login
```

Step 4: get the subscription id

```
sub=$(az account show --query "id" -o tsv)
```

Step 5: Spawn a new VM

List all location:

```
az account list-locations
az account list-locations -o table
```

List of images:

```
az vm image list --output table
```

```
docker-machine create -d azure \
    --azure-subscription-id $sub \
    --azure-ssh-user azureuser \
    --azure-open-port 80 \
    --azure-size "Standard_D2s_v3" \
    --azure-location "eastus" \
    --azure-image "Canonical:UbuntuServer:18.04-LTS:latest" \
    achlys1
```

## Tips

Fix ssh disconnection with the vm:

```
sudo dhclient enp0s8 -v
```

## Documentation

- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/#)
- [Guide Azure](https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html)
- [Azure credentials](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)