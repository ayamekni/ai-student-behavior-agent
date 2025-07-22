import pandas as pd

REQUIRED_COLUMNS = [
    'user_id', 'question_id', 'timestamp',
    'response_time', 'is_correct', 'topic'
]

def load_gameplay_data(file_path):
    """
    Loads and validates gameplay data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Cleaned and validated DataFrame.
        
    Raises:
        ValueError: If required columns are missing.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Validate required columns
    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    return df
