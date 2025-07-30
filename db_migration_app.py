import streamlit as st
from styles import get_styles
from business_logic import recommend_tool, recommend_file_storage

st.set_page_config(page_title="Data Migration Strategy Generator", page_icon="🛠️", layout="centered")
st.markdown(get_styles(), unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center; color:#1a237e; font-family:Segoe UI, sans-serif;'>🛠️ Data Migration Strategy Generator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #42a5f5 0%, #f06292 100%);
                color: white; padding:16px; border-radius:12px; margin-bottom:18px; font-size:20px;">
        <b>
        This tool helps you generate a tailored AWS migration strategy for both databases and shared file storage, based on your requirements.<br>
        Receive the best-fit AWS migration service, approach, step-by-step plan, downtime expectations, cost estimates, monitoring, and rollback recommendations.
        </b>
    </div>
    """,
    unsafe_allow_html=True
)

with st.form("migration_form"):
    st.markdown("""
        <div style="background: linear-gradient(90deg, #f8bbd0 0%, #bbdefb 100%);
                    color: #1a237e; padding:14px; border-radius:10px; margin-bottom:18px; font-size:22px;
                    font-family: 'Segoe UI', sans-serif; text-align:center; box-shadow: 0 2px 8px rgba(33,150,243,0.08);">
            <b>🔎 Source System & Business Constraints</b>
        </div>
        """, unsafe_allow_html=True)
    # Database inputs
    st.markdown("<b style='color:#3949ab;'>Database Migration</b>", unsafe_allow_html=True)
    db_size = st.number_input("📦 DB Size (GB)", min_value=1)
    write_freq = st.selectbox("✍️ Frequency of Writes", ["Low", "Medium", "High"])
    downtime = st.selectbox("⏱️ Downtime Tolerance", ["Zero", "Minutes", "Hours"])
    bandwidth = st.number_input("🌐 Network Bandwidth (Mbps)", min_value=1)
    realtime_sync = st.selectbox("🔄 Real-time Sync Needed", ["No", "Yes"])
    # File storage inputs
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<b style='color:#1a237e;'>Shared File Storage Migration</b>", unsafe_allow_html=True)
    file_size = st.number_input("🗄️ Total File Size (GB)", min_value=1)
    file_count = st.number_input("📁 Number of Files", min_value=1)
    file_change_freq = st.selectbox("🔁 File Change Frequency", ["Low", "Medium", "High"])
    file_downtime = st.selectbox("⏳ File Migration Downtime Tolerance", ["Zero", "Minutes", "Hours"])
    file_realtime_sync = st.selectbox("🔄 Real-time Sync Needed for Files", ["No", "Yes"])
    submitted = st.form_submit_button("✨ Get Recommendation")

if submitted:
    # Database strategy
    tool, approach, plan, detailed_steps, downtime_exp, data_cost, monitoring, rollback, aws_service = recommend_tool(
        db_size, write_freq, downtime, bandwidth, realtime_sync
    )
    st.markdown("<h3 style='color:#1a237e;'>Database Migration Strategy</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>🛠️ Recommended Tool:</b> {tool}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>☁️ AWS Service to Use:</b> {aws_service}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>🚀 Migration Approach:</b> {approach}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>📋 High-Level Migration Plan:</b> {plan}</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1a237e;'>📝 Detailed Step-by-Step Plan</h4>", unsafe_allow_html=True)
    for step in detailed_steps:
        st.markdown(f"<div class='step-box'>{step}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>⏳ Downtime Expectation:</b> {downtime_exp}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>💸 Data Transfer Cost:</b> {data_cost}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>📊 Monitoring Recommendation:</b> {monitoring}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>🔄 Rollback Recommendation:</b> {rollback}</div>", unsafe_allow_html=True)

    # File storage strategy
    file_tool, file_service, file_plan, file_steps, file_downtime_exp, file_cost, file_monitoring, file_rollback = recommend_file_storage(
        file_size, file_count, file_change_freq, file_downtime, bandwidth, file_realtime_sync
    )
    st.markdown("<h3 style='color:#1a237e;'>Shared File Storage Migration Strategy</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>🛠️ Recommended Tool:</b> {file_tool}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>☁️ AWS Service to Use:</b> {file_service}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>📋 High-Level Migration Plan:</b> {file_plan}</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#1a237e;'>📝 Detailed Step-by-Step Plan</h4>", unsafe_allow_html=True)
    for step in file_steps:
        st.markdown(f"<div class='step-box'>{step}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>⏳ Downtime Expectation:</b> {file_downtime_exp}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>💸 Data Transfer Cost:</b> {file_cost}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>📊 Monitoring Recommendation:</b> {file_monitoring}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-box'><b>🔄 Rollback Recommendation:</b> {file_rollback}</div>", unsafe_allow_html=True)