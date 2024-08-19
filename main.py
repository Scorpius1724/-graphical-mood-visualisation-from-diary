import glob
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px


analyzer = SentimentIntensityAnalyzer()

path_list = glob.glob("diary/*.txt")
sorted_path_list = sorted(path_list)

dates = [item.strip("diary\\.txt") for item in sorted_path_list]

content = []
for item in path_list:
    with open(item, "r") as file:
        text = file.read()
        content.append(text)

scores = []
for item in content:
    score = analyzer.polarity_scores(item)
    scores.append(score)

positive_scores = [item["pos"] for item in scores]
negative_scores = [item["neg"] for item in scores]

st.title("Diary Tone")

st.header("Positivity")

figure_1 = px.line(x=dates, y=positive_scores, labels={"x": "DATE", "y": "POSITIVITY"})
st.plotly_chart(figure_1)

st.header("Negativity")

figure_2 = px.line(x=dates, y=negative_scores, labels={"x": "DATES", "y": "NEGATIVITY"})
st.plotly_chart(figure_2)