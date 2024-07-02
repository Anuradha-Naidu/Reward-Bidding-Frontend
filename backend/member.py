class Member:
    def __init__(self, member_id, name, wish_coins):
        self.member_id = member_id
        self.name = name
        self.wish_coins = wish_coins
        self.events_registered = set()

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Wish Coins: {self.wish_coins}"

def add_member(members, member_id, name, wish_coins):
    if member_id in members:
        return f"Member with ID {member_id} already exists"
    members[member_id] = Member(member_id, name, wish_coins)
    return f"{name} added successfully"
