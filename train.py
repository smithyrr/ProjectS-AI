import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
import pandas as pd
import wandb


# Load data from text files
with open('/mnt/d/ProjectSAi/TrainScripts/DailyDialog/dialogues_text.txt', 'r', encoding='utf-8') as f:
    train_inputs = f.read().splitlines()

with open('/mnt/d/ProjectSAi/TrainScripts/DailyDialog/dialogues_emotion.txt', 'r', encoding='utf-8') as f:
    train_outputs = f.read().splitlines()

with open('/mnt/d/ProjectSAi/TrainScripts/DailyDialog/dialogues_topic.txt', 'r', encoding='utf-8') as f:
    train_topics = f.read().splitlines()

with open('/mnt/d/ProjectSAi/TrainScripts/DailyDialog/dialogues_act.txt', 'r', encoding='utf-8') as f:
    train_acts = f.read().splitlines()


# Load validation data from text files
with open('/mnt/d/ProjectSAi/validation/dialogues_validation.txt', 'r', encoding='utf-8') as f:
    val_inputs = f.read().splitlines()

with open('/mnt/d/ProjectSAi/validation/dialogues_emotion_validation.txt', 'r', encoding='utf-8') as f:
    val_outputs = f.read().splitlines()


# Initialize wandb
wandb.init(project='PROJECT-S Ai')

# Load pre-trained model and tokenizer
model_name = 't5-base'
tokenizer = T5Tokenizer.from_pretrained(model_name, model_max_length=512)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Set the device to 'cuda' if available, else use 'cpu'
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Tokenize data
train_encodings = tokenizer(train_inputs, truncation=True, padding=True, max_length=512)
val_encodings = tokenizer(val_inputs, truncation=True, padding=True, max_length=512)

train_labels = tokenizer(train_outputs, truncation=True, padding=True, max_length=512).input_ids
val_labels = tokenizer(val_outputs, truncation=True, padding=True, max_length=512).input_ids


# Prepare datasets
class DialogDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = DialogDataset(train_encodings, train_labels)
val_dataset = DialogDataset(val_encodings, val_labels)

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results', 
    num_train_epochs=1, 
    per_device_train_batch_size=4,  # Decrease batch size
    per_device_eval_batch_size=16,  # Decrease batch size
    warmup_steps=500,
    weight_decay=0.01, 
    logging_dir='./logs', 
    logging_steps=10,
    evaluation_strategy='epoch', 
    save_strategy='epoch',
    load_best_model_at_end=True,
    report_to="wandb",
)

# Create the Trainer and begin training
trainer = Trainer(
model=model,
args=training_args,
train_dataset=train_dataset,
eval_dataset=val_dataset
)

trainer.train()

# Save the trained model
model.save_pretrained('/mnt/d/ProjectSAi/TrainedModels/ModelBase')
tokenizer.save_pretrained('/mnt/d/ProjectSAi/TrainedModels/ModelBase')

# Finish wandb run
wandb.finish()