import pandas as pd 


Test_data = pd.read_csv(r'100-python-projects-data-analysis\Basic Data Analysis Projects\01_exploratory_data_analysis_on_titanic_dataset\datasets\test.csv')
Train_data = pd.read_csv(r'100-python-projects-data-analysis\Basic Data Analysis Projects\01_exploratory_data_analysis_on_titanic_dataset\datasets\train.csv')
print(Train_data.head(5))