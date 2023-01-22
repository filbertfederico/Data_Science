# Machine Learning and the Prevention of Mass Shooting in the United States
## by Arish, Daniel and Filbert
-------------------------------
As mass shootings have become a serious issue around the world, especially in America. We aim to find the root cause of the mass shootings by looking through each individual shooter's past and personal life to find if there are any links to their actions. This repository compiles data from the database created by the Violence Project.

## Files description
The correlation matrix folder contains all the images of the correlation matrix of this dataset

The csv_files folder contains all the csv files used throughout the process

The excel_files folder contains all the excel files used throughout the process, mainly used to make the data more easily readable

The Graph and other vizualization folder contains all the graphs that were made to analyze the dataset

The Statistics folder contains all files that have to do mainly with the statistical analysis

The ViolenceProjectDataBase.xlsx file is the original database created by the Violence Project

The preProcessing file cleans the dataset of data that isn't very relevant to the project or has too many null values in the dataset by deleting them

The FillingMissingValues file finds the missing values and then deletes the cell with the missing value

The data_catagorisation file categorizes the data into multiple categories to make it more organized

the mental_illness_stats file compiles the data within the dataset into smaller categories which are 'Mental Illness Count' and 'Trauma Count' alongside the Number Killed and the total of the two

The labeling file labels the data based on whether the number killed is below or equal to 5 or over 5

The cleaningData file cleans the database to look cleaner and able to be processed into models

The correlationMatrix file contains the correlation matrix betweent he multiple sets of data in the database

The Pearson's correlation file contains the pearson's correlation matrix of a more filtered version of the database

The Meand&SD file contains the means and Standard Deviations of the mental_illness_stats.csv file

The chi square file contains the chi square values for the data of the mental_illness_stats.csv file

The K-meansClustering file contains the K-means Clustering code which finds the similarity between the items and groups them into the clusters using the K-means clustering method

The randomForest file contains the code for the Random Forest Algorithm which uses a learning method consisting of a multitude of decision trees.

The Xgboost file contains the code for the Xgboost algorithm which is an improved version of the Random Forest

The decisionTree file contains the code for the decision tree algorithm which uses supervised machine learning to make a prediction based on the database

The kernerlRBF which contains the code for the Radial Basis Function kernel algorithm which does classification 

the logisticRegression file contains the code for the logisitic regression algorithm which does classification

the polynomialKernel file contains the code for the Polynomial Kernel algorithm which represents the similarity of vectors in a feature space over polynomials of the original variables, allowing learning of non-linear models.
