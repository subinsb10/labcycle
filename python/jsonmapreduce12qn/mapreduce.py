import json
import pandas as pd

with open('data.json') as f:
    data = json.load(f)["Data"]

df = pd.DataFrame(data.items(), columns=["id", "sentence"])
print(df.to_string(index=False))

df["words"] = df["sentence"].str.lower().str.split()
print("\nAfter Splitting Words")
print(df.to_string(index=False))

all_words = df.explode("words")["words"].reset_index(drop=True)
mapped = pd.DataFrame({'word': all_words, 'count': 1})
print("\n Map Output")
print(mapped.to_string(index=False))

reduced = mapped.groupby("word", as_index=False).sum().sort_values(by="count", ascending=False)
print("\n Reduce Output")
print(reduced.to_string(index=False))

