# Predicting Financial Exclusion Among Rural Youth in Kenya

## Project Description

This project develops an end-to-end machine learning workflow to predict whether rural youth in Kenya are likely to be financially excluded. It uses survey data from the FinAccess 2024 Household Survey and combines data preparation, modeling, evaluation, and deployment into a single reproducible project.

The work was built to support better decision-making for policymakers, financial institutions, and development organizations that need to identify barriers to financial inclusion. The system is designed to provide a practical starting point for understanding which factors are most associated with exclusion and how those insights can be translated into targeted interventions.

The project includes both a training pipeline and a simple web application so that predictions can be made through Python or a browser-based interface. This makes the solution useful for technical users as well as non-technical stakeholders who want to explore input profiles and review results.

## Problem Statement

Financial exclusion remains a significant issue for many rural youth in Kenya, even in a market where digital financial services have expanded rapidly. Exclusion can limit access to savings, credit, insurance, and other services that support livelihoods and economic resilience.

Understanding who is most at risk of exclusion is important for designing effective programs and policies. A predictive model can help identify patterns in the data and support more targeted outreach, product design, and public policy decisions.

## Project Objectives

- Build a reproducible classification workflow for predicting financial exclusion
- Identify the main drivers associated with exclusion among rural youth
- Provide a user-friendly way to make predictions from a trained model
- Create a project structure that is easy to understand, extend, and reproduce

## Business Understanding

The solution is intended for organizations that need to understand financial inclusion risk in a practical, data-driven way. By identifying patterns in survey data, the project can support evidence-based planning and help stakeholders focus resources where they are most needed.

The value of the solution lies in its ability to translate complex survey data into clear insights that can inform policy design, outreach campaigns, product development, and program targeting.

## Dataset

The project uses the FinAccess 2024 Household Survey dataset.

- Data source: FinAccess Kenya survey data
- Number of observations: Not fixed in the repository; depends on the local dataset used
- Number of features: Determined by the source workbook
- Target variable: Financial exclusion status
- Key input variables: County, sex, education, age, age group, employment category, internet access, mobile ownership, and digital-access-related indicators
- Data limitations: The raw workbook is large and not committed to the repository
- Data quality considerations: Missing values, inconsistent labels, and survey-specific encoding may require cleaning and validation

## Project Structure

```text
project-name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── data_loader.py
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── models/
├── reports/
├── app/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

- data/raw: Original survey files and source data
- data/processed: Cleaned and prepared datasets
- notebooks: Exploratory analysis and workflow notebooks
- src: Core training, preprocessing, evaluation, and prediction code
- models: Saved trained model artifacts
- reports: Metrics, figures, and output summaries
- app: Web application entry point and related interface logic
- tests: Automated tests for validation

## Methodology

The project follows a standard machine learning workflow:

1. Data collection from the FinAccess survey workbook
2. Data cleaning and validation of survey fields
3. Exploratory data analysis to understand patterns and data quality
4. Feature engineering to create interpretable variables for modeling
5. Data preprocessing for categorical and numeric inputs
6. Model selection across several candidate classifiers
7. Model training and evaluation on a held-out test set
8. Hyperparameter tuning for the strongest model candidate
9. Model interpretation through feature importance and output analysis
10. Model saving for reuse in prediction workflows
11. Deployment of the model through a simple web interface

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | pandas, NumPy |
| Machine Learning | scikit-learn, joblib |
| Visualization | matplotlib |
| Web App | Flask |
| Testing | pytest |
| Environment | pip, virtualenv |

## Installation

Clone the repository and install the dependencies.

```bash
git clone https://github.com/JoelKy-coder/predicting-financial-inclusion-kenya.git
cd predicting-financial-inclusion-kenya
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Prepare the data

Place the FinAccess workbook in the expected location:

```text
data/raw/2024_Finaccess_Publicdata.xlsx
```

### Train the model

