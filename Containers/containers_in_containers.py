"""
You can store containers in other containers. For example, you can store lists in a list:
"""

lists = []
rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin"]

djs = ["Zeds Dead",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

# print(lists)

"""
In this example lists has three indexes. Each index is a list: the first index is a list of rappers, the second index
is a list of rockers and the third index is a list of DJs. You can access these lists using their corresponding index:
"""

# Continue
# from previous example

# rap = lists[0]
# print(rap)

"""
If you append a new item to your rap list, you will see the change when you print your lists:
"""

rap = lists[0]
rap.append("Kendrick Lamar")
print(rap)
print(lists)

"""
You can store a tuple inside a list, a list inside a tuple, and a dictionary inside of a list or a tuple:
"""

locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

# ---------------------------------------------------------------------------

eights = ["Edgar Allan Poe",
          "Charles Dickens"]

nines = ["Hemingway",
         "Fitzgerald",
         "Orwell"]

authors = (eights, nines)
print(authors)