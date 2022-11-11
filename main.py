from flask import Flask, render_template, request
from utilis import DiabetesPrediction

app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("This is home API")
    return render_template("index.html")

@app.route("/predict", methods= ["POST"])
def get_prediction_api():
    Age = (request.form.get("Age"))
    DiabetesPedigreeFunction = (request.form.get("DiabetesPedigreeFunction"))
    BMI = (request.form.get("BMI"))
    Insulin = (request.form.get("Insulin"))
    BloodPressure =(request.form.get("BloodPressure"))
    Glucose = (request.form.get("Glucose"))
    
    diabetes_obj = DiabetesPrediction(Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = diabetes_obj.get_prediction()
    return render_template("index.html", prediction= result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= True, port=1998)
    
    