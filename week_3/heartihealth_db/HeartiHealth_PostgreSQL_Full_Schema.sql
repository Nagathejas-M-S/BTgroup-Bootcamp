-- PostgreSQL Compatible Schema
-- Converted from MySQL

-- -----------------------------------------------------
-- Table memberinfo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS memberinfo (
  member_id VARCHAR(45) NOT NULL,
  username VARCHAR(45) NULL DEFAULT NULL,
  firstname VARCHAR(45) NULL DEFAULT NULL,
  lastname VARCHAR(45) NULL DEFAULT NULL,
  age INTEGER NULL DEFAULT NULL,
  gender VARCHAR(45) NULL DEFAULT NULL,
  email VARCHAR(45) NULL DEFAULT NULL,
  phonenumber BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (member_id)
);

-- -----------------------------------------------------
-- Table addressinfo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS addressinfo (
  address_id VARCHAR(45) NOT NULL,
  city VARCHAR(45) NULL DEFAULT NULL,
  state VARCHAR(45) NULL DEFAULT NULL,
  country VARCHAR(45) NULL DEFAULT NULL,
  pincode VARCHAR(45) NULL DEFAULT NULL,
  memberinfo_member_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (address_id, memberinfo_member_id),
  CONSTRAINT fk_addressinfo_memberinfo
    FOREIGN KEY (memberinfo_member_id)
    REFERENCES memberinfo (member_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_addressinfo_memberinfo_idx ON addressinfo (memberinfo_member_id);

-- -----------------------------------------------------
-- Table cardiodiagnosis
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS cardiodiagnosis (
  cardio_id VARCHAR(45) NOT NULL,
  cardioarrestdetected INTEGER NULL DEFAULT NULL,
  date TIMESTAMP NULL DEFAULT NULL,
  memberinfo_member_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (cardio_id, memberinfo_member_id),
  CONSTRAINT fk_cardiodiagnosis_memberinfo1
    FOREIGN KEY (memberinfo_member_id)
    REFERENCES memberinfo (member_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT uk_cardio_id UNIQUE (cardio_id)
);

CREATE INDEX IF NOT EXISTS fk_cardiodiagnosis_memberinfo1_idx ON cardiodiagnosis (memberinfo_member_id);

-- -----------------------------------------------------
-- Table bloodtest
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS bloodtest (
  blood_id VARCHAR(45) NOT NULL,
  date TIMESTAMP NULL DEFAULT NULL,
  bloodpressure INTEGER NULL DEFAULT NULL,
  fbs INTEGER NULL DEFAULT NULL,
  thal INTEGER NULL DEFAULT NULL,
  serumcholesterol INTEGER NULL DEFAULT NULL,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (blood_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_bloodtest_cardiodiagnosis1
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis (cardio_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_bloodtest_cardiodiagnosis1_idx ON bloodtest (cardiodiagnosis_cardio_id);

-- -----------------------------------------------------
-- Table diseasedetail
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS diseasedetail (
  disease_id VARCHAR(45) NOT NULL,
  diagnoseddate TIMESTAMP NULL DEFAULT NULL,
  recovereddate TIMESTAMP NULL DEFAULT NULL,
  isrecovered BOOLEAN NULL DEFAULT NULL,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (disease_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_dieseasedetail_cardiodiagnosis1
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis (cardio_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_dieseasedetail_cardiodiagnosis1_idx ON diseasedetail (cardiodiagnosis_cardio_id);

-- -----------------------------------------------------
-- Table ecgreport
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ecgreport (
  ecg_id VARCHAR(45) NOT NULL,
  date TIMESTAMP NULL DEFAULT NULL,
  restecg INTEGER NULL DEFAULT NULL,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (ecg_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_ecgreport_cardiodiagnosis1
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis (cardio_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_ecgreport_cardiodiagnosis1_idx ON ecgreport (cardiodiagnosis_cardio_id);

-- -----------------------------------------------------
-- Table symptom
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS symptom (
  symptom_id VARCHAR(45) NOT NULL,
  date TIMESTAMP NULL DEFAULT NULL,
  exang INTEGER NULL DEFAULT NULL,
  oldpeak REAL NULL DEFAULT NULL,
  cp INTEGER NULL DEFAULT NULL,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (symptom_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_symptom_cardiodiagnosis1
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis (cardio_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_symptom_cardiodiagnosis1_idx ON symptom (cardiodiagnosis_cardio_id);

-- -----------------------------------------------------
-- Table wearabledevicedata
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS wearabledevicedata (
  wearable_device_id VARCHAR(45) NOT NULL,
  thalach INTEGER NULL DEFAULT NULL,
  slope INTEGER NULL DEFAULT NULL,
  date TIMESTAMP NULL DEFAULT NULL,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (wearable_device_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_wearabledevicedata_cardiodiagnosis1
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis (cardio_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_wearabledevicedata_cardiodiagnosis1_idx ON wearabledevicedata (cardiodiagnosis_cardio_id);

-- -----------------------------------------------------
-- Table xray
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS xray (
  xray_id VARCHAR(45) NOT NULL,
  date TIMESTAMP NULL DEFAULT NULL,
  ca INTEGER NULL DEFAULT NULL,
  cardiodiagnosis_cardio_id VARCHAR(45) NOT NULL,
  PRIMARY KEY (xray_id, cardiodiagnosis_cardio_id),
  CONSTRAINT fk_xray_cardiodiagnosis1
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis (cardio_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE INDEX IF NOT EXISTS fk_xray_cardiodiagnosis1_idx ON xray (cardiodiagnosis_cardio_id);