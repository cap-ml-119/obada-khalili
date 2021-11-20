# Bike Sharing Demand

Solution for the [Bike Sharing Demand](https://www.kaggle.com/c/bike-sharing-demand) problem, along with a Flask service to do predictions.

# Model

My way of hosting the model: The model is tracked by Git, and pushed to GitHub on evey change, and I read the model file from GitHub in the prediction service.

# Running Locally, and API Docs

## Running via Docker

- First, build the image with:

```sh
docker build -t bike_sharing_demand .
```

- Then run the image:

```sh
docker run -dp 8081:8081 bike_sharing_demand
```

## API Docs

### Single Prediction

- Endpoint: `POST /predict`.
- Request body schema example:

```json
{
  "datetime": "2011-01-01 00:00:00",
  "season": 1,
  "holiday": 0,
  "workingday": 0,
  "weather": 1,
  "temp": 9.84,
  "atemp": 14.395,
  "humidity": 81,
  "windspeed": 0
}
```

- Responses:
  - `{ "prediction": <prediction> }`, 200 status.
  - `"Didn't find feature: '\<feature-name\>'"`, 400 status.
  - `"Internal server error"`, 500 status.

### Batch Prediction

- Endpoint: `POST /batch-predict`.
- The request should have a `model_inputs` form data field, containing an CSV file complying to the following format:

```
datetime,season,holiday,workingday,weather,temp,atemp,humidity,windspeed
2011-01-20 00:00:00,1,0,1,1,10.66,11.365,56,26.0027
2011-01-20 01:00:00,1,0,1,1,10.66,13.635,56,0
2011-01-20 02:00:00,1,0,1,1,10.66,13.635,56,0
2011-01-20 03:00:00,1,0,1,1,10.66,12.88,56,11.0014
.
.
.
```

- Responses:
  - a CSV file containing predictions column, 200 status.
  - `"The request should have a `model_inputs` form data field, containing an CSV file"`, 400 status.
  - `"Features ordering/names should match: ['datetime', 'season', 'holiday', 'workingday', 'weather', 'temp', 'atemp', 'humidity', 'windspeed']"`, 400 status.
  - `"Internal server error"`, 500 status.
