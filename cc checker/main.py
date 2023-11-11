from flask import Flask,render_template,request,jsonify



app= Flask(__name__)



@app.route("/")
def statrt():
    return render_template("index.html")

@app.route('/check_cards', methods=['POST'])
def check_cards():
    card_data = request.form.get('card_data')  # Retrieving the card data from the POST request
    result4 = "Your result string here"  # Your actual result should be here

    if 'Not enough balance' in result4:
        return jsonify({'status': 'CCN', 'message': f'{card_data} Not enough balance'})
    elif '"success":true' in result4:
        return jsonify({'status': 'LIVE', 'message': f'{card_data}CVV: Charged 5$'})
    else:
        return jsonify({'status': 'Declined', f'{card_data}message': 'Insan'})
    # Your card checking logic goes here
    # Process the card_data and determine the card's status (LIVE, CCN, etc.)
    # Return the result back to the JavaScript
    
    # For example:
    # status = check_card_function(card_data)
    # return jsonify({'status': status})
    
    # Just a placeholder response for demonstration purposes
    return jsonify({'status': 'LIVE'})  

app.run(debug=True)