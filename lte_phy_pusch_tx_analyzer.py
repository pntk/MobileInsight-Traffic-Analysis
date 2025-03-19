from mobile_insight.analyzer.analyzer import *

__all__ = ["LtePhyPuschAnalyzer"]

class LtePhyPuschAnalyzer(Analyzer):
	def __init__(self):
		Analyzer.__init__(self)
		self.add_source_callback(self.__msg_callback)

		self.traffic_entity = []

	def set_source(self, source):
		Analyzer.set_source(self, source)
		source.enable_log("LTE_PHY_PUSCH_Tx_Report")

	def __msg_callback(self, msg):
		log_item = msg.data.decode()
		records = log_item['Records']
		timestamp = str(log_item['timestamp'])
		ul_dl =  "UL" if records[0]["Num DL Carriers"] == 0 else "DL"
		size = records[0]["PUSCH TB Size"]
		tx_retx = "Tx" if records[0]["Re-tx Index"] == "First" else "Retx"
		data = {"timestamp": timestamp, "UL/DL": ul_dl, "size": size, "tx_retx": tx_retx }
		self.log_info(str(data))
		self.traffic_entity.append(data)
