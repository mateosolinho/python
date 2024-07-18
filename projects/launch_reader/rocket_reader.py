import pandas as pd

def load_data_from_json(filename):
    try:
        df = pd.read_json(filename)
        return df
    except ValueError as e:
        print(f"Error loading JSON: {e}")
        return pd.DataFrame()

def extract_and_process_data(df):
    # Expand nested columns
    if 'results' in df.columns:
        df_expanded = pd.json_normalize(df['results'])
    else:
        print("Error: 'results' not found in JSON data.")
        return pd.DataFrame()
    
    # Select and rename the columns
    selected_columns = {
        'name': 'Name',
        'net': 'Date',
        'rocket.configuration.full_name': 'Rocket',
        'launch_service_provider.name': 'Provider',
        'pad.location.name': 'Pad',
        'mission.description': 'Mission Description',
        'mission.type': 'Mission Type',
        'status.name': 'Status',
        'failreason': 'Fail Reason',
        'image': 'Image',
    }
    
    df_selected = df_expanded[selected_columns.keys()].rename(columns=selected_columns)
    
    return df_selected

def display_data(df):
    print(df)

if __name__ == "__main__":
    filename = "C:/Users/mateo/Escritorio/python/projects/launch_reader/all_previous_launches.json"
    df = load_data_from_json(filename)
    df_processed = extract_and_process_data(df)
    
    # Mostrar los datos
    display_data(df_processed)
