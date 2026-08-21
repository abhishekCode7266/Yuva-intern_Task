# Cyber Security Risk Assessment

This repository contains a simple, interactive Python script (cyber_risk_assessment_clean.py) that demonstrates a basic cyber security risk assessment/risk matrix. The script stores a small set of predefined risks and provides a command-line menu for viewing the matrix, inspecting details, listing high-priority items, and viewing a summary.

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

## Contribution

Contributions, suggestions, and improvements are welcome. If you'd like to extend the script (e.g., load risks from a file, export reports, or add a GUI), please open an issue or submit a pull request.

## License

This repository does not include a license. Add one if you want to allow others to reuse the code.
