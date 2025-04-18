from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    # Pobranie liczb z parametrów zapytania, jeśli brak to domyślnie 0
    num1 = float(request.args.get('num1', 0))
    num2 = float(request.args.get('num2', 0))
    
    # Reguła predykcji
    prediction = 1 if (num1 + num2) > 5.8 else 0
    
    # Stworzenie odpowiedzi
    response = {
        'prediction': prediction,
        'features': {
            'num1': num1,
            'num2': num2
        }
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
