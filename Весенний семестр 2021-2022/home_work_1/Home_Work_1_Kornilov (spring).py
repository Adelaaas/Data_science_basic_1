import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error

df = pd.read_csv("C:/Users/danik/Downloads/Train.csv")
print(df)
print("-" * 30)
print(df.shape)
print("-" * 30)
print(df.dtypes)
print("-" * 30)
print(df.columns)
print("-" * 30)

df = df.dropna(how='any')

model = preprocessing.LabelEncoder()
model.fit(df['Employee_ID'])
df['Employee_ID'] = model.transform(df['Employee_ID'])
model.fit(df['Gender'])
df['Gender'] = model.transform(df['Gender'])
model.fit(df['Relationship_Status'])
df['Relationship_Status'] = model.transform(df['Relationship_Status'])
model.fit(df['Hometown'])
df['Hometown'] = model.transform(df['Hometown'])
model.fit(df['Unit'])
df['Unit'] = model.transform(df['Unit'])
model.fit(df['Decision_skill_possess'])
df['Decision_skill_possess'] = model.transform(df['Decision_skill_possess'])
model.fit(df['Compensation_and_Benefits'])
df['Compensation_and_Benefits'] = model.transform(df['Compensation_and_Benefits'])

x = df[['Employee_ID', 'Gender', 'Age', 'Education_Level',
        'Relationship_Status', 'Hometown', 'Unit', 'Decision_skill_possess',
        'Time_of_service', 'Time_since_promotion', 'growth_rate', 'Travel_Rate',
        'Post_Level', 'Pay_Scale', 'Compensation_and_Benefits',
        'Work_Life_balance', 'VAR1', 'VAR2', 'VAR3', 'VAR4', 'VAR5', 'VAR6',
        'VAR7']].values
y = df['Attrition_rate'].values
features = pd.Series(['Employee_ID', 'Gender', 'Age', 'Education_Level',
                      'Relationship_Status', 'Hometown', 'Unit', 'Decision_skill_possess',
                      'Time_of_service', 'Time_since_promotion', 'growth_rate', 'Travel_Rate',
                      'Post_Level', 'Pay_Scale', 'Compensation_and_Benefits',
                      'Work_Life_balance', 'VAR1', 'VAR2', 'VAR3', 'VAR4', 'VAR5', 'VAR6',
                      'VAR7'])
print(features)
print("-" * 30)
slr = LinearRegression()
slr.fit(x, y)
coeff_df = pd.DataFrame(slr.coef_, columns=['Coefficient'])
coeff_df['feachures'] = features
print(coeff_df)
print("-" * 30)

x1 = df[['Age']].values
y1 = df['Attrition_rate'].values

slr1 = LinearRegression()
slr1.fit(x1, y1)
y_pred = slr1.predict(x1)
print(f'Slope = {slr1.coef_}')
print(f'Intercept = {slr1.intercept_}')
print(f'y = {slr1.intercept_} + {slr1.coef_} * x')

plt.scatter(x1, y1)
plt.plot(x1, slr1.predict(x1), color='red', linewidth=1)
plt.show()
print('MSE: {:.3f}'.format(mean_squared_error(y, y_pred)))
