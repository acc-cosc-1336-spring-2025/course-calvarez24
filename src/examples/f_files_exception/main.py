#main program

import files

def main():
    file_name = 'names.txt'
    #files.write_to_file(file_name)
    #files.read_from_file(file_name)
    #files.read_from_file_one_line_at_a_time(file_name)
    files.read_from_file_w_a_loop(file_name)

main()