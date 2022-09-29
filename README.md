# coding-test

## Project description
The purpose of the program is to find a list of files with a particular extension in the directory specified. The program recursively will also find such files within any subdirectories present. It will also print the line count for each file and the number of files found, total number of lines and average lines per file.

## Project contents

The folder structure has the main logic in the file "files.py" and unit tests in the file "tests.py". The tests folder contains test files to test the program.

The program has been compiled using Python 3.8 and can run on Python 3 and above.

## How to Install and Run the Project

1. Clone the GitHub repository in a machine with Python 3 and above installed.<br>
2. Specify the directory path and extension in the files.py file. In case no extension is provided, a default extension of ".txt" is used.<br>
3. Run the file "files.py".

## Example output

An example output is shown below when the directory path is the provided tests folder with the extension ".py" on my machine.
The first two lines are the names of the files followed by the number of lines in each file.

/Users/apple/PycharmProjects/pythonProject/test/test1.py 43<br>
/Users/apple/PycharmProjects/pythonProject/test/test1.py 10<br>

========================================================<br>
Number of files found 2<br>
Total number of lines 53<br>
Average lines per file 26.5

