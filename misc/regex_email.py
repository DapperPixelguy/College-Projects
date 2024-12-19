import pandas as pd
import re

pd.set_option('display.max_colwidth', 75)
df = pd.read_csv('data/fraud_email_.csv')

emails = pd.Series(re.findall(r'<.*@.*\..*>', df['Text'].to_string()))
money = pd.Series(re.findall(r'(\$[0-9]+|USD.*[0-9]+|[0-9]+ dollars)', df['Text'].to_string(), re.IGNORECASE))
urgent = pd.Series(re.findall(r'URGENT|ASAP|IMPORTANT', df['Text'].to_string(), re.IGNORECASE))
links = pd.Series(re.findall(r'https?://[^\s]+', df['Text'].to_string(), re.IGNORECASE))
domains = pd.Series(re.findall(r'@.*\.com', df['Text'].to_string(), re.IGNORECASE))

print(pd.unique(emails))
print(len(pd.unique(emails)))
print(money)
print(urgent)
print(links)
print(domains.value_counts())