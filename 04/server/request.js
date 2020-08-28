class Request {
    constructor(action, target, academic_code,
        course_code, academic_year, academic_semester,
        value) {
        
        this.action = action
        this.target = target
        this.academic_code = academic_code
        this.course_code = course_code
        this.academic_year = academic_year
        this.academic_semester = academic_semester
        this.value = value
    }

    get_action = () => {
        return this.action
    }

    set_action = (value) => {
        this.action = value
    }

    get_target = () => {
        return this.target
    }

    set_target = (value) => {
        this.target = value
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
    
    get_value = () => {
        return this.value
    }

    set_value = (value) => {
        this.value = value
    }
    
    get_absences = () => {
        return this.absences
    }

    set_absences = (value) => {
        this.absences = value
    }

}