import scikit_posthocs as sp

y = [0.1581599101, 0.1712449269, 0.1063096112, 0.1492829205, 0.1030595813, 0.1580896686, 0.09545454545, 0.09655172414, 0.14]
y2 = [0.1864842705, 0.2012435943, 0.2011266299, 0.1791651256, 0.2212327902, 0.2368055556, 0.2526984127, 0.2680901857, 0.1928571429]

x = [y, y2]

# https://scikit-posthocs.readthedocs.io/en/latest/generated/scikit_posthocs.posthoc_wilcoxon/

print(sp.posthoc_wilcoxon(x))
print(sp.posthoc_wilcoxon(x, correction=False, p_adjust="bonferroni"))
print(sp.posthoc_wilcoxon(x, correction=False, p_adjust="holm"))
print(sp.posthoc_wilcoxon(x, correction=False, p_adjust="holm-sidak"))

print(type(y))
print(type(y[0]))
print(y[0])


from statsmodels.sandbox.stats.multicomp import multipletests
result = multipletests([.05, 0.3, 0.01], method='bonferroni')
print(result)