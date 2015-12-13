/* database creation */
create database if not exists r_db;

create table if not exists all_threads(id int not null auto_increment,
    year int not null,
    title varchar(500) not null,
    num_of_comments int not null,
    num_of_upvotes int not null,
    source varchar(100) not null,
    subreddit varchar(50) not null,
    primary key (id,year))
    partition by range (year)
    ( partition p0 values less than (2011),
      partition p1 values less than (2012),
      partition p2 values less than (2013),
      partition p3 values less than (2014),
      partition p4 values less than (2015),
    partition p5 values less than (MAXVALUE));
