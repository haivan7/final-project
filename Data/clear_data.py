# Import các thư viện cần thiết
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Đọc dữ liệu từ file CSV
df = pd.read_csv('thehackernews10.csv')

# Loại bỏ các dòng trùng lặp
df = df.drop_duplicates()

# Loại bỏ các dòng không chứa nội dung bài đăng
df = df[df['post_text'].str.strip() != ""]

# Loại bỏ các dòng không chứa thời gian đăng
df = df[pd.notnull(df['time'])]

# Lưu dữ liệu đã làm sạch vào một file mới
df.to_csv('thehackernews10_cleaned.csv', index=False)

# Đọc dữ liệu đã làm sạch từ file CSV
df = pd.read_csv('thehackernews10_cleaned.csv')

# Chuyển đổi thời gian đăng từ chuỗi sang đối tượng datetime
df['time'] = pd.to_datetime(df['time'])

# Điền vào các giá trị bị thiếu
# Ở đây, ta sẽ điền vào các giá trị bị thiếu bằng giá trị xuất hiện nhiều nhất
for column in df.columns:
    mode = df[column].mode()
    if not mode.empty:
        df[column].fillna(mode[0], inplace=True)

# Lưu dữ liệu đã tiền xử lý vào một file mới
df.to_csv('thehackernews10_preprocessed.csv', index=False)
