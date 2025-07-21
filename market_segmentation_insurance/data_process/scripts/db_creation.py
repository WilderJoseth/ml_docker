from scripts import utils

def main():
    '''
        Function that starts the whole process
    '''
    create_process_data_table()
    create_raw_data_table()
    create_eda_data_table()
    create_missing_values_summary_table()
    create_data_consistency_summary_table()
    create_data_profiling_table()
    
def create_process_data_table():
    '''
        Create public.process_data table, which stores the state of the process
    '''
    print("\n------------------ START PROCESS_DATA_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.process_data;"
    query_create = '''
                    CREATE TABLE public.process_data(
                        id SERIAL NOT NULL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        is_done BOOLEAN NOT NULL,
                        date_start timestamp NOT NULL DEFAULT NOW(),
                        date_end timestamp NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.process_data created")
    utils.db_execute_query(query_create)
    print("\n------------------ START PROCESS_DATA_TABLE CREATION ------------------")

def create_raw_data_table():
    '''
        Create public.raw_data table, which stores data without transformation
    '''
    print("\n------------------ START RAW_DATA_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.raw_data;"
    query_create = '''
                    CREATE TABLE public.raw_data(
                        id SERIAL NOT NULL PRIMARY KEY,
                        cust_id VARCHAR(25) NULL,
                        balance VARCHAR(25) NULL,
                        balance_frequency VARCHAR(25) NULL,
                        purchases VARCHAR(25) NULL,
                        oneoff_purchases VARCHAR(25) NULL,
                        installments_purchases VARCHAR(25) NULL,
                        cash_advance VARCHAR(25) NULL,
                        purchases_frequency VARCHAR(25) NULL,
                        oneoff_purchases_frequency VARCHAR(25) NULL,
                        purchases_installments_frequency VARCHAR(25) NULL,
                        cash_advance_frequency VARCHAR(25) NULL,
                        cash_advance_trx VARCHAR(25) NULL,
                        purchases_trx VARCHAR(25) NULL,
                        credit_limit VARCHAR(25) NULL,
                        payments VARCHAR(25) NULL,
                        minimum_payments VARCHAR(25) NULL,
                        prc_full_payment VARCHAR(25) NULL,
                        tenure VARCHAR(25) NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.raw_data created")
    utils.db_execute_query(query_create)
    print("\n------------------ START RAW_DATA_TABLE CREATION ------------------")

def create_eda_data_table():
    '''
        Create public.eda_data table, which stores data after transformation
    '''
    print("\n------------------ START EDA_DATA_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.eda_data;"
    query_create = '''
                    CREATE TABLE public.eda_data(
                        id SERIAL NOT NULL PRIMARY KEY,
                        balance DECIMAL(24, 6) NOT NULL,
                        balance_frequency DECIMAL(24, 6) NOT NULL,
                        purchases DECIMAL(24, 6) NOT NULL,
                        oneoff_purchases DECIMAL(24, 6) NOT NULL,
                        installments_purchases DECIMAL(24, 6) NOT NULL,
                        cash_advance DECIMAL(24, 6) NOT NULL,
                        purchases_frequency DECIMAL(24, 6) NOT NULL,
                        oneoff_purchases_frequency DECIMAL(24, 6) NOT NULL,
                        purchases_installments_frequency DECIMAL(24, 6) NOT NULL,
                        cash_advance_frequency DECIMAL(24, 6) NOT NULL,
                        cash_advance_trx DECIMAL(24, 6) NOT NULL,
                        purchases_trx DECIMAL(24, 6) NOT NULL,
                        credit_limit DECIMAL(24, 6) NOT NULL,
                        payments DECIMAL(24, 6) NOT NULL,
                        minimum_payments DECIMAL(24, 6) NOT NULL,
                        prc_full_payment DECIMAL(24, 6) NOT NULL,
                        tenure VARCHAR(2) NOT NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.eda_data created")
    utils.db_execute_query(query_create)
    print("\n------------------ START EDA_DATA_TABLE CREATION ------------------")

def create_missing_values_summary_table():
    '''
        Create public.missing_values_summary table, which stores information about missing data
    '''
    print("\n------------------ START MIISING_VALUES_SUMMARY_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.missing_values_summary;"
    query_create = '''
                    CREATE TABLE public.missing_values_summary(
                        id SERIAL NOT NULL PRIMARY KEY,
                        feature VARCHAR(50) NOT NULL,
                        frequency INTEGER NOT NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.missing_values_summary created")
    utils.db_execute_query(query_create)
    print("\n------------------ START MIISING_VALUES_SUMMARY_TABLE CREATION ------------------")

def create_data_consistency_summary_table():
    '''
        Create public.data_consistency_summary table, which stores information about quality of data
    '''
    print("\n------------------ START DATA_CONSISTENCY_SUMMARY_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.data_consistency_summary;"
    query_create = '''
                    CREATE TABLE public.data_consistency_summary(
                        id SERIAL NOT NULL PRIMARY KEY,
                        feature VARCHAR(50) NOT NULL,
                        total_no_valid INTEGER NOT NULL,
                        type_data VARCHAR(20) NOT NULL
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.data_consistency_summary created")
    utils.db_execute_query(query_create)
    print("\n------------------ START DATA_CONSISTENCY_SUMMARY_TABLE CREATION ------------------")

def create_data_profiling_table():
    '''
        Create public.data_profiling table, which stores information about quality of data
    '''
    print("\n------------------ START DATA_PROFILING_TABLE CREATION ------------------")
    query_drop = "DROP TABLE IF EXISTS public.data_profiling;"
    query_create = '''
                    CREATE TABLE public.data_profiling(
                        id SERIAL NOT NULL PRIMARY KEY,
                        total_duplicated INT NOT NULL DEFAULT 0
                    );
                    '''
    
    utils.db_execute_query(query_drop)
    print("Table public.data_profiling created")
    utils.db_execute_query(query_create)
    print("\n------------------ START DATA_PROFILING_TABLE CREATION ------------------")