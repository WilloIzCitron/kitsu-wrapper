class KitsuError(Exception):
    pass


class InvalidArgument(KitsuError):
    pass


class ResponseError(KitsuError):
    pass
