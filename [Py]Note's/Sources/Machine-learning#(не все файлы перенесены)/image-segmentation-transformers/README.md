# [How to Perform Image Segmentation using Transformers in Python](https://www.thepythoncode.com/article/image-segmentation-using-huggingface-transformers-python)
##
# [[] / []]()
В этом уроке мы сосредоточимся на том, как выполнить семантическую сегментацию с помощью 🤗 библиотеки Transformers. К концу этого учебника у вас будет четкое представление о том, как использовать подходы, основанные на глубоком обучении, для сегментации изображений. У вас будут навыки, чтобы применить эти методы к вашим проектам.

Примечание: Соответствующую записную книжку Colab для этого учебника можно найти здесь.

Сегментация изображений является важным шагом в компьютерном зрении и обработке изображений. Он делит изображение на несколько сегментов, представляющих определенный объект, фон или область интереса. Сегментация изображения направлена на разделение изображения на значимые области и отделение интересующих объектов от фона.

Существенным преимуществом сегментации изображений является то, что она позволяет нам более эффективно выполнять различные задачи компьютерного зрения. Например, при обнаружении объектов мы можем использовать сегментацию изображения, чтобы сузить интересующую область, так что детектору объектов нужно обрабатывать только соответствующую область, а не все изображение. Таким образом, мы можем сэкономить время и вычислительные ресурсы, что часто приводит к повышению точности.

Другим применением сегментации изображений является удаление фона. Во многих приложениях компьютерного зрения желательно извлекать объекты из их фона и оперировать ими самостоятельно. Сегментация изображений обеспечивает удобный способ разделения изображений на передний и фоновый сегменты.

Существует несколько методов сегментации изображений, начиная от пороговых значений до кластеризации K-средних и заканчивая подходами, основанными на глубоком обучении. В этом уроке мы будем работать с Segformer, подходом, основанным на глубоком обучении. Segformer состоит из иерархического трансформаторного энкодера, а декодер состоит из полностью соединенных слоев, что повышает его точность.

Связанные с: Как использовать кластеризацию K-Means для сегментации изображений с помощью OpenCV в Python

Типы сегментации изображений
Существует три основных типа сегментации изображений: семантическая сегментация, сегментация экземпляров и паноптическая сегментация.

Семантическая сегментация используется для понимания каждого пикселя и классификации каждого пикселя на предопределенные семантические классы, такие как «человек», «автомобиль», «дерево» и так далее. Семантическая сегментация направлена на то, чтобы пометить каждый пиксель в изображении его семантическим значением и создать сегментированное изображение, представляющее объекты и области интереса в изображении.

Сегментация экземпляров включает классификацию пикселей в различные классы, а также различение экземпляров одного и того же объекта. Например, если изображение содержит двух кошек, каждой кошке будет присвоена собственная метка экземпляра. Таким образом, сегментация экземпляров позволяет нам получить более подробное представление об объектах на изображении, поскольку модель теперь также может различать отдельные экземпляры одного и того же класса.

Паноптическая сегментация представляет собой комбинацию семантической и инстансной сегментации. В этом случае все объекты классифицируются, и все экземпляры каждого класса также разделяются. Это также включает в себя классификацию фона! Это приводит к всестороннему и полному пониманию изображения и, следовательно, является наиболее общим случаем сегментации.

Ладно, хватит со всех разговоров. Давайте сразу же углубимся в сегментацию изображений сами!

Сначала мы устанавливаем библиотеку transformers, выполнив следующую команду.

$ pip install requests Pillow numpy torch torchvision transformers
Если вы находитесь на Colab, просто установите трансформаторы:

$ pip install transformers
Настоятельно рекомендуется установить PyTorch с помощью официального руководства. Давайте импортируем различные библиотеки, которые мы будем использовать:

import numpy as np
import torch
import torch.nn.functional as F
from torchvision import transforms
from transformers import pipeline, SegformerImageProcessor, SegformerForSemanticSegmentation
import requests
from PIL import Image
import urllib.parse as parse
import os
Затем делаем функцию для загрузки изображения, на котором мы хотим выполнить сегментацию изображения:

# a function to determine whether a string is a URL or not
def is_url(string):
    try:
        result = parse.urlparse(string)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

# a function to load an image
def load_image(image_path):
    """Helper function to load images from their URLs or paths."""
    if is_url(image_path):
        return Image.open(requests.get(image_path, stream=True).raw)
    elif os.path.exists(image_path):
        return Image.open(image_path)

