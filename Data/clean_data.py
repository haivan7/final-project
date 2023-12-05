# Import các thư viện cần thiết
import pandas as pd
import numpy as np

# Đọc dữ liệu từ file csv
df = pd.read_csv("thehackernews10.csv")

# Làm sạch dữ liệu với cột
# Xóa các cột có giá trị các hàng không có giá trị (đều là NULL)
df.dropna(axis=1, how='all', inplace=True)

# Xóa các cột có giá trị các hàng là trùng nhau
df = df.T.drop_duplicates().T

# Xóa các cột không cần thiết
del df['text']
del df['images']
del df['image_ids']
del df['images_description']
del df['fetched_time']
del df['images_lowquality']

# Làm sạch dữ liệu với hàng
# Xóa các hàng có giá trị NULL ở các cột quan trọng ảnh hưởng đến quá trình phân tích
df.dropna(subset=['reactions'], inplace=True)
df.dropna(subset=['reaction_count'], inplace=True)
df.dropna(subset=['shares'], inplace=True)
df.dropna(subset=['comments'], inplace=True)
df.dropna(subset=['comments_full'], inplace=True)
df.dropna(subset=['time'], inplace=True)

# Chuyển đổi thời gian đăng từ chuỗi sang đối tượng datetime
df['time'] = pd.to_datetime(df['time'])

# Thêm trường thông tin 'date_only' và 'hour_only'
df['date_only'] = df['time'].dt.strftime('%m-%d-%Y')
df['hour_only'] = df['time'].dt.strftime('%H-%M')

# Xác định khoảng thời gian để phân tích dữ liệu
df = df[(df['time'].dt.year == 2023)&(df['time'].dt.month.isin([7, 8, 9, 10, 11]))]

# Xóa các bài post được đăng vào ngày 20/11/2023
row_to_drop = df[df["date_only"] == "11-20-2023"].index
df.drop(row_to_drop, inplace=True)

# Lưu dữ liệu đã tiền xử lý vào một file mới
df.to_csv('Data_clean.csv', index=False)
