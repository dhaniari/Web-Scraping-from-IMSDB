from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

# Custom Dataset for GPT-2 Fine-tuning
class ScreenplayDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length):
        self.tokenizer = tokenizer
        self.texts = texts
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        encoding = self.tokenizer(text, truncation=True, padding='max_length', max_length=self.max_length, return_tensors='pt')
        return encoding['input_ids'].squeeze(), encoding['attention_mask'].squeeze()

# Load Data
screenplay_texts = [...]  # List of preprocessed screenplay texts
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Prepare the dataset
dataset = ScreenplayDataset(screenplay_texts, tokenizer, max_length=512)

# Load Pre-trained GPT-2 model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Training Arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    warmup_steps=500,
    logging_dir='./logs',
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# Fine-tune the model
trainer.train()
