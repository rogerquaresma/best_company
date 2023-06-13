from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

'''
File to instantiate API so that it can communicate with the front-end dashboard

Assumptions:
1) The app.state will only be a minimum equation based on the evaluations from
Roger and Roxana.
'''

#Instantiate FastAPI instance
app = FastAPI()
app.state()
# Allowing all middleware just in case for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/predict')
def predict(variable1: int,
            variable2: int,
            variable3: int,
            variable4: int,
            variable5: int):

    X = np.random.randint(10, size=(25))
    X= list(X)

    for i, num in enumerate(X):
        locals()['X'+f'{i}'] = num

    company_dict = {'Google': variable1*(X0) + variable2*(X1) + variable3*(X2) + variable4*(X3) + variable5*(X4),
                'Amazon': variable1*(X5) + variable2*(X6) + variable3*(X7) + variable4*(X8) + variable5*(X9),
                'Apple': variable1*(X10) + variable2*(X11) + variable3*(X12) + variable4*(X13) + variable5*(X14),
                'Microsoft': variable1*(X15) + variable2*(X16) + variable3*(X17) + variable4*(X18) + variable5*(X19),
                'Meta': variable1*(X20) + variable2*(X21) + variable3*(X22) + variable4*(X23) + variable5*(X24)}

    company_dict_sorted = {k: v for k, v in sorted(company_dict.items(), key=lambda item: item[1])}

    return company_dict_sorted

@app.get('/')
def root():
    return {'Greeting': 'Company Recommendation System'}
