# Batch_deletion
Delete files🗃 in one go with same extension/filetype.

Have you encounterd a situation where you have to select multiple files📁 with same filetype/extension to delete them, I have
when deleting multiple .srt files from my directory.

## Prerequisites
```
python 3
```
## Usage

Clone the repo or download the file.

open command prompt and run python file.
```
python batch_deletion.py
```
There are two arguments you have to pass.

It is ❗important❗ to specify the file type or extension.
```
--filetype
```

It is optional to specify the path, by default it will take current working directory.
```
--path
```
## Example
```
python batch_deletion.py --filetype .txt --path your path
```

## Multiple file type arguments
You can pass multiple filetypes at sametime
```
batch_delete --filetype .txt .java .cpp
```

## Node-version
[Batch Deletion Node](https://github.com/udhaybegyall/batch-deletion-node-version)
