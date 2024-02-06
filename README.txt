# README.txt
This is the README file for the qualtrics data analysis project. 
There are a number of programs that are part of this package. 

PROGRAM				DESCRIPTION
--------------------------------------------------------------------------------------
analyze_train_exp.py 	   |	This program takes as input a cleaned Qualtrics .csv
			   |	file and calculates the percentage of stimuli	
			   |    which are correctly classified as each of the three	
			   |    categories (occlusion, shadow, texture), and outputs
			   |    a .csv file containing a confusion matrix.
--------------------------------------------------------------------------------------			   
setup_test_exp.py	   | 	This program sets up a .csv file for each of the 
			   |	surveys, which is then updated by analyze_test_exp.py			   
--------------------------------------------------------------------------------------
analyze_test_exp.py        |	This program takes a cleaned Qualtrics .csv file and 
			   |    a .csv file created by setup_test_exp.py and
			   |	outputs a .csv file which lists for each
			   |    stimulus the values of the three parameters which 	
                           |    we manipulate, as well as the number of observers 
			   |	who classified the stimulus into each of the three
			   |	categories (occlusion, shadow, texture).
--------------------------------------------------------------------------------------
format_spss.py		   |	This program takes the outputs of analyze_test_exp.py
			   | 	and then formats them for analysis in SPSS
			   |			  
