from member import Member, add_member
from event import Event, add_event

class AuctionSystem:
    def __init__(self):
        self.members = {}
        self.events = {}

    def register_member(self, member_id, event_id):
        if member_id not in self.members:
            return f"Member with ID {member_id} does not exist"
        if event_id not in self.events:
            return f"Event with ID {event_id} does not exist"
        self.members[member_id].events_registered.add(event_id)
        return f"{self.members[member_id].name} registered for the {self.events[event_id].event_name} event successfully"

    def submit_bid(self, member_id, event_id, *bids):
        if member_id not in self.members:
            return f"Member with ID {member_id} does not exist"
        if event_id not in self.events:
            return f"Event with ID {event_id} does not exist"
        if event_id not in self.members[member_id].events_registered:
            return f"Member did not register for the event"
        self.events[event_id].bids[member_id] = bids
        return f"Bids submitted successfully"

    def declare_winner(self, event_id):
        if event_id not in self.events:
            return f"Event with ID {event_id} does not exist"
        event = self.events[event_id]
        if not event.bids:
            return "No bids submitted for this event"
        min_bid = float('inf')
        winner = None
        for member_id, bids in event.bids.items():
            total_bid = sum(bids)
            if total_bid < min_bid:
                min_bid = total_bid
                winner = self.members[member_id].name
        return f"{winner} wins the {event.prize_name} with the lowest bid of {min_bid}"
