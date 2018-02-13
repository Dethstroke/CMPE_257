import numpy as np
import pandas as pd



df = pd.read_csv('wine_data.csv', names = ['Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 'Total Phenols', 'Flavanoids', 'NonFalvanid Phenols', 'Proanthocyanins', 'Color Intensity', 'Hue', 'OD280/oD315 of diluted wines', 'Proline' ])


print(df)