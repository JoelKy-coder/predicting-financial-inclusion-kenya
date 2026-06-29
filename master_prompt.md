# PROJECT PROMPT

# Predicting Barriers to Financial Inclusion Among Rural Youth in Kenya

---

# Role

Act as a Senior Machine Learning Engineer, Data Scientist, Technical Writer, and Educator.

Your task is to create a complete end-to-end Machine Learning Classification project using the **FinAccess 2024 Household Survey (Kenya)**.

The project should follow industry best practices while maintaining the educational approach used throughout Microsoft's **ML-For-Beginners** repository.

The notebook should not simply present code. Instead, it should teach the reader the complete machine learning workflow by explaining every decision, every preprocessing step, every visualization, and every model evaluation.

The finished project should be suitable for:

- GitHub Portfolio
- AI Engineer Portfolio
- Machine Learning Engineer Portfolio
- Data Scientist Portfolio

The project should resemble a real-world data science case study rather than a tutorial.

---

# Project Title

Predicting Barriers to Financial Inclusion Among Rural Youth in Kenya

---

# Executive Summary

Financial inclusion is widely recognized as an important contributor to economic development, poverty reduction, and financial resilience. Access to formal financial services enables individuals to save securely, obtain credit, insure against risks, and participate more effectively in the economy.

Kenya has become a global leader in digital financial services through innovations such as mobile money. Despite this progress, financial exclusion remains a challenge, particularly among rural youth.

This project investigates the demographic, socioeconomic, and digital factors associated with financial exclusion among rural youth aged 18–35 years using the official FinAccess 2024 Household Survey.

Machine learning classification techniques are used to predict financial exclusion and identify the variables that contribute most to exclusion. Beyond predictive performance, the project emphasizes interpretability and evidence-based recommendations that can inform financial inclusion initiatives.

---

# Business Understanding

Financial institutions, government agencies, development organizations, and policymakers require better evidence to identify populations that remain excluded from formal financial systems.

Traditional descriptive statistics provide useful insights but often fail to capture complex interactions among multiple variables.

Machine learning offers an opportunity to model these relationships and identify the characteristics most strongly associated with financial exclusion.

The findings from this project can support the design of targeted financial inclusion programs, digital financial products, and public policies aimed at increasing access to financial services among rural youth.

---

# Problem Statement

Many rural youth in Kenya continue to face barriers to accessing formal financial services despite significant growth in digital finance.

Understanding these barriers is essential for designing interventions that promote equitable access to financial services.

This project develops a binary classification model capable of predicting whether a rural youth is financially excluded using demographic, economic, and technology-related characteristics collected through the FinAccess 2024 Household Survey.

---

# Project Objectives

The project should:

- Understand the FinAccess 2024 Household Survey.
- Assess data quality.
- Clean and prepare the dataset.
- Explore relationships between variables.
- Engineer meaningful features.
- Train multiple classification models.
- Compare model performance.
- Interpret model predictions.
- Identify key predictors of financial exclusion.
- Generate policy recommendations supported by the analysis.

---

# Research Questions

The project should answer questions such as:

- Which demographic characteristics are associated with financial exclusion?
- Does education level influence financial inclusion?
- Does employment status affect access to financial services?
- Does mobile phone ownership improve financial inclusion?
- Does internet access reduce financial exclusion?
- Which variables contribute most to financial exclusion?
- Which classification model provides the best predictive performance?

---

# Machine Learning Task

Machine Learning Type:

Supervised Learning

Learning Task:

Binary Classification

Prediction Target:

Financially Included (0)

Financially Excluded (1)

---

# Dataset

Use the official FinAccess 2024 Household Survey.

Dataset Source:

https://finaccess.knbs.or.ke/reports-and-datasets

The dataset is published through the FinAccess programme, a collaboration between:

- Central Bank of Kenya (CBK)
- Kenya National Bureau of Statistics (KNBS)
- Financial Sector Deepening Kenya (FSD Kenya)

Use the provided dataset:

- 2024_Finaccess_Publicdata.xlsx
- 2024_Finaccess_Publicdata.dta

Do not invent variables or assume the dataset structure before analysis.

Always inspect the dataset before beginning preprocessing.

---

# Phase 1 — Repository Setup

Create the following repository structure.

financial-inclusion-classification/

├── data/

│ ├── raw/

│ ├── processed/

