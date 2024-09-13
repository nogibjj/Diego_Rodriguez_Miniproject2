# test the statistics output with a synthetic dataframe
# test the plot if the route exist. from main import add

import pandas as pd
import numpy as np
import os

from mylib.lib import summary_statistics, log_func, scatter_plot, table_format

file = "test.csv"
y_log = "Log y"
x = "x"
y = "y"
title = "Relationship between x and log(y)"
plot = "test_plot.png"


def test_describe():
    """
    Testing describe function.
    Given that it return a list,
    we are making sure that the order of that list
    is equal to the expected function
    """
    df = pd.read_csv(file)
    sum = summary_statistics(df, x)
    assert sum.iloc[1] == df[x].mean()
    assert sum.iloc[2] == df[x].std()
    assert sum.iloc[3] == df[x].min()
    assert sum.iloc[4] == df[x].quantile(0.25)
    assert sum.iloc[5] == df[x].quantile(0.50)
    assert sum.iloc[6] == df[x].quantile(0.75)
    assert sum.iloc[7] == df[x].max()


def test_log_func():
    """
    Testing that the log function
    is creating a variable using np formula
    """
    df = pd.read_csv(file)
    df = log_func(df, y_log)
    assert (df[y_log] == np.log(df[y_log[4:]])).any()


def test_table_format():
    """Testing that .md formatting is running"""
    assert (
        table_format("Hello Name:")
        == "| Statistics | Value |\n| ----- | ----- |\n| Hello | "
    )


def test_scatter_plot():
    """Testing that the image exist after running"""
    df = pd.read_csv(file)
    df = log_func(df, y_log)
    scatter_plot(df, x, y_log, title, plot)
    assert os.path.isfile("images/test_plot.png")


def test_markdown_file():
    """testing that the markdown is there"""
    assert os.path.isfile("Data_summary.md")


if __name__ == "__main__":
    test_log_func()
    test_describe()
    test_scatter_plot()
    test_markdown_file()
    test_table_format()
