import csv
import socket
import numpy as np


data_headers = []
data = []


with open('dataset_ransomware.csv', 'rb') as f:
    reader = csv.DictReader(f, delimiter=",",skipinitialspace=True)
    data_headers = reader.fieldnames

    i = 0
    for row in reader:
        temp_row = row
        i += 1
        # Empty IP case
        if(row.get(data_headers[7]).strip() == ""):
            print "\nEmpty IP\n\tChecking: ", row.get(data_headers[3])
            try:
                dns_lookup = socket.gethostbyaddr(row.get(data_headers[3]))
                print dns_lookup
                temp_row[data_headers[7]] = dns_lookup[2][0]
            except:
                print "\tHost address cannot be resolved."
                continue
        
        # Multiple IP addresses
        elif("|" in row.get(data_headers[7])):
            print "\nMultiple IP detected"
            ip_list = (row.get(data_headers[7])).split("|")
            ip_list = list(set(ip_list))
            print ip_list
            for elem in ip_list:
                temp_row = row
                temp_row[data_headers[7]] = elem
                print temp_row
                data.append(dict(temp_row))
            continue
        
        data.append(temp_row)

        # if(i > 100):
        #     break

print "Original data size = ", i
print "Size of processed data = ", len(data)

# Save processed data
with open("processed_data.csv", "wb") as output_file:
    writer = csv.writer(output_file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data_headers)
    for row in data:
        temp_list = []
        for head in data_headers:
            temp_list.append(row.get(head))
        writer.writerow(temp_list)