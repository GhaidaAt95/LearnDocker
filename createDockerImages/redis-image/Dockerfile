# Specify a base image ( Use an existing image as a base)
FROM alpine
 
# Download and install a dependency
RUN apk add --update gcc
RUN apk add --update redis

# Specify what the start up command is 
CMD ["redis-server"]