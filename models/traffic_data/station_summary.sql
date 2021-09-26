with source as (
    select * from {{ ref('station_summary') }}
)

SELECT ID, flow_99, flow_max, flow_median, flow_total, n_obs
FROM sensor.StationSummary