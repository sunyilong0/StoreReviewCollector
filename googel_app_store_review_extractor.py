from google_play_scraper import app, Sort, reviews_all
import pandas as pd
from googletrans import Translator

def fetch_reviews(app_id, lang, country):
    # 获取所有评论
    result = reviews_all(
        app_id,
        sleep_milliseconds=0,  # 不暂停抓取评论
        lang=lang,  # 使用的语言
        country=country,  # 使用的国家
        sort=Sort.MOST_RELEVANT,  # 评论排序方式
    )
    return result

def translate_text(text, dest_language='zh-cn'):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_language)
        return translated.text
    except Exception as e:
        return "Error: " + str(e)

if __name__ == "__main__":
    # app_id = 'ai.character.app'
    app_id = input("请输入应用的ID: ")
    translate_confirm = input("是否要翻译评论？(yes/no): ")
    lang = 'en'  # 语言代码
    country = 'us'  # 国家代码
    reviews = fetch_reviews(app_id, lang, country)
    
    df = pd.DataFrame(reviews)
    initial_file_name = "(Google Play)自动抓取评论.xlsx"
    df.to_excel(initial_file_name, index=False)
    print(f"Reviews saved to {initial_file_name}.")
    # df = df[df['content'].str.contains("group chat|group", na=False)]
    # Ask user if they want to translate the reviews

    if translate_confirm.lower() == 'yes':
        # 应用翻译函数到content列
        df['Comment_translated'] = df['content'].apply(lambda x: translate_text(x, 'zh-cn'))
        translated_file_name = "(Google Play)自动抓取评论-翻译.xlsx"
        df.to_excel(translated_file_name, index=False)
        print(f"Translated reviews saved to {translated_file_name}.")
    else:
        print("未进行翻译。")
