incidents = [
    {
        "id": 1,
        "type": "Phishing Attack",
        "severity": "High",
        "threat": "Credential theft",
        "detection": "Suspicious emails and login attempts",
        "action": "Block malicious sender and reset affected passwords"
    },
    {
        "id": 2,
        "type": "Malware Infection",
        "severity": "Critical",
        "threat": "Malicious software",
        "detection": "Endpoint security alerts",
        "action": "Isolate infected system and remove malware"
    },
    {
        "id": 3,
        "type": "Data Breach",
        "severity": "Critical",
        "threat": "Unauthorized data access",
        "detection": "Unusual database activity",
        "action": "Block unauthorized access and investigate affected data"
    },
    {
        "id": 4,
        "type": "DDoS Attack",
        "severity": "High",
        "threat": "Service disruption",
        "detection": "Abnormal network traffic",
        "action": "Enable DDoS protection and filter malicious traffic"
    },
    {
        "id": 5,
        "type": "Unauthorized Access",
        "severity": "Medium",
        "threat": "Compromised account",
        "detection": "Unusual login location or activity",
        "action": "Disable account and enforce password reset"
    }
]


threat_intelligence = [
    {
        "name": "Phishing",
        "risk": "Credential theft",
        "indicator": "Suspicious links and emails",
        "prevention": "Email filtering and user awareness"
    },
    {
        "name": "Ransomware",
        "risk": "Data encryption",
        "indicator": "Unusual file encryption",
        "prevention": "Endpoint protection and regular backups"
    },
    {
        "name": "DDoS",
        "risk": "Service unavailability",
        "indicator": "Large traffic spikes",
        "prevention": "Firewall and DDoS protection"
    },
    {
        "name": "Data Breach",
        "risk": "Data exposure",
        "indicator": "Unauthorized database access",
        "prevention": "Encryption and access control"
    }
]


def show_incidents():
    print("\nINCIDENT RESPONSE REGISTER")
    print("=" * 80)

    print(
        f"{'ID':<4}"
        f"{'INCIDENT':<22}"
        f"{'SEVERITY':<12}"
        f"{'THREAT':<25}"
    )

    print("-" * 80)

    for incident in incidents:
        print(
            f"{incident['id']:<4}"
            f"{incident['type']:<22}"
            f"{incident['severity']:<12}"
            f"{incident['threat']:<25}"
        )


def show_incident_details():
    try:
        incident_id = int(input("\nEnter incident ID: "))
    except ValueError:
        print("Invalid incident ID.")
        return

    for incident in incidents:
        if incident["id"] == incident_id:
            print("\nIncident Details")
            print("-" * 50)
            print(f"Incident: {incident['type']}")
            print(f"Severity: {incident['severity']}")
            print(f"Threat: {incident['threat']}")
            print(f"Detection: {incident['detection']}")
            print(f"Response: {incident['action']}")
            return

    print("Incident not found.")


def show_high_priority():
    print("\nHIGH PRIORITY INCIDENTS")
    print("=" * 50)

    for incident in incidents:
        if incident["severity"] in ["High", "Critical"]:
            print(
                f"{incident['id']}. "
                f"{incident['type']} - "
                f"{incident['severity']}"
            )


def show_threat_intelligence():
    print("\nCYBER THREAT INTELLIGENCE")
    print("=" * 70)

    for threat in threat_intelligence:
        print(f"\nThreat: {threat['name']}")
        print(f"Risk: {threat['risk']}")
        print(f"Indicator: {threat['indicator']}")
        print(f"Prevention: {threat['prevention']}")


def show_response_plan():
    print("\nINCIDENT RESPONSE PLAN")
    print("=" * 60)

    steps = [
        "1. Identify and detect the security incident",
        "2. Assess the severity and impact",
        "3. Contain the affected system or service",
        "4. Remove the threat and fix vulnerabilities",
        "5. Restore affected services",
        "6. Monitor the environment",
        "7. Document the incident and review the response"
    ]

    for step in steps:
        print(step)


def show_summary():
    total = len(incidents)

    critical = sum(
        incident["severity"] == "Critical"
        for incident in incidents
    )

    high = sum(
        incident["severity"] == "High"
        for incident in incidents
    )

    medium = sum(
        incident["severity"] == "Medium"
        for incident in incidents
    )

    print("\nINCIDENT SUMMARY")
    print("=" * 40)
    print(f"Total Incidents : {total}")
    print(f"Critical        : {critical}")
    print(f"High            : {high}")
    print(f"Medium          : {medium}")


def main():
    while True:
        print("\nINCIDENT RESPONSE AND THREAT INTELLIGENCE")
        print("1. View Incidents")
        print("2. View Incident Details")
        print("3. View High Priority Incidents")
        print("4. View Threat Intelligence")
        print("5. View Incident Response Plan")
        print("6. View Summary")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_incidents()
        elif choice == "2":
            show_incident_details()
        elif choice == "3":
            show_high_priority()
        elif choice == "4":
            show_threat_intelligence()
        elif choice == "5":
            show_response_plan()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()