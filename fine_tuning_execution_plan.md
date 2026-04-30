# Fine-Tuning Execution Plan for MedicentreV3 Stock Assistant

## Purpose
To define the real execution path for fine-tuning the MedicentreV3 stock assistant before actual training begins.

## Stage 1 — Dataset preparation
- Build the JSONL stock question-answer dataset
- Validate dataset structure
- Keep answer format consistent:
  - Direct Answer
  - Explanation
  - Relevant Table(s)

## Stage 2 — External training
- Use a fine-tuning framework that can output a LoRA adapter in Safetensors format
- Keep the same base model intended for Ollama serving
- Train on the stock-specific dataset only

## Stage 3 — Import into Ollama
- Create a Modelfile using:
  - FROM <base model>
  - ADAPTER <adapter path>
  - SYSTEM <assistant behavior>
- Build the tuned model with ollama create
- Test the model with ollama run

## Stage 4 — Integrate back into Django
- Update Django or environment configuration to use the new Ollama model name
- Re-test assistant behavior in the web interface
- Compare current model and fine-tuned model using the prepared evaluation questions

## Expected final output
- A tuned Ollama model specialized for MedicentreV3 stock questions
- More consistent structured responses
- Better table identification
- Better boundary discipline
