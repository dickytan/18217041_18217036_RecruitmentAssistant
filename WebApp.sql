--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2019-11-27 13:02:45

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
-- TOC entry 202 (class 1259 OID 16387)
-- Name: account; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account (
    acc_id character varying(100) NOT NULL,
    acc_name character varying(100),
    acc_title character varying(100),
    acc_region character varying(100),
    acc_edu character varying(100),
    acc_wp1 character varying(100),
    acc_wp2 character varying(100)
);


ALTER TABLE public.account OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 24600)
-- Name: todo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.todo (
    user_id character varying(50) NOT NULL,
    hr_id character varying(50) NOT NULL,
    task_id integer NOT NULL,
    task character varying(50) NOT NULL,
    isdone boolean NOT NULL,
    due character varying(50) NOT NULL
);


ALTER TABLE public.todo OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 24598)
-- Name: todo_task_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.todo_task_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.todo_task_id_seq OWNER TO postgres;

--
-- TOC entry 2830 (class 0 OID 0)
-- Dependencies: 203
-- Name: todo_task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.todo_task_id_seq OWNED BY public.todo.task_id;


--
-- TOC entry 2692 (class 2604 OID 24603)
-- Name: todo task_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.todo ALTER COLUMN task_id SET DEFAULT nextval('public.todo_task_id_seq'::regclass);


--
-- TOC entry 2822 (class 0 OID 16387)
-- Dependencies: 202
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('6b00ab158', 'Jan Meyer Saragih', 'Student at Institut Teknologi Bandung', 'West Java Province, Indonesia', 'Institut Teknologi Bandung', 'Comlabs-USDI ITB', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('767a7316a', 'William Halim', 'Student at Institut Teknologi Bandung', 'Indonesia', 'Institut Teknologi Bandung (ITB)', 'Institut Teknologi Bandung', '(ITB)');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('225394158', 'Feby Eliana', 'Most Outstanding Student of STEI ITB | Ex-Product Management Intern at GDP', 'Indonesia', 'Institut Teknologi Bandung', 'Inkubator IT HMIF', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('805965120', 'Hernanta Kusuma Cakrawerdaya', 'Consultant at Packet Systems Indonesia', 'Greater Jakarta Area, Indonesia', 'Telkom University', 'Packet Systems Indonesia', 'Telkom University');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('61a1aa75', 'Rahmad Fadli', 'System Engineer at Packet Systems Indonesia', 'Indonesia', 'Universitas Gunadarma', 'Packet Systems Indonesia', 'Universitas Gunadarma');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('b7177a90', 'Ika Sugiarti', 'Manager at PT HM Sampoerna Tbk', 'East Java Province, Indonesia', 'Unair', 'PT HM Sampoerna Tbk', 'Unair');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('3a0366145', 'Sergio Ryan', 'Information System and Technology Student at Institut Teknologi Bandung | CCNA R&S', 'West Java Province, Indonesia', 'Institut Teknologi Bandung', 'Self-Employed', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('1b052b4b', 'Bobby Prabowo', 'Android Developer Manager at Quipper', 'Banten Province, Indonesia', NULL, 'Quipper', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('b519927', 'Widyawardana Adiprawita', 'Lecturer at Institut Teknologi Bandung', 'Bandung Area, West Java, Indonesia', 'Institut Teknologi Bandung (ITB)', 'Centrums, ITB', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('16ab7495', 'Prangki Tua', 'Systems Engineer at PT. Packet Systems Indonesia', 'Greater Jakarta Area, Indonesia', 'Universitas Bina Nusantara (Binus)', 'PT. Packet Systems Indonesia', 'Universitas Bina Nusantara');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('41363517a', 'Adani Wicaksono Mawaridi', 'Digital Marketing Specialist at PT. BRISK BUSI INDONESIA', 'Greater Jakarta Area, Indonesia', 'Institut Ilmu Sosial dan llmu Politik Jakarta', 'PT. BRISK BUSI INDONESIA', 'Institut Ilmu Sosial dan llmu');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('68a73016b', 'Vincent Siauw', 'Sales Manager bei IPCO Germany GmbH', 'Stuttgart Area, Germany', 'Karlsruher Institut für Technologie (KIT)', 'IPCO AB', 'Karlsruher Institut für');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('70398889', 'D. Baskara Putra', 'Brand Manager at Double Deer & Father of BagiKata.', 'Banten Province, Indonesia', 'Universitas Indonesia (UI)', 'Double Deer', 'Universitas Indonesia (UI)');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('a0babb130', 'Abigail Marcia', 'YLI National Wave 11 by McKinsey & Co', 'Greater Jakarta Area, Indonesia', 'Institut Teknologi Bandung (ITB)', 'Unilever', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('a798b2142', 'Nezela Ardiani', 'Assistant Manager, Financial Planning & Analysis', 'Greater Jakarta Area, Indonesia', 'Institut Teknologi Sepuluh Nopember Surabaya', 'Unilever', 'Institut Teknologi Sepuluh');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('tandicky30@gmail.com', 'Dicky Tan', 'Student at Institut Teknologi Bandung', 'Bandung Area, West Java, Indonesia', 'Institut Teknologi Bandung', 'Lnpoint', 'Institut Teknologi Bandung');
INSERT INTO public.account (acc_id, acc_name, acc_title, acc_region, acc_edu, acc_wp1, acc_wp2) VALUES ('t.williamhalim@gmail.com', 'William Halim', 'Student at Institut Teknologi Bandung', 'Indonesia', 'Institut Teknologi Bandung (ITB)', 'Institut Teknologi Bandung', '(ITB)');


--
-- TOC entry 2824 (class 0 OID 24600)
-- Dependencies: 204
-- Data for Name: todo; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('6b00ab158', '1', 2, 'Send LinkedIn message', false, '30 November 2019');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('6b00ab158', '1', 3, 'Send Online Test', false, '15 Desember 2019');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('6b00ab158', '1', 4, 'HR Interview', false, '30 Desember 2019');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('767a7316a', '2', 6, 'Send LinkedIn message', false, '30 Desember 2019');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('767a7316a', '2', 7, 'Send Online Test', false, '1 Februari 2020');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('767a7316a', '2', 8, 'User Interview', false, '1 Maret 2020');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('225394158', '2', 10, 'User Interview', false, '1 Juni 2020');
INSERT INTO public.todo (user_id, hr_id, task_id, task, isdone, due) VALUES ('225394158', '2', 11, 'User Onboarding', false, '1 September 2020');


--
-- TOC entry 2831 (class 0 OID 0)
-- Dependencies: 203
-- Name: todo_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.todo_task_id_seq', 11, true);


--
-- TOC entry 2694 (class 2606 OID 16394)
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (acc_id);


--
-- TOC entry 2695 (class 2606 OID 24604)
-- Name: todo user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.todo
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.account(acc_id) MATCH FULL;


-- Completed on 2019-11-27 13:02:46

--
-- PostgreSQL database dump complete
--

