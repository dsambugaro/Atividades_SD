
const net = require('net')
const hostname = '127.0.0.1'
const port = 5000
const server = net.createServer()
const message = require('./protobuf_model_pb');

const db = require('./database')

server.on('close', () => {
    console.log('Server closed')
})

server.on('connection', (socket) => {
    console.log('New client connection from ' + socket.remoteAddress + ':' + socket.remotePort)

    socket.on('data', (data) => {
        let request = message.Request.deserializeBinary(data)
        if (request.getAction() === 3) {
            db.list_students(request.getCourseCode(),
                request.getAcademicSemester(),
                request.getAcademicYear(), (error, result) => {
                    if (error) {
                        console.log(error);
                    } else {
                        console.log(result);
                    }
                })
        }
        
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