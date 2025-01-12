## Installation Guide on Apache superset

Superset is not officially supported on Windows unfortunately. One option for Windows users to try out Superset locally is to install an Ubuntu Desktop VM via VirtualBox and proceed with the Docker on Linux instructions inside of that VM. We recommend assigning at least 8GB of RAM to the virtual machine as well as provisioning a hard drive of at least 40GB, so that there will be enough space for both the OS and all of the required dependencies. Docker Desktop recently added support for Windows Subsystem for Linux (WSL) 2, which may be another option.

### Clone the repository 

```
    git clone https://github.com/apache/superset.git
```
Once that command completes successfully, you should see a new superset folder in your current directory.

### Launch the superset through docker compose 

Navigate to the folder you created in step 1:
```
    cd superset
    docker compose up
```
When working on master branch, run the following commands to run production mode using docker compose:
```
    docker compose -f docker-compose-non-dev.yml pull
    docker compose -f docker-compose-non-dev.yml up
```
Alternatively, you can also run a specific version of Superset by first checking out the branch/tag, and then starting docker compose with the TAG variable. For example, to run the 3.0.0 version, run the following commands on Linux-based systems:
```
    git checkout 3.0.0
    TAG=3.0.0 docker compose -f docker-compose-non-dev.yml pull
    TAG=3.0.0 docker compose -f docker-compose-non-dev.yml up
```
If you are using Docker Desktop for Windows then run the following commands:
```
    git checkout 3.0.0
    set TAG=3.0.0
    docker compose -f docker-compose-non-dev.yml pull
    docker compose -f docker-compose-non-dev.yml up 
```

### Log into Superset

Your local Superset instance also includes a Postgres server to store your data and is already pre-loaded with some example datasets that ship with Superset. You can access Superset now via your web browser by visiting http://localhost:8088. Note that many browsers now default to https - if yours is one of them, please make sure it uses http.

Log in with the default username and password:
```
    username: admin
    password: admin
```

### Connecting superset to your local database instance:

When running Superset using Docker or Docker Compose, it operates within its own container, isolated from your host machine. This setup means that attempts to connect to your local database using the hostname "localhost" won't succeed because "localhost" refers to the Docker container Superset is running in, not your actual host machine. However, Docker provides a solution to access network resources on the host machine from within a container, enabling connectivity to your local database instance.

To connect to PostgreSQL (running on your host machine) from Superset (running in its Docker container), you need to follow these steps:

1. *Configure PostgreSQL to Accept Public Incoming Connections*: By default, PostgreSQL only allows incoming connections from localhost. Under Docker, unless you're using --network=host, "localhost" refers to different endpoints on the host machine and within a Docker container. To allow PostgreSQL to accept connections from Docker, you need to make changes to two files: postgresql.conf and pg_hba.conf. You can find instructions tailored to your operating system and PostgreSQL version online. For Docker, it's sufficient to whitelist IPs 172.0.0.0/8 instead of *. Note that making these changes in a production database may have security risks as it opens your database to the public internet.

2. *Use the Correct Hostname to Connect to the Database*: Instead of using "localhost," you should use the following hostnames - *For Mac users and Ubuntu*: host.docker.internal. *For Linux users*: 172.18.0.1
These hostnames are Docker internal details. Docker Desktop creates a DNS entry for host.docker.internal, resolving it to the correct address for the host machine on Mac systems. However, this is not the case for Linux by default. If neither of these hostnames works, you can find the exact hostname by using ifconfig or ip addr show to check the IP address of the docker0 interface created by Docker. Alternatively, you can run docker network inspect bridge (possibly with sudo) to find the "Gateway" entry and note the IP address.

By following these steps, you can successfully connect Superset running in a Docker container to your local PostgreSQL database.