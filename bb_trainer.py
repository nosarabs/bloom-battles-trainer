# from groq import Groq # type: ignore
import random
import openai

def choose_option(options):
  # Add "Random" to the options list
  options_with_random = []
  options_with_random = options + ["Random"]

  print('Choose an option:')
  for i, option in enumerate(options_with_random, 1):
    print(f"{i}. {option}")
      
  while True:
      choice = input("Enter the number of your choice: ")
      if choice.isdigit() and 1 <= int(choice) <= len(options_with_random):
          if int(choice) == len(options_with_random):  # "Random" option selected
              random_choice = random.choice(options)
              return random_choice
          else:
              return options_with_random[int(choice) - 1]

def get_random_num(min,max):
   num = random.randint(min,max)
   return num

def get_recipe(method,process,ratio,grams):
  

    prompt = f'''Give me a great {method} coffee recipe for {grams} grams of a {process} with a ratio of 1:{ratio}. 
            Suggest the best grind size for these characteristics and explain why. 
            Also tell me how many clicks in the comandante c40 the suggested grins size will be.
            Suggest the best pouring schedule for these characteristics and explain why.
            Don't give me tips or notes.
            '''
    if method == 'Aeropress':
        prompt = f'{prompt} For Aeropress take into account its maximum capacity of 200 ml, if I need to brew more than this suggest a recipe with bypass.' 


    client = openai.OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key='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'
    )

    # client = Groq(
    #     api_key="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",
    # )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a coffee expert assistant. Provide the best recipe for the characteristics inputed."
            },
            {
                "role": "user",
                "content": prompt
                            
            }
        ],
        # model="gpt-4o",
        # model="llama3-8b-8192",
        model="gemma-7b-it",
    )

    return chat_completion.choices[0].message.content

methods = ['Aeropress','V60','Origami w/ Flat Filter','Origami w/ Cone Filter','Kalita','Plinc']
process = ['Slow Natural', 'Honey', 'Red Honey', 'Washed']

print('Bloom Battles Trainer!')
print('\n')

method = choose_option(methods)
print('\n')
process = choose_option(process)
print('\n')
grams = get_random_num(12,30)
ratio = get_random_num(10,20)

print('Your selection:')
print(method)
print(process)
print(f'{grams}g')
print(f'1:{ratio}')

print('\n')
choice  = input('Suggest a recipe? (y/n): ')
if choice == 'y':
  recipe = get_recipe(method,process,ratio,grams)
  print(recipe)
  print('Get Bloomin!')
else:
   print('Get Bloomin!')
