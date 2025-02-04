# greens

## Problem Description:

This project analyzes Kickstarter data to help aspiring entrepreneurs and creators successfully launch their projects or startups. It provides valuable insights into what makes a campaign successful, offering guidance on effective marketing strategies and practical recommendations for optimizing campaigns. By understanding key factors like funding goals, campaign duration, and timing, this project empowers users to make informed decisions and maximize their chances of achieving their goals.
## Objective:

Build a machine learning model to predict campaign success, explore key success factors, and provide actionable insights for creators.

## About data

The dataset used in this project is available on Kaggle: [Projects Dataset](https://www.kaggle.com/datasets/mahmoudyasser/green-herbs)
follow the notebook steps to download and discovery
```shell
pip install kaggle


```
Obtain Kaggle API Credentials:

``` shell
1- Log in to your Kaggle account.
2- Go to My Account and scroll to the API section.
3- Click Create New API Token to download the kaggle.json file.

```
Copy your kaggle.json to the project path
``` shell
chmod 600 kaggle.json
kaggle datasets download -d mahmoudyasser/green-herbs
unzip green-herbs.zip
```

## Run app

``` shell
docker build -t kickstart-app .
docker run -it -p 9696:9696 kickstart-app:latest
```

