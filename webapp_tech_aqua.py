import streamlit as st

from PIL import Image
image = Image.open('TechAqua.jpg')
# st.image(image)

st.set_page_config(
     page_title = "TECH AQUA",
     page_icon = image)
# criar um título
st.title('TECH AQUA')

# inserindo os dados do usuario

opcao = st.sidebar.selectbox('Escolha uma opção',
                             ['Adubação', 'Correção de pH'])
# opcao = st.radio('Escolha uma opção.', ['Adubação', 'Correção de pH'])

# Adubação
if opcao == 'Adubação':
  # calculo de adubação
  ar = st.slider('Qual é a area em m² do seu viveiro? (acima de 10000 m² será convetido para hectare)', 1, 50000)
  if ar > 10000:
    area = ar/10000
  elif ar <= 10000 :
    area = ar

  opcao2 = st.radio('Você já fez alguma adubação?', ['Sim', 'Não'])
  
  if opcao2 == 'Sim':
    tipo = 'Manutenção'
    
    disco = st.radio('Qual a transparência com o disco de Secchi?', ['Entre 20 a 40 cm', 'Abaixo de 20 cm', 'Acima de 40 cm'])

    if disco == 'Entre 20 a 40 cm':
      resp = st.success('A transparência está ideal, não é necessario fazer adubação no seu viveiro')

    elif disco == 'Abaixo de 20 cm':
      resp = st.error('Não é necessario fazer a adubação no seu viveiro, se você está em processo de adubação suspenda imediatamente')
    
    elif disco == 'Acima de 40 cm':
      st.warning('Faça uma adubação de manutenção, pressione o botão abaixo')
      
  elif opcao2 == 'Não':
    st.info('Já possuimos as informações necessarias, pressione o botão abaixo')
    tipo = 'Preparo do tanque'

# Botão de resultados adubação
  bt1 = st.button('Resultados para sua adubação')
  if bt1 == True:
    import time

    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    # Fase de preparo do tanque
    if tipo == 'Preparo do tanque' :

      st.text('PREPARO DO TANQUE')
      if ar > 10000 :
        adub_inicial = area*130
        st.write('Você precisará de ', round(adub_inicial), 'kg\ha de sulfato de amônio e de superfosfato simples')
      elif ar <= 10000 :
        adub_inicial = (area*130)/10000
        if adub_inicial > 1:
          st.write('Você precisará de ', round(adub_inicial), 'kg\m² de sulfato de amônio e de superfosfato simples')
        elif adub_inicial <= 1:
          st.write('Você precisará de ', round(adub_inicial)/1000, 'g\m² de sulfato de amônio e de superfosfato simples')
        
    # Manutenção
    elif tipo == 'Manutenção':

      if disco == 'Acima de 40 cm':
        st.text('MANUTENÇÃO')
        if ar > 10000 :
          adub_manu = area*75
          st.write('Você precisará de ', round(adub_manu), 'kg\ha de sulfato de amônio e de superfosfato simples')
        elif ar <= 10000 :
          adub_manu = (area*75)/10000 
          if adub_manu > 1:
            st.write('Você precisará de ', round(adub_manu), 'kg\m² de sulfato de amônio e de superfosfato simples')
          elif adub_manu < 1:
            st.write('Você precisará de ', round(adub_manu)/1000, 'kg\m² de sulfato de amônio e de superfosfato simples')


# Correção de pH
elif opcao == 'Correção de pH':
  # inserindo os dados do viveiro
  ph = st.number_input('Qual o pH da agua')
  solo = st.radio('Qual tipo de solo do seu viveiro?', ['Solo Argiloso', 'Solo Franco-Arenoso'])
  ar = st.slider('Qual é a area em m² do seu viveiro? (acima de 10000 m² será convetido para hectare)', 1, 50000)
  if ar > 10000:
    area = ar/10000
  elif ar <= 10000 :
    area = ar
  # botões de resultados para pH
  bt2 = st.button('RESULTADOS PARA SUA CORREÇÃO DE pH')
  if bt2 == True:
    
    st.write('O seu pH é de:',ph)
    
    # correção
    # SOLO ARGILOSO 
    if solo == 'Solo Argiloso' :
      if ph <= 4:
        if ar >10000:
          correcao = 14.320 * area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 14.320 / area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')

      elif ph > 4 and ph <= 4.5:
        if ar >10000:
          correcao = 10.740*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 10.740/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')

      elif ph > 4.5 and ph <= 5:
        if ar >10000:
          correcao = 8.950*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 8.950/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 5 and ph <= 5.5 :
        if ar >10000:
          correcao = 5.370*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 5.370/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 5.5 and ph <= 6 :
        if ar >10000:
          correcao = 3.580*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 3.580/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 6 and ph <= 6.5 :
        if ar >10000:
          correcao = 1.790*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 1.790/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph >=6.6 :
        st.write('O pH está bom, não é necessario fazer correção')

    # SOLO ARENOSO 
    elif solo == 'Solo Franco-Arenoso' :
      if ph <= 4:
        if ar >10000:
          correcao = 7.160*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 7.160/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 4 and ph <= 4.5:
        if ar >10000:
          correcao = 5.370*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 5.370/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 4.5 and ph <= 5:
        if ar >10000:
          correcao = 4.475*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 4.475/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 5 and ph <= 5.5 :
        if ar >10000:
          correcao = 3.580*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 3.580/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 5.5 and ph <= 6 :
        if ar >10000:
          correcao = 1.790*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 1.790/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph > 6 and ph <= 6.5 :
        if ar >10000:
          correcao = 1.790*area
          st.write('Adicione', round(correcao) ,'mil kg/ha de calcario')
        elif ar <10000:
          correcao = 1.790/area
          if correcao > 1000:
            st.write('Adicione', round(correcao) ,'kg/m² de calcario')
          elif correcao < 1000:
            st.write('Adicione', round(correcao*1000, 3) ,'kg/m² de calcario')
      elif ph >=6.6 :
        st.write('O pH está bom, não é necessario fazer correção')

