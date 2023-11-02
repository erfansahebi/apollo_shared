from marshmallow import Schema as BaseSchema, ValidationError
from apollo_shared import exception


class Schema(BaseSchema):

    def load(
            self,
            *args,
            **kwargs,
    ):
        try:
            return super(Schema, self).load(*args, **kwargs)
        except ValidationError as err:
            raise exception.ValidationError('Invalid Data', err.messages)

    def validate(
            self,
            *args,
            **kwargs,
    ) -> dict[str, list[str]]:
        try:
            return super(Schema, self).validate(*args, **kwargs)
        except ValidationError as err:
            raise exception.ValidationError('Invalid Data', err.messages)
