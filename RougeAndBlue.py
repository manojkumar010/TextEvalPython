import pandas as pd
from rouge import Rouge
from nltk.translate.bleu_score import sentence_bleu

# Load the Excel sheet
df = pd.read_excel('your_excel_file.xlsx')

# Create empty columns for ROUGE and BLEU scores
df['Rouge'] = None
df['Blue'] = None

# Instantiate ROUGE and BLEU objects
rouge = Rouge()

# Iterate through each row and calculate scores
for index, row in df.iterrows():
   summary = row['Summary']
   reference_summary = row['referenceSummary']

   # Calculate ROUGE scores
   rouge_scores = rouge.get_scores(summary, reference_summary)
   rouge_1 = rouge_scores[0]['rouge-1']['f']
   rouge_2 = rouge_scores[0]['rouge-2']['f']
   rouge_l = rouge_scores[0]['rouge-l']['f']

   # Calculate BLEU score
   bleu_score = sentence_bleu([reference_summary.split()], summary.split())

   # Store scores in the DataFrame
   df.loc[index, 'Rouge'] = f"{rouge_1:.4f}, {rouge_2:.4f}, {rouge_l:.4f}"  # Store multiple ROUGE scores
   df.loc[index, 'Blue'] = bleu_score

# Save the modified DataFrame with scores
df.to_excel('output_with_scores.xlsx', index=False)
