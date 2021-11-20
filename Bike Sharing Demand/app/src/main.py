import pandas as pd
from io import BytesIO, StringIO
from functools import reduce
from flask import Flask, request, send_file
from prediction_model import predict, batch_predict, features_ordering


def main():
    app = Flask("Bike Sharing Demand")

    @app.route("/predict", methods=["POST"])
    def singlePredict():
        try:
            model_input = reduce(
                lambda model_input, feature: {
                    **model_input, feature: request.json[feature]
                }, features_ordering, {})
            return {"prediction": predict(model_input)}
        except KeyError as notFoundFeature:
            return f"Didn't find feature: {notFoundFeature}", 400
        except Exception as e:
            print(e)
            return "Internal server error", 500

    @app.route("/batch-predict", methods=["POST"])
    def batchPredict():
        try:
            model_inputs_df = pd.read_csv(
                StringIO(request.files["model_inputs"].read().decode()))

            if model_inputs_df.columns.tolist() != features_ordering:
                return f"Features ordering/names should match: {features_ordering}", 400  # noqa

            predictions = batch_predict(model_inputs_df)
            csv_predictions = reduce(
                lambda csv, prediction: f"{csv}\n{prediction}", predictions,
                "prediction")

            return send_file(BytesIO(csv_predictions.encode()),
                             as_attachment=True,
                             download_name="predictions.csv")
        except KeyError:
            return "The request should have a `model_inputs` form data field, containing an CSV file", 400  # noqa
        except Exception:
            return "Internal server error", 500

    app.run(port=8081, host="0.0.0.0")


if __name__ == "__main__":
    main()