│ └── external/

├── notebooks/

├── src/

├── models/

├── reports/

│ ├── figures/

│ └── tables/

├── images/

├── docs/

├── README.md

├── PROJECT_PROMPT.md

├── requirements.txt

├── .gitignore

└── LICENSE

---

# Phase 2 — Development Environment

Use the following technologies:

Python

Jupyter Notebook

VS Code

Git

GitHub

Pandas

NumPy

Matplotlib

Scikit-learn

OpenPyXL

Joblib

Ensure:

- Reproducible environment
- Clean project structure
- Version control from the beginning
- Meaningful Git commit messages

---

# Phase 3 — Notebook Requirements

Develop the project as a professional Jupyter Notebook.

Every major section must begin with a Markdown explanation describing:

- What will be done.
- Why it is necessary.
- What readers should learn.

The notebook should flow naturally from one section to the next.

Avoid large blocks of unexplained code.

---

# Phase 4 — Code Quality

Every code cell should contain comments explaining the purpose of the code.

Example:

```python
# Import libraries for data manipulation and visualization.
import pandas as pd
import matplotlib.pyplot as plt
```

Use:

- Descriptive variable names
- Modular code
- Reusable functions
- PEP 8 conventions

Avoid:

- Duplicate code
- Magic numbers
- Hard-coded file paths

---

# Phase 5 — Dataset Inspection

Before cleaning the dataset, inspect it thoroughly.

Tasks include:

- Load the dataset.
- Display the first and last five records.
- Display the dataset dimensions.
- Display variable names.
- Display data types.
- Identify missing values.
- Identify duplicate records.
- Generate descriptive statistics.
- Identify categorical variables.
- Identify numerical variables.

Explain the purpose of each inspection step and interpret the findings before proceeding.

Do not begin preprocessing until the dataset has been fully explored.

---

# Expected Deliverables for Part 1

At the end of Part 1, the project should have:

- A professional repository structure.
- A configured development environment.
- A documented project overview.
- A clear business understanding.
- A defined machine learning problem.
- A documented dataset source.
- An initial dataset inspection notebook ready for exploratory analysis.

---

# Phase 6 — Data Quality Assessment

## Objective

Assess the quality of the FinAccess 2024 Household Survey before any preprocessing or modeling begins.

A thorough understanding of the dataset helps identify issues that may affect model performance and ensures that preprocessing decisions are based on evidence rather than assumptions.

## Tasks

Perform a comprehensive data quality assessment by examining:

- Missing values
- Duplicate records
- Invalid values
- Inconsistent data types
- Unique values for categorical variables
- Distribution of numerical variables
- Potential outliers
- Class imbalance (if the target variable already exists)

For each issue identified:

- Describe the problem.
- Explain its potential impact.
- Justify the chosen solution.

Do not remove or modify data without providing a clear explanation.

---

# Phase 7 — Data Cleaning

## Objective

Prepare the dataset for analysis while preserving as much meaningful information as possible.

## Tasks

Clean the dataset by:

- Handling missing values appropriately.
- Removing duplicate records.
- Correcting inconsistent entries.
- Standardizing categorical variables.
- Converting variables to appropriate data types.
- Renaming variables where necessary to improve readability.

Avoid removing records unless there is a clear justification.

Document every cleaning decision.

---

# Phase 8 — Creating a Data Dictionary

## Objective

Help readers understand the dataset before analysis begins.

## Tasks

Create a data dictionary that includes:

| Variable | Description | Data Type | Role |
|----------|-------------|-----------|------|
| Variable Name | Plain-language explanation | Numerical/Categorical | Predictor or Target |

Use the actual variable names from the FinAccess dataset.

Avoid inventing variables.

Where variable labels are unclear, explain them using the official survey documentation.

---

# Phase 9 — Exploratory Data Analysis (EDA)

## Objective

Understand the characteristics of the dataset and identify patterns that may influence financial inclusion.

The purpose of EDA is not simply to generate charts but to develop insights that guide feature selection and model development.

## Questions to Explore

Investigate questions such as:

- What is the age distribution of respondents?
- What proportion of respondents are rural youth?
- What is the distribution of education levels?
- How does employment status vary?
- How many respondents own mobile phones?
- What proportion have internet access?
- What financial services are most commonly used?
- Are there regional differences across counties?

---

# Univariate Analysis

