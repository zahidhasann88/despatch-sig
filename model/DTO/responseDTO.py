'''
# node.js code
class ResponseDto {
    message = 'Operation failed. Something went wrong. Please try again later';
    isSuccess = false;
    statusCode = 500;
    payload = null;
}

module.exports = ResponseDto;
'''


class ResponseDTO:
    message = "Operation Failed or Success."
    isSuccess = False
    statusCode = 500
    payload = None

    def __init__(self,message,isSuccess,statusCode,payload):
        self.message = message
        self.isSuccess = isSuccess
        self.statusCode = statusCode
        self.payload = payload

