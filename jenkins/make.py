"""
v0.0.1
2022.02.07
"""
import subprocess, os

DOCKER_GROUP_ID = subprocess.check_output("getent group docker", shell=True, text=True)

SERVICE = "jenkins"

os.putenv('DOCKER_GROUP_ID', DOCKER_GROUP_ID)

subprocess.run("docker-compose up --build -d", shell=True)
