from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import h5py

caminho_modelo = 'modelo_cachorros_gatos.h5'

with h5py.File(caminho_modelo, 'r') as file:
    model = load_model(file)

caminho_imagem = 'img_teste2.png'

img = load_img(caminho_imagem, target_size=(150, 150))
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0

predicao = model.predict(img_array)

if predicao[0][0] > 0.5:
    print(f"A imagem é de um cachorro com probabilidade {predicao[0][0]*100:.2f}%.")
else:
    print(f"A imagem é de um gato com probabilidade {(1-predicao[0][0])*100:.2f}%.")
