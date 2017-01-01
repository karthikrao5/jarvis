import random, time, sys
print sys.version_info
sys.stdout.write("Hello\n")

for x in range(10):
    sys.stdout(str(random.randint(23,28))+" C")
    time.sleep(random.uniform(0.4,5))

sys.stdout.flush()