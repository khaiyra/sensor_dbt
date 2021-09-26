

  create  table
    `sensor`.`station_summary__dbt_tmp`
  as (
    

SELECT * FROM sensor.StationSummary
  )
