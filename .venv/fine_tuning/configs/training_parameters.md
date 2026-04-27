# Training Parameters for MedicentreV3 Stock Assistant

## Base model
- llama3.2:1b

## Dataset path
- training_data/stock_qa_dataset_v1.jsonl

## Planned adapter output path
- fine_tuning/adapters/medicentre_stock_adapter

## Planned logs/output path
- fine_tuning/outputs/

## Conceptual training parameters

### Epochs
- Planned starting value: 3

### Batch size
- Planned starting value: 2 or 4

### Learning rate
- Planned starting value: 2e-4

### Sequence length
- Planned starting value: 1024

### LoRA rank
- Planned starting value: 8 or 16

### LoRA alpha
- Planned starting value: 16 or 32

## Main training objective
To teach the model to respond more consistently as a MedicentreV3 stock assistant using the required format:
- Direct Answer
- Explanation
- Relevant Table(s)

## Evaluation method
Use the prepared evaluation questions and compare:
- current prompt-guided model
- future fine-tuned model