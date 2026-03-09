import dearpygui.dearpygui as dpg
import os
import datetime
import frontmatter # For handling front matter in markdown files
import argparse
from date_picker import DatePicker

# --- Configuration ---
CONTENT_ROOT = "content" # This will be updated by the command-line argument
MD_FILE_EXTENSION = ".md"

# --- Global State ---
selected_category = None
selected_file_path = None
# Store all front matter fields, not just the default ones
current_front_matter_data = {}
date_input = None

# --- Helper Functions ---
def get_categories():
    """Returns a list of subdirectories under CONTENT_ROOT."""
    if not os.path.exists(CONTENT_ROOT) or not os.path.isdir(CONTENT_ROOT):
        return []
    return sorted([d for d in os.listdir(CONTENT_ROOT) if os.path.isdir(os.path.join(CONTENT_ROOT, d))])

def get_md_files_in_category(category_name):
    """Returns a list of markdown files in the specified category directory."""
    category_path = os.path.join(CONTENT_ROOT, category_name)
    if not os.path.exists(category_path) or not os.path.isdir(category_path):
        return []
    return sorted([f for f in os.listdir(category_path) if f.endswith(MD_FILE_EXTENSION) and os.path.isfile(os.path.join(category_path, f))])

def parse_markdown_file(file_path):
    """Parses a markdown file, separating front matter and content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        return post.metadata, post.content
    except Exception as e:
        print(f"Error parsing file {file_path}: {e}")
        return {}, ""

def construct_markdown_file(metadata, content):
    """Constructs a markdown file content from metadata and content."""
    post = frontmatter.Post(content, **metadata)
    return frontmatter.dumps(post)

def show_message(title, message):
    """Displays a simple message box."""
    # with dpg.window(label=title, modal=True, autosize=True, no_close=True):
        # dpg.add_text(message)
        # dpg.add_button(label="OK", width=75, callback=lambda: dpg.delete_item(dpg.last_item()))
    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Left, modal=True, tag="modal_id"):
        dpg.add_text(message)
        dpg.add_button(label="Close", callback=lambda: dpg.configure_item("modal_id", show=False))

# --- Callbacks ---
def load_categories_ui():
    """Populates the categories listbox."""
    categories = get_categories()
    dpg.configure_item("category_list", items=categories)
    # Clear file list and editor if no categories or current selection is invalid
    if not categories or (selected_category and selected_category not in categories):
        dpg.configure_item("file_list", items=[])
        clear_editor()

def category_selected_callback(sender, app_data, user_data):
    """Handles selection of a category."""
    global selected_category
    selected_category = dpg.get_value(sender)
    
    md_files = get_md_files_in_category(selected_category)
    dpg.configure_item("file_list", items=md_files)
    clear_editor() # Clear editor when category changes

def file_selected_callback(sender, app_data, user_data):
    """Handles selection of a markdown file."""
    global selected_file_path, current_front_matter_data,date_input

    filename = dpg.get_value(sender)
    if not selected_category or not filename:
        return

    selected_file_path = os.path.join(CONTENT_ROOT, selected_category, filename)
    
    metadata, content = parse_markdown_file(selected_file_path)
    current_front_matter_data = metadata # Store all metadata

    # Populate default front matter fields
    dpg.set_value("title_input", current_front_matter_data.get('title', ''))
    
    # Handle date picker
    date_val = current_front_matter_data.get('date', datetime.date.today())
    if isinstance(date_val, str):
        try:
            if 'T' in date_val: # Handle ISO format with time
                date_val = datetime.datetime.fromisoformat(date_val.replace('Z', '+00:00')).date()
            else:
                date_val = datetime.date.fromisoformat(date_val)
        except ValueError:
            date_val = datetime.date.today()
    elif isinstance(date_val, datetime.datetime):
        date_val = date_val.date()
    
    # dpg.set_value("date_input", {'month_day': date_val.day, 'year': date_val.year, 'month': date_val.month-1})
    date_input.set_value(date_val)

    dpg.set_value("draft_checkbox", current_front_matter_data.get('draft', True))

    # Populate body content
    dpg.set_value("body_editor", content)

    # Update path display
    dpg.set_value("selected_file_path_text", f"Editing: {selected_file_path}")

    # Enable editor fields
    enable_editor(True)

def save_file_callback():
    """Saves the current file with updated front matter and content."""
    global date_input
    if not selected_file_path:
        show_message("Error", "No file selected to save.")
        return

    # Update current_front_matter_data with values from UI
    current_front_matter_data['title'] = dpg.get_value("title_input")

    date_dict = date_input.get_value( )
    # Month is 0-indexed in the widget, so add 1 for datetime object
    save_date = date_dict# datetime.date(date_dict['year'], date_dict['month'] + 1, date_dict['month_day'])
    current_front_matter_data['date'] = save_date

    current_front_matter_data['draft'] = dpg.get_value("draft_checkbox")

    body_content = dpg.get_value("body_editor")

    try:
        new_file_content = construct_markdown_file(current_front_matter_data, body_content)
        with open(selected_file_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        show_message("Success", f"File saved: {os.path.basename(selected_file_path)}")
    except Exception as e:
        show_message("Error", f"Failed to save file: {e}")

def create_new_file_dialog():
    """Opens a modal dialog to create a new file."""
    if not selected_category:
        show_message("Error", "Please select a category first to create a new file.")
        return

    with dpg.window(label="New Markdown File", modal=True, autosize=True, no_close=True, tag="new_file_modal"):
        dpg.add_text("Enter new filename (e.g., MyNewPost.md):")
        dpg.add_input_text(tag="new_filename_input", hint="filename.md", width=200)
        dpg.add_button(label="Create", callback=create_new_file_action)
        dpg.add_same_line()
        dpg.add_button(label="Cancel", callback=lambda: dpg.delete_item("new_file_modal"))

def create_new_file_action():
    """Action to create the new markdown file."""
    global selected_file_path
    new_filename = dpg.get_value("new_filename_input").strip()
    dpg.delete_item("new_file_modal") # Close the modal immediately

    if not new_filename:
        show_message("Error", "Filename cannot be empty.")
        return

    if not new_filename.endswith(MD_FILE_EXTENSION):
        new_filename += MD_FILE_EXTENSION

    new_full_path = os.path.join(CONTENT_ROOT, selected_category, new_filename)

    if os.path.exists(new_full_path):
        show_message("Error", f"File '{new_filename}' already exists in '{selected_category}'.")
        return

    # Default front matter for new file
    default_metadata = {
        'title': new_filename.replace(MD_FILE_EXTENSION, '').replace('-', ' ').title(),
        'date': datetime.date.today().isoformat(),
        'draft': True
    }
    default_content = "<!-- Write your content here -->\n"

    try:
        new_file_content = construct_markdown_file(default_metadata, default_content)
        with open(new_full_path, 'w', encoding='utf-8') as f:
            f.write(new_file_content)
        show_message("Success", f"New file created: {new_filename}")
        
        # Refresh file list and select the new file
        md_files = get_md_files_in_category(selected_category)
        dpg.configure_item("file_list", items=md_files)
        # Attempt to select the newly created file (requires dpg.set_value on listbox)
        # This is a bit tricky as listbox doesn't have a direct 'select by item' method
        # A simpler approach for now is just to refresh the list. User can click it.
        # Alternatively, programmatically find the index and set it.
    except Exception as e:
        show_message("Error", f"Failed to create new file: {e}")

def clear_editor():
    """Clears all editor fields and disables them."""
    global selected_file_path, current_front_matter_data, date_input

    selected_file_path = None
    current_front_matter_data = {}
    dpg.set_value("title_input", "")
    
    today = datetime.date.today()
    date_input.set_value(today)
    # dpg.set_value("date_input", {'month_day': today.day, 'year': today.year, 'month': today.month-1})

    dpg.set_value("draft_checkbox", False)
    dpg.set_value("body_editor", "")
    dpg.set_value("selected_file_path_text", "Editing: None")
    enable_editor(False)

def enable_editor(enable: bool):
    """Enables or disables editor input fields."""
    dpg.configure_item("title_input", enabled=enable)
    # dpg.configure_item("date_input", enabled=enable)
    dpg.configure_item("draft_checkbox", enabled=enable)
    dpg.configure_item("body_editor", enabled=enable)
    dpg.configure_item("save_button", enabled=enable)

# --- Dear PyGui Setup ---
def setup_dearpygui(content_root_path):
    global CONTENT_ROOT, date_input
    CONTENT_ROOT = content_root_path

    dpg.create_context()
    dpg.create_viewport(title="Hugo Markdown Editor", width=1200, height=800)
    dpg.setup_dearpygui()

    with dpg.window(label="Hugo Editor", tag="main_window", autosize=True, no_resize=True, no_move=True):
        dpg.set_primary_window("main_window", True)
        
        # Ensure content directory exists
        if not os.path.exists(CONTENT_ROOT) or not os.path.isdir(CONTENT_ROOT):
            dpg.add_text(f"Error: Content directory '{CONTENT_ROOT}' not found.", color=[255, 0, 0])
            dpg.add_text("Please run from your Hugo root or specify the path with the --root argument.")
            dpg.show_viewport()
            dpg.start_dearpygui()
            dpg.destroy_context()
            return

        with dpg.group(horizontal=True):
            # Left Panel: Navigation
            with dpg.child_window(width=300, border=False):
                dpg.add_text("Categories:")
                dpg.add_listbox(items=[], num_items=10, tag="category_list", callback=category_selected_callback)
                dpg.add_spacer(height=5)
                # dpg.add_spacing(count=5)
                dpg.add_text("Files:")
                dpg.add_listbox(items=[], num_items=15, tag="file_list", callback=file_selected_callback)
                # dpg.add_spacing(count=5)
                dpg.add_spacer(height=5)
                dpg.add_button(label="New File", callback=create_new_file_dialog, width=-1)

            dpg.add_separator()

            # Right Panel: Editor
            with dpg.child_window(border=False):
                dpg.add_text("Front Matter:")
                dpg.add_input_text(label="Title", tag="title_input", width=-1, enabled=False)
                # dpg.add_date_picker(label="Date", tag="date_input",  level=dpg.mvDatePickerLevel_Day)
                dpg_text = dpg.add_text()
                date_input = DatePicker(callback=lambda date, *, _dpg_text=dpg_text: dpg.set_value(_dpg_text, date))
                dpg.set_value(dpg_text, date_input.get_value())
                dpg.add_checkbox(label="Draft", tag="draft_checkbox", enabled=False)
                dpg.add_spacer(height=10)
                # dpg.add_spacing(count=10)
                dpg.add_text("Body Content:")
                dpg.add_input_text(multiline=True, height=-100, width=-1, tag="body_editor", enabled=False)
                dpg.add_spacer(height=10)
                # dpg.add_spacing(count=10)
                dpg.add_text("---", color=[100,100,100])
                dpg.add_text("Selected File: ", tag="selected_file_path_text")
                dpg.add_button(label="Save File", callback=save_file_callback, tag="save_button", enabled=False)

    load_categories_ui()
    enable_editor(False)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple Dear PyGui editor for Hugo content.")
    parser.add_argument(
        "--root",
        type=str,
        default="content",
        help="The path to your Hugo content directory. Defaults to 'content'.",
    )
    args = parser.parse_args()
    
    setup_dearpygui(content_root_path=args.root)
