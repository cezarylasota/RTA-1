from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1.0/predict", methods=["GET"])
def predict():
    try:
        # Pobierz wartości z parametrów zapytania
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
    except ValueError:
        # Gdyby podano coś, czego nie da się rzutować na float
        a, b = 0, 0

    # Reguła predykcji
    result = 1 if (a + b) > 5.8 else 0

    # Zwracany słownik
    return jsonify({
        "prediction": result,
        "features": {
            "a": a,
            "b": b
        }
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
