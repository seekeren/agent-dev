from openai import OpenAI

client = OpenAI(
    api_key="sk-90a5a5552b30402fa2375d69a7548306",
    base_url="https://ws-xz8bi38oce1tyn6f.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

response = client.chat.completions.create(model="qwen3.6-flash-2026-04-16", messages=[
    {"role": "system", "content": "你是一个python专家，并且不说废话回答简单"},
    {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},
    {"role": "user", "content": "输出1-10的数字，使用Python代码"}])

print(response.choices[0].message.content)

