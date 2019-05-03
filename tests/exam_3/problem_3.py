import numpy as np
import matplotlib.pyplot as plt

units = ["CS", "ChBE", "Civil", "M&IE", "General", "CpE"]
enrollments = [552, 563, 731, 1463, 210, 410]
# Write the missing statements below this comment
# Do not import anything else
# See question 1 for a description # See question 1 for a description

plt.figure()
plt.pie(x = enrollments, explode=[.05,.05,.05,.05,.05,.05], colors=["blue","gold"], labels=units, counterclock=False)
plt.title("Matplotlib bakery: A pie")
plt.show()
