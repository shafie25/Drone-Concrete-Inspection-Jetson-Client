# 🚁 Drone-Based Concrete Inspection System

### Senior Design Project

This system performs automated concrete surface inspection using:

- RC-controlled drone
- NVIDIA Jetson (onboard computer)
- Camera
- Microphone
- Impactor actuator
- Ground Station (React + Flask)

> ⚠️ There is **no Pixhawk integration** and **no STM32**.
> The drone is manually flown via RC.
> The Ground Station only triggers inspection cycles and displays results.

---

# 🏗️ System Architecture

Pilot (RC Control)

↓

Drone + Jetson

↓

Ground Station (Flask API + React UI)

### Responsibilities

**Pilot**

- Controls flight and positioning.

**Jetson**

- Captures image
- Activates impactor
- Records audio
- Uploads inspection results

**Ground Station**

- Sends `begin_inspection` command
- Stores inspection data
- Displays results in UI

---

# 📁 Project Structure

project-root/

│

├── backend/              # Flask REST API

│   ├── app.py

│   └── API_SPEC.md

│

├── frontend/             # React UI

│   ├── src/

│   └── package.json

│

├── jetson_client/        # Jetson simulator (runs locally for testing)

│   ├── main.py

│   ├── inspector.py

│   ├── api.py

│   ├── config.py

│   ├── requirements.txt

│   └── assets/

│       └── sample.jpg

│

└── README.md


---
# 🔄 System Workflow

1. Pilot positions drone near inspection surface.
2. Operator clicks **BEGIN INSPECTION (JETSON)** in the UI.
3. Backend sets: system_state = INSPECTING

4. Jetson client polls `/command`.
5. Jetson:
   - Captures image (simulated locally)
   - Activates impactor (simulated)
   - Records audio (simulated)
6. Jetson uploads results to `/inspection`.
7. Backend:
   - Stores inspection
   - Saves image
   - Resets system_state → `IDLE`
8. Inspection appears instantly in UI.

---

# 🛠️ Tech Stack

### Frontend
- React
- Fetch API
- CSS

### Backend
- Flask
- REST API
- Base64 image storage

### Jetson Client (Simulated)
- Python
- Requests

---

# 🚀 Running the System Locally

You need **three terminals** open.

---

## 1️⃣ Start Backend

```bash
cd backend
python app.py
---

---

# 🛠️ Tech Stack

### Frontend

- React
- Fetch API
- CSS

### Backend

- Flask
- REST API
- Base64 image storage

### Jetson Client (Simulated)

- Python
- Requests

---

# 🚀 Running the System Locally

You need **three terminals** open.

---

## 1️⃣ Start Backend

```bash
cd backend
python app.py
```

Backend runs at:

http://localhost:5000

## 2️⃣ Start Frontend

<pre class="overflow-visible! px-0!" data-start="2320" data-end="2365"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">cd</span><span> frontend</span><br/><span class="ͼs">npm</span><span> install</span><br/><span class="ͼs">npm</span><span></span><span class="ͼs">start</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Frontend runs at:

<pre class="overflow-visible! px-0!" data-start="2386" data-end="2415"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>http://localhost:3000</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>


## 3️⃣ Start Jetson Simulator

<pre class="overflow-visible! px-0!" data-start="2453" data-end="2528"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">cd</span><span> jetson_client</span><br/><span>pip install </span><span class="ͼu">-r</span><span> requirements.txt</span><br/><span>python main.py</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

This simulates the Jetson onboard system.


# 🧪 Testing the System

1. Open the React UI.
2. Click  **BEGIN INSPECTION (JETSON)** .
3. A new inspection will appear immediately.
4. Click the inspection to view:
   * Image
   * Crack detection result
   * Confidence score

<pre class="overflow-visible! px-0!" data-start="2261" data-end="2290"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div></div></div></div></div></div></div></pre>


# 🌐 API Overview

### Health

<pre class="overflow-visible! px-0!" data-start="2840" data-end="2857"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>GET /ping</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### System

<pre class="overflow-visible! px-0!" data-start="2870" data-end="2923"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>GET /system_status</span><br/><span>POST /command</span><br/><span>GET /command</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### Inspections

<pre class="overflow-visible! px-0!" data-start="2941" data-end="3014"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>POST /inspection</span><br/><span>GET /inspections</span><br/><span>GET /inspection/<inspection_id></span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### Images

<pre class="overflow-visible! px-0!" data-start="3027" data-end="3057"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>GET /images/<filename></span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Full API documentation available in:

<pre class="overflow-visible! px-0!" data-start="3097" data-end="3124"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>backend/API_SPEC.md</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 📊 System States

* `IDLE`
* `INSPECTING`

---

# 🔧 Configuration (Jetson Client)

Environment variables (optional):

<pre class="overflow-visible! px-0!" data-start="3252" data-end="3370"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>GS_API_BASE=http://localhost:5000</span><br/><span>GS_POLL_INTERVAL=1.0</span><br/><span>GS_ENABLE_TELEMETRY=1</span><br/><span>GS_SAMPLE_IMAGE=assets/sample.jpg</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Example (Windows PowerShell):

<pre class="overflow-visible! px-0!" data-start="3403" data-end="3479"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼt">$env:GS_API_BASE</span><span class="ͼn">=</span><span class="ͼr">"http://192.168.1.25:5000"</span><br/><span class="ͼt">python</span><span></span><span class="ͼt">main</span><span>.</span><span class="ͼt">py</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🧠 Current Implementation Status

✔ Jetson command polling

✔ Inspection upload

✔ Base64 image storage

✔ UI inspection display

✔ Instant simulated inspection

---

# 🔮 Future Improvements

* Real camera capture (OpenCV on Jetson)
* Real GPIO control of impactor
* Acoustic waveform visualization
* Real crack detection model integration
* Persistent database (PostgreSQL / SQLite)
* Authentication & user roles
* Cloud deployment

---

# 📌 Notes

This project currently runs fully locally using a simulated Jetson client.

When deployed on the actual Jetson:

* Set `GS_API_BASE` to the laptop’s IP address.
* Ensure both devices are on the same WiFi network.
* Replace simulated capture logic with real hardware calls.

---

# 👨‍🎓 Senior Design Project

American University of Sharjah

Computer Engineering

<pre class="overflow-visible! px-0!" data-start="1607" data-end="2241"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div></div></div></div></div></div></div></pre>
