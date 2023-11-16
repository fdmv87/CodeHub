## Docker

List all images that are locally stored:

    docker images

Remove an image from the docker store:

    docker rmi temp-ubuntu:version-1.0

Rebuild a container image:

    docker build -t temp-ubuntu .

List the running containers:

    docker ps -a

Run container:

    docker run -d tmp-ubuntu

Pause container:

    docker pause <NAME>

Stop a container:

    docker stop <NAME>

Remove a container:

    docker rm <NAME>

After you remove the container, all data in the container is destroyed. It's essential to always consider containers as temporary when thinking about storing data.

Containers can make use of two options to persist data. The first option is to make use of volumes, and the second is bind mounts.

## volume
A volume is stored on the host filesystem at a specific folder location. Choose a folder where you know the data won't be modified by non-Docker processes.

Docker creates and manages the new volume by running the **docker volume create** command. This command can form part of our Dockerfile definition, which means that you can create volumes as part of the container-creation process. Docker will create the volume if it doesn't exist when you try to mount the volume into a container the first time.


## bind mount

A bind mount is conceptually the same as a volume; however, instead of using a specific folder, you can mount any file or folder on the host. You're also expecting that the host can change the contents of these mounts. Just like volumes, the bind mount is created if you mount it and it doesn't yet exist on the host.

Bind mounts have limited functionality compared to volumes, and even though they're more performant, they depend on the host having a specific folder structure in place.

###
Volumes are considered the preferred data-storage strategy to use with containers.

For Windows containers, another option is available: You can mount an SMB path as a volume and present it to containers. This allows containers on different hosts to use the same persistent storage.


## Dockerfile

| Instruction   | Description                                                                    |
| --------------| -------------------------------------------------------------------------------|	
| FROM          | The first instruction in the Dockerfile, it identifies an image to inherit from
| MAINTAINER	| This instruction provides visibility as well as credit to the author of the image
| RUN	        | This instruction executes a Linux command  to install and configure
| ENTRYPOINT	| The final script or application which is used to bootstrap the container and make it an executable application
| CMD	        | This instruction uses a JSON array to provide default arguments to the ENTRYPOINT
| LABEL	        | This instruction contains the name/value metadata about the image
| ENV	        | This instruction sets the environment variables
| COPY	        | This instruction copies files into the container
| ADD	        | This instruction is basically an alternative to the COPY instruction
| WORKDIR	    | This sets a working directory for RUN, CMD, ENTRYPOINT, COPY, and/or ADD instructions
| EXPOSE	    | The ports on which the container listens
| VOLUME	    | This instruction is to create a mount point
| USER	        | An instruction to run RUN, CMD, and/or ENTRYPOINT instructions