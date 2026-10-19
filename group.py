"""Represent a group of acquaintances in Python."""

my_group = {
    "Bohao": {
        "age": 23,
        "job": "Student in Scientific and Data Intensive Computing",
        "relations": ["Group_member"],
    },
    "Zhangjie": {
        "age": 24,
        "job": "Student in Scientific and Data Intensive Computing",
        "relations": ["Group_member"],
    },
}


def forget(person1, person2):
    """Remove the connection between two group members."""
    if person1 not in my_group or person2 not in my_group:
        raise ValueError("Both people must be in the group.")

    if person2 in my_group[person1]["relations"]:
        my_group[person1]["relations"].remove(person2)

    if person1 in my_group[person2]["relations"]:
        my_group[person2]["relations"].remove(person1)


def add_person(name, age, job, relations):
    """Add a member and create connections in both directions."""
    if name in my_group:
        raise ValueError(f"{name} is already in the group.")

    # Remove duplicate names from the supplied relations.
    relations = list(dict.fromkeys(relations))

    for person in relations:
        if person not in my_group:
            raise ValueError(f"{person} is not in the group.")

    my_group[name] = {
        "age": age,
        "job": job,
        "relations": relations,
    }

    for person in relations:
        my_group[person]["relations"].append(name)


def average_age():
    """Return the group's mean age, or None if the group is empty."""
    if not my_group:
        return None

    total_age = sum(person["age"] for person in my_group.values())
    return total_age / len(my_group)