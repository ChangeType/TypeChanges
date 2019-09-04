import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

c = pd.read_csv("/Users/ameya/ICSE2020Data/ClasstypeChangesForTypeMigrationPerCommit.csv")
plt.figure(figsize=(10,3))
sns.set(font_scale=1.5)
g = sns.violinplot(c)
# g.set_xscale("log")

plt.tight_layout()
plt.savefig("/Users/ameya/ICSE2020Data/ClassTypeMigrationRepetitiveness.svg", format="svg", dpi=300,bbox_inches='tight')

figure = svg2rlg("/Users/ameya/ICSE2020Data/ClassTypeMigrationRepetitiveness.svg")
renderPDF.drawToFile(figure, "/Users/ameya/ICSE2020Data/ClassTypeMigrationRepetitiveness.pdf")


plt.show()

