# neo4j-python-example
## Install Neo4J on Ubuntu

```
% cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Ubuntu 18.04.2 LTS"
```

### Installing Java

```
% sudo apt install default-jre
% java -version
openjdk version "11.0.3" 2019-04-16
OpenJDK Runtime Environment (build 11.0.3+7-Ubuntu-1ubuntu218.04.1)
OpenJDK 64-Bit Server VM (build 11.0.3+7-Ubuntu-1ubuntu218.04.1, mixed mode, sharing)
```

### Installing Neo4j

http://debian.neo4j.org/

```
% wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
% echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee /etc/apt/sources.list.d/neo4j.list
% sudo apt-get update
% sudo apt-get install neo4j
```

```
% sudo systemctl start neo4j
% sudo systemctl status neo4j
```

http://localhost:7474/

## Neo4j Bolt Driver for Python

https://github.com/neo4j/neo4j-python-driver

```
% pip install neo4j
```
