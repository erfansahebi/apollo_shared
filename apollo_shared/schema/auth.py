from marshmallow import fields
from .base import Schema


class _AuthenticateSchemaRPCResponse(Schema):
    user_id = fields.Str(required=True)
    token = fields.Str(required=True)


class RegisterSchemaRPC(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class RegisterSchemaRPCResponse(_AuthenticateSchemaRPCResponse):
    pass


class LoginSchemaRPC(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class LoginSchemaRPCResponse(_AuthenticateSchemaRPCResponse):
    pass


class LogoutRPC(Schema):
    token = fields.Str(required=True)


class AuthenticateRPC(Schema):
    token = fields.Str(required=True)


class AuthenticateRPCResponse(Schema):
    user_id = fields.Str(required=True)
