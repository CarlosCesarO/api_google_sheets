# -*- coding: utf-8 -*-
from getLastRow import getlastrow
from quickstart import main
import re
from googleapiclient.discovery import build
import createContact as createcont


creds = main()
service = build('sheets', 'v4', credentials=creds)


def sheetBoleto(n):

    SAMPLE_SPREADSHEET_ID = '1SgNY_G_aZ-AIQOlOnYLlXBnnVudT9y60eR2GqLsO_Wk'
    SAMPLE_RANGE_NAME = 'Mensalidade!A1:Z1'
    
    values = getlastrow(n)

    for i in values:

        listBoleto = []

        if i[10] != 'Já fiz no cartão de crédito' and i[5] != 'Família':

            listBoleto.append(i[6]) #IGREJA
            listBoleto.append(i[1]) #NOME
            listBoleto.append('Ativo') #STATUS
            listBoleto.append(i[12]) #CPF/CNPJ
            listBoleto.append(i[14]) #VENCIMENTO
            if i[13] != '':
                listBoleto.append(re.split('[$,(]',str(i[13]))[1].replace(' ','')) #VALOR
            else:
                listBoleto.append('')
            if "Mensal" in i[13]:
                listBoleto.append('Mensal') #PERIODICIDADE
            if "Semestral" in i[13]:
                listBoleto.append('Semestral') #PERIODICIDADE
            if "Anual" in i[13]:
                listBoleto.append('Anual') #PERIODICIDADE
            if i[13] == '':
                listBoleto.append('') #PERIODICIDADE
            listBoleto.append(i[4]) #E-MAIL
            listBoleto.append(i[3]) #TELEFONE
                    
            body = {

                "values": [listBoleto]
            }

            service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME ,valueInputOption='RAW',body=body).execute()  
 

def sheetClientes(n):

    SAMPLE_SPREADSHEET_ID = '19z4VMHnJunjSsxvBrnErjLGx_c9y1wrR5u02yoXuE14'
    SAMPLE_RANGE_NAME = 'Clientes!A1:Z1'
    
    values = getlastrow(n)

    for i in values:

        listBoleto = []

        listBoleto.append(i[6]) #IGREJA
        listBoleto.append(i[1]) #NOME
        listBoleto.append(i[4]) #E-MAIL
        listBoleto.append(i[3]) #TELEFONE
        listBoleto.append(i[2]) #Cidade
        listBoleto.append('') #Estado
        listBoleto.append(i[8]) #Quantidade de crianças
        listBoleto.append(i[5]) #Igreja ou Família
        if i[10] == 'Já fiz no cartão de crédito':
            listBoleto.append('PagSeguro')
        else:
            listBoleto.append('Boleto')
        if i[13] != '':
            listBoleto.append(re.split('[$,(]',str(i[13]))[1].replace(' ','')) #VALOR
        else:
            listBoleto.append(i[13])
        if "Mensal" in i[13]:
            listBoleto.append('Mensal') #PERIODICIDADE
        if "Semestral" in i[13]:
            listBoleto.append('Semestral') #PERIODICIDADE
        if "Anual" in i[13]:
            listBoleto.append('Anual') #PERIODICIDADE
        if i[13] == '':
            listBoleto.append('') #PERIODICIDADE
        listBoleto.append('Ativo') #STATUS
        listBoleto.append('Internet') #contato
        listBoleto.append(i[0]) #Início data
        listBoleto.append('=HOJE()') #até data
        
        body = {

            "values": [listBoleto]
        }

        service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME ,valueInputOption='RAW',body=body).execute() 


def contact(n):

    values = getlastrow(n)

    for i in values:

        name = i[1]+" "+"-"+" "+i[6]+" LIDER"
        telephone = str(i[3])
        email = i[4]

        createcont.create_contact(name,telephone,email)