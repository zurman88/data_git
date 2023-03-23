import pandas as pd
import random
import numpy as np
import datetime
import re


def word_generetor():
    keys = np.random.randint(0, 7, 5)
    letters_bank = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    word = ''.join(letters_bank[key] for key in keys)
    return word


li_names = [word_generetor() for i in range(0,9)]
li_ages= np.random.rand(9)
data = {'names' : li_names,
         'ages':li_ages}

df = pd.DataFrame(data)
print(df)
