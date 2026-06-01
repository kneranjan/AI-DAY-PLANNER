from google import genai
from google.genai import types

client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash-lite")


def organise_tasks(raw_input):
  #Set up system isntructions rules 
  config_setup = types.GenerateContentConfig(
    system_instruction=f"""
    You are an expert AI day planner and productivity coach. 
    Analyze the following messy task input, clean it up, and organize it into a logically sequenced schedule.
    
    RULES (do no break them):
    1. Do NOT just copy-paste the user's order. Re-order the tasks based on logical priority (e.g., health, medical, and urgent deadlines come FIRST; leisure, games, and hobbies come LAST).
    2. Add a realistic estimated duration to each task if the user didn't provide one (e.g., "Visit the doctor - 1 hour").
    3. Only the same line give the reasoning, on what basis you decided to order them
    
    You MUST respond ONLY with a JSON array of objects. Do not include markdown formatting or ```json blocks.
    Each object in the array must have exactly this key: "task_name".
    
    """
  )
  #make call to api
  response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = raw_input,
    config = config_setup
  )

  return response.text

if __name__ == "__main__":
    raw_input = "buy milk tonight, need to finish assignment by 2pm, gym at 6am, study for quiz" 

    print(organise_tasks(raw_input))