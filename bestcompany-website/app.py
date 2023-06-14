import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import math

'''
# Best Company
'''
# Variable 1 Slider
variable1 = st.slider('Select Rating of Criteria 1:', 1, 10, 1)
# Variable 2 Slider
variable2 = st.slider('Select Rating of Criteria 2:', 1, 10, 1)
# Variable 3 Slider
variable3 = st.slider('Select Rating of Criteria 3:', 1, 10, 1)
# Variable 4 Slider
variable4 = st.slider('Select Rating of Criteria 4:', 1, 10, 1)
# Variable 5 Slider
variable5 = st.slider('Select Rating of Criteria 5:', 1, 10, 1)

# Google Cloud Run URL
#url = 'https://bestcompany-nrfshmhfmq-ew.a.run.app/predict'

url = 'https://bestcompany-nrfshmhfmq-ew.a.run.app/predict'

dict_input = {'variable1': int(variable1), 'variable2': int(variable2),
              'variable3': int(variable3),
              'variable4': int(variable4),
              'variable5': int(variable5)}

response = requests.get(url, params=dict_input)

if response.status_code != 200:
    print('Error')

st.write('Your ranking is:')
st.write(response.json())
