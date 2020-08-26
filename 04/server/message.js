class Message {
    constructor(msg_type, action, academics_codes,
        course_code, academic_year, academic_semester,
        grade, absences) {
        
        this.msg_type = msg_type
        this.action = action
        this.academics_codes = academics_codes
        this.course_code = course_code
        this.academic_year = academic_year
        this.academic_semester = academic_semester
        this.grade = grade
        this.absences = absences
    }

    get_msg_type = () => {
        return this.msg_type
    }

    set_msg_type = (value) => {
        this.msg_type = value
    }

    get_action = () => {
        return this.action
    }

    set_action = (value) => {
        this.action = value
    }
    
    get_academics_codes = () => {
        return this.academics_codes
    }

    set_academics_codes = (value) => {
        this.academics_codes = value
    }
    
    get_course_code = () => {
        return this.course_code
    }

    set_course_code = (value) => {
        this.course_code = value
    }
    
    get_academic_year = () => {
        return this.academic_year
    }

    set_academic_year = (value) => {
        this.academic_year = value
    }
    
    get_academic_semester = () => {
        return this.academic_semester
    }

    set_academic_semester = (value) => {
        this.academic_semester = value
    }
    
    get_grade = () => {
        return this.grade
    }

    set_grade = (value) => {
        this.grade = value
    }
    
    get_absences = () => {
        return this.absences
    }

    set_absences = (value) => {
        this.absences = value
    }

}