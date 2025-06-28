import os
import glob
import re
import json
from datetime import datetime

def extract_field(content, field_name):
    """Extract a field value from the content using regex."""
    pattern = rf'{field_name}:\s*[\'"]([^\'"]*)[\'"]'
    match = re.search(pattern, content)
    if match:
        return match.group(1)
    return ""

def truncate_description(text, max_length):
    """Truncate text to max_length and add ellipsis if it exceeds that length."""
    if text and len(text) > max_length:
        return text[:max_length] + '...'
    return text

def extract_list_field(content, field_name):
    """Extract a list field value from the content using regex."""
    pattern = rf'{field_name}:\s*\[(.*?)\]'
    match = re.search(pattern, content)
    if match:
        items_str = match.group(1).strip()
        if not items_str:
            return []
        items = re.findall(r'"([^"]*)"', items_str)
        return items
    return []

def parse_file(file_path):
    """Parse a file and extract relevant fields."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            if "name:" in content:
                return {
                    'type': 'registration',
                    'name': extract_field(content, 'name'),
                    'description': extract_field(content, 'description'),
                    'contact_method': extract_field(content, 'contact_method'),
                    'contact': extract_field(content, 'contact'),
                    'wallet_address': extract_field(content, 'wallet_address'),
                    'role': extract_field(content, 'role'),
                    'experience_level': extract_field(content, 'experience_level'),
                    'timezone': extract_field(content, 'timezone'),
                    'team_name': extract_field(content, 'team_name'),
                    'team_status': extract_field(content, 'team_status'),
                    'project_name': extract_field(content, 'project_name'),
                    'project_description': truncate_description(extract_field(content, 'project_description'), 100),
                    'tech_stack': extract_field(content, 'tech_stack'),
                    'support_needed': extract_field(content, 'support_needed'),
                    'goals': extract_field(content, 'goals'),
                    'notes': extract_field(content, 'notes'),
                    'file_path': file_path
                }
            else:
                print(f"Unknown file type: {file_path}")
                return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def scan_registration_files():
    """Scan the registration directory for markdown files."""
    registration_dir = os.path.join(os.getcwd(), 'registration')
    if not os.path.exists(registration_dir):
        print(f"Registration directory not found: {registration_dir}")
        return []
    files = glob.glob(os.path.join(registration_dir, '*.md'))
    return [f for f in files if not f.endswith('template.md')]

def update_participants_table(registrations):
    """Update only the participants table in the README file."""
    readme_path = os.path.join(os.getcwd(), 'README.md')

    participants_table = "| Name | Role | Team Status | Project Name | Project Description | Contact |\n|------|------|-------------|--------------|----------------------|---------|\n"

    for reg in registrations:
        name = reg.get('name', '')
        role = reg.get('role', '')
        team_status = reg.get('team_status', '')
        project_name = reg.get('project_name', '')
        project_description = reg.get('project_description', '')
        contact = reg.get('contact', '')
        contact_method = reg.get('contact_method', '')
        file_path = reg.get('file_path', '')

        md_link = name
        if file_path and name:
            filename = os.path.basename(file_path)
            md_link = f'[{name}](./registration/{filename})'

        contact_display = contact
        if contact and contact_method:
            contact_display = f'{contact} ({contact_method})'

        project_description = project_description.replace('|', '&#124;') if project_description else ''

        participants_table += f"| {md_link} | {role} | {team_status} | {project_name} | {project_description} | {contact_display} |\n"

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        pattern = r'(## 👥 Participants)\s+([\s\S]*?)(?=\n##|\Z)'
        match = re.search(pattern, content)

        if match:
            updated_content = re.sub(
                pattern,
                r'\1' + f"\n\n{participants_table}",
                content
            )

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            updated_content = re.sub(
                r'\*Last updated: .*\*',
                f"*Last updated: {timestamp}*",
                updated_content
            )

            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"Updated participants table in README.md")
            return True
        else:
            print("Could not find participants section in README.md")
            return False
    except Exception as e:
        print(f"Error updating README: {e}")
        return False

def update_hackathon():
    """Update the hackathon README with registration information."""
    registration_files = scan_registration_files()
    registrations = []
    for file in registration_files:
        data = parse_file(file)
        if data and data['type'] == 'registration':
            registrations.append(data)

    update_participants_table(registrations)
    print(f"Updated README with {len(registrations)} participants.")
    return True

if __name__ == '__main__':
    update_hackathon()