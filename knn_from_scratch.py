# -*- coding: utf-8 -*-
"""KNN_from_Scratch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YeD-PgtK3WaDRgqQWTJc42YORblDHtSz

**Pseudo Code for KNN**

•	Import all libraries
•	Load the dataset and split it into training and testing sets (20% test, 80% training). Please refer to the *figure 1 of the drawio file* to get a rough estimate of plotted train points on graph
•	Pre-process the dataset to remove outliers, null, missing and duplicate values
•	Extract the features and labels from both testing and training sets
•	Define functions to find Euclidean_Distance, most_repeated_class, compare_prediction, calculate_accuracy and KNN
•	Set the value of k (this will tell the k number of closest neighbors we are going to consider later)
•	Using KNN function, take a data point from test set and iterate it over the whole train set
•	Calculate the Euclidean Distance of test data point with each train data point using Euclidean_Distance function
•	Store the result in an array. This will give the k number of points which are closest to test point. Please refer to the *drawio and view figure 2.*
•	Extract the class that repeated the most using most_repeated_class function.
•	Keep iterating until there left no more train data points
•	Keep repeating the above steps for each data in testing dataset
•	Store the result in an array i.e. prediction
•	Run the model and get the prediction for all test cases and store them in array i.e. prediction
•	Compare it with the y_test that contains labels of test points and get result array using compare_prediction function
•	The above function will return number of correct predictions which will be used in calculate_accuracy function to get the accuracy rate of the model
"""

import pandas as pd                           #importing libraries
import numpy as np
import matplotlib.pyplot as plt
from google.colab import drive
import math
from collections import Counter

drive.mount('/content/drive', force_remount = True)          # mouting to my drive
iris_directory = '/content/drive/MyDrive/irisData/iris.data' # storing the file directory in iris_dictionary

dataset = pd.read_csv(iris_directory, header= None)                         # now reading the dataset from the directory
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
dataset.columns = column_names

# data pre-processing to remove/handle missing/null/duplicate values if any

    dataset.dropna()  # remove all the missing values and return the new series

    #check for null values

    if dataset.isnull().values.any():
        print("The dataset contains null values.")
    else:
        print("The dataset does not contain null values.")

    #check for duplicates

    dataset.drop_duplicates()

    if dataset.duplicated().any():
          print("The dataset contains duplicate values.")
    else:
        print("The dataset does not contain duplicate values.")

    # data visualization

    # print the whole file
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(dataset)

    # print max number of rows and columns
    # num_rows = dataset.shape[0]
    # num_columns = dataset.shape[1]

    # print("Number of rows:", num_rows)
    # print("Number of columns:", num_columns)

# Separate the data based on labels
setosa_data = dataset[dataset['class'] == 'Iris-setosa']
versicolor_data = dataset[dataset['class'] == 'Iris-versicolor']
virginica_data = dataset[dataset['class'] == 'Iris-virginica']

# Plot the data
plt.scatter(setosa_data['sepal_length'], setosa_data['sepal_width'], c='red', label='Iris-setosa')
plt.scatter(versicolor_data['sepal_length'], versicolor_data['sepal_width'], c='green', label='Iris-versicolor')
plt.scatter(virginica_data['sepal_length'], virginica_data['sepal_width'], c='blue', label='Iris-virginica')

# Set the labels and title
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset')

# Show the legend
plt.legend()

# Show the plot
plt.show()

test_size = int(len(dataset) * 0.2)

# Split the dataset into training and testing sets
train_data = dataset[test_size:]
test_data = dataset[:test_size]

# print("training sets")
# print(train_data)

# print("testing sets")
# print(test_data)


# extracting features and labels for both test and train dataset
X_train = train_data.iloc[:, :-1].values
y_train = train_data.iloc[:, -1].values
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# print("training sets")
# print("FEATURES")
# print(X_train)
# print("-------------------------------------------------")
# print("LABELS")
# print(y_train)
# print("-------------------------------------------------")

# print("testing sets")
# print("FEATURES")
# print(X_test)
# print("-------------------------------------------------")
# print("LABELS")
# print(y_test)

# Euclidean Distance function
def Euclidean_Distance(point1, point2):
    squared_diff = 0
    for i in range(len(point1)):
        squared_diff += (point1[i] - point2[i]) ** 2
    distance = math.sqrt(squared_diff)
    return distance

# function to find the most repeated class from the top k tuples
def most_repeated_class(my_tuple):
    string_count = {}
    for item in my_tuple:
        if item[1] in string_count:
            string_count[item[1]] += 1
        else:
            string_count[item[1]] = 1
    max_string = max(string_count, key=string_count.get)
    return max_string

# function to find the correct prediction. the function returns a bool array of predictions
def compare_predictions(predicted_outputs, y_test):
    accuracy_array = [predicted == actual for predicted, actual in zip(predicted_outputs, y_test)]
    return accuracy_array

# function to calculate the accuracy
def calculate_accuracy(predictions):
  total_tests = len(predictions)
  correct_predictions = sum(predictions)
  # print(correct_predictions)
  accuracy = (correct_predictions / total_tests)
  return accuracy

# K nearest neighbor algorithm
def KNN(X_train, y_train, X_test, k):

    final_output = []
    for i in range(len(X_test)):
        distances = []
        for j in range(len(X_train)):

            dis = Euclidean_Distance(X_test[i], X_train[j])
            distances.append((dis, y_train[j]))  # Append as a tuple

        distances = tuple(sorted(distances))
        # print(distances)
        distances = distances[0:k]
        # print(distances)
        result = most_repeated_class(distances)
        # print(result)
        final_output.append(result)

    # print(final_output)
    return final_output

# training the model
k = 3
predicted_outputs = KNN(X_train, y_train, X_test, k)
print(predicted_outputs)

predicted_outputs == y_test
accuracy_array = compare_predictions(predicted_outputs, y_test)
print(accuracy_array)
print(type(accuracy_array))

calculate_accuracy(accuracy_array)

class_array = np.array(accuracy_array)
print(type(class_array))
# print(class_array)

#PLOT RESULTANT GRAPH
plt.subplot(122)
plt.scatter(X_test[:, 0], X_test[:, 1], c=class_array)
plt.title('KNN Classification Result')
plt.xlabel('sepal length')
plt.ylabel('sepal width')

plt.tight_layout()
plt.show()