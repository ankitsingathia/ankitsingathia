<h1 align="center">Ankit Singathia</h1>

<p align="center">
  <b>Software engineer who works with data</b><br>
  I build web apps in React and Node, and analyse large public datasets with SQL and Python.
</p>

<p align="center">
  <a href="https://ankitsingathia.github.io/my-Portfolio/"><img src="https://img.shields.io/badge/Portfolio-0B0B0B?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/ankit-singathia-467203258/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik00Ljk4IDMuNWEyLjUgMi41IDAgMTAwIDUgMi41IDIuNSAwIDAwMC01ek0yLjQgMjEuNWg1LjE2VjkuMzRIMi40VjIxLjV6TTkuOSA5LjM0aDQuOTV2MS42N2guMDdjLjY5LTEuMjQgMi4zOC0yLjU1IDQuOS0yLjU1IDUuMjQgMCA2LjIgMy4zIDYuMiA3LjU4djUuNDZoLTUuMTZ2LTQuODRjMC0xLjE1LS4wMi0yLjY0LTEuNjMtMi42NC0xLjYzIDAtMS44OCAxLjI2LTEuODggMi41NnY0LjkySDkuOVY5LjM0eiIvPjwvc3ZnPg%3D%3D" alt="LinkedIn"></a>
  <a href="mailto:toankitsingathia@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://leetcode.com/u/AnkitSingahia/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"></a>
  <a href="https://www.codechef.com/users/ankitsingathia"><img src="https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef"></a>
</p>

<p align="center">
  <img src="assets/offline-dino.svg" width="100%" alt="Offline dino runner">
</p>

---

### About

**B.Tech Electronics & Communication**, **MNIT Jaipur**, class of 2026.

In summer 2025 I interned at **Bharti Airtel** and built a support chatbot that answers from a set of FAQ documents (RAG). Most of the work was not the model itself. It was checking the output, keeping answers tied to the documents, and handling failures.

- Web apps: **React** on the front end, **Node / Express** on the back end (Flask at Airtel)
- Data: **SQL** in BigQuery and DuckDB, **Python** with pandas, dashboards in Power BI
- Systems: C and C++, in [transceiver firmware](https://github.com/ankitsingathia/optilink) and a [C++17 thread pool](https://github.com/ankitsingathia/work-queue)
- 1,000+ problems solved on LeetCode, contest rating 1862

---

### Experience

**Software Development Intern** · Bharti Airtel Limited · *May – July 2025*

Built an internal RAG-powered support assistant handling network outage, recharge, and complaint-ticket queries.

- FAISS vector knowledge base over **500+ FAQ documents**, with live tower status piped in from MySQL so answers stayed grounded in current network state
- **Flask + WebSocket** backend for real-time bidirectional chat, Redis session caching for concurrent agents
- Intent-based prompt routing across billing, outage, and plan-upgrade flows

---

### Featured Projects

<table>
<tr>
<td colspan="2" valign="top">

#### Where the Google Merchandise Store loses its shoppers

`BigQuery SQL` `dbt` `DuckDB` `Python` `SciPy`

Three months of Google's public GA4 data from its own merch store: 4.3M events from 270K people. Before trusting any of it I audited the export and found three tracking faults, including a shipping event that fires with checkout and would have dropped a third of real buyers from the funnel.

The main leak is getting people from products to checkout (14% make it), and it's the same on phones and desktops. Five store sections convert far worse than the rest, worth roughly 685 orders if they caught up, and one product page sends 58% of its visitors to checkout but only 3.6% of them finish. There's no A/B test in the data, so I designed one on the real numbers and checked the statistics with 1,000 fake tests.

[**Code**](https://github.com/ankitsingathia/ga4-product-analytics) · [**Write-up**](https://ankitsingathia.github.io/ga4-product-analytics/docs/readout.html)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Wanderly: AI trip planner

`React` `Express` `Gemini API` `Firebase` `Leaflet`

Before calling Gemini, the Express server looks the destination up on OpenStreetMap and puts real nearby places into the prompt. Gemini returns each day's plan as **JSON** (stops, travel legs, timings, budget). The server pulls the JSON out even when the model wraps it in text, fills in any missing field before the UI sees it, and returns a 502 when a reply can't be parsed.

Route maps with Leaflet, Google sign-in through Firebase, and a demo mode that needs no keys. The server has unit and API tests that run in CI.

[**Code**](https://github.com/ankitsingathia/tripplanner) · [**Live**](https://tripplanner-jtno.onrender.com/)

</td>
<td width="50%" valign="top">

#### MDPS: multiple disease prediction

`Python` `Streamlit` `scikit-learn` `SQLite`

A Streamlit dashboard with **nine screening modules** (diabetes, heart, kidney, liver, cancer and more), a lab report parser, downloadable PDF reports, and bcrypt logins stored in SQLite.

I tested the model files by giving them inputs with a known right answer instead of trusting their metadata. Two have inverted labels and one returns counts instead of probabilities, all written up in the repo. The models are for learning, not for screening real patients.

[**Code**](https://github.com/ankitsingathia/MDPS) · [**Live**](https://lb6qshk8uqrhexvgmuthwy.streamlit.app/)

</td>
</tr>
</table>

---

### Tech Stack

**Languages**

![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css&logoColor=white)

**Frameworks & Libraries**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![Socket.io](https://img.shields.io/badge/Socket.io-010101?style=flat-square&logo=socketdotio&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**Data & Infrastructure**

![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=flat-square&logo=googlebigquery&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=flat-square&logo=dbt&logoColor=white)
![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?style=flat-square&logo=duckdb&logoColor=black)
![Firebase](https://img.shields.io/badge/Firebase-DD2C00?style=flat-square&logo=firebase&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=flat-square&logo=render&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

**Used at Bharti Airtel** (internal code, not in these repos)

![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white)

**Focus areas:** Product Analytics · A/B Testing · RAG · Data Structures & Algorithms · System Design · ML Pipelines · DBMS · Linux

---

### Competitive Programming

| Platform | Profile | Highlights |
|---|---|---|
| **LeetCode** | [AnkitSingahia](https://leetcode.com/u/AnkitSingahia/) | 1,000+ solved (583 medium, 128 hard) · contest rating **1862** · top 6% |
| **CodeChef** | [ankitsingathia](https://www.codechef.com/users/ankitsingathia) | **3★** · max rating 1656 |

Also: top 1% in **JEE Mains** out of 1M+ candidates.
