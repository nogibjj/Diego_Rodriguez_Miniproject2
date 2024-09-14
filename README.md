[![CI](https://github.com/nogibjj/Diego_Rodriguez_Miniproject1/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/Diego_Rodriguez_Miniproject1/actions/workflows/hello.yml)

# IDS706-Week2
## File Structure 
```
Diego_Rodriguez_Miniproject2/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   ├── workflows/hello.yml
|   ├── workflows/format.yml
|   ├── workflows/lint.yml
|   └── workflows/test.yml
├── Images/
│   ├── plot.png
|   └── test_plot.pmg
├── mylib/
|   └── lib.py
├── .gitignore
├── Data_summary.md
├── main.ipynb
├── main.py
├── Makefile
├── README.md
├── requirements.txt
├── test_lib.py
├── test_main.py
└── test.csv
```

## Purpose of project
The purpose of this project is to present some transformation of data using Pandas and automating the publishing process into Data_summary.md. 


## Visualizations
Here is a scatter plot:

![scatter_plot](images/plot.png)

Plot result can be found under Images folder and a complete summary of the information under Data_summary.md.

## Some summary statistics:
Describe GDP per capita (constant 2010 US$):
|statistics | value |
| -------- | ------------ |   
|count       | 198.000000 |
|mean      | 15335.724729 |
|std       | 22881.307340 |
|min         | 228.432544 |
|25%        | 1844.387439 |
|50%        | 6134.939066 |
|75%       | 17654.996438 |
|max      | 189464.583635 |

Describe Mortality rate, infant (per 1,000 live births):
| Statistics | Value |
| ----- | ----- |
| count | 193.00 |
| mean | 23.40 |
| std | 21.06 |
| min | 1.70 |
| 25% | 6.50 |
| 50% | 15.50 |
| 75% | 35.10 |
| max | 91.60 |

## Requirements
devops
black ==22.3.0 - Formatter
click == 8.1.3
pytest == 7.4.0  - For Testing
pytest-cov == 4.0.0 - For Testing
nbval==0.10.0 - For Testing

rust based linter
ruff==0.0.284
boto3==1.24.87

web
fastapi == 0.85.0
uvicorn == 0.18.3

Python libraries
pandas == 2.2.2
numpy == 2.1.0
seaborn == 0.13.2
jupyter == 1.0.0  
tabulate==0.9.0

## CI/CD
Testing files go with the name test_*

