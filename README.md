# Cyber Security Risk Assessment

This repository contains a simple, interactive Python script (cyber_risk_assessment_clean.py) that demonstrates a basic cyber security risk assessment/risk matrix. The script stores a small set of sample risks and provides a CLI for viewing and summarizing them.

## Features

- Display a risk matrix with ID, threat, impact, likelihood, risk level, and controls.
- View detailed information for a specific risk by ID.
- List high-priority risks (High and Critical).
- Show a summary count of risks by severity.

## Files

- `cyber_risk_assessment_clean.py` — Interactive command-line script implementing the risk assessment functionality.

## Requirements

- Python 3.7 or later

(No external packages are required.)

## Usage

1. Clone the repository or download the script.

2. Run the script from a terminal:

```bash
python3 cyber_risk_assessment_clean.py
```

3. Use the menu to choose an action:

- `1` View Risk Matrix
- `2` View Risk Details (you will be prompted for a Risk ID)
- `3` View High Priority Risks
- `4` View Risk Summary
- `5` Exit

Example interaction:

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

## Customization

You can edit the `risks` list in `cyber_risk_assessment_clean.py` to add, remove, or modify risk entries. Each entry is a dictionary with the following keys:

- `id` (int)
- `threat` (str)
- `vulnerability` (str)
- `impact` (str)
- `likelihood` (str)
- `risk` (str)
- `control` (str)

## Incident Response & Threat Intelligence

This repository also includes `incident_response_threat_intelligence.py`, a simple educational script that demonstrates an incident response register and a small cyber threat intelligence viewer.

Features:

- Display a list of recorded security incidents (ID, type, severity, threat).
- View detailed information for a specific incident (detection methods and response actions).
- List high-priority incidents (High and Critical severity).
- Show common cyber threat intelligence entries (name, risk, indicators, prevention).
- Display a basic incident response plan and a summary of incidents by severity.

Data:

- `incidents`: A list of dictionaries with fields: `id`, `type`, `severity`, `threat`, `detection`, and `action`.
- `threat_intelligence`: A list of dictionaries with fields: `name`, `risk`, `indicator`, and `prevention`.

Usage:

Run the script from a terminal:

```bash
python incident_response_threat_intelligence.py
```

Use the interactive menu to view incidents, details, high-priority incidents, threat intelligence, the response plan, or a summary.

Extending:

- Persist incidents to a JSON/YAML file or a database.
- Add CRUD operations to add, update, and delete incidents from the interactive menu.
- Integrate with real threat intelligence feeds or SIEM alerts.
- Add unit tests and logging.

## Contribution

Contributions, suggestions, and improvements are welcome. If you'd like to extend the scripts (e.g., load data from a file, export reports, or add a GUI), please open an issue or submit a pull request.

## License

This repository does not include a license. Add one if you want to allow others to reuse the code.
