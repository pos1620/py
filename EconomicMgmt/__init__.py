#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      home
#
# Created:     17/02/2019
# Copyright:   (c) home 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import conta;
import os;
import socket
import sys;



#objts
c1=conta();

def cad(ob):
    if ob.__class__.__name__ == "conta":

        # Users inormation
        # p1.setNome("alxsy mostovik")
        p1.setNome(raw_input("Nome do Usuario:"))
        #p1.setEmail(raw_input("Email do Usuario:"))
        # Account Information
        c1.setSalario(float(raw_input("Ganho mensal do Investidor:")));
        c1.setInvestimento(float(raw_input("Investimental mensal do Investidor:")));
        c1.setMonths(int(raw_input("quantidade de meses em investimento:")))
#        c1.setPercentualDeNegocio(float(raw_input("Percenteual de Negocio:")))
        c1.setTipoConta(raw_input("Tipo de conta:"));