from abc import ABC, abstractmethod
from apollo_shared.schema import auth as auth_schema


class AuthRPC(ABC):
    name = 'auth'

    @abstractmethod
    def register(self, data: auth_schema.RegisterSchemaRPC) -> auth_schema.RegisterSchemaRPCResponse:
        pass

    @abstractmethod
    def login(self, data: auth_schema.LoginSchemaRPC) -> auth_schema.LoginSchemaRPCResponse:
        pass

    @abstractmethod
    def logout(self, data: auth_schema.LogoutRPC) -> None:
        pass

    @abstractmethod
    def authenticate(self, data: auth_schema.AuthenticateRPC) -> auth_schema.AuthenticateRPCResponse:
        pass
