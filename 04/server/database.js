const sql = require('sqlite3');

const connect_db = () => {
    let db = new sql.Database('./gerenciamento_notas.db', (err) => {
        if (err) {
            console.error(err.message);
        }
        console.log('Connected to the database');
    });
    return db
}

const close_db = (db) => {
    db.close((err) => {
        if (err) {
            return console.error(err.message);
        }
        console.log('Close the database connection.');
    });
}

exports.list_students = (course_code, semester, year) => {
    let db = connect_db();

    // TODO: SQL to list students at course

    close_db(db);
}

exports.set_student_grade = (course_code, semester, year, student_id, grade) => {
    let db = connect_db();

    // TODO: SQL to set student grade

    close_db(db);
}

exports.remove_student_grade = (course_code, semester, year, student_id) => {
    let db = connect_db();

    // TODO: SQL to remove student grade

    close_db(db);
}

exports.set_student_absences = (course_code, semester, year, student_id, absences) => {
    let db = connect_db();

    // TODO: SQL to set student absences

    close_db(db);
}

exports.remove_student_absences = (course_code, semester, year, student_id) => {
    let db = connect_db();

    // TODO: SQL to set student absences

    close_db(db);
}