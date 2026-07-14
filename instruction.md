there's an access log file at /app/access.log (apache format). read it and
write a summary as JSON to /app/report.json.

the JSON file should have these 3 fields:

- total_requests: how many lines are in the log (integer)
- unique_ips: how many different IP addresses made requests (integer)
- top_path: which URL path got the most hits (string)

success criteria:
1. /app/report.json must exist
2. total_requests must equal the total number of log entries
3. unique_ips must equal the count of distinct client IPs
4. top_path must equal the most requested URL path in the log
