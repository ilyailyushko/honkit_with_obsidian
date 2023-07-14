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

def add_heading_to_summary(heading, file_name):
    with open('SUMMARY.md', 'a', encoding='utf-8') as file:
        file.write(f'* [{heading}](./{file_name})\n')

# Получаем список всех файлов md в корневой директории
md_files = [file for file in os.listdir() if file.endswith('.md')]

if md_files:
    # Получаем первый заголовок первого уровня из каждого файла и добавляем его в summary
    for file_name in md_files:
        file_path = os.path.join(os.getcwd(), file_name)
        first_level_heading = get_first_level_heading(file_path)
        if first_level_heading:
            add_heading_to_summary(first_level_heading, file_name)

# Запускаем команду npx honkit serve
subprocess.run(['npx', 'honkit', 'serve'])
