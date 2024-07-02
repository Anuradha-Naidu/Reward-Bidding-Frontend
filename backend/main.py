from auction_system import AuctionSystem
from member import add_member
from event import add_event

def run_auction_system():
    auction_system = AuctionSystem()

    while True:
        command = input("Enter command (ADD_MEMBER, ADD_EVENT, REGISTER_MEMBER, SUBMIT_BID, DECLARE_WINNER, EXIT): ").strip().upper()

        if command == "ADD_MEMBER":
            _, member_id, name, wish_coins = input("Enter command (ADD_MEMBER <member_id> <name> <wish_coins>): ").split()
            member_id = int(member_id)
            wish_coins = int(wish_coins)
            print(add_member(auction_system.members, member_id, name, wish_coins))

        elif command == "ADD_EVENT":
            _, event_id, event_name, prize_name, event_date = input("Enter command (ADD_EVENT <event_id> <event_name> <prize_name> <event_date>): ").split()
            event_id = int(event_id)
            print(add_event(auction_system.events, event_id, event_name, prize_name, event_date))

        elif command == "REGISTER_MEMBER":
            _, member_id, event_id = input("Enter command (REGISTER_MEMBER <member_id> <event_id>): ").split()
            member_id = int(member_id)
            event_id = int(event_id)
            print(auction_system.register_member(member_id, event_id))

        elif command == "SUBMIT_BID":
            _, member_id, event_id, *bids = input("Enter command (SUBMIT_BID <member_id> <event_id> <bid_1> <bid_2> <bid_3> <bid_4> <bid_5>): ").split()
            member_id = int(member_id)
            event_id = int(event_id)
            bids = list(map(int, bids))
            print(auction_system.submit_bid(member_id, event_id, *bids))

        elif command == "DECLARE_WINNER":
            _, event_id = input("Enter command (DECLARE_WINNER <event_id>): ").split()
            event_id = int(event_id)
            print(auction_system.declare_winner(event_id))

        elif command == "EXIT":
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    run_auction_system()

