# GlassDB

## ガラス情報DB
本データベースではガラスの特性を表現する情報を格納します。  
本ドキュメントはそのDBのスキーマ等の仕様ならびに本DB作成時のメモを記述するものとします。

## ファイル
 - data
    - glass.sqlite3

## テーブル
- t_glass_spec
    - t_glass_spec_hoya
    - t_glass_spec_ohara
    - t_glass_spec_hikari
    - t_glass_spec_schott
- t_maker

## スキーマ
### t_glass_spec
ガラスごとの情報

|キー名|型|型補足|説明|
|-----|---|---|-------|
|id|INTEGER|Primary Key|ID|
|code|INTEGER||６桁の数値(%06d)|
|code_d|INTEGER||６桁の数値(%06d)|
|code_e|INTEGER||６桁の数値(%06d)|
|name|TEXT||例：BK-7|
|maker_id|TEXT||メーカーID|
|maker_name|TEXT||メーカー名|
|n2325|REAL||n2325|
|n2058|REAL||n2058|
|n1970|REAL||n1970|
|n1530|REAL||n1529.6|
|n1129|REAL||n1128.64|
|n1064|REAL||n1064|
|n1060|REAL||n1060|
|n1014|REAL||nt(1013.98)|
|n852|REAL||ns(852.11)|
|n768|REAL||nA'(768.19)|
|n707|REAL||nr(706.52)|
|n656|REAL||nC(656.27)|
|n644|REAL||nC'(643.85)|
|n633|REAL||nHe-Ne(642.80)|
|n589|REAL||nD(589.29)|
|n588|REAL||nd(587.56)|
|n546|REAL||ne(546.07)|
|n486|REAL||nF(486.13)|
|n480|REAL||nF'(479.99)|
|n436|REAL||ng(435.84)|
|n405|REAL||nh(404.66)|
|n389|REAL||n389(388.865)|
|n365|REAL||ni(365.01)|
|n334|REAL||n334(334.1)|
|n313|REAL||n313(312.6)|
|n297|REAL||n297(296.7)|
|n280|REAL||n280(280.4)|
|n248|REAL||n248(248.3)|
|---|---|---|---|
|t280|REAL||tau(280)10mmの透過率|
|t290|REAL||tau(290)|
|t300|REAL||tau(300)|
|t310|REAL||tau(310)|
|t320|REAL||tau(320)|
|t330|REAL||tau(330)|
|t340|REAL||tau(340)|
|t350|REAL||tau(350)|
|t360|REAL||tau(360)|
|t370|REAL||tau(370)|
|t380|REAL||tau(380)|
|t390|REAL||tau(390)|
|t400|REAL||tau(400)|
|t420|REAL||tau(420)|
|t440|REAL||tau(440)|
|t460|REAL||tau(440)|
|t480|REAL||tau(440)|
|t500|REAL||tau(500)|
|t550|REAL||tau(550)|
|t600|REAL||tau(600)|
|t650|REAL||tau(650)|
|t700|REAL||tau(700)|
|t750|REAL||tau(750)|
|t800|REAL||tau(800)|
|t850|REAL||tau(850)|
|t900|REAL||tau(900)|
|t950|REAL||tau(900)|
|t1000|REAL||tau(1000)|
|t1100|REAL||tau(1100)|
|t1200|REAL||tau(1200)|
|t1300|REAL||tau(1300)|
|t1400|REAL||tau(1400)|
|t1500|REAL||tau(1500)|
|t1600|REAL||tau(1600)|
|t1800|REAL||tau(1800)|
|t2000|REAL||tau(2000)|
|t2200|REAL||tau(2200)|
|t2400|REAL||tau(2400)|
|t2500|REAL||tau(2500)|

### t_maker
メーカーごと特性

|キー名|型|型補足|説明|
|-----|---|---|-------|
|id|INTEGER|Primary Key|ID|
|maker_name|TEXT||メーカー名|

## 対応メーカー
本DBで作成したガラスメーカーと元資料

