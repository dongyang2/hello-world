class CustomError(Exception):

    def __init__(self, info):
        self.error_info = info

