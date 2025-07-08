from scripts import utils

def main():
    create_raw_data_table()
    create_eda_data_table()
    
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

def create_eda_data_table():
    print("\n------------------ START EDA_DATA_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.eda_data;"
    query_create = '''
                    CREATE TABLE public.eda_data(
                        id SERIAL NOT NULL PRIMARY KEY,
                        BALANCE DECIMAL(24, 6) NOT NULL,
                        BALANCE_FREQUENCY DECIMAL(24, 6) NOT NULL,
                        PURCHASES DECIMAL(24, 6) NOT NULL,
                        ONEOFF_PURCHASES DECIMAL(24, 6) NOT NULL,
                        INSTALLMENTS_PURCHASES DECIMAL(24, 6) NOT NULL,
                        CASH_ADVANCE DECIMAL(24, 6) NOT NULL,
                        PURCHASES_FREQUENCY DECIMAL(24, 6) NOT NULL,
                        ONEOFF_PURCHASES_FREQUENCY DECIMAL(24, 6) NOT NULL,
                        PURCHASES_INSTALLMENTS_FREQUENCY DECIMAL(24, 6) NOT NULL,
                        CASH_ADVANCE_FREQUENCY DECIMAL(24, 6) NOT NULL,
                        CASH_ADVANCE_TRX DECIMAL(24, 6) NOT NULL,
                        PURCHASES_TRX DECIMAL(24, 6) NOT NULL,
                        CREDIT_LIMIT DECIMAL(24, 6) NOT NULL,
                        PAYMENTS DECIMAL(24, 6) NOT NULL,
                        MINIMUM_PAYMENTS DECIMAL(24, 6) NOT NULL,
                        PRC_FULL_PAYMENT DECIMAL(24, 6) NOT NULL,
                        TENURE DECIMAL(24, 6) NOT NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.eda_data created")
    utils.db_execute_query(query_create)
    print("\n------------------ START EDA_DATA_TABLE CREATION ------------------")