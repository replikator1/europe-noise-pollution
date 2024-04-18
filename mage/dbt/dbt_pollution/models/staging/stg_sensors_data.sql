with 

source as (

    select * from {{ source('staging', 'sensors_external') }}

),

renamed as (

    select
        *
    from source

)

select * from renamed