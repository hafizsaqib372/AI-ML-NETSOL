"""
1. Given customer membership tier ('Platinum', 'Gold', 'Silver', 'Bronze'), purchase amount, and coupon validity:
- Platinum gets 20% discount regardless of purchase amount.
- Gold gets 15% discount if amount >= 10,000, else 10%.
- Silver gets 8% discount if amount >= 5,000, else 5%.
- Bronze / Non-member gets 5% if amount >= 5,000, else 0%.
- If coupon_valid is True, add an additional 5% discount (capped at 25% max total discount).
- If payable amount after discount >= 5,000 or customer is Platinum, shipping is Free (Rs. 0), otherwise Rs. 350.
Calculate and display the original amount, discount percentage, discount value, shipping fee, and final payable amount.
"""

membership = "Gold"
purchase_amount = 12500
coupon_valid = True

if membership == "Platinum":
    discount_rate = 0.20
elif membership == "Gold":
    if purchase_amount >= 10000:
        discount_rate = 0.15
    else:
        discount_rate = 0.10
elif membership == "Silver":
    if purchase_amount >= 5000:
        discount_rate = 0.08
    else:
        discount_rate = 0.05
else:
    if purchase_amount >= 5000:
        discount_rate = 0.05
    else:
        discount_rate = 0.00

if coupon_valid:
    discount_rate = discount_rate + 0.05
    if discount_rate > 0.25:
        discount_rate = 0.25

discount_amount = purchase_amount * discount_rate
amount_after_discount = purchase_amount - discount_amount

if amount_after_discount >= 5000 or membership == "Platinum":
    shipping_fee = 0
else:
    shipping_fee = 350

final_payable = amount_after_discount + shipping_fee

print(f"Original Amount: Rs. {purchase_amount}")
print(f"Applied Discount: {discount_rate * 100:.1f}% (-Rs. {discount_amount:.2f})")
print(f"Shipping Fee: Rs. {shipping_fee}")
print(f"Final Payable Amount: Rs. {final_payable:.2f}")


"""
2. Multi-Tier User Authentication & Role-Based Access Control (RBAC):
Using a dictionary for user credentials & account states, and a dictionary of permission sets for each role:
- Check if the username exists in users_db. If not, print "Error: User not found."
- If user exists, check if account status is 'active'. If suspended or inactive, print "Error: Account is suspended."
- If active, check password. If incorrect, print "Error: Invalid credentials."
- If credentials are valid, check if the requested action is present in the role's authorized permission set.
  Print authorization success or access denial accordingly.
"""

users_db = {
    "admin_usr": {"password": "securePass#1", "role": "superadmin", "status": "active"},
    "dev_bilal": {"password": "codeMaster@2026", "role": "editor", "status": "active"},
    "guest_sara": {"password": "tempPass123", "role": "viewer", "status": "suspended"}
}

role_permissions = {
    "superadmin": {"create", "read", "update", "delete", "deploy"},
    "editor": {"create", "read", "update"},
    "viewer": {"read"}
}

username_input = "dev_bilal"
password_input = "codeMaster@2026"
action_requested = "delete"

if username_input not in users_db:
    print("Error: User not found.")
else:
    user_record = users_db[username_input]
    if user_record["status"] != "active":
        print(f"Error: Account for '{username_input}' is {user_record['status']}. Access denied.")
    elif user_record["password"] != password_input:
        print("Error: Invalid credentials.")
    else:
        user_role = user_record["role"]
        allowed_actions = role_permissions[user_role]
        if action_requested in allowed_actions:
            print(f"Access GRANTED: '{username_input}' ({user_role}) authorized to '{action_requested}'.")
        else:
            print(f"Access DENIED: Role '{user_role}' does not have permission to '{action_requested}'.")


"""
3. University Academic Honors & Financial Scholarship Eligibility Evaluator:
Given student records including CGPA, credit hours enrolled, disciplinary record flag, list of extracurricular clubs, and family monthly income:
- Eligibility check: Credit hours must be at least 15 and disciplinary record must be False.
  If not eligible, print reason and disqualify.
- Honors classification:
  * CGPA >= 3.9 -> "Summa Cum Laude (Highest Honors)"
  * CGPA >= 3.7 -> "Magna Cum Laude (High Honors)"
  * CGPA >= 3.5 -> "Cum Laude (Honors)"
  * Else -> "Good Academic Standing"
- Scholarship Allocation:
  * If CGPA >= 3.8 and family_income <= 80,000 -> "100% Full Need-cum-Merit Scholarship"
  * Elif CGPA >= 3.75 and len(extracurriculars) >= 2 -> "75% Merit-cum-Leadership Scholarship"
  * Elif CGPA >= 3.5 -> "50% Academic Merit Scholarship"
  * Else -> "Not eligible for scholarship aid."
Print full student evaluation summary.
"""

student_name = "Hamza Ali"
cgpa = 3.82
credit_hours = 16
has_disciplinary_issue = False
extracurriculars = ["AI Club", "Debate Society", "ACM Chapter"]
family_income = 72000

if credit_hours < 15 or has_disciplinary_issue:
    print(f"Student {student_name} is NOT eligible for honors or aid due to credit/disciplinary constraints.")
