from flask import Flask, render_template, request
from utilis import DiabetesPrediction

app = Flask(__name__)

@app.route("/")
def hello_flask():
    print("This is home API")
    return render_template("index.html")

@app.route("/predict", methos= ["POST"])
def get_prediction_api():
    Age = int(request.form.get("Age"))
    DiabetesPedigreeFunction = int(request.form.get("DiabetesPedigreeFunction"))
    BMI = int(request.form.get("BMI"))
    Insulin = int(request.form.get("Insulin"))
    BloodPressure =int(request.form.get("BloodPressure"))
    Glucose = int(request.form.get("Glucose"))
    
    diabetes_obj = DiabetesPrediction(Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = diabetes_obj.get_prediction()
    return render_template("index.html", prediction= result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= True, port=1998)
    
    