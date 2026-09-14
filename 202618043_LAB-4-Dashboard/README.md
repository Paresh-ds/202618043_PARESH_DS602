# Statistics Assignment

## Deployed Application

You can access the deployed Streamlit application here:

https://202618043pareshds602-ayvtbbvfe2hyxpow9cri2q.streamlit.app

## Project Overview

This project is based on statistical analysis and understanding the relationship between different variables in a dataset.

The main purpose of this assignment is to apply statistical concepts using Python and understand how the results can be used to make conclusions from data.

The project covers data exploration, descriptive statistics, correlation, linear regression, hypothesis testing, p-values, t-statistics, confidence intervals, R², and adjusted R².

## Dataset

The dataset contains information about different observations and their related variables.

Before performing statistical analysis, the dataset is checked to understand its structure and quality.

The important steps include:

- Loading the dataset
- Checking the number of rows and columns
- Checking data types
- Checking missing values
- Checking duplicate values
- Understanding the variables
- Checking summary statistics

## Descriptive Statistics

Descriptive statistics are used to summarize and understand the data.

Some commonly used measures are:

### Mean

Mean is the average value of a variable.

It is calculated by adding all the values and dividing the total by the number of observations.

### Median

Median is the middle value when the observations are arranged in order.

It is useful when the data contains extreme values because it is less affected by outliers than the mean.

### Standard Deviation

Standard deviation shows how much the observations vary around the mean.

A higher standard deviation means the values are more spread out.

### Minimum and Maximum

Minimum represents the smallest value in the dataset.

Maximum represents the largest value in the dataset.

These values help us understand the range of the data.

## Correlation

Correlation measures the strength and direction of the relationship between two variables.

The correlation value usually ranges from -1 to +1.

A value close to +1 indicates a strong positive relationship.

A value close to -1 indicates a strong negative relationship.

A value close to 0 indicates little or no linear relationship.

Correlation does not necessarily mean that one variable causes another variable to change.

## Linear Regression

Linear Regression is used to understand the relationship between a dependent variable and one or more independent variables.

In this assignment, regression is used to understand how the input variables are related to the target variable.

The general form of a linear regression model is:

Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε

Here:

- Y is the dependent variable
- X represents the independent variables
- β₀ is the intercept
- β₁, β₂, etc. are regression coefficients
- ε represents the error

## Coefficient

A coefficient tells us how the predicted target changes when an independent variable increases by one unit, while keeping the other variables constant.

For example, if the coefficient of a variable is positive, an increase in that variable is associated with an increase in the predicted target.

If the coefficient is negative, an increase in that variable is associated with a decrease in the predicted target.

## Intercept

The intercept is the expected value of the target variable when all independent variables are equal to zero.

It is represented by β₀ in the regression equation.

The intercept is important for the mathematical model, although its practical interpretation may not always make sense if zero is outside the realistic range of the variables.

## Hypothesis Testing

Hypothesis testing is used to determine whether there is enough statistical evidence to support a particular conclusion about a population.

Two hypotheses are generally used.

### Null Hypothesis

The null hypothesis, written as H₀, represents the default assumption.

For example:

H₀: β = 0

This means that there is no linear effect of the variable on the target, after accounting for the other variables in the model.

### Alternative Hypothesis

The alternative hypothesis, written as H₁ or Hₐ, represents the conclusion we consider if the null hypothesis is rejected.

For example:

H₁: β ≠ 0

This means that there is evidence that the coefficient is different from zero.

## P-Value

The p-value helps us decide whether the observed result provides enough evidence against the null hypothesis.

A common significance level is 0.05.

If:

p-value < 0.05

we reject the null hypothesis.

If:

p-value ≥ 0.05

we fail to reject the null hypothesis.

Failing to reject H₀ does not prove that H₀ is true. It means that there is not enough statistical evidence to reject it based on the chosen significance level.

## T-Statistic

The t-statistic measures how far an estimated coefficient is from the hypothesized value relative to its standard error.

It can be represented as:

t = (Estimated coefficient - Hypothesized coefficient) / Standard Error

A larger absolute t-statistic generally provides stronger evidence against the null hypothesis.

The t-statistic is used together with the appropriate statistical distribution to obtain the p-value.

## Standard Error

Standard error measures the uncertainty in an estimated coefficient.

