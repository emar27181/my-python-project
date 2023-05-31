data = {}

with open('data/output/OutputData.txt', 'r') as file:
    for line in file:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = int(value.strip())
            data[key] = value
            # print(f"{key}: {value}")
            
print("data:", data)

