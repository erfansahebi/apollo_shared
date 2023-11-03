from .base import Schema
from marshmallow import fields


class _RSSSchema(Schema):
    id = fields.Str(required=True)
    url = fields.Str(required=True)


class SubscribeRSSSchemaRPC(Schema):
    url = fields.Str(required=True)


class SubscribeRSSSchemaRPCResponse(_RSSSchema):
    pass


class GetRSSesSchemaRPC(Schema):
    pass


class GetRSSesSchemaRPCResponse(_RSSSchema):
    pass


class GetRSSSchemaRPC(Schema):
    id = fields.Str(required=True)


class GetRSSSchemaRPCResponse(_RSSSchema):
    pass


class UnsubscribeRSSSchemaRPC(Schema):
    id = fields.Str(required=True)


class UnsubscribeRSSSchemaRPCResponse(Schema):
    pass


class _FeedSchema(Schema):
    id = fields.Str(required=True)
    data = fields.Dict(required=True)


class GetFeedOfSubscribedRSSSchemaRPC(Schema):
    id = fields.Str(required=True)


class GetFeedOfSubscribedRSSSchemaRPCResponse(_FeedSchema):
    pass


class GetFeedsOfSubscribedRSSesSchemaRPC(Schema):
    pass


class GetFeedsOfSubscribedRSSesSchemaRPCResponse(_FeedSchema):
    pass


class GetFeedsOfSubscribedRSSSchemaRPC(Schema):
    rss_id = fields.Str(required=True)


class GetFeedsOfSubscribedRSSSchemaRPCResponse(_FeedSchema):
    pass
