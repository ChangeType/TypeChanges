import pandas as pd
import matplotlib as matplt
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.lines import Line2D
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import scipy.stats as stats
import math
import scikit_posthocs as posthocs

pr = pd.read_csv("/Users/ameya/ICSE2020Data/ProjectMigration.csv")
pck = pd.read_csv("/Users/ameya/ICSE2020Data/PackageMigration.csv")
c = pd.read_csv("/Users/ameya/ICSE2020Data/ClassMigration.csv")
s = pd.read_csv("/Users/ameya/ICSE2020Data/SelectiveMigration.csv")
# m = pd.read_csv("/Users/ameya/ICSE2020Data/MigrationMigration.csv")
# nr = pd.read_csv("/Users/ameya/NoRelationship.csv")
# plt.figure(figsize=(11,2))
sns.set(font_scale=1.5)

print("PRmax" , pr.iloc[:,0].median(), pr.iloc[:,0].mean())
print("Pckgmax", pck.iloc[:,0].median(), pck.iloc[:,0].mean())
print("Clsmax" , c.iloc[:,0].median(), c.iloc[:,0].mean())
# print("MMean", m.median(), m.mean())
print("Smean", s.iloc[:,0].median(), s.iloc[:,0].mean())

print(c.values.shape)

ii = np.concatenate([c.values,pr.values], axis = 0)


print(stats.kruskal(pr.iloc[:,0],pck.iloc[:,0],c.iloc[:,0],s.iloc[:,0]))
f = posthocs.posthoc_dunn([pr.iloc[:,0],c.iloc[:,0],s.iloc[:,0],pck.iloc[:,0]])
# f.compare_dunn(0,1)

print(f.shape)
print(f.values)

print("Project-Package",stats.mannwhitneyu(pr.iloc[:,0], pck.iloc[:,0], alternative='greater'))
print("Project-class",stats.mannwhitneyu(pr.iloc[:,0], c.iloc[:,0], alternative='greater'))
print("project-selective",stats.mannwhitneyu(pr.iloc[:,0], s.iloc[:,0], alternative='greater'))
print("package-selective",stats.mannwhitneyu(pck.iloc[:,0], s.iloc[:,0], alternative='greater'))
print("class-selective",stats.mannwhitneyu(s.iloc[:,0], c.iloc[:,0], alternative='greater'))


extra_tics = [math.log10(pr.median()),math.log10(pck.median()),math.log10(c.median()), math.log10(s.median())]

custom_lines = [Line2D([0], [0], color= 'r', lw=4),
                Line2D([0], [0], color='g', lw=4)]

fig, axes = plt.subplots(figsize=(10,4))
axes.set_yscale('log')
#, sns.color_pallete("muted")''
# c.iloc[:,0] + pck.iloc[:,0] + pr.iloc[:,0]
#
r = axes.violinplot(dataset=[c.iloc[:,0] , pck.iloc[:,0] , pr.iloc[:,0], s.iloc[:,0] ], showmedians=True, showmeans=True)
r['cmeans'].set_color('r')
r['cmedians'].set_color('g')
# for

print(type((axes.get_yticks()[0])))
print(axes.get_yticks().shape)
z = np.append(extra_tics,axes.get_yticks()[0])
print(type(z))
labels = ['Class','Package', 'Project', 'Selective']
axes.set_xticks(np.arange(1, len(labels) + 1))
axes.set_xticklabels(labels)
axes.set_xlabel('Scope', fontweight='bold')
axes.set_ylabel('No of Changes', fontweight='bold')
axes.add_collection(r['cmedians'])

plt.text(0.9,1,"MDN:1",fontsize=16)
plt.text(1.9,3,"MDN:3", fontsize = 16)
plt.text(2.9,5,"MDN: 5", fontsize=16)
plt.text(3.9,2,"MDN: 2", fontsize = 16 )
plt.text(0.9,1.5,"M:1.5",fontsize=16)
plt.text(1.9,6.1,"M:6.1", fontsize = 16)
plt.text(2.9,12.5,"M: 12.5", fontsize=16)
plt.text(3.9,4.5,"M: 4.5 ", fontsize = 16 )


# plt.plot([nr.mean(), nr.mean()], [0,4], linestyle = "dotted", color="black")
#
# sns.barplot(x="Relationship",y="Frequency", data= pd.DataFrame([["Composition", 10], ["Hierarchy",20], ["No Relationship Inferred",30]],
#                                                                columns=["Relationship","Frequency"]), palette="gray")
plt.tight_layout()
plt.savefig("/Users/ameya/ICSE2020Data/NoOfTypeChangesMigration.pdf", format="pdf", dpi=300,bbox_inches='tight')

# figure = svg2rlg("/Users/ameya/ICSE2020Data/HierarchyVsComposition.svg")
# renderPDF.drawToFile(figure, "/Users/ameya/ICSE2020Data/HierarchyVsComposition.pdf")

#h_a = plt.dist(h.to_numpy().flatten())
#h_m = h_a[1]
#h_f = h_a[0]
#c_a= plt.dist(c.to_numpy().flatten())
#c_m, c_f = c_a[1], c_a[0]
