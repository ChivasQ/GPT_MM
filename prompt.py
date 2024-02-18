import json

import g4f

def ask_gpt(promt:str)->str:
  promt = "Create a mindmap on a given topic in json, write only the json itself, each value should have a list: " + promt
  responce = g4f.ChatCompletion.create(
    provider=g4f.Provider.Bing,
    model=g4f.models.gpt_4_turbo,
    messages=[{"role": "user", "content": promt}]
  )

  # json_start_index = responce.find('{')
  # json_end_index = len(responce) - responce[::-1].find('}')
  # print(responce[json_start_index:json_end_index])
  return responce #[json_start_index:json_end_index]

