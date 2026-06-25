import pandas as pd

data = {
    "name" : ["Alice", "Bob", "Charlie" , "David" , "Emma"],
    "score" : ["83", "74" , "87", "93", "97"]
}

df = pd.DataFrame(data)

high_scores_df = df[df["score" ] > 80]

print(high_scores_df)