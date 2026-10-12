"""
1. A network security monitor analyzes access logs from two servers: 'Server_Alpha' (recorded in a duplicate-heavy list) and 'Server_Beta' (recorded in a tuple), compared against a predefined 'trusted_subnet' set:

alpha_logs = ["192.168.1.1", "192.168.1.5", "10.0.0.1", "192.168.1.1", "172.16.0.4", "10.0.0.1", "192.168.1.15"]
beta_logs = ("192.168.1.5", "10.0.0.2", "172.16.0.4", "192.168.1.10", "10.0.0.2", "192.168.1.15")
trusted_subnet = {"192.168.1.1", "192.168.1.5", "10.0.0.1"}

Perform the following tasks:
- Convert 'alpha_logs' list and 'beta_logs' tuple into sets 'alpha_ips' and 'beta_ips' to deduplicate addresses and display their unique counts.
- Find all unique IP addresses that accessed BOTH servers (intersection &).
- Find all unique IP addresses that accessed EITHER server (union |).
- Find IP addresses that accessed Server_Alpha but NOT Server_Beta (difference -).
- Find IP addresses that accessed ONLY ONE of the two servers, but NOT both (symmetric difference ^).
- Check whether 'trusted_subnet' is a subset of 'alpha_ips' (.issubset()) and check whether 'alpha_ips' is a superset of 'trusted_subnet' (.issuperset()).
- Add an emergency IP '192.168.1.99' to 'alpha_ips', discard '172.16.0.4' from 'beta_ips', and print the updated set sizes and membership check of '192.168.1.99' in 'alpha_ips'.
"""

alpha_logs = [
    "192.168.1.1", "192.168.1.5", "10.0.0.1", "192.168.1.1",
    "172.16.0.4", "10.0.0.1", "192.168.1.15"
]

beta_logs = (
    "192.168.1.5", "10.0.0.2", "172.16.0.4", "192.168.1.10",
    "10.0.0.2", "192.168.1.15"
)

trusted_subnet = {"192.168.1.1", "192.168.1.5", "10.0.0.1"}

alpha_ips = set(alpha_logs)
beta_ips = set(beta_logs)
print(f"Unique Alpha IPs ({len(alpha_ips)}): {alpha_ips}")
print(f"Unique Beta IPs ({len(beta_ips)}): {beta_ips}")

common_ips = alpha_ips & beta_ips
print(f"Common IPs (Both Servers): {common_ips}")

all_unique_ips = alpha_ips | beta_ips
print(f"All Unique Network IPs: {all_unique_ips}")

alpha_only_ips = alpha_ips - beta_ips
print(f"Alpha Only IPs: {alpha_only_ips}")

exclusive_ips = alpha_ips ^ beta_ips
print(f"Exclusive to Single Server: {exclusive_ips}")

is_trusted_subset = trusted_subnet.issubset(alpha_ips)
is_alpha_superset = alpha_ips.issuperset(trusted_subnet)
print(f"Is Trusted Subnet a subset of Alpha IPs? {is_trusted_subset}")
print(f"Is Alpha IPs a superset of Trusted Subnet? {is_alpha_superset}")

alpha_ips.add("192.168.1.99")
beta_ips.discard("172.16.0.4")
print(f"Updated Alpha IPs count: {len(alpha_ips)}")
print(f"Updated Beta IPs count: {len(beta_ips)}")
print(f"Is '192.168.1.99' in Alpha IPs? {'192.168.1.99' in alpha_ips}")
