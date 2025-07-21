from scripts import db_creation, data_extraction, data_transformation, data_load
from scripts import utils

def main():
    '''
        Function that starts the whole process
    '''
    db_creation.main()
    # Register start process
    utils.db_execute_query(f"INSERT INTO public.process_data (name, is_done) VALUES ('Data Process', FALSE);")

    df = data_extraction.main()
    df_transformed = data_transformation.main(df)
    data_load.main(df_transformed)

    # Register end process
    utils.db_execute_query(f"UPDATE public.process_data SET is_done = TRUE, date_end = NOW() WHERE name = 'Data Process';")

if __name__ == "__main__":
    main()
