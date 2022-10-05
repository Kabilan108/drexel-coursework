
# Imports
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yaml

sns.set_style('whitegrid')


# Load data
with open('data/hw1.yml') as f:
	X = yaml.safe_load(f)['a_descr_stats']['x']
X = np.fromstring(X, sep='  ')


# Descriptive Statistics

## Sturges rule
k = 1 + 3.322*np.log10(len(X))  # Num of bins
R = X.max() - X.min()  # Range
w = R / k  # ~bin width

## Stats
mode = stats.mode(X)
mean = np.mean(X)
std = np.std(X)
median = np.percentile(X, 50)
q1 = np.percentile(X, 25)
q3 = np.percentile(X, 75)
iqr = q3 - q1

print(f"""
	Problem A

	1: Histogram
	------------
	Sturge's Rule
		k (# of Bins): {np.round(k)}
		w (~Bin Width): {np.round(w)}
		R (Range): {R}

	2: Mode = {mode.mode}

	4: Mean = {mean}
	   std = {std}

	5: Sorted: {sorted(X)}
	   Median, X_{(len(X) + 1)/2} = {median}
	   Q1, X_{(len(X)+1)/4} = {q1}
	   Q3, X_{3*(len(X)+1)/4} = {q3}

	6: IQR = Q3 - Q1 = {iqr}
	   Outliers = {X[(X > q3 + 1.5*iqr) | (X < q1 - 1.5*iqr)]}

""")

## Histogram
fig, ax = plt.subplots(1, 1, figsize=(6,4))
sns.histplot(x=X, binwidth=np.round(w), bins=np.round(k), ax=ax)
plt.savefig('results/hw1_a_hist.png')

## Boxplot
fig, ax = plt.subplots(1, 1, figsize=(4,6))
sns.boxplot(y=X)
plt.savefig('results/hw1_a_boxplot.png')