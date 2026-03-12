from log_validation import validate_and_normalize

logs = [
("2026-02-05 08:11:20"," warn ","db","DB timeout"),
("2026-02-05 08:11:21","error","auth","Login failed"),
("2026-02-05 08:11:22","debug","api","Request received"),
("2026-02-05 08:11:23","INFO","","Service started"),
("2026-02-05 08:11:24","WARN","disk"," ")
]

for log in logs:
    result = validate_and_normalize(log)
    print(result)
