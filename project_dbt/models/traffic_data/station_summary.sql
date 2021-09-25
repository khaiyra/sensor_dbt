{{ config(materialized='table') }}

SELECT ID, flow_99, flow_max, flow_median, flow_total, n_obs
FROM sensor.StationSummary