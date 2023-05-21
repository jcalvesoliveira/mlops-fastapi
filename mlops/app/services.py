import pickle
import pandas as pd
from numpy.typing import ArrayLike
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

RANDOM_STATE = 42

class HousePrices:
    model = None

    @staticmethod
    def get_train_test_data() -> list[ArrayLike]:
        df = pd.read_csv('app/data/alura_real_estate.csv')
        X = df.drop('price', axis=1)
        y = df['price']
        return train_test_split(X, y, test_size=0.3, random_state=RANDOM_STATE)

    def save_model(self):
        with open('app/data/model.pkl', 'wb') as file:
            pickle.dump(self.model, file)

    def log_model_metris(self, X_test: ArrayLike, y_test: ArrayLike):
        y_pred_test = self.model.predict(X_test)
        print(f'R2 score: {r2_score(y_test, y_pred_test)}')
        print(f'MSE score: {mean_squared_error(y_test, y_pred_test)}')

    def train_model(self):
        X_train, X_test, y_train, y_test = self.get_train_test_data()
        self.model = LinearRegression()
        self.model.fit(X_train.values, y_train)
        self.log_model_metris(X_test, y_test)
        self.save_model()