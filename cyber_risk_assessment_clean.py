risks = [
    {
        "id": 1,
        "threat": "Phishing Attack",
        "vulnerability": "Lack of user awareness",
        "impact": "High",
        "likelihood": "High",
        "risk": "Critical",
        "control": "Security awareness training and MFA" 
    },
    {
        "id": 2,
        "threat": "Data Breach",
        "vulnerability": "Weak access controls",
        "impact": "High",
        "likelihood": "Medium",
        "risk": "High",
        "control": "Encryption and role-based access control"
    },
    {
        "id": 3,
        "threat": "Malware Attack",
        "vulnerability": "Outdated software",
        "impact": "High",
        "likelihood": "Medium",
        "risk": "High",
        "control": "Regular updates and endpoint protection"
    },
    {
        "id": 4,
        "threat": "DDoS Attack",
        "vulnerability": "Insufficient network protection",
        "impact": "High",
        "likelihood": "Medium",
        "risk": "High",
        "control": "Firewall and DDoS protection"
    },
    {
        "id": 5,
        "threat": "Unauthorized Access",
        "vulnerability": "Weak passwords",
        "impact": "Medium",
        "likelihood": "Medium",
        "risk": "Medium",
        "control": "Strong passwords and multi-factor authentication"
    },
    {
        "id": 6,
        "threat": "Insider Threat",
        "vulnerability": "Excessive user privileges",
        "impact": "High",
        "likelihood": "Low",
        "risk": "Medium",
        "control": "Least privilege and activity monitoring"
    }
]


def display_risk_matrix():
    print("\nCYBER SECURITY RISK ASSESSMENT")
    print("=" * 80)

    print(
        f"{'ID':<4}"
        f"{'THREAT':<22}"
        f"{'IMPACT':<10}"
        f"{'LIKELIHOOD':<12}"
        f"{'RISK':<12}"
        f"{'CONTROL'}"
    )

    print("-" * 80)

    for item in risks:
        print(
            f"{item['id']:<4}"
            f"{item['threat']:<22}"
            f"{item['impact']:<10}"
            f"{item['likelihood']:<12}"
            f"{item['risk']:<12}"
            f"{item['control']}"
        )


def show_details():
    try:
        risk_id = int(input("\nEnter Risk ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for item in risks:
        if item["id"] == risk_id:
            print("\nRisk Details")
            print("-" * 40)
            print(f"Threat: {item['threat']}")
            print(f"Vulnerability: {item['vulnerability']}")
            print(f"Impact: {item['impact']}")
            print(f"Likelihood: {item['likelihood']}")
            print(f"Risk Level: {item['risk']}")
            print(f"Control: {item['control']}")
            return

    print("Risk not found.")


def show_high_risks():
    print("\nHIGH PRIORITY RISKS")
    print("=" * 50)

    for item in risks:
        if item["risk"] in ["High", "Critical"]:
            print(
                f"{item['id']}. {item['threat']} - "
                f"{item['risk']}"
            )


def show_summary():
    total = len(risks)
    critical = sum(item["risk"] == "Critical" for item in risks)
    high = sum(item["risk"] == "High" for item in risks)
    medium = sum(item["risk"] == "Medium" for item in risks)

    print("\nRISK SUMMARY")
    print("=" * 40)
    print(f"Total Risks     : {total}")
    print(f"Critical Risks  : {critical}")
    print(f"High Risks      : {high}")
    print(f"Medium Risks    : {medium}")


def main():
    while True:
        print("\nCYBER SECURITY RISK ASSESSMENT")
        print("1. View Risk Matrix")
        print("2. View Risk Details")
        print("3. View High Priority Risks")
        print("4. View Risk Summary")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_risk_matrix()
        elif choice == "2":
            show_details()
        elif choice == "3":
            show_high_risks()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()