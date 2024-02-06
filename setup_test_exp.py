"""
setup_test_exp.py

Description :   This program sets up the .csv file for teach test survey.
                This file is then passed in as input to a program which
                also takes as input the Qualtrics export file for that survey
                in order to tally how many participants classified each
                image as occlusion, shadow, texture

Usage       :   python setup_test_exp.py    <test_survey_num>
"""
import csv
import sys, os

qt_test_image_dir   = '../ARTSTIM/QTTEST/'

def get_survey_images(survey_num):
    # load .csv file with the image names for each test survey
    csv_file        = open("surveys.csv"  ,   newline='')
    csv_reader      = csv.reader(csv_file ,   delimiter=',')
    survey_list     = list(csv_reader)

    image_1_str     = survey_list[survey_num-1][1]
    image_2_str     = survey_list[survey_num-1][2]

    return image_1_str, image_2_str

def make_output_list(num_rows):
    this_list       = []
    for i in range(num_rows):
        this_list.insert(i,[])

    return this_list
def find_occurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
def extract_values(this_fname):

    this_row        = []
    und_ind         = find_occurrences(this_fname,'_')

    qnum_st_ind     = und_ind[1]
    qnum_sp_ind     = und_ind[2]
    lm_st_ind       = und_ind[6]
    lm_sp_ind       = und_ind[7]
    tp_st_ind       = und_ind[8]
    tp_sp_ind       = und_ind[9]
    tm_st_ind       = und_ind[10]
    tm_sp_ind       = und_ind[11]

    this_qnum       = this_fname[(qnum_st_ind+1):qnum_sp_ind]
    this_lm         = this_fname[(lm_st_ind + 1):lm_sp_ind]
    this_tp         = this_fname[(tp_st_ind + 1):tp_sp_ind]
    this_tm         = this_fname[(tm_st_ind + 1):tm_sp_ind]

    this_row        = [this_qnum, this_lm, this_tp, this_tm, '0' , '0', '0']

    return this_row

def main():
    survey_num = int(sys.argv[1])
    print("...setting up datafile for test survey " + str(survey_num))

    (image_1_str, image_2_str) = get_survey_images(survey_num)
    image_dir = qt_test_image_dir + image_1_str + "_" + image_2_str + "/"
    print(image_dir)

    dir_list    = os.listdir(image_dir)
    num_files   = len(dir_list)
    out_list    = make_output_list(num_files)

    for this_fname in dir_list:
        this_row = extract_values(this_fname)
        row_num  = int(this_row[0])
        out_list[row_num-1] = this_row

    header_list = ['im','lm','tp','tm','ne','ns','nt']

    # output a .csv file with the data
    csv_fname_out   = 'qt_survey_' + str(survey_num) + '_' + image_1_str + '_' + image_2_str + '.csv'
    csv_file        = open(csv_fname_out, 'w')
    csv_writer      = csv.writer(csv_file ,   delimiter = ',')
    csv_writer.writerow(header_list)
    for this_row in out_list:
        csv_writer.writerow(this_row)

    csv_file.close()

main()
