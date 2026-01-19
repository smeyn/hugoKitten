
import os
import re
import shutil



def delete_directory_contents(directory_path):
    """
    Deletes a directory and all its contents, including subdirectories.

    Args:
        directory_path (str): The path to the directory to delete.
    """
    
    # --- Safety Check 1: Verify the path exists and is a directory ---
    if not os.path.isdir(directory_path):
        print(f"Error: The path '{directory_path}' is not a valid directory.")
        return

    try:
        # The shutil.rmtree() function recursively deletes the directory.
        shutil.rmtree(directory_path)
        print(f"Successfully deleted '{directory_path}'.")
    except OSError as e:
        print(f"Error deleting directory '{directory_path}': {e}")

source_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'kitten', 'content'))
target_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'target'))
results_dir = os.path.join(target_base_dir, 'results')

print(f"Source directory: {source_base_dir}")
print(f"Target directory for results: {results_dir}")

delete_directory_contents(results_dir)

# Create the results directory if it doesn't exist
os.makedirs(results_dir, exist_ok=True)

# Regex to find bolded text like **Word**
# It captures the text inside the double asterisks
bold_regex = re.compile(r'\*\*(.*?)\*\*')

# --- Pre-scan to find all existing cleaned markdown filenames ---
existing_cleaned_files = set()
for r, _, fnames in os.walk(source_base_dir):
    for fname in fnames:
        if fname.endswith('.md'):
            # Clean the filename using the same logic as the link generation
            cleaned_name = fname.lower().replace(':', '').replace(' ', '_')
            existing_cleaned_files.add(cleaned_name)

processed_files_count = 0
for root, _, files in os.walk(source_base_dir):
    for file_name in files:
        if file_name.endswith('.md'):
            source_file_path = os.path.join(root, file_name)

            # Determine the relative path from the source_base_dir
            relative_path = os.path.relpath(source_file_path, source_base_dir)
            target_file_path = os.path.join(results_dir, relative_path)

            # Ensure the subdirectory structure exists in the target
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

            try:
                with open(source_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Function to perform the replacement for each match
                def replace_bold_with_link(match):
                    original_text = match.group(1)
                    
                    # Clean the link text to check for file existence.
                    link_text_base = original_text.lower().replace(':', '').replace(' ', '_')
                    
                    # The filename to check for existence must match the cleaned names in the set
                    filename_to_check = link_text_base
                    if not filename_to_check.endswith('.md'):
                        filename_to_check += '.md'

                    # Check if the cleaned file exists in our set
                    if filename_to_check in existing_cleaned_files:
                        # It exists, so create the Hugo relref link.
                        # The relref link itself should  contain the .md extension.
                        # return f'[{original_text}]({{< relref "{link_text_base}" >}})'
                        return f'[{original_text}]( '+ '{{< relref "' + link_text_base + '.md" >}})'
                    else:
                        # It doesn't exist, so return the original bolded text
                        return match.group(0)

                new_content = bold_regex.sub(replace_bold_with_link, content)

                with open(target_file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"Processed and saved: {source_file_path} -> {target_file_path}")
                processed_files_count += 1

            except Exception as e:
                print(f"Error processing {source_file_path}: {e}")

print(f"\nFinished processing. Total .md files processed: {processed_files_count}")
