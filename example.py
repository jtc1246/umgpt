from openai import AzureOpenAI
import json


client = AzureOpenAI(
    api_key='xxxx',  # 改成你的 api key
    api_version='2023-05-15',
    azure_endpoint='https://api.umgpt.umich.edu/azure-openai-api-unlimited',
    organization='001145'
)

response = client.chat.completions.create(
    model='gpt-35-turbo',
    # model='gpt-4',
    # 这里需要注意，model 只能是 'gpt-35-turbo' 或 'gpt-4'，别的 (比如gpt-4-torbo gpt-3.5-torbo) 都不行
    temperature=0.6,  # temperature 是可选的
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": 'what is 2*3'},
    ])
result = response.choices[0].message.content

print(result)  # 输出结果

# 查看使用量
usage = json.loads(response.json())['usage']
print(usage)  # {'completion_tokens': 13, 'prompt_tokens': 23, 'total_tokens': 36}
