

                



           
           
           
import os
import json
import shutil

def update_repo_structure():
    print("Starting repository update...")

    # Create data directory structure if it doesn't exist
    os.makedirs('data/businesses', exist_ok=True)

    # Move files to correct structure
    if os.path.exists('output/metadata.json'):
        shutil.copy('output/metadata.json', 'data/metadata.json')
        print("Copied metadata.json to data/")

    # Copy all business files
    business_count = 0
    for filename in os.listdir('output/businesses'):
        if filename.endswith('.json'):
            shutil.copy(
                f'output/businesses/{filename}',
                f'data/businesses/{filename}'
            )
            business_count += 1

    print(f"Copied {business_count} business files to data/businesses/")
    print("\nRepository structure updated!")
    print("\nNow you can:")
    print("1. Use 'git add .' to stage all changes")
    print("2. Use 'git commit -m \"Update repository structure\"' to commit")
    print("3. Use 'git push' to push changes")

if __name__ == "__main__":
    update_repo_structure()
