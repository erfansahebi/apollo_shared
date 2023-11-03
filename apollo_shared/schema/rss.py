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


class _BookmarkSchema(Schema):
    id = fields.Str(required=True)
    feed_id = fields.Str(required=True)


class AddToBookmarksSchemaRPC(Schema):
    feed_id = fields.Str(required=True)


class AddToBookmarksSchemaRPCResponse(_BookmarkSchema):
    pass


class GetBookmarksSchemaRPC(Schema):
    pass


class GetBookmarksSchemaRPCResponse(_BookmarkSchema):
    pass


class GetBookmarkSchemaRPC(Schema):
    bookmark_id = fields.Str(required=True)


class GetBookmarkSchemaRPCResponse(_BookmarkSchema):
    pass


class DeleteFromBookmarksSchemaRPC(Schema):
    bookmark_id = fields.Str(required=True)


class DeleteFromBookmarksSchemaRPCResponse(Schema):
    pass


class _CommentSchema(Schema):
    id = fields.Str(required=True)
    message = fields.Str(required=True)


class AddCommentOnFeedSchemaRPC(Schema):
    feed_id = fields.Str(required=True)
    message = fields.Str(required=True)


class AddCommentOnFeedSchemaRPCResponse(_CommentSchema):
    pass


class GetCommentsOnFeedSchemaRPC(Schema):
    feed_id = fields.Str(required=True)


class GetCommentsOnFeedSchemaRPCResponse(_CommentSchema):
    pass


class GetCommentOnFeedSchemaRPC(Schema):
    feed_id = fields.Str(required=True)
    comment_id = fields.Str(required=True)


class GetCommentOnFeedSchemaRPCResponse(_CommentSchema):
    pass


class DeleteCommentOnFeedSchemaRPC(Schema):
    feed_id = fields.Str(required=True)
    comment_id = fields.Str(required=True)


class DeleteCommentOnFeedSchemaRPCResponse(Schema):
    pass