|No.|メーカー名|説明|データ|
|---|---------|---|-------|
|1|Hoya|日本の光学機器・ガラスメーカー|http://www.hoya-opticalworld.com/japanese/datadownload/|
|2|Schott|ドイツ・マインツに本社を置く、光ファイバーや平面ディスプレイなどの産業用ガラスのメーカー|http://www.http://www.schott.com/advanced_optics/japanese/products/optical-materials/optical-glass/optical-glass/index.html|
|3|Ohara|日本で最初（1935年（昭和10年））に設立された光学ガラス専業メーカー|http://www.ohara-inc.co.jp/jp/product/optical/list/index.html|
|4|Hikari|日本のガラスメーカー。ニコンの子会社|http://www.hikari-g.co.jp/products/catalog.htm|
|5|CDGM||http://www.kryptronic.de/cdgm.html http://www.cdgmgd.com/en/asp/|

## 参考資料

|説明|内容|URL|
|---|---|----|
|edmundoptics|光学ガラスの技術資料|http://www.edmundoptics.jp/technical-resources-center/optics/optical-glass/|
|Glass Identification Data Set|Machine Learning　Datasets|https://archive.ics.uci.edu/ml/datasets/Glass+Identification|

## DB作成メモ
### データベースファイル作成
```bash
$sqlite3 ./data/glass.sqlite3
```
### テーブル作成
```sql
CREATE TABLE t_glass_spec (
    id INTEGER PRIMARY KEY,
    maker TEXT,
    name TEXT,
    code TEXT,
    n300 REAL,
    n310 REAL,
    n320 REAL,
    n330 REAL,
    n340 REAL,
    n350 REAL,
    n360 REAL,
    n370 REAL,
    n380 REAL,
    n390 REAL,
    n400 REAL,
    n410 REAL,
    n420 REAL,
    n430 REAL,
    n440 REAL,
    n450 REAL,
    n460 REAL,
    n470 REAL,
    n480 REAL,
    n490 REAL,
    n500 REAL,
    n510 REAL,
    n520 REAL,
    n530 REAL,
    n540 REAL,
    n550 REAL,
    n560 REAL,
    n570 REAL,
    n580 REAL,
    n590 REAL,
    n600 REAL,
    n610 REAL,
    n620 REAL,
    n630 REAL,
    n640 REAL,
    n650 REAL,
    n660 REAL,
    n670 REAL,
    n680 REAL,
    n690 REAL,
    n700 REAL,
    n710 REAL,
    n720 REAL,
    n730 REAL,
    n740 REAL,
    n750 REAL,
    n760 REAL,
    n770 REAL,
    n780 REAL,
    n790 REAL,
    n800 REAL,
    n810 REAL,
    n820 REAL,
    n830 REAL,
    n840 REAL,
    n850 REAL,
    n860 REAL,
    n870 REAL,
    n880 REAL,
    n890 REAL,
    n900 REAL,
    t300 REAL,
    t310 REAL,
    t320 REAL,
    t330 REAL,
    t340 REAL,
    t350 REAL,
    t360 REAL,
    t370 REAL,
    t380 REAL,
    t390 REAL,
    t400 REAL,
    t410 REAL,
    t420 REAL,
    t430 REAL,
    t440 REAL,
    t450 REAL,
    t460 REAL,
    t470 REAL,
    t480 REAL,
    t490 REAL,
    t500 REAL,
    t510 REAL,
    t520 REAL,
    t530 REAL,
    t540 REAL,
    t550 REAL,
    t560 REAL,
    t570 REAL,
    t580 REAL,
    t590 REAL,
    t600 REAL,
    t610 REAL,
    t620 REAL,
    t630 REAL,
    t640 REAL,
    t650 REAL,
    t660 REAL,
    t670 REAL,
    t680 REAL,
    t690 REAL,
    t700 REAL,
    t710 REAL,
    t720 REAL,
    t730 REAL,
    t740 REAL,
    t750 REAL,
    t760 REAL,
    t770 REAL,
    t780 REAL,
    t790 REAL,
    t800 REAL,
    t810 REAL,
    t820 REAL,
    t830 REAL,
    t840 REAL,
    t850 REAL,
    t860 REAL,
    t870 REAL,
    t880 REAL,
    t890 REAL,
    t900 REAL
);
```
### テーブル確認
```bash
sqlite> .table
sqlite> .explain
sqlite> .schema t_glass_spec
sqlite> SELECT * FROM t_glass_spec
```

