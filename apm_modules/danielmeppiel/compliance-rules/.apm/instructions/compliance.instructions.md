---
applyTo: "**/*.{py,js,ts,tsx,java,cpp,c,h,hpp,cs,php,rb,go,rs,swift,kt}"
description: "Data privacy and compliance standards for secure development"
---

# Data Privacy & Compliance Standards

## GDPR Compliance Requirements

### Personal Data Handling
- **Data Minimization**: Only collect and process personal data that is necessary for specific, explicit, and legitimate purposes
- **Consent Management**: Implement clear consent mechanisms with opt-in/opt-out functionality
- **Right to Erasure**: Provide mechanisms for data deletion upon user request
- **Data Portability**: Enable users to export their data in machine-readable formats

### Code Implementation Standards
- Use encryption for all personal data storage (AES-256 minimum)
- Implement secure authentication with multi-factor authentication
- Log all data access events with timestamps and user identification
- Never store sensitive data in plain text or logs

## Legal Review Checklist

### Before Code Deployment
- [ ] No hardcoded credentials or API keys
- [ ] All user inputs are validated and sanitized
- [ ] Error messages don't leak sensitive information
- [ ] Third-party dependencies are approved and up-to-date
- [ ] Data retention policies are implemented

### AI/ML Specific Requirements
- [ ] Model bias testing completed
- [ ] Training data provenance documented
- [ ] Model interpretability measures in place
- [ ] Algorithmic impact assessment conducted

## Audit Trail Requirements

### Mandatory Logging
- Authentication attempts (successful and failed)
- Data access patterns and queries
- Configuration changes
- Administrative actions
- Model training and deployment events

### Log Retention
- Security logs: 7 years minimum
- Audit logs: 5 years minimum
- Performance logs: 1 year minimum

**Remember**: When in doubt about compliance requirements, consult the Legal & Compliance team before proceeding.