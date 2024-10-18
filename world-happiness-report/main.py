import pandas as pd

df = pd.read_csv('WHR2023.csv')

print(f'Correlation between Healthy life expectancy and Social support: {df["Healthy life expectancy"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Generosity and Perception of corruption: {df["Generosity"].corr(df["Perceptions of corruption"]).round(2)}')
print(f'Correlation between Freedom to make life choices and Social support: {df["Freedom to make life choices"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Freedom to make life choices and Social support: {df["Freedom to make life choices"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Generosity and Logged GDP per capita: {df["Generosity"].corr(df["Logged GDP per capita"]).round(2)}')
print(f'Correlation between Ladder score and Perception of corruption: {df["Ladder score"].corr(df["Perceptions of corruption"]).round(2)}')

