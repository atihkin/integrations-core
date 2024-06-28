# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

SQL_95TH_PERCENTILE = """SELECT `avg_us`, `ro` as `percentile` FROM
(SELECT `avg_us`, @rownum := @rownum + 1 as `ro` FROM
    (SELECT ROUND(avg_timer_wait / 1000000) as `avg_us`
        FROM performance_schema.events_statements_summary_by_digest
        ORDER BY `avg_us` ASC) p,
    (SELECT @rownum := 0) r) q
WHERE q.`ro` > ROUND(.95*@rownum)
ORDER BY `percentile` ASC
LIMIT 1"""

SQL_QUERY_TABLE_ROWS_STATS = """\
SELECT table_schema, table_name, rows_read, rows_changed
FROM information_schema.table_statistics"""

SQL_QUERY_SCHEMA_SIZE = """\
SELECT table_schema, IFNULL(SUM(data_length+index_length)/1024/1024,0) AS total_mb
FROM information_schema.tables
GROUP BY table_schema"""

SQL_QUERY_TABLE_SIZE = """\
SELECT table_schema, table_name,
 IFNULL(index_length/1024/1024,0) AS index_size_mb,
 IFNULL(data_length/1024/1024,0) AS data_size_mb
FROM information_schema.tables
WHERE table_schema not in ('mysql', 'performance_schema', 'information_schema')"""

SQL_QUERY_SYSTEM_TABLE_SIZE = """\
SELECT table_schema, table_name,
 IFNULL(index_length/1024/1024,0) AS index_size_mb,
 IFNULL(data_length/1024/1024,0) AS data_size_mb
FROM information_schema.tables
WHERE table_schema in ('mysql', 'performance_schema', 'information_schema')"""

SQL_AVG_QUERY_RUN_TIME = """\
SELECT schema_name, ROUND((SUM(sum_timer_wait) / SUM(count_star)) / 1000000) AS avg_us
FROM performance_schema.events_statements_summary_by_digest
WHERE schema_name IS NOT NULL
GROUP BY schema_name"""

SQL_WORKER_THREADS = "SELECT THREAD_ID, NAME FROM performance_schema.threads WHERE NAME LIKE '%worker'"

SQL_PROCESS_LIST = "SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE COMMAND LIKE '%Binlog dump%'"

SQL_INNODB_ENGINES = """\
SELECT engine
FROM information_schema.ENGINES
WHERE engine='InnoDB' and support != 'no' and support != 'disabled'"""

SQL_SERVER_ID_AWS_AURORA = """\
SHOW VARIABLES LIKE 'aurora_server_id'"""

SQL_REPLICATION_ROLE_AWS_AURORA = """\
SELECT IF(session_id = 'MASTER_SESSION_ID','writer', 'reader') AS replication_role
FROM information_schema.replica_host_status
WHERE server_id = @@aurora_server_id"""

SQL_GROUP_REPLICATION_MEMBER = """\
SELECT channel_name, member_state, member_role
FROM performance_schema.replication_group_members
WHERE member_id = @@server_uuid"""

SQL_GROUP_REPLICATION_METRICS = """\
SELECT channel_name,count_transactions_in_queue,count_transactions_checked,count_conflicts_detected,
count_transactions_rows_validating,count_transactions_remote_in_applier_queue,count_transactions_remote_applied,
count_transactions_local_proposed,count_transactions_local_rollback
FROM performance_schema.replication_group_member_stats
WHERE channel_name IN ('group_replication_applier', 'group_replication_recovery') AND member_id = @@server_uuid"""

SQL_GROUP_REPLICATION_PLUGIN_STATUS = """\
SELECT plugin_status
FROM information_schema.plugins WHERE plugin_name='group_replication'"""

#TODO check 'mysql', 'performance_schema', 'information_schema' - is this correct
SQL_DATABASES = """
SELECT schema_name as `name`,default_character_set_name,default_collation_name FROM information_schema.SCHEMATA
WHERE schema_name not in ('mysql', 'performance_schema', 'information_schema')"""

SQL_TABLES = """\
SELECT table_name as `name` FROM information_schema.TABLES WHERE TABLE_SCHEMA = "{}"
"""

#do we have ? that can be replaced by the driver
SQL_COLUMNS = """\
SELECT table_name, column_name as `name`, data_type, column_default as `default` , is_nullable as `nullable` ,ordinal_position
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = "{}" AND TABLE_NAME IN ({});
"""

#TODO cardinality is a dinamic property - number of unique values for an index. 
SQL_INDEXES_2 = """\
SELECT TABLE_NAME, NON_UNIQUE, INDEX_NAME, 
GROUP_CONCAT(SEQ_IN_INDEX ORDER BY SEQ_IN_INDEX ASC) as SEQ_IN_INDEX, 
GROUP_CONCAT(COLUMN_NAME ORDER BY SEQ_IN_INDEX ASC) AS COLUMNS, 
GROUP_CONCAT(SUB_PART ORDER BY SEQ_IN_INDEX ASC) AS SUB_PARTS, 
GROUP_CONCAT(PACKED ORDER BY SEQ_IN_INDEX ASC) AS PACKED, 
GROUP_CONCAT(NULLABLE ORDER BY SEQ_IN_INDEX ASC) AS NULLABLES, 
COLLATION, 
CARDINALITY, 
INDEX_TYPE,
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_SCHEMA = "{}" AND TABLE_NAME IN ({});
GROUP BY TABLE_NAME, NON_UNIQUE, INDEX_NAME, COLLATION, CARDINALITY, INDEX_TYPE
"""

