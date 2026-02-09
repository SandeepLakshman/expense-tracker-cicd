from flask import Flask, request, jsonify

app = Flask(__name__)

expenses = []

@app.route("/")
def health():
    return {"status": "ok"}

@app.route("/expense", methods=["POST"])
def add_expense():
    data = request.json
    expenses.append(data)
    return {"message": "Expense added"}, 201

@app.route("/expenses")
def get_expenses():
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
