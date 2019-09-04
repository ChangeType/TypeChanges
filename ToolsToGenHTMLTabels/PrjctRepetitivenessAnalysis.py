import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


pr = pd.read_csv("/Users/ameya/ICSE2020Data/ProjecttypeChangesForTypeMigrationPerCommit.csv")

plt.figure(figsize=(10,3))
sns.set(font_scale=1.5)
g = sns.violinplot(pr)

plt.tight_layout()
plt.savefig("/Users/ameya/ICSE2020Data/PackageTypeMigrationRepetitiveness.svg", format="svg", dpi=300,bbox_inches='tight')


figure = svg2rlg("/Users/ameya/ICSE2020Data/PackageTypeMigrationRepetitiveness.svg")
renderPDF.drawToFile(figure, "/Users/ameya/ICSE2020Data/PackageTypeMigrationRepetitiveness.pdf")

plt.show()

