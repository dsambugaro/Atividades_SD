const sql = require('sqlite3')

// Connects to the database
const connect_db = () => {
    let db = new sql.Database('./gerenciamento_notas.db', (err) => {
        if (err) {
            console.error(error.message)
        }
    })
    return db
}

// Closes connection to the database
const close_db = (db) => {
    db.close((error) => {
        if (error) {
            return console.error(error.message)
        }
    })
}

// Get a course by his code
exports.get_course = (course_code, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT * FROM disciplina WHERE codigo = ?"
    let filter = [course_code]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Get a enrolle by course, semester, year and student id
exports.get_enrolle = (course_code, semester, year, student_id, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT * FROM matricula WHERE ano = ? AND semestre = ? and cod_disciplina = ? and ra_aluno = ?"
    let filter = [year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// List all students of course at semester/year
exports.list_students = (course_code, semester, year, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT ra, nome from aluno WHERE ra IN (SELECT ra_aluno FROM matricula WHERE cod_disciplina = ? AND semestre = ? AND ano = ?)"
    let filter = [course_code, semester, year]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Get a students grade and absences
exports.get_grades_absences = (course_code, semester, year, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT ra_aluno, nota, faltas FROM matricula WHERE ano = ? AND semestre = ? AND cod_disciplina = ?"
    let filter = [year, semester, course_code]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Get a student grade
exports.get_student_grade = (course_code, semester, year, student_id, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT nota FROM matricula WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
    let filter = [year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Set a student grade to value received
exports.set_student_grade = (course_code, semester, year, student_id, grade, callback) => {
    let db = connect_db()
    let sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
    let filter = [grade, year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Set a student grade to 0
exports.remove_student_grade = (course_code, semester, year, student_id, callback) => {
    let db = connect_db()
    let grade = 0
    let sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
    let filter = [grade, year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Get a student absences
exports.get_student_absences = (course_code, semester, year, student_id, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT faltas FROM matricula WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
    let filter = [year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Set a student absences to value received
exports.set_student_absences = (course_code, semester, year, student_id, absences, callback) => {
    let db = connect_db()
    let sqlquery = "UPDATE matricula SET faltas = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
    let filter = [absences, year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}

// Set a student absences to 0
exports.remove_student_absences = (course_code, semester, year, student_id, callback) => {
    let db = connect_db()
    let absences = 0
    let sqlquery = "UPDATE matricula SET faltas = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?"
    let filter = [absences, year, semester, course_code, student_id]

    db.all(sqlquery, filter, callback)

    close_db(db)
}