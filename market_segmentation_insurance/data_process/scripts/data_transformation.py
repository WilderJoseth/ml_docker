
def main(df):
    df = cleaning(df)
    return df

def data_profiling():
    pass

def cleaning(df):
    print("\n------------------ START DATA CLEANING PROCESS ------------------")

    print("\n------------------ START FILLING MISSING VALUES PROCESS ------------------")
    df["MINIMUM_PAYMENTS"] = df["MINIMUM_PAYMENTS"].fillna(df["MINIMUM_PAYMENTS"].median())
    df["CREDIT_LIMIT"] = df["CREDIT_LIMIT"].fillna(df["CREDIT_LIMIT"].median())

    print("Value: median")
    print("Columns: MINIMUM_PAYMENTS and CREDIT_LIMIT")
    print("\n------------------ END FILLING MISSING VALUES PROCESS ------------------")

    print("\n------------------ START REMOVING HIGH CARDINALITY COLUMN ID PROCESS ------------------")
    df = df.drop(columns = "CUST_ID")
    print("\n------------------ END REMOVING HIGH CARDINALITY COLUMN ID PROCESS ------------------")
    
    print("\n------------------ END DATA CLEANING PROCESS ------------------")
    return df