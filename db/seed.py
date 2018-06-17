#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import time

time.sleep(20)

df = pd.read_csv('/db/FL_insurance_sample.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@postgres:5432/dataset')

exists = engine.dialect.has_table(engine, 'insurance')
if not exists:
    df.to_sql("insurance", con=engine, index=False)
    with engine.connect() as con:
        con.execute('ALTER TABLE insurance ADD PRIMARY KEY (policyID);')