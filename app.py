import streamlit as st

st.set_page_config(page_title="حاسبة الخصومات الطبية", layout="wide")

if "covered" not in st.session_state:
    st.session_state.covered = []

if "uncovered" not in st.session_state:
    st.session_state.uncovered = []

if "discounted" not in st.session_state:
    st.session_state.discounted = []

st.title("حاسبة الخصومات الطبية")
st.caption("إعداد: جمعة بالقاسم")

col1, col2, col3 = st.columns(3)

with col3:
    st.subheader("المغطى")
    cov = st.number_input(
        "إضافة قيمة",
        key="cov_input",
        format="%.3f"
    )

    if st.button("إضافة للمغطى"):
        st.session_state.covered.append(cov)

    st.write(st.session_state.covered)

with col2:
    st.subheader("غير المغطى")
    unc = st.number_input(
        "إضافة قيمة ",
        key="unc_input",
        format="%.3f"
    )

    if st.button("إضافة لغير المغطى"):
        st.session_state.uncovered.append(unc)

    st.write(st.session_state.uncovered)

with col1:
    st.subheader("الخاضع للخصم")
    dis = st.number_input(
        "إضافة قيمة  ",
        key="dis_input",
        format="%.3f"
    )

    if st.button("إضافة للخاضع للخصم"):
        st.session_state.discounted.append(dis)

    st.write(st.session_state.discounted)

st.divider()

discount_rate = st.number_input(
    "نسبة الخصم %",
    value=30.0,
    format="%.3f"
)

sum_cov = sum(st.session_state.covered)
sum_unc = sum(st.session_state.uncovered)
sum_dis = sum(st.session_state.discounted)

discount_value = sum_dis * discount_rate / 100
after_discount = sum_dis - discount_value

uncovered_plus_discount = sum_unc + discount_value
total_before_discount = sum_cov + sum_unc + sum_dis
covered_after_discount = sum_cov + after_discount

r1, r2, r3 = st.columns(3)

with r1:
    st.metric("المجموع بعد الخصم", f"{after_discount:.3f}")
    st.metric("المغطى + بعد الخصم", f"{covered_after_discount:.3f}")
    st.metric("صافي المطالبة", f"{covered_after_discount:.3f}")

with r2:
    st.metric("قيمة الخصم", f"{discount_value:.3f}")
    st.metric("غير المغطى + الخصم", f"{uncovered_plus_discount:.3f}")
    st.metric("الإجمالي قبل الخصم", f"{total_before_discount:.3f}")

with r3:
    st.metric("مجموع المغطى", f"{sum_cov:.3f}")
    st.metric("مجموع غير المغطى", f"{sum_unc:.3f}")
    st.metric("مجموع قبل الخصم", f"{sum_dis:.3f}")

st.divider()

st.markdown("## الإجمالي النهائي")

st.success(f"{covered_after_discount:.3f}")

if st.button("حساب جديد"):
    st.session_state.covered = []
    st.session_state.uncovered = []
    st.session_state.discounted = []
    st.rerun()