class Request {
    constructor(action, academic_code,
        course_code, academic_year, academic_semester,
        grade, absences) {
        
        this.action = action
        this.academic_code = academic_code
        this.course_code = course_code
        this.academic_year = academic_year
        this.academic_semester = academic_semester
        this.grade = grade
        this.absences = absences
    }

    get_action = () => {
        return this.action
    }

    set_action = (value) => {
        this.action = value
    }
    
    get_acadmic_code = () => {
        return this.academic_code
    }

    set_acadmic_code = (value) => {
        this.academic_code = value
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