# BEE1 Platform

Sources: `raw/official_teknofest/...Genel_Bilgilendirme_.pdf` (BEE1 spec), `...Mimari_Tanımlama...pdf` (sensor PC architecture).

## Vehicle

- Manufacturer: Beemobs. Model: Bee 1, type L7e-CU. Variant: closed cargo. Drive: rear wheel.
- Dimensions: **2740 × 1060 × 1785 mm** (L × W × H). Wheelbase **1860 mm**. Front overhang 410 mm. Rear overhang 470 mm.
- Front track 886 mm; rear track 850 mm.
- Empty weight 760 kg (front 324 / rear 436); driver weight 835 kg; max gross 1000 kg.
- Max vehicle speed 55 km/h, **limited to 30 km/h** for autonomous use.
- Max acceleration 2.5 m/s²; max deceleration 6.5 m/s².
- Steering: rack & pinion, electric assist, electronic control. Turn radius (wall-to-wall) 4.10 m. Max inner-wheel angle 32.5°, max outer-wheel angle 30°.
- Suspension: front MacPherson, rear rigid axle 1:8.1 ratio. Tires 145/70 R13 / 155/65 R13 (summer). 13" 5J steel rims.
- Brakes: front Ø200 mm disc, rear Ø210 mm drum; electric park brake on rear axle; regen via traction motor.
- Powertrain: PMSM motor, nominal 6 kW / 40 Nm, peak 7.5 kW / 80 Nm. LFP battery, 76.8 V (60–88 V).

## Autonomy hardware

- Vehicle PC: **Advantech MIC-770V3H** (Intel Core i9-12900TE, 32 GB RAM, 1 TB SSD) + **MIC-75G20** GPU expansion module.
- GPU: **NVIDIA RTX 3060 12 GB** (PCIe 4.0 x16, 3584 CUDA cores, 1777 MHz boost). Independent 24 VDC supply, up to 700 W peak.
- LiDAR: **Velodyne VLP-16**, 16 channels, 100 m, ±3 cm, FOV 30° vertical (+15°/-15°), 360° horizontal, rotation 5–20 Hz, dual returns, default IP `192.168.1.201`.
- Camera: **Stereolabs ZED2** stereo, USB 3.0, 110°×70°×120° FOV, depth 0.3–20 m. Output `2208×1242 @ 15 fps`, `1920×1080 @ 30 fps`, `1280×720 @ 60 fps`, `672×376 @ 100 fps`.
- GPS/IMU: **Xsens MTI-680-DK**. GNSS: GPS L1C/A + L2C, GLONASS L1OF + L2OF, Galileo E1-B/C + E5b, BeiDou B1I + B2I. PVT horizontal accuracy 1.5 m without RTK. Gyro ±2000 °/s, accel ±10 g, magnetometer ±8 G.
- Brake actuator: encoded stepper motor `86BHH114-450p-40Mp` with 1:5 reducer.
- WiFi router: WAVLINK AERIAL HD4 / AC1200 (PoE, dual band 2.4/5 GHz).
- Vehicle bus: CANBus (see [CAN-Bus Interface](canbus_interface.md)).
- OS: Ubuntu 20.04 LTS. ROS available: ROS1 Noetic and ROS2 Foxy. Container: Docker. Project lock: ROS2 Foxy (see [ROS2 Foxy Notes](../ros2/ros2_foxy_notes.md)).

## Sensor extrinsics (reference: front-axle midpoint)

| Sensor | X (mm) | Y (mm) | Z (mm) |
|---|---|---|---|
| LiDAR (VLP-16) | -177 | 0 | +620 |
| Right camera (ZED2) | -205 | +60 | +685 |
| Left camera (ZED2) | -205 | -60 | +685 |
| GPS/IMU (Xsens MTI-680) | +1440 | 0 | +1390 |

These values feed `bringup/launch/static_tf.launch.py` (see [TF Standard](../architecture/tf_standard.md)) and must be re-measured during the camp before the real-vehicle run.

## Vehicle network

- WiFi SSID: `robotaxi_1` (192.168.30.100) or `robotaxi_2` (192.168.10.100). Password: `robotaxi`.
- SSH: `ssh smart@192.168.30.100`. SFTP: same credentials, port 22.

## Where to look for raw details

- Hardware feature lists, dimensions: `raw/official_teknofest/2026_..._Genel_Bilgilendirme_.pdf`.
- Sensor PC, GPU, network architecture, software layers (Linux + ROS + Docker): `raw/official_teknofest/2026_..._Mimari_Tanımlama_Dok.pdf`.
- Operational details (boot order, joystick remote, PID tuning): `raw/official_teknofest/2026_..._Kullanıcı_Dokümanı_b.pdf`.
