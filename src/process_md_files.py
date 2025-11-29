
import os
import re
import shutil

source_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'kitten', 'content'))
target_base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'target'))
results_dir = os.path.join(target_base_dir, 'results')

print(f"Source directory: {source_base_dir}")
print(f"Target directory for results: {results_dir}")

# Create the results directory if it doesn't exist
os.makedirs(results_dir, exist_ok=True)

# Regex to find bolded text like **Word**
# It captures the text inside the double asterisks
bold_regex = re.compile(r'\*\*(.*?)\*\*')

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
                    # Convert to lowercase for the link, as specified in the example `worship` -> `Worship`
                    link_text = original_text.lower()
                    return f'[{original_text}]({{< "{link_text}" >}})'

                new_content = bold_regex.sub(replace_bold_with_link, content)

                with open(target_file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f"Processed and saved: {source_file_path} -> {target_file_path}")
                processed_files_count += 1

            except Exception as e:
                print(f"Error processing {source_file_path}: {e}")

print(f"\nFinished processing. Total .md files processed: {processed_files_count}")
