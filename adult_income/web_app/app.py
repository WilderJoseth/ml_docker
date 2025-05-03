from flask import Flask, render_template, jsonify, request
from process import prediction
import os
import pandas as pd
import mlflow
from dotenv import load_dotenv

load_dotenv()

# Read environemnt variables
HOST_MLFLOW = os.getenv("HOST_MLFLOW")
PORT_MLFLOW = os.getenv("PORT_MLFLOW")
HOST_WEB = os.getenv("HOST_WEB")
PORT_WEB = os.getenv("PORT_WEB")

# Set mlflow url repository
mlflow.set_tracking_uri(uri = f"http://{HOST_MLFLOW}:{PORT_MLFLOW}")

# Input object
PATH_DATA = os.path.join(os.getcwd(), "input/data")
PATH_TRANSFORMER = os.path.join(os.getcwd(), "input/transformer")

# Load input object
categorical_transformer = prediction.get_transformer(os.path.join(PATH_TRANSFORMER, "categorical_transformer.sav"))
numeric_transformer = prediction.get_transformer(os.path.join(PATH_TRANSFORMER, "numerical_transformer.sav"))
model_logistic_regression = mlflow.sklearn.load_model("models:/sklearn_model_logistic_regression/1")
model_random_forest = mlflow.sklearn.load_model("models:/sklearn_model_random_forest/1")

# App configuration
app = Flask(__name__)

# Routes
@app.route("/", methods = ["GET"])
def index():
    # Read data
    df = pd.read_csv(os.path.join(PATH_DATA, "adult_cleaned.csv"))

    # Load data from dataset
    data = {}
    data["work_class"] = df["workclass"].unique()
    data["education"] = df["education"].unique()
    data["education_num"] = df["education-num"].unique()
    data["marital_status"] = df["marital-status"].unique()
    data["occupation"] = df["occupation"].unique()
    data["relationship"] = df["relationship"].unique()
    data["race"] = df["race"].unique()
    data["sex"] = df["sex"].unique()
    data["native_country"] = df["native-country"].unique()
    return render_template("index.html", data = data, zip = zip)

@app.route("/predict", methods=["POST"])
def predict():
    '''
        Predict information
    '''
    data = {}

    try:
        model_id = int(request.form.get("model_id"))
        data["age"] = int(request.form.get("age"))
        data["workclass"] = request.form.get("work_class")
        data["fnlwgt"] = int(request.form.get("fnlwgt"))
        data["education-num"] = int(request.form.get("education_num"))
        data["education"] = request.form.get("education")
        data["marital-status"] = request.form.get("marital_status")
        data["occupation"] = request.form.get("occupation")
        data["relationship"] = request.form.get("relationship")
        data["race"] = request.form.get("race")
        data["sex"] = request.form.get("sex")
        data["capital-gain"] = request.form.get("capital_gain")
        data["capital-loss"] = request.form.get("capital_loss")
        data["hours-per-week"] = request.form.get("hours_per_week")
        data["native-country"] = request.form.get("native_country")
        
        print("Data:", data)
        
        if model_id == 1:
            model = model_logistic_regression
            print("Logistic regression selected")
        else:
            model = model_random_forest
            print("Random forest selected")

        # Make prediction
        pred = prediction.predict(data, model, categorical_transformer, numeric_transformer)

        print("Prediction:", pred)
        return jsonify({"message": "Success", "prediction": pred}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": e}), 500
    
if __name__ == "__main__":
    app.run(debug = True, host = HOST_WEB, port = PORT_WEB)
