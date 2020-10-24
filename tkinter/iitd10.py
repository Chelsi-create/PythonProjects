with open('records.txt', 'r') as read_f:
    text = read_f.read()
read_f.close()
print(text)

with open('records.txt', 'w') as write_f:
    write_f.write(text)
write_f.close()
