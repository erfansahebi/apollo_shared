import typing
from dataclasses import dataclass, asdict


@dataclass
class Context:
    request_id: typing.Optional[str] = None
    token: typing.Optional[str] = None
    user_id: typing.Optional[str] = None

    def dict(self):
        return {k: (str(v) if v is not None else None) for k, v in asdict(self).items()}
