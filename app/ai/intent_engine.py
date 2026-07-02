import ollama
SYSTEM_PROMPT='Return only JSON with intent,key,value.'
def detect(message):
 return ollama.chat(model='qwen3:4b',messages=[{'role':'system','content':SYSTEM_PROMPT},{'role':'user','content':message}])['message']['content']
