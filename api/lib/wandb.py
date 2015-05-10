import os
import json 

# returns the phones, all or one given an id
def phones(id=None):
  js_data = _read_json('/phones.json')
  return js_data
  
# returns the networks, all or one given an id  
def networks(id=None):
  js_data = _read_json('/networks.json')
  return js_data
  
# returns the countries, all or one given an id
def countries(id=None):
  js_data = _read_json('/countries.json')
  return js_data
  
def reports():
  js_data = _read_json('/reports.json')
  return js_data  

# # function that determines if phones are compatible with certain networks
# def _report(phone_id, network_id):

#   networkData = networks(network_id)	
#   phoneData = phones(phone_id)	
# 	gsmCompatFreq = []
# 	HSPACompatFreq = []
# 	LTECompatFreq = []
 
#   #generic function that determines the intersection of our phone and network frequencies and returns them as a set
#   def frequencies(protocol,phoneData,networkData):
# 		compatFreq = set(phone_data["id"].[protocol]Freq).intersection(network_data["id"].[protocol]Freq
# 		return compatFreq
 
#   #execute above function for the 3 "protocols" for lack of a better word
# 	gsmCompatFreq = frequencies(gsm,phoneData,networkData)
# 	HSPACompatFreq = frequencies(hspa,phoneData,networkData)
# 	LTECompatFreq = frequencies(lte,phoneData,networkData)
#   #spit the results out as JSON. Logic needed to deal with empty values for the 3 variables above. 
# 	returnData = gsmCompatFreq + HSPACompatFreq + LTECompatFreq
# 	returnData = json.dump(returnData)
 
# 	return returnData
	
# Helper method to read the flat json
def _read_json(file_name):
  base_path = os.path.dirname(os.path.realpath(__file__))
  full_path = base_path + '/json' + file_name
  json_data = open(full_path, 'r')
  data = json.load(json_data)
  json_data.close()
  return data