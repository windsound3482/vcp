# Demographic 

import sys
import json
import numpy as np


# Takes first name and last name via command 
# line arguments and then display them

print("Output from Python")
def json_age_rgb():
    dir_age_rbg = {'18-24':[1.0, 0.7529411764705882, 0.796078431372549],
                    '25-31':[0.9411764705882353, 0.5019607843137255, 0.5019607843137255],
                    '32-38':[0.803921568627451, 0.3607843137254902, 0.3607843137254902],
                    '39-45':[0.6980392156862745, 0.13333333333333333, 0.13333333333333333],
                    '46-52':[0.5450980392156862, 0.0, 0.0],
                    '53-60':[0.5019607843137255, 0.0, 0.0]}
    json_age_rgb = json.dumps(dir_age_rbg)                
    return json_age_rgb             

if sys.argv[2] == 'json_age_rgb':
    print(json_age_rgb())
print(np.array[0,100])
print("First name: " + sys.argv[1])
print("Last name: " + sys.argv[2])