img_path = "https://shorthaircatbreeds.com/wp-content/uploads/2020/06/Urban-cat-crossing-a-road-300x180.jpg"
image = load_image(img_path)
image
Вот с каким образом мы будем работать:



Обе вышеуказанные функции были взяты из учебника по субтитрам к изображениям, is_url() проверяет, является ли строка URL-адресом. load_image() загрузит и загрузит изображение, если это URL-адрес, и загрузит его, если это локальный путь.

# convert PIL Image to pytorch tensors
transform = transforms.ToTensor()
image_tensor = image.convert("RGB")
image_tensor = transform(image_tensor)
Мы также преобразовали изображение PIL в тензор PyTorch, который нам понадобится в будущем.

Теперь определим некоторые вспомогательные функции, которые облегчат нашу жизнь:

def color_palette():
  """Color palette to map each class to its corresponding color."""
  return [[0, 128, 128],
          [255, 170, 0],
          [161, 19, 46],
          [118, 171, 47],
          [255, 255, 0],
          [84, 170, 127],
          [170, 84, 127],
          [33, 138, 200],
          [255, 84, 0]]
Функция color_palette() возвращает список цветов, содержащихся в виде значений RGB. Эти значения представляют цвет сегмента, который мы будем использовать.

def overlay_segments(image, seg_mask):
  """Return different segments predicted by the model overlaid on image."""
  H, W = seg_mask.shape
  image_mask = np.zeros((H, W, 3), dtype=np.uint8)
  colors = np.array(color_palette())
  # convert to a pytorch tensor if seg_mask is not one already
  seg_mask = seg_mask if torch.is_tensor(seg_mask) else torch.tensor(seg_mask)
  unique_labels = torch.unique(seg_mask)
  # map each segment label to a unique color
  for i, label in enumerate(unique_labels):
    image_mask[seg_mask == label.item(), :] = colors[i]
  image = np.array(image)
  # percentage of original image in the final overlaid iamge
  img_weight = 0.5 
  # overlay input image and the generated segment mask
  img = img_weight * np.array(image) * 255 + (1 - img_weight) * image_mask
  return img.astype(np.uint8)
Функция overlay_segment() принимает изображение и маску сегментации и возвращает маску, наложенную поверх изображения. Сначала он заменяет каждую метку класса значением RGB из цветовой палитры, которую мы определили выше. Затем берется средневзвешенное значение исходного изображения и нашей маски сегментации.

def replace_label(mask, label):
  """Replace the segment masks values with label."""
  mask = np.array(mask)
  mask[mask == 255] = label
  return mask
Наконец, функция replace_label() принимает двоичную маску и возвращает массив numpy с меткой. Мы используем эту функцию для создания полной маски сегментации из отдельных масок.

Использование API конвейера
Теперь самый простой способ решить любую задачу на 🤗 трансформаторах – использовать метод трубопровода()! Поэтому мы начинаем с загрузки конвейера сегментации изображений и пользовательской модели, которую мы хотим загрузить. Затем мы передаем ему входное изображение PIL и получаем различные маски для каждого класса:

# load the entire image segmentation pipeline
img_segmentation_pipeline = pipeline('image-segmentation', 
                                     model="nvidia/segformer-b5-finetuned-ade-640-640")
output = img_segmentation_pipeline(image)
output
Выпуск:

[{'score': None,
  'label': 'building',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA03605DDF0>},
 {'score': None,
  'label': 'floor',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA03605D7C0>},
 {'score': None,
  'label': 'road',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA035F9CF70>},
 {'score': None,
  'label': 'person',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA037FA9100>},
 {'score': None,
  'label': 'car',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA037FA9370>},
 {'score': None,
  'label': 'plaything',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA16A93CD30>},
 {'score': None,
  'label': 'minibike',
  'mask': <PIL.Image.Image image mode=L size=300x180 at 0x7FA036074A30>}]
Мы можем визуализировать маску изображения PIL с индексом 0 следующим образом:

output[0]['mask']


Разве не было бы здорово, если бы мы могли визуализировать маски для всех классов за один раз? Давайте сделаем это:

# load the feature extractor (to preprocess images) and the model (to get outputs)
W, H = image.size
segmentation_mask = np.zeros((H, W), dtype=np.uint8)

for i in range(len(output)):
  segmentation_mask += replace_label(output[i]['mask'], i)
После объединения масок мы показываем наложенные сегменты.

