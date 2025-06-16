import os

example = "/home/harry/PycharmProjects/PythonProject/test"

def print_directories(path):
    for root, dirs, files in os.walk(path):
        print(root)
        print(dirs)
        print(files)

print_directories(example)

print(f"{os.path.getmtime(example + "/crazy")}")

# 1749820461.3982635

# 1749909252.5639577