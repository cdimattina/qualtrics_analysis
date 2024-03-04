# README.txt
This is the README file for the qualtrics data analysis project. 
There are a number of programs that are part of this package. 

PROGRAM				DESCRIPTION
--------------------------------------------------------------------------------------
confusion_matrix_train.py  |	This program takes as input a cleaned Qualtrics .csv
			   |	file and calculates the percentage of stimuli	
			   |    which are correctly classified as each of the three	
			   |    categories (occlusion, shadow, texture), and outputs
			   |    to the display the confusion matrix. Rows are the actual
			   |    category (occlusion, shadow, texture) and columns
			   |    are the category guessed by the participants 
			   |    with the same ordering as the rowa	
			   |
			   | 	Usage 
			   |    -----    
			   |	python confusion_matrix_train.py <file>
			   |	
			   |	input  : <file> = classification_results_train_<1,2>.csv
			   |	
--------------------------------------------------------------------------------------			  setup_test_exp.py	   | 	This program sets up a .csv file for each of the 
			   |	test surveys, which is then updated by tabulate_test_survey.py
			   |	to include the number of responses for each category
			   |	from each of the participants
			   |	
			   |    Usage
			   |    -----
			   |	python setup_test.py <survey_num>
			   |	
			   |	input  : <survey_num> = 1-10
			   |   	output : qt_survey_<survey_num>_<im1>_<im2>.csv
			   |
--------------------------------------------------------------------------------------
tabulate_test_survey.py    |	This program takes a cleaned Qualtrics .csv file and 
			   |    a .csv file created by setup_test_exp.py and
			   |	outputs a .csv file which lists for each
			   |    stimulus the values of the three parameters which 	
                           |    we manipulate, as well as the number of observers 
			   |	who classified the stimulus into each of the three
			   |	categories (occlusion, shadow, texture).
			   |
			   |	Usage
			   |	-----
			   |	python tabulate_test_survey.py <survey_num> <empty_survey> 
			   |					<raw_data>
			   |
			   |	input  : <survey_num> 	= 1-10
			   |		 <empty_survey> = qt_survey_<survey_num>_<im1>_<im2>.csv
			   |		 <raw_data>     = qt_survey_<survey_num>_raw.csv
			   |	output : qt_survey_<survey_num>_tab.csv
			   |
--------------------------------------------------------------------------------------
convert_to_instances.py    |	This program takes the outputs of analyze_test_exp.py
			   | 	and then formats them for analysis in SPSS
			   |
			   |	Usage
			   |	-----
			   |	python analyze_test_exp.py <survey_num>
			   |
			   |	input  : <survey_num> 	= 1-10			  
			   |	output : qt_survey_<survey_num>_spss.csv
			   |
