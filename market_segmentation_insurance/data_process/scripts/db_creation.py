from scripts import utils

def create_raw_data_table():
    print("\n------------------ START RAW_DATA_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.raw_data;"
    query_create = '''
                    CREATE TABLE public.raw_data(
                        id SERIAL NOT NULL PRIMARY KEY,
                        CUST_ID VARCHAR(25) NULL,
                        BALANCE VARCHAR(25) NULL,
                        BALANCE_FREQUENCY VARCHAR(25) NULL,
                        PURCHASES VARCHAR(25) NULL,
                        ONEOFF_PURCHASES VARCHAR(25) NULL,
                        INSTALLMENTS_PURCHASES VARCHAR(25) NULL,
                        CASH_ADVANCE VARCHAR(25) NULL,
                        PURCHASES_FREQUENCY VARCHAR(25) NULL,
                        ONEOFF_PURCHASES_FREQUENCY VARCHAR(25) NULL,
                        PURCHASES_INSTALLMENTS_FREQUENCY VARCHAR(25) NULL,
                        CASH_ADVANCE_FREQUENCY VARCHAR(25) NULL,
                        CASH_ADVANCE_TRX VARCHAR(25) NULL,
                        PURCHASES_TRX VARCHAR(25) NULL,
                        CREDIT_LIMIT VARCHAR(25) NULL,
                        PAYMENTS VARCHAR(25) NULL,
                        MINIMUM_PAYMENTS VARCHAR(25) NULL,
                        PRC_FULL_PAYMENT VARCHAR(25) NULL,
                        TENURE VARCHAR(25) NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.raw_data created")
    utils.db_execute_query(query_create)
    print("\n------------------ START RAW_DATA_TABLE CREATION ------------------")