### メーカーテーブル作成
```bash
sqlite> create table t_maker (
   ...>     id INTEGER PRIMARY KEY,
   ...>     name TEXT,
   ...>     nt REAL DEFAULT 1013.98,
   ...>     ns REAL DEFAULT 852.11,
   ...>     nr REAL DEFAULT 706.52,
   ...>     nC REAL DEFAULT 656.27,
   ...>     nD REAL DEFAULT 589.29,
   ...>     ne REAL DEFAULT 546.07,
   ...>     nF REAL DEFAULT 486.13,
   ...>     ng REAL DEFAULT 435.84,
   ...>     nh REAL DEFAULT 404.66,
   ...>     ni REAL DEFAULT 365.01
   ...> );
sqlite> INSERT INTO t_maker VALUES(null, "Hoya");
sqlite> INSERT INTO t_maker VALUES(null, "Schott");
sqlite> INSERT INTO t_maker VALUES(null, "Ohara");
sqlite> INSERT INTO t_maker VALUES(null, "Hikari");
sqlite> INSERT INTO t_maker VALUES(null, "CDGM");
```

# カラム追加
```bash
sqlite> ALTER TABLE t_maker ADD nt REAL
sqlite> ALTER TABLE t_maker ADD ns REAL
sqlite> ALTER TABLE t_maker ADD nr REAL
sqlite> ALTER TABLE t_maker ADD nC REAL
```

# レコード変更
```bash
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
UPDATE t_maker SET nt=1013.98 WHERE name="Hoya";
```

## Hoya テーブル作成
### テーブル作成
```sql
CREATE TABLE t_glass_spec_hoya (
    id INTEGER PRIMARY KEY,
    code INTEGER,
    name TEXT,
    n1530 REAL,
    n1129 REAL,
    n1014 REAL,
    n852 REAL,
    n768 REAL,
    n707 REAL,
    n656 REAL,
    n644 REAL,
    n633 REAL,
    n589 REAL,
    n588 REAL,
    n546 REAL,
    n486 REAL,
    n480 REAL,
    n436 REAL,
    n405 REAL,
    n365 REAL,
    t2500 REAL,
    t2400 REAL,
    t2200 REAL,
    t2000 REAL,
    t1800 REAL,
    t1600 REAL,
    t1550 REAL,
    t1500 REAL,
    t1400 REAL,
    t1300 REAL,
    t1200 REAL,
    t1100 REAL,
    t1060 REAL,
    t1050 REAL,
    t1000 REAL,
    t950 REAL,
    t900 REAL,
    t850 REAL,
    t830 REAL,
    t800 REAL,
    t780 REAL,
    t750 REAL,
    t700 REAL,
    t650 REAL,
    t600 REAL,
    t550 REAL,
    t500 REAL,
    t480 REAL,
    t460 REAL,
    t440 REAL,
    t420 REAL,
    t400 REAL,
    t390 REAL,
    t380 REAL,
    t370 REAL,
    t360 REAL,
    t350 REAL,
    t340 REAL,
    t330 REAL,
    t320 REAL,
    t310 REAL,
    t300 REAL,
    t290 REAL,
    t280 REAL
);
```
### インポート
```sql
sqlite> .export ./tmp/Hoya/HOYA20150615_mod3.psv t_glass_spec_hoya
```
### テーブルのコピー
```sql
sqlite> create table t_glass_spec_hoya2 as select * from t_glass_spec_hoya
```

### いらないエントリ削除
```sql
sqlite> delete from t_glass_spec_hoya2 where id in(53,82,110)
```

## Ohara テーブル作成
### テーブル作成
```sql
CREATE TABLE t_glass_spec_ohara (
    id INTEGER PRIMARY KEY,
    name TEXT,
    code INTEGER,
    code_e INTEGER,
    n2325 REAL,
    n1970 REAL,
    n1530 REAL,
    n1129 REAL,
    n1014 REAL,
    n852 REAL,
    n768 REAL, --nA'
    n707 REAL,
    n656 REAL,
    n644 REAL,
    n633 REAL,--nHe-Ne
    n589 REAL,
    n588 REAL,
    n546 REAL,
    n486 REAL,
    n480 REAL,--nF'
    n442 REAL,--nHe-Cd .44157
    n436 REAL,
    n405 REAL,
    n365 REAL,
    t280 REAL,
    t290 REAL,
    t300 REAL,
    t310 REAL,
    t320 REAL,
    t330 REAL,
    t340 REAL,
    t350 REAL,
    t360 REAL,
    t370 REAL,
    t380 REAL,
    t390 REAL,
    t400 REAL,
    t420 REAL,
    t440 REAL,
    t460 REAL,
    t480 REAL,
    t500 REAL,
    t550 REAL,
    t600 REAL,
    t650 REAL,
    t700 REAL,
    t800 REAL,
    t900 REAL,
    t1000 REAL,
    t1200 REAL,
    t1400 REAL,
    t1600 REAL,
    t1800 REAL,
    t2000 REAL,
    t2200 REAL,
    t2400 REAL
);
```
### インポート
```sql
sqlite> .import ./tmp/Ohara/OHARA20150327_modified.psv t_glass_spec_ohara
```

