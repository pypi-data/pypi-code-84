import logging
import typing
from abc import ABC, abstractmethod
import pandas as pd
from multipledispatch import dispatch
from cell_imaging_utils.datasets_metadata.datasetes_metadata_abstract import DatasetsMetaDataAbstract

from numpy import number

log = logging.getLogger(__name__)

"""
DatasetsMetaDataAbstractTable
------------------
Abstract method th handle datasets metadata
the data is handled as DataFrame of pandas
has table shape


"""

class DatasetsMetaDataAbstractTable(DatasetsMetaDataAbstract):
     
     def __init__(self,destenation,source=None) -> None:
          super().__init__(destenation,source)
     
     def get_shape(self)->tuple:
          return self.data.shape
     
     @dispatch(int,int,(int,str,object))
     def set_item(self,row,column,value)->None:
          self.data.iat[row,column]=value
     
     @dispatch(int,str,(int,str,object))
     def set_item(self,row,column,value)->None:
          self.data.at[row,column]=value
     
     @dispatch(int,int)
     def get_item(self,row:int,column:int)->typing.Any:
          self.data.iat[row,column]

     @dispatch(int,str)
     def get_item(self,row:int,column:str)->typing.Union[str,number]:
          self.data.at[row,column]
     
     def set_row(self,row:int,value:list)->None:
          self.data.iloc[row] = value
     
     def get_row(self,row)->list:
          return self.data.iloc[row]
     
     def add_row(self,value)->None:
          self.data.append(value)
     
     @dispatch(int,int,(int,str))
     def set_column(self,column:int,value)->None:
          self.data.iloc[:,column] = value
          
     @dispatch(int,str,list)
     def set_column(self,column:str,value)->None:
          self.data.loc[:,column] = value
     
     @dispatch(int,str)
     def get_column(self,column:str)->list:
          return self.data.loc[:,column]
     
     @dispatch(int,int)
     def get_column(self,column:int)->list:
          return self.data.iloc[:,column]
     
     def create_header(self,column_names)->None:
          self.columns = column_names
     
     def add_column(self,column_name:str,value:list)->None:
          self.data[column_name] = value
     
     
     
     
     
     
     
     