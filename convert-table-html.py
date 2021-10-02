# import dependency
import pandas as pd

df = pd.read_csv('Images/cities.csv')

html = df.to_html()

text_file = open("table.html", "w")
text_file.write(html)
text_file.close()