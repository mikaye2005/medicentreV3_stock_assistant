# Training Workflow Notes

## Stage 1 — Dataset preparation
- Build stock-specific instruction and answer examples
- Validate JSONL structure
- Keep answers in a consistent format

## Stage 2 — External fine-tuning
- Use a fine-tuning framework that can output a LoRA adapter in Safetensors format
- Keep the same base model as the one intended for Ollama serving

## Stage 3 — Import into Ollama
- Create a Modelfile with:
  - FROM <base model>
  - ADAPTER <adapter path>
  - SYSTEM <assistant behavior>
- Build the model with ollama create
- Test the model with ollama run

## Stage 4 — Integrate back into Django
- Update Django settings to use the fine-tuned Ollama model name
- Re-test assistant answers
- Compare behavior before and after fine-tuning
