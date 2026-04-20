# Mirai Botnet Detection Module for OWASP Nettacker

**GSoC 2026 Contribution by Muhammad Ahmad**

### Goal
This module extends OWASP Nettacker to detect IoT devices vulnerable to the Mirai botnet by testing for common default telnet credentials.

### How It Works
1. Scans target IP for open port 23 (telnet)
2. Attempts login using top 10 username:password pairs from Mirai source code
3. Reports vulnerability if login succeeds

### GSoC 2026 Plan
During GSoC 2026, I will extend this module to:
1. Add all 60+ Mirai credentials from the original source code
2. Add SSH support for port 22  
3. Integrate with Nettacker’s native reporting engine
4. Add multi-threading for faster large-scale scans

### Author
Muhammad Ahmad  
BSCS 6th Semester, CGPA 3.95  
Graduating July 2027  
Jaranwala, Pakistan
