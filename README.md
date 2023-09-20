# C2i Genomics Data Engineer Assignment Solution

Welcome to the solution for the C2i Genomics Data Engineer Assignment! This solution is designed to read data from three input CSV files, perform data integration by joining the information from these files, ensure data cleanliness, and finally, produce a Parquet file and a summary CSV as the output. This entire pipeline is encapsulated within a Docker container for easy deployment and execution.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Data Pipeline](#running-the-data-pipeline)
- [Input Data](#input-data)
- [Feedback and Queries](#feedback-and-queries)

## Prerequisites

Before proceeding, ensure you have the following software installed on your machine:

1. **Docker**: If Docker isn't installed, you can get it from [Docker's official site](https://docs.docker.com/get-docker/).
2. **Git**: If you don't have Git installed, follow the guide [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to set it up.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Aldebrand/c2i.git
   cd c2i
   ```

2. Build the Docker image:
   ```bash
   docker build -t c2i-data-pipeline .
   ```

## Running the Data Pipeline

Once the Docker image is built, you can run the data pipeline as follows:

```bash
docker run c2i-data-pipeline
```

Post successful execution, you'll find two output files in the `output` directory: 
- `output.parquet`: A merged output in Parquet format.
- `summary.csv`: A summarized CSV file providing insights per project, study, and cohort.

## Input Data

The data pipeline works with three primary CSV input files:

1. **Projects, Studies, and Cohorts (CSV 1)**:
   
   - Each project is managed by a designated project manager.
   - A project may consist of multiple studies.
   - Each study can include several cohorts.
   - Records are uniquely identified by the combination of Project code, Study code, and Cohort code.

2. **Subjects and Samples (CSV 2)**:

   - Each subject belongs to a specific cohort.
   - A subject can have multiple associated samples.

3. **Sample Processing Results (CSV 3)**:

   The main columns include:
   - `cancer_detected_(yes_no_na)`: Indicates cancer detection in the sample.
   - `detection_value`: Represents the magnitude of detected cancer (0 to 1 range).
   - `sample_quality`: Measures sample quality (0 to 1 range).
   - `sample_quality_minimum_threshold`: Specifies the threshold for low-quality samples.
   - `sample_status`: Status of the sample (running, finished, or failed).
   - `fail_reason`: Reason for sample failure (technical or quality-based).
   - `date_of_run`: Date of sample processing.

## Feedback and Queries

For feedback or questions regarding this solution, please reach out to me, Or Chen, at [archybald9@gmail.com](mailto:archybald9@gmail.com).