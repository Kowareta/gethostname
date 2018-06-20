# Instructions copied from - https://hub.docker.com/_/python/
FROM python:3-onbuild
# Introducing the creator of the file
MAINTAINER Kowareta
# No buffer
ENV PYTHONUNBUFFERED 1
#Add script to container
ADD gethostname.py /
# Poining at the port number the container should expose
EXPOSE 80/tcp

# run the command
CMD ["python", "./gethostname.py"]