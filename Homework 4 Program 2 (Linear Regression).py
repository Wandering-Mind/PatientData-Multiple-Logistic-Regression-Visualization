
# Homework 4 Assignment
# Date modified 10.24.24

#Assignment Instructions: Do more peopl
# For this part of the assignment, the dependent variable needs to be a 0-1 valued column.
# Fit a logistic regression model using a categorical variable as the dependent variable and
# write up a brief summary of the results, commenting on the decision you are trying to
# support with the model as well as which variables are significant and the interpretation
# of your model results. 
# Program 2 instruction: Logistic Regression
    #(b) fit a logistic regression model using values from the dataset above^ 


import pandas as pd
from scipy import stats
import statsmodels.api as sm

url = 'https://health.data.ny.gov/resource/7dtz-qxmr.json'

patient_data_df = pd.read_json(url)

new_patient_data_df=patient_data_df[['mean_cost', 'discharges','mean_charge']].copy()

# calculating the correlation coefficient between discharges & mean_charge & mean_cost

print("n\Pearsons r: ",\
      stats.pearsonr(new_patient_data_df['mean_cost'],new_patient_data_df['discharges']))

# Performance of a linear regression using the linregress function
slope,intercept, r_value, p_value, std_err = \
                 stats.linregress(new_patient_data_df['mean_cost'],new_patient_data_df['discharges'])

# Report results for slope, intercept, R-value, p-value, andf Standard Error
print("\nslope: ",round(slope,3), "\nintercept: ", round(intercept,3),\
      "\nr_value: ",round(r_value,3), "\np_value: ",format(p_value, '.3e'),\
      "\nstd_err: ",round(std_err,3))

# Report results for skewness of variables
print("\nSkew for Mean Cost Data: ",round(stats.skew(new_patient_data_df['mean_cost']),3))
print("\nSkew for Discharge Data: ", round(stats.skew(new_patient_data_df['discharges']),3))




##### Summary ######

# Overall Summary:
# The correlation between mean cost and discharges is weak but statistically significant. Yes, there is a relationship
# but it's not strong enough to make significant or robust predications. The regression slope suggests that an increase
# in the number of discharges doesn't significantly affect the mean cost. In practical terms,
# this means that mean costs remain relatively stable regardless of how many discharges are reported.
# Both mean cost and discharges are highly skewed, indicating that most data points cluster around lower values,
# with some extreme high outliers. 

######################

# The following insights are drawn from the data provided on the Correlation Coefficient & P-Value:
# (A) Correlation Coefficient (r): -0.1335 --> This indicates a weak negative correlation between
#   'mean_cost' and 'discharges'. A negative value means that as 'discharges' increase,
#   the 'mean_cost' tends to decrease, but the relationship is weak since it's close to zero (0)

# (B) P-value: 2.282e-05 --> The p-value is very small, less than 0.05, meaning this result is statistically significant.
#   Even though the correlation is weak, it's unlikely to have occurred by chance

# The following insights are drawn from the Linear Regression Model:
# (A) Slope (-0.0) suggests that changes in the # of 'discharges' have an extremely
#   minimal or no effect on mean cost.
# (B) Intercept: 41.307 --> this represents the predicted 'mean_cost' when the # of discharges is zero (0).
#   if no discharges are present, the predicted mean cost is $41, 307 (a detriment to the financial operational
#   efficiency and profitability of the facility
# (C) R-squared or r_value: -0.133 --> indicates a weake negative relationship between the 2 variables
# (D) Standard Error: 0.0 --> this is very low, which suggests that the estimate of the slope is precise
# (E) Skewness:
#       (E1) Skew for Mean_Cost Data: 3.934
#       (E2) Skew for Discharge Data: 7.499
#   Both variables have high skewness. Mean Cost's skew of 3.934 indicates that most patients have lower mean costs
#   but there's some with very high mean costs. 'Discharges' have a skew of 7.499, indicating that a small # of hospitals
#   report very high discharge numbers, while most report lower discharge #s


