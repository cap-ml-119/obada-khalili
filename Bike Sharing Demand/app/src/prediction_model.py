import pandas as pd
from sklearn import preprocessing

model_url = "https://github.com/cap-ml-119/obada-khalili/raw/bike-sharing-demand/Bike%20Sharing%20Demand/ML%20model/model.pickle"  # noqa
model = pd.read_pickle(model_url)

poly_transform = preprocessing.PolynomialFeatures(4).fit_transform

features_ordering = [
    "datetime", "season", "holiday", "workingday", "weather", "temp", "atemp",
    "humidity", "windspeed"
]


def predict(model_input):
    model_input["datetime"] = pd.to_datetime(model_input["datetime"]).hour
    del model_input["atemp"]
    model_input = poly_transform([list(model_input.values())])
    return model.predict(model_input)[0]


def batch_predict(model_inputs_df):
    model_inputs_df["datetime"] = model_inputs_df["datetime"].map(
        lambda datetime: pd.to_datetime(datetime).hour)
    model_inputs_df.drop(columns=["atemp"], inplace=True)
    model_inputs = poly_transform(model_inputs_df.values)
    return model.predict(model_inputs)
