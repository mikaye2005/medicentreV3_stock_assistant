# Fine-Tuning Plan for MedicentreV3 Stock Assistant

## Goal
To improve the assistant so that it naturally responds like a MedicentreV3 stock assistant even before long prompt guidance is added.

## Current model serving environment
- Ollama

## Current working base model
- llama3.2:1b

## Planned fine-tuning method
- LoRA adapter fine-tuning

## Why LoRA
LoRA is more practical than full model fine-tuning because it is lighter and more efficient.

## Training data source
- training_data/stock_qa_dataset_v1.jsonl

## Model behavior to improve
1. Recognize the correct stock tables
2. Distinguish current stock from stock movement
3. Explain stock take workflow
4. Explain branch-linked items
5. Answer in the format:
   - Direct Answer
   - Explanation
   - Relevant Table(s)

## Important rule
The adapter must later be attached to the same base model used during fine-tuning.

## Planned future output
- A trained LoRA adapter
- A Modelfile for importing the adapter into Ollama