import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Hypothesis Testing", page_icon="🤔💭📊🧮📝", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.title("Hypothesis Testing")

st.write("Hypothesis testing is a form of statistical inference that uses data from a sample to draw conclusions about a population parameter or a population probability distribution. First, a tentative assumption is made about the parameter or distribution. This assumption is called the null hypothesis and is denoted by H0.")

# read the dataset
df = pd.read_csv('AttendanceMarksSA.csv')
st.write("Our Dataset")
st.write(df)

st.write("Null Hypothesis: There is no significant relationship between attendance percentage and exam marks. In other words, attending more lectures does not result in better exam performance.")
st.write("Alternative Hypothesis: Students who attend more lectures get better exam results. In other words, there is a positive relationship between attendance percentage and exam performance.")

# create a scatter plot

st.markdown("## Scatter Plot")
st.write("Used to visualize the relationship between attendance percentage and exam marks")
st.markdown("### Scatter plot between Attendance and ESE")
sns.scatterplot(x='Attendance', y='ESE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()
# calculate the mean mid-semester exam marks and end semester exam marks for each attendance percentage
df_means = df.groupby('Attendance')[['MSE', 'ESE']].mean().reset_index()

# create a scatter plot
st.markdown("### Scatter plot between Attendance and MSE")
sns.scatterplot(x='Attendance', y='MSE', data=df)
plt.title('Attendance vs Mid Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('Mid Semester Exam Marks')
st.pyplot()


# create a bar chart
st.markdown("## Bar Chart")
st.write("Used to compare the average mid-semester exam marks and end semester exam marks based on attendance percentage")
sns.barplot(x='Attendance', y='value', hue='variable', data=pd.melt(df_means, id_vars='Attendance', var_name='variable', value_name='value'))
plt.title('Exam Marks vs Attendance')
plt.xlabel('Attendance percentage')
plt.ylabel('Marks')
st.pyplot()


from scipy.stats import ttest_ind

# separate the data into two groups based on attendance percentage
high_attendance = df[df['Attendance'] >= 80]['ESE']
low_attendance = df[df['Attendance'] < 80]['ESE']


# create a box plot
st.markdown("## Box Plot")
st.write("We can create a box plot to compare the distribution of exam marks for different attendance percentages. This will allow us to see the range of scores, the median, and any outliers for each group")
st.markdown("### Attendance vs ESE")
sns.boxplot(x='Attendance', y='ESE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()

st.markdown("### Attendance vs MSE")
sns.boxplot(x='Attendance', y='MSE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()

# create a heatmap
st.markdown("## Correlation Map")
st.write("Used to visualize the correlation between attendance percentage, mid-semester exam marks, and end semester exam marks. This will allow us to see if there is a strong correlation between any of the variable")
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Heatmap')
st.pyplot()

# create a scatter plot matrix
st.markdown("## Scatter-Pairplot")
st.write("Used to compare the relationship between all the variables in the dataset. This will allow us to see if there is a strong correlation between any of the variables, and to identify any outliers.")
sns.pairplot(df)
plt.title('Scatter Plot Matrix')
st.pyplot()



# create a line chart
st.markdown("## Lineplot")
st.write("to visualize the trend of end semester exam marks as the attendance percentage increases. This will allow us to see if there is a linear relationship between the two variables")
st.markdown("### Lineplot Attendance vs ESE")
sns.lineplot(x='Attendance', y='ESE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()

st.markdown("### Lineplot Attendance vs MSE")
sns.lineplot(x='Attendance', y='MSE', data=df)
plt.title('Attendance vs Mid Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()

# create a histogram
st.markdown("## Histogram")
st.write("Used to visualize the distribution of attendance percentages in the dataset. This will allow us to see the frequency of different attendance percentages and identify any patterns or outliers")
sns.histplot(data=df, x="Attendance", bins=10)
plt.title('Distribution of Attendance Percentage')
plt.xlabel('Attendance percentage')
plt.ylabel('Count')
st.pyplot()

# create a violin plot
st.markdown("## Violin plot")
st.write("We can create a violin plot to compare the distribution of end semester exam marks for different attendance percentages. This will allow us to see the shape of the distribution, and compare the spread and density of the distributions")
st.markdown("### Violin plot Attendance vs ESE")
sns.violinplot(x='Attendance', y='ESE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()

st.markdown("### Violin plot Attendance vs MSE")
sns.violinplot(x='Attendance', y='MSE', data=df)
plt.title('Attendance vs Mid Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('End Semester Exam Marks')
st.pyplot()

# create a bar chart

st.markdown("## Barplot")
st.write("to compare the mean end and mid semester exam marks for different attendance percentages. This will allow us to see if there is a significant difference in exam performance between students with different attendance percentages")
st.markdown("### Bar plot Attendance vs ESE")
sns.barplot(x='Attendance', y='ESE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('Mean End Semester Exam Marks')
st.pyplot()

st.markdown("### Bar plot Attendance vs MSE")
sns.barplot(x='Attendance', y='MSE', data=df)
plt.title('Attendance vs Mid Semester Exam Marks')
plt.xlabel('Attendance percentage')
plt.ylabel('Mean End Semester Exam Marks')
st.pyplot()

# create a joint plot
st.markdown("## Joint Plot")
st.write("to visualize the distribution of attendance percentage and end-mid semester exam marks together. This will allow us to see the relationship between the two variables and any patterns or outliers")
st.markdown("### Joint plot Attendance vs ESE")
sns.jointplot(x='Attendance', y='ESE', data=df)
plt.title('Attendance vs End Semester Exam Marks')
st.pyplot()

st.markdown("### Joint plot Attendance vs MSE")
sns.jointplot(x='Attendance', y='MSE', data=df)
plt.title('Attendance vs Mid Semester Exam Marks')
st.pyplot()

# perform t-test
t_stat, p_val = ttest_ind(high_attendance, low_attendance)

st.markdown("### T-Test Attendance Vs ESE")
st.write('----- T-Test Summary -----')
st.write('High Attendance group size: ', len(high_attendance))
st.write('Low Attendance group size: ', len(low_attendance))
st.write('High Attendance group mean: ', round(high_attendance.mean(), 2))
st.write('Low Attendance group mean: ', round(low_attendance.mean(), 2))
st.write('T-statistic: ', round(t_stat, 2))
st.write('P-value: ', round(p_val, 4))
if p_val < 0.05:
    st.write('The p-value is', p_val, 'which is less than the significance level of 0.05.')
    st.write('Therefore, we reject the null hypothesis and conclude that students who attend more lectures have better exam results.')
else:
    st.write('The p-value is', p_val, 'which is greater than the significance level of 0.05.')
    st.write('Therefore, we fail to reject the null hypothesis and cannot conclude that there is a significant difference between the two groups.')



high_attendance1 = df[df['Attendance'] >= 80]['MSE']
low_attendance1 = df[df['Attendance'] < 80]['MSE']

t_stat, p_val = ttest_ind(high_attendance1, low_attendance1)
st.markdown("### T-Test Attendance Vs MSE")
st.write('----- T-Test Summary -----')
st.write('High Attendance group size: ', len(high_attendance1))
st.write('Low Attendance group size: ', len(low_attendance1))
st.write('High Attendance group mean: ', round(high_attendance1.mean(), 2))
st.write('Low Attendance group mean: ', round(low_attendance1.mean(), 2))
st.write('T-statistic: ', round(t_stat, 2))
st.write('P-value: ', round(p_val, 4))
if p_val < 0.05:
    st.write('The p-value is', p_val, 'which is less than the significance level of 0.05.')
    st.write('Therefore, we reject the null hypothesis and conclude that students who attend more lectures have better exam results.')
else:
    st.write('The p-value is', p_val, 'which is greater than the significance level of 0.05.')
    st.write('Therefore, we fail to reject the null hypothesis and cannot conclude that there is a significant difference between the two groups.')
st.markdown('''### Done by [JASHVANTH S R ](https://www.linkedin.com/in/jashvanth-s-r-476646213)[HARUL GANESH S B ](https://www.linkedin.com/in/harul-ganesh/)[BALAJI S ](https://www.linkedin.com/in/balaji-s-csbs-dept-03790a202/)[GOWTHAM H](https://www.linkedin.com/in/gowtham-haribabu-9425861bb/)
---
''')
