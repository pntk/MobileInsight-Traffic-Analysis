# MobileInsight-Traffic-Analysis

This repository contains custom-developed analyzers and scripts leveraging MobileInsight to extract and analyze real-time traffic patterns from LTE cellular network logs.

## Project Overview

This project implements analytical tools designed to decode LTE network traffic logs, providing detailed insights into uplink/downlink traffic, packet retransmissions, and overall network performance. These insights can assist in network optimization and performance enhancement decisions.

## Setup Instructions

### Prerequisites

- Operating System: Ubuntu (recommended setup via VirtualBox on Windows 11)
- Python 2.7.x
- MobileInsight (installation instructions included below)
- Wireshark, Cython, VirtualBox, Vagrant, Git

### Installation Steps

1. Clone the repository:

```
git clone https://github.com/mobile-insight/mobileinsight-dev.git
cd mobileinsight-dev
```

2. Setup Virtual Environment:

```
vagrant up
vagrant ssh
```

3. Install MobileInsight:

```
cd ~/mi-dev/mobileinsight-core
./install-ubuntu.sh
```

### Directory Structure

```
MobileInsight-core/mobile_insight/analyzers
   ├── lte_phy_pusch_tx_analyzer.py
   └── lte_rlc_am_pdu_analyzer.py

MobileInsight-core/examples/
   ├── lte_phy_pusch_log_example.py
   └── lte_rlc_am_pdu_example.py
```

## Running the Analysis

### Step-by-step Guide

```
cd ~/mi-dev/mobileinsight-core
./install-ubuntu.sh
```

1. Replay logs and generate JSON output:

```
python3 /home/vagrant/mi-dev/mobileinsight-core/examples/lte_phy_pusch_log_example.py ./<path-to-logfile>.mi2log

python3 /home/vagrant/mi-dev/mobileinsight-core/examples/lte_rlc_am_pdu_example.py ./<path-to-logfile>.mi2log

```

This generates structured JSON logs in the `output/` folder.

2. Perform Data Analysis:

```
python analyze.py
```

This script processes the generated JSON files, aggregates data, and generates graphical representations in the `output/` folder.

## Results and Visualization

Analysis outputs (graphs and JSON files) will be available in the `output/` directory, clearly showing traffic behavior and retransmission patterns.

## References

- [MobileInsight Official Website](http://www.mobileinsight.net/index.html)
- [MobileInsight GitHub](https://github.com/mobile-insight)
- [UCLA LTE Dataset](https://ucla.app.box.com/s/cwd6yt8tg5orhbltckkvho9s73crk74d)

******
