from nameko.exceptions import deserialize_to_instance


class ApolloException(Exception):
    status_code: int = 500

    def __init__(self, message: str, **kwargs):
        self.message = message
        self.kwargs = kwargs
        super(ApolloException, self).__init__(message, *kwargs.values())


@deserialize_to_instance
class BadRequest(ApolloException):
    status_code = 400


@deserialize_to_instance
class ValidationError(ApolloException):
    status_code = 400


@deserialize_to_instance
class Unauthorized(ApolloException):
    status_code = 401


@deserialize_to_instance
class Forbidden(ApolloException):
    status_code = 403


@deserialize_to_instance
class NotFound(ApolloException):
    status_code = 404


@deserialize_to_instance
class TooManyRequest(ApolloException):
    status_code = 429


@deserialize_to_instance
class InternalError(ApolloException):
    status_code = 500
