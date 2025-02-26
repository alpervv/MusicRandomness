# File paths for the input files and output file
# input_files = ["binary_output1.txt", "binary_output2.txt", "binary_output3.txt"]
input_files = ["output_opera.txt", "output_rock.txt"]
output_file_path = "output_xor.txt"

def xor_multiple_files(input_files, output_file):
    """
    Perform XOR on multiple files containing ASCII 0s and 1s.
    The output file will have the length of the smallest file.
    """
    try:
        # Read all file contents into a list
        file_contents = [open(file, 'r').read().strip() for file in input_files]

        # Find the length of the smallest file
        min_length = min(len(content) for content in file_contents)

        # Perform XOR
        result = file_contents[0][:min_length]
        for content in file_contents[1:]:
            result = ''.join(
                '1' if result[i] != content[i] else '0'
                for i in range(min_length)
            )

        # Write the final result to the output file
        with open(output_file, 'w') as output:
            output.write(result)

        print(f"Success. Output written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


xor_multiple_files(input_files, output_file_path)
