import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.lines import Line2D
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import scipy.stats as stats
import scikit_posthocs as posthocs


h = pd.read_csv("/Users/ameya/ICSE2020Data/Hierarchy.csv")
cd = pd.read_csv("/Users/ameya/ICSE2020Data/CommonSuperType.csv")
c = pd.read_csv("/Users/ameya/ICSE2020Data/Composition.csv")
# nr = pd.read_csv("/Users/ameya/NoRelationship.csv")
# plt.figure(figsize=(11,2))

h_c = stats.ranksums(h.iloc[:,0], c.iloc[:,0])#,alternative='less')
h_cd = stats.ranksums(h.iloc[:,0], cd.iloc[:,0])#,alternative='less')
c_cd = stats.ranksums(cd.iloc[:,0], c.iloc[:,0])#,alternative='less')
print("p value for hierarchy and composition", h_c)
print("p value for hierarchy and common st", h_cd)
print("p value for common st and composition", c_cd)

print(stats.f_oneway(h.iloc[:,0], cd.iloc[:,0], c.iloc[:,0]))

f = (stats.kruskal(h.iloc[:,0],cd.iloc[:,0],c.iloc[:,0]))
f1 = posthocs.posthoc_dunn([h.iloc[:,0],c.iloc[:,0],cd.iloc[:,0]])

print("H: " , h.iloc[:,0].mean(),h.iloc[:,0].median())
print("CD: " , cd.iloc[:,0].mean(),cd.iloc[:,0].median())
print("C: " , c.iloc[:,0].mean(),c.iloc[:,0].median())

sns.set(font_scale=1.5)

fig, axes = plt.subplots(figsize=(8, 3))

#, sns.color_pallete("muted")
r = axes.violinplot(dataset=[h.iloc[:,0],cd.iloc[:,0],c.iloc[:,0]], showmeans=True, showmedians=True)
r['cmeans'].set_color('r')
r['cmedians'].set_color('g')
# axes.legend(custom_lines, ['Mean', 'Median'])

labels = ['Parent-Child','Sibling', 'Composition']
axes.set_xticks(np.arange(1, len(labels) + 1))
axes.set_xticklabels(labels)
axes.set_xlabel('Relationship', fontweight='bold')
axes.set_ylabel('Adaptation Complexity', fontweight='bold')

plt.text(0.9,0.25,"M:0.25",fontsize=16)
plt.text(1.9,0.35,"M: 0.35", fontsize = 16)
plt.text(2.9,0.4,"M: 0.4", fontsize=16)
# plt.text(3.9,4.5,"M:4.5 ", fontsize = 16 )

# plt.plot([nr.mean(), nr.mean()], [0,4], linestyle = "dotted", color="black")
#
# sns.barplot(x="Relationship",y="Frequency", data= pd.DataFrame([["Composition", 10], ["Hierarchy",20], ["No Relationship Inferred",30]],
#                                                                columns=["Relationship","Frequency"]), palette="gray")
# plt.tight_layout()
plt.savefig("/Users/ameya/ICSE2020Data/ParentSiblingCompose.pdf", format="pdf", dpi=300,bbox_inches='tight')

# figure = svg2rlg("/Users/ameya/ICSE2020Data/HierarchyVsComposition.svg")
# renderPDF.drawToFile(figure, "/Users/ameya/ICSE2020Data/HierarchyVsComposition.pdf")

#h_a = plt.dist(h.to_numpy().flatten())
#h_m = h_a[1]
#h_f = h_a[0]
#c_a= plt.dist(c.to_numpy().flatten())
#c_m, c_f = c_a[1], c_a[0]
