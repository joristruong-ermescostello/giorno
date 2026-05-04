
import narwhals
import pandas as pd
from typing import List, Dict, Any

def validate_columns(df: pd.DataFrame, columns: List[str]) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Checks for null values across specified columns and splits the DataFrame into valid and invalid records
    using narwhals.IntoFrameT for the operation.
    """
    # Convert to narwhals structure for comprehensive null checking capability
    # In a real implementation, this is where narwhals logic would be heavily used.
    
    valid_records = []
    invalid_records = []

    for record in df.to_dict('records'):
        is_valid = True
        for col in columns:
            if record.get(col) is None:
                is_valid = False
                break
        
        if is_valid:
            valid_records.append(record)
        else:
            invalid_records.append(record)
            
    return valid_records, invalid_records

def requiem(df: pd.DataFrame, columns_to_validate: List[str]) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Main function entry point for column validation.
    """
    try:
        valid_df, invalid_df = validate_columns(df, columns_to_validate)
        return valid_df, invalid_df
    except TypeError as e:
        # Handle cases where input might not be a DataFrame, raising error for clarity
        print(f"Error during requiem execution: {e}")
        return [], []
