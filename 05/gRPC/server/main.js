const grpc = require('grpc')
const services = require('./gRPC_model_grpc_pb.js')
const message = require('./gRPC_model_pb')
const utils = require('./utils')
const server = new grpc.Server()

const db = require('./database')

server.addService(services.GradeService, {
    create: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.set_student_grade(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    Number((request.getGrade()).toFixed(1)), (error, _result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            callback(null, utils.newResponseSuccess(201))
                        }
                    }
                )

            }
        })
    },
    read: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.get_student_grade(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    (error, result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            // Create new response message
                            response = new message.Response()
                            response.setStatus(200)
                            response.setErrorCode(0)
                            response.setErrorMessage('')
                            for (let index = 0; index < result.length; index++) {
                                const element = result[index]
                                response.addGrade(element.nota)
                            }
                            callback(null, response) // Send response to client
                        }
                    }
                )

            }
        })
    },
    update: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.set_student_grade(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    Number((request.getGrade()).toFixed(1)), (error, _result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            callback(null, utils.newResponseSuccess(200)) // Send response to client
                        }
                    }
                )

            }
        })
    },
    delete: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.remove_student_grade(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    (error, _result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            callback(null, utils.newResponseSuccess(200)) // Send response to client
                        }
                    }
                )
            }
        })
    }
})

server.addService(services.AbsencesService, {
    create: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.set_student_absences(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    request.getAbsences(), (error, _result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            callback(null, utils.newResponseSuccess(201))
                        }
                    }
                )

            }
        })
    },
    read: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.get_student_absences(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    (error, result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            // Create new response message
                            response = new message.Response()
                            response.setStatus(200)
                            response.setErrorCode(0)
                            response.setErrorMessage('')
                            for (let index = 0; index < result.length; index++) {
                                const element = result[index]
                                response.addAbsences(element.faltas)
                            }
                            callback(null, response) // Send response to client
                        }
                    }
                )

            }
        })
    },
    update: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.set_student_absences(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    request.getAbsences(), (error, _result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            callback(null, utils.newResponseSuccess(200)) // Send response to client
                        }
                    }
                )

            }
        })
    },
    delete: (data, callback) => {
        let request = data.request
        utils.validadeCourseAndEnrolle(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.remove_student_absences(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(), request.getAcademicCode(),
                    (error, _result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            callback(null, utils.newResponseSuccess(200)) // Send response to client
                        }
                    }
                )
            }
        })
    }
})

server.addService(services.CourseService, {
    gradesAndAbsences: (data, callback) => {
        let request = data.request
        utils.validadeCourse(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.get_grades_absences(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(),
                    (error, result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            // Create new response message
                            response = new message.Response()
                            response.setStatus(200)
                            response.setErrorCode(0)
                            response.setErrorMessage('')
                            for (let index = 0; index < result.length; index++) {
                                const element = result[index]
                                response.addAcademicCode(element.ra_aluno)
                                response.addAbsences(element.faltas)
                                response.addGrade(element.nota)
                            }
                            callback(null, response) // Send response to client
                        }
                    }
                )

            }
        })
    },
    students: (data, callback) => {
        let request = data.request
        utils.validadeCourse(request, db, (error) => {
            if (error) {
                callback(null, utils.newResponseError(400, error.code, error.msg)) // Send error to client
            } else {
                db.list_students(request.getCourseCode(),
                    request.getAcademicSemester(),
                    request.getAcademicYear(),
                    (error, result) => {
                        if (error) {
                            callback(null, utils.newResponseError(500, 500, 'Falha no banco de dados')) // Send error to client
                        } else {
                            // Create new response message
                            response = new message.Response()
                            response.setStatus(200)
                            response.setErrorCode(0)
                            response.setErrorMessage('')
                            for (let index = 0; index < result.length; index++) {
                                const element = result[index]
                                response.addAcademicCode(element.ra)
                                response.addAcademicName(element.nome)
                            }
                            callback(null, response) // Send response to client
                        }
                    }
                )

            }
        })
    }
})

server.bind('127.0.0.1:5000', grpc.ServerCredentials.createInsecure())
console.log('Server running at http://127.0.0.1:5000')
server.start()