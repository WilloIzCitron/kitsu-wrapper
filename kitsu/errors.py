class KitsuError(Exception):
    pass


class InvalidType(KitsuError):
    pass


class ResponseError(KitsuError):
    pass
