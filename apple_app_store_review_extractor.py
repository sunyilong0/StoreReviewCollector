import pandas as pd
import requests
from googletrans import Translator

def fetch_reviews(app_id, app_name, total_pages=10):
    all_reviews = []
    for page_num in range(1, total_pages + 1):
        url = f"https://itunes.apple.com/rss/customerreviews/page={page_num}/id={app_id}/sortby=mostrecent/json?l=en&cc=us"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            entries = data['feed'].get('entry', [])
            reviews = []
            for entry in entries:
                try:
                    reviews.append({
                        "Username": entry['author']['name']['label'],
                        "User URI": entry['author']['uri']['label'],
                        "Date": entry['updated']['label'],
                        "Rating": entry['im:rating']['label'],
                        "Version": entry['im:version']['label'],
                        "Review ID": entry['id']['label'],
                        "Title": entry['title']['label'],
                        "Comment": entry['content']['label'],
                        "Type": entry['content']['attributes']['type'],
                        "Review Link": entry['link']['attributes']['href'],
                        "Vote Sum": entry['im:voteSum']['label'],
                        "Vote Count": entry['im:voteCount']['label'],
                        "Content Type": entry['im:contentType']['attributes']['label']
                    })
                except KeyError:
                    continue
            all_reviews.extend(reviews)
        else:
            print(f"Failed to fetch reviews for page {page_num}.")
    return all_reviews

def save_reviews_to_excel(reviews, app_name, file_desc="reviews"):
    total_reviews = len(reviews)
    file_name = f"{app_name}_抓取{total_reviews}条_{file_desc}.xlsx"
    df = pd.DataFrame(reviews)
    df.to_excel(file_name, index=False)
    print(f"Reviews saved to {file_name}.")
    return file_name

def filter_reviews_by_keyword(df, keyword):
    filtered_df = df[df['Comment'].str.contains(keyword, na=False)]
    return filtered_df

def translate_reviews(df, dest_language='zh-cn'):
    translator = Translator()
    df['Comment_translated'] = df['Comment'].apply(
        lambda x: translate_text(translator, x, dest_language)
    )
    return df

def translate_text(translator, text, dest_language):
    try:
        return translator.translate(text, dest=dest_language).text
    except Exception as e:
        return "Error: " + str(e)

    

def main():
    # 从用户获取应用的ID和名称
    # app_id = "1671705818"
    # app_name = "Character_AI_IOS"
    app_id = input("请输入应用的ID: ")
    app_name = input("请输入应用的名称: ")
    translate_confirm = input("是否要翻译评论？(yes/no): ")

    # 使用用户提供的应用ID和名称获取评论
    reviews = fetch_reviews(app_id, app_name)

    # 保存评论到Excel文件中
    initial_file_name = save_reviews_to_excel(reviews, app_name)
    if translate_confirm.lower() == 'yes':
        df = pd.DataFrame(reviews)
        
        # 筛选和翻译评论
        # df = filter_reviews_by_keyword(df, "group chat|group")
        translated_df = translate_reviews(df)
        filtered_file_name = save_reviews_to_excel(translated_df, app_name, "选取群聊相关_翻译")
    else:
        print("未进行翻译。")

if __name__ == "__main__":
    main()
