#impoort
import json
import datetime
from AI_day_planner.ai_helper import organise_tasks
from database import save_tasks, create_table , get_today_tasks , mark_complete

create_table()

def main():
  while True:
    print("---------AI DAY PLANNER---------")
    print("Welcome")
    print("1. Plan my day")
    print("2. View today's tasks")
    print("3. Mark task complete")
    print("4. Exit")
    print("===========================")

    choice = input("Choose an option (1-4): ").strip()
    #user i/p
    if choice == '1':
      user_tasks = input("Enter Your Tasks (separated by a ','): ")
      print("Processing With AI...")
      #call organsise task func
      clean_schedule = organise_tasks(user_tasks)
      #print it out by conv propely in json
      print("\nYour organized schedule is:")
      try:
          tasks_list = json.loads(clean_schedule)
          # enumerate to start at 1
          for index, item in enumerate(tasks_list, 1):
              print(f"{index}. {item['task_name']}")
      except Exception as e:
          print("Raw Output:", clean_schedule)
      print("--------------------------------")
      #ask user to save/delete
      save_prompt = input("To save: enter Y  |  To Delete: enter D: ")
      save_prompt = save_prompt.lower().strip()
      
      if save_prompt == 'y':
          current_date = str(datetime.date.today())
          
          try:
              tasks_list = json.loads(clean_schedule)
              formatted_data = []
              for item in tasks_list:
                  formatted_data.append((item['task_name'], current_date, 'N'))
              
              save_tasks(formatted_data)
              print(f"Successfully saved {len(formatted_data)} separate tasks to the db!\n")
              
          except Exception as e:
              print("Errorrororoororororo")
              formatted_data = [(clean_schedule, current_date, 'N')]
              save_tasks(formatted_data)
      else:
          print("Deleting schedule")
    elif choice == '2':
       print("--------Here are today's tasks:--------\n")
       today_tasks = get_today_tasks()
       if not today_tasks:
           print("No tasks added/remaining for today")
           print("You can add tasks by selecting option 1")
       else:
           for row in today_tasks:
               #(id,task_name,date,completed)
               task_id = row[0]
               task_name = row[1]
               completed_status = row[3]

               print(f"{task_id}.  {task_name}   {completed_status}")
               print("\n")    

    elif choice == '3':
       print("MARK TASK AS COMPLETE ?")
       today_tasks = get_today_tasks()
       if not today_tasks:
           print("No tasks added to mark them complete")
           print("You can add tasks by selecting option 1")
       else:
           for row in today_tasks:
               task_name = str(row[1]).strip("{}'")
               print(f"{row[0]}. {task_name}")
               print("-------------")
           try:
              complete_id = int(input("Enter the id of the task to mark complete:  "))
              mark_complete(complete_id) 
              print(f"[Success] Task ID {complete_id} marked as complete!")
           except ValueError:
               print("Invalid input.Enter the numerical id of the task You want to mark as complete")
               print("-------------")   

    elif choice == '4':
            print("\nThank you for using AI Day Planner. Goodbye!")
            break

    else:
            print("\nInvalid option! Please enter a number from 1 to 4.")    

if __name__ == "__main__":
    main() 
