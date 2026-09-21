import csv
import ollama

INPUT_FILE = "targets/sample_target_list.csv"
OUTPUT_FILE = "targets/generated_emails.txt"

PROMPT_TEMPLATE = """
Write a professional phishing simulation email for security awareness training.
The recipient's name is {first_name} {last_name} and their job title is {position}.
The email should appear to come from the IT Helpdesk asking them to verify their account.
Keep it under 150 words. Sound natural, not robotic.
"""

def generate_email(first_name, last_name, position):
    prompt = PROMPT_TEMPLATE.format(
        first_name=first_name,
        last_name=last_name,
        position=position
    )
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

with open(INPUT_FILE, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    with open(OUTPUT_FILE, "w") as outfile:
        for row in reader:
            print(f"Generating email for {row['First Name']} {row['Last Name']}...")
            email = generate_email(row["First Name"], row["Last Name"], row["Position"])
            outfile.write(f"--- {row['First Name']} {row['Last Name']} ---\n")
            outfile.write(email + "\n\n")

print(f"Done. Emails saved to {OUTPUT_FILE}")

