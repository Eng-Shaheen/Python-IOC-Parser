# Analyst Observations – Python IOC Parser

## Detection Summary
Automated analysis of system and network logs identified multiple indicators of compromise related to brute-force authentication attempts and potential malware activity.

## Key Findings
- Two external IP addresses performed repeated SSH login failures.
- One IP successfully authenticated after multiple failures, indicating possible credential compromise.
- Repeated outbound connections to suspicious domains were observed.
- Multiple file hashes appeared more than once, suggesting persistent malicious artifacts.

## Threat Assessment
Severity: High

Repeated authentication failures followed by success combined with suspicious outbound traffic indicates a high likelihood of compromise.

## SOC Value
This automation enables analysts to:
- Rapidly extract and prioritize IOCs
- Reduce manual log review time
- Identify high-risk indicators based on frequency
- Support incident triage and escalation workflows

## Extended Dataset Analysis

An expanded enterprise-style dataset was analyzed to simulate higher log volume and realistic SOC conditions.

### Additional Findings
- One IP address exhibited sustained brute-force behavior across multiple time windows.
- Successful authentication following repeated failures indicates high-confidence compromise.
- Malicious domains appeared repeatedly in firewall and proxy logs, increasing confidence.
- Repeated hash sightings suggest persistent malware activity rather than a one-time event.

### Analyst Assessment
The extended dataset reinforces initial findings and demonstrates the tool’s ability to scale with increased log volume while maintaining accurate IOC prioritization.
