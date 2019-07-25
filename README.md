# Udacity_03
Projeto: Aprendizado por Reforço.


MECÂNICA REACH TARGET POSE ( ATINGIR O OBJETIVO )
O segredo que faz "takeOff" se tornar "reach target pose" é o IMPULSO que devemos dar ao drone. Sem o impulso o espaço se torno difuso para assimilação da aprendizagem, ou seja, precisamos dar um "impulso" para dizer ao drone para onde ele deve ir.
O senso de direção nos permite determinar caminhos a serem seguidos. A nível de exemplo usamos a bússola para nos geolocalizar, caso estejamos perdidos. A ideia do impulso é funcionar como uma bússola para o aprendizado, isso permite tornar o "aprendizado infinito" em algo "finito" e "computável".
O impulso serve para jogar ele bem próximo da zona quente, assim ele assimila o que é quente/frio a medida em que explora o ambiente e assimila as recompensas. Igual aquela brincadeira "batata quente", ou uma crosta terrestre de um planeta ( mais próximo do centro, mais quente, no caso maior a recompensa, mais distante do centro, mais frio, no caso menor a recompensa até se tornar nula ).


IDEIA DAS ZONAS VS RECOMPENSAS
Quanto mais próximo do alvo, maior a recompensa ( zona quente ), quanto mais distante, menor se torna a recompensa ( zona fria ), até ser nula.


REFERENTE A FUNÇÃO DE RECOMPENSA
Uso a ideia de Geometria Analítica e Cálculo Vetorial + Recompensa Exponencial ( porque se não o drone fica BURRO, o que chamam de "mínimo local", fica viciado a uma determinada região apenas ) + Correção Inversamente Proporcional, para dar a ideia de uma ESFERA no ar  ( Reach Target Pose ) caso contrário ele subiria ao infinito ( igual um foguete, o que não é o objetivo ).


REFERENTE AOS GRÁFICOS CONTIDOS NO ARQUIVO, DESTACAM-SE:


GEOLOCALIZAÇÃO DE VOOS DO DRONE
Apresenta as cores da zona quente/zona fria, os pontos são onde o drone atingiu de fato.


EVOLUÇÃO DO APRENDIZADO
Apresenta a performance do aprendizado, note a incidência dos picos da recompensa, maior parte deles recaem sobre a zona quente e pouco sobre a zona fria ( quente vermelho, frio azul, meio termo rosa/roxo  Vs eixo da recompensa ).
