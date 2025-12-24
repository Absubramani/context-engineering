# Prompt Evaluation Experiments

## Model Used
GPT-2 (not instruction-tuned)

-------------------------------------

## Experiment Goal
Evaluate how prompt length and wording affect model behavior
for a summarization task.

-------------------------------------

## Input Text
"Transformers changed natural language processing completely."

-------------------------------------

## Prompt Version 1: long.txt

### Prompt
You are a helpful assistant...
(Summarize instruction)

### Output Observed
Repeated input sentence multiple times.

### Failure Analysis
- Model ignored task instruction
- Output showed repetition
- No real summarization

### Reason
GPT-2 is not instruction-tuned and treats instructions as plain text.

-------------------------------------

## Prompt Version 2: compressed.txt

### Prompt
Summarize the following text in one sentence.

### Output Observed
Generated unrelated explanation of the word "transformers".

### Failure Analysis
- Prompt compression changed behavior
- Output became plausible but incorrect

### Reason
Model lacks task-following capability.

-------------------------------------

## Conclusion

Prompt compression affects output behavior, but model capability
is the limiting factor. Instruction-tuned models are required
for reliable task execution.
