 
from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)
                     

completion = client.chat.completions.create(
  model="deepseek-ai/deepseek-r1",
  messages=[{"role":"user","content":"你的名字是小小周，一个聪明、热情、善良的人，后面的对话来自你的朋友。宜昌怎么样？"}],
  temperature=0.6,
  top_p=0.7,
  max_tokens=4096,
  stream=False,
  n=1,
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

