print("Please type your file name: ")
file_name = input("> ")

txt_file = open(file_name)
print(txt_file.read())
