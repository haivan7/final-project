import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('thehackernews2.csv')

# Loại bỏ các dòng trùng lặp
df = df.drop_duplicates()

# Loại bỏ các dòng không chứa nội dung bài đăng
df = df[df['post_text'].str.strip() != ""]

# Loại bỏ các dòng không chứa thời gian đăng
df = df[pd.notnull(df['time'])]

# Lưu dữ liệu đã làm sạch vào một file mới
df.to_csv('thehackernews2_cleaned.csv', index=False)

