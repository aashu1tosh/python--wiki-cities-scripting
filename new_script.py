import re

# Specify the file path
file_path = 'table_content.txt'  # Replace with your file path
append_file_path = 'municipalities.txt'

# Open the file and read its contents
with open(file_path, 'r') as file:
    file_content = file.read()

# Define regex pattern to find each <tr> block
pattern_tr = r'<tr>(.*?)</tr>'
# Define regex pattern to find each <td> within a <tr>
pattern_td = r'<td>(.*?)</td>'

# Find all <tr> blocks in the file content
tr_blocks = re.findall(pattern_tr, file_content, re.DOTALL)

# Process each <tr> block
for tr_block in tr_blocks:
    # Find all <td> elements within the current <tr> block
    td_elements = re.findall(pattern_td, tr_block, re.DOTALL)
    
    # Extract the content of the first two <td> elements
    if len(td_elements) >= 2:
        content_first_td = td_elements[0].strip()
        content_second_td = td_elements[1].strip()
        
        pattern = r'<a[^>]*>\s*(.*?)\s*</a>'

        # Use re.search to find the pattern in the html_string
        match = re.search(pattern, content_first_td, re.DOTALL)

        # If a match is found, extract the text inside the <a> tag
        if match:
            extracted_text = match.group(1).strip()
            content_first_td = extracted_text
        
        # Print or process the content as needed
        # print("{")
        # print("en:", f'"{content_first_td}"')
        # print("ne: ", f'"{content_second_td}"')
        # print("},")
        
        with open(append_file_path, 'a') as file:
        # Redirect print statements to the file
            print("{", file=file)
            print("en:", f'"{content_first_td}"', file=file)
            print("ne: ", f'"{content_second_td}"', file=file)
            print("},", file=file)