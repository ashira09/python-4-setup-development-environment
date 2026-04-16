from db.db import connect_to_database
from dotenv import load_dotenv
from db.models import Base
from db.crud import CategoryCRUD, BookCRUD
from sqlalchemy.orm import Session
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

if db_host is None or db_port is None or db_name is None or db_user is None or db_password is None:
    raise Exception('Не все параметры указаны в .env!')

engine = connect_to_database(
    db_host = db_host,
    db_port = db_port,
    db_name = db_name,
    db_user = db_user,
    db_password = db_password
)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

categoryCRUD = CategoryCRUD()
bookCRUD = BookCRUD()

with Session(engine) as session:
    fiction_category = categoryCRUD.create_category(title='Фантастика', session=session)
    fantasy_category = categoryCRUD.create_category(title='Фэнтези', session=session)
    session.commit()

    tummannost_andromedy = bookCRUD.create_book(
        title="Туманность Андромеды", 
        description="«Туманность Андромеды» (1957) — классический роман отечественной научной фантастики и социальная утопия. Автор повествует о далеком будущем: межзвездные перелеты и невиданные научные свершения. Земля входит в мир Великого Кольца — содружество разумных цивилизаций, которые обмениваются культурным опытом и технологиями. Люди говорят на общем языке, расовые особенности начинают стираться, а средняя продолжительность жизни землянина — около 170 лет. Все силы, ранее задействованные для разрушения, используют на созидание и преобразование мира. Казалось бы, с какими трудностями может столкнуться человечество, если все так идеально?..", 
        price=479, 
        url="https://www.chitai-gorod.ru/product/tumannost-andromedy-3026850",
        category_id=fiction_category.id,
        session=session
    )
    mi = bookCRUD.create_book(
        title="Мы",
        description='Знаковый роман, с которого официально отсчитывают само существование жанра "антиутопия" Запрещенный в советский период, теперь он считается одним из классических произведений не только русской, но и мировой литературы ХХ века. Роман об "обществе равных", в котором человеческая личность сведена к "нумеру". В нем унифицировано все — одежда и квартиры, мысли и чувства. Нет ни семьи, ни прочных привязанностей... Но можно ли вытравить из человека жажду свободы, пока он остается человеком?', 
        price=299,
        url="https://www.chitai-gorod.ru/product/my-2898879",
        category_id=fiction_category.id,
        session=session
    )
    dom_sekretov = bookCRUD.create_book(
        title="Дом секретов",
        description='Трое детей — Брендан, Корделия и Элеонора Уолкер — переезжают с родителями из удобного и суперсовременного дома в роскошный викторианский особняк, прежним хозяином которого был мрачный писатель-фантаст. Никто даже не задумывается, почему хозяева продали дом за такую низкую цену, что за странная женщина живет по соседству и как далеко может завести сила воображения писателя. Стоило только семейству заселиться, как события обрушиваются на них стремительно. Разражается шторм, родители исчезают, а сами дети вместе с домом попадают в девственный лес, где обитают самые невероятные существа…',
        price=460,
        url="https://www.chitai-gorod.ru/product/dom-sekretov-7622818",
        category_id=fantasy_category.id,
        session=session
    )
    vedmak_mech_prednaznacheniya = bookCRUD.create_book(
        title="Ведьмак. Меч Предназначения. (Иллюстрации Дениса Гордеева)",
        description='Ведьмак. Меч Предназначения. (Иллюстрации Дениса Гордеева)',
        price=1799,
        url="https://www.chitai-gorod.ru/product/vedmak-mech-prednaznacheniya-illyustracii-denisa-gordeeva-2491421",
        category_id=fantasy_category.id,
        session=session
    )
    session.commit()