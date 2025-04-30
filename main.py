import pandas as pd
from data_cleaner import cleanData

df = pd.read_csv('data/country_wise_latest.csv')
cleanData('data/country_wise_latest.csv')
newCases = df['New cases'].sum()
print('Latest Total Cases: {}'.format(newCases))
avgDeathperCases = df['Deaths/100 Cases'].sum() / df['Deaths/100 Cases'].count()
print('Latest Average Deaths per 100 Cases: {}'.format(avgDeathperCases))

df = pd.read_csv('data/worldometer_data.csv')
cleanData('data/worldometer_data.csv')
medAmericaCases = df[df['WHO Region'] == 'Americas']['TotalCases'].median()
print('Median of Total Cases in the Americas: {}'.format(medAmericaCases))
stdTotalDeaths = df['TotalDeaths'].std()
print('Standard Deviation of Total Deaths: {}'.format(stdTotalDeaths))
modeTotRecovered = df['TotalRecovered'].mode()
print('Mode of Total Recovered per Total Cases: \n{}\n'.format(modeTotRecovered))