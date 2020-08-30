
const net = require('net')
const hostname = '127.0.0.1'
const port = 5000
const server = net.createServer()
const message = require('./protobuf_model_pb')

const db = require('./database')

// Create a response with error code and message
const newResponseError = (status, code, error_message) => {
    response = new message.Response()
    response.setStatus(status)
    response.setErrorCode(code)
    response.setErrorMessage(error_message)
    response_bytes = response.serializeBinary()
    return response_bytes
}

// Create a response without error code and message
const newResponseSuccess = (status) => {
    response = new message.Response()
    response.setStatus(status)
    response.setErrorCode(0)
    response.setErrorMessage('')
    response_bytes = response.serializeBinary()
    return response_bytes
}

// Check and validade resquest
const validateRequest = (request) => {
    hasAction = request.getAction() ? true : false
    hasTarget = request.getTarget() ? true : false
    hasAcademicCode = request.getAcademicCode() ? true : false
    hasCourseCode = request.getCourseCode() ? true : false
    hasAcademicYear = request.getAcademicYear() ? true : false
    hasAcademicSemester = request.getAcademicSemester() ? true : false
    hasValue = request.getValue() ? true : false

    if (!hasAction || !hasTarget) {
        // If no action or target, request is invalid
        return false
    } else {
        if (request.getAction() === 3) {
            // if request action are 3, request must have this fields
            return hasAcademicYear && hasAcademicSemester && hasCourseCode
        } else if (request.getAction() === 1) {
            // if request action are 1, request must have this fields
            return hasAcademicYear && hasAcademicSemester && hasCourseCode && hasAcademicCode && hasValue
        } else if (request.getAction() === 2) {
            // if request action are 2, request must have this fields
            return hasAcademicYear && hasAcademicSemester && hasCourseCode && hasAcademicCode
        }
    }

}

server.on('close', () => {
    // Called on server close event
    console.log('Server closed')
})

server.on('connection', (socket) => {
    // Called on new connection to server
    console.log('New client connection from ' + socket.remoteAddress + ':' + socket.remotePort)

    socket.on('data', (data) => {
        // Called on data received on server
        let request = message.Request.deserializeBinary(data)
        if (validateRequest(request)) { // Verify request
            // Call methods according to request and send appropriately response
            if (request.getAction() === 3) {
                db.list_students(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), (error, result) => {
                        if (error) {
                            socket.write(newResponseError(500, 500, error))
                        } else {
                            response = new message.Response()
                            response.setStatus(200)
                            for (let i = 0; i < result.length; i++) {
                                const element = result[i]
                                response.addAcademicCode(element.ra)
                                response.addAcademicName(element.nome)
                            }
                            response_bytes = response.serializeBinary()
                            socket.write(response_bytes)
                        }
                    })
            } else if (request.getAction() === 1) {
                if (request.getTarget() === 'grade') {
                    db.set_student_grade(request.getCourseCode(),
                        request.getAcademicSemester(),
                        request.getAcademicYear(), request.getAcademicCode(),
                        Number((request.getValue()).toFixed(1)), (error, _result) => {
                            if (error) {
                                socket.write(newResponseError(500, 500, error))
                            } else {
                                socket.write(newResponseSuccess(200))
                            }
                        })
                } else if (request.getTarget() === 'absences') {
                    db.set_student_absences(request.getCourseCode(),
                        request.getAcademicSemester(),
                        request.getAcademicYear(), request.getAcademicCode(),
                        Math.trunc(request.getValue()), (error, _result) => {
                            if (error) {
                                socket.write(newResponseError(500, 500, error))
                            } else {
                                socket.write(newResponseSuccess(200))
                            }
                        })
                }
            } else if (request.getAction() === 2) {
                if (request.getTarget() === 'grade') {
                    db.remove_student_grade(request.getCourseCode(),
                        request.getAcademicSemester(),
                        request.getAcademicYear(), request.getAcademicCode(),
                        (error, _result) => {
                            if (error) {
                                socket.write(newResponseError(500, 500, error))
                            } else {
                                socket.write(newResponseSuccess(200))
                            }
                        })
                } else if (request.getTarget() === 'absences') {
                    db.remove_student_absences(request.getCourseCode(),
                        request.getAcademicSemester(),
                        request.getAcademicYear(), request.getAcademicCode(),
                        (error, _result) => {
                            if (error) {
                                socket.write(newResponseError(500, 500, error))
                            } else {
                                socket.write(newResponseSuccess(200))
                            }
                        })
                }
            } else {
                socket.write(newResponseError(400, 400, 'Ação inválida'))
            }
        } else {
            // Send error if request was invalids
            socket.write(newResponseError(400, 400, 'Requisição incorreta - Verifique os dados enviados'))
        }

    })

    socket.on('error', (error) => {
        // Called on socket error
        console.log('Socket Error : ' + error)
    })

    socket.on('close', (error) => {
        // Called when socket closes
        console.log('Socket closed!')
        if (error) {
            console.log('Socket was closed because of transmission error')
        }
    })
})

server.on('error', (error) => {
    // Called on server error
    console.log('Server Error: ' + error)
})

server.on('listening', () => {
    // Called when server starts listening
    console.log('Server is listening!')
})

// Start server listening
server.listen(port, hostname)