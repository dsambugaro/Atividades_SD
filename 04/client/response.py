class Response:
    """Class representing a response"""

    status = None
    error_message = None
    error_code = None
    data = []

    def __init__(self, status=None, data=[], error_message=None, error_code=None):
        self.status = status
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
    
    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value
    
    def get_data(self):
        return self.data

    def set_data(self, value):
        self.data = value

    def get_error_code(self):
        return self.error_code

    def set_error_code(self, value):
        self.error_code = value
    
    def get_error_message(self):
        return self.error_message

    def set_error_message(self, value):
        self.error_message = value