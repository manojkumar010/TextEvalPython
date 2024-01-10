# TextEvalPython
Python Script for Text Evaluation Against Reference: Simplifying Assessment Processes
# ROUGE and BLEU Score Calculation for Summaries in Excel

This Python code automates the calculation of ROUGE and BLEU scores for summaries within an Excel file, making it easier to evaluate and compare their quality.

## Features
Simultaneous calculation of multiple scores: Calculates ROUGE-1, ROUGE-2, ROUGE-L, and BLEU scores for each summary.

Direct integration with Excel: Works directly with Excel files for seamless integration into your workflow.

Clear and concise output: Stores scores in separate columns within the same Excel file for easy analysis.

## Requirements
Python 3.x

pandas library (pip install pandas)

rouge library (pip install rouge)

nltk library (pip install nltk and then download the 'punkt' package using nltk.download('punkt'))

## Usage
Save your Excel file with two columns:

Summary: Contains the generated summaries to be evaluated.

referenceSummary: Contains the corresponding reference summaries.

Update the file path in the code: Replace 'your_excel_file.xlsx' with the actual path to your Excel file.

## Run the Python script.
Check the output: The code will create a new Excel file named output_with_scores.xlsx containing the original data along with calculated ROUGE and BLEU scores in their respective columns.

## Interpretation of Scores
Higher scores generally indicate better summaries.

Consider the context and purpose of your summaries when interpreting scores.

Combine with other evaluation methods like human judgment for a more comprehensive assessment.

## Additional Information
Learn more about ROUGE: http://www.aclweb.org/anthology/W04-1013: http://www.aclweb.org/anthology/W04-1013
Learn more about BLEU: https://www.aclweb.org/anthology/P02-1040.pdf: https://www.aclweb.org/anthology/P02-1040.pdf
Contributing


### Feel free to contribute to this project by suggesting improvements or reporting issues!
