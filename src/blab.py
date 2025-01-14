

import random
from PIL import Image, ImageChops
from Genetic import ALL_CHROMOSOME_ENUM, ChromosomeFactory, Organism
import matplotlib.pyplot as plt


def plot():
  generation_number = range(0, 10)
  fitness_10 = [0.1337, 0.2219, 0.2473, 0.3117, 0.3138, 0.3415, 0.3906, 0.3801, 0.3978, 0.3946]
  fitness_20 = [0.3927, 0.5361, 0.6496, 0.7734, 0.8574, 0.9390, 0.9517, 0.9707, 1.0542, 1.0611]
  fitness_30 = [0.6456, 0.7385, 0.9038, 1.0190, 1.2956,1.3415, 1.4488, 1.4488, 1.4488, 1.4488]
  fitness_40 = [0.7972, 0.8865, 0.9221, 0.9784, 1.1286, 1.1576, 1.8305, 2.0141, 2.0141, 2.2475]
  fitness_50 = [0.9262, 1.2604, 1.5083, 2.1459, 2.5254, 2.5925, 3.4943, 3.4943, 3.9408, 4.0339]
  fitness_60 = [0.8143, 1.1994, 1.6329, 1.8572, 3.1987, 3.6135, 3.9513, 4.1841, 4.4680, 4.5838]
  plt.plot(generation_number, fitness_60, label="60% Max Blend")
  plt.plot(generation_number, fitness_50, label="50% Max Blend")
  plt.plot(generation_number, fitness_40, label="40% Max Blend")
  plt.plot(generation_number, fitness_30, label="30% Max Blend")
  plt.plot(generation_number, fitness_20, label="20% Max Blend")
  plt.plot(generation_number, fitness_10, label="10% Max Blend")
  plt.legend()
  plt.xlabel("Generation Number")
  plt.ylabel("Decrease in RestNet Logis (fitness)")
  plt.savefig("fig_all.jpg")


# json_data_1 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'Empty'}, {
#     'Chromosome': 'Empty'}, {'Chromosome': 'Empty'}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}]}
# json_data_2 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'LinearGradient', 'Arguments': {'rotation': 180.0, 'blend_ratio': 0.05}}, {
#     'Chromosome': 'Noise', 'Arguments': {'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}]}
# json_data_3 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'LinearGradient', 'Arguments': {'rotation': 180.0, 'blend_ratio': 0.05}}, {
#     'Chromosome': 'Noise', 'Arguments': {'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}]}
# json_data_4 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05573787135772297}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {
#     'Chromosome': 'Noise', 'Arguments': {'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}]}
# json_data_5 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05573787135772297}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {
#     'Chromosome': 'Noise', 'Arguments': {'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}]}
# json_data_6 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.0632402473386368}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'Noise', 'Arguments': {
#     'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05421998494344368}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05824257674384983}}]}
# json_data_7 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05796374602732975}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'Noise', 'Arguments': {
#     'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05421998494344368}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05824257674384983}}]}
# json_data_8 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05573787135772297}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.046982067322386974}}, {
#     'Chromosome': 'Noise', 'Arguments': {'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05344513155923997}}]}
# json_data_9 = {'DNA': [{'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05796374602732975}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05}}, {'Chromosome': 'Noise', 'Arguments': {
#     'sigma': 0.5, 'blend_ratio': 0.05}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05421998494344368}}, {'Chromosome': 'RadialGradient', 'Arguments': {'blend_ratio': 0.05824257674384983}}]}

