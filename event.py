class Event:
    def __init__(self, event_id, event_name, prize_name, event_date):
        self.event_id = event_id
        self.event_name = event_name
        self.prize_name = prize_name
        self.event_date = event_date
        self.bids = {}

    def __str__(self):
        return f"Event ID: {self.event_id}, Name: {self.event_name}, Prize: {self.prize_name}, Date: {self.event_date}"

def add_event(events, event_id, event_name, prize_name, event_date):
    if event_id in events:
        return f"Event with ID {event_id} already exists"
    events[event_id] = Event(event_id, event_name, prize_name, event_date)
    return f"{event_name} with prize {prize_name} added successfully"
