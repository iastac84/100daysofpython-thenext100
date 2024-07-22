#!/usr/bin/env python3

# Convert a json file to yaml
# Run with python convert_json_to_yaml.py input.json output.yaml

# Dependencies 
# pip install pyyaml

import json
import yaml
import sys

def convert_json_to_yaml(input_file, output_file):
    try:
        # Read JSON data from the input file
        with open(input_file, 'r') as json_file:
            json_data = json.load(json_file)
        
        # Convert JSON data to YAML format
        yaml_data = yaml.dump(json_data, default_flow_style=False)

        # Write YAML data to the output file
        with open(output_file, 'w') as yaml_file:
            yaml_file.write(yaml_data)

        print(f"Successfully converted {input_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file {input_file}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_json_to_yaml.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_json_to_yaml(input_file, output_file)
