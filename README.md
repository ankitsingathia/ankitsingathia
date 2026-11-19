<h1 align="center">Ankit Singathia</h1>

<p align="center">
  <b>Electronics engineer building machine learning on sensor data, down to the microcontroller</b><br>
  Anomaly detection, forecasting and drone video tracking in Python and PyTorch, and C firmware for ARM Cortex-M.
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

**B.Tech Electronics & Communication**, **MNIT Jaipur**, class of 2026. Now a Graduate Engineer Trainee at **Jindal SAW**, in energy and utilities, where the plant's meters and machines are my daily data.

- **Machine learning:** anomaly detection, time-series forecasting, object detection and tracking. PyTorch, scikit-learn, YOLOv8, ONNX Runtime
- **Signal processing:** FFT and envelope analysis of vibration, Kalman filtering, camera-motion estimation with OpenCV
- **Edge AI:** int8 quantisation; a CNN as a bit-exact C kernel sized for an ARM Cortex-M4
- **Embedded:** C firmware for ARM Cortex-M4 ([OptiLink](https://github.com/ankitsingathia/optilink)), I2C and UART drivers, a hardware abstraction layer
- **Data and web:** SQL (BigQuery, DuckDB), pandas, React, Node / Express
- 1,000+ problems solved on LeetCode, contest rating 1887

Every project below states its baseline, the measured improvement, and where the method still fails.

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

#### Machine learning and signal processing

<table>
<tr>
<td colspan="2" valign="top">

#### IndustrialSense AI: bearing fault early warning, down to the microcontroller

`Python` `PyTorch` `SciPy` `scikit-learn` `ONNX Runtime` `C` `FastAPI` `React`

Plants alarm on overall vibration level, which shows that a machine shakes, not what is failing. On NASA run-to-failure data, a threshold that follows slow drift cut false alarms by 91% (117 → 10) and still caught all 4 bearing failures 49–120 hours ahead. Envelope-spectrum features at the bearing's defect frequencies lifted diagnosis macro-F1 from 0.949 to 0.974. A 1D CNN quantised to int8 runs as a C kernel that matches its reference bit for bit, in 23.9 KB of flash for a Cortex-M4. It also shows where things break: on bearings the model has never seen, a score of 0.997 on a random split falls to at most 0.62.

[**Code**](https://github.com/ankitsingathia/industrialsense-ai)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### Counting vehicles from drone video

`YOLOv8` `OpenCV` `Kalman filter` `PyTorch` `ONNX Runtime`

A YOLOv8n fine-tuned on VisDrone, plus SORT and ByteTrack-style trackers written from scratch, with camera-motion compensation from optical flow and RANSAC. On 17 test videos: MOTA 0.231 → 0.633, identity switches down 80%, vehicle count error 24%. ByteTrack's extra pass helps a weak detector and hurts a strong one, and quantising the whole model to int8 broke it.

[**Code**](https://github.com/ankitsingathia/uav-vehicle-tracking)

</td>
<td width="50%" valign="top">

#### Steel plant peak demand, an hour ahead

`Python` `scikit-learn` `PyTorch` `conformal prediction`

The R² of 0.998 widely reported on this dataset comes from a leak. An honest forecast reaches 0.93. Conformal upper bounds warned of 77 of 78 limit crossings within the hour (operator rule: 52); acting on them would cut the month's peak from 629 to 436 kW. An LSTM won on average error but did worse on the peaks that set the bill.

[**Code**](https://github.com/ankitsingathia/steel-peak-demand)

</td>
</tr>
</table>

#### Embedded, data and web

<table>
<tr>
<td colspan="2" valign="top">

#### OptiLink: firmware for an optical transceiver

`C11` `ARM Cortex-M4` `CMIS / I2C` `pytest` `GitHub Actions`

Firmware for the controller inside a pluggable optical transceiver. It serves the CMIS memory map to the host over I2C, samples the analog monitors against alarm thresholds with latched, read-to-clear flags, and runs debounced module and per-lane link state machines. The same sources build for a Cortex-M4 (10,368 bytes of flash, 7.9% of 128 KB) and for a desktop host with a simulated HAL on a virtual clock, so 282 C checks and 54 pytest integration tests run in under a second. It has not been run on real silicon, and the README says so.

[**Code**](https://github.com/ankitsingathia/optilink)

</td>
</tr>
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

- **Languages:** Python, C, C++, SQL, JavaScript
- **Machine learning:** PyTorch, scikit-learn, YOLOv8, ONNX Runtime (int8), conformal prediction, py-motmetrics
- **Signal processing and vision:** NumPy, SciPy (filters, Hilbert, FFT), OpenCV (optical flow, RANSAC), Kalman filters
- **Embedded:** ARM Cortex-M4, register-level I2C and UART drivers, hardware abstraction layer, arm-none-eabi-gcc, Make, Jenkins
- **Data:** BigQuery, DuckDB, dbt, pandas, Power BI, Excel
- **Web and AI apps:** React, Node.js, Express, FastAPI, Socket.IO, Gemini API, LangChain, FAISS (RAG)
- **Tools:** Git, GitHub Actions, pytest, Docker, Linux
- **At work:** SAP ECC (MM), Excel automation. **At Airtel** (internal code, not in these repos): Flask, MySQL, Redis

---

### Competitive Programming

| Platform | Profile | Highlights |
|---|---|---|
| **LeetCode** | [AnkitSingahia](https://leetcode.com/u/AnkitSingahia/) | 1,000+ solved (587 medium, 128 hard) · contest rating **1887** · Knight · top 5.1% |
| **CodeChef** | [ankitsingathia](https://www.codechef.com/users/ankitsingathia) | **3★** · max rating 1656 |

Also: top 1% in **JEE Mains** out of 1M+ candidates.
