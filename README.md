# AWS-Cost-Explorer-Dashboard

<h2>Description</h2>
A simple Flask-based web dashboard that visualizes your AWS service costs using the Cost Explorer API. Hosted on an EC2 instance and secured using IAM roles.
<br />


<h2>## 🚀 Features</h2>

- <b>Query AWS Cost Explorer for daily or monthly usage</b> 
- <b>Select custom date ranges (UTC or HST aligned)</b>
- <b>Break down costs by AWS service</b>
- <b>Deployed on EC2 with auto-starting Flask app</b>
- <b>IAM Role-based secure access (no hardcoded credentials)</b>


<h2>Tech Stack</h2>

- <b>**Flask** (Python web framework)</b>
- <b>**boto3** (AWS SDK for Python)</b>
- <b>**EC2** (Ubuntu host)</b>
- <b>**IAM Role** (for secure API access)</b>

<h2>Environment Setup</h2>

- <b>Virtual Machines: Created in VirtualBox</b>
- <b>Network: Internal/Host-only adapter for isolated communication</b>
- <b>Domain: `david.com`</b>
- <b>DNS and AD DS installed on Windows Server 2022</b>

<h2>Group Policy Configuration Samples</h2>

- <b>Enforce Password Policy: Strong domain password rules</b>
- <b>Disable USB Storage: Prevent use of removable media</b>
- <b>Force Wallpaper: Enforce a company-wide desktop background</b>

<h2>Screenshots</h2>

<p align="center">
 Active Directory Diagram: <br/>
 <img src="https://i.imgur.com/9xb6W00.png" height="80%" width="80%" alt="Diagram"/>
 <br />
 <br />
 VirtualBox Layout:  <br/>
<img src="https://i.imgur.com/kU1XprL.png" height="80%" width="80%" alt="DC & Client"/>
 <br />
 <br />
AD DS, DHCP, DNS Installed: <br/>
<img src="https://i.imgur.com/yYGSV70.png" height="80%" width="80%" alt="Active Directory Domain Services (AD DS), DHCP, DNS"/>
<br />
<br />
 New Forest Configuration:  <br/>
<img src="https://i.imgur.com/nqU1hcS.png" height="80%" width="80%"  alt="Domain name: david.com"/>
<br />
<br />

<h2>PowerShell Automation</h2>

Create_User Script: <br/>
<img src="https://i.imgur.com/GpF8b8t.png" height="80%" width="80%" alt="PowerShell script"/>
<br />
<br />
Delete_user:  <br/>
<img src="https://i.imgur.com/WkPRIgw.png" height="80%" width="80%" alt="PowerShell script"/>
<br />
<br />

<h2>Group Policy Configuration Samples</h2>
Enforce Password Policy: Strong domain password rules:  <br/>
<img src="https://i.imgur.com/YMNGUY6.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Disable USB Storage: Prevent use of removable media:  <br/>
<img src="https://i.imgur.com/SXzeZfS.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Force Wallpaper: Enforce a company-wide desktop background:  <br/>
<img src="https://i.imgur.com/4TesfRu.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>
