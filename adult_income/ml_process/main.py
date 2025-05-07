from scripts import utils
from scripts import data_extraction, data_analysis, data_preparation, model_training

def main():
    print("\n------------------ START ML PROCESS ------------------")
    utils.verify_paths()

    df = data_extraction.read()
    df_cleaned = data_analysis.main(df)
    df_encoded = data_preparation.main(df_cleaned)
    model_training.main(df_encoded)
    print("\n------------------ END ML PROCESS ------------------")

if __name__ == "__main__":
    main()