import time
from scripts import data_extraction, data_preparation, model_training
#from prefect import flow
from scripts import utils

#@flow(name = "ML process - Market segmentation insurance", retries = 1, retry_delay_seconds = 20, timeout_seconds = 30, log_prints = True)
def main():
    '''
        Function that starts the whole process
    '''
    print("\n------------------ START ML PROCESS ------------------")
    utils.verify_data_process_is_ready()
    df = data_extraction.read()
    df_prepared = data_preparation.main(df)
    model_training.main(df_prepared)
    print("\n------------------ END ML PROCESS ------------------")

if __name__ == "__main__":
    main()