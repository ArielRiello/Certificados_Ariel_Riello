# Volume de um tubo

# Seja um tubo com raio de 10cm, com 1,5 metros de comprimento e com uma
#espessura de 1 cm. Qual o volume deste tubo ?

# Volume = PI x raio2 x altura
# PI = 3.14


raio <- 10
espessura <- 1
comprimento <- 70

# Calcula o volume do tubo
volume <- pi*(raio - espessura)^2*comprimento

print(volume)