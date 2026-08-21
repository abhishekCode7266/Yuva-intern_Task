# Cyber Security Risk Assessment

This repository contains simple, interactive Python scripts that demonstrate cyber security concepts including risk assessment, incident response, threat intelligence, and security architecture. The scripts store sample data for educational purposes.

## Files

- `cyber_risk_assessment_clean.py` — Interactive command-line script implementing the risk assessment functionality.
- `incident_response_threat_intelligence.py` — Script demonstrating incident response register and cyber threat intelligence viewer.
- `security_architecture.py` — Script illustrating security architecture, network defense, and security controls.

## Requirements

- Python 3.7 or later

(No external packages are required.)

## Features

### 1. Cyber Security Risk Assessment

- Display a risk matrix with ID, threat, impact, likelihood, risk level, and controls.
- View detailed information for a specific risk by ID.
- List high-priority risks (High and Critical).
- Show a summary count of risks by severity.

**Usage:**

```bash
python3 cyber_risk_assessment_clean.py
```

**Menu Options:**

- `1` View Risk Matrix
- `2` View Risk Details (you will be prompted for a Risk ID)
- `3` View High Priority Risks
- `4` View Risk Summary
- `5` Exit

**Example Interaction:**

```
CYBER SECURITY RISK ASSESSMENT
1. View Risk Matrix
2. View Risk Details
3. View High Priority Risks
4. View Risk Summary
5. Exit
Enter your choice: 1

CYBER SECURITY RISK ASSESSMENT
--------------------------------------------------------------------------------
ID  THREAT                IMPACT    LIKELIHOOD   RISK         CONTROL
--------------------------------------------------------------------------------
1   Phishing Attack       High      High         Critical     Security awareness training and MFA
... (other rows)
```

**Customization:**

You can edit the `risks` list in `cyber_risk_assessment_clean.py` to add, remove, or modify risk entries. Each entry is a dictionary with the following keys:

- `id` (int)
- `threat` (str)
- `vulnerability` (str)
- `impact` (str)
- `likelihood` (str)
- `risk` (str)
- `control` (str)

### 2. Incident Response & Threat Intelligence

This educational script demonstrates an incident response register and a cyber threat intelligence viewer.

**Features:**

- Display a list of recorded security incidents (ID, type, severity, threat).
- View detailed information for a specific incident (detection methods and response actions).
- List high-priority incidents (High and Critical severity).
- Show common cyber threat intelligence entries (name, risk, indicators, prevention).
- Display a basic incident response plan and a summary of incidents by severity.

**Data:**

- `incidents`: A list of dictionaries with fields: `id`, `type`, `severity`, `threat`, `detection`, and `action`.
- `threat_intelligence`: A list of dictionaries with fields: `name`, `risk`, `indicator`, and `prevention`.

**Usage:**

```bash
python incident_response_threat_intelligence.py
```

**Menu Options:**

1. View Incidents
2. View Incident Details
3. View High Priority Incidents
4. View Threat Intelligence
5. View Incident Response Plan
6. View Summary
7. Exit

**Extending:**

- Persist incidents to a JSON/YAML file or a database.
- Add CRUD operations to add, update, and delete incidents from the interactive menu.
- Integrate with real threat intelligence feeds or SIEM alerts.
- Add unit tests and logging.

### 3. Security Architecture & Network Defense

This educational script illustrates security architecture principles, network defense strategies, and security controls.

**Features:**

- Display security architecture and network zones (Internet, DMZ, Application Network, Database Network).
- View configured security controls (Firewall, WAF, MFA, Data Encryption, Intrusion Detection, Backup System).
- View detailed information for a specific security control by ID.
- Display network defense strategy and best practices.
- View security monitoring components and logs.
- Show a summary of enabled controls and architecture components.

**Data:**

- `security_controls`: A list of dictionaries with fields: `id`, `name`, `category`, `purpose`, and `status`.
- `network_zones`: A list of dictionaries with fields: `name`, `purpose`, and `protection`.

**Usage:**

```bash
python security_architecture.py
```

**Menu Options:**

1. View Security Architecture
2. View Security Controls
3. View Control Details
4. View Network Defense Strategy
5. View Security Monitoring
6. View Security Summary
7. Exit

**Security Controls Included:**

- Firewall (Network Security)
- Web Application Firewall (Application Security)
- Multi-Factor Authentication (Identity Security)
- Data Encryption (Data Security)
- Intrusion Detection (Monitoring)
- Backup System (Recovery)

**Network Zones:**

- Internet (Public access with Firewall and DDoS protection)
- DMZ (Public-facing applications with WAF)
- Application Network (Processing with access control and segmentation)
- Database Network (Sensitive data with encryption and restricted access)

## Contribution

Contributions, suggestions, and improvements are welcome. If you'd like to extend the scripts (e.g., load data from a file, export reports, add a GUI, or integrate with real systems), please open an issue or submit a pull request.

## License

This repository does not include a license. Add one if you want to allow others to reuse the code.
