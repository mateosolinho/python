import pandas as pd
import mysql.connector
from mysql.connector import Error

def load_data_from_json(filename):
    try:
        df = pd.read_json(filename)
        return df
    except ValueError as e:
        print(f"Error loading JSON: {e}")
        return pd.DataFrame()

def extract_and_process_data(df):
    if 'results' in df.columns:
        df_expanded = pd.json_normalize(df['results'])
    else:
        print("Error: 'results' not found in JSON data.")
        return pd.DataFrame()
    
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
    
    missing_columns = set(selected_columns.keys()) - set(df_expanded.columns)
    if missing_columns:
        print(f"Warning: Missing columns in the data: {', '.join(missing_columns)}")
    
    df_selected = df_expanded[[col for col in selected_columns.keys() if col in df_expanded.columns]]
    df_selected = df_selected.rename(columns=selected_columns)
    
    return df_selected

def insert_data_to_mysql(df, host, database, user, batch_size=1000):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            create_table_query = """
            CREATE TABLE IF NOT EXISTS launches (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Date DATETIME,
                Rocket VARCHAR(255),
                Provider VARCHAR(255),
                Pad VARCHAR(255),
                Mission_Description TEXT,
                Mission_Type VARCHAR(255),
                Status VARCHAR(255),
                Fail_Reason TEXT,
                Image VARCHAR(255)
            );
            """
            cursor.execute(create_table_query)
            
            # Empty the table before inserting new data
            cursor.execute("TRUNCATE TABLE launches;")
            
            insert_query = """
            INSERT INTO launches (Name, Date, Rocket, Provider, Pad, Mission_Description, Mission_Type, Status, Fail_Reason, Image)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            total_rows = len(df)
            inserted_rows = 0
            
            for start in range(0, total_rows, batch_size):
                end = min(start + batch_size, total_rows)
                batch = df.iloc[start:end]
                
                # Convert NaN to None for SQL compatibility
                batch_data = [tuple(None if pd.isna(x) else x for x in row) for row in batch.itertuples(index=False)]
                
                try:
                    cursor.executemany(insert_query, batch_data)
                    connection.commit()
                    inserted_rows += len(batch)
                    print(f"Inserted rows from {start} to {end}, total inserted: {inserted_rows}/{total_rows}")
                except Error as e:
                    print(f"Error inserting rows from {start} to {end}: {e}")
            
            print(f"Data insertion completed. Total rows inserted: {inserted_rows}")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    filename = "C:/Users/mateo/Escritorio/python/projects/launch_reader/all_previous_launches.json"
    df = load_data_from_json(filename)
    df_processed = extract_and_process_data(df)
    
    mysql_host = "localhost"
    mysql_database = "launch_db"
    mysql_user = "root"
    
    if not df_processed.empty:
        insert_data_to_mysql(df_processed, mysql_host, mysql_database, mysql_user)
    else:
        print("No data to insert.")
