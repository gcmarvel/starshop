from django import template

from django.template import loader
from django.utils.safestring import mark_safe

from oscar.core.loading import get_model
from oscar.apps.partner.strategy import Selector

register = template.Library()

Category = get_model('catalogue', 'category')
Product = get_model('catalogue', 'product')
ProductCategory = get_model('catalogue', 'productcategory')


@register.simple_tag (name="constellation_name", takes_context=True)
def get_name(context, name):
    cat = Category.objects.get(name=name)
    prodcat = ProductCategory.objects.filter(category_id=cat.pk)
    id_list = []
    for pc in prodcat:
        prod_id = Product.objects.get(pk=pc.product_id)
        id_list.append(prod_id.id)
    products = []
    for prod_id in id_list:
        product = Product.objects.get(pk=prod_id)
        products.append(product)

    template_name = "star_layouts/" + cat.slug + ".html"

    template = loader.get_template(template_name)

    return template.render({'products': products}, request=context['request'])


@register.simple_tag (name="constellation_image")
def get_image(category):
    if category == "Феникс":
        return '/static/img/phoenix-full.png'
    if category == "Дельфин":
        return '/static/img/delphinus-full.png'
    if category == "Водолей":
        return '/static/img/aquarius-full.png'
    if category == "Рысь":
        return '/static/img/lynx-full.png'
    if category == "Орион":
        return '/static/img/orion-full.png'
    if category == "Овен":
        return '/static/img/aries-full.png'
    if category == "Лебедь":
        return '/static/img/cygnus-full.png'
    if category == "Козерог":
        return '/static/img/capricorn-full.png'
    if category == "Телец":
        return '/static/img/taurus-full.png'
    if category == "Волк":
        return '/static/img/lupus-full.png'
    if category == "Пегас":
        return '/static/img/pegasus-full.png'
    if category == "Орёл":
        return '/static/img/aquilla-full.png'
    if category == "Лира":
        return '/static/img/lyra-full.png'
    if category == "Стрелец":
        return '/static/img/sagittarius-full.png'
    if category == "Рак":
        return '/static/img/cancer-full.png'
    if category == "Ворон":
        return '/static/img/corvus-full.png'
    if category == "Дева":
        return '/static/img/virgo-full.png'
    if category == "Рыбы":
        return '/static/img/pisces-full.png'
    if category == "Единорог":
        return '/static/img/monoceros-full.png'
    if category == "Скорпион":
        return '/static/img/scorpio-full.png'
    if category == "Весы":
        return '/static/img/libra-full.png'
    if category == "Близнецы":
        return '/static/img/gemini-full.png'
    if category == "Лев":
        return '/static/img/leo-full.png'
    if category == "Дракон":
        return '/static/img/draco-full.png'


@register.simple_tag (name="category_name")
def get_name(prod):
    prod_cat = ProductCategory.objects.get(product_id=prod.id)
    cat = Category.objects.get(id=prod_cat.category_id)
    return cat.name


@register.simple_tag (name="star_color")
def get_class(product):
    if product.product_class_id == 1:
        return '/static/img/star_white.png'
    if product.product_class_id == 2:
        return '/static/img/star_yellow.png'
    if product.product_class_id == 3:
        return '/static/img/star_orange.png'
    if product.product_class_id == 4:
        return '/static/img/star_blue.png'
    if product.product_class_id == 5:
        return '/static/img/star_red.png'
    if product.product_class_id == 6:
        return '/static/img/star_double.png'


@register.simple_tag (name="star_name_color")
def get_class(product):
    if product.product_class_id == 1:
        return '#FFFFFF'
    if product.product_class_id == 2:
        return '#FEC91B'
    if product.product_class_id == 3:
        return '#FE8B1B'
    if product.product_class_id == 4:
        return '#05C8FD'
    if product.product_class_id == 5:
        return '#C41818'
    if product.product_class_id == 6:
        return '#C200C9'


@register.simple_tag (name="star_magnitude")
def get_magnitude(product):
    if 10 > product.attr.magnitude >= 9:
        return 'mag-9'
    if 9 > product.attr.magnitude >= 8:
        return 'mag-8'
    if 8 > product.attr.magnitude >= 7:
        return 'mag-7'
    if 7 > product.attr.magnitude >= 6:
        return 'mag-6'
    if 6 > product.attr.magnitude >= 5:
        return 'mag-5'


@register.simple_tag (name="bundle")
def get_magnitude(product):
    if 10 > product.attr.magnitude >= 9:
        return 'Электронный'
    if 9 > product.attr.magnitude >= 8:
        return 'Стандарт'
    if 8 > product.attr.magnitude >= 7:
        return 'Эксклюзив'
    if 7 > product.attr.magnitude >= 6:
        return 'Премиум'
    if 6 > product.attr.magnitude >= 5:
        return 'Вечность'


@register.simple_tag (name="star_magnitude_round")
def get_magnitude(product):
        return int(product.attr.magnitude)


@register.simple_tag (name="star_class")
def get_class(product):
    if product.product_class_id == 1:
        return 'Белая звезда'
    if product.product_class_id == 2:
        return 'Желтая звезда'
    if product.product_class_id == 3:
        return 'Оранжевая звезда'
    if product.product_class_id == 4:
        return 'Голубая звезда'
    if product.product_class_id == 5:
        return 'Красная звезда'
    if product.product_class_id == 6:
        return 'Двойная звезда'

