import re
from collections import Counter

INPUT_FILE = "../data_extended/enterprise_logs.txt"
OUTPUT_FILE = "../output/extracted_iocs.txt"

IP_REGEX = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
DOMAIN_REGEX = r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
MD5_REGEX = r"\b[a-fA-F0-9]{32}\b"
SHA256_REGEX = r"\b[a-fA-F0-9]{64}\b"

def extract_iocs(pattern, text):
    return Counter(re.findall(pattern, text))

def main():
    with open(INPUT_FILE, "r") as f:
        logs = f.read()

    results = {
        "IP Addresses": extract_iocs(IP_REGEX, logs),
        "Domains": extract_iocs(DOMAIN_REGEX, logs),
        "MD5 Hashes": extract_iocs(MD5_REGEX, logs),
        "SHA256 Hashes": extract_iocs(SHA256_REGEX, logs),
    }

    with open(OUTPUT_FILE, "w") as out:
        for category, items in results.items():
            out.write(f"{category}:\n")
            for value, count in items.most_common():
                out.write(f"  - {value} (seen {count} times)\n")
            out.write("\n")

    print("[+] SOC-grade IOC extraction complete")

if __name__ == "__main__":
    main()
