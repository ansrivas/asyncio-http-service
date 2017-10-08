# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Model to store todos."""


# Todos = sa.Table(
#     'todos', meta,
#     sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
#     sa.Column('created_timestamp', AwareDateTime(), default=tzware_datetime()),
#     sa.Column('modified_timestamp', AwareDateTime(), default=tzware_datetime()),
#
#     sa.Column('notes', sa.String, nullable=False, default=""),
#     sa.Column('status', sa.Boolean, nullable=False, default=False),
#
#     sa.Column('user_id', sa.Integer, ForeignKey('users.id'), index=True),
#     sa.ForeignKeyConstraint(['user_id'], [Users.c.id],
#                             name='user_id_fkey',
#                             ondelete='CASCADE'),
#
#     sa.CheckConstraint('status > 0', name='status_greater_than_0'),
#     sa.CheckConstraint('status < 4', name='status_less_than_4'),
#     sa.CheckConstraint('start_timestamp <  end_timestamp', name='start_less_than_end'),
#
# )

todos_creation = '''CREATE TABLE IF NOT EXISTS todos (
                            id serial PRIMARY KEY NOT NULL,
                            created_timestamp timestamp with time zone NOT NULL,
                            modified_timestamp timestamp with time zone NOT NULL,
                            notes text NOT NULL,
                            completed bool NOT NULL DEFAULT(False),
                            users_id int references users(id) on delete cascade,
                            status int NOT NULL)'''

todos_index_creation = '''CREATE UNIQUE INDEX ix_users_id on todos(users_id)'''


todos_deletion = '''DROP TABLE todos'''

todos_index_deletion = '''DROP INDEX public.ix_users_id'''
