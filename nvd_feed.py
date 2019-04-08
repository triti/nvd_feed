#!/usr/bin/env python
"""Download the NVD feed, parse it, and spit it back out"""

from gzip import GzipFile
from io import BytesIO
import json

import requests


filename = 'nvdcve-1.0-recent.json.gz'
url = 'https://nvd.nist.gov/feeds/json/cve/1.0/' + filename
response = requests.get(url, stream=True, timeout=15.0)

cve_data = json.load(GzipFile(fileobj=BytesIO(response.content)))

for cve_item in cve_data['CVE_Items']:
    cve_timestamp = cve_item['publishedDate']
    cve_id = cve_item['cve']['CVE_data_meta']['ID']
    # for desc_data in cve_item['cve']['description']['description_data']:
    #     if desc_data['lang'] == 'en':
    #         cve_description = desc_data['value']
    #         break
    cve_description = [
        desc_data['value']
        for desc_data in cve_item['cve']['description']['description_data']
        if desc_data['lang'] == 'en'][0]

    print(json.dumps({'timestamp': cve_timestamp,
                      'id': cve_id,
                      'description': cve_description}))
