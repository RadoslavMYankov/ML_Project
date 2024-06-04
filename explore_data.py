import pandas as pd

def prepare_data(root):
    train_data = root + "train.csv"
    train_data = pd.read_csv(train_data)

    y = train_data["Survived"]
    X = train_data.drop("Survived", axis=1)

    return X, y






