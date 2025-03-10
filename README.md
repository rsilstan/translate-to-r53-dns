<b>This package is intended to make it easy to translate a allow/block list from AWS Firewall to the Route 53 Resolver DNS Firewall</b>

✅ Reads an AWS Network Firewall blocklist (assumed to be in a CSV or text file format).
✅ Filters out IP-based rules (since Route 53 Resolver only supports domains).
✅ Extracts fully qualified domain names (FQDNs).
✅ Outputs a formatted allow/block list for use in Terraform or AWS CLI.
