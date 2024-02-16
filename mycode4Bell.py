#author Melika Sherafat
# Function to extract details and generate link based on input name
def extract_details_and_generate_link_for_name(file_path, input_name, name_key, site_val, id_val):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()

        site_id = None
        id_ = None
        device_block = []  # To store lines for each device block
        collecting_device_info = False

        for row in lines:
            if '{' in row:  # Start of a new device block
                collecting_device_info = True
                device_block = []

            if collecting_device_info:
                device_block.append(row)

            if '}' in row:  # End of the current device block
                collecting_device_info = False
                for line in device_block:
                    if name_key in line and input_name in line:
                        for device_line in device_block:
                            if site_val in device_line:
                                site_id = device_line.split(':')[-1].split(',')[0].strip().strip('"')
                            elif id_val in device_line:
                                id_ = device_line.split(':')[-1].split(',')[0].strip().strip('"')
                        break

                # Check if the required details were found
                if site_id and id_:
                    break

        if site_id and id_:
            link = f"https://api.gc2.mist.com/api/v1/sites/{site_id}/devices/{id_}/config_cmd"
            return site_id, id_, link
        else:
            return None, None, "Error: Unable to extract all required details or name not found."


file_path = 'myfile.txt'
name_key = '"name":'
site_val = '"site_id":'
id_val = '"id":'  # Use the actual field name for the ID

# Input name
input_name = input("Enter the name of the device: ")

# Extract details and generate link for both names with a cmd at the end of the hyper link
extracted_site_id, extracted_id, generated_link = extract_details_and_generate_link_for_name(file_path, input_name, name_key, site_val, id_val)

if extracted_site_id and extracted_id:
    print(f"Site ID: {extracted_site_id}, ID: {extracted_id}")
    print("Link:")
    print(generated_link)
else:
    print(f"Error: {generated_link}")
