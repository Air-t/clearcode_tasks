# Web Crawler & CSV Report

Web Crawler - an script to map all possible URL's of a given domain. Returns a dictionary with all
possible links within each possible subdomain.
CSV Report - an script to import csv file, process and output as csv format file, a specific data.


## Installation

Setup virtual envirnoment [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

Use at least Python 3.6.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all necessary libraries.

```bash
pip install -r requirements.txt
```

## Web Crawler Usage

```python
from crawler import site_map

site_map('https://hackaday.com') # return dictionary of available site links

```

## CSV Report Usage

```python
from csv_processing import convert_csv_data

convert_csv_data('input.csv', 'output.csv') # imports csv file, outputs processed data and saves it in output.csv file.

```

Look at input.csv and output.csv file to see how script handles data.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Author

Air-t
