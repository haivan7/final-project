
# Import các thư viện cần thiết
from facebook_scraper import get_posts
import pandas as pd
import numpy as np

# Định nghĩa các biến
FANPAGE_LINK = "thehackernews" # Thay đổi này thành liên kết tới fanpage
FOLDER_PATH = "/workspaces/final-project-haivan7/Data" # Thay đổi này thành thư mục  muốn lưu dữ liệu
COOKIE_PATH = "cookies.txt" # Thay đổi này thành đường dẫn tới file cookie 

POSTS_NUMBER = 200 # Số lượng bài viết  muốn thu thập

# Thu thập dữ liệu từ Facebook
post_list = []
for post in get_posts(FANPAGE_LINK, options={"comments": True, "reactions": True, "allow_extra_requests": True}, extra_info=True, cookies=COOKIE_PATH):
    print(post)
    post_list.append(post)
    if len(post_list) >= POSTS_NUMBER:
        break

# Kiểm tra nếu danh sách post_list không rỗng thì tạo DataFrame
if post_list:
    # Chuyển đổi danh sách các từ điển thành dataframe và lưu vào tệp csv
    post_df_full = pd.DataFrame(columns=post_list[0].keys(), index=range(len(post_list)), data=post_list)
    path = FOLDER_PATH + "/" + FANPAGE_LINK + "10.csv"
    post_df_full.to_csv(path, index=False)
    print(path)
else:
    print("Không có bài viết nào được thu thập.")
