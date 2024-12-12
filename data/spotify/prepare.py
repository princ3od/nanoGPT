import os
import tiktoken
import numpy as np
import pandas as pd

current_dir = os.path.dirname(__file__)
input_file_path = os.path.join(current_dir, 'spotify_millsongdata.csv')

if not os.path.exists(input_file_path):
    print("spotify_millsongdata.csv does not exist. Please run download.py first.")
    exit()

df = pd.read_csv(input_file_path)
data = df['text'].str.cat(sep='\n')

print(f"preview: {data[:100]}")

total, _ = df.shape

n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)

print(f"total has {total:,} songs")
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens
