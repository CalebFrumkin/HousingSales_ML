import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0, 8.0)
import seaborn as sns
from scipy import stats
from scipy.stats import norm
#load data sets
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print(train.head())
#check missing values
print(train.columns[train.isnull().any()])
#finding missing value counts
miss = train.isnull().sum()/len(train)
miss = miss[miss > 0]
miss.sort_values(inplace=True)
print(miss)
#sale price
sns.distplot(train['SalePrice'])

#create numeric plots
num = [f for f in train.columns if train.dtypes[f] !='object']
num.remove('Id')
nd= pd.melt(train, value_vars = num)
n1= sns.FacetGrid (nd, col='variable', col_wrap=4, sharex=False, sharey=False)
n1= n1.map(sns.distplot, 'value')
n1

#boxplots
def boxplot(x,y,**kwargs):
    sns.boxplot(x=x,y=y)
    x=plt.xticks(rotation=90)

cat=[f for f in train.columns if train.dtypes[f] == 'object']

p=pd.melt(train, id_vars='SalePrice', value_vars=cat)
g=sns.FacetGrid(p,col='variable', col_wrap=2, sharex=False, sharey=False, height=5)
g=g.map(boxplot, 'value', 'SalePrice')
g