Investigate individual variables using appropriate visualizations.

Possible visualizations include:

- Histograms
- Bar charts
- Count plots
- Pie charts (only when appropriate)
- Box plots

For every visualization:

Explain:

- What is being shown.
- Why it matters.
- What patterns are observed.
- How the findings relate to financial inclusion.

---

# Bivariate Analysis

Investigate relationships between two variables.

Examples include:

- Education vs Financial Inclusion
- Employment vs Financial Inclusion
- Gender vs Financial Inclusion
- County vs Financial Inclusion
- Mobile Phone Ownership vs Financial Inclusion
- Internet Access vs Financial Inclusion

Possible visualizations include:

- Grouped bar charts
- Stacked bar charts
- Box plots
- Cross-tabulations

Interpret every result.

---

# Multivariate Analysis

Explore relationships involving multiple variables.

Possible analyses include:

- Correlation Heatmap
- Pairwise relationships
- Crosstab summaries
- Grouped statistical summaries

Discuss how multiple variables interact to influence financial inclusion.

---

# Phase 10 — Statistical Analysis

## Objective

Complement exploratory analysis with descriptive statistics.

Calculate:

- Mean
- Median
- Mode
- Standard deviation
- Minimum
- Maximum
- Quartiles

Where appropriate, compare statistics across:

- Gender
- Education level
- County
- Employment status
- Financial inclusion groups

Explain what these statistics reveal.

Avoid reporting numbers without interpretation.

---

# Phase 11 — Feature Engineering

## Objective

Improve the predictive power of the dataset by creating meaningful features.

Only engineer features when they add value.

Possible engineered features may include:

- Age Group
- Income Category
- Digital Access Score
- Financial Service Usage Score
- Employment Category

Use actual variables from the dataset to derive new features.

Explain:

- Why the feature was created.
- How it was constructed.
- Why it may improve prediction.

---

# Phase 12 — Feature Selection

## Objective

Select variables that contribute meaningfully to predicting financial exclusion.

Avoid including variables that:

- Leak target information.
- Have little predictive value.
- Introduce redundancy.

Use methods such as:

- Correlation analysis
- Feature importance
- Domain knowledge
- Variance analysis

Explain why each selected feature is retained.

---

# Phase 13 — Target Variable Preparation

## Objective

Prepare the target variable for binary classification.

Inspect the dataset to determine whether a financial inclusion indicator already exists.

If one exists:

Use it directly.

If not:

Create a binary target variable using financial access indicators from the survey.

Document:

- Variables used
- Logic applied
- Assumptions made

Example:

| Target Value | Meaning |
|--------------|---------|
| 0 | Financially Included |
| 1 | Financially Excluded |

Clearly explain why this formulation is appropriate.

---

# Phase 14 — Data Preprocessing

## Objective

Prepare the cleaned dataset for machine learning.

Tasks include:

- Encoding categorical variables.
- Scaling numerical variables where appropriate.
- Splitting predictors and target.
- Handling class imbalance if necessary.
- Creating training and testing datasets.

Explain:

- Why categorical encoding is necessary.
- When scaling should be applied.
- Why train-test splitting prevents overfitting.

---

# Train-Test Split

Split the dataset into:

- Training Set (80%)
- Testing Set (20%)

Use:

- Random state for reproducibility.
- Stratified sampling where appropriate.

Explain why stratification may improve model evaluation.

---

# Data Leakage Prevention

Prevent leakage throughout preprocessing.

Do not:

- Fit preprocessing steps using the entire dataset.
- Scale the test set before splitting.
- Use future information when creating features.

Clearly explain why preventing data leakage is essential for building trustworthy machine learning models.

---

# Notebook Requirements

Every section must begin with a Markdown explanation covering:

- What is being done.
- Why it is necessary.
- Expected learning outcomes.

After every visualization:

Interpret the results.

Avoid displaying charts without discussion.

After every preprocessing step:

Explain:

- Why the step was performed.
- What effect it has on the dataset.
- Whether it could influence model performance.

---

# Expected Deliverables for Part 2

By the end of this phase, the project should include:

- A cleaned dataset.
- A documented data dictionary.
- Comprehensive exploratory data analysis.
- Statistical summaries.
- Engineered features.
- Selected predictor variables.
- A prepared target variable.
- Training and testing datasets ready for machine learning.

---

