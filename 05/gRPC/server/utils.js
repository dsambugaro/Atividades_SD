const message = require('./gRPC_model_pb')

exports.validadeCourse = (request, db, callback) => {
    db.get_course(request.getCourseCode(), (error, result) => {
        if (error) {
            callback({ code: 500, msg: error }, false)
        } else if (result.length) {
            callback(null)
        } else {
            callback({ code: 404, msg: "Disciplina " + request.getCourseCode() + " não encontrada" })
        }
    })
}

exports.validadeEnrolle = (request, db, callback) => {
    db.get_enrolle(request.getCourseCode(), request.getAcademicSemester(),
        request.getAcademicYear(), request.getAcademicCode(), (error, result) => {
            if (error) {
                callback({ code: 500, msg: error }, false)
            } else if (result.length) {
                callback(null)
            } else {
                callback({ code: 404, msg: "Matrícula do aluno não encontrada" }, false)
            }
        })
}

exports.validadeCourseAndEnrolle = (request, db, callback) => {
    this.validadeCourse(request, db, (error) => {
        if (error) {
            callback(error)
        } else {
            this.validadeEnrolle(request, db, callback)
        }
    })
}

exports.newResponseError = (status, code, error_message) => {
    response = new message.Response()
    response.setStatus(status)
    response.setErrorCode(code)
    response.setErrorMessage(error_message)
    return response
}

exports.newResponseSuccess = (status) => {
    response = new message.Response()
    response.setStatus(status)
    response.setErrorCode(0)
    response.setErrorMessage('')
    return response
}