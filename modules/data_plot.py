import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def hist_box_plot(dataset, var_name):
    '''histogram and boxplot for some dataset with any numerical variable'''
    plt.figure(figsize = (12,8))
    plt.subplot(121)
    sns.histplot(x = var_name, data = dataset, bins = 100)
    plt.subplot(122)
    sns.boxplot(y = var_name, data = dataset)
    plt.show()