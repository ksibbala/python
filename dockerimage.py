# import docker
# client = docker.from_env()
# image_name = "nginx"
# tag = "latest"
# image = client.api.pull(image_name, tag)
# print("Image pulled successfully")
# container = client.containers.run(f"{image_name}:{tag}", detach=True, ports={'80/tcp':'8080'})
# print(client.containers.list())

import docker
import os
client = docker.from_env()

hub_username = 'ksibbala04' 
hub_password = os.getenv('DOCKERHUB_PASSWORD') #getting password from env
image_name = 'ksibbala04/frontend'
tag = 'v1'

#docker hub login 
client.login(username=hub_username, password=hub_password)
print(f"Login Successful")

#pulling image from docker hub
client.images.pull(f"{image_name}:{tag}")
print(f"Image {image_name}:{tag} pulled successfully")

#running containers from images
container = client.containers.run(
    f"{image_name}:{tag}",
    detach=True,
    ports={'80/tcp': 8089}  
)
print(f"Container :{container.id} is running")
print(client.containers.list())

# stopping containers
container.stop()
#removing conatiners
container.remove()

#removing images
client.images.remove(f"{image_name}:{tag}", force=True)
print("No running containers or images left.")


