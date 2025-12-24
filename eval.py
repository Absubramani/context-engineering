from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

def load_prompt(path):
    with open(path, "r") as f:
        return f.read()

def run_prompt(prompt, input_text):
    full_prompt = prompt + "\n\nText:\n" + input_text

    inputs = tokenizer(full_prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=50,
            temperature=0.3
        )

    return tokenizer.decode(output[0], skip_special_tokens=True)

# test case
INPUT_TEXT = "Transformers changed natural language processing completely."

for prompt_file in ["long.txt", "compressed.txt"]:
    prompt = load_prompt(f"prompt_templates/{prompt_file}")
    output = run_prompt(prompt, INPUT_TEXT)

    print(f"\nPROMPT: {prompt_file}")
    print("OUTPUT:", output)
