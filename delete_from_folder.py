import os

def delete_files(folder_path, target_string):
    # Проверяем каждый файл в указанной папке
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if target_string in file_name:
                file_path = os.path.join(root, file_name)
                # Удаление файла, содержащего указанную строку в имени
                os.remove(file_path)
                print(f"Файл {file_path} удален.")

def delete_folders(folder_path):
    deleted_folders_count = 0  # Счетчик удаленных папок
    
    # Проверяем папки в обратном порядке для удаления пустых папок
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for folder_name in dirs:
            folder = os.path.join(root, folder_name)
            if not os.listdir(folder):  # Если папка пуста
                os.rmdir(folder)  # Удаляем пустую папку
                deleted_folders_count += 1
                print(f"Папка {folder} удалена.")
    
    return deleted_folders_count

# Укажите путь к папке, в которой нужно удалить файлы и пустые папки
folder_to_search = 'C:/PROJECTS/development/folderOutput2'
# Указываем строку, которая должна содержаться в имени файла для его удаления
string_to_find = 'output-2'

delete_files(folder_to_search, string_to_find)
deleted_count = delete_folders(folder_to_search)
print(f"Удалено пустых папок: {deleted_count}")





