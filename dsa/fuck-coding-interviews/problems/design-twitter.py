# https://leetcode.com/problems/design-twitter/description/
from . import List, defaultdict, heapq


class Twitter:
    def __init__(self):
        self.followers = defaultdict(set) # key : val_list map
        self.tweets = defaultdict(list) # userId : ()
        self.tweet_counter = 0 

    # o(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_counter -= 1
        self.tweets[userId].append([-self.tweet_counter, tweetId])

    # time: o(k)
    def getNewsFeed(self, userId: int) -> List[int]:
        total_feeds = self.tweets[userId][-10:]
        # time: o((k+1)*o(10)) ==> o(k)
        for follwer in self.followers[userId]:
            if self.tweets[follwer]:
                total_feeds.extend(self.tweets[follwer][-10:])
        return self._recent_feeds(total_feeds)

    # time: o(k)
    @staticmethod
    def _recent_feeds(total_feeds):
        total_feeds.sort(reverse=True) # time: o(klog10)
        return [tweet_id for _, tweet_id in total_feeds[:10]] # time: o(k)
    
    # time: o(k)
    @staticmethod
    def _recent_feeds_heap_version(total_feeds):
        heapq.heapify(total_feeds) # time: o(klog10)
        res = []
        # time: o(10logk) == > o(k)
        while len(res) <= min(10, len(total_feeds)):
            _, tweetId = heapq.heappop(total_feeds)
            res.append(tweetId)
        return res

    # time: o(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        # update news feed.

    # time: o(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        # update news feed. 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)