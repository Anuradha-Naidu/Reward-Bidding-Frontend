from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from auction_system import AuctionSystem
from member import add_member
from event import add_event

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
auction_system = AuctionSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_member', methods=['POST'])
def add_member_route():
    data = request.json
    member_id = int(data['memberId'])
    name = data['memberName']
    wish_coins = int(data['wishCoins'])
    response = add_member(auction_system.members, member_id, name, wish_coins)
    return jsonify({'message': response})

@app.route('/add_event', methods=['POST'])
def add_event_route():
    data = request.json
    event_id = int(data['eventId'])
    event_name = data['eventName']
    prize_name = data['prizeName']
    event_date = data['eventDate']
    response = add_event(auction_system.events, event_id, event_name, prize_name, event_date)
    return jsonify({'message': response})

@app.route('/register_member', methods=['POST'])
def register_member_route():
    data = request.json
    member_id = int(data['memberId'])
    event_id = int(data['eventId'])
    response = auction_system.register_member(member_id, event_id)
    return jsonify({'message': response})

@app.route('/submit_bid', methods=['POST'])
def submit_bid_route():
    data = request.json
    member_id = int(data['memberId'])
    event_id = int(data['eventId'])
    bids = list(map(int, data['bids']))
    response = auction_system.submit_bid(member_id, event_id, *bids)
    return jsonify({'message': response})

@app.route('/declare_winner', methods=['POST'])
def declare_winner_route():
    data = request.json
    event_id = int(data['eventId'])
    response = auction_system.declare_winner(event_id)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
