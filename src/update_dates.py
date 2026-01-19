import argparse
import os
from pathlib import Path
import frontmatter
from datetime import datetime

def update_markdown_dates(directory: str):
    """
    Recursively scans a directory for Markdown files and updates the 'date' in the front matter
    if the file's modification timestamp is more recent.
    """
    path = Path(directory)
    for file_path in path.rglob('*.md'):
        try:
            post = frontmatter.load(file_path)
            
            if 'date' in post.metadata:
                mtime = os.path.getmtime(file_path)
                mtime_dt = datetime.fromtimestamp(mtime)
                
                # Make the frontmatter date timezone-aware if it's not
                frontmatter_date = post.metadata['date']
                if isinstance(frontmatter_date, str):
                    # print("oops")   
                    frontmatter_date = datetime.fromisoformat(str(post.metadata['date']))
                if frontmatter_date.tzinfo is None:
                    # If the date from frontmatter is naive, assume local timezone for comparison    
                    frontmatter_date = frontmatter_date.astimezone()

                # Make the modification time timezone-aware
                mtime_dt = datetime.fromtimestamp(mtime).astimezone()  

                if mtime_dt > frontmatter_date:
                    print(f"Updating date for {file_path}")
                    post.metadata['date'] = mtime_dt
                    frontmatter.dump(post, file_path)
            else:
                # If there's no date, add it
                mtime = os.path.getmtime(file_path)
                mtime_dt = datetime.fromtimestamp(mtime).astimezone()
                post.metadata['date'] = mtime_dt
                frontmatter.dump(post, file_path)


        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Update the 'date' in the front matter of Markdown files.")
    parser.add_argument('directory', type=str, help='The directory to scan for Markdown files.')
    args = parser.parse_args()
    
    update_markdown_dates(args.directory)
