"""make links for Hugo pages"""


import os
import re
import shutil
import argparse

import glob


SOURCE_DIR = 'kitten/content'
TARGET_DIR = 'out'
CLEAR_BEFORE = True
# Regex to find bolded text like **Word**
# It captures the text inside the double asterisks
bold_regex = re.compile(r'\*\*(.*?)\*\*')


def get_existing_files (source_dir:str)->set:
    result = {}
    offset = len(source_dir.split('/'))
    for r, _, fnames in os.walk(source_dir):
        for fname in fnames:
            if fname.endswith('.md'):
                subpath = '/'.join(r.split('/')[offset:])
                if subpath:
                    rel_path = os.path.join(subpath, fname)
                else:
                    rel_path =  fname
                result[fname.lower()] = rel_path
    return result



def upgrade_file(path: str, source_dir, overwrite:bool, destination:str|None)->None:    
    """parse markdown file and replace bolded words with links to appropriate md file"""
    global nr_changes 
    nr_changes = 0
    existing_files = get_existing_files(source_dir)
    full_path = os.path.join(source_dir, path)
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Function to perform the replacement for each match
    def replace_bold_with_link(match):
        global nr_changes
        original_text = match.group(1)
        
        # Clean the link text to check for file existence.
        link_text_base = original_text.lower().replace(':', '').replace(' ', '_')
        
        # The filename to check for existence must match the cleaned names in the set
        filename_to_check = link_text_base
        if not filename_to_check.endswith('.md'):
            filename_to_check += '.md'

        # Check if the cleaned file exists in our set
        if filename_to_check in existing_files:
            # It exists, so create the Hugo relref link.
            # The relref link itself should  contain the .md extension.
            # return f'[{original_text}]({{< relref "{link_text_base}" >}})'
            nr_changes += 1
            return f'[{original_text}]( '+ '{{< relref "' + existing_files[filename_to_check] + '" >}})'
        elif filename_to_check[:-3].endswith('s'):
            filename_to_check=  filename_to_check[:-4] + '.md'
            if filename_to_check in existing_files:
                nr_changes += 1
                return f'[{original_text}]( '+ '{{< relref "' + existing_files[filename_to_check] + '" >}})'
        # It doesn't exist, so return the original bolded text
        return match.group(0)
    
    new_content = bold_regex.sub(replace_bold_with_link, content)
    if nr_changes == 0:
        print (f"No changes made to {path}")
        return
    if destination:
        if destination.endswith('.md'):
            target_file_path = destination
        else:
            target_file_path = os.path.join(destination, os.path.basename(full_path))
    elif overwrite:
        target_file_path = full_path
        # rename existing
        bak_path = full_path+'.bak'
        while os.path.exists(bak_path):
            bak_path = bak_path+'.bak'
        os.rename(full_path, bak_path)
    else:
        target_file_path = full_path + '.new'
    with open(target_file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Processed with {nr_changes} changes and saved: {full_path} -> {target_file_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process files for Hugo pages.")
    parser.add_argument('file_pattern', type=str,
                        help='Path to the file to process (relative to source dir).')
    parser.add_argument('--source_dir', type=str, default=SOURCE_DIR,
                        help='content directory.')
    parser.add_argument('--overwrite', action='store_true',
                        help='Overwrite existing files without prompting.')
    parser.add_argument('--dest', type=str,
                        help='destination for output')
    args = parser.parse_args()
    
    search_path = os.path.join(args.source_dir, args.file_pattern)
    files_to_process = glob.glob(search_path, recursive=True)

    if not files_to_process:
        print(f'No files found matching "{args.file_pattern}" in {args.source_dir}')
    else:
        print(f"Files to process: {len(files_to_process)}")
        print(f"Overwrite mode: {args.overwrite}")
        for file_path in files_to_process:
            relative_path = os.path.relpath(file_path, args.source_dir)
            upgrade_file(relative_path, args.source_dir, args.overwrite, args.dest)