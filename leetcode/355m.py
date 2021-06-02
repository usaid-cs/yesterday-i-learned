class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = 0
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets = [(userId, tweetId)] + self.tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.follows:
            userIds = [userId]
        else:
            userIds = [userId] + self.follows[userId]
        return [p[1] for p in self.tweets if p[0] in userIds][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follows:
            self.follows[followerId].append(followeeId)
        else:
            self.follows[followerId] = [followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.follows:
            return
        self.follows[followerId] = [x for x in self.follows[followerId] if x != followeeId]



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
