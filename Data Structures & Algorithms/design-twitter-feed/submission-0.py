class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Twitter:
    import heapq
    def __init__(self):
        # ID | [heap(news_feed), set(following)]
        self.user_table = dict()


    def createUser(self, userId):
        self.user_table[userId] = [[], set(userId)]
        self.time = 0

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

        res = []
        for _ in range(10):
            t_max = float('-inf')
            for followee in self.user_table[user][1]:
                post_time = self.user_table[followee][0][0]
                if post_time > t_max:
                    recent = followee
                    
            
            res.append(self.user_table[i])

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

        follower = self.user_table[followerId]
        if followeeId in follower[1]:
            follower[1].remove(followeeId)
