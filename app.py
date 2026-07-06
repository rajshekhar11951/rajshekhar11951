from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    income = float(request.form["income"])
    loan = float(request.form["loan"])
    credit_utilization = float(request.form["credit_utilization"])
    payment_history = request.form["payment_history"].lower()
    existing_loans = int(request.form["existing_loans"])

    if (
        income >= 700000
        and credit_utilization < 30
        and payment_history == "excellent"
        and existing_loans <= 1
    ):
        score = "Excellent"
    elif (
        income >= 400000
        and credit_utilization <= 60
        and payment_history in ["good", "excellent"]
        and existing_loans <= 3
    ):
        score = "Good"
    elif income >= 250000 and credit_utilization <= 80:
        score = "Standard"
    else:
        score = "Poor"

    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