# Phase 15 — Machine Learning Model Development

## Objective

Develop multiple supervised machine learning models capable of predicting financial exclusion among rural youth in Kenya.

Rather than selecting a single algorithm immediately, train several classification models and compare their performance to determine the most suitable model for this problem.

The objective is to understand how different algorithms behave on the same dataset and identify the model that provides the best balance between predictive performance and interpretability.

---

# Machine Learning Workflow

Follow this sequence for every model:

1. Introduce the algorithm.
2. Explain why it was selected.
3. Describe how it works conceptually.
4. Train the model.
5. Make predictions.
6. Evaluate performance.
7. Interpret the results.
8. Discuss strengths and weaknesses.

Do not simply train the model and report metrics.

Teach the reader throughout the process.

---

# Phase 16 — Baseline Model

## Objective

Establish a simple benchmark before training more complex models.

Begin with Logistic Regression as the baseline model.

Explain:

- Why baseline models are important.
- How future models will be compared against it.
- Why a simple model should always be evaluated first.

---

# Logistic Regression

## Objective

Train a Logistic Regression classifier.

Explain:

- What Logistic Regression is.
- Why it is appropriate for binary classification.
- How probabilities are converted into class predictions.
- Advantages.
- Limitations.

Train the model using the training dataset.

Generate predictions on the testing dataset.

Evaluate using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Interpret every evaluation metric.

Explain whether Logistic Regression performs well for this problem.

---

# Phase 17 — Decision Tree Classifier

## Objective

Train a Decision Tree classifier.

Explain:

- Decision Trees split data into decision rules.
- How information gain works.
- Tree depth.
- Overfitting.
- Pruning.

Train the model.

Generate predictions.

Evaluate using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Interpret the results.

Compare performance against Logistic Regression.

---

# Visualizing the Decision Tree

Visualize the trained tree.

Explain:

- Root node
- Decision nodes
- Leaf nodes

Interpret how the model makes predictions.

Discuss whether the tree appears overly complex.

---

# Phase 18 — Random Forest Classifier

## Objective

Train a Random Forest classifier.

Explain:

- Ensemble learning
- Bootstrap sampling
- Random feature selection
- Majority voting

Discuss why Random Forest often performs better than a single Decision Tree.

Train the model.

Generate predictions.

Evaluate using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Interpret the findings.

Compare with:

- Logistic Regression
- Decision Tree

---

# Feature Importance

Extract feature importance from the Random Forest model.

Rank variables according to importance.

Visualize feature importance using a horizontal bar chart.

Interpret:

- Which variables matter most.
- Why these variables may influence financial inclusion.
- How the findings relate to the Kenyan context.

Avoid simply displaying rankings.

Provide thoughtful interpretation.

---

# Phase 19 — Support Vector Machine (SVM)

## Objective

Train a Support Vector Machine classifier.

Explain:

- Hyperplane
- Margin
- Support vectors
- Kernel functions

Discuss:

Advantages

Limitations

Computational cost

Train the classifier.

Generate predictions.

Evaluate using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Interpret results.

Compare performance with previous models.

---

# Phase 20 — Hyperparameter Tuning

## Objective

Improve model performance through systematic hyperparameter optimization.

Explain:

- Why default parameters are rarely optimal.
- What hyperparameters control.

Use:

GridSearchCV

or

RandomizedSearchCV

Tune appropriate parameters for:

Decision Tree

Random Forest

Support Vector Machine

Explain every parameter being tuned.

Avoid blindly searching large parameter spaces.

---

# Cross Validation

Use k-fold cross-validation.

Recommended:

5-fold

or

10-fold

Explain:

- Why cross-validation is useful.
- How it estimates generalization performance.
- Why relying on one train-test split may be misleading.

Report:

- Mean Accuracy
- Standard Deviation

Interpret the results.

---

# Phase 21 — Model Evaluation

Evaluate every trained model using the same metrics.

Include:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Classification Report

Present results in a comparison table.

Example:

| Model | Accuracy | Precision | Recall | F1 Score |
|--------|----------|-----------|--------|----------|

Interpret the table.

Explain why one model performs better.

---

# Confusion Matrix Interpretation

For every model:

Interpret:

True Positives

True Negatives

False Positives

False Negatives

Discuss the practical implications.

Example:

False negatives may represent financially excluded youth incorrectly predicted as financially included.

