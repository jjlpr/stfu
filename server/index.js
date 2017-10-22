const express = require('express')
const app = express()
const WebSocket = require('ws');
const fs = require('fs');
const readLastLines = require('read-last-lines');

const filePath = '../output.json';
let lastTimeStamp = 0;


// websoket
const wss = new WebSocket.Server({ port: 8080 });
wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data);
    }
  });
};
wss.on('connection', function connection(ws) {
  console.log('new websocket connection')
});
fs.watchFile(filePath, {interval: 100}, ()=>{
  readLastLines.read(filePath, 1).then( line => {
    const parsedLine = JSON.parse(line);
    if( parsedLine && parsedLine.time ) {
      lastTimeStamp = parsedLine.time;
    }
    console.log( parsedLine );
    wss.broadcast( line )
  })
})

// express
app.get('/', function (req, res) {
  getData(req.query.start, req.query.end)
    .then( r => res.send(r) )
})
app.listen(8000, ()=>{console.log('new express')})


function getData(start, end) {

  // lines is number of seconds from the last timestamp.
  // we get these lines form the bottom of the input file
  // then filter out any that are not in range
  const lines = Math.max(0, Math.floor( (lastTimeStamp - start) / 1000 ));
  return new Promise( resolve => {
    readLastLines.read(filePath, lines).then( lines=> {


      const rtn = lines.split("\n").filter( line => {
        try {
          const parsedLine = JSON.parse(line);
          if( parsedLine.time && parsedLine.time >= start && parsedLine.time <= end ) {
            return true
          }
        } catch(e) {
          return false;
        }
        return false;
      }).join(',');
      resolve(`[${rtn}]`);
    })
  });
}
