# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.cockroachdb.metrics import METRIC_MAP
from datadog_checks.dev import get_docker_hostname
from datadog_checks.dev.utils import get_metadata_metrics

HOST = get_docker_hostname()
PORT = '8080'

COCKROACHDB_VERSION = os.getenv('COCKROACHDB_VERSION')

KNOWN_HISTOGRAMS = {
    'admission_wait_durations_kv',
    'admission_wait_durations_kv_stores',
    'admission_wait_durations_sql_leaf_start',
    'admission_wait_durations_sql_sql_response',
    'admission_wait_durations_sql_kv_response',
    'admission_wait_durations_sql_root_start',
    'liveness_heartbeatlatency',
    'sql.conn.latency',
    'sql.txn.latency',
}

KNOWN_COUNTERS = {
    'addsstable_applications',
    'addsstable_copies',
    'addsstable_proposals',
    'compactor_compactingnanos',
    'compactor_compactions_failure',
    'compactor_compactions_success',
    'compactor_suggestionbytes_compacted',
    'compactor_suggestionbytes_skipped',
    'distsender_batches',
    'distsender_batches_partial',
    'distsender_errors_notleaseholder',
    'distsender_rpc_sent',
    'distsender_rpc_sent_local',
    'distsender_rpc_sent_nextreplicaerror',
    'exec_error',
    'exec_success',
    'gossip_bytes_received',
    'gossip_bytes_sent',
    'gossip_connections_refused',
    'gossip_infos_received',
    'gossip_infos_sent',
    'leases_error',
    'leases_success',
    'leases_transfers_error',
    'leases_transfers_success',
    'liveness_epochincrements',
    'liveness_heartbeatfailures',
    'liveness_heartbeatsuccesses',
    'queue_consistency_process_failure',
    'queue_consistency_process_success',
    'queue_consistency_processingnanos',
    'queue_gc_info_abortspanconsidered',
    'queue_gc_info_abortspangcnum',
    'queue_gc_info_abortspanscanned',
    'queue_gc_info_intentsconsidered',
    'queue_gc_info_intenttxns',
    'queue_gc_info_numkeysaffected',
    'queue_gc_info_pushtxn',
    'queue_gc_info_resolvesuccess',
    'queue_gc_info_resolvetotal',
    'queue_gc_info_transactionspangcaborted',
    'queue_gc_info_transactionspangccommitted',
    'queue_gc_info_transactionspangcpending',
    'queue_gc_info_transactionspanscanned',
    'queue_gc_process_failure',
    'queue_gc_process_success',
    'queue_gc_processingnanos',
    'queue_raftlog_process_failure',
    'queue_raftlog_process_success',
    'queue_raftlog_processingnanos',
    'queue_raftsnapshot_process_failure',
    'queue_raftsnapshot_process_success',
    'queue_raftsnapshot_processingnanos',
    'queue_replicagc_process_failure',
    'queue_replicagc_process_success',
    'queue_replicagc_processingnanos',
    'queue_replicagc_removereplica',
    'queue_replicate_addreplica',
    'queue_replicate_process_failure',
    'queue_replicate_process_success',
    'queue_replicate_processingnanos',
    'queue_replicate_rebalancereplica',
    'queue_replicate_removedeadreplica',
    'queue_replicate_removereplica',
    'queue_replicate_transferlease',
    'queue_split_process_failure',
    'queue_split_process_success',
    'queue_split_processingnanos',
    'queue_tsmaintenance_process_failure',
    'queue_tsmaintenance_process_success',
    'queue_tsmaintenance_processingnanos',
    'raft_commandsapplied',
    'raft_process_tickingnanos',
    'raft_process_workingnanos',
    'raft_rcvd_app',
    'raft_rcvd_appresp',
    'raft_rcvd_dropped',
    'raft_rcvd_heartbeat',
    'raft_rcvd_heartbeatresp',
    'raft_rcvd_prevote',
    'raft_rcvd_prevoteresp',
    'raft_rcvd_prop',
    'raft_rcvd_snap',
    'raft_rcvd_timeoutnow',
    'raft_rcvd_transferleader',
    'raft_rcvd_vote',
    'raft_rcvd_voteresp',
    'raft_ticks',
    'raftlog_truncated',
    'range_adds',
    'range_raftleadertransfers',
    'range_removes',
    'range_snapshots_generated',
    'range_snapshots_normal_applied',
    'range_snapshots_preemptive_applied',
    'range_splits',
    'schedules_BACKUP_failed',
    'schedules_BACKUP_started',
    'schedules_BACKUP_succeeded',
    'sql_bytesin',
    'sql_bytesout',
    'sql_ddl_count',
    'sql_delete_count',
    'sql_distsql_flows_total',
    'sql_distsql_queries_total',
    'sql_distsql_select_count',
    'sql_insert_count',
    'sql_misc_count',
    'sql_query_count',
    'sql_select_count',
    'sql_txn_abort_count',
    'sql_txn_begin_count',
    'sql_txn_commit_count',
    'sql_txn_rollback_count',
    'sql_update_count',
    'timeseries_write_bytes',
    'timeseries_write_errors',
    'timeseries_write_samples',
    'tscache_skl_read_rotations',
    'tscache_skl_write_rotations',
    'txn_abandons',
    'txn_aborts',
    'txn_autoretries',
    'txn_commits',
    'txn_commits1PC',
    'txn_restarts_deleterange',
    'txn_restarts_possiblereplay',
    'txn_restarts_serializable',
    'txn_restarts_writetooold',
    'admission_wait_sum_kv',
    'admission_wait_sum_kv_stores',
    'admission_wait_sum_sql_kv_response',
    'admission_wait_sum_sql_sql_response',
    'changefeed_emitted_messages',
    'changefeed_error_retries',
    'changefeed_failures',
    'jobs_changefeed_resume_retry_error',
    'sql_distsql_contended_queries_count',
    'sql_failure_count',
    'sql_full_scan_count',
    'admission_admitted_sql_sql_response',
    'admission_admitted_sql_leaf_start',
    'admission_wait_sum_sql_leaf_start',
    'admission_requested_kv',
    'admission_requested_kv_stores',
    'admission_errored_sql_root_start',
    'admission_errored_kv',
    'admission_requested_sql_leaf_start',
    'admission_errored_sql_leaf_start',
    'admission_wait_sum_sql_root_start',
    'admission_admitted_kv',
    'admission_admitted_sql_kv_response',
    'admission_admitted_sql_root_start',
    'admission_granter_io_tokens_exhausted_duration_kv',
    'admission_requested_sql_sql_response',
    'admission_errored_sql_kv_response',
    'admission_requested_sql_kv_response',
    'admission_errored_kv_stores',
    'admission_requested_sql_root_start',
    'admission_errored_sql_sql_response',
    'admission_admitted_kv_stores',
    'jobs_backup_fail_or_cancel_completed',
    'jobs_backup_fail_or_cancel_retry_error',
    'jobs_backup_fail_or_cancel_failed',
    'jobs_backup_resume_failed',
    'jobs_backup_resume_retry_error',
    'jobs_backup_resume_completed',
    'rebalancing_queriespersecond',
    'range_merges',
    'sql_new_conns',
    'txnwaitqueue_deadlocks_total',
    'txn_restarts_writetoooldmulti',
    'txn_restarts_unknown',
    'txn_restarts_txnpush',
    'txn_restarts_txnaborted',
    'jobs_auto_create_stats_resume_failed',
    'changefeed_emitted_bytes',
    'jobs_row_level_ttl_resume_completed',
    'jobs_row_level_ttl_resume_failed',
    'jobs_row_level_ttl_rows_selected',
    'jobs_row_level_ttl_rows_deleted',
    'schedules_scheduled_row_level_ttl_executor_failed',
}

EXPECTED_METRICS = []
for raw_metric_name, metric_name in METRIC_MAP.items():
    if raw_metric_name in KNOWN_HISTOGRAMS or raw_metric_name.endswith(('_durations', '_latency', '_max', '_restarts')):
        metric_name += '.bucket'
    elif raw_metric_name in KNOWN_COUNTERS and not metric_name.endswith('.count'):
        metric_name += '.count'

    EXPECTED_METRICS.append(metric_name)


def assert_metrics(aggregator):
    metadata_metrics = get_metadata_metrics()
    for metric in EXPECTED_METRICS:
        aggregator.assert_metric('cockroachdb.{}'.format(metric), at_least=0)

    # Custom transformer
    aggregator.assert_metric('cockroachdb.build.timestamp')

    aggregator.assert_metrics_using_metadata(metadata_metrics, check_submission_type=True)

    assert aggregator.metrics_asserted_pct > 80, 'Missing metrics {}'.format(aggregator.not_asserted())
