
    
    



select count(*) as validation_errors
from (

    select
        id

    from `schema`.`my_first_dbt_model`
    where id is not null
    group by id
    having count(*) > 1

) validation_errors


