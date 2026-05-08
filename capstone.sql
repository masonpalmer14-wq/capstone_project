CREATE TABLE merch_m AS
SELECT DISTINCT
 "Country",
 "Year",
 "Value"
FROM merch_m_clean
SELECT * FROM merch_m
ORDER BY "Year";


CREATE TABLE merch_x AS
SELECT DISTINCT
 "Country",
 "Year",
 "Value"
FROM merch_x_clean
SELECT * FROM merch_x
ORDER BY "Year";


CREATE TABLE service_m AS
SELECT DISTINCT
  "Country",
  "Year",
  "Value"
FROM service_m_clean
SELECT * FROM service_m
ORDER BY "Year";


CREATE TABLE service_x AS
SELECT DISTINCT
  "Country",
  "Year",
  "Value"
FROM service_x_clean
SELECT * FROM service_x
ORDER BY "Year";


CREATE TABLE tariff AS
SELECT DISTINCT
  "Country",
  "Year",
  "Value"
FROM tariff_clean;
ALTER TABLE tariff RENAME COLUMN "Value" to Applied_Rate
SELECT * FROM tariff
ORDER BY "Year";


--------------------------------------------------------------------------------------------------------------


-- Compares US and China Exports
CREATE TABLE us_china_x AS
SELECT
  u."Year",
  u."Value" AS us_exports,
  c."Value" AS china_exports
FROM merch_x u
JOIN merch_x c ON u."Year" = c."Year"
WHERE u."Country" = 'United States of America'
AND c."Country" = 'China';
SELECT * FROM us_china_x
ORDER BY "Year"






-- Compares US and China Imports
CREATE TABLE us_china_m AS
SELECT
  a."Year",
  a."Value" AS us_imports,
  d."Value" AS china_imports
FROM merch_m a
JOIN merch_m d ON a."Year" = d."Year"
WHERE a."Country" = 'United States of America'
AND d."Country" = 'China';
SELECT * FROM us_china_m
ORDER BY "Year"




-- Calculates trade deficit of USA // Compared


CREATE TABLE deficit AS
SELECT DISTINCT
  x."Year",
  x."Value" as exports,
  m."Value" as imports,
  (x."Value"-m."Value") AS trade_deficit,
  t."applied_rate"
FROM merch_x x
JOIN merch_m m ON x."Year" = m."Year"
  AND x."Country" = m."Country"
JOIN tariff t ON x."Year" = t."Year"
  AND x."Country" = t."Country"
WHERE x."Country" = 'United States of America';
SELECT * FROM deficit
ORDER BY "Year"




CREATE TABLE import_tariff_korea AS
SELECT DISTINCT
  b."Year",
  b."Value",
  e."applied_rate"
FROM merch_m b
JOIN tariff e ON b."Year" = e."Year"
AND b."Country" = e."Country"
WHERE b."Country" = 'Korea, Republic of'
ORDER BY "Year";
SELECT * FROM import_tariff_korea




CREATE TABLE import_tariff_canada AS
SELECT DISTINCT
  f."Year",
  f."Value",
  g."applied_rate"
FROM merch_m f
JOIN tariff g ON f."Year" = g."Year"
AND f."Country" = g."Country"
WHERE f."Country" = 'Canada'
ORDER BY "Year";
SELECT * FROM import_tariff_canada


-- seeing if corelation in US-MEXICO trade
CREATE TABLE us_imports_mex_exports AS
SELECT
  a."Year",
  a."Value" AS us_imports,
  mex."Value" AS mex_exports
FROM merch_m a
JOIN merch_x mex ON a."Year" = mex."Year"
WHERE a."Country" = 'United States of America'
AND mex."Country" = 'Mexico';
SELECT * FROM us_imports_mex_exports
ORDER BY "Year"




-- service exports of developing vs developed countries


CREATE TABLE dev_comp AS
SELECT
   id."Value" AS india_service_x,
   cn."Value" AS china_service_x,
   eu."Value" AS eu_service_x
FROM service_x id
JOIN service_x cn ON id."Year" = cn."Year"
JOIN service_x eu ON id."Year" = eu."Year"
WHERE id."Country" = 'India'
 AND cn."Country" = 'China'
 AND eu."Country" = 'European Union'
 AND id."Year" = 2024;
SELECT * FROM dev_comp





