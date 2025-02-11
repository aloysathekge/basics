def find_bots(follow_graph, threshold=2):
    """
    Returns accounts following ≥ threshold accounts but having ≤ 3 followers
    """
    for user, follow in follow_graph.items():
        bot = []
        following_sets = follow["following"]
        followers_sets = follow["followers"]

        following_count = len(following_sets)
        followers_count = len(followers_sets)

        if following_count >= threshold and followers_count <= 3:
            bot.append(user)

        return bot


def suggest_connections(user_a, user_b):
    """Returns followers of user_b that user_a doesn't follow"""
    followers_a = social_graph[user_a]["followers"]
    following_b = social_graph[user_b]["following"]

    suggested_conn = followers_a - following_b

    return suggested_conn


# ind_mutual_followers(follow_graph, user_a, user_b)
#  that returns a set of users who are following both user_a and user_b.


def find_mutual_followers(follow_graph, user_a, user_b):
    """Return mutual followers for user_a and user_b"""
    following_a = social_graph[user_a]["following"]
    following_b = social_graph[user_b]["following"]

    mutual = following_a & following_b
    return mutual


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

# print(find_bots(social_graph))
print(suggest_connections("user1", "user2"))
print(find_mutual_followers(social_graph, "user3", "user2"))
