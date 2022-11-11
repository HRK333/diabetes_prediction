import pickle
import pandas as pd
import numpy as np
import config

class DiabetesPrediction():
    def __init__(self,Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age):
        self.glucose = Glucose
        self.bloodpressure = BloodPressure
        self.insulin = Insulin
        self.bmi = BMI
        self.diabetespedigreefunction = DiabetesPedigreeFunction
        self.age = Age
        
    def load_model(self):
        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)
                
    def get_prediction(self):
        self.model
        
        array = np.zeros(6)
        
        array[0]= self.glucose
        array[1]= self.bloodpressure 
        array[2]= self.insulin
        array[3]= self.bmi
        array[4]= self.diabetespedigreefunction
        array[5]= self.age
        
        predicted_result = self.model.predict([array])
        return predicted_result
    
        
if __name__== "__main__":
    Age = 25
    DiabetesPedigreeFunction = 0.65
    BMI = 27.5
    Insulin = 94
    BloodPressure =68
    Glucose = 150
    
    diabetes_obj = DiabetesPrediction(Glucose,BloodPressure,Insulin,BMI,DiabetesPedigreeFunction,Age)
    result = diabetes_obj.get_prediction()
    if result == 0:
        print("You dont have diabetes")
    else:
        print("You have diabetes.")