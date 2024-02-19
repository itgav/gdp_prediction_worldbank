# Goal

- PROJECT: Configure API pulls to various demographic (related) data sources, do some exploratory EDA, and trying to predict GDP using machine learning.
- PERSONAL: Get more confortable with ML and the project workflow.
  - This project is not meant to actually predict GDP lol

### ML Problem

- Predict t+1 GDP per Capita (quantitative)
- The data:
  - large number of features
  - small number of rows

### Steps

1. `get data.ipynb`: download the datapoints for each country from WorldBank's API and export data to a `csv`
2. `preprocess data.ipynb`: format data and filter out some features
3. `model selection.ipynb`: test various models' prediction error

### Takeaways

- Part of ML is art, another part is just testing algos to see which works best and for what
- Two next projects:
  - datasets for testing: downloaded data and synthetic data generation with varying types of data and distributions
  - framework to plug in a model and test against various data types and distributions to evaluate strengths and limitations of models
    - goal: have an easy to plug into framework for baseline testing models on datasets, which should be beneficial for future ML projects from a knowledge and model selection perspective
