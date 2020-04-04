class KitsuError(Exception):
    pass


class InvalidArgument(KitsuError):
    pass


class ResponseError(KitsuError):
    def __init__(self, *, code, reason):
        self.code = code
        self.reason = reason
