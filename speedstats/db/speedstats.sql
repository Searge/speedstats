CREATE TABLE "User" (
  "UserID" VARCHAR(12) UNIQUE PRIMARY KEY NOT NULL,
  "Hostname" VARCHAR(253),
  "Machine" VARCHAR(16),
  "City" VARCHAR(86),
  "Country" VARCHAR(2)
);

CREATE TABLE "ISP" (
  "ID" SERIAL PRIMARY KEY,
  "Name" VARCHAR(52),
  "ISP_Rating" REAL,
  "Latitude" REAL,
  "Longtitude" REAL,
  "City" VARCHAR,
  "Country" VARCHAR(2),
  "IP" VARCHAR(16)
);

CREATE TABLE "Sponsor" (
  "ID" INTEGER UNIQUE PRIMARY KEY NOT NULL,
  "Host" VARCHAR,
  "Sponsor" VARCHAR(72),
  "Latitude" REAL,
  "Longtitude" REAL,
  "City" VARCHAR,
  "Country" VARCHAR(2)
);

CREATE TABLE "Client" (
  "UserID" VARCHAR PRIMARY KEY,
  "ISP" VARCHAR,
  "Sponsor" VARCHAR,
  "Distanse" REAL,
  "Timestamp" TIMESTAMP DEFAULT NOT NULL
);

CREATE TABLE "Countries" (
  "code" VARCHAR(2) UNIQUE PRIMARY KEY NOT NULL,
  "name" VARCHAR
);

CREATE TABLE "Data" (
  "Timestamp" TIMESTAMP DEFAULT PRIMARY KEY,
  "Ping" REAL,
  "Download" REAL,
  "Upload" REAL,
  "bytes_received" INTEGER,
  "bytes_sent" INTEGER
);

ALTER TABLE "User" ADD FOREIGN KEY ("Country") REFERENCES "Countries" ("code");

ALTER TABLE "ISP" ADD FOREIGN KEY ("Country") REFERENCES "Countries" ("code");

ALTER TABLE "Sponsor" ADD FOREIGN KEY ("Country") REFERENCES "Countries" ("code");

ALTER TABLE "Client" ADD FOREIGN KEY ("UserID") REFERENCES "User" ("UserID");

ALTER TABLE "Client" ADD FOREIGN KEY ("Sponsor") REFERENCES "Sponsor" ("Sponsor");

ALTER TABLE "Client" ADD FOREIGN KEY ("Timestamp") REFERENCES "Data" ("Timestamp");

ALTER TABLE "Client" ADD FOREIGN KEY ("ISP") REFERENCES "ISP" ("Name");
