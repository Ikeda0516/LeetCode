class Twitter:
    def __init__(self):
        self.stack = []
        self.userToTweets = collections.defaultdict(list)
        self.userToFollowers = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userToTweets[userId].append(tweetId)
        self.stack.append([userId, tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for user, tweet in self.stack[::-1]:
            if len(res) == 10:
                return res
            if user in self.userToFollowers[userId] or user == userId:
                res.append(tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowers[followerId].discard(followeeId)