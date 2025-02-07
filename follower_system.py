def find_bots(follow_graph, threshold=6):
    """
    Returns accounts following ≥ threshold accounts but having ≤ 10 followers
    """
    followers_list = []
    following_list = []

    for user, follow in follow_graph.items():
        for item, handles in follow.items():

            if item == "following":
                print(f"{user}: has {handles} following them")
            elif item == "followers":
                print(f"{user}: is following this {handles} accounts")

def suggest_connections(user_a, user_b)

        """Returns followers of user_b that user_a doesn't follow
        """

social_graph = {
    "user1": {"following": {"user2", "user3"}, "followers": {"user2", "user4"}},
    "user2": {"following": {"user1"}, "followers": {"user1", "user3", "user5"}},
    "user3": {"following": {"user1", "user4"}, "followers": {"user1", "user2"}},
    "user4": {"following": {"user3"}, "followers": {"user1", "user5"}},
    "user5": {"following": {"user2"}, "followers": {"user2", "user4"}},
    "user6": {"following": {"user1", "user2", "user3"}, "followers": {"user3"}},
    "user7": {"following": {"user4"}, "followers": {"user1", "user6"}},
    "user8": {"following": {"user5"}, "followers": {"user2", "user3"}},
    "user9": {"following": {"user6"}, "followers": {"user5"}},
    "user10": {
        "following": {"user7", "user8"},
        "followers": {"user1", "user2", "user3"},
    },
}

find_bots(social_graph)
