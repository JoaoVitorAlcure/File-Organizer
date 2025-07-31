from tkinter.filedialog import askdirectory
import shutil, os

def f_extractFileName(path)->list:
    files = []
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_file():
            files.append(entry.name)
    return files

def f_checkExistingExtensions(files)->dict:
    extensions = {}
    for i in files:
        ext = os.path.splitext(i)[1]
        if (ext not in extensions):
            print(f"Extension detected: {ext}. Choose a directory if you want or cancel")
            directory = askdirectory()
            if directory:
                extensions[ext] = directory
            else:
                print("Extension cancelled")
    return extensions

def f_moveFiles(files, extensions, path)->int:
    qtd = 0
    for file in files:
        ext = os.path.splitext(file)[1]
        if ext in extensions:
            shutil.move(os.path.join(path, file), extensions.get(ext))
            qtd += 1
    return qtd

def f_findFile(filename, path):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)
    return None

def main():
    path = input("Insert file path here: ")
    files = f_extractFileName(path)
    extensions = f_checkExistingExtensions(files)
    qtd = f_moveFiles(files, extensions, path)
    print(f"Movidos {qtd} arquivos com sucesso!")
    return 0

if __name__ == "__main__":
    main()