<h1 align="center">Ankit Singathia</h1>

<p align="center">
  <b>Electronics engineer who writes firmware and analyses data</b><br>
  I write C firmware for ARM Cortex-M, build web apps in React and Node, and analyse large public datasets with SQL and Python.
</p>

<p align="center">
  <a href="https://ankitsingathia.github.io/my-Portfolio/"><img src="https://img.shields.io/badge/Portfolio-0B0B0B?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/ankit-singathia-467203258/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPHBhdGggZmlsbD0id2hpdGUiIGQ9Ik00Ljk4IDMuNWEyLjUgMi41IDAgMTAwIDUgMi41IDIuNSAwIDAwMC01ek0yLjQgMjEuNWg1LjE2VjkuMzRIMi40VjIxLjV6TTkuOSA5LjM0aDQuOTV2MS42N2guMDdjLjY5LTEuMjQgMi4zOC0yLjU1IDQuOS0yLjU1IDUuMjQgMCA2LjIgMy4zIDYuMiA3LjU4djUuNDZoLTUuMTZ2LTQuODRjMC0xLjE1LS4wMi0yLjY0LTEuNjMtMi42NC0xLjYzIDAtMS44OCAxLjI2LTEuODggMi41NnY0LjkySDkuOVY5LjM0eiIvPjwvc3ZnPg%3D%3D" alt="LinkedIn"></a>
  <a href="mailto:toankitsingathia@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://leetcode.com/u/AnkitSingahia/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"></a>
  <a href="https://www.codechef.com/users/ankitsingathia"><img src="https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef"></a>
</p>

---

### About

**B.Tech Electronics & Communication**, **MNIT Jaipur**, class of 2026. Now a Graduate Engineer Trainee at **Jindal SAW**, where most of my work has turned into data and automation.

