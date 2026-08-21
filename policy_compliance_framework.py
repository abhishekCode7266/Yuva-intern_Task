policies = [
    {
        "id": 1,
        "area": "Access Control",
        "requirement": "Strong authentication and role-based access",
        "status": "Partial",
        "gap": "MFA is not implemented for all users",
        "recommendation": "Implement MFA and role-based access control"
    },
    {
        "id": 2,
        "area": "Data Protection",
        "requirement": "Protection of sensitive citizen data",
        "status": "Compliant",
        "gap": "No major gap identified",
        "recommendation": "Continue encryption and regular security reviews"
    },
    {
        "id": 3,
        "area": "Incident Response",
        "requirement": "Documented incident response procedure",
        "status": "Partial",
        "gap": "Incident response plan needs regular testing",
        "recommendation": "Create and test an incident response plan"
    },
    {
        "id": 4,
        "area": "Security Awareness",
        "requirement": "Regular cybersecurity awareness training",
        "status": "Non-Compliant",
        "gap": "Training is not conducted regularly",
        "recommendation": "Conduct mandatory security awareness training"
    },
    {
        "id": 5,
        "area": "Backup and Recovery",
        "requirement": "Regular backup and disaster recovery",
        "status": "Partial",
        "gap": "Backup recovery testing is limited",
        "recommendation": "Schedule regular backup and recovery tests"
    },
    {
        "id": 6,
        "area": "Vulnerability Management",
        "requirement": "Regular vulnerability assessment",
        "status": "Non-Compliant",
        "gap": "Security assessments are not performed regularly",
        "recommendation": "Perform periodic vulnerability assessments"
    }
]


def show_policy_review():
    print("\nPOLICY REVIEW AND COMPLIANCE")
    print("=" * 90)

    print(
        f"{'ID':<4}"
        f"{'AREA':<22}"
        f"{'STATUS':<16}"
        f"{'REQUIREMENT'}"
    )

    print("-" * 90)

    for policy in policies:
        print(
            f"{policy['id']:<4}"
            f"{policy['area']:<22}"
            f"{policy['status']:<16}"
            f"{policy['requirement']}"
        )


def show_policy_details():
    try:
        policy_id = int(input("\nEnter policy ID: "))
    except ValueError:
        print("Invalid policy ID.")
        return

    for policy in policies:
        if policy["id"] == policy_id:
            print("\nPolicy Details")
            print("-" * 50)
            print(f"Area: {policy['area']}")
            print(f"Requirement: {policy['requirement']}")
            print(f"Status: {policy['status']}")
            print(f"Compliance Gap: {policy['gap']}")
            print(f"Recommendation: {policy['recommendation']}")
            return

    print("Policy not found.")


def show_compliance_gaps():
    print("\nCOMPLIANCE GAPS")
    print("=" * 70)

    found = False

    for policy in policies:
        if policy["status"] != "Compliant":
            found = True
            print(f"\n{policy['id']}. {policy['area']}")
            print(f"Status: {policy['status']}")
            print(f"Gap: {policy['gap']}")
            print(f"Recommendation: {policy['recommendation']}")

    if not found:
        print("No compliance gaps found.")


def show_recommendations():
    print("\nSECURITY RECOMMENDATIONS")
    print("=" * 60)

    for policy in policies:
        print(
            f"{policy['id']}. "
            f"{policy['recommendation']}"
        )


def show_summary():
    total = len(policies)

    compliant = sum(
        policy["status"] == "Compliant"
        for policy in policies
    )

    partial = sum(
        policy["status"] == "Partial"
        for policy in policies
    )

    non_compliant = sum(
        policy["status"] == "Non-Compliant"
        for policy in policies
    )

    print("\nCOMPLIANCE SUMMARY")
    print("=" * 40)
    print(f"Total Policies     : {total}")
    print(f"Compliant          : {compliant}")
    print(f"Partially Compliant: {partial}")
    print(f"Non-Compliant      : {non_compliant}")


def main():
    while True:
        print("\nPOLICY REVIEW AND COMPLIANCE SYSTEM")
        print("1. View Policy Review")
        print("2. View Policy Details")
        print("3. View Compliance Gaps")
        print("4. View Recommendations")
        print("5. View Compliance Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_policy_review()
        elif choice == "2":
            show_policy_details()
        elif choice == "3":
            show_compliance_gaps()
        elif choice == "4":
            show_recommendations()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()