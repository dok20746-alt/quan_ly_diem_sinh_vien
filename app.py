
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

# 2. Tạo dữ liệu 10 sinh viên
data = {
    "Ho_ten": [
        "Nguyen Van An", "Vo Le Duy",
        "Do Huynh Duy Khoa", "Nguyen Dac Tien",
        "Tran Van Dat", "Ho Nhat Huy",
        "Tran Minh Huy", "Tran Quoc Tien",
        "Nguyen Thi Thanh Ha", "Nguyen Anh Huy"
    ],
    "Chuyen_can": [9, 7, 10, 7, 9, 6, 8, 9, 7, 10],
    "Giua_ky": [8, 7, 9, 6, 8, 7, 6, 8, 9, 9],
    "Cuoi_ky": [9, 8, 10, 7, 9, 5, 7, 9, 8, 10]
}

df = pd.DataFrame(data)

# 3. Tính điểm tổng kết
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

# 4. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Tiêu đề và bảng điểm
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.subheader("Bảng điểm sinh viên")

bang_diem = df.rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_diem, use_container_width=True)

# 6. Thống kê kết quả
st.subheader("Thống kê kết quả")

st.metric(
    "Điểm trung bình lớp",
    round(df["Tong_ket"].mean(), 2)
)

cao = df.loc[df["Tong_ket"].idxmax()]
thap = df.loc[df["Tong_ket"].idxmin()]

col1, col2 = st.columns(2)

with col1:
    st.write("**Sinh viên cao điểm nhất**")
    st.write(cao["Ho_ten"], "-", round(cao["Tong_ket"], 2))

with col2:
    st.write("**Sinh viên thấp điểm nhất**")
    st.write(thap["Ho_ten"], "-", round(thap["Tong_ket"], 2))

st.write(
    "Số sinh viên đạt:",
    int((df["Tong_ket"] >= 5).sum())
)

# 7. Tra cứu thông tin sinh viên
st.subheader("Tra cứu điểm sinh viên")

ten = st.selectbox("Chọn một sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write("Họ tên:", sv["Ho_ten"])
st.write("Điểm chuyên cần:", sv["Chuyen_can"])
st.write("Điểm giữa kỳ:", sv["Giua_ky"])
st.write("Điểm cuối kỳ:", sv["Cuoi_ky"])
st.write("Điểm tổng kết:", round(sv["Tong_ket"], 2))
st.write("Xếp loại:", sv["Xep_loai"])

# 8. Vẽ biểu đồ điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.xticks(rotation=45, ha="right")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. Thông tin người thực hiện
st.markdown("---")
st.caption("Người tạo: ĐỖ HUỲNH DUY KHOA | MSSV: 26")
