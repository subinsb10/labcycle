import json
import pandas as pd

with open('data.json') as f:
    data = json.load(f)["Data"]

df = pd.DataFrame(data.items(), columns=["id", "sentence"])
print(df.to_string(index=False))

df["words"] = df["sentence"].str.lower().str.split()
print("\n--- After Splitting Words ---")
print(df.to_string(index=False))

all_words = df.explode("words")["words"].reset_index(drop=True)
mapped = pd.DataFrame({'word': all_words, 'count': 1})
print("\n--- Map Output (word, 1) ---")
print(mapped.to_string(index=False))

reduced = mapped.groupby("word", as_index=False).sum().sort_values(by="count", ascending=False)
print("\n--- Reduce Output (Final Word Counts) ---")
print(reduced.to_string(index=False))

