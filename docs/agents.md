# AI Agents

The system uses multiple specialized AI agents. Each agent is responsible
for a specific decision-making task.

## 1. Complaint Understanding Agent
- Analyzes grievance text
- Extracts key issue and context
- Handles spelling and language variations

## 2. Department Classification Agent
- Maps grievances to the correct government department
- Examples: Water, Electricity, Roads, Police

## 3. Urgency & Priority Agent
- Assigns urgency levels based on keywords and context
- Example: safety-related issues marked as high priority

## 4. SLA Prediction Agent
- Predicts expected resolution time using historical data
- Assigns a deadline to each grievance

## 5. Escalation Agent
- Monitors grievances for SLA breaches
- Automatically escalates delayed cases
