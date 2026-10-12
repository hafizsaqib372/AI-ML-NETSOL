"""
1. An organization manages employees using a nested dictionary where each employee ID maps to personal info, department, a tuple of assigned project IDs, and a list of quarterly performance ratings.

Perform the following tasks:
- Add a new employee 'EMP103' (name: 'Zain Malik', department: 'Cybersecurity', projects: ('PRJ_AUTH', 'PRJ_CRYPTO'), ratings: [91, 89, 94, 96]) to 'company_data'.
- Update 'EMP101' by appending a new rating 98 to their list and changing their department to 'Senior AI Engineering'.
- Display all active employee IDs using .keys().
- Extract the ratings of 'EMP102', calculate and print their total score, average rating, highest rating, and lowest rating.
- Remove 'EMP103' from 'company_data' using .pop() and store the removed record in 'archived_emp'.
- Iterate over the remaining employees using .items() and print a formatted summary showing employee ID, name, department, total projects count (len of tuple), and average rating (mean of ratings list).
"""

company_data = {
    "EMP101": {
        "name": "Sarah Ahmed",
        "department": "AI Engineering",
        "projects": ("PRJ_AI", "PRJ_CLOUD"),
        "ratings": [88, 92, 95, 90]
    },
    "EMP102": {
        "name": "Bilal Khan",
        "department": "Data Science",
        "projects": ("PRJ_AI", "PRJ_ANALYTICS", "PRJ_OPS"),
        "ratings": [78, 85, 80, 88]
    }
}

company_data["EMP103"] = {
    "name": "Zain Malik",
    "department": "Cybersecurity",
    "projects": ("PRJ_AUTH", "PRJ_CRYPTO"),
    "ratings": [91, 89, 94, 96]
}
print(f"Added EMP103: {company_data['EMP103']}")

company_data["EMP101"]["ratings"].append(98)
company_data["EMP101"]["department"] = "Senior AI Engineering"
print(f"Updated EMP101: {company_data['EMP101']}")

print(f"All Employee IDs: {list(company_data.keys())}")

emp102_ratings = company_data["EMP102"]["ratings"]
emp102_total = sum(emp102_ratings)
emp102_avg = emp102_total / len(emp102_ratings)
emp102_max = max(emp102_ratings)
emp102_min = min(emp102_ratings)

print(f"EMP102 Stats -> Total: {emp102_total}, Avg: {emp102_avg:.2f}, Max: {emp102_max}, Min: {emp102_min}")

archived_emp = company_data.pop("EMP103")
print(f"Archived Employee: {archived_emp['name']} from {archived_emp['department']}")

print("\n--- Active Employees Summary ---")
for emp_id, emp_info in company_data.items():
    proj_count = len(emp_info["projects"])
    avg_rating = sum(emp_info["ratings"]) / len(emp_info["ratings"])
    print(f"ID: {emp_id} | Name: {emp_info['name']} | Dept: {emp_info['department']} | Projects: {proj_count} | Avg Rating: {avg_rating:.2f}")
