remote_adr = []
request_type = []
requested_resorce = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as log_files:
    for line in log_files:
        remote_adr.append(line.split()[0])
        request_type.append(line.split()[5].replace('"', ''))
        requested_resorce.append(line.split()[6])

everything = list(zip(remote_adr,request_type, requested_resorce))
print(everything)
