--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: astapov
--

CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    actor_lname character varying(50),
    actor_fname character varying(50),
    birth_date date
);


ALTER TABLE public.actors OWNER TO astapov;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: astapov
--

CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_actor_id_seq OWNER TO astapov;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astapov
--

ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.actor_id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: astapov
--

CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_lname character varying(50),
    director_fname character varying(50),
    birth_date date,
    films_amount smallint
);


ALTER TABLE public.directors OWNER TO astapov;

--
-- Name: directors_director_id_seq; Type: SEQUENCE; Schema: public; Owner: astapov
--

CREATE SEQUENCE public.directors_director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_director_id_seq OWNER TO astapov;

--
-- Name: directors_director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astapov
--

ALTER SEQUENCE public.directors_director_id_seq OWNED BY public.directors.director_id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: astapov
--

CREATE TABLE public.films (
    film_id integer NOT NULL,
    film_name character varying(125),
    director_lname character varying(50),
    director_fname character varying(50),
    release_year integer,
    imdb numeric
);


ALTER TABLE public.films OWNER TO astapov;

--
-- Name: films_film_id_seq; Type: SEQUENCE; Schema: public; Owner: astapov
--

CREATE SEQUENCE public.films_film_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_film_id_seq OWNER TO astapov;

--
-- Name: films_film_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: astapov
--

ALTER SEQUENCE public.films_film_id_seq OWNED BY public.films.film_id;


--
-- Name: actors actor_id; Type: DEFAULT; Schema: public; Owner: astapov
--

ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);


--
-- Name: directors director_id; Type: DEFAULT; Schema: public; Owner: astapov
--

ALTER TABLE ONLY public.directors ALTER COLUMN director_id SET DEFAULT nextval('public.directors_director_id_seq'::regclass);


--
-- Name: films film_id; Type: DEFAULT; Schema: public; Owner: astapov
--

ALTER TABLE ONLY public.films ALTER COLUMN film_id SET DEFAULT nextval('public.films_film_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: astapov
--

COPY public.actors (actor_id, actor_lname, actor_fname, birth_date) FROM stdin;
1	Chan	Jackie	1954-04-07
2	Depp	John Christopher	1963-06-09
3	Parker	Peter	1962-05-11
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: astapov
--

COPY public.directors (director_id, director_lname, director_fname, birth_date, films_amount) FROM stdin;
1	Cameron	James	1954-08-16	9
2	Whedon	Joseph Hill	1964-06-23	24
3	Bay	Michael Benjamin	1965-02-17	39
4	Verbinski	Gregor	1964-03-16	13
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: astapov
--

COPY public.films (film_id, film_name, director_lname, director_fname, release_year, imdb) FROM stdin;
1	Pirates of the Caribbean	Verbinski	Gregor	2007	8.1
2	Avengers	Whedon	Joseph Hill	2012	8
3	Transformers	Bay	Michael Benjamin	2007	7
4	Sherlock Holmes	Ritchie	Guy	2009	7.6
\.


--
-- Name: actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astapov
--

SELECT pg_catalog.setval('public.actors_actor_id_seq', 3, true);


--
-- Name: directors_director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astapov
--

SELECT pg_catalog.setval('public.directors_director_id_seq', 4, true);


--
-- Name: films_film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: astapov
--

SELECT pg_catalog.setval('public.films_film_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