else:
    if cgpa >= 3.9:
        honors = "Summa Cum Laude (Highest Honors)"
    elif cgpa >= 3.7:
        honors = "Magna Cum Laude (High Honors)"
    elif cgpa >= 3.5:
        honors = "Cum Laude (Honors)"
    else:
        honors = "Good Academic Standing"

    if cgpa >= 3.8 and family_income <= 80000:
        scholarship = "100% Full Need-cum-Merit Scholarship"
    elif cgpa >= 3.75 and len(extracurriculars) >= 2:
        scholarship = "75% Merit-cum-Leadership Scholarship"
    elif cgpa >= 3.5:
        scholarship = "50% Academic Merit Scholarship"
    else:
        scholarship = "Not eligible for financial scholarship."

    print(f"Student: {student_name} | CGPA: {cgpa} | Credits: {credit_hours}")
    print(f"Academic Standing: {honors}")
    print(f"Scholarship Awarded: {scholarship}")


"""
4. Smart Banking ATM Withdrawal & Fraud Rule Engine:
Evaluate an ATM withdrawal request against account state, security status, and limits:
- Check 1: If account_is_locked is True, reject with security lock message.
- Check 2: If entered_pin does not match correct_pin, reject with invalid PIN alert.
- Check 3: If withdraw_amount <= 0 or withdraw_amount % 500 != 0, reject (must be positive multiple of 500).
- Check 4: If withdraw_amount + daily_withdrawn_today > daily_limit, reject due to exceeding daily quota.
- Check 5: If withdraw_amount > account_balance, reject due to insufficient balance.
- Otherwise: Deduct balance, update daily withdrawn total, and print dispensed amount and remaining balances.
"""

account_balance = 75000
daily_withdrawn_today = 20000
daily_limit = 50000
account_is_locked = False
correct_pin = 5821
entered_pin = 5821
withdraw_amount = 25000

if account_is_locked:
    print("Transaction Failed: Your account is locked. Please contact customer support.")
elif entered_pin != correct_pin:
    print("Transaction Failed: Invalid ATM PIN.")
elif withdraw_amount <= 0 or withdraw_amount % 500 != 0:
    print("Transaction Failed: Amount must be positive and in denominations of Rs. 500.")
elif withdraw_amount + daily_withdrawn_today > daily_limit:
    remaining_limit = daily_limit - daily_withdrawn_today
    print(f"Transaction Failed: Daily limit exceeded. You can only withdraw up to Rs. {remaining_limit} today.")
elif withdraw_amount > account_balance:
    print(f"Transaction Failed: Insufficient funds. Current balance is Rs. {account_balance}.")
else:
    account_balance = account_balance - withdraw_amount
    daily_withdrawn_today = daily_withdrawn_today + withdraw_amount
    remaining_daily_limit = daily_limit - daily_withdrawn_today
    print("Transaction Successful!")
    print(f"Dispensed Amount: Rs. {withdraw_amount}")
    print(f"Remaining Balance: Rs. {account_balance}")
    print(f"Remaining Daily Limit: Rs. {remaining_daily_limit}")


"""
5. Network Firewall Packet Inspection & Threat Filter:
Inspect a network packet dictionary with keys: source_ip, destination_port, protocol, payload_size_kb, and flags tuple.
Using sets of blocked_ips, allowed_ports, and allowed_protocols:
- If source_ip is in blocked_ips, verdict is "BLOCKED: Blacklisted IP".
- Elif protocol not in allowed_protocols, verdict is "DROPPED: Unauthorized Protocol".
- Elif destination_port not in allowed_ports, verdict is "DROPPED: Port Not Allowed".
- Elif payload_size_kb > 1024:
  * If destination_port == 443 and "ACK" in flags, verdict is "WARNING: Large HTTPS Packet (Forward to Deep Inspection)".
  * Else, verdict is "DROPPED: Payload Exceeds Maximum Size Limit".
- Else, verdict is "ACCEPTED: Packet Cleared All Firewall Rules".
Output detailed inspection report.
"""

packet = {
    "source_ip": "192.168.1.50",
    "destination_port": 443,
    "protocol": "TCP",
    "payload_size_kb": 1450,
    "flags": ("SYN", "ACK", "PSH")
}

blocked_ips = {"192.168.1.200", "10.0.0.99", "172.16.5.10"}
allowed_ports = {80, 443, 22, 8080}
allowed_protocols = {"TCP", "UDP"}

if packet["source_ip"] in blocked_ips:
    verdict = "BLOCKED: Blacklisted Source IP"
elif packet["protocol"] not in allowed_protocols:
    verdict = f"DROPPED: Unsupported Protocol ({packet['protocol']})"
elif packet["destination_port"] not in allowed_ports:
    verdict = f"DROPPED: Destination Port {packet['destination_port']} is closed"
elif packet["payload_size_kb"] > 1024:
    if packet["destination_port"] == 443 and "ACK" in packet["flags"]:
        verdict = "WARNING: Large HTTPS Packet (Forwarded to Deep Packet Inspection)"
    else:
        verdict = f"DROPPED: Payload ({packet['payload_size_kb']} KB) exceeds 1024 KB limit"
else:
    verdict = "ACCEPTED: Packet Cleared All Firewall Rules"

print("--- Firewall Inspection Report ---")
print(f"Source IP: {packet['source_ip']} | Dest Port: {packet['destination_port']} | Protocol: {packet['protocol']}")
print(f"Payload Size: {packet['payload_size_kb']} KB | Flags: {packet['flags']}")
print(f"Verdict: {verdict}")
