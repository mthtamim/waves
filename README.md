# 🌊 3D Interactive Wave & Acoustics Laboratory

An interactive, high-performance web simulation for wave physics, acoustics, interference, and harmonic superposition in both **3D Space** and **2D Academic Classroom** environments.

---

## ✨ Features & Capabilities

### 🧊 1. 3D Arena (WebGL & Three.js)
- **Real-Time 3D Wave Dynamics**: Continuous spherical wavefront propagation, interference patterns, and amplitude field heightmaps.
- **Multiple Point Sources**: Customize position $(x, y, z)$, frequency $(f)$, amplitude $(A)$, phase $(\phi)$, and wave speed $(v)$ for each emitter.
- **Doppler Effect & Moving Sources**: Realistic acoustic wavefront compression and frequency shifting.
- **Slit Diffraction & Obstacles**: Huygens-Fresnel wavelets, barrier reflections, and double-slit interference.
- **Wave Models**: Instant toggle between **Ideal Waves** (undamped) and **Practical Waves** ($1/r$ spherical spreading).

### 📐 2. 2D Classroom Studio & Textbook Mode
- **Dedicated Physics Classroom**: Clean, distraction-free view designed for textbook problem verification and interactive lectures.
- **Directional Wave Control**: Single-direction propagation toggle ($+x$ forward, $-x$ reverse, or $\pm x$ counter-propagating superposition).
- **Standing Wave & Traveling Wave Modes**: Direct observation of antinodes (সুস্পন্দ বিন্দু), nodes (নিস্পন্দ বিন্দু), and envelope pulsation.
- **Interactive Caliper Ruler**: Live measurement of wavelength ($\lambda$), period ($T$), frequency ($f$), and wave velocity ($v$).
- **Transverse Particle Beads & Energy Field**: Real-time visualization of individual medium particles executing Simple Harmonic Motion (SHM).

### 🧪 3. Custom Wave Equation Studio
- **Arbitrary Formula Compiler**: Define custom mathematical wave equations $f(x, z, t, r)$ using real-time safe AST parsing.
- **Instant Live Simulation**: Type equations like `2.0 * sin(2*x - 4*t)` or `1.8 * sin(3*r - 5*t)` and instantly see the 3D surface and 2D graphs evolve.
- **Interactive Variable Chips**: Quick-insert buttons for trigonometric, exponential, and coordinate variables (`sin`, `cos`, `pow`, `exp`, `PI`, `x`, `z`, `t`, `r`).

### 📊 4. Analytical Instrumentation
- **Dual-Channel Oscilloscope**: Real-time waveform tracing at the receiver position with freeze and trace toggling.
- **Acoustic Sound Pressure Level (SPL) Meter**: Real-time decibel ($\text{dB}$) readout based on resultant acoustic intensity.
- **Phase Wheel Phasors**: Visual angle rotation $(\omega t - \phi)$ for inspecting coherence and path differences.
- **Numerical Probes & CSV Export**: Drop spatial probes across the field and export displacement time-series to CSV.

---

## 🚀 Getting Started

### Local Development
Serve the files using any standard HTTP server:

```bash
# Python 3
python -m http.server 8080

# Or with Node.js
npx serve .
```

Open your browser and navigate to:
```
http://localhost:8080/
```

---

## 🛠 Technology Stack
- **Rendering**: [Three.js](https://threejs.org/) (WebGL)
- **Math & Physics**: Custom pure JavaScript vector wave engines (`WaveMath`, `StandingWaveCalculator`)
- **Audio Synthesis**: Web Audio API (real-time sinusoidal oscillators and spatial panning)
- **UI Architecture**: Modern vanilla JavaScript (ES Modules) with glassmorphism CSS
- **PWA**: Offline caching via Service Worker (`sw.js`) and Web App Manifest (`manifest.json`)
