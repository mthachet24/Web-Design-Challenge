import pandas as pd 


a = pd.read_csv("Resources/cities (1).csv")


a.to_html("data.html")