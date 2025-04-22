def modify_content(text):
    # You can change this function to do other cool transformations
    return text.upper()

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as infile:
            contents = infile.read()
            print("\n✅ File successfully read.")

        modified = modify_content(contents)

        with open("modified_output.txt", "w") as outfile:
            outfile.write(modified)
            print("\n✅ Modified content written to 'modified_output.txt'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: Permission denied.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
