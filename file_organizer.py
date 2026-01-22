import os
import shutil


def sorter(file_extension, home=None):
    
    if home is None:
        home = os.getcwd()
    

    file_extension = file_extension.lower()
    if not file_extension.startswith('.'):
        target_ext = f'.{file_extension}'
    else:
        target_ext = file_extension


    folder_name = f"{target_ext.replace('.', '')} files"
    destination_folder = os.path.join(home, folder_name)


    files_moved = 0
    
    for filename in os.listdir(home):
        source_path = os.path.join(home, filename)
        

        if not os.path.isfile(source_path):
            continue


        _, current_ext = os.path.splitext(filename)
        
        if current_ext.lower() == target_ext:
            

            if os.path.exists(destination_folder):
                pass 
            else:
                os.mkdir(destination_folder)
                print(f"Directory did not exist. Created: {folder_name}")


            destination_path = os.path.join(destination_folder, filename)


            if os.path.exists(destination_path):
                print(f"Skipped: {filename} (File already exists in {folder_name})")
            else:
                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved: {filename}")
                    files_moved += 1
                except Exception as e:
                    print(f"Error moving {filename}: {e}")


    if files_moved == 0:
        print(f"No valid files moved.")
    else:
        print(f"Process complete. Moved {files_moved} files.")








sorter('enter file extension here')

