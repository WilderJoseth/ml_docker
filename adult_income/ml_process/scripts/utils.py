import os

PATH_TEMP = os.path.join(os.getcwd(), "temp")
PATH_INPUT = os.path.join(os.getcwd(), "input")
PATH_OUTPUT = os.path.join(os.getcwd(), "output")

def verify_paths():
    '''
        Verify if paths exist, otherwise create directories
    '''
    print("\n------------------ Start verifying base paths ------------------")
    if not os.path.exists(PATH_INPUT):
        os.mkdir(PATH_INPUT)
    if not os.path.exists(PATH_OUTPUT):
        os.mkdir(PATH_OUTPUT)
    if not os.path.exists(PATH_TEMP):
        os.mkdir(PATH_TEMP)
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts")):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts"))
    print("\n------------------ End verifying base paths ------------------")

def save_dataframe_info(directory_name, df):
    '''
        Save dataframe information like: shape, info and a sample
    '''

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))

    # Create information file
    with open(os.path.join(PATH_OUTPUT, "artifacts", directory_name, "df_info.txt"), "w") as f:
        f.write(f"\nShape: {df.shape}")
        f.write(f"\nInfo:")
        df.info(buf = f)

    # Create sample file
    df.head().to_csv(os.path.join(PATH_OUTPUT, "artifacts", directory_name, "df_head.csv"), index = False)

def save_columns_info(directory_name, df, title, name, is_print = False):
    '''
        Save columns information
    '''
    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))

    # Create file
    print(f"\n{title}: \n{df}", file = open(os.path.join(PATH_OUTPUT, "artifacts", directory_name, f"{name}.txt"), "w"))

    # Show values
    if is_print:
        print(f"\n{title}: \n{df}")

def save_columns_unique(directory_name, df, name, is_print = False):
    '''
        Save columns information about unique values 
    '''
    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))
        
    # Create files
    file_names = []
    for n, v in df.items():
        file_names.append(f"{name}_{n}.txt")
        print(f"\nFeature {n}: {v.unique()}", file = open(os.path.join(PATH_TEMP, f"{name}_{n}.txt"), "w"))
    
    # Merge files
    with open(os.path.join(PATH_OUTPUT, "artifacts", directory_name, f"{name}.txt"), "w") as outfile:
        for f in file_names:
            with open(os.path.join(PATH_TEMP, f), "r") as infile:
                outfile.write(infile.read())

    # Show values
    if is_print:
        print(f"\nFeature {n}: {v.unique()}")

    # Remove files
    for n, v in df.items():
        os.remove(os.path.join(PATH_TEMP, f"{name}_{n}.txt"))

def save_chart_bar(df, directory_name, column_name):
    '''
        Save chart information using bar
    '''
    import matplotlib.pyplot as plt

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))

    # Create chart
    df_count = df[column_name].value_counts()
    fig = plt.figure(figsize = (10, 6))
    plt.barh(df_count.index, df_count.values)
    plt.xlabel("Count")
    plt.ylabel(column_name)
    plt.title(f"Distribution of {column_name}")
    plt.gca().invert_yaxis()

    # Save the figure
    plt.savefig(os.path.join(PATH_OUTPUT, "artifacts", directory_name, f"distribution_of_{column_name}.png"))

def save_chart_box_histogram(df, directory_name, column_name, target_name):
    '''
        Save chart information using boxplot and histograms
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))

    # Create chart
    fig, axs = plt.subplots(1, 2, figsize = (15, 5))
    sns.boxplot(x = target_name, y = column_name, data = df, ax = axs[0])
    axs[0].set_xlabel(target_name)
    axs[0].set_ylabel(column_name)
    axs[0].set_title(f"Distribution of {column_name} by {target_name}")
    sns.histplot(x = column_name, data = df, ax = axs[1])
    axs[1].set_xlabel(column_name)
    axs[1].set_ylabel("Frequency")
    axs[1].set_title(f"Distribution of {column_name}")

    # Save the figure
    plt.savefig(os.path.join(PATH_OUTPUT, "artifacts", directory_name, f"distribution_of_{column_name}.png"))

def save_chart_numeric_information(df, directory_name):
    '''
        Save chart information using boxplot and histograms
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))

    # Relation
    g = sns.PairGrid(df)
    g.map(sns.scatterplot)

    # Correlation
    correlation_matrix = df.corr()
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot = True, cmap = "coolwarm", square = True)
    plt.title("Pearson Correlation Heatmap")

    # Save the figure
    plt.savefig(os.path.join(PATH_OUTPUT, "artifacts", directory_name, "Pearson_Correlation_Heatmap.png"))

def save_dataset(df, name):
    '''
        Save dataset
    '''
    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "data")):
        os.mkdir(os.path.join(PATH_OUTPUT, "data"))

    # Save
    df.to_csv(os.path.join(PATH_OUTPUT, "data", name), index = False)

    print(f"File created {name}")

def save_data_transformers(dt, name):
    '''
        Save data transformers like onehotencoder or numeric scaler
    '''
    import joblib

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "transformers")):
        os.mkdir(os.path.join(PATH_OUTPUT, "transformers"))

    # Save
    joblib.dump(dt, open(os.path.join(PATH_OUTPUT, "transformers", f"{name}.sav"), "wb"))

    print(f"File created {name}.sav")

def save_model(model, name):
    '''
        Save data transformers like onehotencoder or numeric scaler
    '''
    import joblib

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "models")):
        os.mkdir(os.path.join(PATH_OUTPUT, "models"))

    # Save
    joblib.dump(model, open(os.path.join(PATH_OUTPUT, "models", f"{name}.sav"), "wb"))

    print(f"File created {name}.sav")

def save_evaluation_info(directory_name, model_name, acc, prec, rec, f1, roc_auc, cm, cr):
    '''
        Save evaluation information
    '''

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "artifacts", directory_name)):
        os.mkdir(os.path.join(PATH_OUTPUT, "artifacts", directory_name))

    # Create information file
    with open(os.path.join(PATH_OUTPUT, "artifacts", directory_name, f"metrics_{model_name}.txt"), "w") as f:
        f.write(f"\nAccuracy: {acc}")
        f.write(f"\nPrecision: {prec}")
        f.write(f"\nRecall: {rec}")
        f.write(f"\nF1: {f1}")
        f.write(f"\nROC_AUC: {roc_auc}")
        f.write(f"\nConfusion Matrix: \n{cm}")
        f.write(f"\nClassification Report: \n{cr}")