from random import random
from operator import add

from pyspark import SparkContext

if __name__ == "__main__":


    #conf = sparkConf = new SparkConf().serAppName("Dupa")
    sc = SparkContext(appName="mypi")

    partitions = 2
    n = 5000000

    def f(_):
        x = random () * 2 - 1
        y = random () * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0
    count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print("\nPi is dupa %f\n" % (4.0 * count /n))

    sc.stop()