Explain why this matters.

---

# Classification Report

Interpret:

Precision

Recall

F1 Score

Support

Avoid simply printing the report.

Explain what the numbers mean.

---

# ROC Curve

Generate ROC Curves.

Compare all models.

Compute:

AUC Score

Interpret:

- Higher AUC
- Lower AUC

Explain what ROC curves reveal about classifier performance.

---

# Precision-Recall Curve

If classes are imbalanced:

Generate Precision-Recall curves.

Explain why these may be more informative than ROC curves.

---

# Phase 22 — Model Comparison

Compare all trained models.

Discuss:

Prediction accuracy

Interpretability

Training time

Complexity

Robustness

Suitability for policy applications

Do not select a model based only on Accuracy.

Discuss trade-offs.

---

# Model Selection

Choose the final model.

Provide a detailed justification based on:

Evaluation metrics

Cross-validation

Feature importance

Generalization ability

Interpretability

Business context

Explain why the chosen model is the most appropriate.

---

# Model Persistence

Save the best-performing model.

Use:

Joblib

or

Pickle

Explain:

Why models are saved.

How they can be reused.

Document:

Model version

Training date

Parameters

---

# Prediction Pipeline

Create a reusable prediction pipeline.

Pipeline should include:

Preprocessing

Encoding

Scaling

Prediction

Probability estimation

The pipeline should be reusable for new survey responses.

---

# Notebook Requirements

Every model section should include:

Markdown introduction

Algorithm explanation

Training code

Evaluation

Interpretation

Comparison

Reflection

---

# Code Requirements

Every code cell should include meaningful comments.

Example:

```python
# Train the Random Forest classifier using the prepared training dataset.
```

Explain:

Why each step is performed.

Avoid comments that merely restate the code.

---

# Expected Deliverables for Part 3

By the end of this phase, the project should include:

- Baseline Logistic Regression model
- Decision Tree model
- Random Forest model
- Support Vector Machine model
- Hyperparameter tuning
- Cross-validation results
- Model comparison table
- ROC Curve
- Precision-Recall Curve
- Feature Importance visualization
- Saved best-performing model
- Reusable prediction pipeline

---

# Phase 23 — Model Interpretation

## Objective

Move beyond model performance by understanding **why** the model makes its predictions.

A good machine learning model should not only predict accurately but should also provide insights that stakeholders can understand and trust.

The goal of this phase is to explain the factors associated with financial exclusion among rural youth in Kenya using interpretable machine learning techniques.

---

# Feature Importance Analysis

## Objective

Determine which variables contribute most to predicting financial exclusion.

Use feature importance methods appropriate for the selected model.

Examples include:

- Random Forest Feature Importance
- Permutation Importance
- Model Coefficients (Logistic Regression)

Present the results using clear visualizations.

For every important feature:

Explain:

- Why the feature is influential.
- Whether the relationship aligns with expectations.
- How it relates to financial inclusion in Kenya.

Avoid simply listing variables.

Interpret every finding in context.

---

# Model Explainability

Where appropriate, use SHAP (SHapley Additive Explanations) to explain model predictions.

Explain:

- What SHAP values represent.
- Why explainability matters.
- How individual features increase or decrease the probability of financial exclusion.

Create:

- SHAP Summary Plot
- SHAP Bar Plot
- SHAP Force Plot (optional)

Interpret each visualization.

If SHAP is not suitable for the selected model, explain why and use an alternative interpretability method.

---

# Scenario Analysis

Create several hypothetical profiles using realistic examples from the Kenyan context.

Example profiles may include:

### Profile 1

- Rural
- Female
- Age 22
- Primary education
- Unemployed
- No mobile phone
- No internet access

Predict:

- Financial inclusion status
- Probability of exclusion

Explain why the model produced this prediction.

---

### Profile 2

- Rural
- Male
- Age 29
- Secondary education
- Self-employed
- Owns a smartphone
- Uses M-Pesa regularly

Interpret the prediction.

---

### Profile 3

- Rural
- Female
- Age 34
- College education
- Formally employed
- Internet access
- Uses digital banking

Interpret the prediction.

Discuss how changes in socioeconomic characteristics influence predictions.

---

# Phase 24 — Findings

## Objective

Summarize the most important insights discovered during the project.

Discuss findings such as:

