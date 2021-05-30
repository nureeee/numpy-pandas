import pandas as pd
import numpy as np
a = {'name' :['김보람', '오우석', '이누리', 
                           '임수빈', '홍성훈'], 
                 'id' : ['boram', 'wooseok', 'nuri', 'subin',
                         'martin']}
df = pd.DataFrame(a)
df.to_csv('sample.csv')
