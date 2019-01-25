const express = require('express');

const redis = require('redis');

const process = require('process');

const app = express();

const client = redis.createClient({
    // name of the serveice we created in the Docker compose
    host: 'redis-server',
    port: 6379
    // the port by default always used with redis
});

client.set('visits',0);

app.get('/',(req, res)=> {
    // Crash it to practice restarting
    process.exit(0);
    client.get('visits',(err, visits)=>{
        res.send('Number of visits is '+ visits);
        client.set('visits', parseInt(visits)+1);
    });
});

app.listen(8081, ()=>{
    console.log('listening on port 8081');
});