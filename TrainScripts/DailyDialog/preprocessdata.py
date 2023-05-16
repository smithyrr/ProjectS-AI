import pandas as pd

# Read the dialogues text file
with open('dialogues_text.txt', 'r', encoding='utf-8') as f:
    dialogues = f.readlines()

# Read the dialogues topic file
with open('dialogues_topic.txt', 'r', encoding='utf-8') as f:
    topics = f.readlines()

# Read the dialogues act file
with open('dialogues_act.txt', 'r', encoding='utf-8') as f:
    acts = f.readlines()

# Read the dialogues emotion file
with open('dialogues_emotion.txt', 'r', encoding='utf-8') as f:
    emotions = f.readlines()

# Preprocess the data
data = {
    'dialogue': dialogues,
    'topic': [int(topic.strip()) for topic in topics],
    'act': [int(act.split()[0]) for act in acts],
    'emotion': [int(emotion.split()[0]) for emotion in emotions]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the preprocessed dataset to CSV
df.to_csv('preprocessed_dataset.csv', index=False)
