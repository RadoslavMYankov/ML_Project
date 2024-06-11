import pandas as pd


def prepare_data(root):
    train_data = root + "train.csv"
    train_data = pd.read_csv(train_data)

    y = train_data["Survived"]
    X = train_data.drop("Survived", axis=1)

    return X, y


def split_features(df):
    df_num = df.select_dtypes(include='number')
    df_obj = df.select_dtypes(include='object')
    return df_num, df_obj
