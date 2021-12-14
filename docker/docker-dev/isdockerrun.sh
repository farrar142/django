# Build N Run DB Container
# 2020. 09. 18 Zini
##
docker_username="farrar142"
web_image_name="docker-dev_web"
web_container_name="web"
version="1"
port=8000 # Default MySQL Port: 3306

echo "## Automation docker-database build and run ##"

# remove container
echo "=> Remove previous container..."
docker rm -f ${web_container_name}

# remove image
echo "=> Remove previous image..."
docker rmi -f ${docker_username}/${web_image_name}:${version}

# new-build/re-build docker image
echo "=> Build new image..."
docker build --tag ${docker_username}/${web_image_name}:${version} .

# Run container
echo "=> Run container..."
docker-compose up -d