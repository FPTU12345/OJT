import json
from Processing.Processing_v1 import *

def response_encoder_for_processing(response):
  kwargs = response.additional_kwargs
  steps_list = []
  if kwargs:
    json_file = json.loads(kwargs['function_call']['arguments'])
    for step in json_file['steps']:
      name = step['step']['name']
      parameters = step['step']['parameters']
      if name == 'function_for_imputing_outlier':
        steps_list.append((name, [(parameters[0]['column_name'],
                                   parameters[0]['option'])]))
      elif name == 'function_for_dropping_duplicate':
        steps_list.append((name, None))
      elif name == 'function_for_dropping_missing_value':
        steps_list.append((name, None))
      elif name == 'function_for_flooring_capping_outlier':
        steps_list.append((name, [(parameters[0]['column_name'],
                                   parameters[0]['floor'],
                                   parameters[0]['cap'])]))
      elif name == 'function_for_changing_datatype':
        steps_list.append((name, [(parameters[0]['column_name'],
                                   parameters[0]['datatype'])]))
      elif name == 'function_for_imputing_missing_value':
        steps_list.append((name, [(parameters[0]['column_name'],
                                   parameters[0]['option'])]))
      elif name == 'function_for_dropping_column':
        steps_list.append((name, [parameters['column_name'][0]]))

    return steps_list

def processing(processing_list, df):
  functions = {
      'function_for_dropping_missing_value': DropMissingValue,
      'function_for_imputing_missing_value': ImputeMissingValue,
      'function_for_dropping_column': DropColumn,
      'function_for_dropping_duplicate': DropDuplicate,
      'function_for_imputing_outlier': ImputeOutlier,
      'function_for_flooring_capping_outlier': FloorCapOutlier,
      'function_for_changing_datatype': ChangeDataType
  }
  pipeline = Pipeline()
  for function, parameters in processing_list:
    if parameters:
      pipeline.add(functions[function](parameters))
    else:
      pipeline.add(functions[function]())
  res = pipeline.run(df)
  return res

def response_2_df(response, df):
  return processing(response_encoder_for_processing(response), df)