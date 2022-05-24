"""This module contains exercise DE Intro Task"""
import os

import boto3
from botocore.client import Config
from sqlalchemy import create_engine

from intro import intro  # pylint: disable=E0401 (import-error)


def db_connect():
    """This function return connect ot database"""
    password = os.environ['POSTGRES_PASSWORD']
    return create_engine(f'postgresql://postgres:{password}@database:5432/postgres').connect()


def s3_connect():
    """This function return connect ot s3"""
    return boto3.resource(
        's3',
        endpoint_url='http://s3:9000',
        aws_access_key_id=os.environ['MINIO_ROOT_USER'],
        aws_secret_access_key=os.environ['MINIO_ROOT_PASSWORD'],
        config=Config(signature_version='s3v4'),
        region_name='us-west-1'
    )


def main():
    """This function run exercise DE Intro Task"""
    data_frame = intro(s3_connect(), 'intro_bucket')
    data_frame.to_sql('covid_italy', con=db_connect(), if_exists='replace', index=False)


if __name__ == '__main__':
    main()
