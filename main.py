import openai
from openai import OpenAI
from dotenv import load_dotenv

import time
import random

from argparse import Namespace
import os
import requests


# Replace 'YOUR_VIDEO_ID' with the ID of the YouTube video you want to download subtitles for
webpage_url = input("请输入你要生成web网页问题的地址: e.g.")
question_num=input("要生成的问题的个数:")
question_language=input("生成的问题的语言: 中文，English, etc. ")




# 在使用API密钥和基础URL之前加载.env文件
load_dotenv()

# 现在可以通过os.environ访问这些值
API_BASE = os.environ.get("API_BASE")
API_KEY = os.environ.get("API_KEY")

    
client = openai.OpenAI(api_key=API_KEY, base_url=API_BASE)

reader_url = f"https://r.jina.ai/{webpage_url}"
json_response = requests.get(reader_url, headers={"Accept": "application/json"})

if json_response.status_code == 200:
    json_data = json_response.json()
    markdown_content = f"文档名称:{json_data['data']['title']}\n文档原地址:{json_data['data']['url']}\n{json_data['data']['content']}"



completion = client.chat.completions.create(
    model="phi3",
    messages=[{"role": "system", "content":"你是一个QA问答对构建专家，专门根据用户视频的内容构建"+question_num+"个高质量的"+question_language+"问题："},
            {"role":"user","content":"生成"+question_num+"个高质量的问题："+markdown_content+";并每个问题输出显示都要换行"},
            ],
    max_tokens=6000,
    top_p=0.8,
    # stream=True,
)
outputtext=completion.choices[0].message.content
print(outputtext)
with open('questions.txt', 'w', encoding='utf-8') as file:
    file.write(outputtext)

print("输出内容已保存到questions.txt文件中。")
# for chunk in completion:
#     # print(chunk) 
#     print(chunk.choices[0].delta.content or "", end="", flush=True)


# https://www.youtube.com/watch?v=CjTTSa33axg