@register.simple_tag (name="constructor_class")
def get_attribute(product):
    if product.attr.starclass == 'Белая звезда':
        return '/static/img/star_white.png'
    if product.attr.starclass == 'Желтая звезда':
        return '/static/img/star_yellow.png'
    if product.attr.starclass == 'Оранжевая звезда':
        return '/static/img/star_orange.png'
    if product.attr.starclass == 'Голубая звезда':
        return '/static/img/star_blue.png'
    if product.attr.starclass == 'Красная звезда':
        return '/static/img/star_red.png'
    if product.attr.starclass == 'Двойная звезда':
        return '/static/img/star_double.png'

@register.simple_tag (name="constructor_class_big")
def get_attribute(product):
    if product.attr.starclass == 'Белая звезда':
        return '/static/img/detail/white1.png'
    if product.attr.starclass == 'Желтая звезда':
        return '/static/img/detail/yellow1.png'
    if product.attr.starclass == 'Оранжевая звезда':
        return '/static/img/detail/orange1.png'
    if product.attr.starclass == 'Голубая звезда':
        return '/static/img/detail/blue1.png'
    if product.attr.starclass == 'Красная звезда':
        return '/static/img/detail/red1.png'
    if product.attr.starclass == 'Двойная звезда':
        return '/static/img/detail/double1.png'


@register.simple_tag (name="thumbnail_img")
def get_thumbnail(product):
    if product.product_class_id == 1:
        return '/static/img/thumbnail_white.png'
    if product.product_class_id == 2:
        return '/static/img/thumbnail_yellow.png'
    if product.product_class_id == 3:
        return '/static/img/thumbnail_orange.png'
    if product.product_class_id == 4:
        return '/static/img/thumbnail_blue.png'
    if product.product_class_id == 5:
        return '/static/img/thumbnail_red.png'
    if product.product_class_id == 6:
        return '/static/img/thumbnail_double.png'


@register.simple_tag (name="present")
def get_magnitude(product):
    if 10 > product.attr.magnitude >= 9:
        template = """
        <div class="tooltip-present-wrapper">
            <div class="tooltip-present-title">
                Набор Электронный
            </div>
            <div class="tooltip-present-detail">
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Регистрация звезды в международном звёздном каталоге IOASA
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Электронное досье звезды
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Спутниковая фотография с расположением звезды на карте звёздного неба
                </div>
            </div>
        </div>
        """
    elif 9 > product.attr.magnitude >= 8:
        template = """
        <div class="tooltip-present-wrapper">
            <div class="tooltip-present-title">
                Набор Стандарт
            </div>
            <div class="tooltip-present-detail">
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Регистрация звезды в международном звёздном каталоге IOASA
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Электронное досье звезды
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Спутниковая фотография с расположением звезды на карте звёздного неба
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Официальный сертификат в металлической рамке, подтверждающий владение звездой
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды
                </div>   
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Послание или пожелание на свитке с сургучной печатью
                </div>                                  
            </div>
        </div>
        """
    elif 8 > product.attr.magnitude >= 7:
        template = """
        <div class="tooltip-present-wrapper">
            <div class="tooltip-present-title">
                Набор Эксклюкзив
            </div>
            <div class="tooltip-present-detail">
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Регистрация звезды в международном звёздном каталоге IOASA
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Электронное досье звезды
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Спутниковая фотография с расположением звезды на карте звёздного неба
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Официальный сертификат в металлической рамке, подтверждающий владение звездой
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды
                </div>  
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Послание или пожелание на свитке с сургучной печатью
                </div>                 
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Светящаяся в темноте карта звездного неба
                </div>   
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Персональное видеопутешествие к звезде
                </div>                      
            </div>
        </div>
        """
    elif 7 > product.attr.magnitude >= 6:
        template = """
        <div class="tooltip-present-wrapper">
            <div class="tooltip-present-title">
                Набор Премиум
            </div>
            <div class="tooltip-present-detail">
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Регистрация звезды в международном звёздном каталоге IOASA
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Электронное досье звезды
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Спутниковая фотография с расположением звезды на карте звёздного неба
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Официальный сертификат в металлической рамке, подтверждающий владение звездой
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды
                </div>  
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Послание или пожелание на свитке с сургучной печатью
                </div>                 
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Светящаяся в темноте карта звездного неба
                </div>   
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Персональное видеопутешествие к звезде
                </div>          
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Любительский телескоп с 90-кратным увеличением
                </div>                              
            </div>
        </div>
        """
    elif 6 > product.attr.magnitude >= 5:
        template = """
        <div class="tooltip-present-wrapper">
            <div class="tooltip-present-title">
                Набор Вечность
            </div>
            <div class="tooltip-present-detail">
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Регистрация звезды в международном звёздном каталоге IOASA
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Электронное досье звезды
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Спутниковая фотография с расположением звезды на карте звёздного неба
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Официальный сертификат в металлической рамке, подтверждающий владение звездой
                </div>
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды
                </div>  
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Послание или пожелание на свитке с сургучной печатью
                </div>                 
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Светящаяся в темноте карта звездного неба
                </div>   
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Персональное видеопутешествие к звезде
                </div>          
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Любительский телескоп с 90-кратным увеличением
                </div>       
                <div class="row tooltip-present-detail-unit">
                    <div class="star-bullit">
                        <img src="/static/img/star-bullit.png">
                    </div>
                    Оригинальные наручные часы бренда КОСМОС
                </div>                            
            </div>
        </div>
        """
    return mark_safe(template)


