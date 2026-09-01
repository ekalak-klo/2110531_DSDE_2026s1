import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

DROP_COLS = [
    'id', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color-rate',
    'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring',
    'stalk-color-above-ring-rate', 'stalk-color-below-ring-rate',
    'veil-color-rate', 'veil-type',
]


class MushroomClassifier:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = pd.read_csv(data_path)

    def _prepared_df(self):
        df = self.df.dropna(subset=['label'])
        return df.drop(columns=DROP_COLS)

    def _imputed_labeled(self):
        df = self._prepared_df().copy()
        num_cols = df.select_dtypes(include='number').columns
        cat_cols = [c for c in df.select_dtypes(exclude='number').columns if c != 'label']

        for col in num_cols:
            df[col] = df[col].fillna(df[col].mean())
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

        y = df['label'].map({'p': 0, 'e': 1})
        X = df.drop(columns=['label'])
        return X, y

    def _split_encoded(self):
        X, y = self._imputed_labeled()
        X = pd.get_dummies(X, drop_first=True)
        return train_test_split(
            X, y, test_size=0.2, random_state=2020, stratify=y
        )

    def _grid_search(self):
        X_train, X_test, y_train, y_test = self._split_encoded()
        param_grid = {
            'criterion': ['gini', 'entropy'],
            'max_depth': [2, 3],
            'min_samples_leaf': [2, 5],
            'n_estimators': [100],
            'random_state': [2020],
        }
        gs = GridSearchCV(
            RandomForestClassifier(),
            param_grid,
            cv=5,
            n_jobs=-1,
            scoring='f1_weighted',
        )
        gs.fit(X_train, y_train)
        return gs, X_test, y_test

    def Q1(self):  
        """
            1. (From step 1) Before doing the data prep., how many "na" are there in "gill-size" variables?
        """
        return int(self.df['gill-size'].isna().sum())

    def Q2(self):  
        """
            2. (From step 2-4) How many rows of data, how many variables?
        """
        df = self._prepared_df()
        return df.shape[0], df.shape[1]

    def Q3(self):  
        """
            3. (From step 5-6) Answer the quantity class0:class1
        """
        _, y = self._imputed_labeled()
        return int((y == 0).sum()), int((y == 1).sum())

    def Q4(self):  
        """
            4. (From step 7-8) How much is each training and testing sets
        """
        X_train, X_test, _, _ = self._split_encoded()
        return X_train.shape, X_test.shape

    def Q5(self):
        """
            5. (From step 9) Best params after doing random forest grid search.
        """
        gs, _, _ = self._grid_search()
        p = gs.best_params_
        return (
            p['criterion'],
            p['max_depth'],
            p['min_samples_leaf'],
            p['n_estimators'],
            p['random_state'],
        )

    def Q6(self):
        """
            6. (From step 10) F1-score of class 0 and 1 from classification_report (2 digits).
        """
        gs, X_test, y_test = self._grid_search()
        pred = gs.predict(X_test)
        report = classification_report(y_test, pred, output_dict=True)
        return (
            round(report['0']['f1-score'], 2),
            round(report['1']['f1-score'], 2),
        )
