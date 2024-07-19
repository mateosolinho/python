import requests
import json
import time

def fetch_data_from_url(url, batch_size=15):
    """Fetch data from the URL with pagination support."""
    all_results = []
    while url and batch_size > 0:
        print(f"\n[+] Fetching data from: {url}")  # Show current URL
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            if results:
                all_results.extend(results)
                next_url = data.get('next')
                batch_size -= 1
                url = next_url  # Get the next page URL
                time.sleep(1)  # Sleep to avoid hitting rate limits
            else:
                # Break loop if no results are found
                break
        else:
            print(f"Error: {response.status_code}")
            break
    return all_results, url

def load_existing_data(filename):
    """Load existing data from the JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []

def save_data_to_file(data, filename):
    """Save data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print(f"Data saved to {filename}")

def save_progress(url, filename):
    """Save the progress URL to a file."""
    with open(filename, 'w') as file:
        json.dump({'next_url': url}, file)
    print(f"Progress saved to {filename}")

def load_progress(filename):
    """Load the progress URL from a file."""
    try:
        with open(filename, 'r') as file:
            progress = json.load(file)
            return progress.get('next_url')
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return None

def merge_data(existing_data, new_data):
    """Merge new data into existing data, avoiding duplicates."""
    existing_ids = {item['id'] for item in existing_data}
    merged_data = existing_data.copy()
    
    for item in new_data:
        if item['id'] not in existing_ids:
            merged_data.append(item)
            existing_ids.add(item['id'])
    
    return merged_data

def main():
    filename = "new_previous_launches.json"
    progress_filename = "progress.json"
    base_url = "https://ll.thespacedevs.com/2.2.0/launch/previous/?limit=1&offset="
    
    # Load existing data
    existing_data = load_existing_data(filename)
    
    # Load progress
    next_url = load_progress(progress_filename)
    if next_url is None:
        # Start from the initial offset if no progress is found /////////////////////// FECHA 18/07/2024
        current_offset = 0
        next_url = base_url + str(current_offset)
    else:
        # Extract the current offset from the URL if resuming
        current_offset = int(next_url.split('offset=')[1])
    
    # Download new data in batches
    total_downloaded = 0
    while True:
        print(f"Current offset URL: {next_url}")  # Show current URL or offset
        new_data, next_url = fetch_data_from_url(next_url, batch_size=15)
        
        if not new_data:
            print("No new data available at this offset.")
            # If no data is found, we need to retry with the same offset in the next run.
            save_progress(next_url, progress_filename)
            break

        # Merge new data with existing data
        existing_data = merge_data(existing_data, new_data)
        total_downloaded += len(new_data)
        print(f"Downloaded {total_downloaded} new records")

        # Update the offset for the next request
        current_offset += 1
        next_url = base_url + str(current_offset)

        # Save progress
        save_progress(next_url, progress_filename)

    # Save updated data to file
    save_data_to_file(existing_data, filename)

if __name__ == "__main__":
    main()