- Which factors contribute most to financial exclusion.
- The relationship between education and financial inclusion.
- The influence of employment status.
- The importance of digital access.
- Regional differences.
- Mobile money usage.
- Household income.

Support every finding with evidence from the analysis.

Avoid making unsupported claims.

---

# Phase 25 — Policy Recommendations

## Objective

Translate machine learning findings into practical recommendations.

Recommendations should be directly supported by the analysis.

---

## Government

Examples:

- Expand digital infrastructure in underserved rural communities.
- Increase financial literacy programmes for young adults.
- Support youth employment initiatives.
- Improve access to identification documents where they remain a barrier.

Explain how each recommendation relates to the model findings.

---

## Commercial Banks

Recommend strategies such as:

- Youth-friendly savings accounts.
- Simplified onboarding.
- Rural banking outreach.
- Low-cost digital banking services.

---

## SACCOs

Recommend:

- Youth savings programmes.
- Financial education.
- Community outreach.

---

## Mobile Money Providers

Recommend:

- Affordable digital financial products.
- Improved rural network coverage.
- Digital literacy campaigns.

---

## Development Organizations

Recommend:

- Targeted financial inclusion programmes.
- Capacity building.
- Community-based interventions.

Ensure every recommendation is evidence-based.

---

# Phase 26 — Ethical Considerations

## Objective

Discuss responsible use of machine learning.

Topics should include:

- Privacy
- Fairness
- Transparency
- Accountability
- Responsible AI

Discuss whether certain demographic groups may be disproportionately affected by prediction errors.

Explain why human oversight remains important.

---

# Bias Assessment

Investigate whether the model performs differently across groups such as:

- Gender
- County
- Education level
- Employment status

Discuss:

Potential sources of bias.

Possible mitigation strategies.

Limitations of the available data.

---

# Phase 27 — Limitations

Every project has limitations.

Discuss limitations including:

- Sample representation.
- Missing variables.
- Survey design.
- Cross-sectional nature of the data.
- Generalizability.
- Class imbalance.
- Measurement error.

Explain how these limitations affect interpretation.

Avoid overstating conclusions.

---

# Phase 28 — Future Work

Discuss possible extensions such as:

- Testing additional algorithms.
- Gradient Boosting.
- XGBoost.
- LightGBM.
- CatBoost.
- Deep Learning.

Investigate:

- Time-series financial inclusion trends.
- County-level prediction models.
- Multi-class classification.
- Recommendation systems.
- Interactive dashboards.

Explain why these could improve future research.

---

# Phase 29 — Conclusion

Write a professional conclusion summarizing:

- Problem addressed.
- Dataset used.
- Machine learning workflow.
- Best-performing model.
- Key predictors.
- Policy implications.

The conclusion should read like the closing section of an academic case study.

Avoid repeating previous sections.

---

# Phase 30 — Project Documentation

Produce professional documentation including:

- README.md
- requirements.txt
- .gitignore
- LICENSE (MIT)

Document:

Project purpose.

Installation.

Dataset.

Repository structure.

How to reproduce results.

Dependencies.

Model files.

Usage instructions.

References.

Acknowledgements.

---

# README Requirements

The README should include:

- Project title
- Overview
- Background
- Problem Statement
- Objectives
- Dataset
- Repository Structure
- Installation
- Usage
- Machine Learning Workflow
- Results
- Feature Importance
- Policy Recommendations
- Future Work
- References
- License
- Author

Write the README as though it were for an open-source GitHub repository.

---

# Reproducibility

Ensure the project can be reproduced from scratch.

Include:

- Random seeds
- Python version
- Package versions
- Installation instructions
- Environment setup

A new user should be able to clone the repository and reproduce the results without additional guidance.

---

# Code Standards

All Python code should:

- Follow PEP 8.
- Include docstrings for reusable functions.
- Use descriptive variable names.
- Include meaningful comments.
- Handle exceptions where appropriate.
- Avoid duplicated code.
- Be modular and maintainable.

---

# Notebook Standards

Every notebook section should begin with a Markdown explanation describing:

- What is being done.
- Why it is necessary.
- What the reader should learn.

Every visualization should be interpreted.

Every model evaluation should be explained in plain language.

Every preprocessing decision should be justified.

The notebook should read like a guided case study rather than a collection of code cells.

---

# References

Use and cite authoritative sources throughout the project.

Include:

