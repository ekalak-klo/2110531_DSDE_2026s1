#import your other libraries here
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

FEATURES = ['cap-color-rate', 'stalk-color-above-ring-rate']


class Clustering:
    def __init__(self, file_path):  
        self.file_path = file_path
        self.df = None
        self.scaler = None
        self.X_scaled = None
        self.kmeans = None

    def _prepare(self):
        self.df = pd.read_csv(self.file_path)
        edible = self.df.loc[self.df['label'] == 'e', FEATURES].copy()
        edible = edible.fillna(edible.mean())
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(edible)
        return self.X_scaled

    def _fit_kmeans(self):
        if self.X_scaled is None:
            self._prepare()
        self.kmeans = KMeans(n_clusters=5, random_state=0, n_init='auto')
        self.kmeans.fit(self.X_scaled)
        return self.kmeans

    def Q1(self):  
        """
        Step1-4
            1. Load the CSV file.
            2. Choose edible mushrooms only.
            3. Only the variables below have been selected to describe the distinctive
               characteristics of edible mushrooms:
               'cap-color-rate','stalk-color-above-ring-rate'
            4. Provide a proper data preprocessing as follows:
                - Fill missing with mean
                - Standardize variables with Standard Scaler
        """
        return self._prepare().shape

    def Q2(self):  
        """
        Step5-6
            5. K-means clustering with 5 clusters (n_clusters=5, random_state=0, n_init='auto')
            6. Show the maximum centroid of 2 features ('cap-color-rate' and 'stalk-color-above-ring-rate') in 2 digits.
        """
        km = self._fit_kmeans()
        return np.round(km.cluster_centers_.max(axis=0), 2)

    def Q3(self):  
        """
        Step7
            7. Convert the centroid value to the original scale, and show the minimum centroid of 2 features in 2 digits.

        """
        km = self._fit_kmeans()
        original = self.scaler.inverse_transform(km.cluster_centers_)
        return np.round(original.min(axis=0), 2)
