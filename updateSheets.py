from createLists import sheetClientes, sheetBoleto, contact


def updateNewSign(n):

  sheetBoleto(n)
  sheetClientes(n)
  contact(n)

updateNewSign(1)