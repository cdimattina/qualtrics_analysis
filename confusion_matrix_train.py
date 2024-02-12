import pandas as pd
import numpy as np
import sys

csv_file            = sys.argv[1]

df                  = pd.read_csv(csv_file)
confusion_matrix    = np.zeros(shape=(3,3),dtype=int)

for (index, colname) in enumerate(df):
    if(index>0):
        if index <= 50:
            true_row = 0
        elif(index > 50 and index <= 100):
            true_row = 1
        else:
            true_row = 2

        num_edge = list(df[colname].values).count('Occlusion')
        num_shad = list(df[colname].values).count('Shadow')
        num_text = list(df[colname].values).count('Texture')

        confusion_matrix[true_row, 0] +=  num_edge
        confusion_matrix[true_row, 1] +=  num_shad
        confusion_matrix[true_row, 2] +=  num_text

print(confusion_matrix)