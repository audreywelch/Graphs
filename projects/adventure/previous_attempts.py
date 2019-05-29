def mazeTraversal():
    # Create a visited graph
    # {0: {'n': '?', 's': '?', 'e': '?', 'w': '?'},
    # {5: {'n': 0, 's': '?', 'e': '?', 'w': '?'}}
    graph = {}

    # Save the current room ID into a variable
    currentRoomID = player.currentRoom.id

    # While the graph is smaller than 500
    while len(graph) < len(roomGraph):

        # if the currentRoomID is NOT in our graph yet...
        if currentRoomID not in graph:

            # Put the room into our graph with no exits yet
            graph[currentRoomID] = {}

            # For each exit the room has available
            for exit in player.currentRoom.getExits():
                # Set all exit values to '?' the first time visiting the room
                graph[currentRoomID][exit] = "?"

        # if the currentRoomID IS in our graph, or was just added...
        # For each exit the room has available
        for exit in player.currentRoom.getExits():
            # If it has unvisited exits
            if graph[currentRoomID][exit] == "?":
                #DFT looks through all unexplored rooms while appending path
                something = dft(graph)

            # If it has NO unvisited exits
                # BFS looks for closest path to a room that has an exit == '?'

def dft(graph):

    # Save the current room ID into a variable
    currentRoomID = player.currentRoom.id

    # Create an empty stack and push the startingRoomID
    s = Stack()
    s.push(currentRoomID)

    # While the stack is not empty...
    while s.size() > 0:
        # Pop the first vertex/room
        firstRoomID = s.pop()

        # For each possible exit the room contains
        # for exit in firstRoomID.getExits():
        # if 'n' in firstRoomID.getExits():

        # Check if 'n' exit has not been visited...
        if graph[currentRoomID]['n'] is not None and graph[currentRoomID]['n'] == "?":
            # Visit it by traveling there
            player.travel('n')
            # Append movement to traversalPath
            traversalPath.append('n')

            # Update the graph for the previous room
            graph[firstRoomID]['n'] = player.currentRoom.id
            # Update the graph for the current room
            #graph[player.currentRoom.id]['s'] = firstRoomID

            # Add the neighboring room / the room I've just moved into to the top of the stack
            s.push(firstRoomID)

        # Check if 's' exit has not been visited...
        elif graph[currentRoomID]['s'] is not None and graph[currentRoomID]['s'] == "?":
            # Visit it by traveling there
            player.travel('s')
            # Append movement to traversalPath
            traversalPath.append('s')

            # Update the graph for the previous room
            graph[firstRoomID]['s'] = player.currentRoom.id
            # Update the graph for the current room
            graph[player.currentRoom.id]['n'] = firstRoomID

            # Add the neighboring room / the room I've just moved into to the top of the stack
            s.push(firstRoomID)

        # Check if 'e' exit has not been visited...
        elif graph[currentRoomID]['e'] is not None and graph[currentRoomID]['e'] == "?":
            # Visit it by traveling there
            player.travel('e')
            # Append movement to traversalPath
            traversalPath.append('e')

            # Update the graph for the previous room
            graph[firstRoomID]['e'] = player.currentRoom.id
            # Update the graph for the current room
            graph[player.currentRoom.id]['w'] = firstRoomID

            # Add the neighboring room / the room I've just moved into to the top of the stack
            s.push(firstRoomID)

        # Check if 'w' exit has not been visited...
        elif graph[currentRoomID]['w'] is not None and graph[currentRoomID]['w'] == "?":
            # Visit it by traveling there
            player.travel('w')
            # Append movement to traversalPath
            traversalPath.append('w')

            # Update the graph for the previous room
            graph[firstRoomID]['w'] = player.currentRoom.id
            # Update the graph for the current room
            graph[player.currentRoom.id]['e'] = firstRoomID

            # Add the neighboring room / the room I've just moved into to the top of the stack
            s.push(firstRoomID)

    return graph