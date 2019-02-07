import datetime
import pycountry
import pandas as pd


def assign_country(subdivision_name, subdivision_list, countries_list):
    '''
    ISO 3166-2 subivision to ISO ALPHA-3 country abbreviation.

    :param subdivision_name: subdivision name to be translated
    :param subdivision_list: pycountry.Subdivision list
    :param countries_list: pycountry.Country list
    :return: ALPHA-3 string
    '''

    # todo decrease number of operations in future
    for item in subdivision_list:
        if subdivision_name == item.name:
            for country in countries_list:
                if item.country_code == country.alpha_2:
                    return country.alpha_3
    return 'XXX'


def convert_csv_data(file_path='input.csv', output_path='output.csv'):
    '''
    Parses csv format file into DataFrame object.
    UTF-8 and UTF-16 encoding allowed.
    Perform data conversion.
    Save converted data to CSV fF-8 encoding.

    :param file_path: Relative or absolute input file path. Default='input.csv'
    :param output_path: Output file path. Default='output.csv'
    :return: None
    '''

    # temporary DataFrame headers
    headers = ['DATE', 'ALPHA-3', 'NOI', 'CTR']

    try:
        data = pd.read_csv(filepath_or_buffer=file_path,
                           encoding='utf-16', names=headers)
    except UnicodeError as e:
        print(e)
        data = pd.read_csv(filepath_or_buffer=file_path,
                           encoding='utf-8', names=headers)
    except Exception:
        print("Fail to load file.")
        raise Exception

    # ISO 3166-2 to ALPHA-2 country list
    countries = pycountry.countries
    subdivisions = list(pycountry.subdivisions)

    # convert datetime
    try:
        for i in range(len(data)):
            data.loc[i, 'DATE'] = datetime.datetime.strptime(data.loc[i, 'DATE'], '%m/%d/%Y').date()
    except Exception as e:
        print(f"While parsing {data.loc[i, 'DATE']} @ line {i}, an exception has occurred:")
        print(e)

    # todo how to avoid chain indexing. why it is wrong. DONE
    # todo how to read encoding
    # convert CTR
    try:
        for i in range(len(data)):
            data.loc[i, 'CTR'] = int(round((eval(data.loc[i, 'CTR'].rstrip('%')) / 100) * data.loc[i, 'NOI']))
    except Exception as e:
        print(f"While parsing {data.loc[i, 'CTR']} @ line {i}, an exception has occurred:")
        print(e)

    # convert ISO 3166-2 to ISO ALPHA-3
    for i in range(len(data)):
        data.loc[i, 'ALPHA-3'] = assign_country(data.loc[i, 'ALPHA-3'], subdivision_list=subdivisions, countries_list=countries)

    data = data.groupby(['DATE', 'ALPHA-3']).agg({'NOI': 'sum', 'CTR': 'sum'}).reset_index()

    # save output data .csv file
    data.to_csv(path_or_buf='output.csv',
                encoding='utf-8',
                header=False,
                index=False)

    return data


if __name__ == '__main__':
    convert_csv_data()


