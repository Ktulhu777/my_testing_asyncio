from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["tom", "jonny"],
    "tom": ["maty", "baty"],
    "anuj": [],
    "peggy": ["neggy"]
}


def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person[-1] == "m":
            print(person)
            return True
        else:
            search_deque += graph[person]
            searched.append(person)
    return False


search("you")
