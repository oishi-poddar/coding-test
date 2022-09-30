'''
This module finds the count of lines for every
 file in a specified directory and subdirectories.
It also calculates the total number of lines and
average number of lines per file.
'''

import os

class Files:
    '''
        Class to do data analysis on files in directories
    '''

    def get_all_files(self, directory, extension = ".txt"):
        '''
            Parameters:
            directory (str): Path of directory name to be read
            extension (str)[optional]: Only files of this extension will be read

            Returns:
            list: [Contains file paths of all the files in the directories
            and subdirectories specified]

        '''

        try:
            # Fetch names of files and directories in the given directory
            list_of_files = os.listdir(directory)
            all_files = []

            for file in list_of_files:
                # Create full path of file
                full_path = os.path.join(directory, file)
                # If entry is a directory then get the list of files in this directory
                if os.path.isdir(full_path):
                    all_files = all_files + self.get_all_files(full_path, extension)
                else:
                    # Only add those files whose extension is the same as provided
                    if file.endswith(extension):
                        all_files.append(full_path)

            return all_files

        except FileNotFoundError as err:
            print("Exception occurred", err)

        return None




    @staticmethod
    def main(directory, extension = ".txt"):
        '''
            Parameters:
            directory (str): Path of directory name to be read
            extension (str)[optional]: Only files of this extension will be read

            Returns:
            list: [Contains number of files read, total number of lines, avergage lines per file]

        '''
        try:
            # Get the list of all files in directory tree at given path
            files = Files()
            all_files = files.get_all_files(directory, extension)

            total_lines = 0
            total_num_files = len(all_files)

            # Calculate number of files, total lines, average lines per file
            for file in all_files:
                with open(file, 'r', encoding="utf-8") as open_file:
                    num_lines= len(open_file.readlines())
                    print(file, num_lines)
                    total_lines+=num_lines

            avg_lines = round(total_lines/total_num_files, 2)
            number_of_files = len(all_files)
            print("========================================================")
            print("Number of files found", number_of_files)
            print("Total number of lines", total_lines)
            print("Average lines per file", total_lines/total_num_files)

            return [number_of_files, total_lines, avg_lines]

        except IOError:
            print('An error occurred trying to read the file', file)

        except ValueError:
            print('Non-numeric data found in the file', file)

        except ZeroDivisionError:
            print("Error ZeroDivisionError, empty directory!")

        except TypeError:
            print("Type error!")

        return None




if __name__ == "__main__":

    # Specify the directory name and extension here, change as required
    directory_path = os.path.dirname(__file__)
    directory_path = os.path.join(directory_path, 'test')
    EXTENSION_NAME = ".py"
    Files.main(directory_path, EXTENSION_NAME)
