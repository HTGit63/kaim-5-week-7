-- dbt_project/models/staging/stg_telegram_messages.sql

with raw_data as (
    select
        *
    from {{ source('raw', 'lobelia4cosmetics') }}  -- This is the raw data source for lobelia4cosmetics
)

select
    id as message_id,
    date::timestamp as message_date,
    text as message_text,
    has_media,
    channel_name
from raw_data
