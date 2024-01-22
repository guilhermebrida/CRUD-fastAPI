
CREATE TABLE IF NOT EXISTS public.cadastro
(
    "Nome" text COLLATE pg_catalog."default" NOT NULL,
    "Sobrenome" text COLLATE pg_catalog."default" NOT NULL,
    "Email" text COLLATE pg_catalog."default" NOT NULL,
    "CPF" bigint,
    reception_datetime timestamp with time zone DEFAULT timezone('America/Sao_Paulo', now())
    );

    insert into cadastro ("Nome", "Sobrenome", "Email", "CPF") values ('Guilherme', 'Brida', 'guilherme@brida.com', 12345678900);