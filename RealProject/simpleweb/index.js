const express = require('express');

// create a new app
const app = express();

app.get('/',(req, res)=> {
    res.send('Hi Bash');
});

app.listen(8080, ()=> {
    console.log("listening on port 8080");
});