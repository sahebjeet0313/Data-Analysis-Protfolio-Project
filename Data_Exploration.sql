use covid19;
select * from covid_deaths order by 3,4;
select * from covid_vaccinations order by 3,4;
select location,date,total_cases,new_cases,total_deaths,population_density
from covid_deaths order by 1,2;

select distinct continent from covid_deaths where continent is not null;
-- looking at total cases vs total death
select location,date,total_cases,total_deaths,population, (total_deaths/total_cases)*100 as death_percentage
from covid_deaths where location like '%a%' order by 1,2;

-- looking at total cases vs population
select location,date,total_cases,total_deaths,population, (total_cases/population)*100 as case_population
from covid_deaths where location like 'a%' order by 1,2;

-- looking at countries with highest infection rate compared to population
select location,population,max(total_cases) as highest_infect
from covid_deaths group by location,population order by 1,2;

-- showing countries with highest deathcount per population
select location,population, max(total_deaths) as highest_death
from covid_deaths where continent is not null group by location,population;

-- seeing deathcount per continent
select distinct continent,population,max(total_deaths) as highest_death
from covid_deaths where continent is not null group by continent,population;

select distinct continent,max(total_deaths) as highest_death
from covid_deaths where continent is not null group by continent;

-- global numbers
select date,sum(new_cases) as new_cases_per_date,sum(new_deaths) as new_deaths_per_date
from covid_deaths group by date;

select date,sum(new_cases) as new_cases_per_date,sum(new_deaths) as new_deaths_per_date,
(sum(new_deaths)/sum(new_cases))*100 as new_death_percentage
from covid_deaths group by date;

-- using both table usnig joins
select * from covid_deaths d join covid_vaccinations v on d.location = v.location and d.date = v.date;

select d.continent,d.location,d.date,d.population,v.new_vaccinations
from covid_deaths d join covid_vaccinations v on d.location = v.location and d.date = v.date
where d.continent is not null
order by 1,2,3,4; 

-- use of partition by
select d.continent,d.location,d.date,d.population,v.new_vaccinations,
sum(v.new_vaccinations) over (partition by d.location order by d.location,d.date) as p_location
from covid_deaths d join covid_vaccinations v on d.location = v.location and d.date = v.date
where d.continent is not null
order by 1,2,3,4; 

-- use of cte
with popvsvac (continent,location,date,population,new_vaccinations,p_location)
as
(
select d.continent,d.location,d.date,d.population,v.new_vaccinations,
sum(v.new_vaccinations) over (partition by d.location order by d.location,d.date) as p_location
from covid_deaths d join covid_vaccinations v on d.location = v.location and d.date = v.date
where d.continent is not null
order by 1,2,3,4)
select * from popvsvac;

-- use of temp table
create temporary table percent_population_vaccinated
( continent varchar(30), location varchar(20), date datetime, population numeric, new_vaccinations numeric, p_location numeric);

insert into percent_population_vaccination 
select d.continent,d.location,d.date,d.population,v.new_vaccinations,
sum(v.new_vaccinations) over (partition by d.location order by d.location,d.date) as p_location
from covid_deaths d join covid_vaccinations v on d.location = v.location and d.date = v.date
where d.continent is not null;