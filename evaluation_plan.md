# Evaluation Plan for Fine-Tuned MedicentreV3 Stock Assistant

## Purpose
To measure whether the fine-tuned model performs better than the current prompt-guided model on stock-related questions.

## Main evaluation goals
1. Check whether the model identifies correct stock tables
2. Check whether the model explains stock logic correctly
3. Check whether the model follows the required answer structure
4. Check whether the model avoids unsupported claims
5. Check whether the model remains focused on the stock module

## Models to compare
- Current prompt-guided assistant
- Future fine-tuned stock assistant

## Evaluation method
Use the same set of stock-related test questions on both models and compare the responses.

## What will be checked in each answer
- Did the model name the correct table?
- Did the explanation match the investigated schema?
- Did the answer follow the structure:
  - Direct Answer
  - Explanation
  - Relevant Table(s)
- Did the model avoid inventing unsupported facts?
- Did the model remain within the stock module?

## Result interpretation
The fine-tuned model will be considered improved if it:
- gives more correct table names
- gives more stable structured answers
- shows better consistency across question variations
- makes fewer unsupported claims