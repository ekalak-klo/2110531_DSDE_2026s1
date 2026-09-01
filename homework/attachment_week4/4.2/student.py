import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import warnings  
from sklearn.exceptions import ConvergenceWarning  
warnings.filterwarnings("ignore", category=ConvergenceWarning)  

EDUCATION_ORDER = {
    'illiterate': 1,
    'basic.4y': 2,
    'basic.6y': 3,
    'basic.9y': 4,
    'high.school': 5,
    'professional.course': 6,
    'university.degree': 7,
}


class BankLogistic:
    def __init__(self, data_path):  
        self.data_path = data_path
        self.df = pd.read_csv(data_path, sep=',')
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None

    def _deduped_df(self):
        return self.df.drop_duplicates().copy()

    def _flat_columns(self, df):
        return [
            col for col in df.columns
            if col != 'y'
            and df[col].value_counts(normalize=True, dropna=True).max() > 0.99
        ]

    def _split_prepared(self):
        df = self._deduped_df().replace('unknown', np.nan)
        df = df.drop(columns=self._flat_columns(df))
        y = (df['y'] == 'yes').astype(int)
        X = df.drop(columns=['y'])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.3, random_state=0, stratify=y
        )
        return self.X_train, self.X_test, self.y_train, self.y_test

    def _encode_features(self):
        if self.X_train is None:
            self._split_prepared()

        X_train = self.X_train.copy()
        X_test = self.X_test.copy()

        num_cols = X_train.select_dtypes(include='number').columns
        cat_cols = X_train.select_dtypes(exclude='number').columns

        for col in num_cols:
            fill = X_train[col].mean()
            X_train[col] = X_train[col].fillna(fill)
            X_test[col] = X_test[col].fillna(fill)

        for col in cat_cols:
            fill = X_train[col].mode()[0]
            X_train[col] = X_train[col].fillna(fill)
            X_test[col] = X_test[col].fillna(fill)

        if 'education' in X_train.columns:
            X_train['education'] = X_train['education'].map(EDUCATION_ORDER)
            X_test['education'] = X_test['education'].map(EDUCATION_ORDER)

        X_train = pd.get_dummies(X_train)
        X_test = pd.get_dummies(X_test)
        X_train, X_test = X_train.align(X_test, join='left', axis=1, fill_value=0)

        return X_train, X_test

    def Q1(self):  
        """
        Problem 1:
            Load ‘bank-st.csv’ data from the “Attachment”
            How many rows of data are there in total?

        """
        return len(self.df)

    def Q2(self):  
        """
        Problem 2:
            return the tuple of numeric variables and categorical variables are presented in the dataset.
        """
        numeric_count = len(self.df.select_dtypes(include='number').columns)
        categorical_count = len(self.df.select_dtypes(exclude='number').columns)
        return numeric_count, categorical_count

    def Q3(self):  
        """
        Problem 3:
            return the tuple of the Class 0 (no) followed by Class 1 (yes) in 3 digits.
        """
        no_pct = float(round((self.df['y'] == 'no').mean(), 3))
        yes_pct = float(round((self.df['y'] == 'yes').mean(), 3))
        return no_pct, yes_pct

    def Q4(self):  
        """
        Problem 4:
            Remove duplicate records from the data. What are the shape of the dataset afterward?
        """
        return self._deduped_df().shape

    def Q5(self):  
        """
        Problem 5:
            5. Replace unknown value with null
            6. Remove features with more than 99% flat values.
                Hint: There is only one feature should be drop
            7. Split Data
            -	Split the dataset into training and testing sets with a 70:30 ratio.
            -	random_state=0
            -	stratify option
            return the tuple of shapes of X_train and X_test.

        """
        self._split_prepared()
        return self.X_train.shape, self.X_test.shape

    def Q6(self):
        """
        Problem 6:
            8. Impute missing
                -	For numeric variables: Impute missing values using the mean.
                -	For categorical variables: Impute missing values using the mode.
                Hint: Use statistics calculated from the training dataset to avoid data leakage.
            9. Categorical Encoder:
                Map the nominal data for the education variable using the following order:
                education_order = {
                    'illiterate': 1,
                    'basic.4y': 2,
                    'basic.6y': 3,
                    'basic.9y': 4,
                    'high.school': 5,
                    'professional.course': 6,
                    'university.degree': 7}
                Hint: Use One hot encoder or pd.dummy to encode nominal category
            return the shape of X_train.

        """
        X_train, _ = self._encode_features()
        return X_train.shape

    def Q7(self):
        ''' Problem7: Use Logistic Regression as the model with
            random_state=2025,
            class_weight='balanced' and
            max_iter=500.
            Train the model using all the remaining available variables.
            What is the macro F1 score of the model on the test data? in 2 digits
        '''
        X_train, X_test = self._encode_features()
        model = LogisticRegression(
            random_state=2025,
            class_weight='balanced',
            max_iter=500,
        )
        model.fit(X_train, self.y_train)
        pred = model.predict(X_test)
        return round(f1_score(self.y_test, pred, average='macro'), 2)
