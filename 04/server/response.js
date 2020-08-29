class Response {
    constructor(status, data, errorMessage, errorCode) {
        this.status = status
        this.data = data
        this.errorCode = errorCode
        this.errorMessage = errorMessage
    }

    getStatus = () => {
        return this.status
    }

    setStatus = (value) => {
        this.status = value
    }

    getData = () => {
        return this.data
    }

    setData = (value) => {
        this.data = value
    }

    getErrorCode = () => {
        return this.errorCode
    }

    setErrorCode = (value) => {
        this.errorCode = value
    }

    getErrorMessage = () => {
        return this.errorMessage
    }

    setErrorMessage = (value) => {
        this.errorMessage = value
    }

}