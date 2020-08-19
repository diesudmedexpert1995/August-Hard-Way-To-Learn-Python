from collections import deque

s_graph = {}
s_graph["You"] = ["Alice", "Bob", "Claire"]
s_graph["Alice"] = ["Jack", "Sam", "Anujh"]
s_graph["Bob"] = ["Claire", "Yu", "Zara"]
s_graph["Claire"] = ["Naomi", "Jesse", "Tom"]
s_graph["Jack"] = []
s_graph["Sam"] = []
s_graph["Anujh"] = []
s_graph["Yu"] = []
s_graph["Zara"] = []
s_graph["Naomi"] = []
s_graph["Jesse"] = []
s_graph["Tom"] = []


def is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += s_graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(person + " is seller")
                return True
            else:
                search_queue += s_graph[person]
                searched.append(person)
    return False

search("You")
