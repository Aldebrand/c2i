import os

def save_to_parquet(df, filename, output_folder='output'):
    """
    Save the given dataframe to a Parquet file in the specified output folder.

    :param df: Pandas dataframe to be saved
    :param filename: Name of the Parquet file
    :param output_folder: Folder where the Parquet file will be saved (default is 'output')

    :return: Full path of the saved Parquet file or None if an error occured
    """
    try:
        # Ensure the output directory exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        parquet_path = os.path.join(output_folder, filename)
        df.to_parquet(parquet_path, index=False)
        
        return parquet_path
    except Exception as e:
        print(f'Error while saving to Parquet file. Details: {e}')
        
        return None

def save_to_csv(df, filename, output_folder='output', na_rep='N/A'):
    """
    Save the given dataframe to a csv file in the specified output folder.

    :param df: Pandas dataframe to be saved
    :param filename: Name of the csv file
    :param output_folder: Folder where the csv file will be saved (default is 'output')

    :return: Full path of the saved csv file or None if an error occured
    """
    try:

        # Ensure the output directory exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        csv_path = os.path.join(output_folder, filename)
        df.reset_index(drop=True, inplace=True)
        
        df.to_csv(csv_path, index=False, na_rep=na_rep)
        
        return csv_path
    
    except Exception as e:
        print(f'Error while saving to csv file. Details: {e}')
        
        return None