- Web apps: **React** on the front end, **Node / Express** on the back end (Flask at Airtel)
- Data: **SQL** in BigQuery and DuckDB, **Python** with pandas, dbt, Power BI
- Embedded: C firmware for ARM Cortex-M4 ([OptiLink](https://github.com/ankitsingathia/optilink)), and a [C++17 thread pool](https://github.com/ankitsingathia/work-queue)
- 1,000+ problems solved on LeetCode, contest rating 1887

---

### Experience

**Graduate Engineer Trainee, Energy & Utilities** · Jindal SAW Limited, Nashik · *July 2026 – present*

- Built an in-house tool that automates the monthly provisional electricity bill. Work that took two people about a day now runs in under 5 seconds, verified against the manual version: 270,816 cells, zero differences.
- Traced an error in the plant's daily MIS report (23 sheets, 13,000+ formulas): a SUM range starting one row late dropped day 1 from every monthly total. Fixed it so the report ties exactly to the bill.
- Added exception flags to 1,745 calculations so missing readings are caught before the cost allocation that goes into SAP.

**Software Development Intern** · Bharti Airtel Limited · *May – July 2025*

Built an internal RAG support assistant for network outage, recharge and complaint queries.

- FAISS vector knowledge base over **200+ FAQ documents**, with live tower status from MySQL so answers matched the current network state
- **Flask + WebSocket** backend for real-time chat, Redis session caching for concurrent agents
- Intent-based prompt routing across billing, outage and plan-upgrade flows

---

### Featured Projects

<table>
<tr>
<td colspan="2" valign="top">

#### Who borrows from US funds, and is it covered?

`SQL` `DuckDB` `Python` `Power BI` `pytest`

Four quarters of SEC Form N-PORT filings (400–470 MB each) for 12,944 US mutual funds and ETFs. Filers write the same bank many different ways and sometimes file another firm's LEI, so I resolved 307 borrower names to 58 parent groups through the GLEIF registry, with rules that correct or flag a wrong LEI instead of trusting it. Removed $44.6bn of double counting from funds that filed twice. Every rule has a test (55), and the decisions are written down.

[**Code**](https://github.com/ankitsingathia/nport-securities-lending) · [**Report**](https://ankitsingathia.github.io/nport-securities-lending/docs/report.html)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

#### Where the Google Merchandise Store loses its shoppers

`BigQuery SQL` `dbt` `DuckDB` `Python` `SciPy`

Three months of Google's public GA4 data: 4.3M events from 270K people. Before trusting any of it I audited the export and found three tracking faults, including a shipping event that fires with checkout and would have dropped a third of real buyers from the funnel.

The main leak is getting people from products to checkout (14% make it), and it's the same on phones and desktops. Five store sections convert far worse than the rest, worth roughly 685 orders if they caught up. There's no A/B test in the data, so I designed one on the real numbers and checked the statistics with 1,000 simulated tests.

[**Code**](https://github.com/ankitsingathia/ga4-product-analytics) · [**Report**](https://ankitsingathia.github.io/ga4-product-analytics/docs/report.html)

</td>
</tr>
<tr>
<td colspan="2" valign="top">

#### OptiLink: firmware for an optical transceiver

`C11` `ARM Cortex-M4` `CMIS / I2C` `pytest` `GitHub Actions`

Firmware for the controller inside a pluggable optical transceiver. It serves the CMIS memory map to the host over I2C, samples the analog monitors against alarm thresholds with latched, read-to-clear flags, and runs debounced module and per-lane link state machines. The same sources build for a Cortex-M4 (10,368 bytes of flash, 7.9% of 128 KB) and for a desktop host with a simulated HAL on a virtual clock, so 282 C checks and 54 pytest integration tests run in under a second. It has not been run on real silicon, and the README says so.

[**Code**](https://github.com/ankitsingathia/optilink)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Wanderly: AI trip planner

`React` `Express` `Gemini API` `Firebase` `Leaflet`

Before calling Gemini, the Express server looks the destination up on OpenStreetMap and puts real nearby places into the prompt. Gemini returns each day's plan as **JSON**. The server pulls the JSON out even when the model wraps it in text, fills in any missing field before the UI sees it, and returns a 502 when a reply can't be parsed. Server tests run in CI.

[**Code**](https://github.com/ankitsingathia/tripplanner) · [**Live**](https://tripplanner-jtno.onrender.com/) (free hosting, first load can take a minute)

</td>
<td width="50%" valign="top">

#### CodeTogether: collaborative code editor

`React` `Node` `Socket.IO` `Docker` `Monaco`

Rooms where several people edit the same code and run it. Each run goes into a Docker container with no network and limits on memory, CPU and processes, one run per room at a time with a timeout. Socket tests start the real server and drive it like two browser tabs.

[**Code**](https://github.com/ankitsingathia/codetogether)

</td>
</tr>
</table>

---

### Tech stack

- **Languages:** C, C++, Python, SQL, JavaScript
- **Embedded:** ARM Cortex-M4, register-level I2C and UART drivers, hardware abstraction layer, arm-none-eabi-gcc, Make, Jenkins
- **Web:** React, Node.js, Express, Socket.IO, Tailwind CSS
- **Data:** BigQuery, DuckDB, dbt, pandas, SciPy, Power BI, Excel
- **AI:** Gemini API, LangChain, FAISS (RAG)
- **Tools:** Git, GitHub Actions, pytest, Docker, Firebase, Render
- **At work:** SAP ECC (MM), Excel automation. **At Airtel** (internal code, not in these repos): Flask, MySQL, Redis

---

### Competitive Programming

| Platform | Profile | Highlights |
|---|---|---|
| **LeetCode** | [AnkitSingahia](https://leetcode.com/u/AnkitSingahia/) | 1,000+ solved (587 medium, 128 hard) · contest rating **1887** · Knight · top 5.1% |
| **CodeChef** | [ankitsingathia](https://www.codechef.com/users/ankitsingathia) | **3★** · max rating 1656 |

Also: top 1% in **JEE Mains** out of 1M+ candidates.
