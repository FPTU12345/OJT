from abc import ABC, abstractclassmethod
import pandas as pd
import numpy as np

class DataProcessing(ABC):
  @abstractclassmethod
  def apply(self, df):
    pass

class DropMissingValue(DataProcessing):
  def apply(self, df):
    return df.dropna()

class ImputeMissingValue(DataProcessing):
  def __init__(self, imputation_list):
    '''Input:
       imputation_list : [(column_name1, option),
                          (column_name2, option),
                          (column_name3, option), ...]
       Available options: mean, median and mode'''
    self.imputation_list = imputation_list

  def apply(self, df):
    for (column_name, option) in self.imputation_list:
      if option == 'mode':
        df[column_name] = df[column_name].fillna(df[column_name].mode()[0])
      elif option == 'mean':
        df[column_name] = df[column_name].fillna(df[column_name].mean())
      elif option == 'median':
        df[column_name] = df[column_name].fillna(df[column_name].median())
    return df

class DropColumn(DataProcessing):
  def __init__(self, column_list):
    '''Input:
    column_list : [column_name1,
                   column_name2,
                   column_name3,
                   ...]'''
    self.column_list = column_list

  def apply(self, df):
    return df.drop(self.column_list, axis = 1)

class DropDuplicate(DataProcessing):
  def apply(self, df):
    return df.drop_duplicates()

class ImputeOutlier(DataProcessing):
  def __init__(self, column_list):
    '''Input:
       column_list : [(column_name1, option),
                      (column_name2, option),
                      (column_name3, option),
                      ...]
       option: mean or median
    '''
    self.column_list = column_list

  def apply(self, df):
    def outlier_detection(df, column_name):
      q1 = df[column_name].quantile(0.25)
      q3 = df[column_name].quantile(0.75)
      IQR = q3 - q1
      lower_bound = q1 - 1.5 * IQR
      upper_bound = q3 + 1.5 * IQR
      return lower_bound, upper_bound
    for (column_name, option) in self.column_list:
      lower_bound, upper_bound = outlier_detection(df, column_name)
      if option == 'mean':
        df.loc[~((lower_bound < df[column_name]) & (df[column_name] < upper_bound)), [column_name]] = df[column_name].mean()
      elif option == 'median':
        df.loc[~((lower_bound < df[column_name]) & (df[column_name] < upper_bound)), [column_name]] = df[column_name].median()
    return df

class FloorCapOutlier(DataProcessing):
  def __init__(self, column_list):
    '''Input:
       column_list : [(column_name1, 0.1, 0.9),
                      (column_name2, 0.2, 0.8),
                      (column_name3, 0.05, 0.95),
                      ...]
      The structure: (column_name, lower, upper)
      0 < lower < upper < 1
    '''
    self.column_list = column_list

  def apply(self, df):
    for (column_name, lower, upper) in self.column_list:
      lower_bound = df[column_name].quantile(lower)
      upper_bound = df[column_name].quantile(upper)
      df.loc[df[column_name] > upper_bound, [column_name]] = upper_bound
      df.loc[df[column_name] < lower_bound, [column_name]] = lower_bound
    return df

class ChangeDataType(DataProcessing):
  def __init__(self, column_list):
    '''Input:
    column_list : [(column_name1, datatype1),
                   (column_name2, datatype2),
                   (column_name3, datatype3),
                   ...]'''
    self.column_list = column_list

  def apply(self, df):
    column_dictionary = {}
    for (column_name, datatype) in self.column_list:
      if datatype == 'int':
        column_dictionary[column_name] = int
      elif datatype == 'float':
        column_dictionary[column_name] = float
      elif datatype == 'object':
        column_dictionary[column_name] = object
    return df.astype(column_dictionary)

class Pipeline:
  def __init__(self):
    self.steps = []

  def add(self, function):
    self.steps.append(function)

  def run(self, df):
    for step in self.steps:
      df = step.apply(df)
    return df
