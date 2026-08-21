security_controls = [
    {
        "id": 1,
        "name": "Firewall",
        "category": "Network Security",
        "purpose": "Controls incoming and outgoing network traffic",
        "status": "Enabled"  
    },
    {
        "id": 2,
        "name": "Web Application Firewall",
        "category": "Application Security",
        "purpose": "Protects web applications from malicious requests",
        "status": "Enabled"
    },
    {
        "id": 3,
        "name": "Multi-Factor Authentication",
        "category": "Identity Security",
        "purpose": "Provides additional authentication protection",
        "status": "Enabled"
    },
    {
        "id": 4,
        "name": "Data Encryption",
        "category": "Data Security",
        "purpose": "Protects sensitive citizen information",
        "status": "Enabled"
    },
    {
        "id": 5,
        "name": "Intrusion Detection",
        "category": "Monitoring",
        "purpose": "Detects suspicious network activity",
        "status": "Enabled"
    },
    {
        "id": 6,
        "name": "Backup System",
        "category": "Recovery",
        "purpose": "Restores services and data after an incident",
        "status": "Enabled"
    }
]


network_zones = [
    {
        "name": "Internet",
        "purpose": "Public access to digital services",
        "protection": "Firewall and DDoS protection"
    },
    {
        "name": "DMZ",
        "purpose": "Hosts public-facing applications",
        "protection": "Web Application Firewall"
    },
    {
        "name": "Application Network",
        "purpose": "Processes application requests",
        "protection": "Access control and network segmentation"
    },
    {
        "name": "Database Network",
        "purpose": "Stores sensitive citizen data",
        "protection": "Encryption and restricted access"
    }
]


def show_architecture():
    print("\nSECURITY ARCHITECTURE")
    print("=" * 70)

    for zone in network_zones:
        print(f"\nZone: {zone['name']}")
        print(f"Purpose: {zone['purpose']}")
        print(f"Protection: {zone['protection']}")


def show_security_controls():
    print("\nSECURITY CONTROLS")
    print("=" * 80)

    print(
        f"{'ID':<4}"
        f"{'CONTROL':<28}"
        f"{'CATEGORY':<22}"
        f"{'STATUS'}"
    )

    print("-" * 80)

    for control in security_controls:
        print(
            f"{control['id']:<4}"
            f"{control['name']:<28}"
            f"{control['category']:<22}"
            f"{control['status']}"
        )


def show_control_details():
    try:
        control_id = int(input("\nEnter control ID: "))
    except ValueError:
        print("Invalid control ID.")
        return

    for control in security_controls:
        if control["id"] == control_id:
            print("\nSecurity Control Details")
            print("-" * 50)
            print(f"Control: {control['name']}")
            print(f"Category: {control['category']}")
            print(f"Purpose: {control['purpose']}")
            print(f"Status: {control['status']}")
            return

    print("Control not found.")


def show_network_defense():
    print("\nNETWORK DEFENSE STRATEGY")
    print("=" * 60)

    strategies = [
        "Use firewalls to filter unauthorized network traffic.",
        "Separate public, application, and database networks.",
        "Use MFA for administrative and sensitive accounts.",
        "Encrypt sensitive data during storage and transmission.",
        "Monitor network activity for suspicious behavior.",
        "Apply security updates and patches regularly.",
        "Maintain regular backups for disaster recovery.",
        "Review security logs and alerts continuously."
    ]

    for number, strategy in enumerate(strategies, 1):
        print(f"{number}. {strategy}")


def show_monitoring():
    print("\nSECURITY MONITORING")
    print("=" * 60)

    monitoring = [
        "Firewall logs",
        "Web application logs",
        "Authentication logs",
        "Intrusion detection alerts",
        "Database access logs",
        "System activity logs"
    ]

    for item in monitoring:
        print(f"- {item}")


def show_summary():
    total_controls = len(security_controls)
    enabled = sum(
        control["status"] == "Enabled"
        for control in security_controls
    )

    print("\nSECURITY ARCHITECTURE SUMMARY")
    print("=" * 45)
    print(f"Network Zones       : {len(network_zones)}")
    print(f"Security Controls   : {total_controls}")
    print(f"Enabled Controls    : {enabled}")
    print("Monitoring          : Enabled")
    print("Network Segmentation: Enabled")
    print("Data Encryption     : Enabled")
    print("Backup Strategy     : Enabled")


def main():
    while True:
        print("\nSECURITY ARCHITECTURE AND NETWORK DEFENSE")
        print("1. View Security Architecture")
        print("2. View Security Controls")
        print("3. View Control Details")
        print("4. View Network Defense Strategy")
        print("5. View Security Monitoring")
        print("6. View Security Summary")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_architecture()
        elif choice == "2":
            show_security_controls()
        elif choice == "3":
            show_control_details()
        elif choice == "4":
            show_network_defense()
        elif choice == "5":
            show_monitoring()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()