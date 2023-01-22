# Certificado-de-Calibracao

O código apresentado é meu primeiro projeto desenvolvido em Python para calcular as incertezas sobre um instrumento de medição, considerando uma matriz 6x4.
Duas faixas de carga e duas faixas de descarga.

Da posição [0,0]; [0,1]; [0,2]; e assim em diante deve-se colocar os valores obtidos, e ao final da execução o código irá calcular:
- A incerteza devido a histerese
- A incerteza do tipo A sob distribuição de probabilidade quadrática

E então irá somar esses valores obtidos à incerteza de resolução para 0.1 e do método de calibração. Ao final, será dado a incerteza expandida do instrumento desejado.

Fiz esse programa para me auxiliar em um trabalho de metrologia do curso de eletroeletrônica, e após concluí-lo percebi que várias mudanças poderiam ser feitas, como:
- Escolher qual distribuição de probabilidade será utilizada.
- Escolher qual será a resolução do instrumento, ao invés de deixar um valor fixo.
- E se a incerteza do método de calibração ou do instrumento padrão são conhecidas.
