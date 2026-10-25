import streamlit as st

st.set_page_config(
    page_title="GLOWUP AI",
    page_icon="💗",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #fff5f8;
}
h1, h2, h3 {
    color: #c44d7d;
}
.stButton > button {
    background-color: #e86b9a;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("💗 GLOWUP AI")
st.subheader("Your Face. Your Style. Your Makeup.")

st.write(
    "Khám phá phong cách trang điểm phù hợp "
    "với sở thích và ngân sách của bạn!"
)

st.info(
    "Chào mừng bạn đến với bản thử nghiệm GLOWUP AI."
)

st.header("📸 1. Tải ảnh chân dung")

photo = st.file_uploader(
    "Chọn ảnh của bạn",
    type=["jpg", "jpeg", "png"]
)

if photo is not None:
    st.image(
        photo,
        caption="Ảnh bạn đã tải lên",
        use_container_width=True
    )

st.header("💄 2. Chọn phong cách trang điểm")

style = st.selectbox(
    "Bạn thích phong cách nào?",
    [
        "Korean Natural",
        "Clean Girl",
        "Douyin",
        "Soft Glam",
        "Trang điểm đi học"
    ]
)

occasion = st.selectbox(
    "Bạn sẽ trang điểm vào dịp nào?",
    [
        "Đi học",
        "Đi chơi",
        "Hằng ngày",
        "Dự tiệc"
    ]
)

budget = st.selectbox(
    "Ngân sách mỹ phẩm của bạn?",
    [
        "Dưới 200.000đ",
        "200.000đ - 500.000đ",
        "Trên 500.000đ"
    ]
)

guides = {
    "Korean Natural": [
        "Dùng lớp nền mỏng nhẹ",
        "Tán má hồng tự nhiên",
        "Kẻ mắt mảnh",
        "Chọn son hồng nhẹ"
    ],
    "Clean Girl": [
        "Chuẩn bị da và chống nắng",
        "Chải lông mày tự nhiên",
        "Dùng má hồng nhẹ",
        "Chọn son bóng"
    ],
    "Douyin": [
        "Tạo lớp nền đều màu",
        "Nhấn nhũ mắt vừa phải",
        "Chuốt mi và kẻ mắt",
        "Chọn màu son nổi bật"
    ],
    "Soft Glam": [
        "Tạo lớp nền mịn",
        "Tán mắt màu trung tính",
        "Tạo khối nhẹ nhàng",
        "Dùng son nude hoặc hồng đất"
    ],
    "Trang điểm đi học": [
        "Chăm sóc da và chống nắng",
        "Trang điểm nền nhẹ nếu cần",
        "Chải lông mày",
        "Dùng son dưỡng có màu"
    ]
}

st.header("✨ 3. Nhận gợi ý trang điểm")

if st.button("Tạo gợi ý cho tôi"):
    st.subheader(f"Phong cách: {style}")
    st.write(f"Dịp sử dụng: {occasion}")
    st.write(f"Ngân sách: {budget}")

    st.markdown("### Các bước trang điểm")

    for i, step in enumerate(guides[style], start=1):
        st.write(f"{i}. {step}")

    st.success("Đã tạo gợi ý trang điểm!")

    st.caption(
        "Đây là gợi ý theo phong cách bạn chọn, "
        "chưa phải kết quả phân tích ảnh bằng AI."
    )

st.divider()

st.caption("GLOWUP AI | Beauty made personal 💗")