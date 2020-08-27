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
    let sqlquery = "SELECT ra_aluno FROM matricula WHERE cod_disciplina = ? AND semestre = ? AND ano = ?";
    let filter = [course_code, semester, year];

    db.query(sqlquery, filter, function(error, results) {
        if (error) {
          return console.error(err.message);
        }
        console.log(results);
      });

    close_db(db);
}

exports.set_student_grade = (course_code, semester, year, student_id, grade) => {
    let db = connect_db();
    let sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?";
    let filter = [grade, year, semester, course_code, student_id];

    db.query(sqlquery, filter, function(error, results) {
        if (error) {
          return console.error(err.message);
        }
        console.log(results);
      });

    close_db(db);
}

exports.remove_student_grade = (course_code, semester, year, student_id) => {
    let db = connect_db();
    var grade = 0;
    let sqlquery = "UPDATE matricula SET nota = ? WHERE ano = ? AND semestre = ? AND cod_disciplina =  AND ra_aluno = ";
    let filter = [grade, year, semester, course_code, student_id];

    db.query(sqlquery, filter, function(error, results) {
        if (error) {
          return console.error(err.message);
        }
        console.log(results);
      });

    close_db(db);
}

exports.set_student_absences = (course_code, semester, year, student_id, absences) => {
    let db = connect_db();
    let sqlquery = "UPDATE matricula SET faltas = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?";
    let filter = [absences, year, semester, course_code, student_id];

    db.query(sqlquery, filter, function(error, results) {
        if (error) {
          return console.error(err.message);
        }
        console.log(results);
      });
      
    close_db(db);
}

exports.remove_student_absences = (course_code, semester, year, student_id) => {
    let db = connect_db();
    var absences = 0;
    let sqlquery = "UPDATE matricula SET faltas = ? WHERE ano = ? AND semestre = ? AND cod_disciplina = ? AND ra_aluno = ?";
    let filter = [absences, year, semester, course_code, student_id];

    db.query(sqlquery, filter, function(error, results) {
        if (error) {
          return console.error(err.message);
        }
        console.log(results);
      });

    close_db(db);
}