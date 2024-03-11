# Churn-App
An App that will predict if customers will churn at IBM
BUILD APP MACHINE LEARNING WITH Streamlit
Once you create an ML model, the next step is to deploy and share it to use further. If your want ML model to do real time predictions and work as a web-app, then you have couple of options to deploy your model on the web, ranging from full stack frameworks like Pyramid and Django to lightweight services like Flask and FastAPI to specialized web app framework for data science applications like Streamlit.

Exporting Machine Learning Models:

After training, evaluating and testing the models we will first export our model.

There are two possibilities for this, either with Pickle or Joblib.

We will use Joblib.

After installing Joblib we will export our models by creating a dictionary where we include the models scaler numerical inputs and category type inputs.

Then we’re going to do a dump.

Let’s practice

Import librairies

Now create variable and Load the model ,scaler numerical_imputer and categorical_imputer

Add title and subtitle ,load image et setup the layout with 2 columns

Now create input fields

Create a button to make prediction and convert our data to dataframe

Selecting the categorical and numerical columns

Now encode the categoricial columns ,scale the numerical columns and joining

Now make predictn to click on button predict

for more check my Medium: [https://medium.com/@carondemui/build-app-machine-learning-with-streamlit-7cbc2b63f72d](https://medium.com/@carondemui/build-app-machine-learning-with-streamlit-7cbc2b63f72d)https://medium.com/@carondemui/build-app-machine-learning-with-streamlit-7cbc2b63f72d
