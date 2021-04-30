CREATE TABLE "User" (
  "UserID" varchar UNIQUE PRIMARY KEY NOT NULL,
  "Hostname" varchar,
  "Machine" varchar,
  "City" varchar,
  "Country" varchar
);

CREATE TABLE "ISP" (
  "ID" SERIAL PRIMARY KEY,
  "Name" varchar,
  "ISP_Rating" float8,
  "Latitude" float4,
  "Longtitude" float4,
  "City" varchar,
  "Country" varchar
);

CREATE TABLE "Sponsor" (
  "Sponsor" varchar(72) PRIMARY KEY,
  "Latitude" float4,
  "Longtitude" float4,
  "City" varchar,
  "Country" varchar
);

CREATE TABLE "Client" (
  "UserID" varchar PRIMARY KEY,
  "ISP" varchar,
  "Sponsor" varchar,
  "Timestamp" timestamp
);

CREATE TABLE "Data" (
  "Timestamp" timestamp PRIMARY KEY,
  "Ping" float4,
  "Download" float4,
  "Upload" float4,
  "bytes_received" int,
  "bytes_sent" int
);

ALTER TABLE "Client" ADD FOREIGN KEY ("UserID") REFERENCES "User" ("UserID");

ALTER TABLE "Client" ADD FOREIGN KEY ("Sponsor") REFERENCES "Sponsor" ("Sponsor");

ALTER TABLE "Client" ADD FOREIGN KEY ("Timestamp") REFERENCES "Data" ("Timestamp");

ALTER TABLE "Client" ADD FOREIGN KEY ("ISP") REFERENCES "ISP" ("Name");