- FinAccess Kenya Reports and Datasets  
  https://finaccess.knbs.or.ke/reports-and-datasets

- FinAccess 2024 Household Survey Report

- Central Bank of Kenya (CBK)

- Kenya National Bureau of Statistics (KNBS)

- Financial Sector Deepening Kenya (FSD Kenya)

- Microsoft ML-For-Beginners

- Scikit-learn Documentation

- Pandas Documentation

- NumPy Documentation

- Matplotlib Documentation

---

# Final Project Checklist

Before completing the project, verify that:

- Repository structure is complete.
- Dataset source is documented.
- Data quality assessment is complete.
- Exploratory Data Analysis is comprehensive.
- Features are selected and justified.
- Target variable is documented.
- Multiple classification models are trained.
- Hyperparameter tuning is completed.
- Cross-validation is performed.
- Models are compared fairly.
- Evaluation metrics are interpreted.
- Feature importance is explained.
- Policy recommendations are evidence-based.
- Ethical considerations are discussed.
- Limitations are acknowledged.
- Future work is identified.
- README is complete.
- Code follows PEP 8.
- Notebook is fully documented.
- All code cells contain meaningful comments.
- Results are reproducible.
- References are properly cited.

---

# Expected Deliverables for Part 4

By the end of this phase, the project should include:

- Model interpretation and explainability.
- Feature importance analysis.
- Scenario-based predictions.
- Evidence-based findings.
- Policy recommendations for key stakeholders.
- Ethical considerations and bias assessment.
- Project limitations.
- Future work.
- Professional project documentation.
- GitHub-ready README.
- Reproducible repository with complete supporting files.

---

# Final Writing Style

The completed project should read like a professional machine learning case study developed for a real-world policy problem.

Keep the writing:

- Clear
- Professional
- Educational
- Evidence-based
- Well-structured

Avoid:

- Buzzwords
- Marketing language
- Overstated claims
- Unnecessary technical jargon
- Emojis

The final repository should demonstrate a complete end-to-end binary classification workflow using the official **FinAccess 2024 Household Survey** and showcase how machine learning can be used to understand barriers to financial inclusion among rural youth in Kenya while producing actionable insights for policymakers and financial service providers.

---

# Phase 31 — Production-Ready Repository

## Objective

Transform the project from a machine learning notebook into a professional, production-quality GitHub repository.

The repository should be organized, documented, reproducible, and easy for others to understand and contribute to.

---

# Repository Structure

The repository should follow the structure below.

```text
financial-inclusion-classification/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── python-ci.yml
│   └── pull_request_template.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_development.ipynb
│   ├── 06_model_evaluation.ipynb
│   └── 07_conclusion.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── visualization.py
│   └── utils.py
│
├── models/
│
├── reports/
│   ├── figures/
│   └── tables/
│
├── docs/
│
├── tests/
│
├── README.md
├── PROJECT_PROMPT.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── .gitignore
└── pyproject.toml
```

---

# Phase 32 — Documentation Standards

## Objective

Ensure that every part of the repository is properly documented.

Documentation should help another developer reproduce, understand, and extend the project without additional explanations.

Every notebook should contain:

- Introduction
- Objectives
- Methodology
- Interpretation
- Summary

Every Python module should contain:

- Module docstring
- Function docstrings
- Type hints
- Comments where necessary

---

# Phase 33 — README Requirements

Create a professional README.md suitable for GitHub.

Include:

# Project Title

# Background

Explain:

- Financial Inclusion
- Rural Youth
- Kenya
- FinAccess 2024

# Problem Statement

# Project Objectives

# Dataset

Include:

Dataset Source

Official FinAccess Kenya website

Dataset description

Variables

Target variable

Project workflow

Repository structure

Installation

Usage

Model comparison

Results

Key findings

Policy recommendations

Limitations

Future work

License

Acknowledgements

Author

---

# Phase 34 — Code Quality

Ensure all Python code follows professional software engineering standards.

Requirements:

PEP 8 compliant

Type hints

Docstrings

Reusable functions

Exception handling

Logging

No duplicated code

Readable variable names

Modular design

Reusable utilities

---

# Phase 35 — Testing

Create a testing strategy.

Use:

pytest

Tests should verify:

Data loading

Preprocessing

Feature engineering

Prediction pipeline

Model loading

Model prediction

Utility functions

