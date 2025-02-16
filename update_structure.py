import os
import json
import shutil
import re

def clean_filename(name):
    """Convert filename to clean lowercase with no special characters"""
    return ''.join(c.lower() for c in name if c.isalnum())

def update_repo_structure():
    print("Starting repository update...")

    # Create data directories if they don't exist
    os.makedirs('data/businesses', exist_ok=True)

    # First clean business filenames
    business_count = 0
    for filename in os.listdir('output/businesses'):
        if filename.endswith('.json'):
            # Clean the filename
            old_path = f'output/businesses/{filename}'
            new_filename = clean_filename(filename.replace('.json', '')) + '.json'
            new_path = f'data/businesses/{new_filename}'

            # Copy with new filename
            shutil.copy(old_path, new_path)
            business_count += 1
            print(f"Copied {filename} → {new_filename}")

            # Read the file
            with open(f'output/businesses/{filename}', 'r') as f:
                data = json.load(f)

            # Clean the name for site_id
            clean_name = clean_filename(data['basic_info']['name'])

            # Update the site_id
            if 'ids' in data:
                data['ids']['site_id'] = clean_name

            #Write the updated data back to the file.  This was missing from the original.
            with open(new_path, 'w') as f:
                json.dump(data, f, indent=4)


    # Copy metadata
    if os.path.exists('output/metadata.json'):
        shutil.copy('output/metadata.json', 'data/metadata.json')
        print("Copied metadata.json")

    print(f"\nRepository structure updated!")
    print(f"Processed {business_count} business files")
    print("\nNow run:")
    print("git add .")
    print("git commit -m \"Update repository structure with clean filenames\"")
    print("git push")

if __name__ == "__main__":
    update_repo_structure()