import pandas as pd
import numpy as np
import tkinter as ttk
import joblib
import os

# Initialize the Flask application
app = ttk.Tk()
app.configure(background='white')
app.geometry('350x400')
app.title('Medical Expense Estimator')

# Load the model from the saved file
scaler = joblib.load('scaler.save')
model = joblib.load('Medical Expenses Prediction.save')

age = ttk.Variable(app)
ttk.Label(app, text='Age', padx=15 , pady=15, background='white').grid(row=0, column=0)
ttk.Entry(app, textvariable=age).grid(row=0, column=1)

sex = ttk.Variable(app)
values = ['Select','Male','Female']
sex.set(values[0])
ttk.Label(app, text='Sex', padx=15 , pady=15, background='white').grid(row=1, column=0)
ttk.OptionMenu(app, sex, *values).grid(row=1, column=1)

bmi = ttk.Variable(app)
ttk.Label(app, text='BMI', padx=15 , pady=15, background='white').grid(row=2, column=0)
ttk.Entry(app, textvariable=bmi).grid(row=2, column=1)

children = ttk.Variable(app)
ttk.Label(app, text='Children', padx=15 , pady=15, background='white').grid(row=3, column=0)
ttk.Entry(app, textvariable=children).grid(row=3, column=1)

smoker = ttk.Variable(app)
values1 = ['Select','Yes','No']
smoker.set(values1[0])
ttk.Label(app, text='Smoker', padx=15 , pady=15, background='white').grid(row=4, column=0)
ttk.OptionMenu(app, smoker, *values1).grid(row=4, column=1)

region = ttk.Variable(app)
values2 = ['Select','North-East','North-West','South-East','South-West']
region.set(values2[0])
ttk.Label(app, text='Region', padx=15 , pady=15, background='white').grid(row=5, column=0)
ttk.OptionMenu(app, region, *values2).grid(row=5, column=1)

def prediction():
    global model
    if sex.get() == 'Male':
        if smoker.get() == 'No':
            if region.get() == 'North-East':
                x = [age.get(),0,bmi.get(),children.get(),0,0]
            elif region.get() == 'North-West':
                x = [age.get(),0,bmi.get(),children.get(),0,1]
            elif region.get() == 'South-East':
                x = [age.get(),0,bmi.get(),children.get(),0,2]
            elif region.get() == 'South-West':
                x = [age.get(),0,bmi.get(),children.get(),0,3]
 
        elif smoker.get() == 'Yes':
            if region.get() == 'North-East':
                x = [age.get(),0,bmi.get(),children.get(),1,0]
            elif region.get() == 'North-West':
                x = [age.get(),0,bmi.get(),children.get(),1,1]
            elif region.get() == 'South-East':
                x = [age.get(),0,bmi.get(),children.get(),1,2]
            elif region.get() == 'South-West':
                x = [age.get(),0,bmi.get(),children.get(),1,3]
 
    elif sex.get() == 'Female':
        if smoker.get() == 'No':
            if region.get() == 'North-East':
                x = [age.get(),1,bmi.get(),children.get(),0,0]
            elif region.get() == 'North-West':
                x = [age.get(),1,bmi.get(),children.get(),0,1]
            elif region.get() == 'South-East':
                x = [age.get(),1,bmi.get(),children.get(),0,2]
            elif region.get() == 'South-West':
                x = [age.get(),1,bmi.get(),children.get(),0,3]

        elif smoker.get() == 'Yes':
            if region.get() == 'North-East':
                x = [age.get(),1,bmi.get(),children.get(),1,0]
            elif region.get() == 'North-West':
                x = [age.get(),1,bmi.get(),children.get(),1,1]
            elif region.get() == 'South-East':
                x = [age.get(),1,bmi.get(),children.get(),1,2]
            elif region.get() == 'South-West':
                x = [age.get(),1,bmi.get(),children.get(),1,3]
       
    x = np.array(x).reshape(1,-1)
    
    expense = model.predict(scaler.transform(x))
    result.set(f'{(round(expense[0],2))} $')

ttk.Button(app, text='Predict', command=prediction).grid(row=6, column=0, columnspan=2)
result = ttk.Variable(app)
ttk.Label(app, textvariable=result, pady=15, font=('Arial',20), background='white').grid(row=7, column=0, columnspan=2)

app.mainloop()