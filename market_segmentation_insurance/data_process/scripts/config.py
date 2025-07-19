######################### DATA FEATURES #########################
FEATURES = ["cust_id", "balance", "balance_frequency", "purchases", "oneoff_purchases", "installments_purchases", "cash_advance", "purchases_frequency", 
            "oneoff_purchases_frequency", "purchases_installments_frequency", "cash_advance_frequency", "cash_advance_trx", "purchases_trx", 
            "credit_limit", "payments", "minimum_payments", "prc_full_payment", "tenure"]
NUMERIC_FEATURES = ["balance", "balance_frequency", "purchases", "oneoff_purchases", "installments_purchases", "cash_advance", "purchases_frequency", 
                    "oneoff_purchases_frequency", "purchases_installments_frequency", "cash_advance_frequency", "cash_advance_trx", "purchases_trx", 
                    "credit_limit", "payments", "minimum_payments", "prc_full_payment"]
CATEGORICAL_FEATURES = ["tenure"]
######################### DATA FEATURES #########################