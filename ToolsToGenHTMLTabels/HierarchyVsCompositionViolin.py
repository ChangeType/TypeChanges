import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

h = pd.read_csv("/Users/ameya/ICSE2020Data/Hierarchy.csv")
cd = pd.read_csv("/Users/ameya/ICSE2020Data/CommonSuperType.csv")
c = pd.read_csv("/Users/ameya/ICSE2020Data/Composition.csv")
# nr = pd.read_csv("/Users/ameya/NoRelationship.csv")


print(h.shape)
print(c.shape)

plt.figure(figsize=(9.2,4))
sns.set(font_scale=1.5)
#, sns.color_pallete("muted")


g1 = sns.distplot(h, hist=False, rug=False, label = "Parent Child Hierarchy", norm_hist=True, kde = True, color="midnightblue", axlabel="Adaptation Complexity",kde_kws={"linestyle":"solid"})
g3 = sns.distplot(cd, hist=False, rug=False, label = "Sibling Hierarchy", norm_hist=True, kde = True, color="midnightblue", axlabel="Adaptation Complexity",kde_kws={"linestyle":"dotted"})
g1.set(yticks=[])
g1.set_xlabel("Adaptation Complexity", fontweight='bold')
g1.set_ylabel("Density of type changes", fontweight='bold')
g2 = sns.distplot(c, hist=False, rug=False, label ='Composition', norm_hist= True,kde = True,color="midnightblue",kde_kws={"linestyle":"dashed"})
g2.set(yticks=[])
plt.plot([c.mean(), c.mean()], [0, 4], linestyle = "dashed", color="midnightblue")
plt.plot([h.mean(), h.mean()], [0, 4], linestyle = "solid", color="midnightblue")
plt.plot([cd.mean(), cd.mean()], [0, 4], linestyle = "dotted", color="midnightblue")
plt.legend()
plt.xlim(0,1)


# plt.plot([nr.mean(), nr.mean()], [0,4], linestyle = "dotted", color="black")
#
# sns.barplot(x="Relationship",y="Frequency", data= pd.DataFrame([["Composition", 10], ["Hierarchy",20], ["No Relationship Inferred",30]],
#                                                                columns=["Relationship","Frequency"]), palette="gray")
plt.tight_layout()
plt.savefig("/Users/ameya/ICSE2020Data/HierarchyVsComposition.pdf", format="svg", dpi=300,bbox_inches='tight')

# figure = svg2rlg("/Users/ameya/ICSE2020Data/HierarchyVsComposition.svg")
# renderPDF.drawToFile(figure, "/Users/ameya/ICSE2020Data/HierarchyVsComposition.pdf")
plt.show()
#h_a = plt.dist(h.to_numpy().flatten())
#h_m = h_a[1]
#h_f = h_a[0]
#c_a= plt.dist(c.to_numpy().flatten())
#c_m, c_f = c_a[1], c_a[0]
