class Response {
    constructor(status, data, error_message, error_code) {
        this.status = status
        this.data = data
        this.error_code = error_code
        this.error_message = error_message
    }

    get_status = () => {
        return this.status
    }

    set_status = (value) => {
        this.status = value
    }

    get_data = () => {
        return this.data
    }

    set_data = (value) => {
        this.data = value
    }

    get_error_code = () => {
        return this.error_code
    }

    set_error_code = (value) => {
        this.error_code = value
    }

    get_error_message = () => {
        return this.error_message
    }

    set_error_message = (value) => {
        this.error_message = value
    }

}