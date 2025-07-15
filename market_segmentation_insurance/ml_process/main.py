from scripts import data_extraction, data_preparation, model_training
#from prefect import flow
from scripts import utils

#@flow(name = "ML process - Market segmentation insurance", retries = 1, retry_delay_seconds = 20, timeout_seconds = 30, log_prints = True)
def main():
    print("\n------------------ START ML PROCESS ------------------")   
    df = data_extraction.read()
    df_prepared = data_preparation.main(df)
    model_training.main(df_prepared)
    print("\n------------------ END ML PROCESS ------------------")

if __name__ == "__main__":
    main()