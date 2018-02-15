#-*- coding:utf-8 -*-
import os, errno
import sys
from func.yamlfunc import Yamlfunc
import pymysql.cursors
yaml = Yamlfunc()
yaml.settings['host_MySQL']

conn = pymysql.connect(host=yaml.settings['host_MySQL'],
        user=yaml.settings['id_MySQL'],
        password=yaml.settings['pw_MySQL'],
        db=yaml.settings['db_MySQL'],
        charset='utf8mb4')

# select
def getData():
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM users'
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print('I got error on search table')
        pass
def insertData(tele_id, name):
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO users (user_tele_id, user_name) VALUES (%s, %s)'
            cursor.execute(sql, (tele_id, name))
        conn.commit()
        print('I successed on inserting ID')
    except Exception as e:
        print('I got error on inserting ID')
        updateData(tele_id, name)
        pass
def updateData(tele_id, name):
    try:
        with conn.cursor() as cursor:
            sql = 'UPDATE users SET user_name = %s WHERE user_tele_id = %s'
            cursor.execute(sql, (name, tele_id))
        conn.commit()
        print('I successed on updating ID')
    except:
        print('I got error on updating ID')
        pass


getData()
insertData('1234568', 'jjjj')
conn.close()

