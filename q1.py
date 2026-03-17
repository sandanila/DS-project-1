import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Attendance': [90, 85, 60, 45, 95, 30, 88, 72, 55, 98],
    'Marks': [85, 80, 55, 40, 92, 25, 82, 68, 50, 96]
}
df = pd.DataFrame(data)
print(df)

sns.scatterplot(x='Attendance', y='Marks', data=df)
plt.title('Attendance vs Marks')
plt.show()
