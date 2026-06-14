import streamlit as st

st.set_page_config(
    page_title="حاسبة الخصومات الطبية",
    layout="wide"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

.big-total {
    background-color: #111;
    color: #00ffff;
    text-align: center;
    padding: 20px;
    border-radius: 10px;
    font-size: 40px;
    font-weight: bold;
}

.metric-box {
    border: 1px solid #444;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

if "covered" not in st.session_state:
    st.session_state.covered = []

if "uncovered" not in st.session_state:
    st.session_state.uncovered = []

if "discounted" not in st.session_state:
    st.session_state.discounted = []

st.title("حاسبة الخصومات الطبية")
st.caption("إعداد: جمعة بالقاسم")

c1, c2, c3 = st.columns(3)

with c3:
    st.subheader("المغطى")
    v = st.text_input("إضافة قيمة", key="cov")
    if st.button("إضافة للمغطى"):
        try:
            st.session_state.covered.append(float(v))
        except:
            pass

    st.write([f"{x:.3f}" for x in st.session_state.covered])

with c2:
    st.subheader("غير المغطى")
    v = st.text_input("إضافة قيمة ", key="unc")

    if st.button("إضافة لغير المغطى"):
        try:
            st.session_state.uncovered.append(float(v))
        except:
            pass

    st.write([f"{x:.3f}" for x in st.session_state.uncovered])

with c1:
    st.subheader("الخاضع للخصم")
    v = st.text_input("إضافة قيمة  ", key="dis")

    if st.button("إضافة للخاضع للخصم"):
        try:
            st.session_state.discounted.append(float(v))
        except:
            pass

    st.write([f"{x:.3f}" for x in st.session_state.discounted])

st.divider()

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
total_before = sum_cov + sum_unc + sum_dis
covered_after_discount = sum_cov + after_discount

st.header("النتائج")

r1, r2, r3 = st.columns(3)

with r1:
    st.metric("المجموع بعد الخصم", f"{after_discount:.3f}")
    st.metric("المغطى + بعد الخصم", f"{covered_after_discount:.3f}")
    st.metric("صافي المطالبة", f"{covered_after_discount:.3f}")

with r2:
    st.metric("قيمة الخصم", f"{discount_value:.3f}")
    st.metric("غير المغطى + الخصم", f"{uncovered_plus_discount:.3f}")
    st.metric("الإجمالي قبل الخصم", f"{total_before:.3f}")

with r3:
    st.metric("مجموع المغطى", f"{sum_cov:.3f}")
    st.metric("مجموع غير المغطى", f"{sum_unc:.3f}")
    st.metric("مجموع قبل الخصم", f"{sum_dis:.3f}")

st.markdown("### الإجمالي النهائي")

st.markdown(
    f'<div class="big-total">{covered_after_discount:.3f}</div>',
    unsafe_allow_html=True
)

st.write("")

if st.button("حساب جديد"):
    st.session_state.covered = []
    st.session_state.uncovered = []
    st.session_state.discounted = []
    st.rerun()