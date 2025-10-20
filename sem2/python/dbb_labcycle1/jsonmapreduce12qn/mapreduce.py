import json
import pandas as pd

with open('data.json') as f:
    data = json.load(f)["Data"]

df = pd.DataFrame(data.items(), columns=["id", "sentence"])
print(df.to_string(index=False),"\n")

df["words"] = df["sentence"].str.lower().str.split()
print(df.to_string(index=False),"\n")

all_words = df.explode("words")["words"].reset_index(drop=True)
mapped = pd.DataFrame({'word': all_words, 'count': 1})
print(mapped.to_string(index=False),"\n")

reduced = mapped.groupby("word", as_index=False).sum().sort_values(by="count", ascending=False)
print(reduced.to_string(index=False))

