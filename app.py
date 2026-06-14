import streamlit as st

st.set_page_config(
    page_title="حاسبة الخصومات الطبية",
    layout="wide"
)

# -------------------------
# تنسيق الواجهة
# -------------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

.stApp{
    background-color:#f4f6f8;
}

.big-total{
    background:#0f172a;
    color:#22d3ee;
    text-align:center;
    padding:20px;
    border-radius:12px;
    font-size:42px;
    font-weight:bold;
    border:2px solid #22d3ee;
}

.small-title{
    color:#666;
    font-size:12px;
}

.block{
    background:white;
    padding:15px;
    border-radius:10px;
    border:1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# تهيئة البيانات
# -------------------------
if "covered" not in st.session_state:
    st.session_state.covered = []

if "uncovered" not in st.session_state:
    st.session_state.uncovered = []

if "discounted" not in st.session_state:
    st.session_state.discounted = []

# -------------------------
# العنوان
# -------------------------
st.title("حاسبة الخصومات الطبية")
st.markdown(
    "<div class='small-title'>إعداد : جمعة بالقاسم</div>",
    unsafe_allow_html=True
)

st.divider()

# -------------------------
# الإدخال
# -------------------------
c1, c2, c3 = st.columns(3)

# المغطى
with c3:
    st.subheader("المغطى")

    covered_value = st.number_input(
        "أدخل قيمة",
        min_value=0.0,
        step=0.001,
        format="%.3f",
        key="covered_input"
    )

    if st.button("إضافة للمغطى"):
        st.session_state.covered.append(covered_value)

    st.write("القائمة:")

    for i, v in enumerate(st.session_state.covered):
        st.write(f"{i+1} - {v:.3f}")

# غير المغطى
with c2:
    st.subheader("غير المغطى")

    uncovered_value = st.number_input(
        "أدخل قيمة ",
        min_value=0.0,
        step=0.001,
        format="%.3f",
        key="uncovered_input"
    )

    if st.button("إضافة لغير المغطى"):
        st.session_state.uncovered.append(uncovered_value)

    st.write("القائمة:")

    for i, v in enumerate(st.session_state.uncovered):
        st.write(f"{i+1} - {v:.3f}")

# الخاضع للخصم
with c1:
    st.subheader("الخاضع للخصم")

    discounted_value = st.number_input(
        "أدخل قيمة  ",
        min_value=0.0,
        step=0.001,
        format="%.3f",
        key="discounted_input"
    )

    if st.button("إضافة للخاضع للخصم"):
        st.session_state.discounted.append(discounted_value)

    st.write("القائمة:")

    for i, v in enumerate(st.session_state.discounted):
        st.write(f"{i+1} - {v:.3f}")

st.divider()

# -------------------------
# الحسابات
# -------------------------
discount_rate = st.number_input(
    "نسبة الخصم %",
    value=30.0,
    step=1.0,
    format="%.3f"
)

sum_cov = sum(st.session_state.covered)
sum_unc = sum(st.session_state.uncovered)
sum_dis = sum(st.session_state.discounted)

discount_value = sum_dis * discount_rate / 100

after_discount = sum_dis - discount_value

uncovered_plus_discount = sum_unc + discount_value

total_before_discount = (
    sum_cov +
    sum_unc +
    sum_dis
)

covered_after_discount = (
    sum_cov +
    after_discount
)

# -------------------------
# النتائج
# -------------------------
st.header("النتائج")

r1, r2, r3 = st.columns(3)

with r1:
    st.metric(
        "المجموع بعد الخصم",
        f"{after_discount:.3f}"
    )

    st.metric(
        "المغطى + بعد الخصم",
        f"{covered_after_discount:.3f}"
    )

    st.metric(
        "الإجمالي النهائي",
        f"{covered_after_discount:.3f}"
    )

with r2:
    st.metric(
        "قيمة الخصم",
        f"{discount_value:.3f}"
    )

    st.metric(
        "غير المغطى + الخصم",
        f"{uncovered_plus_discount:.3f}"
    )

    st.metric(
        "الإجمالي قبل الخصم",
        f"{total_before_discount:.3f}"
    )

with r3:
    st.metric(
        "مجموع المغطى",
        f"{sum_cov:.3f}"
    )

    st.metric(
        "مجموع غير المغطى",
        f"{sum_unc:.3f}"
    )

    st.metric(
        "مجموع قبل الخصم",
        f"{sum_dis:.3f}"
    )

st.divider()

# -------------------------
# الإجمالي النهائي
# -------------------------
st.subheader("الإجمالي النهائي")

st.markdown(
    f"<div class='big-total'>{covered_after_discount:.3f}</div>",
    unsafe_allow_html=True
)

st.write("")

# -------------------------
# إعادة التهيئة
# -------------------------
if st.button("حساب جديد"):
    st.session_state.covered = []
    st.session_state.uncovered = []
    st.session_state.discounted = []
    st.rerun()