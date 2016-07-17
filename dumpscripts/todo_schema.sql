-- Schema per gli esempi dell'applicazione to-do.

-- I progetti sono le attività di alto livello composte da compiti
create table progetto (
    nome        text primary key,
    descrizione text,
    scadenza    date
);

-- I compiti sono le attività che possono essere svolte per completare un progetto

create table compito (
    id            integer primary key autoincrement not null,
    priorita      integer default 1,
    dettagli      text,
    stato         text,
    scadenza      date,
    completato_il date,
    progetto      text not null references project(name)
);
