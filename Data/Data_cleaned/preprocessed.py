import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Đọc dữ liệu từ file CSV
df = pd.read_csv('thehackernews2_cleaned.csv')

# Chuyển đổi thời gian đăng từ chuỗi sang đối tượng datetime
df['time'] = pd.to_datetime(df['time'])

# Điền vào các giá trị bị thiếu
# Ở đây,  ta sẽ điền vào các giá trị bị thiếu bằng giá trị xuất hiện nhiều nhất
for column in df.columns:
    mode = df[column].mode()
    if not mode.empty:
        df[column].fillna(mode[0], inplace=True)

# Lưu dữ liệu đã tiền xử lý vào một file mới
df.to_csv('thehackernews2_preprocessed.csv', index=False)
