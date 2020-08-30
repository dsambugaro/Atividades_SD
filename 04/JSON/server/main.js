
const net = require('net')
const hostname = '127.0.0.1'
const port = 5000
const server = net.createServer()

const db = require('./database')

// Create a response with error code and message
const newResponseError = (status, code, error_message) => {
    response = {
        status: status,
        error_code: code,
        error_message: error_message
    }
    response_bytes = JSON.stringify(response)
    return response_bytes
}

// Create a response without error code and message
const newResponseSuccess = (status) => {
    response = {
        status: status,
        error_code: 0,
        error_message: ''
    }
    response_bytes = JSON.stringify(response)
    return response_bytes
}

// Check and validade resquest
const validateRequest = (request) => {
    hasAction = request.action ? true : false
    hasTarget = request.target ? true : false
    hasAcademicCode = request.academic_code ? true : false
    hasCourseCode = request.course_code ? true : false
    hasAcademicYear = request.academic_year ? true : false
    hasAcademicSemester = request.academic_semester ? true : false
    hasValue = request.value ? true : false

    if (!hasAction || !hasTarget) {
        // If no action or target, request is invalid
        return false
    } else {
        if (request.action === 3) {
            // if request action are 3, request must have this fields
            return hasAcademicYear && hasAcademicSemester && hasCourseCode
        } else if (request.action === 1) {
            // if request action are 1, request must have this fields
            return hasAcademicYear && hasAcademicSemester && hasCourseCode && hasAcademicCode && hasValue
        } else if (request.action === 2) {
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
        request = JSON.parse(data)
        if (validateRequest(request)) { // Verify request
            // Call methods according to request and send appropriately response
            if (request.action === 3) {
                db.get_course(request.course_code, (error, result) => {
                    if (error) {
                        socket.write(newResponseError(500, 500, error))
                    } else if (result.length) {
                        db.list_students(request.course_code,
                            request.academic_semester,
                            request.academic_year, (error, result) => {
                                if (error) {
                                    socket.write(newResponseError(500, 500, error))
                                } else {
                                    response = {
                                        status: 200,
                                        error_code: 0,
                                        error_message: '',
                                        data: result
                                        
                                    }
                                    response_bytes = JSON.stringify(response)
                                    socket.write(response_bytes)
                                }
                            })
                    } else {
                        socket.write(newResponseError(404, 404, "Disciplina " + request.course_code + " não encontrada"))
                    }
                })
            } else if (request.action === 1) {
                if (request.target === 'grade') {
                    db.get_course(request.course_code, (error, result) => {
                        if (error) {
                            socket.write(newResponseError(500, 500, error))
                        } else if (result.length) {
                            db.get_enrolle(request.course_code, request.academic_semester,
                                request.academic_year, request.academic_code, (error, result) => {
                                    if (error) {
                                        socket.write(newResponseError(500, 500, error))
                                    } else if (result.length) {
                                        db.set_student_grade(request.course_code,
                                            request.academic_semester,
                                            request.academic_year, request.academic_code,
                                            Number((request.value).toFixed(1)), (error, _result) => {
                                                if (error) {
                                                    socket.write(newResponseError(500, 500, error))
                                                } else {
                                                    socket.write(newResponseSuccess(200))
                                                }
                                            })
                                    } else {
                                        socket.write(newResponseError(404, 404, "Matrícula do aluno não encontrada"))
                                    }
                                })
                        } else {
                            socket.write(newResponseError(404, 404, "Disciplina " + request.course_code + " não encontrada"))
                        }
                    })
                } else if (request.target === 'absences') {
                    db.get_course(request.course_code, (error, result) => {
                        if (error) {
                            socket.write(newResponseError(500, 500, error))
                        } else if (result.length) {
                            db.get_enrolle(request.course_code, request.academic_semester,
                                request.academic_year, request.academic_code, (error, result) => {
                                    if (error) {
                                        socket.write(newResponseError(500, 500, error))
                                    } else if (result.length) {
                                        db.set_student_absences(request.course_code,
                                            request.academic_semester,
                                            request.academic_year, request.academic_code,
                                            Math.trunc(request.value), (error, _result) => {
                                                if (error) {
                                                    socket.write(newResponseError(500, 500, error))
                                                } else {
                                                    socket.write(newResponseSuccess(200))
                                                }
                                            })
                                    } else {
                                        socket.write(newResponseError(404, 404, "Matrícula do aluno não encontrada"))
                                    }
                                })
                        } else {
                            socket.write(newResponseError(404, 404, "Disciplina " + request.course_code + " não encontrada"))
                        }
                    })
                }
            } else if (request.action === 2) {
                if (request.target === 'grade') {
                    db.get_course(request.course_code, (error, result) => {
                        if (error) {
                            socket.write(newResponseError(500, 500, error))
                        } else if (result.length) {
                            db.get_enrolle(request.course_code, request.academic_semester,
                                request.academic_year, request.academic_code, (error, result) => {
                                    if (error) {
                                        socket.write(newResponseError(500, 500, error))
                                    } else if (result.length) {
                                        db.remove_student_grade(request.course_code,
                                            request.academic_semester,
                                            request.academic_year, request.academic_code,
                                            (error, _result) => {
                                                if (error) {
                                                    socket.write(newResponseError(500, 500, error))
                                                } else {
                                                    socket.write(newResponseSuccess(200))
                                                }
                                            })
                                    } else {
                                        socket.write(newResponseError(404, 404, "Matrícula do aluno não encontrada"))
                                    }
                                })
                        } else {
                            socket.write(newResponseError(404, 404, "Disciplina " + request.course_code + " não encontrada"))
                        }
                    })
                } else if (request.target === 'absences') {
                    db.get_course(request.course_code, (error, result) => {
                        if (error) {
                            socket.write(newResponseError(500, 500, error))
                        } else if (result.length) {
                            db.get_enrolle(request.course_code, request.academic_semester,
                                request.academic_year, request.academic_code, (error, result) => {
                                    if (error) {
                                        socket.write(newResponseError(500, 500, error))
                                    } else if (result.length) {
                                        db.remove_student_absences(request.course_code,
                                            request.academic_semester,
                                            request.academic_year, request.academic_code,
                                            (error, _result) => {
                                                if (error) {
                                                    socket.write(newResponseError(500, 500, error))
                                                } else {
                                                    socket.write(newResponseSuccess(200))
                                                }
                                            })
                                    } else {
                                        socket.write(newResponseError(404, 404, "Matrícula do aluno não encontrada"))
                                    }
                                })
                        } else {
                            socket.write(newResponseError(404, 404, "Disciplina " + request.course_code + " não encontrada"))
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