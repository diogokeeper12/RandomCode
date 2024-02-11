CREATE TABLE galaxy (
    galaxy_id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(60) NOT NULL UNIQUE,
    description TEXT,
    habitable BOOLEAN NOT NULL,
    yearOfDiscovery INT NOT NULL,
    distance NUMERIC(10,2) NOT NULL
);

CREATE TABLE star(
  star_id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(60) NOT NULL UNIQUE,
  description TEXT,
  yearOfDiscovery INT NOT NULL,
  years INT NOT NULL,
  galaxy_id INT REFERENCES galaxy(galaxy_id)
);

CREATE TABLE planet(
  planet_id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(60) NOT NULL UNIQUE,
  description TEXT,
  yearOfDiscovery INT NOT NULL,
  years INT NOT NULL,
  star_id INT REFERENCES star(star_id)
);

CREATE TABLE moon(
  moon_id SERIAL PRIMARY KEY NOT NULL,
  name VARCHAR(60) NOT NULL UNIQUE,
  description TEXT,
  yearOfDiscovery INT NOT NULL,
  years INT NOT NULL,
  planet_id INT REFERENCES planet(planet_id)
);


