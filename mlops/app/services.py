import pandas as pd
from numpy.typing import ArrayLike
from sklearn.model_selection import train_test_split

RANDOM_STATE = 42

class HousePrices:
    @staticmethod
    def get_train_test_data() -> list[ArrayLike]:
        df = pd.read_csv('app/data/alura_real_estate.csv')
        X = df.drop('price', axis=1)
        y = df['price']
        return train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE)