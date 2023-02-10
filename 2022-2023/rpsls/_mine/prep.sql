# create database if not exists swp_rubner_rpsls;
# use swp_rubner_rpsls;
create table if not exists t_hands(
	id int, 
    name varchar(255),
    primary key(id)
);
create table if not exists t_stats(
	id int auto_increment,
    user_name varchar(255),
    user_hand_id int,
    com_hand_id int,
    has_user_won bool,
    primary key(id),
    foreign key(user_hand_id) references t_hands(id),
    foreign key(com_hand_id) references t_hands(id)
);

create table if not exists rpsls_flask(
	name varchar(255),
    hand varchar(255),
    amount int,
    primary key(name, hand)
);