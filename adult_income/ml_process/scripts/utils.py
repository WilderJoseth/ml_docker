import os
import mlflow

PATH_TEMP = os.path.join(os.getcwd(), "temp")

def save_mlflow_artifact_dataframe_info(artifact_path, df):
    '''
        Save dataframe information like: shape, info and a sample
    '''

    # Create information file
    with open(os.path.join(PATH_TEMP, "df_info.txt"), "w") as f:
        f.write(f"\nShape: {df.shape}")
        f.write(f"\nInfo:")
        df.info(buf = f)

    # Create sample file
    df.head().to_csv(os.path.join(PATH_TEMP, "df_head.csv"), index = False)

    # Save artifacs in mlflow repository
    mlflow.log_artifact(os.path.join(PATH_TEMP, "df_info.txt"), artifact_path = artifact_path)
    mlflow.log_artifact(os.path.join(PATH_TEMP, "df_head.csv"), artifact_path = artifact_path)

    # Remove files
    os.remove(os.path.join(PATH_TEMP, "df_info.txt"))
    os.remove(os.path.join(PATH_TEMP, "df_head.csv"))

def save_mlflow_artifact_dataframe(artifact_path, df, name, index = False):
    '''
        Save dataframe
    '''

    # Create file
    df.to_csv(os.path.join(PATH_TEMP, f"{name}.csv"), index = index)

    # Save artifacs in mlflow repository
    mlflow.log_artifact(os.path.join(PATH_TEMP, f"{name}.csv"), artifact_path = artifact_path)

    # Remove files
    os.remove(os.path.join(PATH_TEMP, f"{name}.csv"))

def save_mlflow_artifact_columns_info(artifact_path, df, title, name, is_print = False):
    '''
        Save columns information
    '''
    
    # Create file
    print(f"\n{title}: \n{df}", file = open(os.path.join(PATH_TEMP, f"{name}.txt"), "w"))

    # Save artifacs in mlflow repository
    mlflow.log_artifact(os.path.join(PATH_TEMP, f"{name}.txt"), artifact_path = artifact_path)

    # Show values
    if is_print:
        print(f"\n{title}: \n{df}")

    # Remove files
    os.remove(os.path.join(PATH_TEMP, f"{name}.txt"))

def save_mlflow_artifact_columns_unique(artifact_path, df, name, is_print = False):
    '''
        Save columns information about unique values 
    '''

    # Create files
    file_names = []
    for n, v in df.items():
        file_names.append(f"{name}_{n}.txt")
        print(f"\nFeature {n}: {v.unique()}", file = open(os.path.join(PATH_TEMP, f"{name}_{n}.txt"), "w"))
    
    # Merge files
    with open(os.path.join(PATH_TEMP, f"{name}.txt"), "w") as outfile:
        for f in file_names:
            with open(os.path.join(PATH_TEMP, f), "r") as infile:
                outfile.write(infile.read())

    # Save artifacs in mlflow repository
    mlflow.log_artifact(os.path.join(PATH_TEMP, f"{name}.txt"), artifact_path = artifact_path)

    # Show values
    if is_print:
        print(f"\nFeature {n}: {v.unique()}")

    # Remove files
    for n, v in df.items():
        os.remove(os.path.join(PATH_TEMP, f"{name}_{n}.txt"))
    os.remove(os.path.join(PATH_TEMP, f"{name}.txt"))

def save_mlflow_artifact_chart_bar(df, artifact_path, column_name):
    '''
        Save chart information using bar
    '''
    import matplotlib.pyplot as plt

    # Create chart
    df_count = df[column_name].value_counts()
    fig = plt.figure(figsize = (10, 6))
    plt.barh(df_count.index, df_count.values)
    plt.xlabel("Count")
    plt.ylabel(column_name)
    plt.title(f"Distribution of {column_name}")
    plt.gca().invert_yaxis()

    # Save artifacs in mlflow repository
    mlflow.log_figure(fig, f"{artifact_path}.png")

def save_mlflow_artifact_chart_box_histogram(df, artifact_path, column_name, target_name):
    '''
        Save chart information using boxplot and histograms
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

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

    # Save artifacs in mlflow repository
    mlflow.log_figure(fig, f"{artifact_path}.png")

def save_mlflow_artifact_chart_numeric_information(df):
    '''
        Save chart information using boxplot and histograms
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Relation
    g = sns.PairGrid(df)
    g.map(sns.scatterplot)

    # Save artifacs in mlflow repository
    mlflow.log_figure(g.figure, "eda_numerical/numerical_relationship.png")

    # Correlation
    correlation_matrix = df.corr()
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot = True, cmap = "coolwarm", square = True)
    plt.title("Pearson Correlation Heatmap")

    # Save artifacs in mlflow repository
    mlflow.log_figure(fig, "eda_numerical/Pearson_Correlation_Heatmap.png")

def save_dataset(df, name, target_name, dataset_source_url, context = "training"):
    '''
        Save dataset
    '''
    # Create an instance of a PandasDataset
    dataset = mlflow.data.from_pandas(
        df, source = dataset_source_url, name = name, targets = target_name
    )

    # Save data
    mlflow.log_input(dataset, context = context)