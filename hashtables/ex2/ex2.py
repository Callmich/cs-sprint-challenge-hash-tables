# # One-Way Flight Trip
# Write a function `reconstruct_trip` to reconstruct your trip from your
# mass of flight tickets. Each ticket is represented as a class with the following form:

# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination

# where the `source` string represents the starting airport and the
# `destination` string represents the next airport along our trip. The
# ticket for your first flight has a destination with a `source` of
# `NONE`, and the ticket for your final flight has a `source` with a
# `destination` of `NONE`. 

# tickets = [
#     Ticket{ source: "PIT", destination: "ORD" },
#     Ticket{ source: "XNA", destination: "CID" },
#     Ticket{ source: "SFO", destination: "BHM" },
#     Ticket{ source: "FLG", destination: "XNA" },
#     Ticket{ source: "NONE", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "CID", destination: "SLC" },
#     Ticket{ source: "ORD", destination: "NONE" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "BHM", destination: "FLG" }
# ]

# Your function should output an array of strings with the entire route of
# your trip. For the above example, it should look like this:

# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

# Your solution should run in linear time. You can assume that your
# function will always be handed a valid ticket chain as input. 

# ## Hints

# * The crux of this problem requires us to 'link' tickets together to
#   reconstruct the entire trip. For example, if we have a ticket `('SJC',
#   'BOS')` that has us flying from San Jose to Boston, then there exists
#   another ticket where Boston is the starting location, `('BOS',
#   'JFK')`. 

# * We can hash each ticket such that the starting location is the key and
#   the destination is the value. Then, when constructing the entire
#   route, the `i`th location in the route can be found by checking the
#   hash table for the `i-1`th location.


#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # set up a dictionary with the tickets
    # use a for loop for the length of the tickets
        # set the current airport to None.
        # find the current airpoirt
        # append the destination into the route
        # change the current airport to the destination and go through the loop
    my_dict = {}
    route = []

    for tic in tickets:
        my_dict[tic.source] = tic.destination

    current_airport = "NONE"
    for x in range(length):
        destination = my_dict[current_airport]
        route.append(destination)
        current_airport = destination
        

    return route
