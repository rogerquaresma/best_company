from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

'''
File to instantiate API so that it can communicate with the front-end dashboard

Assumptions:
The app.state will only be a minimum equation based on the evaluations from
Roger and Roxana.
'''

#Instantiate FastAPI instance
app = FastAPI()

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
    try:

        X = np.random.randint(10, size=(25)).tolist()
#        X= list(X)

        company_dict = {'Google': variable1*X[0] + variable2*X[1] + variable3*X[2] + variable4*X[3] + variable5*X[4],
                    'Amazon': variable1*X[5] + variable2*X[6] + variable3*X[7] + variable4*X[8] + variable5*X[9],
                    'Apple': variable1*X[10] + variable2*X[11] + variable3*X[12] + variable4*X[13] + variable5*X[14],
                    'Microsoft': variable1*X[15] + variable2*X[16] + variable3*X[17] + variable4*X[18] + variable5*X[19],
                    'Meta': variable1*X[20] + variable2*X[21] + variable3*X[22] + variable4*X[23] + variable5*X[24]}



        company_dict_sorted = {k: v for k, v in sorted(company_dict.items(), key=lambda item: item[1])}

        return {'Sorted_Company': company_dict_sorted}
        #return dict(Sorted_Company=company_dict_sorted)

    except Exception as e:
        return {"error": str(e)}

@app.get('/')
def root():
    return {'Greeting': 'Company Recommendation System'}
