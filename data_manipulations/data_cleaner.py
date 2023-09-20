import pandas as pd

def basic_cleanup(df):
    """
    Basic cleanup of dataframe

    :param df: Pandas dataframe

    :return: Pandas dataframe
    """
    df.drop_duplicates(inplace=True)
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    return df

def clean_subject_samples_df(df):
    """
    Clean subject samples dataframe and convert subject_id and sample_id to int

    :param df: Pandas dataframe - the subject samples dataframe

    :return: The cleaned dataframe
    """
    df = basic_cleanup(df)
    df['subject_id'] = df['subject_id'].astype(int)
    df['sample_id'] = df['sample_id'].astype(int)

    return df

def clean_samples_results_df(df):
    """
    Clean samples results dataframe.
    Fill missing values with appropriate values and convert date of run to datetime object.

    :param df: Pandas dataframe - the samples results dataframe

    :return: The cleaned dataframe
    """
    df = basic_cleanup(df)

    # try:
    #     df['detection_value'] = df['detection_value'].astype(float)
    # except ValueError:
    #     problematic_values = df['detection_value'].apply(lambda x: not isinstance(x, (int, float)) and not isinstance(x, str) and not x.replace('.', '', 1).isdigit())
        
    #     print(f"Found problematic values in 'detection_value': {df[problematic_values]['detection_value'].unique()}")
    #     df = df[~problematic_values] # Remove problematic values

    df['detection_value'] = pd.to_numeric(df['detection_value'], errors='coerce')
    df['is_cancer_detected'].fillna('NA', inplace=True)
    df['detection_value'].fillna(0, inplace=True)
    df['sample_quality'].fillna(df['sample_quality'].median(), inplace=True)
    df['fail_reason'].fillna('Not Applicable', inplace=True)
    df['date_of_run'] = pd.to_datetime(df['date_of_run'], dayfirst=True)
    
    return df

