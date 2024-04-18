with 

source as (

    select * from {{ source('staging', 'location_external') }}

),

renamed as (

    select
        *
    from source

)

select * from renamed