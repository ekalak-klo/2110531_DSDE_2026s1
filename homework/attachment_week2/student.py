import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic_to_student.csv) and answer the questions.
    (Note that the following functions already take the Titanic dataset as a DataFrame, so you don’t need to use read_csv.)

"""


def Q1(df):
    """
        Problem 1:
            How many rows are there in the "titanic_to_student.csv"?
    """
    return len(df)


def Q2(df: pd.DataFrame):
    '''
        Problem 2:
            2.1 Drop variables with missing > 50%
            2.2 Check all columns except 'Age' and 'Fare' for flat values, drop the columns where flat value > 70%
            From 2.1 and 2.2, how many columns do we have left?
            Note: 
            -Ensure missing values are considered in your calculation. If you use normalize in .value_counts(), please include dropna=False.
    '''
    df = df.copy()
    df = df.loc[:, df.isna().mean() <= 0.5]
    flat_cols = [
        col for col in df.columns
        if col not in ("Age", "Fare")
        and df[col].value_counts(normalize=True, dropna=False).max() > 0.7
    ]
    df = df.drop(columns=flat_cols) # drop columns with flat values > 70%
    return df.shape[1]


def Q3(df: pd.DataFrame):
    '''
       Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            How many rows do we have left?
    '''
    return len(df.dropna(subset=["Survived"]))


def Q4(df: pd.DataFrame):
    '''
       Problem 4:
            Handle outliers
            For the variable “Fare”, replace outlier values with the boundary values
            If value < (Q1 - 1.5IQR), replace with (Q1 - 1.5IQR)
            If value > (Q3 + 1.5IQR), replace with (Q3 + 1.5IQR)
            What is the mean of “Fare” after replacing the outliers (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    fare = df["Fare"].copy()
    q1 = fare.quantile(0.25)
    q3 = fare.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    fare = fare.clip(lower=lower, upper=upper)
    return round(fare.mean(), 2)


def Q5(df: pd.DataFrame):
    '''
       Problem 5:
            Impute missing value
            For number type column, impute missing values with mean
            What is the average (mean) of “Age” after imputing the missing values (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    df = df.copy()
    df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
    return round(df["Age"].mean(), 2)


def Q6(df: pd.DataFrame):
    '''
        Problem 6:
            Convert categorical to numeric values
            For the variable “Embarked”, perform the dummy coding.
            What is the average (mean) of “Embarked_Q” after performing dummy coding (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    df = df.copy()
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    enc = OneHotEncoder(handle_unknown="ignore")
    encoded = enc.fit_transform(df[["Embarked"]]).toarray()
    dummy_df = pd.DataFrame(
        encoded,
        columns=[f"Embarked_{c}" for c in enc.categories_[0]],
        index=df.index,
    )
    return round(dummy_df["Embarked_Q"].mean(), 2)


def Q7(df: pd.DataFrame):
    '''
        Problem 7:
            Split train/test split with stratification using 70%:30% and random seed with 123
            Show a proportion between survived (1) and died (0) in all data sets (total data, train, test)
            What is the proportion of survivors (survived = 1) in the training data (round 2 decimal points)?
            Hint: Use function round(_, 2), and train_test_split() from sklearn.model_selection, 
            Don't forget to impute missing values with mean.
    '''
    df = df.copy()
    df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
    y = df["Survived"]
    X = df.drop(columns=["Survived"])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=123, stratify=y
    )
    return round((y_train == 1).mean(), 2)
