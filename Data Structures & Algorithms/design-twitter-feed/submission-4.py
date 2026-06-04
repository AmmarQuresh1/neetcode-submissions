class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Twitter:
    import heapq
    def __init__(self):
        # ID | [heap(news_feed), set(following)]
        self.user_table = dict()
        self.time = 1

    def createUser(self, userId):
        self.user_table[userId] = [[], set()]
        self.user_table[userId][1].add(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_table:
            self.createUser(userId)
        
        user = self.user_table[userId]
        heapq.heappush(user[0], (-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_table:
            self.createUser(userId)

        user = self.user_table[userId]

        feed_heaps = []
        for i in user[1]:
            heapq.heappush(feed_heaps, (list(self.user_table[i][0])))
        
        res = []
        for _ in range(10):
            if len(feed_heaps) == 0:
                return res
            print(feed_heaps)
            res.append(heapq.heappop(feed_heaps)[0][1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_table:
            self.createUser(followerId)
        if followeeId not in self.user_table:
            self.createUser(followeeId)

        follower = self.user_table[followerId]
        if followeeId not in follower[1]:
            follower[1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_table:
            self.createUser(followerId)
        if followeeId not in self.user_table:
            self.createUser(followeeId)
        
        # cannot unfollow self
        if followerId == followeeId:
            return None

        follower = self.user_table[followerId]
        if followeeId in follower[1]:
            follower[1].remove(followeeId)
