import pandas as pd

# Base path for the summary files
summary_base_path = 'C:/Excel Hockey Data/Hockey/Summary ({index}).xlsx'

# Load the file with all the players under 21
under_21_file_path = "C:/Excel Hockey Data/Under21RookieStats.xlsx"
under_21_data = pd.read_excel(under_21_file_path)

# Initialize an empty DataFrame to hold the merged data
merged_data = pd.DataFrame()

# Loop through the range of summary files
for i in range(1, 29):
    # Construct the file path for the current summary file
    current_file_path = summary_base_path.format(index=i)
    try:
        # Load the current summary file
        summary_data = pd.read_excel(current_file_path)
        
        # Merge with the under 21 players data
        merged = pd.merge(under_21_data, summary_data, how='inner', on='Player')  # Replace 'common_identifier' with the actual column name used for matching

        # Concatenate with the previously merged data
        merged_data = pd.concat([merged_data, merged], ignore_index=True)
    except Exception as e:
        print(f"Error reading file {current_file_path}: {e}")

# Save the merged data to a new Excel file
output_file_path = "C:/Excel Hockey Data/Under21RookieStatsFinal.xlsx" # Replace with your desired save location
merged_data.to_excel(output_file_path, index=False)

print(f"File saved: {output_file_path}")
  
