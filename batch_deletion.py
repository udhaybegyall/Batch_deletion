import os
import argparse

parser = argparse.ArgumentParser(
    description = "Delete multiple files at same time"
)

parser.add_argument(
    "--filetype",
    type = str,
    default = None,
    help = "Files with the given name will be deleted (e.g: .txt)"
)

parser.add_argument(
    "--path",
    type = str,
    default = ".",
    help = "Path of the directory need to be cleaned."
)

args = parser.parse_args()

type_filter = args.filetype
path = args.path

# get all files from the given directory

dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
deleted = 0

for doc in docs:

    # seperate name from file extension
    full_doc_path , filetype = os.path.splitext(doc)

    # delete file if the given filetype matches
    if filetype == type_filter or type_filter is None:
        
        os.remove(doc)
        deleted += 1

        print(f"Deleted file {doc}.")

print(f"Deleted {deleted} of {len(docs)} files.")
