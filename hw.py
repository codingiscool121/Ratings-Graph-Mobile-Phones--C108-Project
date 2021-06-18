import plotly.express as pd
import pandas as px
import plotly.figure_factory as pf

read=px.read_csv("rating.csv")
rating = read["Avg Rating"]
graph = pf.create_distplot([rating], ["Ratings for Smart Phones"], show_hist=False)
print("Opening ratings graph now...")
graph.show()
print('Ratings graph successfully opened.')

