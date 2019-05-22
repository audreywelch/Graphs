
# Undirected Graph
# We are looking for connected components
import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
    def __repr__(self):
        return self.friendships

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
        Plan:
            - Do a BFS
            - When we reach an unvisited user, append the path to the visited dictionary
            - return visited
        """

        # UserID is the starting vertex
        # Friendship node is the target vertex

        # Create an empty queue
        q = Queue()

        # Create an empty visited dictionary to store visited vertices and their paths
        visited = {}  # Note that this is a dictionary, not a set

        # Add a path to the starting vertex to the Queue
        q.enqueue([userID])

        # While the queue is not empty...
        while q.size() > 0:

            path = q.dequeue()

            # Grab the last vertex/friend from the path
            friend = path[-1]

            # if the key is NOT in the dictinoary already
            if friend not in visited:
                # When we reach an unvisited user, append the path to the visited dictionary
                visited[friend] = path

                for neighbor in self.friendships[friend]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    #print(sg.users)
    print("------------")
    print(sg.friendships)
    print("------------")
    connections = sg.getAllSocialPaths(1)
    print(connections)


    # def getAllSocialPathsFirstAttempt(self, userID):
    #     """
    #     Takes a user's userID as an argument

    #     Returns a dictionary containing every user in that user's
    #     extended network with the shortest friendship path between them = BFS
        
    #     The key is the friend's ID and the value is the path.
        
    #     EX: {1: {2, 4, 7}} Node with nodes it connects to
    #     Returns: {2: [1, 5, 2], 4: [None], 7: [1, 10, 2, 7]}

    #     Execution:
    #         - BFS (finds shortest path) for each node in the set of connections
    #         - the path that is returned is inserted into the `visited` dictionary as the value to the key (userID)
        
    #     """
    #     # Create an empty queue
    #     q = Queue()

    #     # Create an empty set to store visited sets in order to keep track along the way
    #     visited_set = set()

    #     # Create an empty visited dictionary to store visited vertices and their paths
    #     visited = {}  # Note that this is a dictionary, not a set

    #     # Get the values/friendships stored with each user
    #     all_friendships = self.friendships[userID]
    #     print(f'{all_friendships}')

    #     # UserID is the starting vertex
    #     # Friendship node is the target vertex

    #     # Enqueue a path that starts at the starting_vertex into the queue
    #     q.enqueue( [userID] )

    #     # While the queue is not empty...
    #     while q.size() > 0:

    #         for each_friendship in self.friendships[userID]:

    #             # Add the friendships to our final dictionary
    #             visited.update({each_friendship:[]})
    #             print(visited)

    #             #Dequeue the first path from the front of the array
    #             path = q.dequeue()

    #             # Grab the last vertex of the path
    #             v = path[-1]

    #             # Check if v is the target
    #             if v == each_friendship:
    #                 # If v is the target AND the length of the path is less than the one currently in the dictionary:
    #                 if len(path) < len(visited[each_friendship]):
    #                     # Update the path in the dictionary
    #                     visited.update(each_friendship = path)

    #             # Check if in visited
    #             if v not in visited_set:

    #                 # Add the vertex to Visited
    #                 visited_set.add(v)

    #                 # Then enqueue each path to each of its neighbors in the queue
    #                 path_copy = path.copy()
    #                 path_copy.append(v)
    #                 q.enqueue(path_copy)
    #                 print(visited_set)
    #                 print(q)
        

    #     return visited