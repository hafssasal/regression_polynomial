from flask import Flask, render_template, request
from model import predict_production

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    
    if request.method == "POST":
        x = float(request.form["engrais"])
        y = predict_production(x)
        result = f"🌾 Production estimée : {y} tonnes"
    
    return render_template("index.html", result=result)

app.run(debug=True)