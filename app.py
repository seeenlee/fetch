from flask import Flask, request, jsonify

app = Flask(__name__)

transactions = []
balances = {}

@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.json
        payer = data['payer']
        points = data['points']
        timestamp = data['timestamp']

    except:
        return "Error parsing request", 400

    transactions.append({'payer': payer, 'points': points, 'timestamp': timestamp})
    transactions.sort(key=lambda x: x['timestamp']) # this sort will run in O(N) because Python uses Timsort

    balances[payer] = balances.get(payer, 0) + points

    return '', 200
    
@app.route('/spend', methods=['POST'])
def spend():
    try:
        data = request.json
        points = data['points']
    except:
        return "Error parsing request", 400
    
    if points <= 0:
        return "Can't spend zero or negative points", 400
    
    if points > sum(balances.values()):
        return "User doesn't have enough points", 400
    
    affected = {}
    to_remove = []

    for index, transaction in enumerate(transactions):
        payer = transaction['payer']
        payment_points = transaction['points']

        removable_points = min(payment_points, points)
        balances[payer] -= removable_points
        transaction['points'] -= removable_points
        if transaction['points'] == 0:
            to_remove.append(index)
        
        affected[payer] = affected.get(payer, 0) - removable_points
        points -= removable_points

        if points == 0:
            break
    
    # removing in reverse order will preserve index accuracy
    # ex: removing index 0 will make the old index 1 the new index 0
    for index in reversed(to_remove):
        del transactions[index]
    
    # return in the array format specified in handout
    return [{"payer": key, "points": val} for key, val in affected.items()], 200

@app.route('/balance', methods=['GET'])
def balance():
    return jsonify(balances), 200

if __name__ == '__main__':
    app.run(port=8000)