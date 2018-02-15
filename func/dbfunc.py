#-*- coding:utf-8 -*-
import os, errno
import sys
from func.yamlfunc import Yamlfunc
import pymysql.cursors

class DBfunc:
    def __init__(self):
        pass

    def initDB(self):
        yaml = Yamlfunc()
        conn = pymysql.connect(host=yaml.settings['host_MySQL'],
        user=yaml.settings['id_MySQL'],
        password=yaml.settings['pw_MySQL'],
        db=yaml.settings['db_MySQL'],
        charset='utf8mb4')
        return conn

    def get_status(self):
        conn = self.initDB()
        try:
            with conn.cursor() as cursor:
                sql = 'SELECT * FROM users'
                cursor.execute(sql)
                result = cursor.fetchall()
                #print(result)
        except Exception as e:
            print('I got error on search table')
            conn.close()
        conn.close()
        return result
    
    def set_user(self, tele_id, user_name):
        conn = self.initDB()
        try:
            with conn.cursor() as cursor:
                sql = 'INSERT INTO users (user_tele_id, user_name) VALUES (%s, %s)'
                cursor.execute(sql, (tele_id, user_name))
            conn.commit()
            print('I successed on inserting ID')
        except Exception as e:
            print('I got error on inserting ID')
            print(e)
            conn.close()
            return 0
        conn.close()
        return 1

    def update_user(self, tele_id, user_name):
        conn = self.initDB()
        try:
            with conn.cursor() as cursor:
                sql = 'UPDATE users SET user_name = %s WHERE user_tele_id = %s'
                cursor.execute(sql, (user_name, tele_id))
            conn.commit()
            print('I successed on updating ID')
        except Exception as e:
            print('I got error on updating ID')
            print(e)
            conn.close()
        conn.close()

# got tags list
    def update_tags(self, tele_id, tags):
        conn = self.initDB()
        try:
            with conn.cursor() as cursor:
                sql = 'UPDATE users SET user_tag1 = %s, user_tag2 = %s, user_tag3 = %s WHERE user_tele_id = %s'
                cursor.execute(sql, (tags[0],tags[1],tags[2],tele_id))
            conn.commit()
            print('I successed on updating tags')
        except Exception as e:
            print('I got error on updating tags')
            print(e)
            conn.close()
        conn.close()

    def update_users(self, tele_id, users):
        conn = self.initDB()
        try:
            with conn.cursor() as cursor:
                sql = 'UPDATE users SET target_user1 = %s, target_user2 = %s, target_user3 = %s, target_user4 = %s, target_user5 = %s WHERE user_tele_id = %s'
                cursor.execute(sql, (users[0],users[1],users[2],users[3],users[4],tele_id))
            conn.commit()
            print('I successed on updating tags')
        except Exception as e:
            print('I got error on updating tags')
            print(e)
            conn.close()
        conn.close()