# AWS-Cost-Explorer-Dashboard

<h2>Overview</h2>
A web application built with Flask that interacts with AWS Cost Explorer API to fetch, display, and visualize your AWS cost and usage data. This tool helps users monitor and analyze their cloud expenses over customizable date ranges.
<br />


<h2>## 🚀 Features</h2>

- <b>Retrieve detailed AWS cost data by service and date range</b> 
- <b>Filter costs by time period with user input (start and end dates)</b>
- <b>Group costs by AWS service dimension</b>
- <b>Display costs in a clean, tabular format with total cost summary</b>
- <b>Supports daily granularity of usage and cost data</b>
- <b>Simple and intuitive web interface</b>
- <b>Error handling and informative messages on API call failures</b>


<h2>Tech Stack</h2>

- <b>**Flask** (Python web framework)</b>
- <b>**boto3** (AWS SDK for Python)</b>
- <b>**EC2** (Ubuntu host)</b>
- <b>**IAM Role** (for secure API access)</b>

<h2>Setup Instructions</h2>

- <b>AWS Account with Cost Explorer enabled</b>
- <b>AWS credentials configured locally (~/.aws/credentials) with permissions for Cost Explorer (ce:GetCostAndUsage)</b>
- <b>Python 3 installed</b>
- <b>Pip package manager</b>

<h2></h2>

- <b>Enforce Password Policy: Strong domain password rules</b>
- <b>Disable USB Storage: Prevent use of removable media</b>
- <b>Force Wallpaper: Enforce a company-wide desktop background</b>

<h2>Screenshots</h2>

<p align="center">
 AWS Cost_Explorer: <br/>
 <img src="https://i.imgur.com/zKSOXCV.png" height="80%" width="80%" alt="Cost"/>
 <br />
 <br />
 IAM Role:  <br/>
<img src="https://i.imgur.com/qVovDKL.png" height="80%" width="80%" alt="JSON"/>
 <br />
 <br />

