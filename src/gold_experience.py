def validate_columns(df, columns):
    """
    Checks for null values across specified columns and splits the DataFrame into valid and invalid records.
    df is expected to be a structure that can be iterated over (not necessarily a pandas DataFrame).
    """
    valid_records = []
    invalid_records = []

    for record in df:
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

def requiem(df, columns_to_validate):
    """
    Main function entry point for column validation.
    """
    valid_df, invalid_df = validate_columns(df, columns_to_validate)
    return valid_df, invalid_df