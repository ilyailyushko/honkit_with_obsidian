import os
import re
import subprocess

def get_first_level_heading(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None

def get_second_level_headings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'^##\s+(.*)$', content, re.MULTILINE)
        return [match.strip() for match in matches]

def add_heading_to_summary(heading, file_name, indent):
    with open('content/SUMMARY.md', 'a', encoding='utf-8') as file:
        file.write(f'{" " * indent}* [{heading}](./{file_name}#{heading.lower().replace(" ", "-")})\n')

# Создаем папку "content", если она не существует
if not os.path.exists('content'):
    os.makedirs('content')

# Очищаем содержимое файла SUMMARY.md
with open('content/SUMMARY.md', 'w', encoding='utf-8') as file:
    file.write('# Summary\n\n')

# Получаем список всех файлов md в папке "content"
md_files = [file for file in os.listdir('content') if file.endswith('.md')]

if md_files:
    # Получаем первый заголовок первого уровня из каждого файла и добавляем его в summary
    for file_name in md_files:
        if file_name == 'SUMMARY.md':
            continue  # Пропускаем файл SUMMARY.md
        file_path = os.path.join('content', file_name)
        first_level_heading = get_first_level_heading(file_path)
        if first_level_heading:
            add_heading_to_summary(first_level_heading, file_name, 0)
        
        second_level_headings = get_second_level_headings(file_path)
        if second_level_headings:
            for heading in second_level_headings:
                indent = 4  # Уровень отступа для заголовков второго уровня
                add_heading_to_summary(heading, file_name, indent)

# Запускаем команду npx honkit serve
subprocess.run(['npx', 'honkit', 'serve', 'content'])
