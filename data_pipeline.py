import data_manipulations.data_cleaner as data_cleaner
import data_analysis.projects_analytics as projects_analytics

from data_loaders.files_loader import load_data_from_csv
from data_extractors.files_extractor import save_to_parquet
from config import PROJECTS_STUDIES_COHORTS_FILE, SUBJECTS_SAMPLES_FILE, SAMPLE_RUN_RESULTS_FILE

# --------------------------------------------
# Load data
# --------------------------------------------
print('Loading data...')

projects_studies_cohorts = load_data_from_csv(PROJECTS_STUDIES_COHORTS_FILE)
subject_samples = load_data_from_csv(SUBJECTS_SAMPLES_FILE)
samples_results = load_data_from_csv(SAMPLE_RUN_RESULTS_FILE)

if any(df is None for df in [projects_studies_cohorts, subject_samples, samples_results]):
    print('One or more datasets could not be loaded. Exiting the pipeline.')
    exit(1)

# Creating a dictionary to map original column names to their desired new names.
# This is to make the column names more consistent and easier to manage.
rename_dict = {
        'cancer_detected_(yes_no)': 'is_cancer_detected',
        ' detection_value ': 'detection_value',
        'sample_status(running/finished/failed)': 'sample_status',
        'fail_reason(technical/quality)': 'fail_reason',
        'date of run': 'date_of_run'
    }
    
samples_results.rename(columns=rename_dict, inplace=True)

print('Data loaded successfully.')

# --------------------------------------------
# Clean data
# --------------------------------------------
print('Start cleaning data...')

projects_studies_cohorts = data_cleaner.basic_cleanup(projects_studies_cohorts)
subject_samples = data_cleaner.clean_subject_samples_df(subject_samples)
samples_results = data_cleaner.clean_samples_results_df(samples_results)

print('Data cleaned successfully.')

# --------------------------------------------
# Merge data
# --------------------------------------------
print('Merging the dataframes...')

merged_df = projects_studies_cohorts.merge(subject_samples, on=['project_code', 'study_code', 'study_cohort_code'], how='left')\
                                        .merge(samples_results, on='sample_id', how='left')

print('Dataframes merged successfully.')

# --------------------------------------------
# Save the cleaned and merged dataframe to a Parquet file
# --------------------------------------------
print('Saving the merged dataframe to a Parquet file...')

output_file_path = save_to_parquet(merged_df, 'output.parquet')

print(f'Data saved successfully to {output_file_path}.')

# --------------------------------------------
# Generate project summaries
# --------------------------------------------
print('Generating project summaries...')

project_summaries_path = projects_analytics.generate_project_summaries(merged_df)

print(f'Project summaries generated successfully. Saved to {project_summaries_path}.')
print('Pipeline finished successfully.')


