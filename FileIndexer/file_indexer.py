import os

class FileIndexer:
    class Node:
        def __init__(self, name, path):
            self.fileName = name
            self.filePath = path
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_node(self, file_name, file_path):
        #Insert node into the tree
        if self.root is None:
            self.root = self.Node(file_name, file_path)
            return

        current = self.root
        while True:
            if file_name < current.fileName:
                if current.left is None:
                    current.left = self.Node(file_name, file_path)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = self.Node(file_name, file_path)
                    return
                current = current.right

    def index_directory_helper(self, dir_path):
        #If it's not a directory, return
        if not os.path.isdir(dir_path):
            return

        #Loop over files within the directory
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_file():
                    self.insert_node(entry.name, entry.path)

        #Loop over directories within the directory
        with os.scandir(dir_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    #Recursive indexing
                    self.index_directory_helper(entry.path)

    def delete_subtree(self, root):
        if root is not None:
            self.delete_subtree(root.left)
            self.delete_subtree(root.right)
            root = None

    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(f"{root.fileName}: {root.filePath}")
            self.traverse(root.right)

    def index_directory(self, directory_path):
        self.root = None
        self.index_directory_helper(directory_path)

    def print_files(self):
        print("Indexed files:")
        self.traverse(self.root)

    def search_file_location(self, filename):
        #Search for a file in the BST
        current = self.root
        while current is not None:
            if filename == current.fileName:
                return current.filePath  #File found
            elif filename < current.fileName:
                current = current.left  #Search in the left subtree
            else:
                current = current.right  #Search in the right subtree
        return ""  #File not found

if __name__ == "__main__":
    path = input("Path to index recursively: ")

    indexer = FileIndexer()
    indexer.index_directory(path)
    indexer.print_files()

    filename_to_search = input("Let's search for a file's location. "
                               "Give the file name: ")

    location = indexer.search_file_location(filename_to_search)
    if location:
        print(f"File {filename_to_search} found. Location: {location}")
    else:
        print(f"File {filename_to_search} not found.")