Explain why testing improves software reliability.

---

# Phase 36 — Reproducibility

The project must be reproducible.

Include:

Python version

Package versions

requirements.txt

environment.yml

Random seeds

Installation guide

Execution order

Expected outputs

Anyone cloning the repository should obtain similar results.

---

# Phase 37 — Version Control

Follow Git best practices.

Examples of commits:

Initial project structure

Load FinAccess dataset

Complete exploratory analysis

Train Logistic Regression

Train Random Forest

Model comparison

Update documentation

Avoid generic commit messages.

---

# Phase 38 — GitHub Actions

Create a GitHub Actions workflow.

Automate:

Install dependencies

Run tests

Run linting

Verify notebook execution (optional)

The workflow should fail if tests fail.

---

# Phase 39 — Code Formatting

Use:

black

isort

flake8

Explain why consistent formatting improves maintainability.

---

# Phase 40 — Project Milestones

Plan the project using milestones.

Milestone 1

Repository setup

Milestone 2

Data understanding

Milestone 3

Exploratory analysis

Milestone 4

Feature engineering

Milestone 5

Model development

Milestone 6

Evaluation

Milestone 7

Documentation

Milestone 8

Publication

---

# Phase 41 — Portfolio Presentation

The repository should demonstrate:

Machine Learning

Python

Data Cleaning

Feature Engineering

EDA

Visualization

Classification

Model Evaluation

Documentation

Git

GitHub

Software Engineering

Professional Communication

The project should clearly communicate both technical ability and problem-solving skills.

---

# Phase 42 — Writing Standards

Throughout the project:

Use professional language.

Explain concepts clearly.

Avoid unnecessary jargon.

Avoid exaggerated claims.

Avoid unsupported conclusions.

Every claim should be supported by:

Data

Visualizations

Evaluation metrics

Feature importance

Survey evidence

---

# Phase 43 — Final Quality Review

Before publishing the repository verify:

Repository is organized.

Notebook runs from start to finish.

No missing files.

No broken imports.

No hidden errors.

Visualizations render correctly.

README is complete.

References are cited.

Results are reproducible.

Code is documented.

Notebook explanations are clear.

Policy recommendations are evidence-based.

---

# Phase 44 — Publication Checklist

Before pushing to GitHub:

Remove temporary files.

Clear notebook outputs if appropriate.

Verify file paths.

Check .gitignore.

Verify requirements.txt.

Confirm LICENSE.

Confirm README.

Confirm dataset documentation.

Review notebook spelling and grammar.

Run the notebook from a clean environment.

Commit changes.

Push to GitHub.

---

# Phase 45 — Reflection

Conclude the project with a reflective section.

Discuss:

What was learned.

Challenges encountered.

How they were addressed.

Skills developed.

Lessons for future projects.

Future improvements.

The reflection should be honest, thoughtful, and grounded in the work completed.

---

# Final Deliverables

The completed repository should contain:

- Professional README.md
- PROJECT_PROMPT.md
- Fully documented Jupyter Notebook(s)
- Clean and reproducible Python code
- Trained machine learning model
- Saved model artifacts
- Data preprocessing pipeline
- Evaluation report
- Feature importance analysis
- Publication-quality visualizations
- Policy recommendations
- requirements.txt
- environment.yml
- .gitignore
- MIT LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- GitHub Actions workflow
- Unit tests
- Complete project documentation

---

# Success Criteria

The project will be considered complete when it:

- Uses the official FinAccess 2024 Household Survey.
- Implements an end-to-end binary classification workflow.
- Compares multiple classification algorithms.
- Produces interpretable and reproducible results.
- Provides evidence-based policy recommendations.
- Demonstrates strong software engineering practices.
- Meets Microsoft ML-For-Beginners educational standards.
- Is suitable for a professional GitHub portfolio targeting Machine Learning Engineer, AI Engineer, and Data Scientist roles.

---

# Final Instruction to the AI

Build this project as though it were being developed for publication in a professional GitHub portfolio.

Every notebook, script, visualization, table, explanation, and document should contribute to a cohesive, reproducible, and well-documented machine learning case study.

Focus on clarity, technical accuracy, reproducibility, and practical insights. Do not invent dataset variables or results. Base all analysis on the actual FinAccess 2024 Household Survey, document every assumption, and ensure conclusions are supported by the evidence produced throughout the project.