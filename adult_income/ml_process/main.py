import os
import mlflow
from dotenv import load_dotenv
from scripts import data_extraction, data_analysis, data_preparation, model_training

load_dotenv()

HOST_MLFLOW = os.getenv("HOST_MLFLOW")
PORT_MLFLOW = os.getenv("PORT_MLFLOW")

mlflow.set_tracking_uri(uri = f"http://{HOST_MLFLOW}:{PORT_MLFLOW}")
mlflow.set_experiment("MLflow Adult Income")

PATH_TEMP = os.path.join(os.getcwd(), "temp")
PATH_DATA_IN = os.path.join(os.getcwd(), "data")
PATH_DATA_OUT = os.path.join(os.getcwd(), "output/data")
PATH_TRANSFORMER = os.path.join(os.getcwd(), "output/transformer")

def main():
    print("\n------------------ START ML PROCESS ------------------")
    with mlflow.start_run():
        print("\n------------------ Start verifying paths ------------------")
        if not os.path.exists(PATH_TEMP):
            os.mkdir(PATH_TEMP)
        if not os.path.exists(os.path.join(os.getcwd(), "output")):
            os.mkdir(os.path.join(os.getcwd(), "output"))
        if not os.path.exists(PATH_DATA_OUT):
            os.mkdir(PATH_DATA_OUT)
        if not os.path.exists(PATH_TRANSFORMER):
            os.mkdir(PATH_TRANSFORMER)
        print("\n------------------ End verifying paths ------------------")

        mlflow.set_tag("Machine learning classification trainer", "Adult Income data")
        df = data_extraction.read()
        df_cleaned = data_analysis.main(df)
        df_encoded = data_preparation.main(df_cleaned)
        model_training.main(df_encoded)
    print("\n------------------ END ML PROCESS ------------------")

if __name__ == "__main__":
    main()