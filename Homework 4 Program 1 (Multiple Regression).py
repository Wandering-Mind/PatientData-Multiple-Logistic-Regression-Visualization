# Homework 4 Assignment
# Rose Dunderdale
# Date modified 10.25.24

# Program 1 instruction: Multiple Regression 
    # (a) fit a multiple regression model using values
    # from this dataset - https://data.ny.gov/Human-Services/Patient-Characteristics-Survey-PCS-2022-Persons-Se/w8eu-45mn/about_data

import pandas as pd
import statsmodels as sm
import statsmodels.formula.api as smf

# dependent variable: mean_charge

# loaing the dataset
patient_df = pd.read_json('https://health.data.ny.gov/resource/7tt5-bh39.json?')
print(patient_df.mean_charge.value_counts())

# Selecting relevant columns and creating a new dataframe
new_patient_df = patient_df[['mean_charge', 'apr_severity_of_illness_code','discharges']].copy()

# multiple regression using ols function
model= smf.ols("""mean_charge ~ apr_severity_of_illness_code + discharges""", data=new_patient_df).fit()

# results report for model using summary method
print("\nModel summary: ", model.summary())


######### SUMMARY ##########

# What the dataset, as a whole, contains is information - beginning in 2009 -
# on the volume of discharges, All Payer Refined Diagnosis Related Group (APR-DRG),
# the severity of illness level (SOI),medical or surgical classification the median charge,
# median cost, average charge and average cost per discharge.

# The dependent variable chosen for this program is "mean_charge" - a figure, a number (in )USD),
# that represents cost to the patient. This program considers and will measure
# the variation of the mean_charge to the patient based the severity of illness and number of
# discharges the patient has undergone. 

# The issights derived from this model are these:
# (A) Intercept (coef = 6022.1398) means when all independent variables are ZERO, the mean charge is
#       about ~ $6022.14
# (B) The 'apr_severity_of_illness_code' (coef = 1.204e+04) suggests that as the severity of illness increases (increasing complexity)
#       by one unit, the mean charge increases by $12,040. The severity of illness has a strong effect on the
#       on the mean charge to the patient
# (C) Discharges (coef = 1.2955) coefficient suggests that each additional discharge increases the mean charge by
#       $1.30. This effect is not statistically significant, as indicated by a p-value of 0.965.
#       Thus, discharges don't significant impact the mean charge.
# In closing, the model does not explain much of the variance in 'mean_charge', as seen in the R-Squared
#       F-statistic. Only the 'apr_severity_of_illness_code' seems to have a significant impact on
#       'mean_charge', chile discharges do not. In order to imporve this model, one may need to include
#       additional variables to better capture the factors affecting 'mean_charge'. 
