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

def generate_participants_table(registrations, language='zh'):
    """Generate participants table in Chinese or English."""
    if language == 'zh':
        # Chinese headers
        table_header = "| 姓名 | 角色 | 团队状态 | 项目名称 | 项目描述 | 联系方式 |\n|------|------|----------|----------|----------|----------|\n"
    else:
        # English headers  
        table_header = "| Name | Role | Team Status | Project Name | Project Description | Contact |\n|------|------|-------------|--------------|----------------------|---------|\n"
    
    participants_table = table_header

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
    
    return participants_table

def update_participants_table(registrations, readme_path, language='zh'):
    """Update only the participants table in the specified README file."""
    
    participants_table = generate_participants_table(registrations, language)
    
    section_title = "## 👥 参与者" if language == 'zh' else "## 👥 Participants"

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for the participants section
        if language == 'zh':
            pattern = r'(## 👥 参与者)\s*([\s\S]*?)(?=\n##|\Z)'
        else:
            pattern = r'(## 👥 Participants)\s*([\s\S]*?)(?=\n##|\Z)'
        
        match = re.search(pattern, content)

        if match:
            # Replace existing participants section
            updated_content = re.sub(
                pattern,
                r'\1' + f"\n\n{participants_table}",
                content
            )
        else:
            # Add participants section before the last sections
            # Find a good insertion point (before ## 💬 or similar sections)
            if language == 'zh':
                insertion_patterns = [r'(## 💬 加入讨论)', r'(## 🤝 联合组织)', r'(_Last updated:)']
            else:
                insertion_patterns = [r'(## 💬 Join the discussion)', r'(## 🤝 Co-organizers)', r'(_Last updated:)']
            
            inserted = False
            for pattern in insertion_patterns:
                if re.search(pattern, content):
                    updated_content = re.sub(
                        pattern,
                        f"{section_title}\n\n{participants_table}\n\n" + r'\1',
                        content
                    )
                    inserted = True
                    break
            
            if not inserted:
                # If no insertion point found, append at the end
                updated_content = content + f"\n\n{section_title}\n\n{participants_table}\n"

        # Update timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_content = re.sub(
            r'_Last updated: .*_',
            f"_Last updated: {timestamp}_",
            updated_content
        )

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Updated participants table in {os.path.basename(readme_path)}")
        return True
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")
        return False

def copy_readme_to_zh_cn():
    """直接复制 README.md 文件为 README_ZH-CN.md"""
    import shutil
    
    readme_path = os.path.join(os.getcwd(), 'README.md')
    readme_zh_cn_path = os.path.join(os.getcwd(), 'README_ZH-CN.md')
    
    try:
        if not os.path.exists(readme_path):
            print(f"Source file not found: {readme_path}")
            return False
            
        # 直接复制文件，覆盖目标文件
        shutil.copy2(readme_path, readme_zh_cn_path)
        
        print(f"Successfully copied {os.path.basename(readme_path)} to {os.path.basename(readme_zh_cn_path)}")
        return True
        
    except Exception as e:
        print(f"Error copying README file: {e}")
        return False

def update_hackathon():
    """Update both Chinese and English hackathon README files with registration information."""
    registration_files = scan_registration_files()
    registrations = []
    for file in registration_files:
        data = parse_file(file)
        if data and data['type'] == 'registration':
            registrations.append(data)

    # Update Chinese README (default)
    readme_zh_path = os.path.join(os.getcwd(), 'README.md')
    if os.path.exists(readme_zh_path):
        update_participants_table(registrations, readme_zh_path, 'zh')
    else:
        print(f"Chinese README not found: {readme_zh_path}")

    # Update English README  
    readme_en_path = os.path.join(os.getcwd(), 'README_EN.md')
    if os.path.exists(readme_en_path):
        update_participants_table(registrations, readme_en_path, 'en')
    else:
        print(f"English README not found: {readme_en_path}")

    # 复制 README.md 到 README_ZH-CN.md
    copy_readme_to_zh_cn()

    print(f"Updated both README files with {len(registrations)} participants.")
    return True

if __name__ == '__main__':
    import sys
    
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == '--copy-only':
            # 只执行复制操作
            copy_readme_to_zh_cn()
        elif sys.argv[1] == '--help':
            print("Usage:")
            print("  python update_hackathon.py                  # 完整更新流程")
            print("  python update_hackathon.py --copy-only      # 只复制README.md到README_ZH-CN.md")
            print("  python update_hackathon.py --help           # 显示帮助信息")
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Use --help for usage information")
    else:
        # 执行完整的更新操作
        update_hackathon()