#------------------------------------------------------------------------------------
# This is an iris flower classification model deployment project using flask
#------------------------------------------------------------------------------------

# Required libraries:
pandas
sklearn
flask
flask-JWT
flask-wtf
joblib
WTForms

#------------------------------------------------------------------------------------
# In Visual Studio Code activate your conda environment
#------------------------------------------------------------------------------------

CTRL+SHIFT+P -> Python select Interpreter

#------------------------------------------------------------------------------------
# Open a Terminal window and navigate to your working folder 
#------------------------------------------------------------------------------------

# e.g.: ...\flask_example_iris_model

#------------------------------------------------------------------------------------
# Run the knn model to create and save a machine learning model
#------------------------------------------------------------------------------------

python model.py

#------------------------------------------------------------------------------------
# Run the flask application
#------------------------------------------------------------------------------------

python app.py

#------------------------------------------------------------------------------------
# Access the web aplication in a web browser by using the following url
#------------------------------------------------------------------------------------

http://localhost:8080

# Now, inlude some values to predict the corresponding Iris species
# Remember that the values refer to the:
# sepal.length 
# sepal.width
# petal.length
# petal.width
# in cm of the iris flowers. 
# For example, you can use: 5, 4, 2, 1
