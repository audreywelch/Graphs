
# Undirected Graph
# We are looking for connected components
import random

class User:
    def __init__(self, name):
        self.name = name
    def __repr___(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {} # Vertices - indexed by ID
        self.friendships = {} # Edges between users

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set() # Initialize with an empty set

    # Seed our social network
    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users - we want to create `numUsers` number of users
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # Generate every possible combination of friendships, shuffle it, then slice off exactly how many friendships we need to generate
        possibleFriendships = []

        # Generate all possible friendship combinations
        for userID in self.users: # get all the keys in the users dictionary
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Shuffle the friendship combinations
        random.shuffle(possibleFriendships)

        # Slice off exactly how many friendships we need to generate
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.users)
    print(sg.friendships)
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