# overlay the predicted segmentation masks on the original image
segmented_img = overlay_segments(image_tensor.permute(1, 2, 0), segmentation_mask)

# convert to PIL Image
Image.fromarray(segmented_img)
Вуаля! Это сегментированное изображение, которое дала нам наша модель:



Теперь, когда мы знаем, как работать с конвейером, давайте сделаем сегментацию изображений без использования конвейера.

Использование 🤗 пользовательских моделей трансформаторов
Во-первых, мы загрузим нашу точно настроенную модель и экстрактор функций. Мы выбираем nvidia/segformer-b5-finetuned-ade-640-640, которая является моделью SegFormer, точно настроенной на набор данных сегментации изображений ADE20k (более 20K образцов) с разрешением 640x640. Он был представлен NVIDIA в этой статье.

Ниже приведена архитектура SegFormer, где кодировщик состоит из трансформаторных блоков, а декодер — просто MLP (Многослойные персептроны):

SegFormer АрхитектураРисунок 1: SegFormer Architecture из официальной статьи.

 

Экстрактор объектов берет изображение и предварительно обрабатывает его, чтобы мы могли передать его нашей модели:

# load the feature extractor (to preprocess images) and the model (to get outputs)
feature_extractor = SegformerImageProcessor.from_pretrained("nvidia/segformer-b5-finetuned-ade-640-640")
model = SegformerForSemanticSegmentation.from_pretrained("nvidia/segformer-b5-finetuned-ade-640-640")
Далее, приведенный ниже код отвечает за выполнение сегментации изображения на изображении:

def to_tensor(image):
  """Convert PIL Image to pytorch tensor."""
  transform = transforms.ToTensor()
  image_tensor = image.convert("RGB")
  image_tensor = transform(image_tensor)
  return image_tensor

# a function that takes an image and return the segmented image
def get_segmented_image(model, feature_extractor, image_path):
  """Return the predicted segmentation mask for the input image."""
  # load the image
  image = load_image(image_path)
  # preprocess input
  inputs = feature_extractor(images=image, return_tensors="pt")
  # convert to pytorch tensor
  image_tensor = to_tensor(image)
  # pass the processed input to the model
  outputs = model(**inputs)
  print("outputs.logits.shape:", outputs.logits.shape)
  # interpolate output logits to the same shape as the input image
  upsampled_logits = F.interpolate(
      outputs.logits, # tensor to be interpolated
      size=image_tensor.shape[1:], # output size we want
      mode='bilinear', # do bilinear interpolation
      align_corners=False)

  # get the class with max probabilities
  segmentation_mask = upsampled_logits.argmax(dim=1)[0]
  print(f"{segmentation_mask.shape=}")
  # get the segmented image
  segmented_img = overlay_segments(image_tensor.permute(1, 2, 0), segmentation_mask)
  # convert to PIL Image
  return Image.fromarray(segmented_img)
В get_segmented_image() мы делаем следующее:

Мы предварительно обрабатываем входное изображение с помощью feature_extractor.
Мы передаем предварительно обработанные значения пикселей в нашу модель для вывода, чтобы получить выходные данные.
Затем мы интерполируем выходные маски сегментации, чтобы получить маски того же размера, что и наше изображение, с помощью функции F.interpolate() PyTorch.
После этого мы присваиваем каждое значение пикселя в наших масках определенному классу.
Получив маски, мы возвращаем наложенные сегменты.
Теперь воспользуемся функцией:

get_segmented_image(model, feature_extractor, "https://shorthaircatbreeds.com/wp-content/uploads/2020/06/Urban-cat-crossing-a-road-300x180.jpg")
Получаем следующий результат:



Другой пример:

get_segmented_image(model, feature_extractor, "http://images.cocodataset.org/test-stuff2017/000000000001.jpg")
Выпуск:



Ура! Наша модель работает хорошо. Теперь вы знаете, как сделать сегментацию изображений самостоятельно. В этом уроке мы использовали модель nvidia/segformer-b5-finetuned-ade-640-640 от 🤗 Transformers. Вы также можете проверить различные другие модели сегментации изображений по этой ссылке.

Ссылки и полезные ссылки
Тонкая настройка модели семантической сегментации с помощью пользовательского набора данных
Сегментация изображения - Huggingface
Модельная карта NVIDIA SegFormer
Источник изображения: Короткошерстные породы кошек
Чтобы просмотреть полный код, проверьте эту ссылку.