import pandas as pd
import numpy as np
import seaborn.objects as so


def summary_statistics(df, x):
    summary_stats = df[x].describe()
    return summary_stats


def log_func(df, x):
    if x[0:3] == "log" or x[0:3] == "Log":
        df[x] = np.log(df[x[4:]])
    if x[0:2] == "ln" or x[0:2] == "ln":
        df[x] = np.log(df[x[3:]])
    return df


def scatter_plot(df, x, y, title, plot="plot.png"):
    my_chart = (
        so.Plot(
            df,
            x=x,
            y=y,
        )
        .add(so.Line(), so.PolyFit(order=2))
        .add(so.Dot())
        .label(title=title)
    )
    return my_chart.save("images/" + plot)


def generate_general_markdown(df, x, y):
    """generate an md file with outputs"""
    markdown_table1 = summary_statistics(df, x)
    markdown_table2 = summary_statistics(df, y)
    markdown_table1 = str(markdown_table1)
    markdown_table2 = str(markdown_table2)

    # Write the markdown table to a file
    with open("Data_summary.md", "w", encoding="utf-8") as file:
        file.write(f"Describe {x}:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write(f"Describe {y}:\n")
        file.write(markdown_table2)
        file.write("\n\n")  # Add a new line
        file.write("![scatter_plot](images/plot.png)\n")


# x = "GDP per capita (constant 2010 US$)"
# y = "Mortality rate, infant (per 1,000 live births)"
# title = "Log GDP and Under-5 Mortality"

# print(df[x])
# summary_statistics(df, x)
# df = log_func(df, x)
# scatter_plot(df, "log " + x, y, title)
