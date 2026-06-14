with c3:
    st.subheader("المغطى")
    v = st.number_input(
        "إضافة قيمة",
        min_value=0.0,
        value=None,
        step=0.001,
        format="%.3f",
        key="cov_input"
    )

    if st.button("إضافة للمغطى"):
        if v is not None:
            st.session_state.covered.append(v)
            st.rerun()
            st.header("النتائج")
            st.write(
                "المغطى:",
                sum_cov,
                "غير المغطى:",
                sum_unc,
                "الخاضع للخصم:",
                sum_dis
            )