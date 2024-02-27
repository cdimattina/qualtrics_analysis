"""
convert_to_instances.py
Usage: python convert_to_instances.py <survey_num>
"""

import sys
import pandas as pd

survey_num          = int(sys.argv[1])
survey_name         = 'qt_survey_' + sys.argv[1] + '_tab.csv'
data_frame_input    = pd.read_csv(survey_name)

input_headers       = data_frame_input.columns.values.tolist()
output_headers      = input_headers[0:4]
output_headers.append('ct')

# get number of rows in the data frame
num_rows            = data_frame_input.shape[0]

# output list
output_list = []

for this_row in range(num_rows):
    this_input_row_list  = data_frame_input.iloc[this_row].tolist()
    this_output_row_list = this_input_row_list[0:4]
    num_edges            = int(this_input_row_list[4])
    num_shad             = int(this_input_row_list[5])
    num_text             = int(this_input_row_list[6])

    for edge_count in range(num_edges):
        this_row_entry  = this_output_row_list + ["Occlusion"]
        output_list.append(this_row_entry)

    for shad_count in range(num_shad):
        this_row_entry  = this_output_row_list + ["Shadow"]
        output_list.append(this_row_entry)

    for text_count in range(num_text):
        this_row_entry  = this_output_row_list + ["Texture"]
        output_list.append(this_row_entry)


df_out = pd.DataFrame(output_list,columns=output_headers)

# save output to
spss_file_full_name = 'qt_survey_' + str(survey_num) + '_spss.csv'
print('full spss file  : ' + spss_file_full_name)
df_out[output_headers].to_csv(spss_file_full_name,index=False)


