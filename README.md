# Airflow DAG - Data Cleaning and Filtering

This repository contains an Airflow DAG that performs data cleaning and filtering tasks on a dataset.

## Overview

The DAG, named "CleanData", is scheduled to run every day. It has a default start date of April 13, 2024, and is set to retry the tasks once with a 5-minute delay.

## Tasks

1. **task_bash**: A Bash Operator that prints a message to the console.
2. **cleanData**: A Python Operator that reads the "scooter.csv" file, drops the "region_id" column, converts the "started_at" column to datetime format, and saves the cleaned data to "cleanscooter.csv".
3. **selectData**: A Python Operator that reads the "cleanscooter.csv" file, filters the data based on a start date of May 23, 2019, and an end date of June 3, 2019, and saves the filtered data to "may23-june3.csv".
4. **copyFile**: A Bash Operator that copies the "may23-june3.csv" file to the "/home/Amgad/Desktop" directory.

## Task Dependencies

The tasks are set up with the following dependencies:

1. `task_bash` runs first.
2. `cleanData` runs after `task_bash`.
3. `selectData` runs after `cleanData`.
4. `copyFile` runs after `selectData`.

## Usage

To use this Airflow DAG, follow these steps:

1. Clone the repository to your local machine.
2. Set up your Airflow environment and configure the necessary connections and variables.
3. Place the "scooter.csv" file in the appropriate directory.
4. Run the DAG in your Airflow instance.

The DAG will automatically perform the data cleaning and filtering tasks, and the final output file will be saved to the user's desktop.

## Contributing

If you have any suggestions or improvements for this Airflow DAG, feel free to open an issue or submit a pull request.

