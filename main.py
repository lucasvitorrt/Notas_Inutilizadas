# ------ Insert Notas Inutilizadas -----
# Adicição de notas inutilizadas em um BD
# baseado em SQL server, através do comando insert
#
# By @Lucas Vitor.
#
import PySimpleGUI as sg
import subprocess as sp
import functions as f

var = []
reset = 0

# Comando para fechar o cmd assim que abrir o executavel!
sp.Popen('cmd', shell=True)

# Tema da janela
sg.theme('BrownBlue')

# Layout da janela
layout = [
    [sg.T('UNEM_ID:'), sg.Input(size=(8, 1), key='unem_id', font=('', 9))],
    [sg.Frame(layout=[
        [sg.Text('Num Nota'), sg.T(' ' * 7),
         sg.Text('Modelo Nota'), sg.T(' ' * 5),
         sg.Text('Serie Nota'), sg.T(' ' * 6),
         sg.Text('Data Nota'), sg.T(' ' * 1)]],
        title='Dados', title_color='Orange', relief=sg.RELIEF_SUNKEN)],
    [sg.Multiline(size=(10, 15), key='numero_nota', font=('', 9)), sg.T(' ' * 1),
     sg.Multiline(size=(10, 15), key='modelo_nota', font=('', 9)), sg.T(' ' * 1),
     sg.Multiline(size=(10, 15), key='serie_nota', font=('', 9)), sg.T(' ' * 1),
     sg.Multiline(size=(10, 15), key='data_nota', font=('', 9))],
    [sg.Button('Processar'), sg.Button('Limpar'), sg.T(' ' * 64), sg.Button('Sair')],
    [sg.Output(size=(60, 15), key='output', font=('', 9))],
    [sg.Text('Developed by: Lucas Vitor', size=(23, 1), font=('', 7, 'italic'), text_color='Black')]
]
# Criação da janela principal
window = sg.Window('Insert Inutilizadas', layout, icon=('C:\icon2.ico'), disable_close=True)

# Vetores para o tratamento de informação
vet = []
num_nota = []
mod_nota = []
ser_nota = []
dt_nota = []


