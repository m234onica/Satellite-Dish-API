# Satellite-Dish-API

## TABLE events
```
id              INT           NOT NULL    AUTO_INCREMENT
img             VARCHAR(100)  NOT NULL
title           VARCHAR(50)   NOT NULL
link            VARCHAR(100)  NOT NULL
desc            TEXT          NOT NULL
created_at      TIMESTAMP     NOT NULL    DEFAULT CURRENT_TIMESTAMP
start_date      DATE          NOT NULL
end_date        DATE          NOT NULL
display_date    TEXT          NOT NULL
location        TEXT          NOT NULL
note            TEXT
category        ENUM("music", "visual_art", "market", "theatre") NOT NULL
reporter_name   VARCHAR(20)   NOT NULL
reporter_email  VARCHAR(50)   NOT NULL
reporter_phone  VARCHAR(20)   NOT NULL    UNIQUE
region          VARCHAR(10)
home_banner     boolean
category_banner boolean
status          boolean
PRIMARY KEY( id )
```


## Run project
```
python3 run.py
```
