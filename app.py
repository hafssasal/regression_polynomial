from flask import Flask, render_template, request
from model import predict_production

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    engrais_value = ""
    
    if request.method == "POST":
        engrais_value = request.form["engrais"]
        x = float(engrais_value)
        y = predict_production(x)
        result = f"🌾 Production estimée : {y} tonnes"
    
    return render_template("index.html", result=result, engrais_value=engrais_value)

app.run(debug=True)