# Função de execução principal.
def begin(window, reseto):
    global test
    test = 1
    while True:
        event, values = window.Read()
        window['output'].Update('')
        f.read_enter_num(values, vet, num_nota)
        f.read_enter_mod(values, vet, mod_nota)
        f.read_enter_serie(values, vet, ser_nota)
        f.read_enter_data(values, vet, dt_nota)
        if event == 'Sair':
            break
        if event == 'Limpar':
            window['numero_nota'].Update('')
            window['serie_nota'].Update('')
            window['data_nota'].Update('')
            window['modelo_nota'].Update('')
            window['unem_id'].Update('')
            window['output'].Update('')
            reseto = 1
            break
        else:
            #GERA INSERT
            if event == 'Processar' and values['numero_nota'] != '' and values['modelo_nota'] != '' and values['serie_nota'] != '' and values['data_nota'] != '':
                if len(num_nota) == len(mod_nota) == len(ser_nota) == len(dt_nota):
                    unem = str(values['unem_id'])
                    if unem == '':
                        print('Adicione a unidade empresarial')
                    else:
                        print(
                            'INSERT INTO DOCUMENTOS_FISCAIS (RDCZ_ID, VDDR_ID, DCFS_TIPO_DOC_ECF, DCFS_MODELO_DOC, DCFS_CHAVE_NFE, DCFS_COD_MOD, DCFS_COD_SIT, DCFS_NUM_DOC, DCFS_DT_DOC, DCFS_VL_DOC, DCFS_VL_PIS, DCFS_VL_COFINS, DCFS_CPF_CNPJ, DCFS_NOM_ADQ, DCFS_HR_VENDA, DCFS_DESCCONTO, DCFS_VRL_PAGO, DCFS_VALETROCA, DCFS_CANCELADO, DCFS_DESCONTO_ICMS, DCFS_VALEPRESENTE, DCFS_IND_OPER, DCFS_IND_EMIT, DCFS_SER, DCFS_DT_E_S, DCFS_IND_PGTO, DCFS_VL_ABAT_NT, DCFS_VL_MERC, DCFS_IND_FRT, DCFS_VL_FRT, DCFS_VL_SEG, DCFS_VL_OUT_DA, DCFS_VL_BC_ICMS, DCFS_VL_ICMS, DCFS_VL_BC_ICMS_ST, DCFS_VL_ICMS_ST, DCFS_VL_IPI, DCFS_VL_PIS_ST, DCFS_VL_COFINS_ST, PESS_ID, UNEM_ID, DCFS_TIPO_FRETE, DCFS_NUMNOTA, DCFS_ACRECIMO, DCFS_CONTRAVALE, DCFS_NR_NOTA_DEVOLUCAO, DCFS_CONCILIADO, ENTG_ID, DCFS_DT_ENTREGA, DCFS_TIPO_PAGAMENTO, USRS_ID, DCFS_IND_CONTABIL, DCFS_PROPRIA,DCFS_OBS, DCFS_ID_REF, PDDS_ID, OPCM_ID, PESS_ID_TRANSP, DCFS_NCONTROLE, DCFS_PONTOS_ANT, DCFS_PONTOS__NACOMPRA, DCFS_PONTOS_UTILIZADOS, DCFS_PONTOS_SALDO, DCFS_QTD_VOLUMES, DCFS_ENV_CTB, DCFS_ARQ_XML, DCFS_PESO_SAIDA, DCFS_ISVENDA, DCFS_VDDR_NOME, DCFS_STATUS_NFE_MOTIVO, DCFS_STATUS_NFE, DCFS_CHAVE_NFE_REF, DCFS_EXPORTADO, DCFS_EXPORTAR, LCAM_ID, DCFS_ID_PROG, DCFS_ISVENDA_PROG, DCFS_TURNO, DCFS_INSCMUNICIPAL, DCFS_NUMERO_OS, DOC_DCFS_NUMERO_OS, DCFS_NOME_VOLUME, DCFS_LASTUPDATE)\nVALUES')
                        z = (len(num_nota) - 1)
                        if len(num_nota) > 1:
                            for i in range(0, (len(num_nota) - 1)):
                                print(
                                    '    (NULL, NULL, \'ECF\', \'{}\', \'\', \'{}\', \'5\', \'{}\', \'{}\', 0, 0, 0, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, \'1\', \'0\', \'{}\', \'{}\', \'2\', 0, 0, \'1\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', NULL, \'{}\',  NULL, NULL, \'0\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'1\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'2019-02-22 00:00:00.000\'),'.format(
                                        mod_nota[i], mod_nota[i], num_nota[i], dt_nota[i], ser_nota[i], dt_nota[i],
                                        unem))
                            print(
                                '    (NULL, NULL, \'ECF\', \'{}\', \'\', \'{}\', \'5\', \'{}\', \'{}\', 0, 0, 0, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, \'1\', \'0\', \'{}\', \'{}\', \'2\', 0, 0, \'1\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', NULL, \'{}\',  NULL, NULL, \'0\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'1\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'2019-02-22 00:00:00.000\');'.format(
                                    mod_nota[z], mod_nota[z], num_nota[z], dt_nota[z], ser_nota[z], dt_nota[z], unem))
                        else:
                            for i in range(0, len(num_nota)):
                                print(
                                    '    (NULL, NULL, \'ECF\', \'{}\', \'\', \'{}\', \'5\', \'{}\', \'{}\', 0, 0, 0, NULL, NULL, NULL, NULL, 0, 0, 0, 0, 0, \'1\', \'0\', \'{}\', \'{}\', \'2\', 0, 0, \'1\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', \'0\', NULL, \'{}\',  NULL, NULL, \'0\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'1\', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, \'2019-02-22 00:00:00.000\');'.format(
                                        mod_nota[i], mod_nota[i], num_nota[i], dt_nota[i], ser_nota[i], dt_nota[i],
                                        unem))
                else:
                    sg.PopupOK('Campos com quantidades diferentes \n', icon=('C:\icon2.ico'))
            else:
                sg.PopupOK('Preencha todos os Campos \n', icon=('C:\icon2.ico'))
    return reseto


while True:
    loop = begin(window, reset)
    if loop == 1:
        reset = 0
        begin(window, reset)
    else:
        break
