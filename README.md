<div align="center">
  
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>


# nonebot_plugin_HttpCat
  
_✨Nonebot猫猫http状态码插件✨_

---
  
<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/ANGJustinl/nonebot_plugin_HttpCat" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_HttpCat">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_HttpCat.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
</a>

---  
 </div> 
  
## 💿 安装

### 1. nb-cli安装（推荐）

bot根目录下打开命令行，执行nb命令安装插件，插件配置会自动添加至配置文件 
```
nb plugin install nonebot_plugin_HttpCat
```
### 2. pip安装
```
pip install nonebot_plugin_HttpCat --upgrade
```  
打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  

```nonebot.load_plugin('nonebot_plugin_HttpCat')```  

或在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_HttpCat```即可  

### 3.应用思路（开发者）

本包提供了两个函数,分别对应了httpcat的 解释msg 和 图片url,或许大家可以拿来让http报错不再无聊~（笑）

```from nonebot_plugin_HttpCat import httpcat_msg, httpcat_pic```

...

``` send(msgs + MessageSegment.image(file=url)) ```

## 🎉 使用
### 指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| httpcat + http status code | 否 | 群聊/私聊 | 后加http提示码 |



**注意**

默认情况下, 您应该在指令前加上命令前缀, 通常是 /


### 🧡特别感谢 

omega-miya: https://github.com/Ailitonia/omega-miya 超可爱的Miyabot提供的httpcat思路
