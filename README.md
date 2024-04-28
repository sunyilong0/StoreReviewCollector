# README.md

## 概述
本文档提供了如何使用脚本从Google Play商店和Apple App商店提取特定应用的评论的说明。

## 前提条件
- 已安装必要库（例如 `requests`、`pandas` 等）的Python环境
google-play-scraper
pandas version: 2.0.3
googletrans version: 4.0.0-rc.1
requests version: 2.31.0

- 访问终端或命令行界面

## 从Google Play商店提取评论

### 脚本：`googel_app_store_review_extractor.py`

#### 运行步骤：
1. 导航到您的工作目录：
   ```
   cd StoreReviewCollector
   ```
2. 使用Python执行脚本：
   ```
    python googel_app_store_review_extractor.py 
   ```
3. 根据提示，输入您希望提取评论的应用ID：
   ```
   请输入应用的ID: ai.character.app
   ```
4. 选择是否翻译评论：
   ```
   是否要翻译评论？(yes/no): no
   ```
5. 评论将被保存到一个名为 `Google Play 自动抓取评论.xlsx` 的Excel文件中，未进行翻译，如果选择yes就会调用谷歌的去翻译。

#### 获取应用ID：
- Google Play商店的应用ID (`ai.character.app`) 可以从应用的URL中获取：
  ```
  https://play.google.com/store/apps/details?id=ai.character.app&hl=en_US
  ```

## 从Apple App商店提取评论

### 脚本：`apple_app_store_review_extractor.py`

#### 运行步骤：
1. 导航到您的工作目录：
   ```
   cd StoreReviewCollector
   ```
2. 使用Python执行脚本：
   ```
   python apple_app_store_review_extractor.py
   ```
3. 根据提示，输入应用ID和名称：
   ```
   请输入应用的ID: 1671705818
   请输入应用的名称: Character_AI_IOS
   ```
4. 选择是否翻译评论：
   ```
   是否要翻译评论？(yes/no): no
   ```
5. 评论将被保存到一个名为 `Character_AI_IOS_抓取500条_reviews.xlsx` 的Excel文件中，未进行翻译，如果选择yes就会调用谷歌的去翻译。

#### 获取应用ID和名称：
- Apple App商店的应用ID (`1671705818`) 和应用名称 (`Character_AI_IOS`) 可以从应用的URL中获取：
  ```
  https://apps.apple.com/us/app/character-ai-ai-powered-chat/id1671705818
  ```

## 结论
按照这些步骤，您可以从Google Play商店和Apple App商店为特定应用提取并保存评论。根据您的需求调整应用ID和名称。
