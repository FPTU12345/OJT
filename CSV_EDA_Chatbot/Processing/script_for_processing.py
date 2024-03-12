from pydantic import BaseModel, Field
from typing import Union, List
from enum import Enum

class function_for_dropping_missing_value(BaseModel):
  name: str = 'function_for_dropping_missing_value'
  parameters: None

class function_for_dropping_duplicate(BaseModel):
  name: str = 'function_for_dropping_duplicate'
  parameters: None

class option_for_changing_datatype(Enum):
  float_ = 'float'
  int_ = 'int'
  object_ = 'object'

class parameters_for_changing_datatype(BaseModel):
  datatype: option_for_changing_datatype
  column_name: str

class function_for_changing_datatype(BaseModel):
  name: str = 'function_for_changing_datatype'
  parameters: List[parameters_for_changing_datatype]

class parameters_for_flooring_capping_outlier(BaseModel):
  cap: float
  floor: float
  column_name: str

class function_for_flooring_capping_outlier(BaseModel):
  name: str = 'function_for_flooring_capping_outlier'
  parameters: List[parameters_for_flooring_capping_outlier]

class parameters_for_dropping_column(BaseModel):
  column_name: List[str]

class function_for_dropping_column(BaseModel):
  name: str = 'function_for_dropping_column'
  parameters: parameters_for_dropping_column

class option_for_imputing_outlier(Enum):
  mean = 'mean'
  median = 'median'

class parameters_for_imputing_outlier(BaseModel):
  option: option_for_imputing_outlier
  column_name: str

class function_for_imputing_outlier(BaseModel):
  name: str = 'function_for_imputing_outlier'
  parameters: List[parameters_for_imputing_outlier]

class option_for_imputing_missing_value(Enum):
  mean = 'mean'
  mode = 'mode'
  median = 'median'

class prameters_for_imputing_missing_value(BaseModel):
  column_name: str = Field('Name of the column')
  option: option_for_imputing_missing_value

class function_for_imputing_missing_value(BaseModel):
  name: str = 'function_for_imputing_missing_value'
  parameters:  List[prameters_for_imputing_missing_value]

class Step(BaseModel):
  step: Union[function_for_dropping_duplicate,
              function_for_dropping_column,
              function_for_dropping_missing_value,
              function_for_changing_datatype,
              function_for_imputing_missing_value,
              function_for_flooring_capping_outlier,
              function_for_imputing_outlier]

class Processing(BaseModel):
  steps: List[Step]

