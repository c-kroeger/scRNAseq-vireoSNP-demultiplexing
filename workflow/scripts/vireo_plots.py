# -*- coding: utf-8 -*-
"""
Visualize Vireo output

@author: kroegerc
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# get sample
#sample = snakemake.wildcards

# load vireo output
data_path = snakemake.input[0]
df_vireo = pd.read_table(data_path)

df_counts = df_vireo["donor_id"].value_counts().rename_axis('donor_id').reset_index(name='counts')
df_counts = df_counts.sort_values(by="donor_id")
df_counts = df_counts.assign(ind = np.arange(len(df_counts["donor_id"])))

# barchart of barcodes per donor
fig, ax = plt.subplots()

hbars = ax.barh(df_counts["ind"],df_counts["counts"], align='center')
ax.set_yticks(df_counts["ind"])
ax.set_yticklabels(df_counts["donor_id"])
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel("#barcodes")
ax.set_title("identified barcodes per donor")
ax.bar_label(hbars)
#plt.show()

plt.savefig(snakemake.output[0], bbox_inches="tight")


# boxplots of variants per barcode per donor
fig, ax = plt.subplots()

n=0
for i in df_counts["donor_id"]:
    tmp = df_vireo[df_vireo["donor_id"]==i]["n_vars"]
    n = n+1
    bp= plt.boxplot(tmp, positions=[n], widths=0.6)

ax.set_xticklabels(df_counts["donor_id"])
ax.set_ylabel("#variants")
ax.set_title("identified variants per barcode")
plt.xticks(rotation=90, ha="center")

plt.savefig(snakemake.output[1], bbox_inches="tight")