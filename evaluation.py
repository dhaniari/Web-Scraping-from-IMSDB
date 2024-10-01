from transformers import GPT2LMHeadModel, GPT2Tokenizer

def calculate_perplexity(model, input_text):
    model.eval()
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    loss = outputs.loss
    perplexity = torch.exp(loss)
    return perplexity.item()

# Example usage
perplexity = calculate_perplexity(model, "INT. LIVING ROOM - DAY\nJohn enters the room.")
print(f"Perplexity: {perplexity}")
