# Simulate lotto 6/49 draw (numbers extraction).

import random
import time

print("The numbers are...")
print("\x1B[3msound of the balls moving\x1B[23m")

for i in range(0, 6):
    time.sleep(2)

    print(random.randint(1, 49))
