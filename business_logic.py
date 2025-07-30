def recommend_tool(db_size, write_freq, downtime, bandwidth, realtime_sync):
    if realtime_sync == "Yes":
        tool = "AWS DMS with CDC"
        approach = "Real-time Change Data Capture"
        plan = "Set up AWS Database Migration Service (DMS) with CDC between source and target. Validate sync, monitor latency, cutover after full sync."
        detailed_steps = [
            "Assess source and target DB compatibility.",
            "Set up AWS DMS replication instance.",
            "Configure source and target endpoints.",
            "Enable CDC on source DB.",
            "Start migration task with CDC enabled.",
            "Monitor replication lag and validate data.",
            "Cutover to target DB after full sync.",
            "Decommission replication and clean up resources."
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
            "Evaluate DB schema and compatibility.",
            "Provision AWS DMS replication instance.",
            "Configure endpoints for source and target.",
            "Enable CDC on source DB.",
            "Start full load and CDC migration task.",
            "Monitor migration progress and validate data.",
            "Cutover to target DB after sync completes.",
            "Clean up DMS resources."
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
            "Plan migration window and notify stakeholders.",
            "Export DB data using native tools (e.g., mysqldump, pg_dump).",
            "Transfer export files via AWS S3 or direct copy.",
            "Import data into target DB.",
            "Validate data integrity and application connectivity.",
            "Resume operations on target DB."
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
            "Assess DB compatibility and replication support.",
            "Set up AWS DMS replication instance.",
            "Configure endpoints and enable log-based replication.",
            "Start migration task and monitor replication.",
            "Validate data consistency.",
            "Cutover to target DB after sync.",
            "Clean up resources."
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
            "Backup source DB using native tools.",
            "Transfer backup files to target environment.",
            "Restore backup on target DB.",
            "Validate data and application connectivity.",
            "Switch operations to target DB."
        ]
        downtime_exp = "Moderate to high (depends on backup/restore time)"
        data_cost = "Storage and transfer costs for backup files."
        monitoring = "Monitor backup/restore progress and logs."
        rollback = "Retain source DB backup; restore if migration fails."
        aws_service = "AWS RDS Snapshot/Restore or AWS DMS"
    return tool, approach, plan, detailed_steps, downtime_exp, data_cost, monitoring, rollback, aws_service

def recommend_file_storage(file_size, file_count, file_change_freq, file_downtime, bandwidth, file_realtime_sync):
    if file_realtime_sync == "Yes":
        tool = "AWS DataSync with continuous sync"
        service = "AWS DataSync"
        plan = "Set up AWS DataSync for continuous file replication between source and target. Monitor sync status and cutover after full sync."
        steps = [
            "Deploy AWS DataSync agent on-premises or in VM.",
            "Configure source and destination locations (e.g., NFS, SMB, S3, EFS).",
            "Create and start DataSync task with continuous sync.",
            "Monitor sync progress and validate file integrity.",
            "Cutover to target storage after full sync.",
            "Decommission DataSync agent after migration."
        ]
        downtime_exp = "Minimal (seconds to minutes during cutover)"
        cost = "Based on total data transferred and DataSync usage."
        monitoring = "Monitor DataSync task status and CloudWatch metrics."
        rollback = "Keep source storage available until cutover; revert if needed."
    elif file_size > 1000 or file_count > 100000:
        tool = "AWS Snowball or DataSync (batch)"
        service = "AWS Snowball, AWS DataSync"
        plan = "Use AWS Snowball for large-scale transfer or DataSync for batch migration. Validate files after transfer."
        steps = [
            "Order and configure AWS Snowball device or set up DataSync agent.",
            "Copy files to Snowball or start DataSync batch task.",
            "Ship Snowball device to AWS or monitor DataSync progress.",
            "Import files into target storage (S3, EFS, FSx).",
            "Validate file integrity and permissions.",
            "Switch access to target storage."
        ]
        downtime_exp = "Moderate (hours to days, depending on transfer size)"
        cost = "Snowball device fee or DataSync transfer costs."
        monitoring = "Monitor transfer logs and CloudWatch metrics."
        rollback = "Retain source files until migration is validated."
    elif bandwidth < 100:
        tool = "AWS Storage Gateway or DataSync (scheduled)"
        service = "AWS Storage Gateway, AWS DataSync"
        plan = "Use Storage Gateway or schedule DataSync during off-peak hours. Validate files after migration."
        steps = [
            "Deploy Storage Gateway or DataSync agent.",
            "Configure source and target locations.",
            "Schedule migration during low network usage.",
            "Monitor transfer progress.",
            "Validate files and permissions.",
            "Switch access to target storage."
        ]
        downtime_exp = "High (hours, depending on transfer speed)"
        cost = "Gateway or DataSync usage fees."
        monitoring = "Monitor transfer logs and CloudWatch metrics."
        rollback = "Retain source files for rollback if needed."
    else:
        tool = "AWS DataSync (one-time)"
        service = "AWS DataSync"
        plan = "Use AWS DataSync for one-time file migration. Validate files after transfer."
        steps = [
            "Deploy DataSync agent.",
            "Configure source and destination.",
            "Start migration task.",
            "Monitor progress and validate files.",
            "Switch access to target storage."
        ]
        downtime_exp = "Low to moderate (minutes to hours)"
        cost = "DataSync transfer costs."
        monitoring = "Monitor DataSync task and CloudWatch metrics."
        rollback = "Retain source files until migration is validated."
    return tool, service, plan, steps, downtime_exp, cost, monitoring, rollback