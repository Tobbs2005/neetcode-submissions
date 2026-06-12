class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.following = defaultdict(set)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        usertweets = self.posts[userId]
        usertweets.append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        recents = []
        self.following[userId].add(userId)   
        for follow in self.following[userId]:
            if follow in self.posts:
                recentpost = self.posts[follow][-1]
                heapq.heappush(recents, [recentpost[0], recentpost[1], len(self.posts[follow])-1, follow])
        while recents and len(res) < 10:
            time, tweetId, index, follow = heapq.heappop(recents)
            res.append(tweetId)
            if index > 0:
                nextTweet = self.posts[follow][index-1]
                heapq.heappush(recents, [nextTweet[0], nextTweet[1], index-1, follow])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
