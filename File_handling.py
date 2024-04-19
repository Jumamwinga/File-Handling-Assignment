def write_to_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Future here I come 1\n")
            f.write("12345 future\n")
            f.write("Power learn future tech: 2,7,6.9 \n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f" Error: Permission denied to write to'{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("File creation process completed.")

def read_and_display(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read from '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
def append_to_file(filename):
    try:
        with open(filename, 'a') as f:
            f.write("\n Additional line 1\n")
            f.write("986454\n")
            f.write("Last line appended\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to append to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("File appending completed.")

if __name__ == "__main__":
    filename = "my_file.txt"

    # Writing to file
    write_to_file(filename)

    # Read and display contents
    read_and_display(filename)

    # Appending 
    append_to_file(filename)

    # Reading and displaying updated file contents
    read_and_display(filename)     