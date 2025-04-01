# Radar Tracking Experiments with Conical Pendulum and CubeSat Models

This repository contains code and documentation for experiments using radar to track, filter, and classify objects in motion, particularly focused on 3U CubeSat models suspended in conical pendulum motion in a motion capture environment.

## Table of Contents
- [Experiment Progress Tracker](#experiment-progress-tracker)
  - [Preliminary Work](#preliminary-work)
  - [Experiment 1: Filter Performance Analysis](#experiment-1-filter-performance-analysis)
  - [Experiment 2: Trajectory Prediction](#experiment-2-trajectory-prediction)
  - [Experiment 3: Micro-Doppler Classification](#experiment-3-micro-doppler-classification)
  - [Experiment 4: Multi-Object Discrimination](#experiment-4-multi-object-discrimination)
- [Experiment Details](#experiment-details)
  - [Experiment 1: Filter Performance Analysis](#experiment-1-filter-performance-analysis-1)
  - [Experiment 2: Trajectory Prediction](#experiment-2-trajectory-prediction-1)
  - [Experiment 3: Micro-Doppler Classification](#experiment-3-micro-doppler-classification-1)
  - [Experiment 4: Multi-Object Discrimination](#experiment-4-multi-object-discrimination-1)
- [Results](#results)
  - [Experiment 1: Filter Performance Analysis Results](#experiment-1-filter-performance-analysis-results)
  - [Experiment 2: Trajectory Prediction Results](#experiment-2-trajectory-prediction-results)
  - [Experiment 3: Micro-Doppler Classification Results](#experiment-3-micro-doppler-classification-results)
  - [Experiment 4: Multi-Object Discrimination Results](#experiment-4-multi-object-discrimination-results)
- [Data Collection and Storage Format](#data-collection-and-storage-format)
  - [Experiments 1 & 2: Filter Performance and Trajectory Prediction](#experiments-1--2-filter-performance-and-trajectory-prediction)
  - [Experiment 3: Micro-Doppler Classification](#experiment-3-micro-doppler-classification-2)
  - [Experiment 4: Multi-Object Discrimination](#experiment-4-multi-object-discrimination-2)

## Experiment Progress Tracker

### Preliminary Work
- [x] Fix Range Doppler Jitters
- [ ] Set up 3U CubeSat model with aluminum foil covering
- [ ] **Configure motion capture system for ground truth data**
- [x] Establish data export format for raw I/Q samples
- [ ] *Implement metadata logging for experimental parameters*
- [ ] **Synchronize radar and motion capture timestamps**
- [ ] Determine damping coefficient for physics based estimation
- [ ] *Create file structure code*
- [ ] *Create auto program shutdown*
- [ ] *Implement CFAR into post-processing program*

### Experiment 1: Filter Performance Analysis
- [ ] Collect raw radar data of pendulum motion
- [ ] Implement MTI (Moving Target Indicator) filtering
  - [ ] 1-pulse canceller
  - [ ] 2-pulse canceller
  - [ ] 3-pulse canceller
- [ ] Implement CFAR (Constant False Alarm Rate) detection
  - [ ] CA-CFAR (Cell Averaging)
  - [ ] OS-CFAR (Ordered Statistics)
- [ ] Create hybrid filter combinations (MTI + CFAR)
- [ ] Extract range and velocity estimates using peak frequency finder
- [ ] Compare filter performance metrics
  - [ ] Detection probability vs false alarm rate (determined by not matching truth data)
  - [ ] Range estimation accuracy
  - [ ] Velocity estimation accuracy

### Experiment 2: Trajectory Prediction
- [ ] Implement conical pendulum motion equations
- [ ] Create trajectory prediction algorithm
- [ ] Develop algorithm to update predictions based on measurement error
- [ ] Implement adaptive search region based on prediction confidence
- [ ] Test prediction accuracy at different time horizons
- [ ] Evaluate trajectory model against motion capture ground truth
- [ ] Optimize parameters for real-time prediction
- [ ] Create ML trajectory prediction for comparison using similar method

### Experiment 3: Micro-Doppler Classification
- [ ] Create different surface texture variations for CubeSat model
  - [ ] Aluminum foil covering
  - [ ] Paper covering
  - [ ] Sandpaper covering
  - [ ] Grass turf covering
- [ ] Collect micro-Doppler signatures for each variation
- [ ] Extract time-frequency features from micro-Doppler data
- [ ] Prepare training dataset for machine learning
- [ ] Implement feature extraction pipeline
- [ ] Test classification algorithms on dataset
- [ ] Evaluate classification accuracy

### Experiment 4: Multi-Object Discrimination
- [ ] Configure multiple CubeSat models with different rotational patterns
- [ ] Collect radar data with multiple objects present
- [ ] Implement multi-target detection algorithm
- [ ] Test object counting accuracy with various filters
  - [ ] MTI filtering variations
  - [ ] CFAR detection variations
  - [ ] Combined approaches
- [ ] Compare position estimation accuracy for multiple objects
- [ ] Evaluate scalability with increasing number of objects

## Experiment Details

### Experiment 1: Filter Performance Analysis

This experiment focuses on applying different radar signal processing techniques to the raw radar data and evaluating their performance. The raw data will be collected from a 3U CubeSat model covered in aluminum foil, suspended on a string in a conical pendulum motion within a motion capture room.

The procedure involves:
1. Collecting raw radar I/Q data along with motion capture ground truth
2. Processing the raw data through various filtering techniques:
   - Moving Target Indicator (MTI) filtering at different pulse cancellation levels
   - Constant False Alarm Rate (CFAR) detection with different algorithms and parameters
   - Combinations of MTI and CFAR techniques
3. For each filtering approach, applying peak frequency detection to estimate range and velocity
4. Calculating performance metrics to compare filter effectiveness
5. Determining optimal filtering parameters for subsequent experiments

The goal is to establish which filtering techniques provide the most reliable target detection and parameter estimation for a moving CubeSat model, laying the groundwork for more complex experiments.

### Experiment 2: Trajectory Prediction

This experiment builds upon the filtering techniques from Experiment 1 to implement and test algorithms for predicting the future trajectory of a moving target. The experiment uses the conical pendulum model's predictable harmonic motion as a testbed for trajectory prediction.

The procedure involves:
1. Implementing harmonic equations of motion for the conical pendulum
2. Using the equations to predict future positions of the target
3. Validating predictions against actual radar measurements
4. When predictions differ from measurements, updating the trajectory model
5. Testing different prediction time horizons
6. Implementing adaptive search regions based on prediction confidence

The goal is to develop a robust trajectory prediction capability that can track objects even when measurements are temporarily unavailable or unreliable, and to quantify the accuracy of physics-based prediction models for space object tracking.

### Experiment 3: Micro-Doppler Classification

This experiment investigates the micro-Doppler characteristics of different surface textures on a CubeSat model to develop classification capabilities. Micro-Doppler signatures arise from subtle motions and surface characteristics that modulate the main Doppler shift.

The procedure involves:
1. Creating multiple variations of the 3U CubeSat model with different surface treatments:
   - Aluminum foil (reflective metal)
   - Paper (smooth non-metallic)
   - Sandpaper (rough surface)
   - Grass turf (complex textured surface)
2. Collecting radar data for each variation under controlled pendulum motion
3. Extracting micro-Doppler features from the radar signals
4. Building a dataset suitable for machine learning classification
5. Testing classification algorithms on the feature set

The goal is to determine whether micro-Doppler analysis can reliably differentiate between objects with different surface characteristics, which has applications in space object identification.

### Experiment 4: Multi-Object Discrimination

This experiment extends the single-object detection and filtering techniques to scenarios with multiple objects present. The challenge is to correctly identify the number of objects and estimate the position of each.

The procedure involves:
1. Setting up multiple CubeSat models with different rotational patterns in the motion capture room
2. Collecting radar data of all objects simultaneously
3. Applying the filtering techniques evaluated in Experiment 1
4. Implementing multi-target detection algorithms
5. Estimating the number of objects present
6. Determining the position and velocity of each object
7. Comparing detection and estimation performance across different filtering approaches

The goal is to develop and validate techniques for discriminating between multiple similar objects in close proximity, which is essential for space situational awareness applications.

## Results

### Experiment 1: Filter Performance Analysis Results

**For CA-CFAR, parameters used: Guard Cells = X, Reference Cells = Y, Bias = Z dB**
**For OS-CFAR, parameters used: Guard Cells = X, Reference Cells = Y, Bias = Z dB**

| Filter Type | Detection Rate | False Alarm Rate | Range RMSE (m) | Velocity RMSE (m/s) | Processing Time (ms) |
|-------------|----------------|------------------|----------------|---------------------|----------------------|
| No Filter   | | | | | |
| MTI-1       | | | | | |
| MTI-2       | | | | | |
| MTI-3       | | | | | |
| CA-CFAR     | | | | | |
| OS-CFAR     | | | | | |
| MTI-1 + CA-CFAR | | | | | |
| MTI-2 + CA-CFAR | | | | | |
| MTI-3 + CA-CFAR | | | | | |
| MTI-1 + OS-CFAR | | | | | |
| MTI-2 + OS-CFAR | | | | | |
| MTI-3 + OS-CFAR | | | | | |

**Summary of Findings:**
[To be filled after experiment completion]

**Optimal Filter Configuration:**
[To be filled after experiment completion]

**Visual Comparisons:**
[Links to comparative visualizations to be added]

### Experiment 2: Trajectory Prediction Results

| Prediction Horizon | Position RMS (m) | Velocity RMS (m/s) | Angular Error (deg) | Correction Rate |
|--------------------|-------------------|---------------------|---------------------|-----------------|
| 0.5 seconds        | | | | |
| 1.0 seconds        | | | | |
| 2.0 seconds        | | | | |
| 5.0 seconds        | | | | |

**Model Parameter Estimates:**
- String Length: [TBD] m
- Estimated Damping Coefficient: [TBD]
- Estimated Initial Angle: [TBD] degrees

**Adaptive Search Performance:**
- Average Search Region Size: [TBD] m²
- Target Reacquisition Rate: [TBD]%
- Average Reacquisition Time: [TBD] s

**Summary of Findings:**
[To be filled after experiment completion]

**Visualization of Predicted vs. Actual Trajectories:**
[Links to trajectory visualizations to be added]

### Experiment 3: Micro-Doppler Classification Results

[Insert Andrew's fun graphics]

**Summary of Findings:**
[To be filled after experiment completion]

**Micro-Doppler Signature Visualizations:**
[Links to signature visualizations to be added]

### Experiment 4: Multi-Object Discrimination Results

**Performance Visualization:**

[Object Count Accuracy Visualization per filter type]
[Object ID Consistency Visualization per filter type (how consistently each technique maintains object identity across frames)]

**Detection Performance vs. Object Separation:**
[To be filled after experiment completion]

**Summary of Findings:**
[To be filled after experiment completion]

**Multi-Object Tracking Visualizations:**
[Links to tracking visualizations to be added]

## Data Collection and Storage Format

### Experiments 1 & 2: Filter Performance and Trajectory Prediction

```
DataExports/
├── Experiment1-2/
│   ├── RawData/
│   │   └── YYYY-MM-DD_HHMMSS/
│   │       ├── radar_data.npy (raw I/Q samples)
│   │       ├── mocap_data.csv (ground truth positions)
│   │       ├── metadata.json (experimental parameters)
│   │       ├── Frames/ 
│   │       │   ├── frame_0001.png
│   │       │   ├── frame_0002.png
│   │       │   └── ...
│   │       └── Data/ 
│   │           ├── frame_0001.csv
│   │           ├── frame_0002.csv
│   │           └── ...
│   └── ProcessedData/
│       └── YYYY-MM-DD_HHMMSS/
│           ├── MTI/
│           │   ├── MTI1Pulse/
│           │   │   ├── range_doppler_estimates.csv
│           │   │   └── Frames/ (processed frame images)
│           │   │       ├── frame_0001.png
│           │   │       ├── frame_0002.png
│           │   │       └── ...
│           │   ├── MTI2Pulse/
│           │   │   ├── range_doppler_estimates.csv
│           │   │   └── Frames/
│           │   └── MTI3Pulse/
│           │       ├── range_doppler_estimates.csv
│           │       └── Frames/
│           ├── CFAR/
│           │   ├── CA-CFAR/
│           │   │   ├── param_set1/
│           │   │   │   ├── range_doppler_estimates.csv
│           │   │   │   └── Frames/
│           │   │   └── param_set2/
│           │   │       ├── range_doppler_estimates.csv
│           │   │       └── Frames/
│           │   └── OS-CFAR/
│           │       ├── param_set1/
│           │       └── param_set2/
│           ├── Combined/
│           │   ├── MTI1_CA-CFAR/
│           │   ├── MTI2_CA-CFAR/
│           │   ├── MTI3_CA-CFAR/
│           │   ├── MTI1_OS-CFAR/
│           │   ├── MTI2_OS-CFAR/
│           │   └── MTI3_OS-CFAR/
│           │       
│           └── Trajectory/
│               ├── predictions.csv (Experiment 2 only)
│               ├── error_metrics.csv (Experiment 2 only)
│               └── Frames/ (with trajectory overlays)
│                   ├── frame_0001-0010_trajectory.png
│                   ├── frame_0010-0020_trajectory.png
│                   └── ...
└── ...
```

### Experiment 3: Micro-Doppler Classification

```
DataExports/
├── Experiment3/
│   ├── RawData/
│   │   ├── AluminumFoil/
│   │   │   ├── YYYY-MM-DD_HHMMSS/
│   │   │   │   ├── radar_data.npy
│   │   │   │   ├── mocap_data.csv
│   │   │   │   ├── metadata.json
│   │   │   │   └── Frames/
│   │   │   │       ├── frame_0001.png
│   │   │   │       └── ...
│   │   │   └── [additional trials]/
│   │   ├── Paper/
│   │   ├── Sandpaper/
│   │   └── GrassTurf/
│   └── ProcessedData/
│       └── Idk, Andrew, help
└── ...
```

### Experiment 4: Multi-Object Discrimination

```
DataExports/
├── Experiment4/
│   ├── RawData/
│   │   ├── 2Objects/
│   │   │   ├── YYYY-MM-DD_HHMMSS/
│   │   │   │   ├── radar_data.npy
│   │   │   │   ├── mocap_data.csv
│   │   │   │   ├── metadata.json
│   │   │   │   └── Frames/
│   │   │   │       ├── frame_0001.png
│   │   │   │       ├── frame_0002.png
│   │   │   │       └── ...
│   │   │   └── [additional trials]/
│   │   ├── 3Objects/
│   │   ├── 4Objects/
│   │   └── 5Objects/
│   └── ProcessedData/
│       ├── 2Objects/
│       │   └── YYYY-MM-DD_HHMMSS/
│       │       ├── MTI/
│       │       │   ├── MTI1Pulse/
│       │       │   │   ├── object_count.csv
│       │       │   │   ├── object_positions.csv
│       │       │   │   └── Frames/
│       │       │   │       ├── frame_0001.png
│       │       │   │       └── ...
│       │       │   ├── MTI2Pulse/
│       │       │   └── MTI3Pulse/
│       │       ├── CFAR/
│       │       │   ├── CA-CFAR/
│       │       │   │   ├── param_set1/
│       │       │   │   │   ├── object_count.csv
│       │       │   │   │   ├── object_positions.csv
│       │       │   │   │   └── Frames/
│       │       │   │   └── param_set2/
│       │       │   └── OS-CFAR/
│       │       └── Combined/
│       │           ├── MTI1_CA-CFAR/
│       │           ├── MTI2_CA-CFAR/
│       │           ├── MTI3_CA-CFAR/
│       │           ├── MTI1_OS-CFAR/
│       │           ├── MTI2_OS-CFAR/
│       │           └── MTI3_OS-CFAR/
│       ├── 3Objects/
│       │   └── YYYY-MM-DD_HHMMSS/
│       │       ├── MTI/
│       │       ├── CFAR/
│       │       └── Combined/
│       └── 4Objects/
│           └── YYYY-MM-DD_HHMMSS/
│               ├── MTI/
│               ├── CFAR/
│               └── Combined/
```

The metadata for all experiments will include:
- Radar configuration parameters (sample rate, bandwidth, etc.)
- Physical parameters (pendulum length, angle, mass)
- Object characteristics (dimensions, material)
- Environmental conditions (room dimensions, temperature)
- Processing configuration (filter parameters)
- Timestamp information
- Frame rate and total number of frames
- Frame resolution and format information

Each frame image will be stored with appropriate naming to ensure sequential ordering and easy association with the corresponding processed data. This structure supports the expected volume of 300+ frames per experiment while maintaining clear organization of both the numerical data (CSV/NPY) and visual representations.
