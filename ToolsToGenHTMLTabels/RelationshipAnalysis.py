import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from matplotlib.figure import figaspect

h = pd.read_csv("/Users/ameya/ICSE2020Data/Hierarchy.csv")
cd = pd.read_csv("/Users/ameya/ICSE2020Data/CommonSuperType.csv")

c = pd.read_csv("/Users/ameya/ICSE2020Data/Composition.csv")
nr = pd.read_csv("/Users/ameya/ICSE2020Data/NoRelationship.csv")

hh = h.iloc[:,0] +cd.iloc[:,0]
print(type(hh))
plt.figure(figsize=(9,3))
sns.set(font_scale=1.5)
b = sns.barplot(x="Relationship",y="Occurences", data= pd.DataFrame([["Composition", 11205], ["Hierarchy",28379+5694], ["No Relationship",265046]],
                                                               columns=["Relationship","Occurences"]), palette="Blues")

for p in b.patches:
    _x = p.get_x() + p.get_width() / 2
    _y = p.get_y() + p.get_height()
    value = int(p.get_height())
    b.text(_x, _y, value, ha="center")

b.set_xlabel("Relationship", fontweight='bold')
b.set_ylabel("Occurences",fontweight='bold')
plt.tight_layout()
plt.savefig("/Users/ameya/ICSE2020Data/Relationships.svg", format="svg", dpi=300,bbox_inches='tight')

figure = svg2rlg("/Users/ameya/ICSE2020Data/Relationships.svg")
renderPDF.drawToFile(figure, "/Users/ameya/ICSE2020Data/Relationships.pdf")
plt.show()


