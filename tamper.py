import random

input_file = "secure_application.elf"
output_file = "application_hacked.elf"

with open(input_file, "rb") as f:
    data = bytearray(f.read())

# choose random location to corrupt
for i in range(20):   # corrupt 20 bytes
    index = random.randint(0, len(data)-1)
    data[index] = random.randint(0,255)

with open(output_file, "wb") as f:
    f.write(data)

print("Firmware tampered successfully!")
