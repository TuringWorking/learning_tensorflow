# learning_tensorflow
# this my first readme

import numpy as np
Z = np.random.randint(1, 30, 10)

print(Z)
sqrt_result = 0
for i in Z:
    sqrt_result = sqrt_result + i*i

print(np.sqrt(sqrt_result))

