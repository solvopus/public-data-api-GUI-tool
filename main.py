# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:16:49 2020

@author: User
"""
#//*[@class='col-table left line']/p[text() = '출력결과(Response Element)']/../table//tbody/tr/td[2]

import pandas as pd
import requests
import urllib
import json

    

def fileOpen():
    try:
        fileReader = pd.read_csv('code_dong_in_Busan.csv', encoding="euc-kr")
    
    except IOError as e:
        print("파일 불러오기 실패 ", e)
        return 0
    
    dongList = fileReader.법정동코드
    return dongList


def getDataFromAPI(dongList):
    try:
        URL = 'http://apis.data.go.kr/B553501/flChimWlService/getFlChimWlInfo'
        apiKey = ''
        decodeKey = urllib.parse.unquote(apiKey)
        pageNumber = 1
        numberOfRows = 100
        adm_cd_List = [dong for dong in dongList]
        
        for admCD in adm_cd_List:
            parameters = {'serviceKey': decodeKey, 'pageNo': pageNumber, 'numOfRows': numberOfRows, 'adm_cd': admCD}
            
            try:
                response = requests.get(URL, params = parameters)
                
            except requests.exceptions.RequestException as e:
                print("Request 에러 발생 ", e)
                break
            
            finally:
                if response.json()['resultMsg'] != 'NODATA_ERROR':
                    print(type(response.json()))
                    print(response.json())
                    
                    responseDictList = dict(response.json())
            

    except:
        print("에러 발생")

    finally:
        return responseDictList
    

def writeData(responseDictList):
    try:
        fileWriter = open('abc.txt', 'w')
        
    except IOError as e:
        print("파일 불러오기 실패 ", e)
        return 0
    
    finally:
        for response in responseDictList:
            responseJson = json.dumps(response)
            json.dump(responseJson, fileWriter)
            

# def getDataFromAPI_test(dongList):
#     try:
#         URL = 'http://apis.data.go.kr/B553501/flChimWlService/getFlChimWlInfo'
#         apiKey = 'iZmGj4rrQPgJXyYi4UUocBUYpJ0%2BSxQ%2Bz8x0ztlDf%2B5CMglAc9hB6qY1RLfzVGR3HtvIhPfEl7FHyIi53%2FPeRg%3D%3D'
#         decodeKey = urllib.parse.unquote(apiKey)
#         pageNumber = 1
#         numberOfRows = 100
#         admCD = 2611012000

#         parameters = {'serviceKey': decodeKey, 'pageNo': pageNumber, 'numOfRows': numberOfRows, 'adm_cd': admCD}

#         response = requests.get(URL, params = parameters)
                
#     except:
#         print("에러 발생")

#     finally:
#         return response

def main():
    try:
        dongList = fileOpen()
        responseDictList = getDataFromAPI(dongList)
        writeData(responseDictList)
        

    finally:
        return
        
    

if __name__ == "__main__":
    main()