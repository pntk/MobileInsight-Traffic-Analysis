from mobile_insight.analyzer.analyzer import *

__all__ = ["LteRlcAmPDUAnalyzer"]

class LteRlcAmPDUAnalyzer(Analyzer):
	def __init__(self):
		Analyzer.__init__(self)
		self.add_source_callback(self.__msg_callback)

		self.traffic_entity = []

	def set_source(self, source):
		Analyzer.set_source(self, source)
		source.enable_log("LTE_RLC_UL_AM_All_PDU")
		source.enable_log("LTE_RLC_DL_AM_All_PDU")

	def __msg_callback(self, msg):
		log_item = msg.data.decode()
		subpacket = log_item['Subpackets'][0]
		timestamp = str(log_item['timestamp'])
		#ul_dl =  "UL" if records[0]["Num DL Carriers"] == 0 else "DL"
		
		ul_dl = None
		pdu = None
		
		if msg.type_id == "LTE_RLC_UL_AM_All_PDU":
			ul_dl = "UL"
			pdu = subpacket["RLCUL PDUs"][0]
		
		if msg.type_id == "LTE_RLC_DL_AM_All_PDU":
			ul_dl = "DL"
			pdu = subpacket["RLCDL PDUs"][0]


		size = subpacket["Subpacket Size"]

		tx_retx = "Tx" if "DATA" in pdu["PDU TYPE"] and pdu["RF"] == "0" else "Retx"
		
		data = {"timestamp": timestamp, "UL/DL": ul_dl, "size": size, "tx_retx": tx_retx }
		
		self.log_info(str(data))
		self.traffic_entity.append(data)
