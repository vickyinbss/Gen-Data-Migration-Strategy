import streamlit as st

def recommend_tool(db_size, write_freq, downtime, bandwidth, realtime_sync):
    if realtime_sync == "Yes":
        tool = "AWS DMS with CDC"
        approach = "Real-time Change Data Capture"
        plan = "Set up AWS Database Migration Service (DMS) with CDC between source and target. Validate sync, monitor latency, cutover after full sync."
        detailed_steps = [
            "1. Assess source and target DB compatibility.",
            "2. Set up AWS DMS replication instance.",
            "3. Configure source and target endpoints.",
            "4. Enable CDC on source DB.",
            "5. Start migration task with CDC enabled.",
            "6. Monitor replication lag and validate data.",
            "7. Cutover to target DB after full sync.",
            "8. Decommission replication and clean up resources."
        ]
        downtime_exp = "Minimal (seconds to minutes during cutover)"
        data_cost = "Depends on data volume and AWS DMS/S3 transfer rates."
        monitoring = "Monitor DMS task status, replication lag, and error logs via AWS Console/CloudWatch."
        rollback = "Keep source DB in sync until cutover. In case of issues, revert application connections to source DB."
        aws_service = "AWS Database Migration Service (DMS)"
    elif db_size > 500 and downtime == "Zero":
        tool = "AWS DMS with CDC"
        approach = "Change Data Capture"
        plan = "Use AWS DMS with CDC for near-zero downtime migration. Set up source and target endpoints, enable CDC, validate sync, cutover after sync."
        detailed_steps = [
            "1. Evaluate DB schema and compatibility.",
            "2. Provision AWS DMS replication instance.",
            "3. Configure endpoints for source and target.",
            "4. Enable CDC on source DB.",
            "5. Start full load and CDC migration task.",
            "6. Monitor migration progress and validate data.",
            "7. Cutover to target DB after sync completes.",
            "8. Clean up DMS resources."
        ]
        downtime_exp = "Near-zero (seconds to minutes during cutover)"
        data_cost = "Based on data volume and AWS DMS usage."
        monitoring = "Monitor DMS tasks, replication lag, and CloudWatch metrics."
        rollback = "Switch back to source DB if cutover fails; keep CDC running until successful migration."
        aws_service = "AWS Database Migration Service (DMS)"
    elif bandwidth < 100:
        tool = "AWS native DB export/import"
        approach = "Offline Migration"
        plan = "Schedule downtime, export data using AWS native DB tools, transfer during low network usage, import and validate."
        detailed_steps = [
            "1. Plan migration window and notify stakeholders.",
            "2. Export DB data using native tools (e.g., mysqldump, pg_dump).",
            "3. Transfer export files via AWS S3 or direct copy.",
            "4. Import data into target DB.",
            "5. Validate data integrity and application connectivity.",
            "6. Resume operations on target DB."
        ]
        downtime_exp = "High (hours, depending on data size and transfer speed)"
        data_cost = "S3 storage and transfer costs; minimal if using direct copy."
        monitoring = "Monitor transfer progress and import logs."
        rollback = "Retain source DB backup; restore if migration fails."
        aws_service = "AWS RDS Snapshot/Restore or AWS S3 for data transfer"
    elif write_freq == "High":
        tool = "AWS DMS with log-based replication"
        approach = "Continuous Replication"
        plan = "Set up AWS DMS with log-based replication, sync data continuously, cutover after validation."
        detailed_steps = [
            "1. Assess DB compatibility and replication support.",
            "2. Set up AWS DMS replication instance.",
            "3. Configure endpoints and enable log-based replication.",
            "4. Start migration task and monitor replication.",
            "5. Validate data consistency.",
            "6. Cutover to target DB after sync.",
            "7. Clean up resources."
        ]
        downtime_exp = "Low (minutes during cutover)"
        data_cost = "AWS DMS instance and data transfer charges."
        monitoring = "Monitor DMS task status, replication lag, and CloudWatch metrics."
        rollback = "Keep source DB operational until cutover; revert if issues arise."
        aws_service = "AWS Database Migration Service (DMS)"
    else:
        tool = "AWS native DB migration utilities"
        approach = "Full Backup & Restore"
        plan = "Perform full backup using AWS native tools, transfer, restore, and validate data integrity."
        detailed_steps = [
            "1. Backup source DB using native tools.",
            "2. Transfer backup files to target environment.",
            "3. Restore backup on target DB.",
            "4. Validate data and application connectivity.",
            "5. Switch operations to target DB."
        ]
        downtime_exp = "Moderate to high (depends on backup/restore time)"
        data_cost = "Storage and transfer costs for backup files."
        monitoring = "Monitor backup/restore progress and logs."
        rollback = "Retain source DB backup; restore if migration fails."
        aws_service = "AWS RDS Snapshot/Restore or AWS DMS"
    return tool, approach, plan, detailed_steps, downtime_exp, data_cost, monitoring, rollback, aws_service

st.title("DB Migration Recommendation Tool")

db_size = st.number_input("DB Size (GB)", min_value=1)
write_freq = st.selectbox("Frequency of Writes", ["Low", "Medium", "High"])
downtime = st.selectbox("Downtime Tolerance", ["Zero", "Minutes", "Hours"])
bandwidth = st.number_input("Network Bandwidth (Mbps)", min_value=1)
realtime_sync = st.selectbox("Real-time Sync Needed", ["No", "Yes"])

if st.button("Get Recommendation"):
    tool, approach, plan, detailed_steps, downtime_exp, data_cost, monitoring, rollback, aws_service = recommend_tool(
        db_size, write_freq, downtime, bandwidth, realtime_sync
    )
    st.subheader("Recommended Tool")
    st.write(tool)
    st.subheader("AWS Service to Use")
    st.write(aws_service)
    st.subheader("Migration Approach")
    st.write(approach)
    st.subheader("High-Level Migration Plan")
    st.write(plan)
    st.subheader("Detailed Step-by-Step Plan")
    for step in detailed_steps:
        st.write(step)
    st.subheader("Downtime Expectation")
    st.write(downtime_exp)
    st.subheader("Data Transfer Cost")
    st.write(data_cost)
    st.subheader("Monitoring Recommendation")
    st.write(monitoring)
    st.subheader("Rollback Recommendation")
    st.write(rollback)