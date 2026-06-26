from openai import OpenAI

client = OpenAI(
    base_url="https://ws-xz8bi38oce1tyn6f.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

response = client.chat.completions.create(model="qwen3.6-flash-2026-04-16", messages=[
    {"role": "system", "content": "你是一个AI助理，说话精简不说废话"},
    {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},
    {"role": "user", "content": "输出1-10的数字，使用Python代码"}]
                                          , stream=True)

for chunk in response:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content,
          end=" ",  # 每一段之间以空格分隔,不加的话是以回车符分隔
          flush=True
          )