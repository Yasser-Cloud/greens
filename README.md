# Greens

## Problem Description

Many young people struggle to distinguish between common greens like Dill, Parsley, Coriander, and Watercress, often feeling shy to ask. Misidentifying them can lead to cooking mishaps or even dietary mistakes.

Greens Classifier is here to help! 📸✨ Just snap a picture, and our model will instantly tell you what green it is. No more confusion—just fun, learning, and perfectly seasoned dishes!
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

## Install
``` shell
pip install -r requirements.txt 
```
## Run app

``` shell
docker build -t kickstart-app .
docker run -it -p 9696:9696 kickstart-app:latest
```

