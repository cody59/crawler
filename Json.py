import json

pre = driver.find_element_by_tag_name("pre").text
data = json.loads(pre)
print(data)