#Specify base image
FROM node:11-alpine
# Install dependincies 
WORKDIR /usr/app
COPY ./package.json ./ 
RUN npm install

COPY ./ ./

# Default / startup commands
CMD ["npm","start"]