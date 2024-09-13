# test the statistics output with a synthetic dataframe
# test the plot if the route exist. from main import add

import pandas as pd
import numpy as np
import os

from main import summary_statistics, log_func, generate_general_markdown, scatter_plot

file = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
x_log = "Log GDP per capita (constant 2010 US$)"
x = "GDP per capita (constant 2010 US$)"
y = "Mortality rate, infant (per 1,000 live births)"
title = "Log GDP and Under-5 Mortality"


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
    df = log_func(df, x_log)
    assert (df[x_log] == np.log(df[x_log[4:]])).any()


def test_scatter_plot():
    """Testing that the image exist after running"""
    df = pd.read_csv(file)
    df = log_func(df, x_log)
    scatter_plot(df, x_log, y, title)
    assert os.path.isfile("images/plot.png")


def test_markdown_file():
    """testing that the markdown is there"""
    df = pd.read_csv(file)
    generate_general_markdown(df, x, y)
    assert os.path.isfile("Data_summary.md")


if __name__ == "__main__":
    test_log_func()
    test_describe()
    test_scatter_plot()
    test_markdown_file()
