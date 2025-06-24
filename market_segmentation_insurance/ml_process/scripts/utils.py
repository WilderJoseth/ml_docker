import os
import pickle

PATH_OUTPUT = os.path.join(os.getcwd(), "output")

def save_data_transformers(dt, name):
    '''
        Save data transformers like onehotencoder or numeric scaler
    '''

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "transformers")):
        os.mkdir(os.path.join(PATH_OUTPUT, "transformers"))

    # Save
    with open(os.path.join(PATH_OUTPUT, "transformers", f"{name}.pkl"), 'wb') as file:
        pickle.dump(dt, file)

    print(f"Transformer created {name}.pkl")

def save_model(model, name):
    '''
        Save models
    '''

    # Verify artifacts path
    if not os.path.exists(os.path.join(PATH_OUTPUT, "models")):
        os.mkdir(os.path.join(PATH_OUTPUT, "models"))

    # Save
    with open(os.path.join(PATH_OUTPUT, "models", f"{name}.pkl"), 'wb') as file:
        pickle.dump(model, file)

    print(f"Model created {name}.pkl")
