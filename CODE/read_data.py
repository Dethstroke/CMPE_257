import numpy as np
import pandas as pd



df = pd.read_csv('wine_data.csv', index_col=False,names = ['cultivar','Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 'Total Phenols', 'Flavanoids', 'NonFalvanid Phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'OD280/oD315 of diluted wines', 'Proline' ])


new_df = df.loc[df['cultivar'] == 1]

alcohol_mean = new_df['Alcohol'].mean()

print('Cultivar 1 Alchohol Mean: ' + str(alcohol_mean))


new_df = df.loc[df['cultivar'] == 2]

alcohol_mean = new_df['Alcohol'].mean()

print('Cultivar 2 Alchohol Mean: ' + str(alcohol_mean))

new_df = df.loc[df['cultivar'] == 3]

pd.new_df.plot

alcohol_mean = new_df['Alcohol'].mean()

print('Cultivar 3 Alchohol Mean: ' + str(alcohol_mean))




