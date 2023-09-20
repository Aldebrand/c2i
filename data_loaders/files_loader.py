import pandas as pd

def load_data_from_csv(path):
    """
    Load data from csv file
    :param path: path to csv file

    :return: Pandas dataframe or None if an error occured
    """
    try:
        dataframe = pd.read_csv(path)

        return dataframe
    except FileNotFoundError as fnfe:
        print(f'Could not find file {path}.\n Details: {fnfe}')

        return None
    except Exception as e:
        print('Unexpexcted error occured. Details: {e}')

        return None
    
