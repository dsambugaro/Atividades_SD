
const net = require('net')
const hostname = '127.0.0.1'
const port = 5000
const server = net.createServer()

const db = require('./database')

db.list_students()

server.on('close', () => {
    console.log('Server closed')
})

server.on('connection', (socket) => {
    socket.setEncoding('utf8')
    console.log('New client connection from ' + socket.remoteAddress + ':' + socket.remotePort)

    socket.on('data', (data) => {
        console.log('Data sent to server : ' + data)
    })

    socket.on('error', (error) => {
        console.log('Socket Error : ' + error)
    })

    socket.on('close', (error) => {
        console.log('Socket closed!')
        if (error) {
            console.log('Socket was closed because of transmission error')
        }
    })
})

server.on('error', (error) => {
    console.log('Server Error: ' + error)
})

server.on('listening', () => {
    console.log('Server is listening!')
})

server.listen(port, hostname)