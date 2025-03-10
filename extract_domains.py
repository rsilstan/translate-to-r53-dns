#run as : python extract_domains.py

import re
import csv

# Input file (change this to the actual file path)
input_file = "network_firewall_blocklist.txt"
output_file = "route53_resolver_blocklist.txt"

# Regular expression to match domain names (excluding IP addresses)
domain_regex = re.compile(r"^(?!\d+\.\d+\.\d+\.\d+$)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$")

def extract_domains(input_path, output_path):
    domain_set = set()  # Use a set to avoid duplicates

    with open(input_path, "r") as infile:
        for line in infile:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue

            # Extract domain names
            match = domain_regex.match(line)
            if match:
                domain_set.add(match.group(1))

    # Write the extracted domains to a new file
    with open(output_path, "w") as outfile:
        for domain in sorted(domain_set):
            outfile.write(domain + "\n")

    print(f"Successfully Extracted {len(domain_set)} domain names and saved to {output_path}")

# Run the extraction process
extract_domains(input_file, output_file)

