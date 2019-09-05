# Docker hands-on
---

## Dockerfile cheatsheet
|Command|Description|
|--|--|
|`FROM`|Define base image|
|`RUN`|Execute command when building image|
|`EXPOSE`|Informs on which ports listen at runtime|
|`ENV`|Environment variable|
|`ARG`|Build-time variable|
|`ADD`|Copy new files from local or URL|
|`COPY`|Copy files from local|
|`ENTRYPOINT`|Default  executable  when running container|
|`CMD`|Command passed to entrypoint|
|`VOLUME`|Informs  that a volume can  be  mount  between host and container|
|`WORKDIR`|Set the  working directory|
<br>
<br>


## docker build cheatsheet

### docker build syntax

`docker build --params dockerfileDirectory`

|Parameter|Description|Example|
|--|--|--|
|`build-arg`|Define  build-time variables|`docker build --build-args  argName=value dockerfileDirectory`|
|`-q, --quiet`|Silent mode when building|`docker build –q dockerfileDirectory`|
|`-t, --tag`|Image  name (name:tag format)|`docker build –t imageName  dockerfileDirectory`|
<br>
<br>


## docker run cheatsheet

### docker run syntax

`docker run --params imageName cmdToExecute`

|Parameter|Description|Example|
|--|--|--|
|`-d, --detach`|Run container in background|`docker run -d imageName cmdToExecute`|
|`--entrypoint`|Overwrite default entrypoint|`docker run --entrypoint "myEntrypoint" imageName cmdToExecute`|
|`-e, --env`|Define environment variables|`docker run -e "envVarName=value" imageName cmdToExecute`|
|`-i, --interactive`|Keep STDIN open|`docker run -i imageName cmdToExecute`|
|`--name`|Name of the container|`docker run --name containerName imageName cmdToExecute`|
|`-p, --publish`|Publish container's port|`docker run -p hostPort:containerPort imageName cmdToExecute`|
|`-v, --volume`|Mount a volume|`docker run -v hostPath:containerPath imageName cmdToExecute`|
|`-t, --tty`|Allocate a pseudo-tty|`docker run -t imageName cmdToExecute`|
<br>
<br>


## docker-compose.yml cheatsheet
|Command|Description|Example|
|--|--|--|
|`image`|Define base image|`image: my_image`|
|`build`|Build image from file|`build: dockerfile_directory`|
|`ports`|Expose ports|`ports:`<br/>&nbsp;&nbsp;`- "8000:8000"`|
|`environment`|Environment variables|`environment:`<br/>&nbsp;&nbsp;`- env_var_name=value`|
|`entrypoint`|Default executable when running container|`entrypoint: my_entrypoint`|
|`command`|Command passed to entrypoint|`command: ["bundle", "param1"]`|
|`volumes`|Mount volumes between host and container|`volumes:`<br/>&nbsp;&nbsp;`- host_path:container_path`|
|`networks`|Set networks for service|`networks:`<br/>&nbsp;&nbsp;`- my_network`|
|`restart`|Restart service option|`restart: unless-stopped`|
|`depends_on`|Create a dependency|`depends_on: other_service_name`|
