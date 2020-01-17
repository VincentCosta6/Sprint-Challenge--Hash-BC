#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    sources = HashTable(8)

    for i in range(length):
        ticket = tickets[i]

        hash_table_insert(sources, ticket.source, ticket)

    find = "NONE"
    for i in range(length):
        if i != 0:
            find = route[i - 1]

        route[i] = hash_table_retrieve(sources, find).destination

    return route