@register.simple_tag (name="star_description")
def get_magnitude(product):

    template_white = """
        <div class="star-description">
            <p>Большие и ослепительно яркие белые звезды формируют основу видимого нами звездного неба. И хотя белые 
            звёзды составляют не более 4% от всех известных нам небесных светил,  36 % самых ярких, видимых 
            невооруженным глазом звёзд являются белыми звёздами. Самые яркие звёзды - Сириус и Канопус - также являются 
            белыми звёздами.</p>
            <p>Большая часть белых звёзд, так называемые белые звёзды главной последовательности, относятся к 
            спектральным классам A и F. Температура на их поверхности колеблется в диапазоне 6000К - 10000К, их масса и 
            радиус до 2 раз больше солнечной, а светимость до 25 раз выше светимости солнца. Несмотря на яркость и 
            температуру белых звёзд, они относительно спокойны: на их поверхности не бывает сильных звездных ветров и 
            вспышек, они почти не имеют рентгеновского излучения и таким образом могут обеспечить стабильность 
            атмосферы окружающих их планет, необходимую для возникновения жизни. Белые звёзды главной 
            последовательности живут около 2,5 миллиардов лет и, как и и остальные звезды главной последовательности, 
            исчерпав водород  превращаются в красных гигантов.</p>
            <p>Белые гиганты по своим характеристикам схожи с голубыми гигантами и отличаются более низкой температурой 
            на своей поверхности. Белыми гигантами становятся наиболее массивные звёзды главной последовательности, 
            которые исчерпав водород, проводят непродолжительный отрезок жизни в качестве голубых или белых 
            звёзд - гигантов, и впоследствии становятся красными сверхгигантами. </p> 
            <p>Белые сверхгиганты - одни из самых больших и ярких звёзд в нашей Вселенной. Одной из таких звёзд является 
            Денеб - самая далекая из самых ярких звёзд солнечного неба. Её радиус равен расстоянию от Солнца до Земли, 
            а светимость в 200000 раз больше светимости Солнца. За один день Денеб излучает больше света, чем Солнце 
            за 140 лет. Если бы Денеб находился бы от нас на том же расстоянии, что и Сириус, то он светил бы 
            ярче Лун</p> 
            <p>Самые известные белые звёзды: Полярная звезда, Сириус, Канопус, Денеб, Вега, Альтаир, Фомальгаут, 
            Процион, Кастор и Алиот.</p> 
        </div>
        """
    template_yellow = """
        <div class="star-description">
            <p>Среди всех звёзд в галактике Млечный Путь только 7.5% звёзд являются жёлтыми 
            звёздами, однако именно этот тип звёзд самый значимый для всего человечества. Солнце, источник жизни на 
            Земле, самая близкая и важная звезда для всех нас, является жёлтой звездой. К жёлтым звездам относятся любые 
            звёзды спектрального класса G. Солнце - это жёлтый карлик со спектральным классом G2V.</p>
            <p>Температура на поверхности жёлтых карликов находится в диапазоне 5000 - 6000К, масса и радиус 
            подобных звёзд составляет от 0,8 до 1,2 массы солнца, а светимость от 0,5 до 1,5 солнечной светимости. 
            Главным источником энергии жёлтых карликов является термоядерный синтез гелия из водорода. Каждую секунду 
            звёзды подобные Солнцу превращают 600 миллионов тонн водорода в гелий, в результате чего 4 миллиона тонн 
            вещества становятся энергией. Атмосфера желтых звёзд помимо водорода и гелия содержит ионы кальция, железа, 
            углерода, хрома и других элементов. Жёлтые карлики живут около 10 миллиардов лет, и в конце жизни, когда 
            звезды израсходуют водород и гелий, они многократно увеличиваются в размерах и превращаются в красных 
            гигантов.</p>
            <p>Около четверти всех жёлтых звезд являются звёздами - гигантами. Жёлтые гиганты составляют 10% от всех 
            звёзд - гигантов в нашей галактике. Жёлтыми гигантами становятся жёлтые и оранжевые звёзды главной 
            последовательности массой от 0,5 до 11 солнечной на поздних этапах эволюции на пути к превращению в красного 
            гиганта.</p> 
            <p>Сверхмассивные жёлтые звёзды называются жёлтыми сверхгигантами, и это одни из самых редких звёзд 
            во вселенной. Жёлтыми сверхгигантами становятся звезды главной последовательности класса O и B, исчерпавшие 
            водород. Их масса в 12 - 20 раз больше массы солнца, радиус в 30 - 300 раз больше радиуса солнца, 
            а светимость в 1000 - 100000 раз больше солнечной.</p> 
            <p>Самые известные жёлтые звёзды: Солнце, Капелла, Толиман, Хара, Арнеб, Муфрид, Садальсууд, Альшаин, 
            Виндемиатрикс, Садальмелик и Везен.</p> 
        </div>
        """
    template_orange = """
        <div class="star-description">
            <p>Оранжевые звёзды составляют 12% от всех звёзд нашей Галактики и относятся к спектральному классу K. Они 
            имеют слабо выраженные линии водорода, содержат в своей атмосфере нейтральные металлы, такие как магний, 
            железо и кремний и излучают приятный жёлто - оранжевый свет.</p>
            <p>40% оранжевых звёзд относятся к звёздам главной последовательности и именуются оранжевыми карликами. Эти 
            звёзды имеют температуру поверхности 3900К - 5200К, 0,5 - 0,8 солнечных масс и светимость 0,1 - 0,6 от 
            светимости солнца. Оранжевые карлики представляют особый интерес для астрономов как главные кандидаты в 
            поиске внеземных цивилизаций. Эти стабильные звёзды существуют 15 - 30 миллиардов лет, достаточное время для 
            возникновения жизни на  окружающих их планетах, они довольно яркие и поддерживают вокруг себя обширную 
            зону обитаемости, а также достаточно спокойные в плане солнечной активности, что снижает риск потери 
            атмосферы в результате солнечных вспышек.</p>
            <p>Оставшиеся 60% оранжевых звёзд относятся к звёздам - гигантам. Оранжевые гиганты - это короткая, в 
            масштабах жизни звезды, стадия сошедших с главной последовательности звёзд на пути к становлению красными 
            гигантами. Эти звёзды более горячие, чем красные гиганты и имеют меньший радиус. Поллукс, ярчайшая звезда в 
            созвездии Близнецы и одна из  самых ярких звёзд звёздного неба является оранжевым гигантом. Оранжевые 
            гиганты более редкие, чем красные, но довольно яркие, чтобы составлять основу видимых оранжевых звёзд 
            звездного неба.</p> 
            <p>Оранжевые сверхгиганты - это класс звёзд, очень похожих по своим свойствам на красных сверхгигантов. Они 
            образуются в результате эволюции массивных звёзд главной последовательности спектрального класса O и B. Их 
            радиус составляет тысячи радиусов Солнца, а светимость сотни тысяч солнечной. </p> 
            <p>Самые известные оранжевые звёзды: Арктур, Поллукс, Альдебаран, Дубхе, Авиор, Атрия, Альфард, Хамаль, 
            Альгиеба, Дифда и Шедар.</p> 
        </div>
        """
    template_blue = """
        <div class="star-description">
            <p>Голубые звёзды - самые яркие, горячие, массивные и редкие звёзды в известной нам Вселенной. Мы можем 
            наблюдать их яркий свет даже из далёких галактик. Эти голубые светила служат маяками, благодаря которым мы 
            узнаем о масштабах всего видимого пространства. К голубым звёздам относятся звёзды со спектральными классами 
            O и B.</p>
            <p>Голубые звёзды главной последовательности спектрального класса B имеют температуру поверхности 
            10000К - 30000К, их масса в 2 - 16 раз больше массы Солнца, радиус в 1,6 - 6,6 раз, а светимость в 
            25 - 300000 раз больше солнечной. Лишь 1 из 800 звёзд нашей галактики относится к голубым звёздам класса B. 
            Эти звёзды не имеют короны и зоны конвекции, а их продолжительность жизни составляет от 10 миллионов до 
            1,7 миллиардов лет. Звёзды класса O  это самые массивные и яркие звёзды главной последовательности. Они 
            чрезвычайно редки - всего одна звезда из 3000000 является звездой спектрального класса O. Их масса 
            от 15 до 90 раз больше массы солнца, температура поверхности 30000К - 50000К, а светимость 
            от 40000 до 1000000 раз выше светимости Солнца. Все звёзды класса O очень молодые, так как продолжительность 
            их жизни составляет всего несколько миллионов лет. Израсходовав  водород, голубые звёзды главной 
            последовательности схлопываются и превращаются в сверхгигантов.</p>
            <p>Голубые гиганты происходят из звёзд главной последовательности, которые только начали расширяться, 
            израсходовав термоядерное топливо. Голубые гиганты встречаются намного реже красных гигантов, так как могут 
            образовываться только из более массивных и реже встречающихся звёзд. Голубые гиганты имеют радиус всего 
            5 - 10 раз больше радиуса Солнца, что немного по сравнению с красными гигантами, чей радиус может быть 
            в 100 раз больше.</p> 
            <p>Голубые сверхгиганты - это горячие и яркие звёзды с массой в 10 - 50 солнечных масс. Из-за огромной массы 
            их жизнь крайне недолгая по меркам звёзд - всего 10 - 50 миллионов лет. Несмотря на их редкость и 
            малочисленность, их яркость, которая может быть в 10 миллионов раз больше яркости Солнца, позволяет увидеть 
            их на небе даже с огромного расстояния.</p> 
            <p>Самые известные голубые звёзды: Ригель, Ахернар, Хадар, Акрукс, Спика, Бекрукс, Регул,  Беллатрикс, 
            Альнаир, Адара и Шаула.</p> 
        </div>
        """
    template_red = """
        <div class="star-description">
            <p>Красные звёзды - самые холодные звёзды в нашей галактике и, вполне вероятно, во всей Вселенной. К красным 
            звёздам относят звёзды спектрального класса M, а температура на их поверхности составляет всего 2400К - 3700К. 
            И хотя у двух самых известных типов красных звёзд - красных карликов и красных гигантов - совпадают цвет и 
            температура поверхности, по своему происхождению и по своим свойствам это два совершенно разных типа небесных 
            объектов.</p>
            <p>Красные звезды главной последовательности, или, как их еще называют, красные карлики - это самые 
            распространенные звёзды в галактике Млечный Путь. 75% известных нам звезд являются красными карликами. 
            Самая близкая к нам звезда, Проксима Центавра, является красным карликом. Вторая по близости звёздная система, 
            звезда Барнарда, ещё известная как звезда-беглянка, также является красным карликом. Но несмотря на такую 
            частоту красных карликов, эти звёзды имеют крайне низкую светимость. Самый яркий красный карлик - звезда HD 202560 
            в созвездии Микроскоп, которая находится в 12 световых годах от нас, имеет звёздную величину всего 6,7, что означает, 
            что его можно с трудом увидеть только при благоприятных условиях. Из низкой светимости красных карликов следует то, 
            что они очень медленно расходуют своё термоядерное топливо, и поэтому они - самые долгоживущие звёзды 
            главной последовательности. В среднем красные карлики могут существовать 10 триллионов лет, что в тысячу раз 
            превышает срок жизни Солнца и в 500 раз больше возраста Вселенной. </p>
            <p>Красные гиганты - это последняя форма в эволюции сошедших с главной последовательности звёзд - гигантов. 
            Звёзды, исчерпавшие водород для термоядерной реакции в своём ядре продолжают термоядерную реакцию с участием 
            водорода в своей оболочке, что приводит к резкому увеличению их радиуса и светимости. В среднем радиус красных гигантов 
            составляет 200 радиусов Солнца, а светимость в 75 раз больше солнечной светимости. Красные гиганты существуют 
            от 100 миллионов до нескольких миллиардов лет, и, исчерпав водород в своей оболочке, сбрасывают её, а 
            ядро звезды сжимается, превращаясь в компактную звезду, состоящую из электронно-ядерной плазмы, лишённую источников 
            термоядерной энергии - белого карлика.</p> 
            <p>Красные сверхгиганты - это самые большие по объему звёзды во Вселенной. Их радиус может составлять тысячи 
            радиусов Солнца. Эти массивные и яркие звёзды имеют крайне небольшой срок жизни - всего несколько 
            десятков миллионов, но несмотря на свою редкость и короткую жизнь их яркость в 10000 - 100000 светимости Солнца 
            позволяет увидеть эти звёзды даже с самых отдаленных уголков нашей галактики.</p> 
            <p>Самые известные красные звёзды: Бетельгейзе, Антарес, Гакрукс, Мирах, Груид и Шеат.</p> 
        </div>
        """
    template_double = """
        <div class="star-description">
            <p>Звёздные системы, состоящие из двух гравитационно связанных звёзд, вращающихся вокруг общего центра массы 
            называют двойными звёздами. Двойные звёзды достаточно широко распространены в нашей галактике - почти половина 
            всех окружающих нас звёзд, включая звёзды, которые мы видим на ночном небе, на самом деле, являются 
            двойными звёздами. Ближайшая к нам звёздная система, Альфа Центавра, является двойной звездой. Другим известным 
            примером двойной системы звёзд является Сириус - яркая белая звезда Сириус A вращается вместе с еле уловимым 
            белым карликом Сириусом B. </p>
            <p>Чаще всего двойные звёзды образуются почти одновременно в результате разделения звёздного протооблака на 
            ранних этапах формирования звезды. Звёзды изначально стремятся уравновесить массу между собой, но впоследствии 
            между звёздами может начаться перетекание массы, в результате чего одна из звёзд может значительно увеличить 
            массу за счет своего соседа. Перетекание массы может проходить по разным сценариям. Иногда одна звезда полностью 
            поглощает звезду - соседа, а иногда звёзды попеременно обмениваются массой, создавая новоподобные вспышки. </p>
            <p>Если в двойной звёздной системе один из компонентов оказывается красным гигантом, а второй - белым карликом, 
            то в такой системе может вспыхнуть новая звезда, или нова. Новая звезда, вразрез своему названию, характеризует 
            не рождение звезды, а яркую вспышку, на короткое время увеличивающую светимость звезды на десять порядков. 
            Белый карлик, будучи сверхкомпактной звездой, лишенной водорода и термоядерной реакции, захватывает богатую 
            водородом оболочку красного гиганта. При накоплении критической массы в белом карлике вновь запускается 
            термоядерная реакция, но ввиду его высокой плотности, водород внутри звезды не начинает постепенно прогорать, 
            а происходит детонация, в результате которой огромной количество звёздного вещества выбрасывается в 
            открытый космос. Из выброшенного вещества впоследствии образуются новые звёзды и планеты, тем самым завершая 
            цикл круговорота жизни во Вселенной.</p> 
        </div>
        """

    if product.product_class_id == 1:
        template = template_white

    if product.product_class_id == 2:
        template = template_yellow

    if product.product_class_id == 3:
        template = template_orange

    if product.product_class_id == 4:
        template = template_blue

    if product.product_class_id == 5:
        template = template_red

    if product.product_class_id == 6:
        template = template_double

    if product.product_class_id == 7:

        if product.attr.starclass == 'Белая звезда':
            template = template_white

        if product.attr.starclass == 'Желтая звезда':
            template = template_white

        if product.attr.starclass == 'Оранжевая звезда':
            template = template_white

        if product.attr.starclass == 'Голубая звезда':
            template = template_white

        if product.attr.starclass == 'Красная звезда':
            template = template_white

        if product.attr.starclass == 'Двойная звезда':
            template = template_double

    return mark_safe(template)


