from scripts import db_creation, data_extraction, data_transformation, data_load

def main():
    db_creation.main()
    df = data_extraction.main()
    df_transformed = data_transformation.main(df)
    data_load.main(df_transformed)

if __name__ == "__main__":
    main()
