from abc import ABC, abstractmethod
from apollo_shared.utils import Context
from apollo_shared.schema import rss as rss_schema


class RssRPC(ABC):
    name = 'rss'

    @abstractmethod
    def subscribe_rss(self, context: Context,
                      data: rss_schema.SubscribeRSSSchemaRPC) -> rss_schema.SubscribeRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_rsses(self, context: Context, data: rss_schema.GetRSSesSchemaRPC) -> rss_schema.GetRSSesSchemaRPCResponse:
        pass

    @abstractmethod
    def get_rss(self, context: Context, data: rss_schema.GetRSSSchemaRPC) -> rss_schema.GetRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def unsubscribe_rss(self, context: Context,
                        data: rss_schema.UnsubscribeRSSSchemaRPC) -> rss_schema.UnsubscribeRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_feed_of_subscribed_rss(self, context: Context,
                                   data: rss_schema.GetFeedOfSubscribedRSSSchemaRPC) -> rss_schema.GetFeedOfSubscribedRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_feeds_of_subscribed_rss(self, context: Context,
                                    data: rss_schema.GetFeedsOfSubscribedRSSSchemaRPC) -> rss_schema.GetFeedsOfSubscribedRSSSchemaRPCResponse:
        pass
