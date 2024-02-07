# KNN from Scratch

## Overview
This notebook implements the K Nearest Neighbors (KNN) algorithm from scratch using Python. KNN is a simple and intuitive algorithm used for classification and regression tasks. The pseudo code provided outlines the steps involved in the implementation.

## Code Description
1. **Import Libraries**: Necessary libraries such as Pandas, NumPy, and Matplotlib are imported.
2. **Load Dataset**: The Iris dataset is loaded and preprocessed to handle missing, null, and duplicate values.
3. **Data Visualization**: The data is visualized using scatter plots to understand the distribution of classes.
4. **Split Dataset**: The dataset is split into training and testing sets.
5. **Feature Extraction**: Features and labels are extracted from both the training and testing sets.
6. **Euclidean Distance Function**: A function to calculate the Euclidean distance between two data points is defined.
7. **Most Repeated Class Function**: A function to determine the most repeated class from the top k tuples is defined.
8. **Compare Predictions Function**: A function to compare predicted outputs with actual labels and calculate correct predictions is defined.
9. **Calculate Accuracy Function**: A function to calculate the accuracy of the model based on correct predictions is defined.
10. **KNN Algorithm Function**: The KNN algorithm is implemented, which iterates through each test data point, calculates distances to all training data points, selects the k nearest neighbors, and predicts the class based on the most repeated class among them.
11. **Model Training**: The model is trained using the KNN algorithm.
12. **Model Evaluation**: The accuracy of the model is evaluated, and a scatter plot is generated to visualize the classification result.

## How to Use
1. Run each cell sequentially to execute the code.
2. Adjust parameters such as the value of k for KNN algorithm as needed.
3. Interpret the visualization to understand the classification result.

## Files
- `KNN_from_Scratch.py`: Jupyter Notebook containing the KNN implementation.

## Prerequisites
- Basic understanding of Python programming.
- Familiarity with classification algorithms and KNN.

## Notes
- This implementation is for educational purposes and may not be optimized for large datasets.
- Further optimizations and enhancements can be made based on specific requirements.

## References
- [Scikit-learn KNN Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [UCI Machine Learning Repository - Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

Feel free to explore and modify the code to suit your needs!
