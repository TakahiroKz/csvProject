import matplotlib.pyplot as plt

def generate_bar_chart(labels, values,country=""):
    fig , ax =plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f"./recursos/{country}BarChart.jpg")

def generate_pi_chart(labels,values,country=""):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig(f"./recursos/{country}PieChart.jpg")



if __name__ == '__main__':

    labels = ['A','B','C']
    values = [100,200,300]
    generate_bar_chart(labels, values)
    generate_pi_chart(labels,values)

