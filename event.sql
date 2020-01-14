CREATE TABLE events (
  id              INT           NOT NULL    AUTO_INCREMENT,
  img             VARCHAR(300)  NOT NULL,
  title           VARCHAR(50)   NOT NULL,
  link            VARCHAR(300)  NOT NULL,
  description     TEXT          NOT NULL,
  start_date      DATE          NOT NULL,
  end_date        DATE          NOT NULL,
  display_date    VARCHAR(50)          NOT NULL,
  location        VARCHAR(100)          NOT NULL,
  note            VARCHAR(1000),
  category        ENUM("music", "visual_art", "market", "theater") NOT NULL,
  reporter_name   VARCHAR(20)   NOT NULL,
  reporter_email  VARCHAR(100)   NOT NULL,
  reporter_phone  VARCHAR(20),
  region          VARCHAR(10)   NOT NULL,
  home_banner     boolean                   DEFAULT 0,
  category_banner boolean                   DEFAULT 0,
  show_banner     boolean                   DEFAULT 0,
  status          boolean                   DEFAULT 0,
  created_at      TIMESTAMP     NOT NULL    DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY( id )
);

INSERT INTO events
  (
  img,
  title,
  link,
  description,
  start_date,
  end_date,
  display_date,
  location,
  category,
  reporter_name,
  reporter_email,
  reporter_phone,
  region,
  status
)
VALUES
(
  "https://satellite-l5yx88bg3.now.sh/fakePics/1.jpeg",
  "10 Urban Nomad Freakout Music Fest | 2019 遊牧怪奇音樂祭",
  "https://accupass",
  "10氣可價著高告別，了進個假時雖父馬算水：那省線山兒飛了：樣個不不縣有用。三或物不好媽蘭車者不能於了日去因公流平斯作研車火整委評金……的計規今應取事白相萬日香微支還味說精文地友位一記灣業常品喜初？化現愛們點這苦。數府是底稱子現玩園然，此成專定聞",
  "2019-10-01",
  "2019-11-10",
  "11/20（一）、11/30（一）、12/5 （一）",
  "新光三越 台北信義新天地(台北市台北市信義區松高路19號)",
  "theater",
  "投稿人姓名",
  "linroex@coder.tw",
  "0930330321",
  "北部",
  0
);