############ FEATURES ############
NUMERIC_FEATURES = ["balance", "balance_frequency", "purchases", "oneoff_purchases", "installments_purchases", "cash_advance", "purchases_frequency", 
                    "oneoff_purchases_frequency", "purchases_installments_frequency", "cash_advance_frequency", "cash_advance_trx", "purchases_trx", 
                    "credit_limit", "payments", "minimum_payments", "prc_full_payment"]

CATEGORICAL_FEATURES = ["tenure"]
############ FEATURES ############

############ DATA PREPARATION ############
N_COMPONENTS_PCA = 4
KERNEL_PCA = "poly"
############ DATA PREPARATION ############

############ MODEL TRAINING ############
PARAMS_MODEL = {"n_clusters": 3, "init": "Cao", "random_state": 42}
############ MODEL TRAINING ############