def blab():
  json_data_20 = {'DNA': [{'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.4677401404399206, -1.1013987929060371, 0.21334844794800184, 0.9503168864428588), 'quality': 25, 'blend_ratio': 0.16783167330006116}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.4231206669026746, -0.9420071907846321, 0.48460007409794226, 1.1864028350445777), 'quality': 12, 'blend_ratio': 0.16952033778952877}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.723345837032491, -1.0120598652260784, 0.49184541507135415, 1.1010951688723913), 'quality': 7, 'blend_ratio': 0.16695299401563737}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5, -1, 0.5, 1), 'quality': 20, 'blend_ratio': 0.15}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.3846389096393972, -1.0725898720235554, 0.39920840883446634, 0.8523334723569334), 'quality': 15, 'blend_ratio': 0.1799576806106762}}]}
  json_data_30 = {'DNA': [{'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5, -1, 0.5, 1), 'quality': 20, 'blend_ratio': 0.2}}, {'Chromosome': 'Empty'}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.7954736835011238, -1.262649493549769, 0.7985329931271778, 0.37198382167384025), 'quality': 10, 'blend_ratio': 0.3148536744575686}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5, -1, 0.5, 1), 'quality': 20, 'blend_ratio': 0.2}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5585719425383031, -0.8943016429312887, 0.5015395153373021, 1.0889377707956727), 'quality': 18, 'blend_ratio': 0.24876322811738902}}]}
  json_data_40 = {'DNA': [{'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5447704666689839, -1.0618746586262922, 0.49177705990406156, 1.1418342587655914), 'quality': 21, 'blend_ratio': 0.2930116115754494}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.4297208902715437, -1.0526501539204332, 0.4946981709587635, 1.0890970514634999), 'quality': 23, 'blend_ratio': 0.2715353214752767}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.590019909197066, -1.3540357601381792, 0.4529708809428853, 0.6874228994815004), 'quality': 9, 'blend_ratio': 0.26470417853843}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.4307059639237802, -0.9654708883625618, 0.5074489220515863, 1.0541717696331496), 'quality': 17, 'blend_ratio': 0.2691023687222611}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.4537740042500433, -1.067367435027313, 0.4126114092255133, 1.0667711149542514), 'quality': 6, 'blend_ratio': 0.32703877129146725}}]}
  json_data_50 = {'DNA': [{'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.566655875621806, -1.1292721260658078, 0.23441740449200388, 1.2436158796160894), 'quality': 25, 'blend_ratio': 0.26761876428014497}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.3330660875877285, -1.0036771583384043, 0.37499839014455766, 1.1472512126043142), 'quality': 24, 'blend_ratio': 0.34518685706176255}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.4578456165284306, -1.1974131752643913, 0.6126316547612235, 1.0606630987290027), 'quality': 19, 'blend_ratio': 0.3190753780603243}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5833597593073814, -0.9126718630250862, 0.5777749756447861, 1.0185319312463625), 'quality': 22, 'blend_ratio': 0.382735488417065}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.3369680683370513, -1.1634463981510585, 0.7465666888710838, 1.149351590485265), 'quality': 6, 'blend_ratio': 0.414068426459538}}]}
  json_data_60 = {'DNA': [{'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.5265384645279245, -1.0268288102073866, 0.7251260232215058, 1.0305527060140427), 'quality': 13, 'blend_ratio': 0.449122851237667}}, {'Chromosome': 'LinearGradient', 'Arguments': {'rotation': 213.53585709536713, 'blend_ratio': 0.5417598861808574}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.9016021237325922, -1.0125611773669174, 0.2744381571064733, 1.8496742189934328), 'quality': 16, 'blend_ratio': 0.3861474028890341}}, {'Chromosome': 'Mandelbrot', 'Arguments': {'zoom_box': (-1.6345531012863432, -1.4575849363429334, 0.6694142795997533, 1.0708043147525608), 'quality': 23, 'blend_ratio': 0.4107620421146307}}, {'Chromosome': 'LinearGradient', 'Arguments': {'rotation': 164.45201622155128, 'blend_ratio': 0.5350584496854368}}]}
  count = 20
  # for json_data in [json_data_1, json_data_2, json_data_3, json_data_4, json_data_5, json_data_6, json_data_7, json_data_8, json_data_9,]:
  for json_data in [json_data_20, json_data_30, json_data_40, json_data_50, json_data_60, ]:
    org = Organism([])
    org.from_json(json_data)

    initial_cat: Image = Image.open("./TestImages/cat1.jpg")
    img = org.modify_image(initial_cat)
    img.save(f"pic{count}.jpg")
    count = count + 10

if __name__ == "__main__":
  plot()

