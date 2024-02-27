"""
tabulate_test_survey.py

This program takes the outputs of the raw surveys and tabulates the proportion of observers who
classified each image as being occlusion, shadow, or texture. It also outputs a file suitable for
chi-squared analysis using the cross-tabs feature of SPSS.

tabulate_test_survey.py <survey_num> <raw_file> <tab_file>

"""

import sys
import pandas as pd

num_test_questions  = 64

raw_file_name       = sys.argv[2]
tab_file_empty_name = sys.argv[3]
survey_num          = int(sys.argv[1])

spss_file           = 'qt_survey_' + str(survey_num) + '_spss.csv'

print('survey         : ' + str(survey_num))
print('raw file       : ' + raw_file_name)
print('empty tab file : ' + tab_file_empty_name)

# first load the empty tabulated file into a Pandas data frame
data_frame_empty    = pd.read_csv(tab_file_empty_name)
tab_empty_list      = data_frame_empty.values.tolist()
tab_full_list       = tab_empty_list
tab_full_headers    = data_frame_empty.columns.values.tolist()

# now load the raw data in order to tabulate the information
data_frame_raw      = pd.read_csv(raw_file_name)

for this_index in range(num_test_questions):
    # get dataframe header
    header_str      = 'Q' + str(this_index + 1)
    this_col_list   = data_frame_raw[header_str].values.tolist()
    tab_full_list[this_index][4] = this_col_list.count('Occlusion')
    tab_full_list[this_index][5] = this_col_list.count('Shadow')
    tab_full_list[this_index][6] = this_col_list.count('Texture')

df_out = pd.DataFrame(tab_full_list,columns=tab_full_headers)

# save output to
tab_file_full_name = 'qt_survey_' + str(survey_num) + '_tab.csv'
print('full tab file  : ' + tab_file_full_name)
df_out[tab_full_headers].to_csv(tab_file_full_name,index=False)