SQL_INDEXES = """\
SELECT 
    table_name, 
    index_name, 
    collation,  
    cardinality,  
    index_type, 
    group_concat(seq_in_index order by seq_in_index asc) as seq_in_index,  
    group_concat(column_name order by seq_in_index asc) as columns,  
    group_concat(sub_part order by seq_in_index asc) as sub_parts,  
    group_concat(packed order by seq_in_index asc) as packed,  
    group_concat(nullable order by seq_in_index asc) as nullables,  
    group_concat(non_unique order by seq_in_index asc) as non_uniques
FROM INFORMATION_SCHEMA.STATISTICS 
WHERE TABLE_SCHEMA = "{}" AND TABLE_NAME IN ({})
GROUP BY table_name, index_name, collation, cardinality, index_type;
"""

#TODO can CONSTRAINT_SCHEMA be not equal to TABLE_SCHEMA
# TODO this is only ofr foreign keys why not other constraints i.e REFERENCED_TABLE_NAME is null
SQL_FOREIGN_KEYS = """\
SELECT
    constraint_schema,
    constraint_name,
    table_name,
    group_concat(column_name) as column_names,
    referenced_table_schema,
    referenced_table_name,
    group_concat(referenced_column_name) as referenced_column_names
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    table_schema = "{}" and table_name in ({})
    and referenced_table_name is not null
GROUP BY constraint_schema, constraint_name, table_name, referenced_table_schema, referenced_table_name;
"""

SQL_PARTITION = """\
SELECT
    table_name,
    partition_name, 
    group_concat(subpartition_name order by subpartition_ordinal_position asc) as subpartition_names,
    partition_ordinal_position,
    group_concat(subpartition_ordinal_position order by subpartition_ordinal_position asc) as subpartition_ordinal_positions, 
    partition_method, 
    group_concat(subpartition_method order by subpartition_ordinal_position asc) as subpartition_ordinal_positions, 
    partition_expression, 
    group_concat(subpartition_expression order by subpartition_ordinal_position asc) as subpartition_expressions, 
    partition_description, 
    table_rows , 
    group_concat(data_length order by subpartition_ordinal_position asc) as data_lengths, 
    group_concat(max_data_length order by subpartition_ordinal_position asc) as max_data_lengths, 
    group_concat(index_length order by subpartition_ordinal_position asc) as index_lengths, 
    group_concat(data_free order by subpartition_ordinal_position asc) as data_free,
    partition_comment, 
    tablespace_name
FROM INFORMATION_SCHEMA.PARTITIONS
WHERE
    table_schema = "{}" AND table_name in ({}) AND partition_name IS NOT NULL
GROUP BY table_name, partition_name, partition_ordinal_position, partition_method, partition_expression, partition_description, table_rows, partition_comment, tablespace_name
"""

QUERY_DEADLOCKS = {
    'name': 'information_schema.INNODB_METRICS.lock_deadlocks',
    'query': """
        SELECT
            count as deadlocks
        FROM
            information_schema.INNODB_METRICS
        WHERE
            NAME='lock_deadlocks'
    """.strip(),
    'columns': [{'name': 'mysql.innodb.deadlocks', 'type': 'monotonic_count'}],
}

QUERY_USER_CONNECTIONS = {
    'name': 'performance_schema.threads',
    'query': """
        SELECT
            COUNT(processlist_user) AS connections,
            processlist_user,
            processlist_host,
            processlist_db,
            processlist_state
        FROM
            performance_schema.threads
        WHERE
            processlist_user IS NOT NULL AND
            processlist_state IS NOT NULL
        GROUP BY processlist_user, processlist_host, processlist_db, processlist_state
    """.strip(),
    'columns': [
        {'name': 'mysql.performance.user_connections', 'type': 'gauge'},
        {'name': 'processlist_user', 'type': 'tag'},
        {'name': 'processlist_host', 'type': 'tag'},
        {'name': 'processlist_db', 'type': 'tag'},
        {'name': 'processlist_state', 'type': 'tag'},
    ],
}


def show_replica_status_query(version, is_mariadb, channel=''):
    if version.version_compatible((10, 5, 1)) or not is_mariadb and version.version_compatible((8, 0, 22)):
        base_query = "SHOW REPLICA STATUS"
    else:
        base_query = "SHOW SLAVE STATUS"
    if channel and not is_mariadb:
        return "{0} FOR CHANNEL '{1}';".format(base_query, channel)
    else:
        return "{0};".format(base_query)
