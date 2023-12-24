import pandas as pd

def load_excel_file(file_path):
    """
    Load an Excel file into a pandas DataFrame.
    """
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def merge_dataframes(df1, df2, key_column):
    """
    Merge two dataframes based on a key column. Only keep rows that are present in both dataframes.
    """
    return pd.merge(df1, df2, on=key_column, how='inner')

path_22_years_or_older = "C:/Excel Hockey Data/22yearsOrOlderFinal.xlsx"
summary_paths = [f'C:/Excel Hockey Data/Hockey/Summary ({i}).xlsx' for i in range(1, 29)]

df_22_years_or_older = load_excel_file(path_22_years_or_older)

if df_22_years_or_older is None:
    print("The 22 years or older dataframe could not be loaded.")
else:
    all_merged_data = pd.DataFrame()

    # Loop over summary files
    for summary_file_path in summary_paths:
        df_summary = load_excel_file(summary_file_path)
        
        if df_summary is not None:
            # Remove potential duplicates in the summary file
            df_summary.drop_duplicates(subset='Player', inplace=True)

            # Merge dataframes
            merged_df = merge_dataframes(df_22_years_or_older, df_summary, key_column='Player')
            all_merged_data = pd.concat([all_merged_data, merged_df], ignore_index=True)
    
    all_merged_data_unique = all_merged_data.drop_duplicates(subset='Player')

    output_file_path = "C:/Excel Hockey Data/FinalMergedFile.xlsx"
  
    all_merged_data_unique.to_excel(output_file_path, index=False)
    print("Merging completed. Total unique rows in the final DataFrame:", len(all_merged_data_unique))
