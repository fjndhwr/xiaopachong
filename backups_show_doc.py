from shutil import copyfile, copytree
import time

if __name__ == '__main__':
    file_name = r'Sqlite'
    target_name = r'Sqlite' + str(time.time())
    #source_file = "c:/test.txt"
    source_file = r'/showdoc_data/html/' + file_name
    destination_file = '/backups/' + target_name
    #destination_file = r'//192.168.1.168/d/sql' + target_name
    copytree(source_file, destination_file)
