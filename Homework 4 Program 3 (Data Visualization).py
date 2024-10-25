# Homework 4 Assignment
# Date modified 10.24.24


# Program 3 instruction: Data Visualization
#(a) create at least 1 data visualization 

#For this portion of the assignment, create a Python program
#that uses the seaborn package to create visualization(s)
#of the data from your dataset. Your completed assignment is
# to include the following: 

# Comments to explain what is happening at each step as well
# as one in the beginning of your code that has your name and
# the date the code was created and/or last modified.
#At least one visualization that uses the seaborn package that includes at least
# two plots charted together.


# This code loads patient data, performs a multiple regression analysis, and creates a visualization with Seaborn.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Load the dataset
patient_df = pd.read_json('https://health.data.ny.gov/resource/7tt5-bh39.json?')
print(patient_df.mean_charge.value_counts())

# Select relevant columns for the creation of a new dataframe
new_patient_df = patient_df[['mean_charge', 'apr_severity_of_illness_code', 'discharges']].copy()

# Performance of a multiple regression analysis
model = smf.ols("mean_charge ~ apr_severity_of_illness_code + discharges", data=new_patient_df).fit()
print("\nModel summary:", model.summary())

# Visualization creation using Seaborn: Scatter plot with a regression line
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Scatter plot for mean_charge vs. discharges
sns.scatterplot(x='discharges', y='mean_charge', hue='apr_severity_of_illness_code', data=new_patient_df, palette="viridis", alpha=0.7)

# Addition of a regression line for each severity level
sns.regplot(x='discharges', y='mean_charge', data=new_patient_df, scatter=False, color="blue", line_kws={'label':'Regression Line'})

# Customization of plot 
plt.title("Mean Charge vs Discharges with APR Severity Levels")
plt.xlabel("Discharges")
plt.ylabel("Mean Charge")
plt.legend(title="APR Severity of Illness Code")
plt.show()


########### SUMMARY ###########

# The scatter plot can be used to analyze several things:
# (A) Relationship between Discharges and Mean Charge: The scatter plot shows how the
#       mean_charge varies with the number of discharges. A visible upward trend in
#       the regression line would suggest that higher discharge counts
#       correlate with higher mean charges, implying that patient volume may
#       influence average charge levels.

# (B) Impact of Severity on Charges: By coloring points according to apr_severity_of_illness_code,
#       you can observe whether severity affects charges. For instance, if higher severity levels
#       cluster at higher mean_charge values,this would indicate that more severe cases generally
#       incur greater costs.

# (C) Fit & Predictive Power/Ability: Additional variables should be considered in order for these/this
#       model(s) to increase the ability of a predictive analysis

# (D) Outliers & Clusters: Outliers or clusters in this data reveal more atypical cases. Very high
#   charges for low discharge numbers may suggest specific high-cost cases - inclusive of high-cost treatments, service fees
#   and/or pre-existing conditions that have yet to be treated but have begun to be treated at the time of visit/inpatient stay
