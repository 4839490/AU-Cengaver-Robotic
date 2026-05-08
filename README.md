# AU-Cengaver-Robotic          
# AU Cengaver Robotaxi 2026

Bu repository, **AU CENGAVER ROBOTICS** takımının TEKNOFEST 2026 Robotaksi-Binek Otonom Araç Yarışması hazır araç kategorisi için geliştirdiği otonom sürüş yazılım altyapısını içerir.

Proje; algılama, lokalizasyon, planlama, FSM karar mekanizması, kontrolcü, güvenlik denetimi ve test yayıncıları gibi katmanlardan oluşan modüler bir ROS2 mimarisi üzerine kuruludur.

---

## Repository Yapısı

```text
au-cengaver-robotaxi-2026/
├── README.md
├── .gitignore
├── docs/                      # v1.2/v1.3 sözleşmeleri ve teknik dokümantasyon
├── config/                    # YAML parametre dosyaları
└── ros2_ws/
    └── src/
        ├── common_msgs/       # Ortak enum ve sabit mesaj tanımları
        ├── perception_msgs/   # Algılama katmanı mesajları
        ├── localization_msgs/ # Lokalizasyon / konumlandırma mesajları
        ├── planning_msgs/     # Planlama, trajectory ve hedef hız mesajları
        ├── fsm_msgs/          # FSM karar mekanizması mesajları
        ├── controller_msgs/   # Kontrolcü geri besleme mesajları
        ├── cengaver_perception/   # YOLO, UFLD, LiDAR ve füzyon kodları
        ├── cengaver_planning/     # Rota, GeoJSON ve trajectory planlama kodları
        ├── cengaver_localization/ # EKF, odometri ve map origin mantığı
        ├── cengaver_fsm/          # State machine ve görev akışı
        ├── cengaver_controller/   # Stanley, PID ve Ackermann kontrolcüleri
        ├── cengaver_bringup/      # Launch dosyaları
        └── fake_publishers/       # Test ve sahte veri yayıncıları


















au-cengaver-robotaxi-2026/
│
├── README.md
├── .gitignore
├── CONTRIBUTING.md
├── TEAM_ROLES.md
│
├── docs/
│   ├── contracts/
│   │   ├── perception_planner_fsm_contract_v1_3.md
│   │   ├── localization_planner_contract_v1_2.md
│   │   ├── planner_controller_contract_v1_2.md
│   │   └── fsm_planner_contract_v1_2.md
│   │
│   ├── competition/
│   │   ├── genel_bilgilendirme_notes.md
│   │   ├── sartname_notes.md
│   │   ├── hazir_arac_kullanici_notes.md
│   │   └── mimari_tanimlama_notes.md
│   │
│   ├── architecture/
│   │   ├── system_overview.md
│   │   ├── ros2_topic_map.md
│   │   ├── tf_tree.md
│   │   ├── data_flow.md
│   │   └── fail_safe_policy.md
│   │
│   └── reports/
│       └── algorithm_table_final.md
│
├── config/
│   ├── vehicle_params.yaml
│   ├── topic_names.yaml
│   ├── frame_names.yaml
│   ├── safety_limits.yaml
│   ├── planner_params.yaml
│   ├── perception_params.yaml
│   ├── localization_params.yaml
│   ├── controller_params.yaml
│   └── fsm_params.yaml
│
├── ros2_ws/
│   └── src/
│       │
│       ├── common_msgs/
│       │   ├── msg/
│       │   │   ├── AutonomyMode.msg
│       │   │   └── StopReason.msg
│       │   ├── CMakeLists.txt
│       │   └── package.xml
│       │
│       ├── perception_msgs/
│       │   ├── msg/
│       │   │   ├── LaneModel.msg
│       │   │   ├── TrafficLightState.msg
│       │   │   ├── TrafficSign.msg
│       │   │   ├── TrafficSigns.msg
│       │   │   ├── ObstacleTrack.msg
│       │   │   ├── ObstacleTracks.msg
│       │   │   ├── StopTarget.msg
│       │   │   └── PerceptionDiagnostics.msg
│       │   ├── CMakeLists.txt
│       │   └── package.xml
│       │
│       ├── localization_msgs/
│       │   ├── msg/
│       │   │   ├── LocalizationPose.msg
│       │   │   ├── LocalizationOdometry.msg
│       │   │   ├── LocalizationStatus.msg
│       │   │   ├── LocalizationDiagnostics.msg
│       │   │   ├── MapOrigin.msg
│       │   │   └── RawGps.msg
│       │   ├── CMakeLists.txt
│       │   └── package.xml
│       │
│       ├── planning_msgs/
│       │   ├── msg/
│       │   │   ├── ActiveRouteContext.msg
│       │   │   ├── Trajectory.msg
│       │   │   ├── TrajectoryPoint.msg
│       │   │   ├── TargetSpeed.msg
│       │   │   ├── PlanningStatus.msg
│       │   │   ├── GoalReached.msg
│       │   │   ├── ParkComplete.msg
│       │   │   ├── ControllerFeedback.msg
│       │   │   └── FSMRequest.msg
│       │   ├── CMakeLists.txt
│       │   └── package.xml
│       │
│       ├── fsm_msgs/
│       │   ├── msg/
│       │   │   ├── CurrentMode.msg
│       │   │   ├── MissionState.msg
│       │   │   └── FSMEvent.msg
│       │   ├── CMakeLists.txt
│       │   └── package.xml
│       │
│       ├── perception/
│       │   ├── perception/
│       │   │   ├── __init__.py
│       │   │   ├── lane_node.py
│       │   │   ├── traffic_light_node.py
│       │   │   ├── traffic_sign_node.py
│       │   │   ├── lidar_obstacle_node.py
│       │   │   ├── fusion_node.py
│       │   │   ├── stop_target_node.py
│       │   │   └── perception_diagnostics_node.py
│       │   ├── models/
│       │   │   ├── README.md
│       │   │   ├── yolo/
│       │   │   └── ufld/
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       ├── localization/
│       │   ├── localization/
│       │   │   ├── __init__.py
│       │   │   ├── local_ekf_node.py
│       │   │   ├── global_localization_node.py
│       │   │   ├── map_origin_node.py
│       │   │   ├── raw_gps_node.py
│       │   │   └── localization_diagnostics_node.py
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       ├── planning/
│       │   ├── planning/
│       │   │   ├── __init__.py
│       │   │   ├── planner_node.py
│       │   │   ├── geojson_loader.py
│       │   │   ├── coordinate_transform.py
│       │   │   ├── waypoint_manager.py
│       │   │   ├── route_context_publisher.py
│       │   │   ├── trajectory_builder.py
│       │   │   ├── speed_profile.py
│       │   │   ├── obstacle_decision.py
│       │   │   ├── stop_decision.py
│       │   │   ├── parking_planner.py
│       │   │   ├── timeout_checker.py
│       │   │   └── mode_handler.py
│       │   ├── missions/
│       │   │   ├── sample_mission.geojson
│       │   │   └── README.md
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       ├── fsm/
│       │   ├── fsm/
│       │   │   ├── __init__.py
│       │   │   ├── fsm_node.py
│       │   │   ├── mode_manager.py
│       │   │   ├── transition_rules.py
│       │   │   ├── event_handler.py
│       │   │   └── mission_state_manager.py
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       ├── controller/
│       │   ├── controller/
│       │   │   ├── __init__.py
│       │   │   ├── controller_node.py
│       │   │   ├── pure_pursuit.py
│       │   │   ├── stanley_controller.py
│       │   │   ├── ackermann_model.py
│       │   │   ├── speed_controller.py
│       │   │   ├── can_interface.py
│       │   │   └── controller_feedback_node.py
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       ├── safety_supervisor/
│       │   ├── safety_supervisor/
│       │   │   ├── __init__.py
│       │   │   ├── safety_supervisor_node.py
│       │   │   ├── watchdog.py
│       │   │   └── emergency_policy.py
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       ├── fake_publishers/
│       │   ├── fake_publishers/
│       │   │   ├── __init__.py
│       │   │   ├── fake_perception.py
│       │   │   ├── fake_localization.py
│       │   │   ├── fake_fsm.py
│       │   │   ├── fake_controller_feedback.py
│       │   │   └── scenario_runner.py
│       │   ├── scenarios/
│       │   │   ├── red_light.yaml
│       │   │   ├── localization_lost.yaml
│       │   │   ├── lane_lost.yaml
│       │   │   ├── obstacle_ttc_critical.yaml
│       │   │   └── full_mission_mvp.yaml
│       │   ├── launch/
│       │   ├── test/
│       │   ├── package.xml
│       │   └── setup.py
│       │
│       └── robotaxi_bringup/
│           ├── launch/
│           │   ├── mvp_fake_system.launch.py
│           │   ├── full_system.launch.py
│           │   ├── perception.launch.py
│           │   ├── localization.launch.py
│           │   ├── planning.launch.py
│           │   ├── fsm.launch.py
│           │   └── controller.launch.py
│           ├── config/
│           ├── package.xml
│           └── setup.py
│
├── tests/
│   ├── contract_tests/
│   │   ├── perception_contract_tests.md
│   │   ├── localization_contract_tests.md
│   │   ├── planner_controller_tests.md
│   │   └── fsm_planner_tests.md
│   │
│   ├── integration_tests/
│   │   ├── test_red_light_stop.md
│   │   ├── test_localization_lost.md
│   │   ├── test_obstacle_ttc.md
│   │   └── test_full_mission.md
│   │
│   └── rosbag_checklists/
│       ├── required_bag_topics.md
│       └── test_acceptance_criteria.md
│
├── tools/
│   ├── geojson_tools/
│   │   ├── validate_geojson.py
│   │   └── convert_geojson_to_map.py
│   │
│   ├── bag_tools/
│   │   ├── extract_topic_hz.py
│   │   └── check_timeouts.py
│   │
│   └── visualization/
│       ├── plot_trajectory.py
│       └── plot_waypoints.py
│
├── scripts/
│   ├── build.sh
│   ├── clean.sh
│   ├── format.sh
│   ├── run_fake_system.sh
│   └── record_rosbag.sh
│
├── bags/
│   └── README.md
│
└── .github/
    ├── workflows/
    │   └── lint.yml
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── task.md
    └── pull_request_template.md
