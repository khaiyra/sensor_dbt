-- Use the `ref` function to select from other models

select *
from `sensor`.`my_first_dbt_model`
where id = 1