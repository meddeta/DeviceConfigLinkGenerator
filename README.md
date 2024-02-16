# DeviceConfigLinkGenerator
This Python script is designed to extract specific details from a structured text file and generate a custom link based on the input name of a device. It reads through a file containing device configurations, searches for a device by name, and then constructs a hyperlink that includes the device's site ID and unique ID as parameters. This tool is particularly useful for managing and accessing device configurations in environments where devices are identified through a centralized API.

Features
Extracts device details from a structured text file.
Generates a hyperlink to access device configurations via an API endpoint.
Searches for devices by name.
Requirements
Python 3.x
Text file containing device details in a structured format.
Setup
Ensure Python 3.x is installed on your system.
Prepare a text file (myfile.txt by default) with device details in the required format.
Place the Python script and the text file in the same directory.
Usage
To use this script, follow these steps:

Open your terminal or command prompt.
Navigate to the directory containing the script and the device details file.
Run the script using the following command:
python extract_details_and_generate_link.py
When prompted, enter the name of the device for which you want to generate the link.
The script will output the site ID and ID of the device, along with the generated hyperlink. If the device name is not found, or the required details are missing, an error message will be displayed.
