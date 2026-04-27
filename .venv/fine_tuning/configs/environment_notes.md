# Fine-Tuning Environment Notes

## Purpose
This folder will support the future fine-tuning stage for the MedicentreV3 stock assistant.

## Planned structure
- adapters/: trained LoRA adapters
- configs/: training configuration notes and future config files
- scripts/: fine-tuning scripts
- outputs/: logs and training results

## Current chosen base model
- llama3.2:1b

## Current training dataset
- training_data/stock_qa_dataset_v1.jsonl

## Fine-tuning goal
To improve the model's ability to answer MedicentreV3 stock questions accurately, consistently, and in the required structured format.

## Important rule
The same base model used for training must later be used in the Ollama Modelfile when attaching the adapter.