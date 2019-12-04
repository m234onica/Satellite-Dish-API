USE testDB;
-- CREATE TABLE events(
--   id              INT           NOT NULL    AUTO_INCREMENT,
--   img             VARCHAR(100)  NOT NULL,
--   title           VARCHAR(50)   NOT NULL,
--   link            VARCHAR(100)  NOT NULL,
--   desc            TEXT          NOT NULL,
--   created_at      TIMESTAMP     NOT NULL    DEFAULT CURRENT_TIMESTAMP,
--   start_date      DATE          NOT NULL,
--   end_date        DATE          NOT NULL,
--   display_date    TEXT          NOT NULL,
--   location        TEXT          NOT NULL,
--   note            TEXT,
--   category        ENUM("music", "visual_art", "market", "theater") NOT NULL,
--   reporter_name   VARCHAR(20)   NOT NULL,
--   reporter_email  VARCHAR(50)   NOT NULL,
--   reporter_phone  VARCHAR(20)   NOT NULL    UNIQUE,
--   PRIMARY KEY( id )
-- );

INSERT INTO events
  (
  img,

le,
  link,
  `desc`,
  start_date,
  end_date,
  display_date,
  location,
  category,
  reporter_name,
  reporter_email,
  reporter_phone
  )
VALUES
(
  "https://satellite-l5yx88bg3.now.sh/fakePics/1.jpeg",
  "Urban Nomad Freakout Music Fest | 2019 遊牧怪奇音樂祭",
  "https://accupass",
  "氣可價著高告別，了進個假時雖父馬算水：那省線山兒飛了：樣個不不縣有用。三或物不好媽蘭車者不能於了日去因公流平斯作研車火整委評金……的計規今應取事白相萬日香微支還味說精文地友位一記灣業常品喜初？化現愛們點這苦。數府是底稱子現玩園然，此成專定聞",
  "2019-11-01",
  "2019-12-10",
  "11/20（一）、11/30（一）、12/5 （一）",
  "新光三越 台北信義新天地(台北市台北市信義區松高路19號)",
  "market",
  "投稿人姓名",
  "linroex@coder.tw",
  "0930330425"
  );
