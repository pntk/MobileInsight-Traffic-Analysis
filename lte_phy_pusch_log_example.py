import sys
import json

from mobile_insight.monitor import OfflineReplayer
from mobile_insight.analyzer import LtePhyPuschAnalyzer

if __name__ == "__main__":
    src = OfflineReplayer()
    src.set_input_path(sys.argv[1])
    lteAnalyzer = LtePhyPuschAnalyzer()
    lteAnalyzer.set_source(src)
    src.run()
    lteAnalyzer.log_info(f"Successfully extracted {len(lteAnalyzer.traffic_entity)} Messages")
    with open("pusch_data_demo2.json", "w") as fp :
        json.dump(lteAnalyzer.traffic_entity, fp, indent=4)
