from data_extractors.files_extractor import save_to_csv

def generate_project_summaries(df):
    """
    Generate a CSV summary file for each project-sutdy-cohort combination.

    :param df: Pandas dataframe - the dataframe that contains the projects data.

    :return: A list of the full paths of the generated CSV files.
    """
    grouped = df.groupby(['project_code', 'study_code', 'study_cohort_code'])

    aggregations = {
        'sample_id': 'count',
        'sample_status': lambda statuses: (statuses.str.lower()=='finished').sum() / len(statuses) * 100,
        'detection_value': lambda detection_values: detection_values[detection_values > 0].min() if not detection_values[detection_values > 0].empty else None,
    }

    summary = grouped.agg(aggregations)
    summary.columns = ['total_samples', 'percentage_finished', 'min_detected_value']

    # Formatting the percentage_finished column to have two decimal places followed by a percentage sign
    summary['percentage_finished'] = summary['percentage_finished'].apply(lambda x: "{:.2f}%".format(x))

    # Saving the summary to a single CSV file
    file_name = 'summary.csv'
    output_file_path = save_to_csv(summary.reset_index(), file_name)

    return output_file_path