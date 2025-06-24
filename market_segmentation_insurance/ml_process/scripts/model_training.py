from prefect import task
from scripts import config, utils

@task(name = "main training process", description = "Main function that calls training process workflow", retries = 3, retry_delay_seconds = 60, tags = ["model_training"])
def main(df):
    print("\n------------------ START TRAINING ------------------")
    x_train = df.values
    train(x_train)
    print("\n------------------ END TRAINING ------------------")

def train(x_train):
    k_prototypes(x_train)

def k_prototypes(x_train):
    '''
        Train KPrototypes
    '''
    from kmodes.kprototypes import KPrototypes
    from sklearn.metrics import silhouette_score

    print("\n------------------ START KPrototypes ------------------")
    kproto = KPrototypes(**config.PARAMS_MODEL)
    y = kproto.fit_predict(x_train, categorical = [c for c in range(config.N_COMPONENTS_PCA, config.N_COMPONENTS_PCA + 6)])
    score = silhouette_score(x_train, y)
    print("Silhouette score:", score)

    utils.save_model(kproto, "kprototypes_model")
    print("\n------------------ END KPrototypes ------------------")
  