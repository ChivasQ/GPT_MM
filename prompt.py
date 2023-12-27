import g4f

def ask_gpt(promt:str)->str:
  responce = g4f.ChatCompletion.create(
    provider=g4f.Provider.Bing,
    model=g4f.models.gpt_35_turbo,
    messages=[{"role": "user", "content": promt}]
  )
  with open('test.txt', 'w', encoding="utf-8") as file:
    file.write(responce)
    file.close()
  return responce

