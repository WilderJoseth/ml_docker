import mlflow
from mlflow.models import infer_signature

target_variable = "income"

def main(df):
    print("\n------------------ START TRAINING ------------------")
    x_train, x_val, y_train, y_val = split_data(df)
    train(x_train, x_val, y_train, y_val)
    print("\n------------------ END TRAINING ------------------")

def split_data(df):
    '''
        Split data between training and validation
    '''
    print("\n------------------ START SPLITING DATA ------------------")
    from sklearn.model_selection import train_test_split
    
    x = df.drop(target_variable, axis = 1).values
    y = df[target_variable].values

    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size = 0.2, random_state = 42)

    print("x_train shape:", x_train.shape)
    print("x_val shape:", x_val.shape)
    print("y_train shape:", y_train.shape)
    print("y_val shape:", y_val.shape)

    mlflow.log_params({"data_test_size": 0.2})
    print("\n------------------ END SPLITING DATA ------------------")
    return x_train, x_val, y_train, y_val

def train(x_train, x_val, y_train, y_val):
    logistic_regression(x_train, x_val, y_train, y_val)
    random_forest(x_train, x_val, y_train, y_val)

def logistic_regression(x_train, x_val, y_train, y_val):
    '''
        Train logistic regression model
    '''
    print("\n------------------ START LOGISTIC REGRESSION ------------------")
    from sklearn.linear_model import LogisticRegression

    hyperparameters = {"class_weight": "balanced", "penalty": "l2", "solver": "liblinear", "C": 100}
    lr = LogisticRegression(**hyperparameters)
    model = lr.fit(x_train, y_train)
    evaluation(model, x_val, y_val)
    
    # Infer the model signature
    signature = infer_signature(x_train, lr.predict(x_train))

    # Register model
    mlflow.sklearn.log_model(
        sk_model = model,
        artifact_path = "sklearn_model_logistic_regression",
        signature = signature,
        input_example = x_train,
        registered_model_name="sklearn_model_logistic_regression",
    )
    print("\n------------------ END LOGISTIC REGRESSION ------------------")

def random_forest(x_train, x_val, y_train, y_val):
    '''
        Train random forest model
    '''
    print("\n------------------ START RANDOM FOREST ------------------")
    from sklearn.ensemble import RandomForestClassifier

    hyperparameters = {"n_estimators": 500, "min_samples_split": 5, "min_samples_leaf": 1, "max_depth": 50, "class_weight": "balanced"}
    lr = RandomForestClassifier(**hyperparameters)
    model = lr.fit(x_train, y_train)

    #mlflow.log_params(hyperparameters)

    evaluation(model, x_val, y_val)
    
    # Infer the model signature
    signature = infer_signature(x_train, lr.predict(x_train))

    # Register model
    mlflow.sklearn.log_model(
        sk_model = model,
        artifact_path = "sklearn_model_random_forest",
        signature = signature,
        input_example = x_train,
        registered_model_name="sklearn_model_random_forest",
    )
    print("\n------------------ END RANDOM FOREST ------------------")

def evaluation(model, x_val, y_val):
    '''
        Evaluation model
    '''
    from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, precision_score, recall_score, f1_score, accuracy_score

    # Prediction
    y_pred = model.predict(x_val)

    # Probabilities for ROC AUC
    y_prob = model.predict_proba(x_val)[:, 1]

    # Accuracy
    print("\nAccuracy:", accuracy_score(y_val, y_pred))

    # Precision
    print("\nPrecision:", precision_score(y_val, y_pred))

    # Recall
    print("\nRecall:", recall_score(y_val, y_pred))

    # F1
    print("\nF1:", f1_score(y_val, y_pred))

    # ROC AUC Score
    roc_auc = roc_auc_score(y_val, y_prob)
    print("\nROC AUC Score:", roc_auc)

    # Confusion Matrix
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_val, y_pred))

    # Classification Report
    print("\nClassification Report:")
    print(classification_report(y_val, y_pred))
