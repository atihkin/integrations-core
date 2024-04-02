# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

import copy
import functools

from datadog_checks.base.config import is_affirmative

from .base import SqlserverDatabaseMetricsBase

DB_FRAGMENTATION_QUERY = {
    "name": "sys.dm_db_index_physical_stats",
    "query": """SELECT
        DB_NAME(DDIPS.database_id) as database_name,
        OBJECT_NAME(DDIPS.object_id, DDIPS.database_id) as object_name,
        DDIPS.index_id as index_id,
        I.name as index_name,
        DDIPS.fragment_count as fragment_count,
        DDIPS.avg_fragment_size_in_pages as avg_fragment_size_in_pages,
        DDIPS.page_count as page_count,
        DDIPS.avg_fragmentation_in_percent as avg_fragmentation_in_percent
        FROM sys.dm_db_index_physical_stats (DB_ID('{db}'),null,null,null,null) as DDIPS
        INNER JOIN sys.indexes as I ON I.object_id = DDIPS.object_id
        AND DDIPS.index_id = I.index_id
        WHERE DDIPS.fragment_count is not null
    """,
    "columns": [
        {"name": "database_name", "type": "tag"},
        {"name": "object_name", "type": "tag"},
        {"name": "index_id", "type": "tag"},
        {"name": "index_name", "type": "tag"},
        {"name": "database.fragment_count", "type": "gauge"},
        {"name": "database.avg_fragment_size_in_pages", "type": "gauge"},
        {"name": "database.index_page_count", "type": "gauge"},
        {"name": "database.avg_fragmentation_in_percent", "type": "gauge"},
    ],
}


class SqlserverDBFragmentationMetrics(SqlserverDatabaseMetricsBase):
    # sys.dm_db_index_physical_stats
    #
    # Returns size and fragmentation information for the data and
    # indexes of the specified table or view in SQL Server.
    #
    # There are reports of this query being very slow for large datasets,
    # so debug query timing are included to help monitor it.
    # https://dba.stackexchange.com/q/76374
    #
    # https://docs.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-index-physical-stats-transact-sql?view=sql-server-ver15
    @property
    def include_db_fragmentation_metrics(self):
        return is_affirmative(self.instance_config.get('include_db_fragmentation_metrics', False))

    @property
    def db_fragmentation_object_names(self):
        return self.instance_config.get('db_fragmentation_object_names', [])

    @property
    def enabled(self):
        if not self.include_db_fragmentation_metrics:
            return False
        return True

    @property
    def queries(self):
        return [DB_FRAGMENTATION_QUERY]

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"enabled={self.enabled}, "
            f"include_db_fragmentation_metrics={self.include_db_fragmentation_metrics}, "
            f"db_fragmentation_object_names={self.db_fragmentation_object_names})"
        )

    @property
    def query_executors(self):
        executors = []
        for database in self.databases:
            queries = copy.deepcopy(self.queries)
            for query in queries:
                query['query'] = query['query'].format(db=database)
                if self.db_fragmentation_object_names:
                    query['query'] += " AND OBJECT_NAME(DDIPS.object_id, DDIPS.database_id) IN ({})".format(
                        ','.join(["'{}'".format(name) for name in self.db_fragmentation_object_names])
                    )
            executor = self.new_query_executor(
                queries,
                executor=functools.partial(self.execute_query_handler, db=database),
                extra_tags=['db:{}'.format(database)],
            )
            executor.compile_queries()
            executors.append(executor)
        return executors