```bash
python -m src.train --sample-size 2000
```

### Evaluate the model

The training script generates evaluation metrics and reports under the reports directory.

### Make predictions

```python
from src.predict import predict_exclusion

profile = {
    "county": "Kisumu",
    "Sex": "Female",
    "Education": "Secondary",
    "A20": "Secondary completed",
    "age_years": 24,
    "age_group_youth": "18-25",
    "employment_category": "self_employment",
    "internet_access": "yes",
    "owns_private_mobile": "yes",
    "S6": "Strong",
    "S7_5": "I can manage",
    "digital_access_score": 3,
}

result = predict_exclusion(profile)
print(result)
```

### Run the application

```bash
python app.py
```

Then open the app in a browser at http://127.0.0.1:5000/.

## Model Evaluation

Model performance is evaluated using accuracy, precision, recall, F1 score, and ROC AUC. These metrics help assess both overall prediction quality and the ability to identify excluded youth correctly.

The current results from the repository are:

| Metric | Score |
|---|---:|
| Accuracy | 0.8925 |
| Precision | 0.5714 |
| Recall | 0.9231 |
| F1 Score | 0.7059 |
| ROC AUC | 0.9490 |

These results indicate that the tuned random forest model performed well for the intended classification task, particularly in identifying the positive class.

## Results

The trained model shows that digital access, age-related factors, and employment context are among the strongest signals associated with financial exclusion in the sample used for this project. The results support the idea that exclusion is not driven by a single factor, but by a mix of socioeconomic and digital-access characteristics.

The project also produces visual outputs such as feature importance plots and evaluation summaries, which can be reviewed in the reports directory.

## Challenges

Several challenges are common in this type of project:

- Missing or inconsistent values in survey data
- Class imbalance between included and excluded groups
- Feature engineering based on categorical survey responses
- Risk of overfitting when working with a relatively small or imbalanced sample
- The need to avoid leakage from variables that directly describe financial access

## Future Improvements

Possible improvements include:

- Adding more data from larger or newer surveys
- Improving feature engineering and variable selection
- Exploring additional models and ensemble approaches
- Adding explainability tools such as SHAP
- Monitoring model performance after deployment
- Deploying the application to a cloud platform
- Adding CI/CD pipelines for automated testing and releases

## Policy Recommendations

The recommendations below are based on the findings of the analysis and are intended to support evidence-based decision-making. They should be interpreted alongside the project's limitations and validated with domain experts before implementation.

### Government

- Expand financial literacy programs in rural communities where financial exclusion is highest.
- Invest in digital infrastructure to improve access to mobile and online financial services.
- Develop policies that encourage financial institutions to serve underserved populations.

### Financial Institutions

- Design affordable financial products tailored to rural youth.
- Use data-driven approaches to identify communities with low levels of financial inclusion.
- Strengthen customer education on digital financial services.

### Development Partners

- Support initiatives that promote financial education and entrepreneurship among young people.
- Partner with local organizations to improve awareness of available financial services.

### Future Policy Considerations

- Conduct further studies using more recent and region-specific data.
- Monitor the impact of implemented policies through regular data collection and evaluation.
- Explore additional socioeconomic factors that may influence financial inclusion.

## Reproducibility

To reproduce the project from scratch, follow the installation steps, place the raw survey workbook in the expected data folder, run the training pipeline, and then use the resulting model artifacts for prediction or deployment.

## Contributing

Contributions are welcome. If you would like to contribute, please open an issue or submit a pull request with a clear description of the proposed changes.

## License

This project is currently licensed under the MIT License.

## Author

- Name: JoelKy-coder
- GitHub: https://github.com/JoelKy-coder
- LinkedIn: Add your profile link
- Portfolio: Add your portfolio link
- Email: Add your email address

## Acknowledgements

This project makes use of the FinAccess survey data and the open-source Python ecosystem, including pandas, scikit-learn, Flask, and matplotlib.
