import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(3,2),columns = ["Scooter","Bike"], index = ['a','b','c'])
print(df)