A smaller standard error means the coefficient has been estimated more precisely.

A larger standard error indicates greater uncertainty around the estimated coefficient.

## Confidence Interval

A confidence interval provides a range of plausible values for a population parameter based on the sample data.

For example, a 95% confidence interval gives a range calculated using a method that would capture the true parameter in about 95% of repeated samples under the assumptions of the method.

If a confidence interval for a regression coefficient does not contain zero, this is consistent with rejecting the null hypothesis β = 0 at the corresponding two-sided 5% significance level.

## R² Score

R², also called the coefficient of determination, measures how much of the variation in the dependent variable is explained by the regression model.

For example, an R² of 0.80 means the model explains approximately 80% of the variation in the target variable in the sample used to calculate the score.

A higher R² generally indicates a better fit, but R² alone should not be used to decide whether a model is statistically or practically good.

## Adjusted R²

Adjusted R² is a modified version of R² that takes the number of predictors in the model into account.

Normal R² can increase when additional variables are added, even if those variables provide very little useful information.

Adjusted R² penalizes unnecessary predictors.

Therefore, adjusted R² can be useful when comparing regression models with different numbers of independent variables.

## Residuals

A residual is the difference between the actual value and the value predicted by the regression model.

Residual:

Actual value - Predicted value

Residual analysis helps us understand whether the regression model is making systematic errors.

If the residuals show clear patterns, it may indicate that some assumptions of the regression model are not satisfied.

## Outliers

An outlier is an observation that is unusually far from most other observations.

Outliers can strongly affect statistical calculations and regression results.

Therefore, the data should be checked for unusual observations before drawing conclusions.

An outlier should not automatically be removed. It should first be investigated to determine whether it is a genuine observation or a data problem.

## Statistical Significance

A result is commonly called statistically significant when its p-value is below the selected significance level, such as 0.05.

Statistical significance means that the data provides evidence against the null hypothesis.

It does not automatically mean that the effect is large or practically important.

## Uncertainty

Uncertainty means that an estimated value from a sample is not known with complete certainty.

For example, a regression coefficient is estimated from sample data. A different sample could produce a somewhat different coefficient.

The standard error and confidence interval help us understand this uncertainty.

## Assumptions of Linear Regression

Linear regression relies on several important assumptions.

### Linearity

The relationship between the predictors and the target should be reasonably linear.

### Independence

The observations should be independent of each other.

### Homoscedasticity

The spread of residuals should be reasonably constant across the predicted values.

### Normality of Residuals

For some statistical inference procedures, residuals are assumed to be approximately normally distributed.

### No Strong Multicollinearity

The independent variables should not have extremely strong linear relationships with each other.

## Multicollinearity

Multicollinearity occurs when two or more independent variables are strongly related to each other.

It can make regression coefficients unstable and increase their standard errors.

This can make it harder to determine the individual effect of each variable.

## Interpretation of Results

The statistical results should not be interpreted only by looking at one value.

For example, when examining a regression coefficient, we can consider:

- The coefficient value
- Its direction
- Standard error
- t-statistic
- p-value
- Confidence interval

These values together provide a better understanding of the relationship between the predictor and target.

## Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Statsmodels

Scikit-learn

Streamlit

## Project Workflow

The overall workflow of the Statistics Assignment is:

1. Load the dataset
2. Understand the dataset
3. Clean the data
4. Check missing and duplicate values
5. Calculate descriptive statistics
6. Study relationships between variables
7. Calculate correlations
8. Build the linear regression model
9. Examine regression coefficients
10. Perform hypothesis testing
11. Analyze p-values and t-statistics
12. Calculate confidence intervals
13. Evaluate R² and adjusted R²
14. Analyze residuals
15. Interpret the statistical results
16. Create the Streamlit application
17. Deploy the application

## Conclusion

This assignment helped in understanding how statistical methods can be applied to real-world data.

The analysis starts with understanding the dataset and continues with descriptive statistics, correlation, regression, and hypothesis testing.

The regression results help explain the relationship between the variables, while p-values, t-statistics, confidence intervals, and standard errors help understand the uncertainty and statistical evidence behind the results.

The final analysis is presented through a Streamlit application so that the results can be accessed through a web interface.

## Deployed Application

https://202618043pareshds602-ayvtbbvfe2hyxpow9cri2q.streamlit.app