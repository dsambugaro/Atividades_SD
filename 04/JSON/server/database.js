const sql = require('sqlite3')

// Connects to the database
const connect_db = () => {
    let db = new sql.Database('./gerenciamento_notas.db', (err) => {
        if (err) {
            console.error(error.message)
        }
        console.log('Connected to the database')
    })
    return db
}

// Closes connection to the database
const close_db = (db) => {
    db.close((error) => {
        if (error) {
            return console.error(error.message)
        }
        console.log('Close the database connection.')
    })
}

// List all students of course at semester/year
exports.list_students = (course_code, semester, year, callback) => {
    let db = connect_db()
    let sqlquery = "SELECT ra, nome from aluno WHERE ra IN (SELECT ra_aluno FROM matricula WHERE cod_disciplina = ? AND semestre = ? AND ano = ?)"
    let filter = [course_code, semester, year]
    let students = []

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
    let sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina =  AND ra_aluno = "
    let filter = [grade, year, semester, course_code, student_id]

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