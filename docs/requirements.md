# 数据库系统概论 大作业描述

## 考核方式

- 组队完成，3-5人一队
- 需要在课堂上答辩
- 需要提交大作业报告和源码

## 应用场景

- obe系统
- 学院主页
- 新浪财经
- 等等

> [!TIP]
> 自行选择上述网站的部分功能，其中至少包含数据写入、数据更改和数据查找各1项
>
> 可以根据需要设置多个不同类型用户，比如obe系统可以设计学生和教师用户；学院主页可以设置普通访客和网站管理员等

## 任务1. 在大模型辅助下完成数据库设计

- 学习使用提示词（Prompt）和KimiChat、ChatGLM等大模型应用交互，完成ER图和数据库模式的设计
- 具体要求
  - 学习Prompt的使用技巧，能够通过Prompt让大模型更好完成任务
  - 能够评判大模型输出结果的正确性和好坏，并通过和大模型多次交互逐渐改进结果
  - 从规范化程度和应用开发的方便性综合评判最终选择的数据库模式
  - 最终需要得到E-R图，并且其形式需要与教材上介绍的E-R模型尽量接近
  - 实体和表的数量均在6个以上

## 任务2：实现简单功能，响应用户请求

- 选项1：采用传统动态网站开发方式，如Python Django，Java JSP，PHP等

- 选项2：结合大模型来响应请求
  - 让用户以自然语言的形式提交请求，并用大模型部分替代传统的应用程序
  - 学习通过使用大模型API（例如kimichat、chatGLM）与模型交互
    - 将自然语言转换为对数据库的操作（SQL），并调用程序来执行SQL操作，将操作执行或查询的结果以合适方式展示给用户
    - 检查用户的权限，判断操作是否能够执行，例如学生不可查询其他用户的密码
    - 根据应用逻辑，判断操作能否执行比如，一个班级容量40人，则超过40人就不能执行选课