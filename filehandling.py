with open("input.txt", "w") as file: file.write("Hello, My name is Benedict Ngetich. I am 20 years old . I attend Princeton University. I am taking python courses at PLP. I aspire to be a coder and a tech guru.")
# Read from input.txt
with open("input.txt", "r") as infile:
    contents = infile.read()

# Count words
word_count = len(contents.split())

# Convert text to uppercase
uppercase_contents = contents.upper()


# Prepare output content
output_text = f"{uppercase_contents}\n\nWORD COUNT: {word_count}"

# Write to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(output_text)

# Print success message
print("Success! 'output.txt' has been created with the processed content.")

