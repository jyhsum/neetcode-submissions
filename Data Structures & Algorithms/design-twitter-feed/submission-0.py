import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        self.follow_map[userId].add(userId)

        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(min_heap)
            res.append(tweetId)

            if idx >= 0:
                next_count, next_tweetId = self.tweet_map[followeeId][idx]
                heapq.heappush(min_heap, [next_count, next_tweetId, followeeId, idx - 1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
