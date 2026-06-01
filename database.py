#libraraies to be imported
import sqlite3


#function to create a table in the database
def create_table():
  conn = sqlite3.connect('DayPlanner.db')
  cursor = conn.cursor()
  cmd = """CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, task_name TEXT, date INTEGER, completed TEXT)"""
  cursor.execute(cmd)
  conn.commit()
  conn.close()

#function to save tasks in the database
def save_tasks(tasks):
  conn = sqlite3.connect('DayPlanner.db')
  cursor = conn.cursor()
  cmd = """  
  INSERT INTO tasks(task_name, date, completed)
  VALUES
  (?,?,?)
  """
  cursor.executemany(cmd,tasks)
  conn.commit()
  conn.close()





def get_today_tasks():
  conn = sqlite3.connect('DayPlanner.db')
  cursor = conn.cursor()
  cmd = """

  SELECT id,task_name,date,completed
  FROM tasks

  """
  cursor.execute(cmd)
  task_list = cursor.fetchall()
  conn.close()
  return task_list


def mark_complete(id):
  conn = sqlite3.connect('DayPlanner.db')
  cursor = conn.cursor()
  cmd = """
  UPDATE tasks
  SET completed = 'Y'
  WHERE id = ?

  """
  cursor.execute(cmd,(id,))
  conn.commit()
  conn.close()

