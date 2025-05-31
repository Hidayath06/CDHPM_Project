import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")        #setting up api

import base64
image_path="rashes.jpg"
image_file=open(image_path,"rb")                                            #conversion of image into reqiured format
encoded_image=base64.b64encode(image_file.read()).decode('utf-8')

from groq import Groq
client=Groq()
print("Provide your query below")
query=input()
model="meta-llama/llama-4-scout-17b-16e-instruct"
messages = [
    {
        "role":"user",
        "content": [
            {                                                                               #setting up multimodal LLM
                "type":"text",
                "text": query
            },
            {
                "type":"image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                },
            },
        ],
    }
]
chat_completion = client.chat.completions.create(
    messages=messages,
    model=model
)

print(chat_completion.choices[0].message.content)



