import pandas as pd
import numpy as np
from prefect import task, flow
from scripts import config, utils
import mlflow
from mlflow.models import infer_signature

@flow(name = "Training process workflow", retries = 1, retry_delay_seconds = 20)
def main(df: pd.DataFrame):
    print("\n------------------ START TRAINING ------------------")
    x_train = df.values
    train(x_train)
    print("\n------------------ END TRAINING ------------------")

@task(name = "Train models")
def train(x_train: np.array):
    mlflow.set_tracking_uri("sqlite:///output/mlflow_tracking.db")
    mlflow.set_experiment("market_segmentation_insurance")
    k_prototypes(x_train)

def k_prototypes(x_train: np.array):
    '''
        Train KPrototypes
    '''
    from kmodes.kprototypes import KPrototypes
    from sklearn.metrics import silhouette_score

    print("\n------------------ START KPrototypes ------------------")
    with mlflow.start_run(run_name = f"K-Prototypes_cluster_{config.PARAMS_MODEL['n_clusters']}"):
        # Log parameters
        mlflow.log_params(config.PARAMS_MODEL)

        kproto = KPrototypes(**config.PARAMS_MODEL)
        y = kproto.fit_predict(x_train, categorical = [c for c in range(config.N_COMPONENTS_PCA, config.N_COMPONENTS_PCA + 6)])
        score = silhouette_score(x_train, y)
        print("Silhouette score:", score)

        # Log metrics
        mlflow.log_metric("Cost", kproto.cost_)
        mlflow.log_metric("silhouette_score", score)

        # Log model
        mlflow.sklearn.log_model(
            sk_model = kproto, 
            artifact_path = "kmodes-KPrototypes-model",
            signature = infer_signature(x_train),
            registered_model_name = "market-segmentation-insurance-model")
        
    utils.save_model(kproto, "kprototypes_model")
    print("\n------------------ END KPrototypes ------------------")
  