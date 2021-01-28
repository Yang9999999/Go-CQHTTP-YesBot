<p align="center">
  <a href="https://ishkong.github.io/go-cqhttp-docs/"><img src="https://i.loli.net/2021/01/28/XFrqchNZ5o2MOLB.jpg" width="200" height="200" alt="go-cqhttp"></a>
</p>


<div align="center">

# Yes酱-会发涩图的群管理机器人

_✨ 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，使用[OneBot](https://github.com/howmanybots/onebot)标准的插件 ✨_

</div>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/python-v3.7%2B-blue" alt="license">
  </a>
  <a href="https://github.com/Yang9999999/Go-CQHTTP-YesBot">
    <img src="https://img.shields.io/badge/release-v1.0-red" alt="release">
  </a>
  <a href="https://github.com/howmanybots/onebot/blob/master/README.md">
    <img src="https://img.shields.io/badge/OneBot-v11-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
  <a href="https://github.com/Mrs4s/go-cqhttp/actions">
    <img src="https://github.com/Mrs4s/go-cqhttp/workflows/CI/badge.svg" alt="action">
  </a>
</p>



---

Go-CQHTTP-YesBot 是采用python编写，**可拓展的**，**适合新手**的入门级QQ机器人插件

## 目前拥有的功能

- 发送setu/猫猫图返回一张涩图/猫猫图
- 检测关键字禁言
- 私聊调教对话
- ~~发送huangse获得R18涩图~~
- 更多功能待开发....

## 配置

配置信息在**config.json**中

```json
{
    "path":"/C:\\Users\\86175\\Desktop\\mybot\\pic\\mao\\",    储存猫猫图的路径  Linux下"/root/mybot1/pic/mao/"
	"ban_words":["科学上网","黑产","翻墙"],    禁言关键词
    "apikey":"xxxxxxxxxxxxxxxx",    涩图API的apikey
    "group":[123456789,987654321],     Yes酱管理的群号
    "self_qq":"2013996860"       Yes酱的QQ号
}
```



## API

- 机器人采用的[涩图API](https://api.lolicon.app/#/setu)

## 编写目的

用于python学习和交流

## 文档
