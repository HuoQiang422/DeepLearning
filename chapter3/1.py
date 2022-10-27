import matplotlib_inline.backend_inline
import torch
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import random

num_inputs=2
num_examples=1000
true_w=[2,-3.4]
true_b=4.2
features = torch.randn(num_examples, num_inputs, dtype=torch.float32)
labels=true_w[0]*features[:,0]+true_w[1]*features[:,1]+true_b
labels+=torch.tensor(np.random.normal(0,0.01,size=labels.size()),dtype=torch.float32)
print(features[0], labels[0])

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
fig_size=(3.5, 2.5)
plt.rcParams['figure.figsize'] =fig_size
plt.scatter(features[:, 1].numpy(),labels.numpy(),1);
plt.show()



