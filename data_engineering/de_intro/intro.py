"""This module contains execution exercise DE Intro Task"""
import pandas as pd
from pandas.core.frame import DataFrame


def get_csv_files(s3_connect, bucket_name: str):
    """This function return generator read csv files in the bucket"""
    bucket = s3_connect.Bucket(bucket_name)
    return (pd.read_csv(s3_object.get()['Body']) for s3_object in bucket.objects.all())


def concatenated_df(s3_connect, bucket_name: str) -> DataFrame:
    """This function return concatenate each csv file in folder"""
    return pd.concat(get_csv_files(s3_connect, bucket_name), ignore_index=True)


def rename_columns_df(data_frame):
    """This function rename data frame column"""
    data_frame.rename(
        columns={
            'data': 'date',
            'stato': 'state',
            'codice_regione': 'code_region',
            'denominazione_regione': 'denomination_region',
            'codice_provincia': 'code_province',
            'denominazione_provincia': 'denomination_province',
            'sigla_provincia': 'initials_province',
            'totale_casi': 'total_cases',
            'codice_nuts_1': 'code_nuts_1',
            'codice_nuts_2': 'code_nuts_2',
            'codice_nuts_3': 'code_nuts_3'
        },
        inplace=True
    )


def change_type(data_frame):
    """This function change type data frame column"""
    data_frame['date'] = pd.to_datetime(data_frame['date'], format='%Y-%m-%d %H:%M:%S')


def intro(s3_connect, bucket_name: str) -> DataFrame:
    """This function contains execution exercise DE Intro Task and return corrected data frame"""
    data_frame = concatenated_df(s3_connect, bucket_name)
    rename_columns_df(data_frame)
    change_type(data_frame)
    return data_frame
