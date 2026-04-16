import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import os

def train_model():
    print("Loading data...")
    df = pd.read_csv("data/student_data.csv")

    # Define target and features INSIDE function
    y = df["math score"]
    X = df.drop("math score", axis=1)

    # Convert categorical to numeric
    X = pd.get_dummies(X)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    print("Evaluating...")
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)

    print("R2 Score:", score)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

    return score

if __name__ == "__main__":
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import joblib
import os

def train_model():
    print("Loading data...")
    df = pd.read_csv("data/student_data.csv")

    # Define target and features INSIDE function
    y = df["math score"]
    X = df.drop("math score", axis=1)

    # Convert categorical to numeric
    X = pd.get_dummies(X)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    print("Evaluating...")
    y_pred = model.predict(X_test)
    score = r2_score(y_test, y_pred)

    print("R2 Score:", score)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")

    return score

if __name__ == "__main__":
    train_model()
