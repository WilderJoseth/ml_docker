from scripts import utils

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

    model_name = "sklearn_model_logistic_regression"
    hyperparameters = {"class_weight": "balanced", "penalty": "l2", "solver": "liblinear", "C": 100}
    lr = LogisticRegression(**hyperparameters)
    model = lr.fit(x_train, y_train)
    evaluation(model, x_val, y_val, model_name)
    
    # Save model
    utils.save_model(model, model_name)
    print("\n------------------ END LOGISTIC REGRESSION ------------------")

def random_forest(x_train, x_val, y_train, y_val):
    '''
        Train random forest model
    '''
    print("\n------------------ START RANDOM FOREST ------------------")
    from sklearn.ensemble import RandomForestClassifier

    model_name = "sklearn_model_random_forest"
    hyperparameters = {"n_estimators": 500, "min_samples_split": 5, "min_samples_leaf": 1, "max_depth": 50, "class_weight": "balanced"}
    lr = RandomForestClassifier(**hyperparameters)
    model = lr.fit(x_train, y_train)
    evaluation(model, x_val, y_val, model_name)
    
    # Save model
    utils.save_model(model, model_name)
    print("\n------------------ END RANDOM FOREST ------------------")

def evaluation(model, x_val, y_val, model_name):
    '''
        Evaluation model
    '''
    from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, precision_score, recall_score, f1_score, accuracy_score

    # Prediction
    y_pred = model.predict(x_val)

    # Probabilities for ROC AUC
    y_prob = model.predict_proba(x_val)[:, 1]

    # Accuracy
    acc = accuracy_score(y_val, y_pred)
    print("\nAccuracy:", acc)

    # Precision
    prec = precision_score(y_val, y_pred)
    print("\nPrecision:", prec)

    # Recall
    rec = recall_score(y_val, y_pred)
    print("\nRecall:", rec)

    # F1
    f1 = f1_score(y_val, y_pred)
    print("\nF1:", f1)

    # ROC AUC Score
    roc_auc = roc_auc_score(y_val, y_prob)
    print("\nROC AUC Score:", roc_auc)

    # Confusion Matrix
    cm = confusion_matrix(y_val, y_pred)
    print("\nConfusion Matrix:")
    print(cm)

    # Classification Report
    cr = classification_report(y_val, y_pred)
    print("\nClassification Report:")
    print(cr)

    utils.save_evaluation_info("6_metrics", model_name, acc, prec, rec, f1, roc_auc, cm, cr)