### テーブルのコピー
```sql
sqlite> create table t_glass_spec_ohara2 as select * from t_glass_spec_ohara
```

## Hikari テーブル作成
### テーブル作成
```sql
CREATE TABLE t_glass_spec_hikari (
    name TEXT,
    code INTEGER,
    code_e INTEGER,
    n2058 REAL,--1
    n1970 REAL,
    n1530 REAL,
    n1129 REAL,
    n1064 REAL,--5
    n1014 REAL,--6
    n852 REAL,
    n768 REAL, --nA'
    n707 REAL,
    n656 REAL,--10
    n644 REAL,--11
    n633 REAL,--nHe-Ne
    n589 REAL,
    n588 REAL,
    n546 REAL,--15
    n486 REAL,
    n480 REAL,--nF'
    n436 REAL,
    n405 REAL,--19
    n389 REAL,--0.388865
    n365 REAL,
    t280 REAL,--1
    t290 REAL,
    t300 REAL,
    t310 REAL,
    t320 REAL,--5
    t330 REAL,
    t340 REAL,
    t350 REAL,
    t360 REAL,
    t365 REAL, --10
    t370 REAL,
    t380 REAL,
    t390 REAL,
    t400 REAL,
    t420 REAL,--15
    t440 REAL,
    t460 REAL,
    t480 REAL,
    t500 REAL,
    t550 REAL,--20
    t600 REAL,
    t650 REAL,
    t700 REAL,
    t800 REAL,
    t900 REAL,--25
    t1000 REAL,
    t1200 REAL,
    t1400 REAL,
    t1600 REAL,
    t1800 REAL,--39
    t2000 REAL,
    t2200 REAL,
    t2400 REAL
);
```
### インポート
```sql
sqlite> .import ./tmp/Hikari/HIKARI_All_Catalog_Data_modified.psv t_glass_spec_hikari
```

### テーブルのコピー
```sql
sqlite> create table t_glass_spec_hikari2 as select * from t_glass_spec_hikari
```

## Schott テーブル作成
### テーブル作成
```sql
CREATE TABLE t_glass_spec_shott (
    name TEXT,
    code INTEGER,
    t2500 REAL,
    t2325 REAL,
    t1970 REAL,
    t1530 REAL,
    t1060 REAL,
    t700 REAL,
    t660 REAL,
    t620 REAL,
    t580 REAL,
    t546 REAL,
    t500 REAL,
    t460 REAL,
    t436 REAL,
    t420 REAL,
    t405 REAL,
    t400 REAL,
    t390 REAL,
    t380 REAL,
    t370 REAL,
    t365 REAL,
    t350 REAL,
    t334 REAL,
    t320 REAL,
    t310 REAL,
    t300 REAL,
    t290 REAL,
    t280 REAL,
    t270 REAL,
    t260 REAL,
    t250 REAL,
    n2325 REAL,--n2325.4
    n1970 REAL,--n1970.1
    n1530 REAL,--n1529.6
    n1060 REAL,--n1060.0
    n1014 REAL,--nt
    n852 REAL,--ns
    n706 REAL,--nr
    n656 REAL,--nC
    n643 REAL,--nC'
    n633 REAL,--n632.8
    n589 REAL,
    n588 REAL,
    n546 REAL,
    n486 REAL,
    n480 REAL,--nF'
    n436 REAL,
    n405 REAL,
    n365 REAL,
    n334 REAL,--n334.1
    n313 REAL,--n312.6
    n297 REAL,--n296.7
    n280 REAL,--n280.4
    n248 REAL--n248.3
);
```
### インポート
```sql
sqlite> .import ./tmp/Schott/schott-optical-glass-catalogue-excel-july-2015.psv t_glass_spec_shott
```

### テーブルのコピー
```sql
sqlite> create table t_glass_spec_shott2 as select * from t_glass_spec_shott
```
