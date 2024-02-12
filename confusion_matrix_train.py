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


"""
def calculate_confusion_matrix(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Initialize dictionaries to store counts and correct classifications
    counts = {'occlusion': {'occlusion': 0, 'shadow': 0, 'texture': 0},
              'shadow': {'occlusion': 0, 'shadow': 0, 'texture': 0},
              'texture': {'occlusion': 0, 'shadow': 0, 'texture': 0}}
    correct_counts = {'occlusion': 0, 'shadow': 0, 'texture': 0}

    # Loop through each row in the DataFrame
    for index, row in df.iterrows():
        stimulus_category = row['Stimulus Category']
        observer_classification = row['Does this image patch contain an occlusion edge (boundary between two different surfaces), a shadow edge (change in illumination on a single surface), or a uniform texture (single surface)?']
        
        # Update counts
        counts[stimulus_category][observer_classification] += 1
        
        # Update correct counts
        if observer_classification == stimulus_category:
            correct_counts[stimulus_category] += 1

    # Calculate proportions
    confusion_matrix = pd.DataFrame(counts)
    confusion_matrix.index = ['occlusion', 'shadow', 'texture']
    confusion_matrix_percent = confusion_matrix.div(confusion_matrix.sum(axis=1), axis=0) * 100
    
    # Calculate percent correct
    percent_correct = {category: correct_counts[category] / confusion_matrix[category].sum() * 100 for category in correct_counts}

    return confusion_matrix_percent, percent_correct

# Example usage:
confusion_matrix, percent_correct = calculate_confusion_matrix('classification_results_train_1.csv')
print("Confusion Matrix:")
print(confusion_matrix)
print("\nPercent Correct:")
print(percent_correct)

# Note to Self: Find list of correct answers for "stimulus_category"
# Update the file path in the function call calculate_confusion_matrix('classification_results_train_1.csv') to point to the CSV file containing classification results.
"""

