#prob.py
import collections
import scipy.stats as stats
import matplotlib.pyplot as plt

def freq_calc(data):
    tally = collections.Counter(data)
    for k,v in tally.iteritems():
        print "The frequency of {number} in the data set is {freq}".format(number = k, freq = float(v) / len(data))

def gen_plots(data_name, data):
    plt.figure()
    plt.boxplot(data)
    plt.savefig("{0}_boxplot.png".format(data_name))
    plt.figure()
    plt.hist(data)
    plt.savefig("{0}_histogram.png".format(data_name))
    plt.figure()
    qqplot = stats.probplot(data, dist = "norm", plot = plt)
    plt.savefig("{0}_qqplot.png".format(data_name))

def main():
    testlist = [1, 4, 5, 6, 9, 9, 9]
    box_data = x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
    data_dict = {"testlist":testlist, "box_data":box_data}
    for data_name in data_dict.keys():
        freq_calc(data_dict[data_name])
        gen_plots(data_name, data_dict[data_name])

main()