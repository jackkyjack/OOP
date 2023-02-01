def update_records(record, id, property, value):
  if id not in record.keys():
    return record
  if value =='':
    del record[id][property]
  if property != 'tracks' and value !='':
    record[id].update({property:value})
  elif property == 'tracks' and value !='':
    record[id][property].append(value)  
  return record