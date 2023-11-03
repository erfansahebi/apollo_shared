from abc import ABC, abstractmethod
from apollo_shared.utils import Context
from apollo_shared.schema import rss as rss_schema


class RssRPC(ABC):
    name = 'rss'

    @abstractmethod
    def subscribe_rss(self,
                      context: Context,
                      data: rss_schema.SubscribeRSSSchemaRPC,
                      ) -> rss_schema.SubscribeRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_rsses(self,
                  context: Context,
                  data: rss_schema.GetRSSesSchemaRPC,
                  ) -> rss_schema.GetRSSesSchemaRPCResponse:
        pass

    @abstractmethod
    def get_rss(self,
                context: Context,
                data: rss_schema.GetRSSSchemaRPC,
                ) -> rss_schema.GetRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def unsubscribe_rss(self,
                        context: Context,
                        data: rss_schema.UnsubscribeRSSSchemaRPC,
                        ) -> rss_schema.UnsubscribeRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_feed_of_subscribed_rss(self,
                                   context: Context,
                                   data: rss_schema.GetFeedOfSubscribedRSSSchemaRPC,
                                   ) -> rss_schema.GetFeedOfSubscribedRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_feeds_of_subscribed_rsses(self,
                                      context: Context,
                                      data: rss_schema.GetFeedsOfSubscribedRSSesSchemaRPC,
                                      ) -> rss_schema.GetFeedsOfSubscribedRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def get_feeds_of_subscribed_rss(self,
                                    context: Context,
                                    data: rss_schema.GetFeedsOfSubscribedRSSSchemaRPC,
                                    ) -> rss_schema.GetFeedsOfSubscribedRSSSchemaRPCResponse:
        pass

    @abstractmethod
    def add_comment_on_feed(self,
                            context: Context,
                            data: rss_schema.AddCommentOnFeedSchemaRPC,
                            ) -> rss_schema.AddCommentOnFeedSchemaRPCResponse:
        pass

    @abstractmethod
    def get_comments_on_feed(self,
                             context: Context,
                             data: rss_schema.GetCommentsOnFeedSchemaRPC,
                             ) -> rss_schema.GetCommentsOnFeedSchemaRPCResponse:
        pass

    @abstractmethod
    def get_comment_on_feed(self,
                            context: Context,
                            data: rss_schema.GetCommentOnFeedSchemaRPC,
                            ) -> rss_schema.GetCommentOnFeedSchemaRPCResponse:
        pass

    @abstractmethod
    def delete_comment_on_feed(self,
                               context: Context,
                               data: rss_schema.DeleteCommentOnFeedSchemaRPC,
                               ) -> rss_schema.DeleteCommentOnFeedSchemaRPCResponse:
        pass

    @abstractmethod
    def add_to_bookmarks(self,
                         context: Context,
                         data: rss_schema.AddToBookmarksSchemaRPC,
                         ) -> rss_schema.AddToBookmarksSchemaRPCResponse:
        pass

    @abstractmethod
    def get_bookmarks(self,
                      context: Context,
                      data: rss_schema.GetBookmarksSchemaRPC,
                      ) -> rss_schema.GetBookmarksSchemaRPCResponse:
        pass

    @abstractmethod
    def get_bookmark(self,
                     context: Context,
                     data: rss_schema.GetBookmarkSchemaRPC,
                     ) -> rss_schema.GetBookmarkSchemaRPCResponse:
        pass

    @abstractmethod
    def delete_from_bookmarks(self,
                              context: Context,
                              data: rss_schema.DeleteFromBookmarksSchemaRPC,
                              ) -> rss_schema.DeleteFromBookmarksSchemaRPCResponse:
        pass
