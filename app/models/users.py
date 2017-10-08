# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model to store users."""

# Users = sa.Table(
#     'users', meta,
#     sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
#     sa.Column('created_timestamp', AwareDateTime(), default=tzware_datetime()),
#     sa.Column('modified_timestamp', AwareDateTime(), default=tzware_datetime()),
#     sa.Column('email_address', sa.String(255), nullable=False, unique=True, index=True),
# )


users_creation = '''CREATE TABLE IF NOT EXISTS users (
                            id serial PRIMARY KEY NOT NULL,
                            created_timestamp timestamp with time zone NOT NULL,
                            modified_timestamp timestamp with time zone NOT NULL,
                            email_address text NOT NULL)'''

users_index_creation = '''CREATE UNIQUE INDEX ix_email_address on users(email_address)'''

users_deletion = '''DROP TABLE users CASCADE'''

users_index_deletion = '''DROP INDEX public.ix_email_address'''
