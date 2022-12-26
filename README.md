# WebMusic

### 

## 功能设计
- 实现基于Web的播放音乐，精彩评论、配图、文字分享平台。

## 技术架构


- 本项目基于django@latest、vue@latest、mysql实现

## 部署文档

### 环境准备

- Python3.9以上，npm，nodeJS
- Django相关组件安装
- Vue3相关组件安装
- Git

### 文件下载

- Clone [项目地址](https://github.com/wty92911/SE)

### 运行

- 开启后端服务：在`SE/WebMusic`目录下，运行`python3 manage.py runserver `
- 数据库默认路径为课程服务器路径，如有需求请自行修改
- 如在本地开启后端服务，需修改`SE/WebMusic/frontend/src/api/index.js`中Axios的baseURL以适配本地路径
- 运行前端组件：在`SE/WebMusic/frontend`目录下，运行`npm install`，`npm run dev`
- 成功运行后访问终端显示地址即可运行。
## 小组分工

- UI设计 前端 zyn lyz lxz
- 后端  zjr ddy jyt
- 数据处理 wty zx

## 环境准备
- python3.10
- django@latest
- 一些python依赖包


## 项目规划
- ### 核心需求

  - 歌曲播放、检索、评论
  - 音乐可视化互动（律动动画，弹幕）
  - 改善用户阅读评论体验 
    - 评论标签化分类	
    - 检索多元（热度、时间、内容相关性）
    - 区别于传统阅读评论交互式设计：弹幕/卡片式渐入渐出（动画）

- ### 其他需求

  - 支持个人账户登录
  - 一起听功能：多人、交流
  - 歌曲个性化推荐
  - Web安全相关防护
  - 评论词义分析、识别恶意评论、自动分类 

- ### 项目流程

  - 详见甘特图

- ### 分工汇报

  - 

