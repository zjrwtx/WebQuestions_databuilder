

# 一句话概述：

通过Yi模型或ollama的本地小模型对输入的webpage网页地址的内容合成高质量的questions数据供[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)项目进行sft微调数据合成使用

# 演示视频地址

[通过零一万物的Yi模型或ollama的本地小模型对输入的webpage网页地址的内容合成高质量的questions数据供sft微调项目使用_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1rJ4m1n7CS/?spm_id_from=333.999.0.0)
![](https://cdn.nlark.com/yuque/0/2024/png/22859856/1714052729621-26e11c49-447e-4694-a9f6-7656d7fcd7ad.png#averageHue=%23fed776&clientId=uf7c9d25c-e51d-4&from=paste&height=611&id=u3e3215fc&originHeight=916&originWidth=1908&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=247556&status=done&style=none&taskId=ud7d91d8e-8e3d-4faa-9289-e9fa1998165&title=&width=1272#averageHue=%23fed776&id=EkT1g&originHeight=916&originWidth=1908&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)
![](https://cdn.nlark.com/yuque/0/2024/png/22859856/1714052768380-8c96a6aa-5138-4c9b-af5c-f2947958704d.png#averageHue=%23e6a68a&clientId=uf7c9d25c-e51d-4&from=paste&height=611&id=u91344d52&originHeight=916&originWidth=1908&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=358232&status=done&style=none&taskId=u2ca365e2-57bd-4a72-ab91-e804c4f6aba&title=&width=1272#averageHue=%23e6a68a&id=QT04h&originHeight=916&originWidth=1908&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)



## 使用过程描述：

使用本项目生成指定webpage地址的questions文件——[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)项目读取questions文件——然后基于零一万物模型生成基于视频内容的回答后自我调整——最后将回答保存到answers.json文件。

本项目遵循GPL许可证，欢迎贡献代码或提出改进建议。项目地址：[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)



# 如何运行

1、克隆到本地

```git
git clone https://github.com/zjrwtx/WebQuestions_databuilder.git
```

2、安装依赖

```git
poetry install
```

3、复制.env.example文件为.env 填写大模型的环境变量

4、运行python main.py 如顺利无报错 即可开始填内容生成questions数据了


5、开始在可视化程序上读取questions文件，填写必要内容，利用零一万物大模型生成对应数据answers......详细见[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)项目



# 贡献

欢迎贡献。请先 fork 仓库，然后提交一个 pull request 包含你的更改。



# 联系我



## 微信：

agi_isallyouneed



## 微信公众号：正经人王同学

![](https://cdn.nlark.com/yuque/0/2024/jpeg/22859856/1713801561819-9d19cb9a-1233-4295-ad90-56042bbabd3c.jpeg#averageHue=%23a2a1a0&clientId=u7b5f5d88-e731-4&from=paste&height=172&id=u329dbc86&originHeight=430&originWidth=430&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=40862&status=done&style=none&taskId=u7551bc0b-a19a-4ff7-8b6e-1c0d27b3ae1&title=&width=171.66668701171875#averageHue=%23a2a1a0&id=SjL3U&originHeight=430&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=#averageHue=%23a2a1a0&id=dJonX&originHeight=430&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=#averageHue=%23a2a1a0&id=Wxfkz&originHeight=430&originWidth=430&originalType=binary&ratio=1&rotation=0&showTitle=false&status=done&style=none&title=)



## X（推特)正经人王同学:[https://twitter.com/zjrwtx](https://twitter.com/zjrwtx)



# 许可证

本项目遵循GPL许可证，欢迎贡献代码或提出改进建议。项目地址：[https://github.com/zjrwtx/VideoQA_databuilder](https://github.com/zjrwtx/VideoQA_databuilder)

非商业用途：本项目的所有源代码和相关文档仅限于非商业用途。任何商业用途均被严格禁止。

出处声明：任何个人或实体在修改、分发或使用本项目时，必须清楚地标明本项目的原始来源，并且保留原始作者的版权声明。



# 特别感谢
[零一万物](https://github.com/01-ai/Yi)

[GitHub - jina-ai/reader: Convert any URL to an LLM-friendly input with a simple prefix https://r.jina.ai/](https://github.com/jina-ai/reader)

