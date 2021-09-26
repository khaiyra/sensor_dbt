
  create view `sensor`.`station_model2__dbt_tmp` as (
    select * 
from `sensor`.`station_summary`
where ID = 1
  );