@register.simple_tag (name="detail_present")
def get_magnitude(product):
    if 10 > product.attr.magnitude >= 9:
        template = """
        <div class="present-wrapper">
            <div class="magnitude-description">
                <p>Астрономы насчитывают около 300000 звёзд девятой величины на звёздном небе. Звёзды девятой величины 
                слишком тусклые, чтобы было возможно увидеть их невооруженным глазом или в бинокль, однако их можно
                 увидеть в любительский телескоп со стократным увеличением.</p>
            </div>
            <div class="present-title">
                <h2>Подарочный набор <span class="present-title-name">Электронный</h2>
                <p>В стоимость подарка входит:</p>
            </div>
            <div class="present-detail">
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-registration.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Регистрация звезды в международном звёздном каталоге IOASA</h3>   
                            <p>Имя человека, которому вы подарили звезду и характеристика звезды регистрируются в каталоге на 
                            сайте международной организации и на главной странице нашего сайта. Имя звезды и подробная 
                            информация о ней будут также опубликованы в ежегодном печатном звёздном каталоге IOASA тиражом 2000
                            экземпляров, который можно найти в библиотеках крупнейших университетов мира.</p> 
                        </div> 
                    </div>                 
                </div>
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-dosier.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Электронное досье звезды</h3>   
                            <p>Персональная интернет - страница с детальной информацией и изображением звезды на нашем сайте. 
                            Доступ к странице предоставляется навсегда.</p> 
                        </div> 
                    </div>                 
                </div>         
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-starphoto.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Спутниковая фотография с расположением звезды на карте звёздного неба</h3>   
                            <p>Настоящая фотография звезды, сделанная орбитальным телескопом с точной и подробной информацией о 
                            её расположении на звездном небе. Вы всегда легко и быстро сможете найти свою звезду на небосклоне. 
                            Фотография публикуются в электронном досье звезды.</p> 
                        </div> 
                    </div>                 
                </div>
            </div>
        </div>
        """
    if 9 > product.attr.magnitude >= 8:
        template = """
        <div class="present-wrapper">
            <div class="magnitude-description">
                <p>На звёздном небе насчитывается 78000 звёзд восьмой величины. Эти звёзды нельзя увидеть невооруженным
                глазом, но они довольно яркие, чтобы их можно было рассмотреть в бинокль, подзорную трубу или 
                небольшой любительский телескоп.</p>
            </div>
            <div class="present-title">
                <h2>Подарочный набор <span class="present-title-name">Стандарт</h2>
                <p>В стоимость подарка входит:</p>
            </div>
            <div class="present-detail">
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-registration.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Регистрация звезды в международном звёздном каталоге IOASA</h3>   
                            <p>Имя человека, которому вы подарили звезду и характеристика звезды регистрируются в каталоге на 
                            сайте международной организации и на главной странице нашего сайта. Имя звезды и подробная 
                            информация о ней будут также опубликованы в ежегодном печатном звёздном каталоге IOASA тиражом 2000
                            экземпляров, который можно найти в библиотеках крупнейших университетов мира.</p> 
                        </div> 
                    </div>                 
                </div>
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-dosier.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Электронное досье звезды</h3>   
                            <p>Персональная интернет - страница с детальной информацией и изображением звезды на нашем сайте. 
                            Доступ к странице предоставляется навсегда.</p> 
                        </div> 
                    </div>                 
                </div>         
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-starphoto.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Спутниковая фотография с расположением звезды на карте звёздного неба</h3>   
                            <p>Настоящая фотография звезды, сделанная орбитальным телескопом с точной и подробной информацией о 
                            её расположении на звездном небе. Вы всегда легко и быстро сможете найти свою звезду на небосклоне. 
                            Фотография публикуются в электронном досье звезды.</p> 
                        </div> 
                    </div>                 
                </div>                             
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-certificate.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Официальный сертификат в металлической рамке, подтверждающий владение звездой</h3>   
                            <p>Роскошный и стильный сертификат с голограммой IOASA в красивой металлической рамке с именем
                            звезды и ее подробной характеристикой, который прекрасно подойдет любому интерьеру и будет всегда
                            напоминать о подарившем её человеке.</p> 
                        </div> 
                    </div>                 
                </div>    
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-qr.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды</h3>   
                            <p>Стилизованный QR-код в фоторамке в одно мгновение перенесет вас к электронному досье вашей 
                            звезды. Наведите камеру вашего смартфона на изображение и на экране появится полная и подробная 
                            информация о принадлежащем Вам небесном светиле.</p> 
                        </div> 
                    </div>                 
                </div>      
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-message.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Послание или пожелание на свитке с сургучной печатью</h3>   
                            <p>Оставьте своё личное послание на свитке человеку, которому дарите звезду. Пожелайте успехов, 
                            удачи или признайтесь в любви - ваша фантазия ничем не ограничена.</p> 
                        </div> 
                    </div>                 
                </div>                
            </div>
        </div>
        """
    if 8 > product.attr.magnitude >= 7:
        template = """
        <div class="present-wrapper">
            <div class="magnitude-description">
                <p>Всего на звёздном небе можно насчитывается 27000 звёзд седьмой величины. Звёзды седьмой величины 
                можно увидеть невооруженном только при очень хорошей видимости, за городом при абсолютно тёмном небе, 
                поэтому лучше их рассматривать в бинокль или небольшой телескоп.</p>
            </div>
            <div class="present-title">
                <h2>Подарочный набор <span class="present-title-name">Эксклюзив</h2>
                <p>В стоимость подарка входит:</p>
            </div>
            <div class="present-detail">
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-registration.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Регистрация звезды в международном звёздном каталоге IOASA</h3>   
                            <p>Имя человека, которому вы подарили звезду и характеристика звезды регистрируются в каталоге на 
                            сайте международной организации и на главной странице нашего сайта. Имя звезды и подробная 
                            информация о ней будут также опубликованы в ежегодном печатном звёздном каталоге IOASA тиражом 2000
                            экземпляров, который можно найти в библиотеках крупнейших университетов мира.</p> 
                        </div> 
                    </div>                 
                </div>
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-dosier.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Электронное досье звезды</h3>   
                            <p>Персональная интернет - страница с детальной информацией и изображением звезды на нашем сайте. 
                            Доступ к странице предоставляется навсегда.</p> 
                        </div> 
                    </div>                 
                </div>         
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-starphoto.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Спутниковая фотография с расположением звезды на карте звёздного неба</h3>   
                            <p>Настоящая фотография звезды, сделанная орбитальным телескопом с точной и подробной информацией о 
                            её расположении на звездном небе. Вы всегда легко и быстро сможете найти свою звезду на небосклоне. 
                            Фотография публикуются в электронном досье звезды.</p> 
                        </div> 
                    </div>                 
                </div>                             
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-certificate.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Официальный сертификат в металлической рамке, подтверждающий владение звездой</h3>   
                            <p>Роскошный и стильный сертификат с голограммой IOASA в красивой металлической рамке с именем
                            звезды и ее подробной характеристикой, который прекрасно подойдет любому интерьеру и будет всегда
                            напоминать о подарившем её человеке.</p> 
                        </div> 
                    </div>                 
                </div>    
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-qr.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды</h3>   
                            <p>Стилизованный QR-код в фоторамке в одно мгновение перенесет вас к электронному досье вашей 
                            звезды. Наведите камеру вашего смартфона на изображение и на экране появится полная и подробная 
                            информация о принадлежащем Вам небесном светиле.</p> 
                        </div> 
                    </div>                 
                </div>      
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-message.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Послание или пожелание на свитке с сургучной печатью</h3>   
                            <p>Оставьте своё личное послание на свитке человеку, которому дарите звезду. Пожелайте успехов, 
                            удачи или признайтесь в любви - ваша фантазия ничем не ограничена.</p> 
                        </div> 
                    </div>                 
                </div>     
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-map.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Светящаяся в темноте карта звездного неба</h3>   
                            <p>Фирменная астрономическая карта на мелованной бумаге размером 40 см х 83 см. Звёздная карта 
                            накапливает свет в течение дня и светится в темноте. Карта идёт в комплекте с фирменным тубусом. 
                            Звёздная карта - это прекрасный и познавательный подарок, который не оставит равнодушным никого.</p> 
                        </div> 
                    </div>                 
                </div>       
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-video.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Персональное видеопутешествие к звезде</h3>   
                            <p>Уникальное и реалистичное составленное вручную видеопутешествие от Земли до Вашей звезды. 
                            Путешествие сквозь пространство время позволит увидить Вам вашу звезду в непосредственной близости
                            и оставить любое пожелание в течение межзвёздного полёта.</p> 
                        </div> 
                    </div>                 
                </div>                                                                                            
            </div>
        </div>
        """
    if 7 > product.attr.magnitude >= 6:
        template = """
        <div class="present-wrapper">
            <div class="magnitude-description">
                <p>На звёздном небе присутствует всего 9900 звёзд шестой величины. Эти звёзды довольно яркие и их 
                можно увидеть невооруженным глазом ночью в безоблачную погоду. Многие из этих звёзд были известны 
                древнейшим астроном и нанесены на самые ранние карты звездного неба.</p>
            </div>
            <div class="present-title">
                <h2>Подарочный набор <span class="present-title-name">Премиум</h2>
                <p>В стоимость подарка входит:</p>
            </div>
            <div class="present-detail">
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-registration.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Регистрация звезды в международном звёздном каталоге IOASA</h3>   
                            <p>Имя человека, которому вы подарили звезду и характеристика звезды регистрируются в каталоге на 
                            сайте международной организации и на главной странице нашего сайта. Имя звезды и подробная 
                            информация о ней будут также опубликованы в ежегодном печатном звёздном каталоге IOASA тиражом 2000
                            экземпляров, который можно найти в библиотеках крупнейших университетов мира.</p> 
                        </div> 
                    </div>                 
                </div>
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-dosier.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Электронное досье звезды</h3>   
                            <p>Персональная интернет - страница с детальной информацией и изображением звезды на нашем сайте. 
                            Доступ к странице предоставляется навсегда.</p> 
                        </div> 
                    </div>                 
                </div>         
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-starphoto.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Спутниковая фотография с расположением звезды на карте звёздного неба</h3>   
                            <p>Настоящая фотография звезды, сделанная орбитальным телескопом с точной и подробной информацией о 
                            её расположении на звездном небе. Вы всегда легко и быстро сможете найти свою звезду на небосклоне. 
                            Фотография публикуются в электронном досье звезды.</p> 
                        </div> 
                    </div>                 
                </div>                             
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-certificate.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Официальный сертификат в металлической рамке, подтверждающий владение звездой</h3>   
                            <p>Роскошный и стильный сертификат с голограммой IOASA в красивой металлической рамке с именем
                            звезды и ее подробной характеристикой, который прекрасно подойдет любому интерьеру и будет всегда
                            напоминать о подарившем её человеке.</p> 
                        </div> 
                    </div>                 
                </div>    
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-qr.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды</h3>   
                            <p>Стилизованный QR-код в фоторамке в одно мгновение перенесет вас к электронному досье вашей 
                            звезды. Наведите камеру вашего смартфона на изображение и на экране появится полная и подробная 
                            информация о принадлежащем Вам небесном светиле.</p> 
                        </div> 
                    </div>                 
                </div>      
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-message.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Послание или пожелание на свитке с сургучной печатью</h3>   
                            <p>Оставьте своё личное послание на свитке человеку, которому дарите звезду. Пожелайте успехов, 
                            удачи или признайтесь в любви - ваша фантазия ничем не ограничена.</p> 
                        </div> 
                    </div>                 
                </div>     
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-map.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Светящаяся в темноте карта звездного неба</h3>   
                            <p>Фирменная астрономическая карта на мелованной бумаге размером 40 см х 83 см. Звёздная карта 
                            накапливает свет в течение дня и светится в темноте. Карта идёт в комплекте с фирменным тубусом. 
                            Звёздная карта - это прекрасный и познавательный подарок, который не оставит равнодушным никого.</p> 
                        </div> 
                    </div>                 
                </div>       
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-video.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Персональное видеопутешествие к звезде</h3>   
                            <p>Уникальное и реалистичное составленное вручную видеопутешествие от Земли до Вашей звезды. 
                            Путешествие сквозь пространство время позволит увидить Вам вашу звезду в непосредственной близости
                            и оставить любое пожелание в течение межзвёздного полёта.</p> 
                        </div> 
                    </div>                 
                </div>           
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-telescope.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Любительский телескоп с 90 - кратным увеличением</h3>   
                            <p>Телескоп для наблюдений за звёздным небом в удобном противоударном кейсе. 90 - кратное 
                            увеличение позолит вам легко наблюдать любые космические объекты до 10 звёздной величины. 
                            Почуствуйте себя настоящим астрономом наблюдая за звёздами и планетами в удобный и простой в 
                            настройке телескоп - рефрактор. </p> 
                        </div> 
                    </div>                 
                </div>                                                                                 
            </div>
        </div>
        """
    if 6 > product.attr.magnitude >= 5:
        template = """
        <div class="present-wrapper">
            <div class="magnitude-description">
                <p>На ночном небе можно увидеть только лишь около 1900 звёзд пятой величины. Эти яркие звёзды легко 
                видны невооруженным глазом, даже не смотря на огни города. Это самые яркие звёзды, которые могут 
                быть внесены в каталог IOASA, так как звёзды болшей светимости уже имеют свои традиционные имена.</p>
            </div>
            <div class="present-title">
                <h2>Подарочный набор <span class="present-title-name">Вечность</h2>
                <p>В стоимость подарка входит:</p>
            </div>
            <div class="present-detail">
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-registration.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Регистрация звезды в международном звёздном каталоге IOASA</h3>   
                            <p>Имя человека, которому вы подарили звезду и характеристика звезды регистрируются в каталоге на 
                            сайте международной организации и на главной странице нашего сайта. Имя звезды и подробная 
                            информация о ней будут также опубликованы в ежегодном печатном звёздном каталоге IOASA тиражом 2000
                            экземпляров, который можно найти в библиотеках крупнейших университетов мира.</p> 
                        </div> 
                    </div>                 
                </div>
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-dosier.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Электронное досье звезды</h3>   
                            <p>Персональная интернет - страница с детальной информацией и изображением звезды на нашем сайте. 
                            Доступ к странице предоставляется навсегда.</p> 
                        </div> 
                    </div>                 
                </div>         
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-starphoto.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Спутниковая фотография с расположением звезды на карте звёздного неба</h3>   
                            <p>Настоящая фотография звезды, сделанная орбитальным телескопом с точной и подробной информацией о 
                            её расположении на звездном небе. Вы всегда легко и быстро сможете найти свою звезду на небосклоне. 
                            Фотография публикуются в электронном досье звезды.</p> 
                        </div> 
                    </div>                 
                </div>                             
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-certificate.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Официальный сертификат в металлической рамке, подтверждающий владение звездой</h3>   
                            <p>Роскошный и стильный сертификат с голограммой IOASA в красивой металлической рамке с именем
                            звезды и ее подробной характеристикой, который прекрасно подойдет любому интерьеру и будет всегда
                            напоминать о подарившем её человеке.</p> 
                        </div> 
                    </div>                 
                </div>    
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-qr.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Сертификат QR-код в металлической рамке со ссылкой на электронное досье звезды</h3>   
                            <p>Стилизованный QR-код в фоторамке в одно мгновение перенесет вас к электронному досье вашей 
                            звезды. Наведите камеру вашего смартфона на изображение и на экране появится полная и подробная 
                            информация о принадлежащем Вам небесном светиле.</p> 
                        </div> 
                    </div>                 
                </div>      
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-message.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Послание или пожелание на свитке с сургучной печатью</h3>   
                            <p>Оставьте своё личное послание на свитке человеку, которому дарите звезду. Пожелайте успехов, 
                            удачи или признайтесь в любви - ваша фантазия ничем не ограничена.</p> 
                        </div> 
                    </div>                 
                </div>     
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-map.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Светящаяся в темноте карта звездного неба</h3>   
                            <p>Фирменная астрономическая карта на мелованной бумаге размером 40 см х 83 см. Звёздная карта 
                            накапливает свет в течение дня и светится в темноте. Карта идёт в комплекте с фирменным тубусом. 
                            Звёздная карта - это прекрасный и познавательный подарок, который не оставит равнодушным никого.</p> 
                        </div> 
                    </div>                 
                </div>       
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-video.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Персональное видеопутешествие к звезде</h3>   
                            <p>Уникальное и реалистичное составленное вручную видеопутешествие от Земли до Вашей звезды. 
                            Путешествие сквозь пространство время позволит увидить Вам вашу звезду в непосредственной близости
                            и оставить любое пожелание в течение межзвёздного полёта.</p> 
                        </div> 
                    </div>                 
                </div>           
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-telescope.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Любительский телескоп с 90 - кратным увеличением</h3>   
                            <p>Телескоп для наблюдений за звёздным небом в удобном противоударном кейсе. 90 - кратное 
                            увеличение позолит вам легко наблюдать любые космические объекты до 10 звёздной величины. 
                            Почуствуйте себя настоящим астрономом наблюдая за звёздами и планетами в удобный и простой в 
                            настройке телескоп - рефрактор. </p> 
                        </div> 
                    </div>                 
                </div>       
                <div class="present-detail-unit">
                    <div class="present-row">
                        <div class="present-row-image">
                            <img src="/static/img/gift-watches.png">
                        </div>
                        <div class="present-row-text">
                            <h3>Оригинальные наручные часы бренда КОСМОС</h3>   
                            <p>Оригинальные часы всемирно известного российского бренда КОСМОС. Тонкий и элегантный 
                            корпус, изогнутый циферблат, защищенный минеральным стеклом, и высокоточные японские 
                            механизмы - это неизменные характеристики часов бренда КОСМОС, благодаря которым они 
                            превосходят по качеству даже популярные швейцарские модели. Часы КОСМОС - это подарок, 
                            которого достойны только самые лучшие. </p> 
                        </div> 
                    </div>                 
                </div>                                                                                           
            </div>
        </div>
        """
    return mark_safe(template)


@register.simple_tag (name="star_price")
def get_price(product):
    strategy = Selector().strategy()
    info = strategy.fetch_for_product(product)
    if info.availability.is_available_to_buy:
        return str(info.price.incl_tax) + " ₽"
    else:
        return mark_safe('<span style="color: red">Звезда зарегестрирована</span>')
