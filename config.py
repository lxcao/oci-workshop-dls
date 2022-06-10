# for help, run:
# python3 help.py

# config file path
config_file_path="~/.oci/config"
# config file profile
config_profile="specialist2-4sdk"
# region identifier of DLS Dataset
region_identifier="ap-singapore-1"
# compartment where DLS Dataset exists
compartment_id = "ocid1.compartment.oc1..aaaaaaaayjcsmu5ii7ac3kncp5qlbsslaj7irtc3mo4oco22w7ucsiq3atmq"
# ocid of the DLS Dataset
dataset_id = "ocid1.datalabelingdataset.oc1.ap-singapore-1.amaaaaaacuco5yqam326md3gyf6nb3rghmcn4fyzvx5uqs6vtyjo7sk367wq"
# an array where the elements are all of the labels that you will use to annotate records in your DLS Dataset with. Each element is a separate label.
labels = ["cell", "stripe", "debris"]
# the algorithm that will be used to assign labels to DLS Dataset records
labeling_algorithm = "first_letter"
# use for first_match labeling algorithm
first_match_regex_pattern = r'^([^/]*)/.*$'
# maximum number of DLS Dataset records that can be retrieved from the list_records API operation for labeling
# limit=1000 is the hard limit for list_records
list_records_limit = 1000