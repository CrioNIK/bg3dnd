"""Human-reviewed Ukrainian localization overrides.

Keys are exact English source strings.  Keep contextual exceptions in UID_OVERRIDES.
"""


UID_OVERRIDES: dict[str, str] = {
    # Contextual corrections where an ambiguous official exact match is wrong here.
    "h5b423612ge7e5g8736gd607g7c134dc79c3a": "Артистичність",
    "hcb060b97gfe11gfd82gc6b9g3e44da81f15a": """Володіння зброєю: Послаблення

Якщо ви влучите в істоту цією зброєю, її наступний кидок атаки до початку вашого наступного ходу матиме заваду.""",
    "h0eb341bcgb4f9g7430gafc5g64f46cf69004": """Реагуванням ви можете накласти <LSTag Tooltip="Disadvantage">заваду</LSTag> на <LSTag Tooltip="AttackRoll">кидок атаки</LSTag> проти вас.

Якщо атака промахнеться, ви на 1 хід отримуєте <LSTag Tooltip="Advantage">перевагу</LSTag> на свій наступний кидок атаки проти нападника.

Застосувавши цю особливість, ви не зможете зробити це знову до завершення короткого або довгого відпочинку, якщо не витратите чарунку Магії договору (дія не потрібна), щоб відновити застосування.""",
    """You can imbue yourself with a primal power called <LSTag Type="Status" Tooltip="RAGE">Rage</LSTag>, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren’t wearing Heavy armor.

You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.""":
        """Ви можете сповнитися первісною силою, що зветься <LSTag Type="Status" Tooltip="RAGE">Люттю</LSTag> і наділяє надзвичайною міццю та витривалістю. Якщо на вас немає важких обладунків, ви можете увійти в Лють вторинною дією.

Кількість входжень у Лють указано для вашого рівня варвара у стовпці «Лють» таблиці особливостей варвара. Ви відновлюєте одне витрачене застосування після короткого відпочинку і всі витрачені застосування — після довгого.""",
    """You can weave fey magic into a song or dance to fill others with vigor. As a Bonus Action, you can expend one use of Bardic Inspiration and roll your Bardic Inspiration die. When you do so, choose a number of other creatures within [1] of yourself, up to your Charisma modifier (minimum of one creature).

Each of those creatures gains Temporary Hit Points equal to twice the number rolled on the Bardic Inspiration die, and each can move without provoking Opportunity Attacks until the end of its next turn.""":
        """Ви можете вплітати фейську магію в пісню чи танець, наповнюючи інших снагою. Вторинною дією ви можете витратити одне застосування Бардівського натхнення й кинути його кістку. Виберіть інших істот у межах [1] від вас у кількості, що не перевищує вашого модифікатора харизми (щонайменше одну істоту).

Кожна з цих істот отримує тимчасові очки здоров’я в кількості, що вдвічі перевищує результат кидка, і може переміщуватися, не провокуючи принагідних атак, до кінця свого наступного ходу.""",
    "Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Cleric cantrip.":
        "Могутнє проказування. Додайте свій модифікатор мудрості до шкоди, яку ви завдаєте будь-яким замовлянням клірика.",
    "Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Druid cantrip.":
        "Могутнє проказування. Додайте свій модифікатор мудрості до шкоди, яку ви завдаєте будь-яким замовлянням друїда.",
    "When a spell you cast with a spell slot restores Hit Points to a creature, that creature regains additional Hit Points on the turn you cast the spell. The additional Hit Points equal 2 plus the spell slot’s level.":
        "Коли проказане вами за допомогою чарунки закляття відновлює істоті очки здоров’я, у хід проказування вона відновлює додаткові очки здоров’я в кількості, що дорівнює 2 + рівень чарунки.",
    """You can use a Bonus Action to transform into a known Beast form using Wild Shape. You can end the transformation early as a Bonus Action. You can use Wild Shape twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest. When you assume a Wild Shape form, you gain a number of Temporary Hit Points equal to your Druid level. You can’t cast spells, but shape-shifting doesn’t break your Concentration or otherwise interfere with a spell you’ve already cast.""":
        "Ви можете вторинною дією скористатися «Дикою подобою» і перетворитися на відому вам форму звіра. Ви також можете достроково завершити перетворення вторинною дією. «Дику подобу» можна застосувати двічі. Одне витрачене застосування відновлюється після короткого відпочинку, а всі — після довгого. Набувши Дикої подоби, ви отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому рівню друїда. У цій формі ви не можете проказувати закляття, але перетворення не перериває вашого зосередження й не заважає вже проказаному закляттю.",
    "If you fail a saving throw, you can instead treat it as a success. Once you use this feature, you can’t use it again until you finish a Long Rest.":
        "Коли ви провалюєте кидок протидії, ви можете натомість вважати його успішним. Застосувавши цю особливість, ви не зможете зробити це знову до завершення довгого відпочинку.",
    """You gain the ability to heal yourself. As a Bonus Action, you can roll your Martial Arts die. You regain a number of Hit Points equal to the number rolled plus your Wisdom modifier (minimum of 1 Hit Point regained).

You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.""":
        """Ви навчаєтеся зцілювати себе. Вторинною дією киньте свою кістку Бойових мистецтв. Ви відновлюєте очки здоров’я в кількості, що дорівнює результату кидка + ваш модифікатор мудрості (щонайменше 1 очко).

Ви можете застосувати цю особливість стільки разів, скільки становить ваш модифікатор мудрості (щонайменше один раз). Усі витрачені застосування відновлюються після довгого відпочинку.""",
    """You can channel oath energy directly from the Outer Planes, using it to fuel magical effects. You start with one such effect: Divine Sense, which is described below. Other Paladin features give additional Channel Oath effect options. Each time you use this class’s Channel Oath, you choose which effect from this class to create.

You can use this class’s Channel Oath twice. You regain one of its expended uses when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest. You gain an additional use when you reach Paladin level 11.

If a Channel Oath effect requires a saving throw, the DC equals the spell save DC from this class’s Spellcasting feature.""":
        """Ви можете спрямовувати енергію обітниці безпосередньо із Зовнішніх планів і живити нею магічні ефекти. Спочатку вам доступний один такий ефект — «Божественне чуття», описане нижче. Інші особливості паладина дають додаткові варіанти ефектів Обітного наснаження. Застосовуючи Обітне наснаження цього класу, ви обираєте, який з його ефектів створити.

Обітне наснаження цього класу можна застосувати двічі. Одне витрачене застосування відновлюється після короткого відпочинку, а всі — після довгого. На 11-му рівні паладина ви отримуєте ще одне застосування.

Якщо ефект Обітного наснаження вимагає кидка протидії, його МС дорівнює МС протидії закляттям з особливості «Проказування» цього класу.""",
    "You always have the Divine Smite spell prepared. In addition, you can cast it without expending a spell slot, but you must finish a Long Rest before you can cast it in this way again.":
        "Ви завжди маєте підготовленою «Божу кару». Крім того, ви можете проказати її, не витрачаючи чарунки, але не зможете зробити це знову до завершення довгого відпочинку.",
    "You can cast Divine Smite without expending a spell slot, but you must finish a Long Rest before you can cast it in this way again.":
        "Ви можете проказати «Божу кару», не витрачаючи чарунки, але не зможете зробити це знову до завершення довгого відпочинку.",
    """You can call on the aid of an otherworldly steed. You always have the Find Steed spell prepared.

You can also cast the spell once without expending a spell slot, and you regain the ability to do so when you finish a Long Rest.""":
        """Ви можете покликати на допомогу потойбічного скакуна. Ви завжди маєте підготовленим закляття «Пошук скакуна».

Ви також можете один раз проказати це закляття, не витрачаючи чарунки, і відновлюєте цю змогу після довгого відпочинку.""",
    "You can also cast Find Steed once without expending a spell slot, and you regain the ability to do so when you finish a Long Rest.":
        "Ви також можете один раз проказати «Пошук скакуна», не витрачаючи чарунки, і відновлюєте цю змогу після довгого відпочинку.",
    """You always have the Hunter’s Mark spell prepared. You can cast it twice without expending a spell slot, and you regain all expended uses of this ability when you finish a Long Rest.

The number of times you can cast the spell without a spell slot increases when you reach certain Ranger levels, as shown in the Favored Enemy column of the Ranger Features table.""":
        """Ви завжди маєте підготовленою «Мітку мисливця». Ви можете двічі проказати її, не витрачаючи чарунки, і відновлюєте всі витрачені застосування цієї змоги після довгого відпочинку.

Кількість проказувань без витрати чарунки збільшується на певних рівнях слідопита, як указано у стовпці «Улюблений ворог» таблиці особливостей слідопита.""",
}

_MISPLACED_EXACT_OVERRIDES = {
    key: value for key, value in UID_OVERRIDES.items() if not key.startswith("h")
}
UID_OVERRIDES = {
    key: value for key, value in UID_OVERRIDES.items() if key.startswith("h")
}


EXACT_OVERRIDES: dict[str, str] = {
    # Spell/action titles, editorial batch 1 (A-C).
    "Abjure Foes": "Відлякування ворогів",
    "Abjure the Extraplanar": "Вигнання екстрапланарних істот",
    "Acid Blood": "Кислотна кров",
    "Activate Enervation": "Активувати виснаження",
    "Acumen": "Кмітливість",
    "Aganazzar's Scorcher": "Пекучий струмінь Аґанаццара",
    "Agile Strikes": "Спритні удари",
    "All Will Be Dust": "Усе стане прахом",
    "Arcane Alchemy": "Магічна алхімія",
    "Arcane Vigor": "Містична снага",
    "Arcane Vigor: D6": "Містична снага: d6",
    "Arcane Vigor: D8": "Містична снага: d8",
    "Arcane Vigor: D10": "Містична снага: d10",
    "Arcane Vigor: D12": "Містична снага: d12",
    "Armor Model": "Модель обладунків",
    "Armor of the Faithful": "Обладунки вірних",
    "Ashardalon's Stride": "Крок Ашардалона",
    "Astral Flood": "Астральний потоп",
    "Aura of Vitality": "Аура життєвої сили",
    "Ballistic Smite": "Балістична кара",
    "Ballistic Smite: Acid": "Балістична кара: кислота",
    "Ballistic Smite: Cold": "Балістична кара: холод",
    "Ballistic Smite: Fire": "Балістична кара: вогонь",
    "Ballistic Smite: Lightning": "Балістична кара: блискавка",
    "Ballistic Smite: Poison": "Балістична кара: отрута",
    "Ballistic Smite: Thunder": "Балістична кара: грім",
    "Balm of the Summer Court": "Бальзам Літнього двору",
    "Bastion of Law": "Бастіон закону",
    "Battle Medic": "Бойовий медик",
    "Beak": "Дзьоб",
    "Beguiling Magic: Charmed": "Зваблива магія: причарування",
    "Beguiling Magic: Frightened": "Зваблива магія: переляк",
    "Bind Pact Weapon (Necrotic Damage)": "Прив’язати зброю договору (некротична шкода)",
    "Bind Pact Weapon (Psychic Damage)": "Прив’язати зброю договору (психічна шкода)",
    "Bind Pact Weapon (Radiant Damage)": "Прив’язати зброю договору (променева шкода)",
    "Bite the Bullet": "Зціпити зуби",
    "Blessing of the Forge: Magic Armor": "Благословення кузні: магічні обладунки",
    "Blessing of the Forge: Magic Weapon": "Благословення кузні: магічна зброя",
    "Blessings of Moonlight": "Благословення місячного сяйва",
    "Blindfire": "Стрільба наосліп",
    "Blood Bolt": "Кривавий заряд",
    "Body Warping of Gorgoroth": "Викривлення тіла Ґорґорота",
    "Bolstering Flames": "Зміцнювальне полум’я",
    "Bolstering Touch": "Зміцнювальний дотик",
    "Bound Weapon: Primary": "Зв’язана зброя: основна",
    "Bound Weapon: Secondary": "Зв’язана зброя: другорядна",
    "Branches of the Tree": "Гілки Дерева",
    "Breath Weapon": "Дихальна зброя",
    "Burning Seals: Fire": "Пекучі печатки: вогонь",
    "Burning Seals: Necrotic": "Пекучі печатки: некротична енергія",
    "Cacophonic Shield": "Какофонічний щит",
    "Catapult": "Катапульта",
    "Celestial Resilience": "Небесна стійкість",
    "Celestial Revelation": "Небесне одкровення",
    "Chains of Judgement": "Ланцюги суду",
    "Charger: Unarmed Attack": "Нападник: беззбройна атака",
    "Circle of Power": "Коло сили",
    "Circle of the Land Spells": "Закляття Кола землі",
    "Circle of the Land Spells: Arid Land": "Закляття Кола землі: посушливий край",
    "Circle of the Land Spells: Polar Land": "Закляття Кола землі: полярний край",
    "Circle of the Land Spells: Temperate Land": "Закляття Кола землі: помірний край",
    "Circle of the Land Spells: Tropical Land": "Закляття Кола землі: тропічний край",
    "Circle of the Moon Spells": "Закляття Кола місяця",
    "Cloak of Shadow": "Плащ тіні",
    "Cloud Strike": "Хмарний удар",
    "Cloud’s Jaunt": "Хмарна мандрівка",

    # Spell/action titles, editorial batch 2 (C-E).
    "Conflagrant Channel": "Полум’яне спрямування",
    "Conjure Celestial": "Прикликати небесника",
    "Consume Darkness": "Поглинути темряву",
    "Controlled Channeling": "Кероване спрямування",
    "Controlled Channeling: Arsonist": "Кероване спрямування: палій",
    "Controlled Channeling: Avenger": "Кероване спрямування: месник",
    "Controlled Channeling: Beloved": "Кероване спрямування: улюбленець",
    "Controlled Channeling: Coward": "Кероване спрямування: боягуз",
    "Controlled Channeling: Fortune Teller": "Кероване спрямування: ворожбит",
    "Controlled Channeling: Renegade": "Кероване спрямування: відступник",
    "Controlled Channeling: Shade": "Кероване спрямування: тінь",
    "Controlled Channeling: Sharpshooter": "Кероване спрямування: влучний стрілець",
    "Controlled Channeling: Trickster": "Кероване спрямування: хитрун",
    "Controlled Channeling: Wayfarer": "Кероване спрямування: мандрівник",
    "Create Ice": "Створити лід",
    "Create Void": "Створити порожнечу",
    "Creeping Fog": "Повзучий туман",
    "Darkbolt": "Темна стріла",
    "Dawn": "Світанок",
    "Dazing Blast": "Ошелешливий вибух",
    "Deadly Archery": "Смертельна стрільба",
    "Death Armor": "Смертельні обладунки",
    "Defensive Field": "Захисне поле",
    "Deflect Attack: Redirect": "Відбиття атаки: переспрямування",
    "Devastator: Melee Weapon Attack": "Руйнівник: атака зброєю ближнього бою",
    "Devastator: Ranged Weapon Attack": "Руйнівник: атака зброєю дальнього бою",
    "Devastator: Unarmed Attack": "Руйнівник: беззбройна атака",
    "Disappearing Step": "Зникальний крок",
    "Dismiss Psychic Blades": "Прибрати психічні клинки",
    "Dismiss Shape-Shifter": "Скасувати подобу перевертня",
    "Divine Spark": "Божественна іскра",
    "Divine Spark: Heal": "Божественна іскра: зцілення",
    "Divine Spark: Necrotic Damage": "Божественна іскра: некротична шкода",
    "Divine Spark: Radiant Damage": "Божественна іскра: променева шкода",
    "Djinni’s Escape": "Втеча джина",
    "Dodge Roll": "Перекат",
    "Doom Song": "Пісня приречення",
    "Draconic Flight": "Драконячий політ",
    "Dragon Fear": "Драконячий страх",
    "Dragon Shape": "Подоба дракона",
    "Dragon's Breath": "Дихання дракона",
    "Dragon's Terror": "Драконячий жах",
    "Dread Allegiance": "Моторошна відданість",
    "Dread Allegiance: Bane": "Моторошна відданість: Бейн",
    "Dread Allegiance: Bhaal": "Моторошна відданість: Баал",
    "Dread Allegiance: Myrkul": "Моторошна відданість: Міркул",
    "Dreadful Step": "Моторошний крок",
    "Dreadful Strike (Melee)": "Жахливий удар (ближній бій)",
    "Dreadful Strike (Ranged)": "Жахливий удар (дальній бій)",
    "Dreadnaught": "Дредноут",
    "Dream": "Сон",
    "Dummy Spell": "Службове закляття",
    "Duplicitous Cantrip": "Двоїсте замовляння",
    "Duplicitous Casting": "Двоїсте проказування",
    "Eldritch Smite": "Потойбічна кара",
    "Eldritch Smite (Ranged)": "Потойбічна кара (дальній бій)",
    "Elemental Attunement": "Налаштування на стихії",
    "Elemental Burst": "Стихійний вибух",
    "Elemental Burst: Acid": "Стихійний вибух: кислота",
    "Elemental Burst: Cold": "Стихійний вибух: холод",
    "Elemental Burst: Fire": "Стихійний вибух: вогонь",
    "Elemental Burst: Lightning": "Стихійний вибух: блискавка",
    "Elemental Burst: Thunder": "Стихійний вибух: грім",
    "Elemental Exhalation": "Стихійний видих",

    # Spell/action titles, editorial batch 3 (E-I).
    "Elixir of the Colossus": "Еліксир колоса",
    "Elminster's Elusion": "Вислиз Ельмінстера",
    "Embolden Allies": "Підбадьорити союзників",
    "Encourage Ally": "Підбадьорити союзника",
    "Encouraging Song": "Підбадьорлива пісня",
    "Enervation": "Виснаження",
    "Erupting Blades": "Виверження клинків",
    "Experimental Elixir": "Експериментальний еліксир",
    "Exsanguinate": "Знекровити",
    "Extend Rage": "Подовжити лють",
    "Eyes of Night": "Очі ночі",
    "Fade to Black": "Згасання",
    "Family First": "Сім’я понад усе",
    "Fey Step": "Фейський крок",
    "Fey Step: Autumn": "Фейський крок: осінь",
    "Fey Step: Spring": "Фейський крок: весна",
    "Fey Step: Summer": "Фейський крок: літо",
    "Fey Step: Winter": "Фейський крок: зима",
    "Find Steed": "Знайти скакуна",
    "Finger Guns": "Пістолі з пальців",
    "Fire Dance": "Танець вогню",
    "Fire Rune": "Вогняна руна",
    "Fire Strike": "Вогняний удар",
    "Flamethrower": "Вогнемет",
    "Flurry of Harm": "Шквал кривди",
    "Flurry of Healing": "Шквал зцілення",
    "Force Ballista": "Силова баліста",
    "Force Demolisher: Pull": "Силовий руйнівник: притягнення",
    "Force Demolisher: Push": "Силовий руйнівник: відштовхування",
    "Force-Empowered Rend": "Підсилене силою роздирання",
    "Fortifying Soul": "Зміцнення душі",
    "Fount of Moonlight": "Джерело місячного сяйва",
    "Frightful Start": "Жахливий початок",
    "Frost Strike": "Морозний удар",
    "Giant Stature": "Велетенський зріст",
    "Giant’s Might": "Міць велета",
    "Gleam of Wrath": "Відблиск гніву",
    "Grand Strategist": "Великий стратег",
    "Green-Flame Blade": "Клинок зеленого полум’я",
    "Group Recovery": "Групове відновлення",
    "Guardian": "Вартовий",
    "Guiding Whispers": "Спрямувальний шепіт",
    "Hair Trigger": "Чутливий спуск",
    "Hand of Healing": "Рука зцілення",
    "Healing Hands": "Цілющі руки",
    "Healing Light": "Цілюще світло",
    "Healing Touch": "Цілющий дотик",
    "Hearth of Moonlight and Shadow": "Осередок місячного сяйва й тіні",
    "Heavenly Wings": "Небесні крила",
    "Hell’s Lash": "Батіг Пекла",
    "Heroic Soul": "Героїчна душа",
    "Hidden Paths": "Приховані шляхи",
    "Hill Strike": "Удар пагорба",
    "Holy Weapon": "Свята зброя",
    "Holy Weapon Burst": "Спалах святої зброї",
    "Holy Word": "Святе слово",
    "Horse Lord": "Володар коней",
    "Hungering Blade": "Голодний клинок",
    "Hunter’s Prey": "Здобич мисливця",
    "Improved Shillelagh": "Покращений дубець",
    "Infiltrator": "Диверсант",
    "Infused": "Насичення",
    "Infused: Acid": "Насичення: кислота",
    "Infused: Cold": "Насичення: холод",
    "Infused: Fire": "Насичення: вогонь",
    "Infused: Lightning": "Насичення: блискавка",
    "Infused: Poison": "Насичення: отрута",
    "Infused: Thunder": "Насичення: грім",

    # Spell/action titles, editorial batch 4 (I-R).
    "Innate Sorcery": "Вроджене чародійство",
    "Inner Radiance": "Внутрішнє сяйво",
    "Inspirational Dance": "Надихальний танець",
    "Inspired Eclipse": "Натхненне затемнення",
    "Inspiring Glory": "Надихальна слава",
    "Inspiring Movement": "Надихальний рух",
    "Invigorate": "Наснажити",
    "Invocation: Gift of the Protectors": "Інвокація: дар захисників",
    "Invoke Frost Rune": "Активувати руну морозу",
    "Invoke Hill Rune": "Активувати руну пагорба",
    "Invoke Stone Rune": "Активувати руну каменю",
    "Invoke Storm Rune": "Активувати руну бурі",
    "Jump Down": "Зістрибнути",
    "Kensei’s Shot": "Постріл кенсея",
    "Laeral's Silver Lance": "Срібний спис Лаераля",
    "Land’s Aid": "Допомога землі",
    "Large Form": "Велика подоба",
    "Level 10: Armor of Resistance": "Рівень 10: обладунки опору",
    "Level 10: Ring of Free Action": "Рівень 10: перстень вільної дії",
    "Level 10: Ring of Protection": "Рівень 10: перстень захисту",
    "Level 2: Alchemy Jug": "Рівень 2: алхімічний глек",
    "Level 2: Bag of Holding": "Рівень 2: бездонна торба",
    "Level 2: Goggles of Night": "Рівень 2: окуляри нічного бачення",
    "Level 2: Magic Shield": "Рівень 2: магічний щит",
    "Level 2: Magic Weapon": "Рівень 2: магічна зброя",
    "Level 2: Wand of the War Mage": "Рівень 2: жезл бойового мага",
    "Level 2: Wraps of Unarmed Power": "Рівень 2: обмотки сили беззбройного бою",
    "Level 6: Helm of Awareness": "Рівень 6: шолом пильності",
    "Level 6: Lantern of Revealing": "Рівень 6: ліхтар викриття",
    "Level 6: Magic Armor": "Рівень 6: магічні обладунки",
    "Level 6: Mind Sharpener": "Рівень 6: загострювач розуму",
    "Liar’s Dice": "Кості брехуна",
    "Life-Giving Force": "Життєдайна сила",
    "Lightning Launcher": "Блискавкомет",
    "Long Jump": "Стрибок у довжину",
    "Magic Initiate (Cleric): Cantrip": "Магічний хист (клірик): замовляння",
    "Magic Initiate (Cleric): Spell": "Магічний хист (клірик): закляття",
    "Magic Initiate (Druid): Cantrip": "Магічний хист (друїд): замовляння",
    "Magic Initiate (Druid): Spell": "Магічний хист (друїд): закляття",
    "Magic Initiate (Wizard): Cantrip": "Магічний хист (чарівник): замовляння",
    "Magic Initiate (Wizard): Spell": "Магічний хист (чарівник): закляття",
    "Magical Cunning": "Магічна кмітливість",
    "Might": "Міць",
    "Mind Sliver": "Уламок розуму",
    "Moonlight Step": "Місячний крок",
    "Move Cloud of Daggers": "Перемістити хмару кинджалів",
    "Move Dawn": "Перемістити «Світанок»",
    "Move Duplicity": "Перемістити двійника",
    "Multiattack Defense": "Захист від численних атак",
    "Murder of Crows ": "Вороняча зграя",
    "Murmurs of Doom": "Шепіт приречення",
    "Necrotic Shroud": "Некротичний саван",
    "No Escape": "Не втекти",
    "Off-Hand Attack (Dual Wielder)": "Атака другою рукою («Двозбройне фехтування»)",
    "Pact of the Tome: Cantrip": "Книжна угода: замовляння",
    "Paladin's Smite": "Кара паладина",
    "Paralytic Venom": "Паралітична отрута",
    "Path to the Grave": "Шлях до могили",
    "Patient Defense": "Виважений захист",
    "Phantom Steed": "Примарний скакун",
    "Place Seal": "Розмістити печатку",
    "Prestidigitation": "Фокуси",
    "Prestidigitation: Clean": "Фокуси: очистити",
    "Prestidigitation: Ignite": "Фокуси: запалити",
    "Prestidigitation: Snuff": "Фокуси: загасити",
    "Protector": "Захисник",
    "Psi-Powered Leap": "Псіонічний стрибок",
    "Psychic Blade": "Психічний клинок",
    "Psychic Blades": "Психічні клинки",
    "Psychic Teleportation": "Психічна телепортація",
    "Psychic Veil": "Психічна завіса",
    "Radiant Fire: Fire": "Променевий вогонь: вогонь",
    "Radiant Fire: Radiant": "Променевий вогонь: сяйво",
    "Radiant Sun Bolt": "Променевий сонячний заряд",
    "Radiant Sun Bolt: Bonus Action": "Променевий сонячний заряд: вторинна дія",
    "Rallying Cry": "Гуртувальний клич",
    "Rallying Surge": "Гуртувальний порив",
    "Rangers Companion": "Супутник слідопита",

    # Spell/action titles, editorial batch 5 (R-T).
    "Recharge Arcane Ward": "Відновити магічний оберіг",
    "Reckless Attack (Unarmed)": "Зухвала атака (беззбройна)",
    "Reckless Attack: Forceful Blow": "Зухвала атака: силовий удар",
    "Reckless Attack: Hamstring Blow": "Зухвала атака: удар по сухожиллю",
    "Refreshing Step": "Відновлювальний крок",
    "Rend the Blasphemous": "Роздерти богохульника",
    "Renegade": "Відступник",
    "Replicate Magic Item": "Відтворити магічний предмет",
    "Restorative Energy": "Відновлювальна енергія",
    "Rime's Binding Ice": "Сковувальний лід Райма",
    "Roving Aim": "Рухоме прицілювання",
    "Sanctified Blade": "Освячений клинок",
    "Searing Arc Strike": "Пекучий дуговий удар",
    "Searing Orb": "Пекуча куля",
    "Searing Sunburst": "Пекучий сонячний спалах",
    "Severed from Dreams": "Відрив від снів",
    "Severed from Dreams: Charisma": "Відрив від снів: харизма",
    "Severed from Dreams: Dexterity": "Відрив від снів: спритність",
    "Severed from Dreams: Intelligence": "Відрив від снів: інтелект",
    "Severed from Dreams: Strength": "Відрив від снів: сила",
    "Severed from Dreams: Wisdom": "Відрив від снів: мудрість",
    "Shadow Grasp": "Тіньова хватка",
    "Shadow Shroud": "Тіньовий саван",
    "Shadow Smoke": "Тіньовий дим",
    "Shape-Shifter": "Змінювач подоби",
    "Sharpen the Blade": "Нагострити лезо",
    "Shield Bash: Prone": "Удар щитом: повалення",
    "Shield Bash: Shove": "Удар щитом: відштовхування",
    "Shield of Faith: War God’s Blessing": "Щит віри: благословення бога війни",
    "Skilled: Acrobatics": "Обдарований: Акробатика",
    "Skilled: Animal Handling": "Обдарований: Розуміння тварин",
    "Skilled: Arcana": "Обдарований: Магія",
    "Skilled: Athletics": "Обдарований: Атлетика",
    "Skilled: Deception": "Обдарований: Обман",
    "Skilled: History": "Обдарований: Історія",
    "Skilled: Insight": "Обдарований: Проникливість",
    "Skilled: Intimidation": "Обдарований: Залякування",
    "Skilled: Investigation": "Обдарований: Розслідування",
    "Skilled: Medicine": "Обдарований: Медицина",
    "Skilled: Nature": "Обдарований: Природа",
    "Skilled: Perception": "Обдарований: Відчуття",
    "Skilled: Performance": "Обдарований: Виступ",
    "Skilled: Persuasion": "Обдарований: Переконання",
    "Skilled: Religion": "Обдарований: Релігія",
    "Skilled: Sleight of Hand": "Обдарований: Спритність рук",
    "Skilled: Stealth": "Обдарований: Скрадання",
    "Skilled: Survival": "Обдарований: Виживання",
    "Snilloc's Snowball Swarm": "Сніжковий рій Снілока",
    "Sorcerous Burst": "Чародійський спалах",
    "Sorcerous Restoration": "Чародійське відновлення",
    "Spatial Exchange": "Просторовий обмін",
    "Spectral Slash": "Примарний розтин",
    "Spectral Slash Weapon Attack": "Збройна атака «Примарний розтин»",
    "Spellfire Burst": "Чаровогняний вибух",
    "Spellfire Flare": "Чаровогняний спалах",
    "Spellfire Storm": "Чаровогняна буря",
    "Spiritual Weapon: War God’s Blessing": "Духовна зброя: благословення бога війни",
    "Starry Wisp": "Зоряний вогник",
    "Steady Aim": "Стійке прицілювання",
    "Steed Attack": "Атака скакуна",
    "Steel Defender": "Сталевий захисник",
    "Steel Wind Strike": "Удар сталевого вітру",
    "Step of the Wind Jump": "Вітровий крок: стрибок",
    "Steps of Night": "Кроки ночі",
    "Stone Strike": "Кам’яний удар",
    "Storm Prophetic: Advantage": "Пророцтво бурі: перевага",
    "Storm Prophetic: Disadvantage": "Пророцтво бурі: завада",
    "Storm Strike": "Буревійний удар",
    "Storm’s Thunder": "Грім бурі",
    "Strike from the Dark": "Удар із темряви",
    "Strike of the Giants": "Удар велетів",
    "Summon Beast: Giant Eagle": "Викликати звіра: велетенського орла",
    "Summon Beast: Giant Eagle (Illusion)": "Викликати звіра: велетенського орла (ілюзія)",
    "Summon Dragon": "Викликати дракона",
    "Summon Fey: Red Cap": "Викликати фейську істоту: червоношапку",
    "Summon Fey: Red Cap (Illusion)": "Викликати фейську істоту: червоношапку (ілюзія)",
    "Superior Hunter’s Prey": "Покращена здобич мисливця",
    "Swift Witchcraft": "Швидке чаклування",
    "Sword Burst": "Вибух меча",
    "Synaptic Static": "Синаптичний розряд",
    "Tandem Footwork": "Злагоджений крок",
    "Tasha's Mind Whip": "Батіг розуму Таші",
    "Taunting Step": "Глузливий крок",
    "Telekinetic Movement": "Телекінетичний рух",
    "Thorn Armor": "Тернові обладунки",

    # Spell/action titles, editorial batch 6 (T-Z).
    "Throw: Fast Hand": "Кидок («Спритні руки»)",
    "Thunder Pulse": "Громовий імпульс",
    "Tidal Wave": "Припливна хвиля",
    "Tide of Darkness": "Приплив темряви",
    "Tireless": "Невтомність",
    "Trickster’s Transposition": "Переміщення хитруна",
    "Trollblood Infusion": "Вливання тролячої крові",
    "True Strike (Melee)": "Справжній удар (ближній бій)",
    "True Strike (Ranged)": "Справжній удар (дальній бій)",
    "Twilight Sanctuary": "Сутінкове святилище",
    "Umbral Tendril": "Тіньове щупальце",
    "Uncanny Metabolism": "Надприродний метаболізм",
    "Unholy Resuscitation": "Нечестиве воскрешення",
    "Unleash Hell: Fire": "Вивільнити пекло: вогонь",
    "Unleash Hell: Necrotic": "Вивільнити пекло: некротична енергія",
    "Unleashing a Spirit": "Вивільнення духа",
    "Unleashing a Spirit: Arsonist": "Вивільнення духа: палій",
    "Unleashing a Spirit: Avenger": "Вивільнення духа: месник",
    "Unleashing a Spirit: Beloved": "Вивільнення духа: улюбленець",
    "Unleashing a Spirit: Coward": "Вивільнення духа: боягуз",
    "Unleashing a Spirit: Fortune Teller": "Вивільнення духа: ворожбит",
    "Unleashing a Spirit: Renegade": "Вивільнення духа: відступник",
    "Unleashing a Spirit: Shade": "Вивільнення духа: тінь",
    "Unleashing a Spirit: Sharpshooter": "Вивільнення духа: влучний стрілець",
    "Unleashing a Spirit: Trickster": "Вивільнення духа: хитрун",
    "Unleashing a Spirit: Wayfarer": "Вивільнення духа: мандрівник",
    "Use Hit Point Dice": "Використати кістки здоров’я",
    "Use Hit Point Dice: D6": "Використати кістки здоров’я: d6",
    "Use Hit Point Dice: D8": "Використати кістки здоров’я: d8",
    "Use Hit Point Dice: D10": "Використати кістки здоров’я: d10",
    "Use Hit Point Dice: D12": "Використати кістки здоров’я: d12",
    "Use Poisoner’s Kit": "Скористатися набором отруйника",
    "Use Poisoner’s Kit: Poison": "Скористатися набором отруйника: отрута",
    "Use Poisoner’s Kit: Toxin": "Скористатися набором отруйника: токсин",
    "Vengeful Blade": "Мстивий клинок",
    "Vengeful Shot": "Мстивий постріл",
    "Venomous Strike": "Отруйний удар",
    "Vigilant Blessing": "Благословення пильності",
    "Visions of Annihilation": "Видіння знищення",
    "Vitriolic Sphere": "Їдка сфера",
    "Void Strike": "Удар порожнечі",
    "Void Strike Recast": "Повторити удар порожнечі",
    "Voltedge": "Блискавкове вістря",
    "Wardaway": "Відгін",
    "Warrior of the Gods": "Воїн богів",
    "Watcher’s Will": "Воля дозорця",
    "Web Swing": "Гойдання на павутині",
    "Wild Recovery": "Дике відновлення",
    "Wild Resurgence": "Дике відродження",
    "Wild Shape: Sea": "Дика подоба: море",
    "Word of Radiance": "Слово сяйва",
    "Wrath of the Sea": "Гнів моря",
    "Wrath of the Wild": "Гнів дикої природи",
    "Zealous Presence": "Присутність ревнителя",

    # Spell descriptions, editorial batch 1 (rows 0-29).
    "Leap up to 30 feet, consuming 10 feet of movement.":
        "Стрибнути на відстань до 30 футів, витративши 10 футів пересування.",
    "Choose Acid, Cold, Fire, Lightning, Poison, or Thunder damage. The target hit by the attack takes an extra damage of the chosen type.":
        "Виберіть один із типів шкоди: кислотна, холодова, вогняна, блискавкова, отруйна або громова. Уражена атакою ціль зазнає додаткової шкоди вибраного типу.",
    "You hurl a twisting bolt of blood at a creature within range. Make a ranged spell attack against the target. On a hit, the target takes [1], and you gain a number of Temporary Hit Points equal to your Proficiency Bonus.":
        "Ви жбурляєте викривлений заряд крові в істоту в межах досяжності. Виконайте дальню атаку закляттям проти цілі. У разі влучання ціль зазнає [1], а ви отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому бонусу спеціалізації.",
    "Choose one object weighing 1 to 5 pounds within range that isn’t being worn or carried. The object flies in a straight line up to 60 feet in a direction you choose before falling to the ground, stopping early if it impacts against a solid surface. If the object would strike a creature, that creature must make a Dexterity saving throw. On a failed save, the object strikes the target and stops moving. When the object strikes something, the object and what it strikes each take bludgeoning damage.":
        "Виберіть у межах досяжності предмет вагою від 1 до 5 фунтів, який ніхто не носить і не тримає. Він летить прямою на відстань до 60 футів у вибраному напрямку, а тоді падає на землю; зіткнувшись із твердою поверхнею, він зупиняється раніше. Якщо предмет має влучити в істоту, вона повинна виконати кидок протидії спритністю. У разі невдачі предмет влучає в ціль і зупиняється. Предмет і те, у що він влучив, зазнають забійної шкоди.",
    "Hurl caustic energy that damages the target.":
        "Жбурнути в ціль їдку енергію, що завдає їй шкоди.",
    "Hurl freezing energy that damages the target.":
        "Жбурнути в ціль морозну енергію, що завдає їй шкоди.",
    "Hurl fiery energy that damages the target.":
        "Жбурнути в ціль вогняну енергію, що завдає їй шкоди.",
    "Hurl lightning energy that damages the target.":
        "Жбурнути в ціль блискавкову енергію, що завдає їй шкоди.",
    "Hurl poisonous energy that damages the target.":
        "Жбурнути в ціль отруйну енергію, що завдає їй шкоди.",
    "You utter a quick invocation to create a black nimbus around your hand, then hurl three rays of darkness at one or more targets in range. The rays can be divided among targets however you like. Make a ranged spell attack for each ray; each ray that hits deals 1d10 cold damage. A target that was hit by a ray must succeed on a Constitution saving throw or be unable to use reactions until the start of its next turn.":
        "Ви промовляєте коротке закляття, огортаєте руку чорним німбом і випускаєте три промені темряви в одну чи кілька цілей у межах досяжності. Промені можна розподілити між цілями на ваш вибір. Виконайте дальню атаку закляттям для кожного променя; кожне влучання завдає 1d10 холодової шкоди. Уражена променем ціль повинна успішно виконати кидок протидії статурою, інакше не зможе застосовувати реагування до початку свого наступного ходу.",
    "A wave of force leaves your palms, targeting a creature within range. The target makes a Constitution saving throw. On a failed save, the creature takes 2d6 Force damage and has the <LSTag Type=\"Status\" Tooltip=\"STUNNED\">Stunned</LSTag> condition until the end of its next turn. On a successful save, the creature takes the damage only.":
        "Із ваших долонь виривається силова хвиля в істоту в межах досяжності. Ціль повинна виконати кидок протидії статурою. У разі невдачі істота зазнає 2d6 силової шкоди й перебуває у стані <LSTag Type=\"Status\" Tooltip=\"STUNNED\">Приголомшення</LSTag> до кінця свого наступного ходу. У разі успіху істота зазнає лише шкоди.",
    "Reduce the damage and redirect it back at your attacker.":
        "Зменшити шкоду й переспрямувати атаку назад у нападника.",
    "Make a ranged spell attack originating from the cannon at one creature or object. On a hit, the target takes Force damage, and if the target is a creature, it is pushed up to 5 feet away from the cannon.":
        "Виконайте з гармати дальню атаку закляттям проти однієї істоти чи предмета. У разі влучання ціль зазнає силової шкоди; якщо ціль — істота, її також відштовхує від гармати на відстань до 5 футів.",
    "As your attack hits or misses the target, the weapon or ammunition you’re using transforms into a lightning bolt. Instead of taking any damage or other effects from the attack, the target takes 4d8 Lightning damage on a hit, or half as much damage on a miss. Each creature within 10 feet of the target takes 2d8 Lightning damage.":
        "Незалежно від того, влучає атака в ціль чи ні, використана зброя або боєприпас перетворюється на блискавку. Замість звичайної шкоди й інших ефектів атаки ціль зазнає 4d8 блискавкової шкоди в разі влучання або половину цієї шкоди в разі промаху. Кожна істота в межах 10 футів від цілі зазнає 2d8 блискавкової шкоди.",
    "You extend your forefinger and thumb, a dangerous gesture mimicking a gun.":
        "Ви випростовуєте вказівний і великий пальці, небезпечно наслідуючи жестом пістоль.",
    "You can make one weapon attack on the first turn of combat without using an action.":
        "Під час першого ходу в бою ви можете виконати одну збройну атаку, не витрачаючи дії.",
    "Jump to the selected location, consuming movement equal to the distance jumped.":
        "Стрибнути у вибране місце, витративши пересування, що дорівнює відстані стрибка.",
    "Once on each of your turns when you hit a creature with the launcher, you can deal an extra 1d6 Lightning damage to that target.":
        "Один раз за кожен свій хід, влучивши в істоту блискавкометом, ви можете завдати цій цілі додатково 1d6 блискавкової шкоди.",
    """A beam of enervating energy shoots from you toward a creature within range. The target must make a Constitution saving throw. On a successful save, the target has Disadvantage on the next attack roll it makes until the start of your next turn.

On a failed save, the target has Disadvantage on Strength-based D20 Tests for the duration. During that time, it also subtracts 1d8 from all its damage rolls. The target repeats the save at the end of each of its turns, ending the spell on a success.""":
        """Промінь виснажливої енергії летить від вас до істоти в межах досяжності. Ціль повинна виконати кидок протидії статурою. У разі успіху вона має заваду для наступного кидка атаки до початку вашого наступного ходу.

У разі невдачі ціль має заваду для перевірок d20, що залежать від сили, до завершення дії закляття. Упродовж цього часу вона також віднімає 1d8 від усіх своїх кидків шкоди. Наприкінці кожного свого ходу ціль повторює кидок протидії, завершуючи дію закляття в разі успіху.""",
    "As a bonus action, you can fly to a position using only 10 feet of movement. Once you use this bonus action, you can’t do so again until you finish a short or long rest, unless you expend a Psionic Energy die (no action required) to regain its use.":
        "Вторинною дією ви можете перелетіти у вибране місце, витративши лише 10 футів пересування. Після цього ви не зможете скористатися цією вторинною дією знову до короткого або довгого відпочинку, якщо не витратите кістку псіонічної енергії (дія не потрібна), щоб відновити її використання.",
    "As a Bonus Action, you manifest a Psychic Blade, expend one Psionic Energy Die and roll it, and throw the blade at an unoccupied space you can see up to 30 feet away. You then teleport to that space, and the blade vanishes.":
        "Вторинною дією ви створюєте психічний клинок, витрачаєте й кидаєте одну кістку псіонічної енергії, а потім метаєте клинок у вільне місце, яке бачите в межах 30 футів. Ви телепортуєтеся в це місце, після чого клинок зникає.",
    "Hurl a searing bolt of magical radiance at a creature. You add your Dexterity modifier to the attack and damage rolls, and the bolt deals Radiant damage equal to your Martial Arts die.":
        "Жбурнути в істоту пекучий заряд магічного сяйва. Ви додаєте модифікатор спритності до кидків атаки й шкоди, а заряд завдає променевої шкоди відповідно до кістки бойових мистецтв.",
    "Hurl two searing bolts of magical radiance, making the special attack twice. You can send both bolts at the same creature or split them between two.":
        "Жбурнути два пекучі заряди магічного сяйва, двічі виконавши особливу атаку. Обидва заряди можна спрямувати в одну істоту або розподілити між двома.",

    # Spell descriptions, editorial batch 2 (rows 30-59).
    "A beam of enervating energy shoots from you toward a creature within range. The target must make a Constitution saving throw. On a successful save, the target has Disadvantage on the next attack roll it makes until the start of your next turn.":
        "Промінь виснажливої енергії летить від вас до істоти в межах досяжності. Ціль повинна виконати кидок протидії статурою. У разі успіху вона має заваду для наступного кидка атаки до початку вашого наступного ходу.",
    "<LSTag Type=\"Status\" Tooltip=\"POISONED\">Poisons</LSTag> the target.":
        "<LSTag Type=\"Status\" Tooltip=\"POISONED\">Отруює</LSTag> ціль.",
    "You create and hurl a pulsing orb of energy at one creature within range. Make a ranged spell attack against the target. On a hit, the target takes Radiant damage. Hit or miss, the orb then explodes in a flash of light. The target and each creature within 10 feet of it make a Constitution saving throw. On a failed save, a creature has the <LSTag Type=\"Status\" Tooltip=\"BLINDED\">Blinded</LSTag> condition until the end of its next turn.":
        "Ви створюєте пульсівну енергетичну кулю й жбурляєте її в одну істоту в межах досяжності. Виконайте дальню атаку закляттям проти цілі. У разі влучання ціль зазнає променевої шкоди. Незалежно від влучання куля вибухає спалахом світла. Ціль і кожна істота в межах 10 футів від неї повинні виконати кидок протидії статурою. У разі невдачі істота перебуває у стані <LSTag Type=\"Status\" Tooltip=\"BLINDED\">Засліплення</LSTag> до кінця свого наступного ходу.",
    "Create an orb of light and hurl it at a point of your choice, where it erupts into a sphere of radiant light for a brief but deadly instant, searing every creature caught in the blast.":
        "Створити кулю світла й жбурнути її у вибрану точку, де вона на коротку, але смертоносну мить вибухає сферою променевого сяйва, обпалюючи кожну істоту в зоні вибуху.",
    "Once per turn when you hit a creature with your pact weapon, you can expend a Pact Magic spell slot to deal an extra 1d8 Force damage to the target, plus another 1d8 per level of the spell slot, and you can give the target the Prone condition if it is Huge or smaller.":
        "Один раз за хід, влучивши в істоту зброєю договору, ви можете витратити чарунку магії договору, щоб завдати цілі додатково 1d8 силової шкоди та ще 1d8 за кожен рівень чарунки. Якщо ціль величезна або менша, ви також можете повалити її.",
    "When you deal Sneak Attack damage, you can forgo your Sneak Attack's extra damage. If you do, the target must succeed on a Constitution saving throw or be Paralyzed until the end of your next turn.":
        "Завдаючи шкоди підступним ударом, ви можете відмовитися від його додаткової шкоди. Тоді ціль повинна успішно виконати кидок протидії статурою, інакше буде паралізована до кінця вашого наступного ходу.",
    "You throw [1] snowballs at a point you choose within range. Each snowball affects creatures in a 5-foot-radius sphere centered on that point. Each creature in the area must make a Dexterity saving throw, taking [2] per snowball on a failed save, or half as much damage on a successful one.":
        "Ви кидаєте [1] сніжки у вибрану точку в межах досяжності. Кожна сніжка вражає істот у сфері радіусом 5 футів із центром у цій точці. Кожна істота в зоні повинна виконати кидок протидії спритністю: у разі невдачі вона зазнає [2] за кожну сніжку, а в разі успіху — половину цієї шкоди.",
    """You cast sorcerous energy at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes damage of a type you choose: Acid, Cold, Fire, Lightning, Poison, Psychic, or Thunder.

Sometimes the magic surges and deals additional damage. The chance of a magical surge increases each time this cantrip’s damage increases at higher levels.""":
        """Ви спрямовуєте чародійську енергію в одну істоту чи предмет у межах досяжності. Виконайте дальню атаку закляттям проти цілі. У разі влучання ціль зазнає шкоди вибраного типу: кислотної, холодової, вогняної, блискавкової, отруйної, психічної або громової.

Іноді магія спалахує й завдає додаткової шкоди. Імовірність такого спалаху зростає щоразу, коли на вищих рівнях збільшується шкода цього замовляння.""",
    "You unleash a blast of brilliant fire. Make a ranged spell attack against a target within range. On a hit, the target takes Radiant damage.":
        "Ви вивільняєте вибух яскравого вогню. Виконайте дальню атаку закляттям проти цілі в межах досяжності. У разі влучання ціль зазнає променевої шкоди.",
    "You launch a mote of light at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes Radiant damage, and until the end of your next turn, it emits Dim Light in a [1] radius and can’t benefit from the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition.":
        "Ви запускаєте іскру світла в одну істоту чи предмет у межах досяжності. Виконайте дальню атаку закляттям проти цілі. У разі влучання ціль зазнає променевої шкоди, а до кінця вашого наступного ходу випромінює тьмяне світло в радіусі [1] і не може скористатися станом <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимості</LSTag>.",
    "You flourish the weapon used in the casting and then vanish to strike like the wind, reappearing beside a creature you can see within range and making a melee spell attack against it. You then continue on, moving between nearby foes to attack again, striking up to five different creatures in total. On a hit, a target takes [1].":
        "Ви змахуєте зброєю, використаною для проказування, і зникаєте, щоб ударити подібно до вітру. З’явившись біля видимої істоти в межах досяжності, ви виконуєте проти неї атаку закляттям ближнього бою. Потім ви рухаєтеся далі між сусідніми ворогами, уражаючи загалом до п’яти різних істот. У разі влучання ціль зазнає [1].",
    "Leap up to twice your normal jump distance. This jump consumes movement equal to half the distance traveled.":
        "Стрибнути на відстань до подвійної звичайної дальності стрибка. Це витрачає пересування, що дорівнює половині подоланої відстані.",
    "As a Bonus Action, you manifest a second Psychic Blade in your free hand and throw it at a creature you can see, dealing Psychic damage. The blade has the Vex weapon mastery property, then vanishes.":
        "Вторинною дією ви створюєте другий психічний клинок у вільній руці й метаєте його у видиму істоту, завдаючи психічної шкоди. Клинок має властивість майстерності зброї «Збентеження», після чого зникає.",
    "Guided by a flash of magical insight, you make one attack with the weapon used in the spell’s casting. The attack uses your spellcasting ability for the attack and damage rolls instead of using Strength or Dexterity. If the attack deals damage, it can be Radiant damage or the weapon’s normal damage type (your choice).":
        "Керуючись спалахом магічного осяяння, ви виконуєте одну атаку зброєю, використаною для проказування закляття. Для кидків атаки й шкоди ця атака використовує вашу базову характеристику проказування замість сили чи спритності. Якщо атака завдає шкоди, на ваш вибір це може бути променева шкода або звичайний тип шкоди зброї.",
    "You point at a location within range, and a glowing, 1-foot-diameter ball of acid streaks there and explodes in a 20-foot-radius Sphere. Each creature in that area makes a Dexterity saving throw. On a failed save, a creature takes [1] and another [2] at the end of its next turn. On a successful save, a creature takes half the initial damage only.":
        "Ви вказуєте на місце в межах досяжності: туди стрімко летить сяйна кислотна куля діаметром 1 фут і вибухає сферою радіусом 20 футів. Кожна істота в цій зоні повинна виконати кидок протидії спритністю. У разі невдачі істота зазнає [1], а наприкінці свого наступного ходу — ще [2]. У разі успіху вона зазнає лише половини початкової шкоди.",
    "With a short phrase of void speech, you gather writhing darkness around your hand. When you cast the spell, and as an action on subsequent turns, you can unleash a bolt of darkness at a target within range. Make a ranged spell attack. If your target is in dim light or darkness, you have advantage on the roll. On a hit, the target takes necrotic damage and is frightened of you until the start of your next turn.":
        "Короткою фразою мовою порожнечі ви збираєте довкола руки звивисту темряву. Проказуючи закляття, а також основною дією в наступні ходи, ви можете випустити заряд темряви в ціль у межах досяжності. Виконайте дальню атаку закляттям. Якщо ціль перебуває в тьмяному світлі або темряві, ви маєте перевагу для цього кидка. У разі влучання ціль зазнає некротичної шкоди й боїться вас до початку вашого наступного ходу.",
    "You hurl a disorienting magical force toward one creature within range. The target makes a Constitution saving throw. On a failed save, the target takes Force damage, its Speed is halved until the start of your next turn, and on its next turn, it can take only an action or a Bonus Action (but not both). On a successful save, the target takes half as much damage only.":
        "Ви жбурляєте дезорієнтувальну магічну силу в одну істоту в межах досяжності. Ціль повинна виконати кидок протидії статурою. У разі невдачі вона зазнає силової шкоди, її швидкість зменшується вдвічі до початку вашого наступного ходу, а у свій наступний хід вона може виконати лише основну або вторинну дію, але не обидві. У разі успіху ціль зазнає лише половини шкоди.",
    "Charge forward and attack the first enemy in your way.":
        "Кинутися вперед і атакувати першого ворога на своєму шляху.",
    "Deal more damage: charge forward and slam into the first enemy in your way.":
        "Завдати більше шкоди: кинутися вперед і врізатися в першого ворога на своєму шляху.",
    "You can expend one Risk Die to move up to 30 feet. This movement doesn’t provoke Opportunity Attacks and is unaffected by Difficult Terrain.":
        "Ви можете витратити одну кістку ризику, щоб переміститися на відстань до 30 футів. Це пересування не провокує принагідних атак і не залежить від важкопрохідної місцевості.",

    # Spell descriptions, editorial batch 3 (rows 60-89).
    "Charge forward, possibly knocking the target <LSTag Type=\"Status\" Tooltip=\"PRONE\">Prone</LSTag>.":
        "Кинутися вперед, маючи шанс <LSTag Type=\"Status\" Tooltip=\"PRONE\">повалити</LSTag> ціль.",
    "<LSTag Type=\"Status\" Tooltip=\"TURNED\">Turn</LSTag> nearby aberrations, celestials, elementals, feys, or fiends. They are forced to flee and cannot come close to you.":
        "<LSTag Type=\"Status\" Tooltip=\"TURNED\">Вигнати</LSTag> поблизьких покручів, небожителів, стихійників, фейських істот або нечисть. Вони змушені тікати й не можуть наблизитися до вас.",
    "The spell captures some of the incoming energy, lessening its effect on you and storing it for your next melee attack. You have resistance to the triggering damage type until the start of your next turn. Also, the first time you hit with a melee attack on your next turn, the target takes an extra [1] damage of the triggering type, and the spell ends.":
        "Закляття поглинає частину спрямованої на вас енергії, послаблюючи її вплив і зберігаючи для вашої наступної атаки ближнього бою. До початку свого наступного ходу ви маєте стійкість до типу шкоди, що спричинив реагування. Крім того, перше влучання атакою ближнього бою під час вашого наступного ходу завдає цілі додатково [1] шкоди цього типу, після чого дія закляття завершується.",
    "You gain proficiency in any combination of three skills of your choice.":
        "Ви отримуєте спеціалізацію в будь-яких трьох навичках на свій вибір.",
    "You can take the <LSTag Type=\"Spell\" Tooltip=\"Shout_Dash\">Dash</LSTag> action as a Bonus Action. When you do so, you gain a number of Temporary Hit Points equal to your Proficiency Bonus.":
        "Ви можете виконати <LSTag Type=\"Spell\" Tooltip=\"Shout_Dash\">Біг</LSTag> вторинною дією. Зробивши це, ви отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому бонусу спеціалізації.",
    "You tap into your life force to heal yourself. Roll [1] of your unexpended Hit Point Dice, and regain a number of Hit Points equal to the roll’s total plus your spellcasting ability modifier. Those dice are then expended.":
        "Ви звертаєтеся до власної життєвої сили, щоб зцілитися. Киньте [1] невитрачених кісток здоров’я й відновіть очки здоров’я в кількості, що дорівнює сумі результатів кидків і вашого модифікатора базової характеристики проказування. Після цього кістки витрачаються.",
    "You can expend a spell slot, and the ward regains a number of Hit Points equal to twice the level of the spell slot expended.":
        "Ви можете витратити чарунку заклять, щоб оберіг відновив очки здоров’я в кількості, що дорівнює подвоєному рівню витраченої чарунки.",
    "You can customize your Arcane Armor. When you do so, choose one of the following armor models: Dreadnaught, Guardian, or Infiltrator. The model you choose gives you special benefits while you wear it. Each model includes a special weapon. When you attack with that weapon, you can add your Intelligence modifier, instead of your Strength or Dexterity modifier, to the attack and damage rolls.":
        "Ви можете налаштовувати свої магічні обладунки. Виберіть одну з моделей: Дредноут, Вартовий або Диверсант. Обрана модель надає особливі переваги, доки ви носите обладунки, а також містить особливу зброю. Атакуючи цією зброєю, ви можете додавати до кидків атаки й шкоди модифікатор інтелекту замість модифікатора сили чи спритності.",
    """You design your armor to become a towering juggernaut in battle. It has the following features:

Force Demolisher. An arcane wrecking ball or sledgehammer projects from your armor. The demolisher counts as a Simple Melee weapon with the Reach property, and it deals 1d10 Force damage on a hit. If you hit a creature that is at least one size smaller than you with the demolisher, you can push the creature up to 10 feet straight away from yourself or pull the creature up to 10 feet toward yourself.
Giant Stature. As a Bonus Action, you transform and enlarge your armor for 1 minute.""":
        """Ви проєктуєте свої обладунки так, щоб стати велетенським тараном у бою. Вони мають такі особливості:

Силовий руйнівник. З обладунків висувається магічна таранна куля або кувалда. Руйнівник вважається простою зброєю ближнього бою з властивістю «Досяжність» і в разі влучання завдає 1d10 силової шкоди. Влучивши руйнівником в істоту щонайменше на один розмір меншу за вас, ви можете відштовхнути її від себе або притягнути до себе на відстань до 10 футів.
Велетенський зріст. Вторинною дією ви перетворюєте й збільшуєте обладунки на 1 хвилину.""",
    """You design your armor to be in the front line of conflict. It has the following features:

Thunder Pulse. You can discharge concussive blasts with strikes from your armor. The pulse counts as a Simple Melee weapon and deals 1d8 Thunder damage on a hit. A creature hit by the pulse has Disadvantage on attack rolls against targets other than you until the start of your next turn.
Defensive Field. While Bloodied, you can take a Bonus Action to gain Temporary Hit Points equal to your Artificer level. You lose these Temporary Hit Points if you doff the armor.""":
        """Ви проєктуєте свої обладунки для бою на передовій. Вони мають такі особливості:

Громовий імпульс. Ударами обладунків ви можете створювати струсові вибухи. Імпульс вважається простою зброєю ближнього бою й у разі влучання завдає 1d8 громової шкоди. Уражена імпульсом істота до початку вашого наступного ходу має заваду для кидків атаки проти всіх цілей, крім вас.
Захисне поле. Поки ви закривавлені, вторинною дією можете отримати тимчасові очки здоров’я в кількості, що дорівнює вашому рівню винахідника. Знявши обладунки, ви втрачаєте ці тимчасові очки здоров’я.""",
    """You customize your armor for subtler undertakings. It has the following features:

Lightning Launcher. A gemlike node appears on your armor, from which you can shoot bolts of lightning. The launcher counts as a Simple Ranged weapon, and it deals 1d6 Lightning damage on a hit. Once on each of your turns when you hit a creature with the launcher, you can deal an extra 1d6 Lightning damage to that target.
Powered Steps. Your Speed increases by 5 feet.
Dampening Field. You have Advantage on Dexterity (<LSTag Type=\"Skills\" Tooltip=\"Stealth\">Stealth</LSTag>) checks.""":
        """Ви налаштовуєте свої обладунки для непомітніших завдань. Вони мають такі особливості:

Блискавкомет. На обладунках з’являється вузол, схожий на самоцвіт, із якого можна стріляти блискавковими зарядами. Блискавкомет вважається простою зброєю дальнього бою й у разі влучання завдає 1d6 блискавкової шкоди. Один раз за кожен свій хід, влучивши в істоту блискавкометом, ви можете завдати цій цілі додатково 1d6 блискавкової шкоди.
Підсилені кроки. Ваша швидкість збільшується на 5 футів.
Приглушувальне поле. Ви маєте перевагу для перевірок спритності (<LSTag Type=\"Skills\" Tooltip=\"Stealth\">Скрадання</LSTag>).""",
    "The billowing flames of a dragon blast from your feet, granting you explosive speed. For the duration, your Speed increases by [1], and moving doesn't provoke Opportunity Attacks. Whenever you move within [2] of a creature, it takes Fire damage from your trail of heat. A creature can take this damage only once during a turn.":
        "Із-під ваших ніг виривається бурхливе драконяче полум’я, надаючи вибухову швидкість. На час дії закляття ваша швидкість збільшується на [1], а пересування не провокує принагідних атак. Коли ви проходите в межах [2] від істоти, вона зазнає вогняної шкоди від вашого жаркого сліду. Істота може зазнати цієї шкоди лише один раз за хід.",
    """You constantly emanate a menacing aura while you’re not incapacitated. The aura extends 10 feet from you in every direction, but not through total cover.

If a creature is frightened of you, it has Disadvantage on ability checks and attack rolls while in the aura, and that creature takes psychic damage equal to half your paladin level if it starts its turn there.""":
        """Поки ви не недієздатні, від вас постійно шириться загрозлива аура на 10 футів у всіх напрямках, але не крізь повне укриття.

Істота, яка боїться вас, у межах аури має заваду для перевірок характеристик і кидків атаки. Якщо така істота починає там свій хід, вона зазнає психічної шкоди в кількості, що дорівнює половині вашого рівня паладина.""",
    "While this aura lasts, you can cast <LSTag Type=\"Spell\" Tooltip=\"Target_AuraOfVitality_Activate\">Restore Vitality</LSTag> to heal yourself or nearby allies.":
        "Поки діє ця аура, ви можете проказати <LSTag Type=\"Spell\" Tooltip=\"Target_AuraOfVitality_Activate\">Відновлення життєвої сили</LSTag>, щоб зцілити себе або поблизьких союзників.",
    "You and any nearby allies have Resistance to Necrotic, Psychic, and Radiant damage. The aura disappears if you fall <LSTag Type=\"Status\" Tooltip=\"DOWNED\">Unconscious</LSTag>.":
        "Ви й поблизькі союзники маєте стійкість до некротичної, психічної та променевої шкоди. Аура зникає, якщо ви <LSTag Type=\"Status\" Tooltip=\"DOWNED\">знепритомнієте</LSTag>.",
    "You can expend one Risk Die to gain Temporary Hit Points equal to the number rolled on the die plus your Gunslinger level.":
        "Ви можете витратити одну кістку ризику, щоб отримати тимчасові очки здоров’я в кількості, що дорівнює результату кидка кістки плюс ваш рівень стрільця.",
    "Whenever a creature makes an attack roll against you before the spell ends, the attacker subtracts 1d4 from the attack roll.":
        "Щоразу, коли до завершення дії закляття істота виконує проти вас кидок атаки, нападник віднімає 1d4 від результату цього кидка.",
    """While the Bladesong is active, you gain the following benefits.

Agility. You gain a bonus to your AC equal to your Intelligence modifier (minimum of +1), and your Speed increases by 10 feet. In addition, you have Advantage on Dexterity (<LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Acrobatics</LSTag>) checks.

Bladework. Whenever you attack with a weapon with which you have proficiency, you can use your Intelligence modifier for the attack and damage rolls instead of using Strength or Dexterity.

Focus. When you make a Constitution saving throw to maintain Concentration, you can add your Intelligence modifier to the total.""":
        """Поки діє Пісня клинка, ви отримуєте такі переваги.

Спритність. Ви отримуєте бонус до рівня захисту, що дорівнює модифікатору інтелекту (щонайменше +1), а ваша швидкість збільшується на 10 футів. Крім того, ви маєте перевагу для перевірок спритності (<LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Акробатика</LSTag>).

Майстерність клинка. Атакуючи зброєю, у якій маєте спеціалізацію, ви можете використовувати для кидків атаки й шкоди модифікатор інтелекту замість сили чи спритності.

Зосередженість. Виконуючи кидок протидії статурою для підтримання концентрації, ви можете додати до результату модифікатор інтелекту.""",
    "You can expend one Risk Die to gain Blindsight with a range of 30 feet until the end of the current turn.":
        "Ви можете витратити одну кістку ризику, щоб отримати сліпобачення в радіусі 30 футів до кінця поточного ходу.",
    """Thunderous reverberations fill a 10-foot Emanation originating from you for the duration. Whenever the Emanation enters a creature’s space and whenever a creature enters the Emanation or ends its turn there, the creature makes a Constitution saving throw. On a failed save, the creature takes Thunder damage. On a successful save, the creature takes half as much damage only. A creature makes this save only once per turn.

In addition, you have Resistance to Thunder damage, and ranged attack rolls against you are made with Disadvantage.""":
        """На час дії закляття громові відлуння наповнюють 10-футову еманацію, що виходить від вас. Коли еманація входить у простір істоти, а також коли істота входить до еманації або завершує там свій хід, вона повинна виконати кидок протидії статурою. У разі невдачі істота зазнає громової шкоди, а в разі успіху — половини цієї шкоди. Істота виконує цей кидок лише один раз за хід.

Крім того, ви маєте стійкість до громової шкоди, а дальні кидки атаки проти вас виконуються із завадою.""",
    "You and each ally within 30 feet of you gain Temporary Hit Points equal to your Warlock level plus your Charisma modifier. Once you use this feature, you can’t use it again until you finish a Short Rest.":
        "Ви й кожен союзник у межах 30 футів отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому рівню чаклуна плюс модифікатор харизми. Скориставшись цією особливістю, ви не зможете використати її знову до короткого відпочинку.",
    """When you reach character level 3, you can transform as a Bonus Action using one of the options. The transformation lasts for 1 minute or until you end it (no action required). Once you transform, you can’t do so again until you finish a Long Rest.

You can deal extra damage to a target when you deal damage to it with an attack or a spell. The extra damage equals your Proficiency Bonus. The damage type is Necrotic for Necrotic Shroud, or Radiant for Heavenly Wings and Inner Radiance.""":
        """Досягнувши 3-го рівня персонажа, ви можете вторинною дією перетворитися за одним із доступних варіантів. Перетворення триває 1 хвилину або доки ви його не завершите (дія не потрібна). Після перетворення ви не зможете зробити це знову до довгого відпочинку.

Завдаючи цілі шкоди атакою або закляттям, ви можете завдати їй додаткової шкоди в кількості, що дорівнює вашому бонусу спеціалізації. «Некротичний саван» завдає некротичної шкоди, а «Небесні крила» й «Внутрішнє сяйво» — променевої.""",
    "Two spectral wings sprout from your back temporarily. Until the transformation ends, you have a Fly Speed equal to your Speed.":
        "На вашій спині тимчасово виростають два примарні крила. До завершення перетворення ваша швидкість польоту дорівнює звичайній швидкості.",
    "Your eyes become pools of darkness, and flightless wings briefly sprout from your back. Creatures of your choice within 10 feet of you must succeed on a Charisma saving throw or have the Frightened condition for 1 minute.":
        "Ваші очі стають проваллями темряви, а на спині ненадовго виростають нелітаючі крила. Вибрані вами істоти в межах 10 футів повинні успішно виконати кидок протидії харизмою, інакше перебуватимуть у стані переляку протягом 1 хвилини.",
    "Searing light temporarily radiates from your eyes and mouth. For the duration, you shed Bright Light in a 10-foot radius and Dim Light for an additional 10 feet, and at the end of each of your turns, each creature within 10 feet of you takes Radiant damage equal to your Proficiency Bonus.":
        "Ваші очі й рот тимчасово випромінюють пекуче світло. На час дії перетворення ви випромінюєте яскраве світло в радіусі 10 футів і тьмяне світло ще на 10 футів. Наприкінці кожного вашого ходу кожна істота в межах 10 футів зазнає променевої шкоди в кількості, що дорівнює вашому бонусу спеціалізації.",
    "An aura radiates from you in a 30-foot Emanation for the duration. While in the aura, you and your allies have Advantage on saving throws against spells and other magical effects and take only half damage from them.":
        "На час дії закляття від вас шириться 30-футова еманація. Перебуваючи в аурі, ви й ваші союзники мають перевагу для кидків протидії закляттям та іншим магічним ефектам і зазнають від них лише половини шкоди.",
    """Whenever you finish a Long Rest, you choose one type of land: arid, polar, temperate, or tropical. Based on your choice, you consult the corresponding table and have all listed spells for your Druid level and lower prepared.

If you choose Arid Land, you have Blur, Burning Hands, and Fire Bolt prepared at 3rd level; Fireball at 5th level; Blight at 7th level; and Wall of Stone at 9th level.

If you choose Polar Land, you have Fog Cloud, Hold Person, and Ray of Frost prepared at 3rd level; Sleet Storm at 5th level; Ice Storm at 7th level; and Cone of Cold at 9th level.

If you choose Temperate Land, you have Misty Step, <LSTag Type=\"Spell\" Tooltip=\"Target_ShockingGrasp\">Shocking Grasp</LSTag>, and Sleep prepared at 3rd level; Lightning Bolt at 5th level; Freedom of Movement at 7th level; and Greater Restoration at 9th level.

If you choose Tropical Land, you have Acid Splash, Ray of Sickness, and Web prepared at 3rd level; Stinking Cloud at 5th level; Polymorph at 7th level; and Insect Plague at 9th level.""":
        """Після кожного довгого відпочинку виберіть один тип краю: посушливий, полярний, помірний або тропічний. Відповідно до вибору ви матимете підготовленими всі закляття з відповідної таблиці, доступні на вашому рівні друїда й нижчих рівнях.

Посушливий край: на 3-му рівні — Розмиття, Палючі руки й Вогняний заряд; на 5-му — Вогняна куля; на 7-му — Гниль; на 9-му — Стіна каменю.

Полярний край: на 3-му рівні — Хмара туману, Утримання особи й Струмінь морозу; на 5-му — Хуртовина; на 7-му — Крижана буря; на 9-му — Конус холоду.

Помірний край: на 3-му рівні — Маревний крок, <LSTag Type=\"Spell\" Tooltip=\"Target_ShockingGrasp\">Шоковий хват</LSTag> і Сон; на 5-му — Розряд блискавки; на 7-му — Свобода руху; на 9-му — Велике відновлення.

Тропічний край: на 3-му рівні — Кислотні бризки, Струмінь хвороби й Павутина; на 5-му — Смердюча хмара; на 7-му — Перетворення; на 9-му — Комашина чума.""",
    "If you choose Arid Land, you have Blur, Burning Hands, and Fire Bolt prepared at 3rd level; Fireball at 5th level; Blight at 7th level; and Wall of Stone at 9th level.":
        "Якщо ви обираєте посушливий край, на 3-му рівні у вас підготовлені Розмиття, Палючі руки й Вогняний заряд; на 5-му — Вогняна куля; на 7-му — Гниль; на 9-му — Стіна каменю.",
    "If you choose Polar Land, you have Fog Cloud, Hold Person, and Ray of Frost prepared at 3rd level; Sleet Storm at 5th level; Ice Storm at 7th level; and Cone of Cold at 9th level.":
        "Якщо ви обираєте полярний край, на 3-му рівні у вас підготовлені Хмара туману, Утримання особи й Струмінь морозу; на 5-му — Хуртовина; на 7-му — Крижана буря; на 9-му — Конус холоду.",
    "If you choose Temperate Land, you have Misty Step, <LSTag Type=\"Spell\" Tooltip=\"Target_ShockingGrasp\">Shocking Grasp</LSTag>, and Sleep prepared at 3rd level; Lightning Bolt at 5th level; Freedom of Movement at 7th level; and Greater Restoration at 9th level.":
        "Якщо ви обираєте помірний край, на 3-му рівні у вас підготовлені Маревний крок, <LSTag Type=\"Spell\" Tooltip=\"Target_ShockingGrasp\">Шоковий хват</LSTag> і Сон; на 5-му — Розряд блискавки; на 7-му — Свобода руху; на 9-му — Велике відновлення.",
    "If you choose Tropical Land, you have Acid Splash, Ray of Sickness, and Web prepared at 3rd level; Stinking Cloud at 5th level; Polymorph at 7th level; and Insect Plague at 9th level.":
        "Якщо ви обираєте тропічний край, на 3-му рівні у вас підготовлені Кислотні бризки, Струмінь хвороби й Павутина; на 5-му — Смердюча хмара; на 7-му — Перетворення; на 9-му — Комашина чума.",
    "You cloak yourself in shadow, giving you advantage on Dexterity (<LSTag Type=\"Skills\" Tooltip=\"Stealth\">Stealth</LSTag>) checks against creatures that rely on sight.":
        "Ви огортаєтеся тінню й отримуєте перевагу для перевірок спритності (<LSTag Type=\"Skills\" Tooltip=\"Stealth\">Непомітність</LSTag>) проти істот, які покладаються на зір.",
    "You can use your Channel Oath to exude a terrifying presence. You force each creature of your choice that you can see within 30 feet of you to make a Wisdom saving throw. On a failed save, a creature becomes frightened of you for 1 minute. The frightened creature can repeat this saving throw at the end of each of its turns, ending the effect on itself on a success.":
        "Ви можете скористатися Обітним наснаженням, щоб випромінити жахливу присутність. Кожна вибрана вами істота, яку ви бачите в межах 30 футів, повинна виконати кидок протидії мудрістю. У разі невдачі істота боїться вас протягом 1 хвилини. Наприкінці кожного свого ходу налякана істота може повторити цей кидок протидії, у разі успіху припиняючи дію ефекту на собі.",
    "While <LSTag Type=\"Status\" Tooltip=\"RAGE\">raging</LSTag>, you can feed on the shadows around you to restore your vitality. While in dim light or darkness, you can use a bonus action to regain hit points equal to 1d12 + your Constitution modifier.":
        "Під час <LSTag Type=\"Status\" Tooltip=\"RAGE\">люті</LSTag> ви можете живитися навколишніми тінями, щоб відновити життєву силу. Перебуваючи в тьмяному світлі або темряві, ви можете вторинною дією відновити очки здоров’я в кількості 1d12 + модифікатор статури.",
    "As a Bonus Action, you can expend a use of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> and channel a specific spirit. When you do so, choose the spirit from the <LSTag Type=\"Passive\" Tooltip=\"Spirits_3_SpiritsFromBeyond\">Spirits from Beyond</LSTag> table rather than rolling. The chosen spirit’s corresponding number must be less than or equal to the highest number on your Bardic Inspiration die; for example, if your Bardic Inspiration die is a d8, you can choose to channel any spirit up to (and including) the Shade.":
        "Вторинною дією ви можете витратити одне використання <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> і спрямувати конкретного духа. Замість кидка виберіть духа з таблиці <LSTag Type=\"Passive\" Tooltip=\"Spirits_3_SpiritsFromBeyond\">«Духи з потойбіччя»</LSTag>. Номер вибраного духа має бути не більшим за найбільше число на вашій кістці Бардівського натхнення; наприклад, з кісткою d8 ви можете спрямувати будь-якого духа аж до Тіні включно.",
    "Spend Sorcery Points to unlock a <LSTag Tooltip=\"SpellSlot\">spell slot</LSTag>. Creating another spell slot of the same level has no effect until this one is used.":
        "Витратьте очки чародійства, щоб створити <LSTag Tooltip=\"SpellSlot\">чарунку заклять</LSTag>. Інша чарунка того самого рівня не матиме ефекту, доки ви не використаєте цю.",
    "Spend [1] Sorcery Points to unlock a level [2] <LSTag Tooltip=\"SpellSlot\">spell slot</LSTag>. Creating another spell slot of the same level has no effect until this one is used.":
        "Витратьте [1] очок чародійства, щоб створити <LSTag Tooltip=\"SpellSlot\">чарунку заклять</LSTag> [2]-го рівня. Інша чарунка того самого рівня не матиме ефекту, доки ви не використаєте цю.",
    "As a Bonus Action, you give yourself Advantage on your ranged weapon attack roll on the current turn. You can use this feature only if you haven’t moved during this turn, and after you use it, your Speed is 0 until the end of the current turn.":
        "Вторинною дією ви надаєте собі перевагу для кидка атаки зброєю дальнього бою в поточний хід. Цю особливість можна використати, лише якщо ви ще не пересувалися цього ходу; після її використання ваша швидкість дорівнює 0 до кінця ходу.",
    "While Bloodied, you can take a Bonus Action to gain Temporary Hit Points equal to your Artificer level. You lose these Temporary Hit Points if you doff the armor.":
        "Поки ви закривавлені, вторинною дією можете отримати тимчасові очки здоров’я в кількості, що дорівнює вашому рівню винахідника. Знявши обладунки, ви втрачаєте ці тимчасові очки здоров’я.",
    "You replace the Defensive Tactics option with the other one.":
        "Ви замінюєте поточний варіант «Захисної тактики» на інший.",
    "Opportunity Attacks have Disadvantage against you.":
        "Принагідні атаки проти вас виконуються із завадою.",
    "When a creature hits you with an attack roll, that creature has Disadvantage on all other attack rolls against you this turn.":
        "Коли істота влучає у вас атакою, до кінця цього ходу вона має заваду для всіх наступних кидків атаки проти вас.",
    "You can expend one use of your Breath Weapon to roar, forcing each creature of your choice within 30 feet of you to make a Wisdom saving throw. On a failed save, a target becomes frightened of you for 1 minute.":
        "Ви можете витратити одне використання Дихальної зброї, щоб заревти й змусити кожну вибрану вами істоту в межах 30 футів виконати кидок протидії мудрістю. У разі невдачі ціль боїться вас протягом 1 хвилини.",
    "When you reach Druid levels 6 and 10, your Dragon Shape becomes more powerful.":
        "На 6-му й 10-му рівнях друїда ваша Подоба дракона стає могутнішою.",
    """You can expend a use of your Wild Shape feature as a bonus action to transform into a unique form: your dragon shape. You become a Medium dragon while in this form, standing on all fours, but retain your normal character statistics and senses.

While in Dragon Shape, you can use claw attacks and a breath weapon. You gain a flying speed equal to twice your movement speed, and you have Resistance to Acid, Cold, Fire, Lightning, and Poison damage.""":
        """Вторинною дією ви можете витратити використання Дикої подоби, щоб перетворитися на унікальну Подобу дракона. У цій подобі ви стаєте середнім драконом на чотирьох лапах, але зберігаєте звичайні характеристики й чуття персонажа.

У Подобі дракона ви можете атакувати кігтями й застосовувати дихальну зброю. Ваша швидкість польоту вдвічі більша за звичайну швидкість, а також ви маєте стійкість до кислотної, холодової, вогняної, блискавкової та отруйної шкоди.""",
    "You form a Dread Allegiance by choosing one of the Dead Three: Bane, Bhaal, or Myrkul. Your choice grants you Resistance to a specific damage type and the ability to cast an associated cantrip, using Intelligence as your spellcasting ability.":
        "Ви укладаєте Моторошну відданість, обираючи одного з Мертвої Трійці: Бейна, Баала або Міркула. Ваш вибір надає стійкість до певного типу шкоди й змогу проказувати відповідне замовляння, використовуючи інтелект як базову характеристику проказування.",
    "If you choose Bane, you gain Resistance to Psychic damage and can cast <LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Minor Illusion</LSTag>.":
        "Якщо ви обираєте Бейна, ви отримуєте стійкість до психічної шкоди й можете проказувати <LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Малу ілюзію</LSTag>.",
    "If you choose Bhaal, you gain Resistance to Poison damage and can cast <LSTag Type=\"Spell\" Tooltip=\"Shout_BladeWard\">Blade Ward</LSTag>.":
        "Якщо ви обираєте Баала, ви отримуєте стійкість до отруйної шкоди й можете проказувати <LSTag Type=\"Spell\" Tooltip=\"Shout_BladeWard\">Оберіг від зброї</LSTag>.",
    "If you choose Myrkul, you gain Resistance to Necrotic damage and can cast Chill Touch.":
        "Якщо ви обираєте Міркула, ви отримуєте стійкість до некротичної шкоди й можете проказувати Крижаний дотик.",
    "The cannon emits a burst of positive energy that grants itself and each creature of your choice within 10 feet of the cannon a number of Temporary Hit Points equal to 1d8 plus your Intelligence modifier (minimum of +1).":
        "Гармата випромінює сплеск позитивної енергії, надаючи собі й кожній вибраній вами істоті в межах 10 футів тимчасові очки здоров’я в кількості 1d8 + ваш модифікатор інтелекту (щонайменше +1).",
    "You create a Elixir of Bloodlust.":
        "Ви створюєте еліксир жаги крові.",
    "You create a Elixir of the Colossus.":
        "Ви створюєте еліксир колоса.",
    "You create a Potion of Feather Fall.":
        "Ви створюєте зілля «Легкість пір’їни».",
    "You create a Potion of Flying.":
        "Ви створюєте зілля польоту.",
    "You create a Potion of Glorious Vaulting.":
        "Ви створюєте зілля надзвичайних стрибків.",
    "You create a Potion of Healing. The amount it restores increases when you reach 5th and 9th level in this class.":
        "Ви створюєте цілюще зілля. Кількість очок здоров’я, які воно відновлює, збільшується на 5-му й 9-му рівнях цього класу.",
    "You create a Elixir of Heroism.":
        "Ви створюєте еліксир героїзму.",
    "You create a Elixir of Hill Giant Strength.":
        "Ви створюєте еліксир сили гірського велета.",
    "You create a Potion of Invisibility.":
        "Ви створюєте зілля невидимості.",
    "You create a Elixir of Peerless Focus.":
        "Ви створюєте еліксир незрівнянного зосередження.",
    "You regain expended uses of Experimental Elixir.":
        "Ви відновлюєте витрачені використання «Експериментального еліксиру».",
    "You create a Potion of Speed.":
        "Ви створюєте зілля швидкості.",
    "You create a Elixir of Vigilance.":
        "Ви створюєте еліксир пильності.",
    "Arcane wards protect you against magic for the duration. You have Advantage on saving throws against spells and magical effects. Additionally, you have Resistance to damage from spells.":
        "На час дії магічні обереги захищають вас від чарів. Ви маєте перевагу для кидків протидії закляттям і магічним ефектам, а також стійкість до шкоди від заклять.",
    "You can use your action on each of your turns to automatically deal [1] necrotic damage to the target.":
        "У кожен свій хід ви можете дією автоматично завдати цілі [1] некротичної шкоди.",
    "You instantly create a potion of your choice.":
        "Ви миттєво створюєте вибране вами зілля.",
    "As an action, you can magically share the darkvision with willing creatures you can see within 30 feet of you.":
        "Дією ви можете магічно поділитися темнозором з охочими істотами, яких бачите в межах 30 футів.",
    "As a bonus action, you can magically become invisible for 1 minute.":
        "Вторинною дією ви можете магічно набути невидимості на 1 хвилину.",
    "You gain 2d4 + [1] <LSTag Tooltip=\"TemporaryHitPoints\">temporary hit points</LSTag>.":
        "Ви отримуєте 2d4 + [1] <LSTag Tooltip=\"TemporaryHitPoints\">тимчасових очок здоров’я</LSTag>.",
    "Once per Long Rest, you grant yourself and allies within 30 feet of you Advantage on Initiative rolls.":
        "Раз за довгий відпочинок ви надаєте собі й союзникам у межах 30 футів перевагу для кидків ініціативи.",
    """You summon an otherworldly steed and immediately mount it.

The steed can take one of the following actions of your choice on each of its turns: <LSTag Type="Spell" Tooltip="Shout_Dash">Dash</LSTag>, Disengage, Dodge, or Attack.

While mounted on the steed, when you take damage of 4 or higher, you must make a DC 8 Dexterity saving throw. On a failed save, you fall off the steed and have the Prone condition for 1 turn.


Only a player with a pure heart can see the steed.""":
        """Ви прикликаєте потойбічного скакуна й одразу сідаєте на нього верхи.

У кожен свій хід скакун може виконати одну з вибраних вами дій: <LSTag Type="Spell" Tooltip="Shout_Dash">Ривок</LSTag>, Відступ, Ухилення або Атаку.

Перебуваючи верхи, щоразу, коли ви зазнаєте 4 або більше шкоди, мусите виконати кидок протидії спритністю зі СК 8. У разі невдачі ви падаєте зі скакуна й перебуваєте в стані повалення протягом 1 ходу.


Скакуна може побачити лише гравець із чистим серцем.""",
    "You conjure motes of dancing flame that hover and drift around you for the duration. At the start of each of their turns, non-allied creatures within 20 feet of the flames must succeed on a Wisdom saving throw or become charmed until the start of their next turn. While charmed in this way, the creature is incapacitated and has a speed of 0.":
        "Ви прикликаєте іскорки танцюючого полум’я, які ширяють навколо вас протягом усієї дії закляття. На початку кожного свого ходу істоти, що не є вашими союзниками й перебувають у межах 20 футів від полум’я, повинні успішно виконати кидок протидії мудрістю, інакше будуть зачаровані до початку свого наступного ходу. Зачарована в такий спосіб істота недієздатна, а її швидкість дорівнює 0.",
    "Expend a spell slot to regain one expended use of Bardic Inspiration.":
        "Витратьте чарунку заклять, щоб відновити одне витрачене використання Бардівського натхнення.",
    """As a Bonus Action, you transform into an avatar of your patron’s dreadful power, gaining the benefits below for 1 minute, until you have the Incapacitated condition, or until you end the form (no action required). You can transform a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.

Facsimile of Life. You gain Temporary Hit Points equal to 1d10 plus your Warlock level.

Fearless Form. You have Immunity to the Frightened condition. If you are Frightened when you transform, the condition immediately ends for you.

Frightful Avatar. Once per turn, when you hit a creature with an attack roll, you can force it to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the Frightened condition until the end of your next turn.""":
        """Вторинною дією ви перетворюєтеся на втілення жахливої сили свого покровителя й отримуєте наведені нижче переваги на 1 хвилину — доки не станете недієздатними або не припините цю подобу (дія не потрібна). Ви можете перетворитися стільки разів, скільки становить ваш модифікатор харизми (щонайменше один раз), і відновлюєте всі витрачені використання після довгого відпочинку.

Відбиток життя. Ви отримуєте тимчасові очки здоров’я в кількості 1d10 + ваш рівень чаклуна.

Безстрашна подоба. Ви маєте імунітет до переляку. Якщо в мить перетворення ви налякані, цей стан негайно припиняється.

Жахливе втілення. Раз за хід, коли ви влучаєте в істоту атакою, можете змусити її виконати кидок протидії мудрістю проти вашої СК протидії закляттям. У разі невдачі ціль перебуває в стані переляку до кінця вашого наступного ходу.""",
    "Until the spell ends, you have Resistance to Radiant damage, and your melee attacks deal an extra [1] on a hit.":
        "До завершення закляття ви маєте стійкість до променевої шкоди, а ваші атаки ближнього бою в разі влучання завдають додатково [1].",
    "You gain a +2 bonus to all ability checks and saving throws that use Strength or Constitution.":
        "Ви отримуєте бонус +2 до всіх перевірок характеристик і кидків протидії, що використовують силу або статуру.",
    "As a bonus action, you can cause a melee weapon you are wielding to emit dim light in a 10-foot radius for 10 turns. The light is sunlight. While the weapon gleams, it deals radiant damage instead of its normal damage type.":
        "Вторинною дією ви можете змусити зброю ближнього бою у своїх руках протягом 10 ходів випромінювати тьмяне світло в радіусі 10 футів. Це світло вважається сонячним. Доки зброя сяє, вона завдає променевої шкоди замість звичайного типу шкоди.",
    """At the start of your turn, you can expend 1 Focus Point to imbue yourself with elemental energy. The energy lasts for 10 minutes. You gain the following benefits while this feature is active.

Reach: When you make an Unarmed Strike, your reach is [1] greater than normal, as elemental energy extends from you.

Elemental Strikes: Whenever you hit with your Unarmed Strike, you can cause it to deal your choice of Acid, Cold, Fire, Lightning, or Thunder damage rather than its normal damage type. When you deal one of these types with it, you can also force the target to make a Strength saving throw. On a failed save, you can move the target up to [1] toward or away from you, as elemental energy swirls around it.""":
        """На початку свого ходу ви можете витратити 1 очко зосередження, щоб наситити себе стихійною енергією на 10 хвилин. Поки ця особливість діє, ви отримуєте наведені нижче переваги.

Досяжність. Коли ви завдаєте Удару голіруч, ваша досяжність збільшується на [1], адже від вас простягається стихійна енергія.

Стихійні удари. Щоразу, коли ви влучаєте Ударом голіруч, можете замінити його звичайний тип шкоди на кислотну, холодову, вогняну, блискавкову або громову шкоду. У такому разі ви також можете змусити ціль виконати кидок протидії силою. У разі невдачі можете перемістити ціль на відстань до [1] до себе або від себе, поки навколо неї вирує стихійна енергія.""",
    "At the start of each of your turns, you can spend 1 Sorcery Point to gain Temporary Hit Points equal to 1d6 plus your Sorcerer level (no action required).":
        "На початку кожного свого ходу ви можете витратити 1 очко чародійства, щоб отримати тимчасові очки здоров’я в кількості 1d6 + ваш рівень чародія (дія не потрібна).",
    "You can invoke the rune as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage for 1 minute.":
        "Вторинною дією ви можете активувати руну й на 1 хвилину отримати стійкість до дробильної, колотої та рубаної шкоди.",
    "You can spend Hit Dice during a Short Rest to regain Hit Points.":
        "Під час короткого відпочинку ви можете витрачати кістки здоров’я, щоб відновлювати очки здоров’я.",
    "As a bonus action on your turn, you can dismiss this spell and cause the weapon to emit a burst of radiance. Each creature of your choice that you can see within 30 feet of the weapon must make a Constitution saving throw. On a failed save, a creature takes 4d8 radiant damage, and it is blinded for 1 minute. On a successful save, a creature takes half as much damage and isn’t blinded. At the end of each of its turns, a blinded creature can make a Constitution saving throw, ending the effect on itself on a success.":
        "Вторинною дією у свій хід ви можете припинити це закляття й змусити зброю випустити спалах сяйва. Кожна вибрана вами істота, яку ви бачите в межах 30 футів від зброї, повинна виконати кидок протидії статурою. У разі невдачі істота зазнає 4d8 променевої шкоди й сліпне на 1 хвилину. У разі успіху вона зазнає вдвічі менше шкоди й не сліпне. Наприкінці кожного свого ходу засліплена істота може повторити кидок протидії статурою, у разі успіху припиняючи дію ефекту на собі.",
    "You can spend 1 minute grooming and caring for your mount, at the end of which it gains a number of Temporary Hit Points equal to twice your Rogue level.":
        "Ви можете витратити 1 хвилину на догляд за своїм скакуном, після чого він отримує тимчасові очки здоров’я в кількості, що дорівнює подвоєному рівню вашого пройдисвіта.",
    "You imbue a weapon you are holding, or your Unarmed Strikes, with ravenous negative energy. For the duration, when you hit a creature with an attack using the empowered weapon or Unarmed Strike for the first time on a turn, the target takes Necrotic damage equal to your spellcasting ability modifier, and you gain a number of Temporary Hit Points equal to the Necrotic damage dealt.":
        "Ви насичуєте зброю у своїх руках або Удари голіруч ненаситною негативною енергією. На час дії, коли ви вперше за хід влучаєте в істоту атакою посиленою зброєю або Ударом голіруч, ціль зазнає некротичної шкоди в кількості, що дорівнює модифікатору вашої базової характеристики проказування, а ви отримуєте стільки ж тимчасових очок здоров’я.",
    "You replace the Hunter’s Prey option with the other one.":
        "Ви замінюєте поточний варіант «Здобичі мисливця» на інший.",
    "Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon, the weapon deals an extra 1d8 damage to the target if it’s missing any of its Hit Points. You can deal this extra damage only once per turn.":
        "Ваша завзятість здатна виснажити навіть найвитриваліших ворогів. Коли ви влучаєте в істоту зброєю, та завдає цілі додатково 1d8 шкоди, якщо ціль втратила хоча б частину очок здоров’я. Цю додаткову шкоду можна завдати лише раз за хід.",
    "Once on each of your turns when you make an attack with a weapon, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target, that is within the weapon’s range, and that you haven’t attacked this turn.":
        "Раз у кожен свій хід, атакуючи зброєю, ви можете виконати ще одну атаку тією самою зброєю проти іншої істоти, яка перебуває в межах 5 футів від початкової цілі, у межах досяжності зброї та яку ви ще не атакували цього ходу.",
    """A Weapon you are holding is imbued with nature’s power. For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon’s damage die becomes a d8. If the attack deals damage, it is Force damage.

The spell ends early if you cast it again or if you let go of the weapon.

Cantrip Upgrade. The damage die changes when you reach levels 5 (d10), 10 (d12).""":
        """Зброя у ваших руках насичується силою природи. На час дії ви можете використовувати базову характеристику проказування замість сили для кидків атаки й шкоди атак ближнього бою цією зброєю, а її кістка шкоди стає d8. Завдана атакою шкода є силовою.

Закляття завершується достроково, якщо ви прокажете його знову або випустите зброю з рук.

Поліпшення замовляння. Кістка шкоди змінюється на 5-му рівні (d10) і 10-му рівні (d12).""",
    """An event in your past left an indelible mark on you, infusing you with simmering magic. As a Bonus Action, you can unleash that magic for 1 minute, during which you gain the following benefits:

The spell save DC of your Sorcerer spells increases by 1.
You have Advantage on the attack rolls of Sorcerer spells you cast.

You can use this feature twice, and you regain all expended uses of it when you finish a Long Rest.""":
        """Подія з вашого минулого залишила незгладимий слід і сповнила вас магією, що нуртує всередині. Вторинною дією ви можете вивільнити її на 1 хвилину й отримати такі переваги:

СК протидії вашим закляттям чародія збільшується на 1.
Ви маєте перевагу для кидків атаки закляттями чародія.

Цю особливість можна використати двічі; усі витрачені використання відновлюються після довгого відпочинку.""",
    "When you finish a Short or Long Rest, you can give an inspiring performance: a speech, song, or dance. You can use this feature once per Short Rest. When you do so, each ally within 30 feet of you gains Temporary Hit Points equal to your character level plus your Proficiency Bonus.":
        "Після короткого або довгого відпочинку ви можете влаштувати натхненний виступ: виголосити промову, заспівати чи станцювати. Цю особливість можна використати раз за короткий відпочинок. Кожен союзник у межах 30 футів від вас отримує тимчасові очки здоров’я в кількості, що дорівнює вашому рівню персонажа + бонус спеціалізації.",
    "You can take a Reaction and expend one use of your Bardic Inspiration to move up to half your Speed. Then one ally of your choice within 30 feet of you can also move up to half their Speed. None of this feature’s movement provokes Opportunity Attacks.":
        "Реагуванням ви можете витратити одне використання Бардівського натхнення й переміститися на відстань до половини своєї швидкості. Потім один вибраний вами союзник у межах 30 футів також може переміститися на відстань до половини своєї швидкості. Це переміщення не провокує принагідних атак.",
    "You can use a bonus action on your turn to make your ranged attacks with a kensei weapon more deadly. When you do so, any target you hit with a ranged attack using a kensei weapon takes an extra 1d4 damage of the weapon’s type. You retain this benefit until the end of the current turn.":
        "Вторинною дією у свій хід ви можете посилити атаки дальнього бою зброєю кенсея. До кінця поточного ходу кожна ціль, у яку ви влучите такою атакою, зазнає додатково 1d4 шкоди того самого типу, що й зброя.",
    "Starting at character level 5, you can change your size to Large as a Bonus Action if you’re in a big enough space. This transformation lasts for 10 minutes.":
        "Починаючи з 5-го рівня персонажа, вторинною дією ви можете збільшитися до великого розміру, якщо для цього достатньо місця. Перетворення триває 10 хвилин.",
    "By expending a Risk Die, you roll a d20. If the result is 10 or higher, the damage of your next ranged weapon attack is doubled. If the result is lower than 10, the damage of your ranged weapon attacks this turn is halved.":
        "Витративши кістку ризику, киньте d20. Якщо результат становить 10 або більше, шкода вашої наступної атаки зброєю дальнього бою подвоюється. Якщо результат менший за 10, шкода ваших атак зброєю дальнього бою цього ходу зменшується вдвічі.",
    """Cantrip learning mode is active. All Cleric cantrips are added to your spell list.

Selecting a cantrip to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting two different cantrips, this mode ends.""":
        """Активовано режим вивчення замовлянь. Усі замовляння клірика додано до вашого списку заклять.

Щойно ви виберете замовляння для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору двох різних замовлянь.""",
    """Spell learning mode is active. All Cleric spells are added to your spell list.

Selecting a spell to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting a spell, this mode ends.""":
        """Активовано режим вивчення заклять. Усі закляття клірика додано до вашого списку заклять.

Щойно ви виберете закляття для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору закляття.""",
    """Cantrip learning mode is active. All Druid cantrips are added to your spell list.

Selecting a cantrip to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting two different cantrips, this mode ends.""":
        """Активовано режим вивчення замовлянь. Усі замовляння друїда додано до вашого списку заклять.

Щойно ви виберете замовляння для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору двох різних замовлянь.""",
    """Spell learning mode is active. All Druid spells are added to your spell list.

Selecting a spell to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting a spell, this mode ends.""":
        """Активовано режим вивчення заклять. Усі закляття друїда додано до вашого списку заклять.

Щойно ви виберете закляття для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору закляття.""",
    """Cantrip learning mode is active. All Wizard cantrips are added to your spell list.

Selecting a cantrip to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting two different cantrips, this mode ends.""":
        """Активовано режим вивчення замовлянь. Усі замовляння чарівника додано до вашого списку заклять.

Щойно ви виберете замовляння для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору двох різних замовлянь.""",
    """Spell learning mode is active. All Wizard spells are added to your spell list.

Selecting a spell to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting a spell, this mode ends.""":
        """Активовано режим вивчення заклять. Усі закляття чарівника додано до вашого списку заклять.

Щойно ви виберете закляття для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору закляття.""",
    "You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell slots but no more than a number equal to half your maximum (round up). Once you use this feature, you can’t do so again until you finish a Long Rest.":
        "Ви можете протягом 1 хвилини виконувати езотеричний обряд. Після його завершення ви відновлюєте витрачені чарунки Магії договору в кількості, що не перевищує половини вашого максимуму (з округленням угору). Після використання цієї особливості ви не зможете скористатися нею знову до завершення довгого відпочинку.",
    "For 1 minute, your blood becomes acidic. Each time a creature hits you with an attack while within 5 feet of you, it takes 2d6 Acid damage.":
        "На 1 хвилину ваша кров стає кислотною. Щоразу, коли істота в межах 5 футів влучає у вас атакою, вона зазнає 2d6 кислотної шкоди.",
    "For 1 hour, you have Advantage on <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Intimidation</LSTag> and <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag> check.":
        "Протягом 1 години ви маєте перевагу для перевірок <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливості</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Залякування</LSTag> й <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливості</LSTag>.",
    "For 10 minutes, you grow leathery, feathery, or spectral wings from your back. You gain a Fly Speed equal to your Speed. You can’t benefit from this mutation while wearing Heavy armor.":
        "На 10 хвилин у вас за спиною виростають шкірясті, пір’яні або примарні крила. Ваша швидкість польоту дорівнює звичайній швидкості. Ця мутація не діє, поки ви носите важкі обладунки.",
    "Choose one of the following damage types: Acid, Cold, Fire, Lightning, Poison, or Thunder. For 10 minutes, whenever you hit with a weapon attack, you can cause it to deal the chosen type rather than its normal damage type.":
        "Виберіть один із типів шкоди: кислотна, холодова, вогняна, блискавкова, отруйна або громова. Протягом 10 хвилин, коли ви влучаєте атакою зброєю, можете замінити її звичайний тип шкоди на вибраний.",
    "For 10 minutes, you have the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition. This effect ends early if you dismiss it (no action required), or you attack or cast a spell.":
        "Протягом 10 хвилин ви маєте стан <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимість</LSTag>. Ефект завершується достроково, якщо ви його припините (дія не потрібна), атакуєте або прокажете закляття.",
    "For 1 minute, you have Advantage on Strength checks and saving throws. You also have Advantage on attack rolls using Strength, and you deal 1d6 extra damage to targets you hit with a Strength-based attack. The damage is the same type dealt by the attack.":
        "Протягом 1 хвилини ви маєте перевагу для перевірок сили й кидків протидії силою, а також для кидків атак, що використовують силу. Влучаючи атакою на основі сили, ви завдаєте цілі додатково 1d6 шкоди того самого типу, що й атака.",
    "You regain Hit Points equal to 2d8 plus your Monster Hunter level.":
        "Ви відновлюєте очки здоров’я в кількості 2d8 + ваш рівень мисливця на чудовиськ.",
    "For 1 minute, you have Resistance to Bludgeoning, Piercing, and Slashing damage.":
        "Протягом 1 хвилини ви маєте стійкість до дробильної, колотої та рубаної шкоди.",
    "Vanish into the darkness and become <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag>.":
        "Зникніть у темряві й станьте <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">невидимими</LSTag>.",
    """As a Bonus Action, you can conjure a pact weapon in your hand—a Simple or Martial Melee weapon of your choice with which you bond—or create a bond with a magic weapon you touch; you can’t bond with a magic weapon if someone else is attuned to it or another Warlock is bonded with it. Until the bond ends, you have proficiency with the weapon, and you can use it as a Spellcasting Focus.

Whenever you attack with the bonded weapon, you can use your Charisma modifier for the attack and damage rolls instead of using Strength or Dexterity; and you can cause the weapon to deal Necrotic, Psychic, or Radiant damage or its normal damage type.

Your bond with the weapon ends if you use this feature’s Bonus Action again, if the weapon is more than 5 feet away from you for 1 minute or more, or if you die. A conjured weapon disappears when the bond ends.""":
        """Вторинною дією ви можете прикликати в руку зброю договору — вибрану просту або бойову зброю ближнього бою, з якою встановлюєте зв’язок, — або зв’язатися з магічною зброєю, якої торкаєтеся. Ви не можете зв’язатися з магічною зброєю, якщо на неї налаштований хтось інший або з нею вже зв’язаний інший чаклун. До припинення зв’язку ви володієте цією зброєю й можете використовувати її як фокус проказування.

Атакуючи зв’язаною зброєю, ви можете використовувати модифікатор харизми замість сили чи спритності для кидків атаки й шкоди, а також завдавати нею некротичної, психічної, променевої шкоди або шкоди її звичайного типу.

Зв’язок зі зброєю припиняється, якщо ви знову використаєте вторинну дію цієї особливості, якщо зброя перебуватиме далі ніж за 5 футів від вас протягом щонайменше 1 хвилини або якщо ви помрете. Прикликана зброя зникає після припинення зв’язку.""",
    """Cantrip learning mode is active. Every cantrip from every class's spell list is added to your spell list.

Selecting a cantrip to cast permanently teaches it to you right away — you don't need a valid target or to finish casting it.

After selecting three different cantrips, this mode ends.""":
        """Активовано режим вивчення замовлянь. Усі замовляння зі списків заклять усіх класів додано до вашого списку заклять.

Щойно ви виберете замовляння для проказування, то назавжди вивчите його — не потрібно вибирати дійсну ціль або завершувати проказування.

Режим завершується після вибору трьох різних замовлянь.""",
    "You can expend 1 Focus Point to take both the Disengage and the Dodge actions as a Bonus Action.":
        "Ви можете витратити 1 очко зосередження, щоб вторинною дією виконати одночасно Відступ та Ухилення.",
    "Apply Poison or Toxin to your currently equipped weapon set.":
        "Нанесіть отруту або токсин на споряджений комплект зброї.",
    "The Poison you apply becomes more potent each time you reach Rogue levels 5 and 9.":
        "Нанесена вами отрута стає сильнішою на 5-му й 9-му рівнях пройдисвіта.",
    "The Poison you apply becomes more potent each time you reach levels 5 and 9.":
        "Нанесена вами отрута стає сильнішою на 5-му й 9-му рівнях.",
    "Apply Poison to your currently equipped weapon set.":
        "Нанесіть отруту на споряджений комплект зброї.",
    "Apply Toxin to your currently equipped weapon set.":
        "Нанесіть токсин на споряджений комплект зброї.",
    "When you apply a toxin, you can deal damage immediately. The Poison you apply becomes more potent each time you reach Rogue levels 5 and 9.":
        "Наносячи токсин, ви можете негайно завдати шкоди. Нанесена вами отрута стає сильнішою на 5-му й 9-му рівнях пройдисвіта.",
    "When you apply a toxin, you can deal damage immediately. The Poison you apply becomes more potent each time you reach levels 5 and 9.":
        "Наносячи токсин, ви можете негайно завдати шкоди. Нанесена вами отрута стає сильнішою на 5-му й 9-му рівнях.",
    "Gain the benefits of a Short Rest.":
        "Отримайте всі переваги короткого відпочинку.",
    """You create a minor magical effect within range, producing one of the following results:

Ignite. You light a light source, such as a candle, torch, or small campfire.
Snuff. You extinguish a light source, such as a candle, torch, or small campfire.
Clean. You instantaneously clean an object no larger than 1 cubic foot.""":
        """Ви створюєте в межах досяжності незначний магічний ефект з одним із таких результатів:

Запалити. Ви запалюєте джерело світла, наприклад свічку, смолоскип або невелике багаття.
Загасити. Ви гасите джерело світла, наприклад свічку, смолоскип або невелике багаття.
Очистити. Ви миттєво очищуєте предмет об’ємом не більше 1 кубічного фута.""",
    "You instantaneously clean an object no larger than 1 cubic foot.":
        "Ви миттєво очищуєте предмет об’ємом не більше 1 кубічного фута.",
    "You extinguish a light source, such as a candle, torch, or small campfire.":
        "Ви гасите джерело світла, наприклад свічку, смолоскип або невелике багаття.",
    "You light a light source, such as a candle, torch, or small campfire.":
        "Ви запалюєте джерело світла, наприклад свічку, смолоскип або невелике багаття.",
    """You can manifest shimmering blades of psychic energy.

While wielding a dagger, shortsword, or scimitar, you can change the weapon’s damage type to Psychic and give it the <LSTag Tooltip="Thrown">Thrown</LSTag> property.""":
        """Ви можете матеріалізувати мерехтливі клинки з психічної енергії.

Тримаючи кинджал, короткий меч або скімітар, ви можете змінити тип шкоди зброї на психічний і надати їй властивість <LSTag Tooltip="Thrown">Метальне</LSTag>.""",
    "You can weave a veil of psychic static to mask yourself. As a Magic action, you gain the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition for 1 hour. This invisibility ends early immediately after you deal damage to a creature or you force a creature to make a saving throw.":
        "Ви можете сплести завісу психічних завад, щоб приховати себе. Магічною дією ви набуваєте стану <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимість</LSTag> на 1 годину. Невидимість достроково припиняється одразу після того, як ви завдасте істоті шкоди або змусите її виконати кидок протидії.",
    "As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to emit a flash of light in a 30-foot Emanation originating from yourself. Any magical Darkness—such as that created by the Darkness spell—in that area is dispelled. Additionally, each creature of your choice in that area must make a Constitution saving throw, taking Radiant damage equal to 2d10 plus your Cleric level on a failed save or half as much damage on a successful one.":
        "Магічною дією ви здіймаєте священний символ і витрачаєте одне використання Божого наснаження, випускаючи від себе спалах світла у 30-футовій еманації. Уся магічна Темрява в цій зоні — зокрема створена закляттям «Темрява» — розвіюється. Крім того, кожна вибрана вами істота в зоні повинна виконати кидок протидії статурою. У разі невдачі вона зазнає променевої шкоди в кількості 2d10 + ваш рівень клірика, а в разі успіху — вдвічі менше.",
    "You can use <LSTag Type=\"Spell\" Tooltip=\"Shout_PackHowl_Barbarian\">Inciting Howl</LSTag>, and your allies have <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag> against enemies within [1] of you.":
        "Ви можете застосовувати <LSTag Type=\"Spell\" Tooltip=\"Shout_PackHowl_Barbarian\">Підбурливе виття</LSTag>, а ваші союзники мають <LSTag Tooltip=\"Advantage\">перевагу</LSTag> для <LSTag Tooltip=\"AttackRoll\">кидків атаки</LSTag> проти ворогів у межах [1] від вас.",
    "Expend a spell slot to regain the use of your Ranger's Companion.":
        "Витратьте чарунку заклять, щоб відновити використання Супутника слідопита.",
    "As a Bonus Action, you give yourself Advantage on your next attack roll on the current turn.":
        "Вторинною дією ви надаєте собі перевагу для наступного кидка атаки в поточний хід.",
    "Whenever you finish a Short Rest, you can perform a ritual on a melee weapon you are proficient with that deals Piercing or Slashing damage, sanctifying it. It becomes your sanctified blade, and you can only have one such blade at a time. The blade gains the Finesse property for you, and attacks made with it against Aberrations, Fiends, and Undead ignore Resistance to damage.":
        "Після кожного короткого відпочинку ви можете виконати ритуал над зброєю ближнього бою, якою володієте та яка завдає колотої або рубаної шкоди, освятивши її. Вона стає вашим Освяченим клинком; одночасно ви можете мати лише один такий клинок. Для вас він набуває властивості «Фехтувальна», а атаки ним проти покручів, нечисті й невмерлих ігнорують стійкість до шкоди.",
    "This spell is a dummy with no functionality. When choosing a spell to add to your spellbook through the Wizard's Savant feature, level-up cannot proceed if you have already learned every eligible spell by other means, such as scribing scrolls, leaving nothing left to pick. This spell was added as a workaround for that situation.":
        "Це службове закляття без власної функції. Під час вибору закляття для додавання до книги заклять за допомогою особливості «Знавець-чарівник» підвищення рівня неможливо продовжити, якщо ви вже вивчили всі доступні закляття в інший спосіб — наприклад, переписавши їх із сувоїв, — і вибирати більше нічого. Це закляття додано як технічний обхід такого випадку.",
    "While you are <LSTag Type=\"Status\" Tooltip=\"RAGE\">raging</LSTag>, once per turn, you can emit tendrils of shadow smoke. The smoke extends 10 feet from you in every direction. Any creature other than you that is within the smoke is <LSTag Type=\"Status\" Tooltip=\"BLINDED\">Blinded</LSTag>.":
        "Під час <LSTag Type=\"Status\" Tooltip=\"RAGE\">люті</LSTag> ви раз за хід можете випустити пасма тіньового диму. Дим простягається на 10 футів від вас у всіх напрямках. Усі істоти в диму, крім вас, перебувають у стані <LSTag Type=\"Status\" Tooltip=\"BLINDED\">Сліпота</LSTag>.",
    "You gain the ability to augment your weapons further with your ki. As a bonus action, you can expend 1 ki points to grant one kensei weapon you touch a bonus to attack and damage rolls when you attack with it. This bonus lasts for 1 minute or until you use this feature again.":
        "Ви навчаєтеся додатково посилювати зброю за допомогою кі. Вторинною дією ви можете витратити 1 очко кі, щоб надати одній зброї кенсея, якої торкаєтеся, бонус до кидків атаки й шкоди нею. Бонус діє 1 хвилину або доки ви не скористаєтеся цією особливістю знову.",
    """A Club or Quarterstaff you are holding is imbued with nature’s power. For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon, and the weapon’s damage die becomes a d8. If the attack deals damage, it is Force damage.

The spell ends early if you cast it again or if you let go of the weapon.

Cantrip Upgrade. The damage die changes when you reach levels 5 (d10), 10 (d12).""":
        """Палиця або бойовий посох у ваших руках насичується силою природи. На час дії ви можете використовувати базову характеристику проказування замість сили для кидків атаки й шкоди атак ближнього бою цією зброєю, а її кістка шкоди стає d8. Завдана атакою шкода є силовою.

Закляття завершується достроково, якщо ви прокажете його знову або випустите зброю з рук.

Поліпшення замовляння. Кістка шкоди змінюється на 5-му рівні (d10) і 10-му рівні (d12).""",
    """Home can be wherever you are. You draw upon the Gloaming Court’s quiet dominion over shadow and secrecy, wrapping yourself and your allies in its subtle protection. As an action, you invoke this power to conjure a protective refuge and immediately gain the benefits of a short rest.

Until you complete your next long rest, you and your allies gain a +5 bonus to Dexterity (<LSTag Type="Skills" Tooltip="Stealth">Stealth</LSTag>) and Wisdom (<LSTag Type="Skills" Tooltip="Perception">Perception</LSTag>) checks.""":
        """Ваш дім — там, де ви. Ви звертаєтеся до тихої влади Присмеркового двору над тінню й таємницями, огортаючи себе та союзників його непомітним захистом. Дією ви прикликаєте цю силу, створюєте захищений прихисток і негайно отримуєте всі переваги короткого відпочинку.

До завершення вашого наступного довгого відпочинку ви й ваші союзники отримуєте бонус +5 до перевірок спритності (<LSTag Type="Skills" Tooltip="Stealth">Непомітність</LSTag>) і мудрості (<LSTag Type="Skills" Tooltip="Perception">Відчуття</LSTag>).""",
    "You regain Sorcery Points equal to half your maximum.":
        "Ви відновлюєте очки чародійства в кількості, що дорівнює половині вашого максимуму.",
    "As a Bonus Action, you give yourself Advantage on your next attack roll on the current turn. You can use this feature only if you haven’t moved during this turn, and after you use it, your Speed is 0 until the end of the current turn.":
        "Вторинною дією ви надаєте собі перевагу для наступного кидка атаки в поточний хід. Цю особливість можна використати, лише якщо ви ще не пересувалися цього ходу; після її використання ваша швидкість дорівнює 0 до кінця ходу.",
    "You can expend 1 Focus Point to take both the Disengage and <LSTag Type=\"Spell\" Tooltip=\"Shout_Dash\">Dash</LSTag> actions as a Bonus Action, and your jump distance is doubled for the turn.":
        "Ви можете витратити 1 очко зосередження, щоб вторинною дією виконати одночасно Відступ і <LSTag Type=\"Spell\" Tooltip=\"Shout_Dash\">Ривок</LSTag>. До кінця ходу дальність ваших стрибків подвоюється.",
    "You can draw on the mystical power of night to rise into the air. As a bonus action when you are in dim light or darkness, you can magically give yourself a flying speed equal to your walking speed for 1 minute. You can use this bonus action a number of times equal to your wisdom modifier, and you regain all expended uses when you finish a long rest.":
        "Ви можете звернутися до містичної сили ночі й здійнятися в повітря. Перебуваючи в тьмяному світлі або темряві, ви можете вторинною дією на 1 хвилину магічно отримати швидкість польоту, що дорівнює швидкості ходьби. Цю вторинну дію можна використати стільки разів, скільки становить ваш модифікатор мудрості; усі витрачені використання відновлюються після довгого відпочинку.",
    "You can invoke the rune as a bonus action to enter a prophetic state for 1 minute or until you’re incapacitated. Until the state ends, when you or another creature you can see within 60 feet of you makes an attack roll, a saving throw, or an ability check, you can use your reaction to cause the roll to have advantage or disadvantage.":
        "Вторинною дією ви можете активувати руну й увійти в пророчий стан на 1 хвилину або до набуття недієздатності. Доки цей стан триває, коли ви або інша видима вам істота в межах 60 футів виконує кидок атаки, кидок протидії чи перевірку характеристики, ви можете реагуванням надати цьому кидку перевагу або заваду.",
    "You have absorbed primeval magic that gives you an echo of the might of giants. When you take this feat, choose one of the benefits listed below. Once per turn, when you hit a target with a melee weapon attack or a ranged weapon attack using a thrown weapon, you can imbue the attack with an additional effect depending on the benefit you chose:":
        "Ви увібрали первісну магію, що дарує вам відгомін могутності велетнів. Обравши цю рису, виберіть одну з наведених нижче переваг. Раз за хід, влучивши в ціль атакою зброєю ближнього бою або атакою дальнього бою метальною зброєю, ви можете додати до атаки ефект, що залежить від вибраної переваги:",
    "You can use this feat a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.":
        "Цю рису можна використати стільки разів, скільки становить ваш бонус спеціалізації; усі витрачені використання відновлюються після довгого відпочинку.",
    "The target takes an extra 1d4 thunder damage. You become invisible to it until the start of your next turn or until immediately after you make an attack roll or cast a spell.":
        "Ціль зазнає додатково 1d4 громової шкоди. Ви стаєте невидимими для неї до початку свого наступного ходу або доки не виконаєте кидок атаки чи не прокажете закляття.",
    "The target takes an extra 1d10 fire damage.":
        "Ціль зазнає додатково 1d10 вогняної шкоди.",
    "The target takes an extra 1d6 cold damage. If the target is a creature, it must succeed on a Constitution saving throw, or its speed is reduced to 0 until the start of your next turn.":
        "Ціль зазнає додатково 1d6 холодової шкоди. Якщо ціль — істота, вона повинна успішно виконати кидок протидії статурою, інакше її швидкість дорівнюватиме 0 до початку вашого наступного ходу.",
    "The target takes an extra 1d6 force damage. If the target is a creature, it must succeed on a Strength saving throw or have the prone condition.":
        "Ціль зазнає додатково 1d6 силової шкоди. Якщо ціль — істота, вона повинна успішно виконати кидок протидії силою, інакше набуде стану повалення.",
    "The target takes an extra 1d6 force damage. If the target is a creature, it must succeed on a Strength saving throw or be pushed 10 feet from you in a straight line.":
        "Ціль зазнає додатково 1d6 силової шкоди. Якщо ціль — істота, вона повинна успішно виконати кидок протидії силою, інакше її відштовхне від вас на 10 футів по прямій.",
    "The target takes an extra 1d6 lightning damage. If the target is a creature, it must succeed on a Constitution saving throw, or it has disadvantage on attack rolls until the start of your next turn.":
        "Ціль зазнає додатково 1d6 блискавкової шкоди. Якщо ціль — істота, вона повинна успішно виконати кидок протидії статурою, інакше матиме заваду для кидків атаки до початку вашого наступного ходу.",
    "When you use this action, you are not subject to the <LSTag Type=\"Status\" Tooltip=\"ONE_SPELL_WITH_A_SPELL_SLOT_PER_TURN\">One Spell with a Spell Slot per Turn</LSTag> restriction.":
        "Коли ви використовуєте цю дію, на вас не поширюється обмеження <LSTag Type=\"Status\" Tooltip=\"ONE_SPELL_WITH_A_SPELL_SLOT_PER_TURN\">«Одне закляття з чарункою за хід»</LSTag>.",
    "You can cast more than one spell that uses a spell slot on your turn. Once you use this benefit, you can’t do so again until you finish a Long Rest.":
        "У свій хід ви можете проказати більше одного закляття, що витрачає чарунку. Після використання цієї переваги ви не зможете скористатися нею знову до завершення довгого відпочинку.",
    "You create a momentary circle of spectral blades that sweep around you. All other creatures within 5 feet of you must succeed on a Dexterity saving throw or take [1].":
        "Ви на мить створюєте коло примарних клинків, що проносяться навколо вас. Усі інші істоти в межах 5 футів повинні успішно виконати кидок протидії спритністю, інакше зазнають [1].",
    "You can expend one use of your Bardic Inspiration to encourage allies within 30 feet of yourself. An encouraged ally gains a +5 bonus to its next Initiative roll.":
        "Ви можете витратити одне використання Бардівського натхнення, щоб підбадьорити союзників у межах 30 футів. Підбадьорений союзник отримує бонус +5 до свого наступного кидка ініціативи.",
    "Each creature in a [1] Emanation originating from you must succeed on a Constitution saving throw or take Thunder damage.":
        "Кожна істота в еманації радіусом [1], що виходить від вас, повинна успішно виконати кидок протидії статурою, інакше зазнає громової шкоди.",
    "You unleash a wave of swirling shadows that fills an area next to you. Each creature in a 10-foot Cube of Darkness originating from you when you cast the spell makes a Wisdom saving throw. On a failed save, a creature takes 2d8 psychic damage and is Blinded until the start of your next turn. On a successful save, it takes half as much damage and isn’t Blinded.":
        "Ви вивільняєте хвилю вихрових тіней, що заповнює зону поруч із вами. Кожна істота в 10-футовому кубі темряви, що виникає від вас під час проказування закляття, виконує кидок протидії мудрістю. У разі невдачі істота зазнає 2d8 психічної шкоди й сліпне до початку вашого наступного ходу. У разі успіху вона зазнає вдвічі менше шкоди й не сліпне.",
    "As a Magic action, you can give yourself a number of Temporary Hit Points equal to 1d8 plus your Wisdom modifier (minimum of 1).":
        "Магічною дією ви можете отримати тимчасові очки здоров’я в кількості 1d8 + ваш модифікатор мудрості (щонайменше 1).",
    "As an action, you present your holy symbol, and a sphere of twilight emanates from you. The sphere is centered on you, has a 30-foot radius, and is filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature ends its turn in the sphere, it gains temporary hit points equal to 1d6 plus your Cleric level and ends one effect causing it to be charmed or frightened.":
        "Дією ви здіймаєте священний символ, і від вас поширюється сфера присмерку радіусом 30 футів, наповнена тьмяним світлом. Вона рухається разом із вами й існує 1 хвилину, доки ви не станете недієздатними або не помрете. Щоразу, коли істота завершує хід у сфері, вона отримує тимчасові очки здоров’я в кількості 1d6 + ваш рівень клірика й припиняє один ефект, через який вона зачарована або налякана.",
    "You can regain all expended Focus Points. When you do so, roll your Martial Arts die, and regain a number of Hit Points equal to your Monk level plus the number rolled.":
        "Ви можете відновити всі витрачені очки зосередження. Після цього киньте кістку бойових мистецтв і відновіть очки здоров’я в кількості, що дорівнює вашому рівню монаха + результат кидка.",
    "As a Bonus Action, you can make one attack with a weapon or an Unarmed Strike.":
        "Вторинною дією ви можете виконати одну атаку зброєю або один Удар голіруч.",
    """A divine entity helps ensure you can continue the fight. You have a pool of four d12s that you can spend to heal yourself. As a Bonus Action, you can expend dice from the pool, roll them, and regain a number of Hit Points equal to the roll’s total.

Your pool regains all expended dice when you finish a Long Rest.

The pool’s maximum number of dice increases by one when you reach Barbarian levels 6 (5 dice), 12 (6 dice), and 17 (7 dice).""":
        """Божественна сутність допомагає вам продовжувати бій. Ви маєте запас із чотирьох кісток d12, які можна витрачати на зцілення. Вторинною дією ви можете витратити кістки із запасу, кинути їх і відновити очки здоров’я в кількості, що дорівнює сумі результатів.

Усі витрачені кістки запасу відновлюються після довгого відпочинку.

Максимальна кількість кісток у запасі зростає на одну на 6-му (5 кісток), 12-му (6 кісток) і 17-му (7 кісток) рівнях варвара.""",
    "As a Bonus Action, you can roll your Martial Arts die. You regain a number of Hit Points equal to the number rolled plus your Wisdom modifier (minimum of 1 Hit Point regained).":
        "Вторинною дією ви можете кинути кістку бойових мистецтв і відновити очки здоров’я в кількості, що дорівнює результату кидка + ваш модифікатор мудрості (щонайменше 1 очко здоров’я).",
    "As a Bonus Action, you can expend a use of your Wild Shape to regain a number of Hit Points equal to 2d6 plus your Druid level. This healing increases by 1d6 when you reach Druid levels 5 (3d6 plus your Druid level) and 10 (4d6 plus your Druid level).":
        "Вторинною дією ви можете витратити використання Дикої подоби й відновити очки здоров’я в кількості 2d6 + ваш рівень друїда. Зцілення збільшується на 1d6 на 5-му рівні друїда (3d6 + рівень друїда) і ще раз на 10-му рівні (4d6 + рівень друїда).",
    "You can restore one use of Wild Shape by expending a spell slot (no action required).":
        "Ви можете відновити одне використання Дикої подоби, витративши чарунку заклять (дія не потрібна).",
    "Assume the shape of a giant badger that can <LSTag Type=\"Spell\" Tooltip=\"Target_Burrow_GiantBadger\">Burrow</LSTag> into the ground.":
        "Перекиньтеся на велетенського борсука, який може <LSTag Type=\"Spell\" Tooltip=\"Target_Burrow_GiantBadger\">зариватися</LSTag> в землю.",
    "While in animal shape, you can't talk or cast spells. You take on the attributes of your beast form - excluding your <LSTag Tooltip=\"Intelligence\">Intelligence</LSTag>, <LSTag Tooltip=\"Wisdom\">Wisdom</LSTag>, and <LSTag Tooltip=\"Charisma\">Charisma</LSTag> scores.":
        "У звіриній подобі ви не можете говорити й проказувати закляття. Ви переймаєте всі риси звіриної подоби, за винятком <LSTag Tooltip=\"Intelligence\">інтелекту</LSTag>, <LSTag Tooltip=\"Wisdom\">мудрості</LSTag> й <LSTag Tooltip=\"Charisma\">харизми</LSTag>.",
    "Assume the shape of a polar bear that can <LSTag Type=\"Spell\" Tooltip=\"Shout_GoadingRoar_Bear_Summon\">Goad</LSTag> enemies into attacking it.":
        "Перекиньтеся на полярного ведмедя, який може <LSTag Type=\"Spell\" Tooltip=\"Shout_GoadingRoar_Bear_Summon\">дратувати</LSTag> ворогів, примушуючи їх атакувати себе.",
    "Take the shape of a cat that can avoid attention and <LSTag Type=\"Spell\" Tooltip=\"Shout_Distract_Cat_Summon\">Meow</LSTag> to distract enemies.":
        "Перекиньтеся на кота, який здатен бути непомітним і <LSTag Type=\"Spell\" Tooltip=\"Shout_Distract_Cat_Summon\">нявчати</LSTag>, щоб відвертати увагу ворогів.",
    "Assume the shape of a deep rothé that casts <LSTag Type=\"Spell\" Tooltip=\"Target_DancingLights\">Dancing Lights</LSTag> and <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_DeepRothe\">Charges</LSTag> its enemies.":
        "Перекиньтеся на глибинного ротея, який може проказувати <LSTag Type=\"Spell\" Tooltip=\"Target_DancingLights\">Танок вогників</LSTag> і робити <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_DeepRothe\">ривок</LSTag> у ворогів.",
    "You can cast Circle of the Moon Spells while you’re in Wild Shape.":
        "Перебуваючи в Дикій подобі, ви можете проказувати закляття Кола Місяця.",
    "Take the shape of a dire raven that can avoid attention and <LSTag Type=\"Spell\" Tooltip=\"Target_RendVision_Raven_Summon\">Blind</LSTag> enemies.":
        "Перекиньтеся на лютоворона, який може лишатися непомітним й <LSTag Type=\"Spell\" Tooltip=\"Target_RendVision_Raven_Summon\">осліплювати</LSTag> ворогів.",
    "Assume the shape of a giant spider that can <LSTag Type=\"Spell\" Tooltip=\"Target_Web_Spider\">Enweb</LSTag> enemies.":
        "Перекиньтеся на велетенського павука, який може <LSTag Type=\"Spell\" Tooltip=\"Target_Web_Spider\">обліплювати</LSTag> ворогів павутинням.",
    "Assume the shape of a dire wolf that can <LSTag Type=\"Spell\" Tooltip=\"Shout_PackHowl_Wolf_Dire\">Incite</LSTag> allies and <LSTag Type=\"Spell\" Tooltip=\"Target_Bite_Wolf_Dire_Wildshape\">Distract</LSTag> enemies.":
        "Перекиньтеся на лютововка, який може <LSTag Type=\"Spell\" Tooltip=\"Shout_PackHowl_Wolf_Dire\">надихати</LSTag> союзників і <LSTag Type=\"Spell\" Tooltip=\"Target_Bite_Wolf_Dire_Wildshape\">відвертати увагу</LSTag> ворогів.",
    "A constellation of a wise dragon appears on you. When you make a <LSTag Tooltip=\"SavingThrow\">Saving Throw</LSTag> to maintain <LSTag Tooltip=\"Concentration\">Concentration</LSTag> on a spell, a roll result of 9 or lower is considered a 10.":
        "На вас проступає сузір’я мудрого дракона. Коли ви виконуєте <LSTag Tooltip=\"SavingThrow\">кидок протидії</LSTag> для підтримання <LSTag Tooltip=\"Concentration\">концентрації</LSTag> на заклятті, результат 9 або менше вважається 10.",
    "Burning radiance erupts from you in a [1] Emanation. Each creature of your choice that you can see in it must succeed on a Constitution saving throw or take Radiant damage.":
        "Від вас у еманації радіусом [1] виривається пекуче сяйво. Кожна вибрана вами видима істота в еманації повинна успішно виконати кидок протидії статурою, інакше зазнає променевої шкоди.",
    "As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that takes the form of ocean spray that surrounds you. It ends early if you dismiss it (no action required), manifest it again, or have the Incapacitated condition.":
        "Вторинною дією ви можете витратити використання Дикої подоби, щоб створити навколо себе 5-футову еманацію океанських бризок. Вона достроково зникає, якщо ви її припините (дія не потрібна), створите знову або набудете стану недієздатності.",
    """You draw power from the strange and ancient horrors of the land, causing you to sprout unnatural growths, such as bloody antlers or putrid fangs, or causing your shadow to lengthen or twist around you. As a Bonus Action, you can expend a use of Favored Enemy to transform into a ghastly form, gaining the following benefits for 1 minute or until you have the Incapacitated condition, die, or end the transformation (no action required).

Ancient Armor. You gain a +1 bonus to AC, as your body is wreathed in rotten bark and beastly bristles. This bonus increases to +2 when you reach Ranger level 11.

Prowling Retribution. Immediately after a creature you can see within 5 feet of yourself deals damage to you or one of your allies, you can make an Opportunity Attack against that creature.

Unnerving Aura. When you transform and at the start of each of your subsequent turns, each creature of your choice in a 10-foot Emanation originating from you makes a Wisdom saving throw against your spell save DC. On a failed save, a creature has the Frightened condition until the start of your next turn.""":
        """Ви черпаєте силу з дивних прадавніх жахів краю: на вас проростають неприродні нарости — криваві роги або гнилі ікла, — а ваша тінь видовжується чи звивається довкола. Вторинною дією ви можете витратити використання Знання ворога й набути жаскої подоби. Вона триває 1 хвилину, доки ви не станете недієздатними, не помрете або не припините перетворення (дія не потрібна), і надає такі переваги:

Прадавній панцир. Ваше тіло огортають гнила кора та звіряча щетина, надаючи бонус +1 до РЗ. На 11-му рівні слідопита бонус зростає до +2.

Підкрадлива відплата. Одразу після того, як видима вам істота в межах 5 футів завдає шкоди вам або вашому союзнику, ви можете виконати принагідну атаку проти неї.

Тривожна аура. Коли ви перетворюєтеся та на початку кожного наступного свого ходу, кожна вибрана вами істота в 10-футовій еманації від вас виконує кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі істота перебуває в стані переляку до початку вашого наступного ходу.""",
    "Once per Short Rest, as a Bonus Action, you unleash a battle cry infused with divine energy; creatures of your choice within 60 feet of you gain Advantage on attack rolls and saving throws until the start of your next turn.":
        "Раз за короткий відпочинок ви можете вторинною дією видати бойовий клич, сповнений божественної енергії. Вибрані вами істоти в межах 60 футів отримують перевагу для кидків атаки й протидії до початку вашого наступного ходу.",
    "As a Magic action, you can expend one use of this class’s Channel Oath to overwhelm foes with awe. As you present your Holy Symbol or weapon, you can target a number of creatures equal to your Charisma modifier (minimum of one creature) that you can see within [1] of yourself. Each target must succeed on a Wisdom saving throw or have the Frightened condition for 1 minute.":
        "Магічною дією ви можете витратити одне використання Обітного наснаження цього класу, щоб приголомшити ворогів благоговінням. Здійнявши священний символ або зброю, виберіть видимих вам істот у межах [1] у кількості, що дорівнює вашому модифікатору харизми (щонайменше одну). Кожна ціль повинна успішно виконати кидок протидії мудрістю, інакше перебуватиме в стані переляку протягом 1 хвилини.",
    "When you expend a use of your Bardic Inspiration as part of an action, a Bonus Action, or a Reaction, you can make one Unarmed Strike as part of that action, Bonus Action, or Reaction.":
        "Коли ви витрачаєте використання Бардівського натхнення як частину дії, вторинної дії або реагування, можете в межах тієї самої дії виконати один Удар голіруч.",
    "Increase your allies' hit point maximum by [1].":
        "Збільште максимум очок здоров’я союзників на [1].",
    "You can use your Channel Divinity to twist a creature’s fate. As a Bonus Action, you can expend one use of your Channel Divinity to choose a creature you can see within 120 feet of yourself. That creature has Disadvantage on the next saving throw it makes against your spells before the end of your next turn.":
        "Ви можете скористатися Божим наснаженням, щоб перекрутити долю істоти. Вторинною дією витратьте одне використання Божого наснаження й виберіть видиму вам істоту в межах 120 футів. До кінця вашого наступного ходу ця істота має заваду для наступного кидка протидії одному з ваших заклять.",
    "You project a line of web at a point you can see within 30 feet, pulling yourself to that point in a straight line without provoking Opportunity Attacks.":
        "Ви випускаєте павутину в видиму точку в межах 30 футів і притягуєте себе до неї по прямій, не провокуючи принагідних атак.",
    "Choose one creature or object you can see within 30 feet of the target. Healing energy flows into the chosen recipient, restoring 2d6 Hit Points to it.":
        "Виберіть видиму істоту або предмет у межах 30 футів від цілі. Цілюща енергія вливається у вибраного одержувача й відновлює йому 2d6 очок здоров’я.",
    "Heal yourself or a nearby ally. ":
        "Зціліть себе або союзника поблизу.",
    "You attempt to bring a dim-witted creature to heel. A creature with an <LSTag Tooltip=\"Intelligence\">Intelligence</LSTag> of 3 or lower must succeed on an <LSTag Tooltip=\"Intelligence\">Intelligence</LSTag> <LSTag Tooltip=\"SavingThrow\">Saving Throw</LSTag> or become <LSTag Type=\"Status\" Tooltip=\"AWAKEN\">Dominated</LSTag> by you until you finish a <LSTag Tooltip=\"LongRest\">Long Rest</LSTag>.":
        "Ви намагаєтеся підкорити нерозумну істоту. Істота з показником <LSTag Tooltip=\"Intelligence\">інтелекту</LSTag> 3 або менше повинна успішно виконати <LSTag Tooltip=\"Intelligence\">інтелектуальний</LSTag> <LSTag Tooltip=\"SavingThrow\">кидок протидії</LSTag>, інакше стане <LSTag Type=\"Status\" Tooltip=\"AWAKEN\">підкореною</LSTag> вами до завершення <LSTag Tooltip=\"LongRest\">довгого відпочинку</LSTag>.",
    "As a bonus action, you can choose one creature you can see within 60 feet of you and spend a number of those dice equal to half your druid level or less. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent.":
        "Вторинною дією ви можете вибрати видиму істоту в межах 60 футів і витратити кількість цих кісток, що не перевищує половини вашого рівня друїда. Киньте витрачені кістки й додайте результати. Ціль відновлює стільки очок здоров’я, скільки випало загалом, а також отримує 1 тимчасове очко здоров’я за кожну витрачену кістку.",
    "Protect a creature from attacks: increase its <LSTag Tooltip=\"ArmourClass\">Armour Class</LSTag> up to 17.":
        "Захистіть істоту від атак: підвищте її <LSTag Tooltip=\"ArmourClass\">рівень захисту</LSTag> до 17.",
    """You can tap into the grand equation of existence to imbue a creature with a shimmering shield of order. As a Magic action, you can expend 1 to 5 Sorcery Points to create a magical ward around yourself or another creature you can see within 30 feet of yourself. The ward is represented by a number of d8s equal to the number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice.

The ward lasts until you finish a Long Rest or until you use this feature again.""":
        """Ви можете звернутися до великого рівняння буття й огорнути істоту мерехтливим щитом порядку. Магічною дією витратьте від 1 до 5 очок чародійства, щоб створити магічний оберіг навколо себе або іншої видимої істоти в межах 30 футів. Оберіг має стільки кісток d8, скільки очок чародійства витрачено на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.

Оберіг діє до завершення вашого довгого відпочинку або доки ви не скористаєтеся цією особливістю знову.""",
    "You can touch one nonmagical object that is a suit of armor or a simple or martial weapon. Until the end of your next long rest or until you die, the object becomes a magic item, granting a +1 bonus to AC if it’s armor or a +1 bonus to attack and damage rolls if it’s a weapon.":
        "Ви можете торкнутися одного немагічного предмета: комплекту обладунків або простої чи бойової зброї. До завершення вашого наступного довгого відпочинку або до вашої смерті предмет стає магічним і надає бонус +1 до РЗ, якщо це обладунки, або бонус +1 до кидків атаки й шкоди, якщо це зброя.",
    "While you cast Moonbeam, a creature of your choice that you can see within 60 feet of yourself regains 2d4 Hit Points.":
        "Коли ви проказуєте «Місячний промінь», вибрана вами видима істота в межах 60 футів відновлює 2d4 очок здоров’я.",
    "Choose a Humanoid of your size that you can see in range. You physically transform to become an exact duplicate of that creature for the duration. Even a thorough physical examination fails to find any differences between you and the target.":
        "Виберіть видимого гуманоїда вашого розміру в межах досяжності. На час дії ви фізично перетворюєтеся на точну копію цієї істоти. Навіть ретельний огляд не виявляє жодних відмінностей між вами й ціллю.",
    "While your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is active, you can use your Reaction to lash out with spectral branches of the World Tree and pull a creature you can see within 30 feet of you. The target must succeed on a Strength saving throw (DC 8 + your Strength modifier + your Proficiency Bonus) or be pulled up to 20 feet straight toward you. After pulling the target, you can reduce its Speed to 0 until the start of your next turn.":
        "Поки триває ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, ви можете реагуванням простягнути примарні гілки Світового Дерева й потягнути видиму істоту в межах 30 футів. Ціль повинна успішно виконати кидок протидії силою (МС 8 + ваш модифікатор сили + бонус спеціалізації), інакше її притягне до вас по прямій на відстань до 20 футів. Після притягування ви можете зменшити її швидкість до 0 до початку свого наступного ходу.",
    """You burn all seals you have placed on the creature, dealing 1d6 fire or necrotic damage (your choice) to it per seal burned. Once a seal is burned, it immediately vanishes.

Once you reach 5th level in this class, your connection to your archdevil strengthens. Each burned seal deals an extra 1d6 damage, for a total of 2d6 per seal. The damage per seal increases by an additional 1d6 when you reach 10th level (for a total of 3d6 per seal).""":
        """Ви спалюєте всі накладені на істоту печатки. За кожну спалену печатку вона зазнає 1d6 вогняної або некротичної шкоди на ваш вибір. Спалена печатка негайно зникає.

На 5-му рівні цього класу ваш зв’язок з архідияволом зміцнюється, і кожна спалена печатка завдає додатково 1d6 шкоди — загалом 2d6 за печатку. На 10-му рівні шкода від кожної печатки зростає ще на 1d6 — загалом до 3d6.""",
    "When you hit a creature with your sanctified blade, you can expend 1 Divine Point to bind it in holy chains. The target must succeed on a Strength saving throw or take Radiant damage equal to your Wisdom modifier and gain the Restrained condition until the end of your next turn.":
        "Коли ви влучаєте в істоту Освяченим клинком, можете витратити 1 божественне очко й скувати її святими ланцюгами. Ціль повинна успішно виконати кидок протидії силою, інакше зазнає променевої шкоди в кількості, що дорівнює вашому модифікатору мудрості, і набуде стану знерухомлення до кінця вашого наступного ходу.",
    """You conjure spinning daggers in a 5-foot-radius, 40-foot-high Cylinder centered on a point within range. Each creature in that area takes Slashing damage. A creature also takes this damage if it ends its turn there or if the Cylinder moves into its space. A creature takes this damage only once per turn.

On your later turns, you can take a Magic action to move the Cylinder up to 30 feet.""":
        """Ви прикликаєте вихор кинджалів у циліндрі радіусом 5 футів і заввишки 40 футів із центром у вибраній точці в межах досяжності. Кожна істота в цій зоні зазнає рубаної шкоди. Істота також зазнає цієї шкоди, якщо завершує там свій хід або якщо циліндр переміщується в її простір, але не більше одного разу за хід.

У наступні ходи ви можете магічною дією перемістити циліндр на відстань до 30 футів.""",
    "Take a Magic action to teleport the daggers up to 30 feet.":
        "Магічною дією телепортуйте кинджали на відстань до 30 футів.",
    "As a Bonus Action, you magically teleport up to 30 feet to an unoccupied space you can see.":
        "Вторинною дією ви магічно телепортуєтеся на відстань до 30 футів у видимий вільний простір.",
    "Choose a willing ally who can see or hear you, and an enemy for that ally to attack, then expend one Superiority Die. Your ally can immediately use its Reaction to make one attack with a weapon against the chosen enemy, adding the Superiority Die to the attack’s damage roll on a hit.":
        "Виберіть згодного союзника, який бачить або чує вас, і ворога, якого він має атакувати, а потім витратьте одну кістку переваги. Союзник може негайно реагуванням виконати одну атаку зброєю проти вибраного ворога й у разі влучання додати кістку переваги до кидка шкоди.",
    "You can expend a seal as a bonus action to teleport up to an unoccupied space you can see.":
        "Вторинною дією ви можете витратити печатку, щоб телепортуватися у видимий вільний простір.",
    """You conjure spirits from the Elemental Planes that flit around you in a 15-foot Emanation for the duration. Until the spell ends, any attack you make deals an extra [1] damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack).

In addition, the ground in the Emanation is Difficult Terrain for your enemies.""":
        """На час дії ви прикликаєте духів зі Стихійних Планів, які пурхають навколо вас у 15-футовій еманації. До завершення закляття кожна ваша атака, що влучає в істоту в еманації, завдає додатково [1] кислотної, холодової, вогняної або блискавкової шкоди на ваш вибір під час атаки.

Крім того, поверхня в еманації є важкопрохідною місцевістю для ваших ворогів.""",
    """You conjure nature spirits that flit around you in a 10-foot Emanation for the duration. Whenever the Emanation enters the space of a creature you can see and whenever a creature you can see enters the Emanation or ends its turn there, you can force that creature to make a Wisdom saving throw. The creature takes Force damage on a failed save or half as much damage on a successful one. A creature makes this save only once per turn.

In addition, you can take the Disengage action as a Bonus Action for the spell’s duration.""":
        """На час дії ви прикликаєте духів природи, які пурхають навколо вас у 10-футовій еманації. Коли еманація вперше за хід входить у простір видимої істоти або коли видима істота входить до еманації чи завершує там хід, ви можете змусити її виконати кидок протидії мудрістю. У разі невдачі істота зазнає силової шкоди, а в разі успіху — вдвічі менше. Кожна істота виконує цей кидок не більше одного разу за хід.

Крім того, на час дії закляття ви можете виконувати Відступ вторинною дією.""",
    "You can take a Bonus Action to magically create icy terrain on up to five spaces. The ice-covered spaces become Difficult Terrain and remain until the end of your next turn. When you take this Bonus Action, you may spend one or more Sorcery Points to freeze an additional five spaces for each Sorcery Point spent.":
        "Вторинною дією ви можете магічно вкрити льодом до п’яти ділянок. Вони стають важкопрохідною місцевістю до кінця вашого наступного ходу. Виконуючи цю вторинну дію, ви можете витратити одне або більше очок чародійства, щоб за кожне витрачене очко заморозити ще п’ять ділянок.",
    "As a Bonus Action, you can expend a use of your Channel Divinity to open a planar tear at a point you can see within 60 feet of you, creating a powerful vacuum in a 15-foot-radius Sphere centered on that point. Each creature in the area must make a Dexterity saving throw. On a failed save, a creature takes Force damage equal to 1d8 plus your Cleric level and is pulled up to 15 feet toward the point. On a successful save, a creature takes half as much Force damage only. The tear then vanishes.":
        "Вторинною дією ви можете витратити використання Божого наснаження й відкрити планарний розрив у видимій точці в межах 60 футів. У сфері радіусом 15 футів із центром у цій точці виникає потужний вакуум. Кожна істота в зоні виконує кидок протидії спритністю. У разі невдачі істота зазнає силової шкоди в кількості 1d8 + ваш рівень клірика й притягується до точки на відстань до 15 футів; у разі успіху вона зазнає лише половини шкоди. Після цього розрив зникає.",
    "Teleport to an unoccupied, obscured spot. Before or after teleporting, you can make one attack.":
        "Телепортуйтеся у вільне затінене місце. До або після телепортації ви можете виконати одну атаку.",
    """The light of dawn shines down on a location you specify within range. Until the spell ends, a 30-foot-radius, 40-foot-high cylinder of bright light glimmers there. This light is sunlight.

When the cylinder appears, each creature in it must make a Constitution saving throw, taking 4d10 radiant damage on a failed save, or half as much damage on a successful one. A creature must also make this saving throw whenever it ends its turn in the cylinder.

If you’re within 60 feet of the cylinder, you can move it up to 60 feet as a bonus action on your turn.""":
        """Світло світанку осяває вибрану вами точку в межах досяжності. До завершення закляття там мерехтить циліндр яскравого світла радіусом 30 футів і заввишки 40 футів. Це світло вважається сонячним.

Коли циліндр з’являється, кожна істота в ньому повинна виконати кидок протидії статурою. У разі невдачі вона зазнає 4d10 променевої шкоди, а в разі успіху — вдвічі менше. Істота також виконує цей кидок щоразу, коли завершує свій хід у циліндрі.

Якщо ви перебуваєте в межах 60 футів від циліндра, у свій хід можете вторинною дією перемістити його на відстань до 60 футів.""",
    "Move the cylinder of dawnlight up to [1]. Creatures caught in the light where it reappears, and creatures that end their turn within it, are seared by sunlight.":
        "Перемістіть циліндр світла «Світанку» на відстань до [1]. Істот у місці його появи, а також тих, що завершують у ньому хід, обпалює сонячне світло.",
    "For the duration, an inky aura surrounds one creature you touch. The target has Advantage on Death Saving Throws, and once per turn, when a creature within 5 feet of the target hits it with a melee attack roll, the attacker takes 2d4 Necrotic damage.":
        "На час дії істоту, якої ви торкаєтеся, оточує чорнильна аура. Ціль має перевагу для кидків протидії смерті. Раз за хід, коли істота в межах 5 футів від цілі влучає в неї атакою ближнього бою, нападник зазнає 2d4 некротичної шкоди.",
    "As an action, you invoke the authority of Dispater. You make a weapon attack and choose a number of willing creatures up to your proficiency bonus who you can see within 30 feet of you. Each creature you choose can use a reaction to make a weapon attack or cast a damage-dealing cantrip with a casting time of 1 action.":
        "Дією ви звертаєтеся до влади Диспатера. Виконайте атаку зброєю й виберіть видимих згодних істот у межах 30 футів у кількості, що не перевищує ваш бонус спеціалізації. Кожна вибрана істота може реагуванням виконати атаку зброєю або проказати замовляння, яке завдає шкоди й має час проказування 1 дія.",
    "You have the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition until the start of your next turn or until immediately after you make an attack roll, deal damage, or cast a spell.":
        "Ви перебуваєте в стані <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимість</LSTag> до початку свого наступного ходу або доки не виконаєте кидок атаки, не завдасте шкоди чи не прокажете закляття.",
    "One creature of your choice that you can see within range hears a discordant melody in its mind. The target makes a Wisdom saving throw. On a failed save, it takes Psychic damage and use its next turn to move as far away from you as it can. On a successful save, the target takes half as much damage only.":
        "Вибрана вами видима істота в межах досяжності чує у своїй свідомості дисонансну мелодію й виконує кидок протидії мудрістю. У разі невдачі вона зазнає психічної шкоди й у свій наступний хід відходить від вас якомога далі. У разі успіху ціль зазнає лише половини шкоди.",
    "As a Magic action, you point your Holy Symbol at another creature you can see within [1] of yourself and focus divine energy at it. You either restore Hit Points to the creature or force the creature to make a Constitution saving throw. On a failed save, the creature takes Necrotic or Radiant damage (your choice). On a successful save, the creature takes half as much damage (round down).":
        "Магічною дією спрямуйте священний символ на іншу видиму істоту в межах [1] і зосередьте на ній божественну енергію. Ви або відновлюєте істоті очки здоров’я, або змушуєте її виконати кидок протидії статурою. У разі невдачі вона зазнає некротичної або променевої шкоди на ваш вибір, а в разі успіху — вдвічі менше з округленням донизу.",
    "You restore Hit Points to a creature.":
        "Ви відновлюєте істоті очки здоров’я.",
    "You deal damage to a creature.":
        "Ви завдаєте істоті шкоди.",
    "You teleport to an unoccupied space you can see within 30 feet of yourself and take on a semi-incorporeal form, which lasts until the end of your next turn. While in this form, you have Resistance to Bludgeoning, Piercing, and Slashing damage, and you have Immunity to the Prone, and Restrained conditions.":
        "Ви телепортуєтеся у видимий вільний простір у межах 30 футів і набуваєте напівбезтілесної подоби до кінця свого наступного ходу. У цій подобі ви маєте стійкість до дробильної, колотої та рубаної шкоди й імунітет до станів повалення та знерухомлення.",
    "You can use your Channel Divinity to hasten a creature’s doom. As a Bonus Action, you can expend one use your Channel Divinity to choose a creature you can see within 120 feet of yourself. For 10 minutes, attack rolls against the creature can score a Critical Hit on a roll of 19 or 20 on the d20.":
        "Ви можете скористатися Божим наснаженням, щоб наблизити загибель істоти. Вторинною дією витратьте одне використання Божого наснаження й виберіть видиму істоту в межах 120 футів. Протягом 10 хвилин кидки атаки проти неї завдають критичного удару, якщо на d20 випало 19 або 20.",
    "When you reach character level 5, you can channel draconic magic to give yourself temporary flight. As a Bonus Action, you sprout spectral wings on your back that last for 10 minutes or until you retract the wings (no action required) or have the Incapacitated condition. During that time, you have a Fly Speed equal to your Speed. Your wings appear to be made of the same energy as your Breath Weapon. Once you use this trait, you can’t use it again until you finish a Long Rest.":
        "На 5-му рівні персонажа ви навчаєтеся спрямовувати драконічну магію для тимчасового польоту. Вторинною дією виростіть за спиною примарні крила на 10 хвилин — доки не сховаєте їх (дія не потрібна) або не набудете стану недієздатності. Ваша швидкість польоту дорівнює звичайній швидкості, а крила здаються створеними з тієї самої енергії, що й ваша Дихальна зброя. Після використання цієї риси ви не зможете скористатися нею знову до завершення довгого відпочинку.",
    "You touch one willing creature, and choose Acid, Cold, Fire, Lightning, or Poison. Until the spell ends, the target can take a Magic action to exhale a 15-foot Cone. Each creature in that area makes a Dexterity saving throw, taking damage of the chosen type on a failed save or half as much damage on a successful one.":
        "Торкніться однієї згодної істоти й виберіть кислотну, холодову, вогняну, блискавкову або отруйну шкоду. До завершення закляття ціль може магічною дією видихнути 15-футовий конус. Кожна істота в зоні виконує кидок протидії спритністю. У разі невдачі вона зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.",
    "You can take a Magic action to instill terror in a creature you can see within 30 feet of yourself. The target must succeed on a Wisdom saving throw or have the Frightened condition until the end of your next turn.":
        "Магічною дією ви можете вселити жах у видиму істоту в межах 30 футів. Ціль повинна успішно виконати кидок протидії мудрістю, інакше перебуватиме в стані переляку до кінця вашого наступного ходу.",
    "On a failed Wisdom saving throw, the target is trapped in a dream, gaining no benefit from its rest. When the target wakes up, it takes 3d6 Psychic damage.":
        "У разі невдалого кидка протидії мудрістю ціль опиняється в пастці сновидіння й не отримує користі від відпочинку. Прокинувшись, вона зазнає 3d6 психічної шкоди.",
    "Expend an action to channel your magic through your duplicate. On its turn, it can cast one of your cantrips, using your spell save DC and spell attack bonus — letting you cast as though you were in the illusion's space.":
        "Витратьте дію, щоб спрямувати магію крізь свого двійника. У свій хід він може проказати одне з ваших замовлянь, використовуючи вашу МС протидії закляттям і бонус до атаки закляттям, наче ви перебуваєте в просторі ілюзії.",
    "Expend an action and a spell slot to channel your magic through your duplicate. On its turn, it can cast one of your prepared spells with that slot, using your spell save DC and spell attack bonus — letting you cast as though you were in the illusion's space.":
        "Витратьте дію й чарунку заклять, щоб спрямувати магію крізь свого двійника. У свій хід він може проказати одне з ваших підготовлених заклять за допомогою цієї чарунки, використовуючи вашу МС протидії закляттям і бонус до атаки закляттям, наче ви перебуваєте в просторі ілюзії.",
    "As a Magic action, you can expend 2 Focus Points to cause elemental energy to burst in a [1] radius Sphere centered on a point within [2] of yourself. Choose a damage type: Acid, Cold, Fire, Lightning, or Thunder.\n\nEach creature in the Sphere must make a Dexterity saving throw. On a failed save, a creature takes damage of the chosen type equal to three rolls of your Martial Arts die. On a successful save, a creature takes half as much damage.":
        "Магічною дією ви можете витратити 2 очки зосередження й вивільнити стихійну енергію у сфері радіусом [1] із центром у точці в межах [2] від вас. Виберіть тип шкоди: кислотна, холодова, вогняна, блискавкова або громова.\n\nКожна істота у сфері виконує кидок протидії спритністю. У разі невдачі вона зазнає шкоди вибраного типу в кількості, що дорівнює трьом кидкам вашої кістки бойових мистецтв, а в разі успіху — вдвічі менше.",
    "As a bonus action, you restore a total number of hit points equal to five times your illrigger level, divided however you choose between yourself and other creatures within 30 feet of you.":
        "Вторинною дією ви відновлюєте загальну кількість очок здоров’я, що дорівнює п’ятикратному рівню вашого ілриґера, довільно розподіляючи їх між собою та іншими істотами в межах 30 футів.",
    "As a Bonus Action, you bolster one ally you can see within 30 feet. That ally gains Temporary Hit Points equal to 2d6 plus your Proficiency Bonus. You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.":
        "Вторинною дією ви можете підтримати одного видимого союзника в межах 30 футів. Він отримує тимчасові очки здоров’я в кількості 2d6 + ваш бонус спеціалізації. Цю вторинну дію можна використати стільки разів, скільки становить ваш бонус спеціалізації; усі витрачені використання відновлюються після довгого відпочинку.",
    "As you finish a Short or Long Rest, you can play a song on a Musical Instrument with which you have proficiency and give <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Heroic Inspiration</LSTag> to allies who hear the song. The number of allies you can affect in this way equals your Proficiency Bonus.":
        "Завершуючи короткий або довгий відпочинок, ви можете зіграти пісню на музичному інструменті, яким володієте, і надати <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Героїчне натхнення</LSTag> союзникам, які її чують. У такий спосіб можна вплинути на стількох союзників, скільки становить ваш бонус спеціалізації.",
    """A tendril of inky darkness reaches out from you, touching a creature you can see within range to drain life from it. The target must make a Dexterity saving throw. On a successful save, the target takes [1] necrotic damage, and the spell ends. On a failed save, the target takes [2] necrotic damage, and until the spell ends, you can use your action on each of your turns to automatically deal 4d8 necrotic damage to the target. The spell ends if you use your action to do anything else, if the target is ever outside the spell’s range, or if the target has total cover from you.

Whenever the spell deals damage to a target, you regain hit points equal to half the amount of necrotic damage the target takes.""":
        """Пасмо чорнильної темряви простягається від вас до видимої істоти в межах досяжності й висмоктує з неї життя. Ціль повинна виконати кидок протидії спритністю. У разі успіху вона зазнає [1] некротичної шкоди, а закляття завершується. У разі невдачі ціль зазнає [2] некротичної шкоди, і до завершення закляття ви можете дією в кожен свій хід автоматично завдавати їй 4d8 некротичної шкоди. Закляття завершується, якщо ви витратите дію на щось інше, ціль опиниться поза межами досяжності закляття або матиме від вас повне укриття.

Щоразу, коли закляття завдає цілі шкоди, ви відновлюєте очки здоров’я в кількості, що дорівнює половині завданої їй некротичної шкоди.""",
    "You can drain enemies to embolden your allies. Whenever you burn one or more seals on a creature, you can choose an ally you can see within 30 feet of you. That ally gains Temporary Hit Points equal to the number rolled on one Seal damage die.":
        "Ви можете виснажувати ворогів, наснажуючи союзників. Щоразу, коли ви спалюєте на істоті одну або більше печаток, виберіть видимого союзника в межах 30 футів. Він отримує тимчасові очки здоров’я в кількості, що дорівнює результату кидка однієї кістки шкоди печатки.",
    "As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see.":
        "Вторинною дією ви можете магічно телепортуватися на відстань до 30 футів у видимий вільний простір.",
    "Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to the creatures.":
        "Одразу після використання Фейського кроку виберіть до двох видимих істот у межах 10 футів. Вони повинні успішно виконати кидок протидії мудрістю, інакше будуть зачаровані вами на 1 хвилину або доки ви чи ваші супутники не завдасте їм шкоди.",
    "Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your proficiency bonus.":
        "Одразу після використання Фейського кроку кожна вибрана вами видима істота в межах 5 футів зазнає вогняної шкоди в кількості, що дорівнює вашому бонусу спеціалізації.",
    "You touch a melee weapon and place a magical effect into it, creating a visible rune etched into the weapon. Attacks made by the invoked weapon deal an extra 1d8 Fire damage on a hit.":
        "Ви торкаєтеся зброї ближнього бою й вкладаєте в неї магічний ефект, викарбовуючи на ній видиму руну. У разі влучання атаки цією зброєю завдають додатково 1d8 вогняної шкоди.",
    "You touch a willing creature. For the duration, the target gains a Fly Speed of 60 feet and can hover. When the spell ends, the target falls if it is still aloft unless it can stop the fall.":
        "Ви торкаєтеся згодної істоти. На час дії ціль отримує швидкість польоту 60 футів і може зависати в повітрі. Коли закляття завершується, ціль падає, якщо досі перебуває в повітрі й не може зупинити падіння.",
    "If you hit a creature that is at least one size smaller than you with the demolisher, you can pull the creature up to 10 feet toward yourself.":
        "Якщо ви влучаєте руйнівником в істоту, щонайменше на один розмір меншу за вас, можете притягнути її до себе на відстань до 10 футів.",
    "If you hit a creature that is at least one size smaller than you with the demolisher, you can push the creature up to 10 feet straight away from yourself.":
        "Якщо ви влучаєте руйнівником в істоту, щонайменше на один розмір меншу за вас, можете відштовхнути її від себе по прямій на відстань до 10 футів.",
    "As a Magic action, choose a number of creatures you can see equal to your Wisdom modifier (minimum of one). Each chosen creature regains Hit Points equal to 1d10 plus your Ranger level and has Advantage on saving throws to avoid or end the Frightened condition for 1 hour.":
        "Магічною дією виберіть видимих істот у кількості, що дорівнює вашому модифікатору мудрості (щонайменше одну). Кожна з них відновлює очки здоров’я в кількості 1d10 + ваш рівень слідопита й протягом 1 години має перевагу для кидків протидії, щоб уникнути або припинити стан переляку.",
    "You twist your visage to scare a creature that you can see within range. The creature must succeed on a Wisdom saving throw or have the Frightened condition until the start of your next turn.":
        "Ви викривляєте риси свого обличчя, щоб налякати видиму істоту в межах досяжності. Вона повинна успішно виконати кидок протидії мудрістю, інакше перебуватиме в стані переляку до початку вашого наступного ходу.",
    "You cause numbing frost to form on one creature that you can see within range. The target must make a Constitution saving throw. On a failed save, the target takes cold damage, and it has disadvantage on the next weapon attack roll it makes before the end of its next turn.":
        "Ви вкриваєте видиму істоту в межах досяжності морозом, що сковує чуття. Ціль повинна виконати кидок протидії статурою. У разі невдачі вона зазнає холодової шкоди й має заваду для наступного кидка атаки зброєю до кінця свого наступного ходу.",
    "You can order your allies to follow your formation (no action required). Choose a number of creatures within 60 feet of you that can hear you, up to your proficiency bonus. Each target can immediately move up to its speed without provoking opportunity attacks.":
        "Ви можете наказати союзникам тримати стрій (дія не потрібна). Виберіть істот у межах 60 футів, які чують вас, у кількості, що не перевищує ваш бонус спеціалізації. Кожна ціль може негайно переміститися на відстань до своєї швидкості, не провокуючи принагідних атак.",
    "You brandish the weapon used in the spell’s casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack’s normal effects, and you can cause green fire to leap from the target to a different creature that you can see within 5 feet of it. The second creature takes [1].":
        "Ви замахуєтеся зброєю, використаною для проказування закляття, і виконуєте нею атаку ближнього бою проти істоти в межах 5 футів. У разі влучання ціль зазнає звичайних ефектів атаки зброєю, а ви можете змусити зелене полум’я перекинутися з неї на іншу видиму істоту в межах 5 футів. Друга істота зазнає [1].",
    "You choose a number of allies within a 30-foot emanation originating from you, up to a number of allies equal to your Charisma modifier. Each of those allies regains Hit Points equal to 1d10 + your Fighter level.":
        "Виберіть союзників у 30-футовій еманації від вас у кількості, що не перевищує ваш модифікатор харизми. Кожен із них відновлює очки здоров’я в кількості 1d10 + ваш рівень бійця.",
    "You can make one weapon attack on the first turn of combat without using an action.":
        "У перший хід бою ви можете виконати одну атаку зброєю, не витрачаючи дії.",
    "As a Magic action, you can expend 1 Focus Point to touch a creature and restore a number of Hit Points equal to a roll of your Martial Arts die plus your Wisdom modifier.":
        "Магічною дією ви можете витратити 1 очко зосередження, торкнутися істоти й відновити їй очки здоров’я в кількості, що дорівнює кидку вашої кістки бойових мистецтв + модифікатор мудрості.",
    "As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus. The creature regains a number of Hit Points equal to the total rolled.":
        "Магічною дією торкніться істоти й киньте стільки кісток d4, скільки становить ваш бонус спеціалізації. Істота відновлює очки здоров’я в кількості, що дорівнює сумі результатів.",
    """You gain the ability to channel celestial energy to heal wounds. You have a pool of d6s to fuel this healing. The number of dice in the pool equals 1 plus your Warlock level.

As a Bonus Action, you can heal yourself or one creature you can see within 60 feet of yourself, expending dice from the pool. The maximum number of dice you can expend at once equals your Charisma modifier (minimum of one die). Roll the dice you expend, and restore a number of Hit Points equal to the roll’s total. Your pool regains all expended dice when you finish a Long Rest.""":
        """Ви навчаєтеся спрямовувати небесну енергію для зцілення ран. Ви маєте запас кісток d6; їхня кількість дорівнює 1 + ваш рівень чаклуна.

Вторинною дією ви можете зцілити себе або одну видиму істоту в межах 60 футів, витративши кістки із запасу. За раз можна витратити не більше кісток, ніж становить ваш модифікатор харизми (щонайменше одну). Киньте витрачені кістки й відновіть очки здоров’я в кількості, що дорівнює сумі результатів. Усі витрачені кістки запасу відновлюються після довгого відпочинку.""",
    "You create an eruption of smoldering hellfire around a creature you can see within range.":
        "Ви здіймаєте спалах тліючого пекельного вогню навколо видимої істоти в межах досяжності.",
    "If the target is an interdicted creature, it makes the saving throw with Disadvantage.":
        "Якщо ціль позначена інтердиктом, вона виконує кидок протидії із завадою.",
    "You lash a whip of crimson energy at a creature you can see within range, creating a conduit between you and the target. The target must succeed on a Constitution saving throw or take 4d4 fire damage and be tethered. A tethered creature takes 2d4 fire damage at the beginning of each of their turns. A tethered creature can repeat the saving throw at the end of each of their turns, ending the effect on a success.":
        "Ви б’єте батогом багряної енергії по видимій істоті в межах досяжності й створюєте зв’язок між собою та ціллю. Ціль повинна успішно виконати кидок протидії статурою, інакше зазнає 4d4 вогняної шкоди й буде прив’язана. На початку кожного свого ходу прив’язана істота зазнає 2d4 вогняної шкоди. Наприкінці кожного свого ходу вона може повторити кидок протидії, у разі успіху припиняючи цей ефект.",
    "Deal an additional [1] when you attack the target and impart <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Charisma <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag>.":
        "Коли ви атакуєте ціль, вона зазнає додатково [1] шкоди й має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> харизми.",
    "Deal an additional [1] when you attack the target and impart <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Constitution <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag>.":
        "Коли ви атакуєте ціль, вона зазнає додатково [1] шкоди й має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> статури.",
    "Deal an additional [1] when you attack the target and impart <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Dexterity <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag>.":
        "Коли ви атакуєте ціль, вона зазнає додатково [1] шкоди й має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> спритності.",
    "Deal an additional [1] when you attack the target and impart <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Intelligence <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag>.":
        "Коли ви атакуєте ціль, вона зазнає додатково [1] шкоди й має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> інтелекту.",
    "Deal an additional [1] when you attack the target and impart <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Strength <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag>.":
        "Коли ви атакуєте ціль, вона зазнає додатково [1] шкоди й має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> сили.",
    "Deal an additional [1] when you attack the target and impart <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Wisdom <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag>.":
        "Коли ви атакуєте ціль, вона зазнає додатково [1] шкоди й має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> мудрості.",
    """You imbue a weapon you touch with holy power. Until the spell ends, the weapon emits bright light in a 30-foot radius and dim light for an additional 30 feet. In addition, weapon attacks made with it deal an extra 2d8 radiant damage on a hit. If the weapon isn’t already a magic weapon, it becomes one for the duration.

As a bonus action on your turn, you can dismiss this spell and cause the weapon to emit a burst of radiance. Each creature of your choice that you can see within 30 feet of the weapon must make a Constitution saving throw. On a failed save, a creature takes 4d8 radiant damage, and it is blinded for 1 minute. On a successful save, a creature takes half as much damage and isn’t blinded. At the end of each of its turns, a blinded creature can make a Constitution saving throw, ending the effect on itself on a success.""":
        """Ви насичуєте святою силою зброю, якої торкаєтеся. До завершення закляття вона випромінює яскраве світло в радіусі 30 футів і тьмяне світло ще на 30 футів, а атаки нею в разі влучання завдають додатково 2d8 променевої шкоди. Якщо зброя не була магічною, вона стає такою на час дії.

Вторинною дією у свій хід ви можете припинити це закляття й змусити зброю випустити спалах сяйва. Кожна вибрана вами видима істота в межах 30 футів від зброї повинна виконати кидок протидії статурою. У разі невдачі істота зазнає 4d8 променевої шкоди й сліпне на 1 хвилину. У разі успіху вона зазнає вдвічі менше шкоди й не сліпне. Наприкінці кожного свого ходу засліплена істота може повторити кидок протидії статурою, у разі успіху припиняючи ефект на собі.""",
    "You whisper a divine word under your breath, careful not to speak loudly, for such celestial power isn’t for the unworthy. Make a ranged spell attack against a target within range. On a hit, the target takes Radiant damage. If the target is a Fey, Fiend, or an Undead, its Speed is reduced by 10 feet and it can’t take Reactions until the end of its next turn.":
        "Ви пошепки промовляєте божественне слово, адже така небесна сила не призначена для недостойних. Виконайте атаку закляттям дальнього бою проти цілі в межах досяжності. У разі влучання ціль зазнає променевої шкоди. Якщо ціль — фея, нечисть або невмерлий, її швидкість зменшується на 10 футів і вона не може виконувати реагування до кінця свого наступного ходу.",
    "The target must make a Constitution saving throw. On a failed save, it takes [1], and you regain hit points equal to the damage dealt. On a successful save, it takes half as much damage, and you regain hit points equal to the damage dealt.":
        "Ціль повинна виконати кидок протидії статурою. У разі невдачі вона зазнає [1], а в разі успіху — вдвічі менше. Ви відновлюєте очки здоров’я в кількості, що дорівнює завданій шкоді.",
    "Roll your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die; that creature gains a number of Temporary Hit Points equal to the number rolled plus your Charisma modifier (minimum of 2 Temporary Hit Points). When a creature gains Temporary Hit Points in this way, it can immediately take a Reaction to move up to its Speed without provoking Opportunity Attacks or take the Dodge action.":
        "Киньте кістку <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>. Істота отримує тимчасові очки здоров’я в кількості, що дорівнює результату кидка + ваш модифікатор харизми (щонайменше 2). Отримавши ці тимчасові очки здоров’я, істота може негайно реагуванням або переміститися на відстань до своєї швидкості, не провокуючи принагідних атак, або виконати Ухилення.",
    "When you take a Bonus Action to give a creature a <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die, you can have the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition and teleport up to 30 feet to an unoccupied space you can see as part of that Bonus Action. This invisibility lasts until the start of your next turn and ends early immediately after you make an attack roll, deal damage, or cast a spell.":
        "Коли ви вторинною дією надаєте істоті кістку <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>, у межах тієї самої вторинної дії можете набути стану <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимість</LSTag> і телепортуватися на відстань до 30 футів у видимий вільний простір. Невидимість триває до початку вашого наступного ходу й достроково припиняється одразу після кидка атаки, завдання шкоди або проказування закляття.",
    "You can expend one use of your Channel Oath and distribute Temporary Hit Points to creatures of your choice within 30 feet of yourself, which can include you. The total number of Temporary Hit Points equals 2d8 plus your Paladin level, divided among the chosen creatures however you like.":
        "Ви можете витратити одне використання Обітного наснаження й довільно розподілити між вибраними істотами в межах 30 футів, зокрема собою, тимчасові очки здоров’я в загальній кількості 2d8 + ваш рівень паладина.",
    "One ally of your choice within 30 feet of you can move up to half their Speed. This movement does not provoke Opportunity Attacks.":
        "Один вибраний вами союзник у межах 30 футів може переміститися на відстань до половини своєї швидкості. Це переміщення не провокує принагідних атак.",
    "Distract your enemies with an illusion. Within [1] of the illusion, <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag> have <LSTag Tooltip=\"Advantage\">Advantage</LSTag> for you and your allies. Both the attacker and the creature must be within [1] of the illusion.":
        "Відверніть увагу ворогів ілюзією. Ви й ваші союзники маєте <LSTag Tooltip=\"Advantage\">перевагу</LSTag> для <LSTag Tooltip=\"AttackRoll\">кидків атаки</LSTag>, якщо нападник перебуває в межах [1] від ілюзії й ціль також перебуває в межах [1] від неї.",
    "You can cast spells as though you were in the illusion’s space, but you must use your own senses.":
        "Ви можете проказувати закляття так, наче перебуваєте в просторі ілюзії, але використовуєте власні чуття.",
    "Touch a willing creature. For the duration, once on each of the target's turns, it can spend 10 feet of movement to jump up to 30 feet. In addition, the target's maximum jump distance is tripled.":
        "Торкніться згодної істоти. На час дії раз у кожен свій хід ціль може витратити 10 футів руху, щоб стрибнути на відстань до 30 футів. Крім того, її максимальна дальність стрибка потроюється.",
    "Turn a creature's flesh hard as stone. It takes only <LSTag Tooltip=\"Resistant\">half the damage</LSTag> of all Bludgeoning, Piercing, and Slashing damage.":
        "Зробіть плоть істоти твердою, мов камінь. Вона зазнає лише <LSTag Tooltip=\"Resistant\">половини шкоди</LSTag> від усіх джерел дробильної, колотої та рубаної шкоди.",
    "The spell ends if you drop to 0 Hit Points. It also ends if the spell is cast again on either of the connected creatures. The spell remains in effect only while you and the target are within 60 feet of each other.":
        "Закляття завершується, якщо ваші очки здоров’я зменшуються до 0 або якщо його знову проказують на будь-яку з пов’язаних істот. Воно діє лише доки ви й ціль перебуваєте не далі ніж за 60 футів одне від одного.",
    """As a Magic action, you can expend a use of your Wild Shape and choose a point within 60 feet of yourself. Vitality-giving flowers and life-draining thorns briefly appear in a 10-foot-radius Sphere centered on that point. Enemy creatures in the Sphere take 2d6 Necrotic damage. Creatures in the area that are not your enemies regain 2d6 Hit Points.

The damage and healing each increase by 1d6 when you reach Druid level 5 (3d6) and level 10 (4d6).""":
        """Магічною дією ви можете витратити використання Дикої подоби й вибрати точку в межах 60 футів. У сфері радіусом 10 футів із центром у цій точці на мить з’являються життєдайні квіти та шипи, що висмоктують життя. Ворожі істоти у сфері зазнають 2d6 некротичної шкоди, а інші істоти відновлюють 2d6 очок здоров’я.

Шкода й зцілення збільшуються на 1d6 на 5-му рівні друїда (3d6) і ще раз на 10-му рівні (4d6).""",
    "At the start of each of your turns while your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is active, you can choose another creature within 10 feet of yourself to gain Temporary Hit Points. To determine the number of Temporary Hit Points, roll a number of d6s equal to your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> Damage bonus, and add them together. If any of these Temporary Hit Points remain when your Rage ends, they vanish.":
        "На початку кожного свого ходу, поки триває ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, ви можете надати іншій істоті в межах 10 футів тимчасові очки здоров’я. Киньте стільки кісток d6, скільки становить ваш бонус до шкоди від <LSTag Type=\"Status\" Tooltip=\"RAGE\">Люті</LSTag>, і додайте результати. Ціль отримує стільки тимчасових очок здоров’я; їхній залишок зникає після завершення Люті.",
    "You touch a willing creature. When the creature takes damage before the spell ends, the creature reduces the total damage taken by 1d4. A creature can benefit from this spell only once per turn.":
        "Ви торкаєтеся згодної істоти. Коли вона зазнає шкоди до завершення закляття, то зменшує загальну кількість шкоди на 1d4. Істота може отримати цю перевагу лише раз за хід.",
    "Reach into the target's pockets and attempt to steal an item. The Dexterity (<LSTag Type=\"Skills\" Tooltip=\"SleightOfHand\">Sleight of Hand</LSTag>) check uses your own modifier as the Arcane Trickster.":
        "Залізьте до кишень цілі й спробуйте викрасти предмет. Для перевірки спритності (<LSTag Type=\"Skills\" Tooltip=\"SleightOfHand\">Спритність рук</LSTag>) використовується ваш власний модифікатор Містичного штукаря.",
    "You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +[1] bonus to attack rolls and damage rolls. The spell ends early if you cast it again.":
        "Ви торкаєтеся немагічної зброї. До завершення закляття вона стає магічною й отримує бонус +[1] до кидків атаки та шкоди. Закляття достроково завершується, якщо ви прокажете його знову.",
    "Each of those creatures gains Temporary Hit Points equal to twice the number rolled on the Bardic Inspiration die, and each can move without provoking Opportunity Attacks until the end of its next turn.":
        "Кожна з цих істот отримує тимчасові очки здоров’я в кількості, що дорівнює подвоєному результату кидка кістки Бардівського натхнення, і до кінця свого наступного ходу може пересуватися, не провокуючи принагідних атак.",
    "You try to temporarily sliver the mind of one creature you can see within range. The target must succeed on an Intelligence saving throw or take Psychic damage and subtract 1d4 from the next saving throw it makes before the end of your next turn.":
        "Ви намагаєтеся на мить розщепити свідомість однієї видимої істоти в межах досяжності. Ціль повинна успішно виконати кидок протидії інтелектом, інакше зазнає психічної шкоди й відніме 1d4 від наступного кидка протидії, виконаного до кінця вашого наступного ходу.",
    "You drive a spike of psionic energy into the mind of one creature you can see within range. The target makes a Wisdom saving throw, taking Psychic damage on a failed save or half as much damage on a successful one. On a failed save, you also always know the target’s location until the spell ends. While you have this knowledge, the target can’t become hidden from you, and if it has the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition, it gains no benefit from that condition against you.":
        "Ви встромляєте шип псіонічної енергії у свідомість однієї видимої істоти в межах досяжності. Ціль виконує кидок протидії мудрістю. У разі невдачі вона зазнає психічної шкоди, а в разі успіху — вдвічі менше. Після невдачі ви також знаєте місцеперебування цілі до завершення закляття. Доки ви це знаєте, ціль не може сховатися від вас, а стан <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимість</LSTag> не надає їй переваг проти вас.",
    "You psychically lash out at one creature you can see within range. The target must make an Intelligence saving throw. On a failed save, the target takes psychic damage, and it can’t take a reaction until the end of its next turn. Moreover, on its next turn, it must choose whether it gets an action, or a bonus action; it gets only one of the two. On a successful save, the target takes half as much damage and suffers none of the spell’s other effects.":
        "Ви завдаєте психічного удару одній видимій істоті в межах досяжності. Ціль повинна виконати кидок протидії інтелектом. У разі невдачі вона зазнає психічної шкоди, не може виконувати реагування до кінця свого наступного ходу, а в наступний хід мусить вибрати лише одне: дію або вторинну дію. У разі успіху ціль зазнає вдвічі менше шкоди й уникає решти ефектів закляття.",
    """A silvery beam of pale light shines down in a 5-foot-radius, 40-foot-high Cylinder centered on a point within range. Until the spell ends, Dim Light fills the Cylinder, and you can take a Magic action on later turns to move the Cylinder up to 60 feet.

When the Cylinder appears, each creature in it makes a Constitution saving throw. On a failed save, a creature takes Radiant damage. On a successful save, a creature takes half as much damage only. A creature also makes this save when the spell’s area moves into its space and when it ends its turn there. A creature makes this save only once per turn.""":
        """Сріблястий промінь блідого світла осяває циліндр радіусом 5 футів і заввишки 40 футів із центром у вибраній точці в межах досяжності. До завершення закляття циліндр наповнений тьмяним світлом, а в наступні ходи ви можете магічною дією перемістити його на відстань до 60 футів.

Коли циліндр з’являється, кожна істота в ньому виконує кидок протидії статурою. У разі невдачі вона зазнає променевої шкоди, а в разі успіху — вдвічі менше. Істота також виконує цей кидок, коли зона закляття входить у її простір або коли вона завершує там хід, але не більше одного разу за хід.""",
    "Move the beam of moonlight up to [1].":
        "Перемістіть промінь місячного світла на відстань до [1].",
    "You magically transport yourself, reappearing amid a burst of moonlight.":
        "Ви магічно переноситеся й з’являєтеся у спалаху місячного світла.",
    "You begin a whispered dirge that is magically accompanied by the howling of spirits and other grim portents. For the duration, an aura radiates from you in a 30-foot Emanation. When you create the aura and at the start of each of your turns while it persists, you can choose one creature in it to make a Constitution saving throw. On a failure, the creature takes 3d8 Necrotic damage.":
        "Ви пошепки починаєте жалобну пісню, яку магічно супроводжують виття духів та інші лиховісні знамення. На час дії від вас поширюється 30-футова еманація аури. Коли ви створюєте ауру та на початку кожного свого ходу, доки вона існує, можете вибрати в ній одну істоту й змусити її виконати кидок протидії статурою. У разі невдачі істота зазнає 3d8 некротичної шкоди.",
    "As a Bonus Action, wrap a shadow rope around a creature's throat to start <LSTag Type=\"Status\" Tooltip=\"GARROTE_TARGET_HUMANOID\">Garrotting</LSTag> it.":
        "Вторинною дією обмотайте горло істоти тіньовою мотузкою й почніть її <LSTag Type=\"Status\" Tooltip=\"GARROTE_TARGET_HUMANOID\">душити</LSTag>.",
    """As a Bonus Action, you present your Holy Symbol and expend a use of Channel Divinity to curse one creature you can see within 30 feet of yourself until the start of your next turn. While cursed, the creature has Disadvantage on attack rolls and saving throws.

When you or an ally you can see hits the cursed target with an attack roll, you can end the curse early (no action required) to deal extra Necrotic or Radiant damage (your choice) equal to your Cleric level.""":
        """Вторинною дією ви здіймаєте священний символ і витрачаєте використання Божого наснаження, щоб проклясти одну видиму істоту в межах 30 футів до початку свого наступного ходу. Проклята істота має заваду для кидків атаки й протидії.

Коли ви або видимий вам союзник влучаєте в прокляту ціль атакою, ви можете достроково припинити прокляття (дія не потрібна), щоб завдати додаткової некротичної або променевої шкоди на ваш вибір у кількості, що дорівнює вашому рівню клірика.""",
    "Haunt a creature with its worst nightmares. It takes [1] per turn, has <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on <LSTag Tooltip=\"AbilityCheck\">Ability Checks</LSTag> and <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag>.":
        "Переслідуйте істоту її найгіршими кошмарами. Щохід вона зазнає [1] і має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок характеристик</LSTag> та <LSTag Tooltip=\"AttackRoll\">кидків атаки</LSTag>.",
    """You summon a phantom steed in an unoccupied space near the target, and the target immediately mounts it.

The steed can take one of the following actions of your choice on each of its turns: <LSTag Type="Spell" Tooltip="Shout_Dash">Dash</LSTag>, Disengage, Dodge

While mounted on the steed, when you take damage of 4 or higher, you must make a DC 8 Dexterity saving throw. On a failed save, you fall off the steed and have the Prone condition for 1 turn.


Only a player with a pure heart can see the steed.""":
        """Ви прикликаєте примарного скакуна у вільному просторі біля цілі, і ціль одразу сідає на нього верхи.

У кожен свій хід скакун може виконати одну з вибраних вами дій: <LSTag Type="Spell" Tooltip="Shout_Dash">Ривок</LSTag>, Відступ або Ухилення.

Перебуваючи верхи, щоразу, коли ви зазнаєте 4 або більше шкоди, мусите виконати кидок протидії спритністю з МС 8. У разі невдачі ви падаєте зі скакуна й перебуваєте в стані повалення протягом 1 ходу.


Скакуна може побачити лише гравець із чистим серцем.""",
    "As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to evoke healing energy that can restore a number of Hit Points equal to five times your Cleric level. Choose Bloodied creatures within [1] of yourself (which can include you), and divide those Hit Points among them.":
        "Магічною дією ви здіймаєте священний символ і витрачаєте використання Божого наснаження, щоб вивільнити цілющу енергію, яка відновлює очки здоров’я в загальній кількості, що дорівнює п’ятикратному рівню вашого клірика. Виберіть закривавлених істот у межах [1], зокрема за бажанням себе, і довільно розподіліть ці очки здоров’я між ними.",
    "You can choose a number of creatures equal to your Proficiency Bonus that you can see within 30 feet of yourself. Those creatures gain <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Heroic Inspiration</LSTag>.":
        "Виберіть видимих істот у межах 30 футів у кількості, що дорівнює вашому бонусу спеціалізації. Вони отримують <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Героїчне натхнення</LSTag>.",
    "If the bearer succeeds on a DC 15 <LSTag Type=\"Skills\" Tooltip=\"Medicine\">Medicine</LSTag> check, they can produce two alchemical extracts.":
        "Якщо носій успішно виконує перевірку <LSTag Type=\"Skills\" Tooltip=\"Medicine\">Медицини</LSTag> з МС 15, то може виготовити два алхімічні екстракти.",
    "The bearer gains resistance to bludgeoning, piercing, and slashing damage from both nonmagical and magical attacks.":
        "Носій отримує стійкість до дробильної, колотої та рубаної шкоди як від немагічних, так і від магічних атак.",
    "The bearer’s carrying capacity is increased tenfold.":
        "Вантажність носія збільшується вдесятеро.",
    "The bearer can see through darkness, including magical darkness.":
        "Носій бачить крізь темряву, зокрема магічну.",
    "The bearer gains a +5 bonus to initiative rolls and can’t be surprised.":
        "Носій отримує бонус +5 до кидків ініціативи, і його неможливо захопити зненацька.",
    "The bearer can perceive invisible creatures.":
        "Носій бачить невидимих істот.",
    "While the bearer is wearing armor, their AC increases by 1.":
        "Поки носій має на собі обладунки, його РЗ збільшується на 1.",
    "The effect improves when you reach 10th level in this class.":
        "Ефект посилюється на 10-му рівні цього класу.",
    "While the bearer is wielding a shield, the bonus to AC granted by the shield increases by 1.":
        "Поки носій тримає щит, наданий ним бонус до РЗ збільшується на 1.",
    "The bearer gains a +1 bonus to weapon attack rolls and damage rolls.":
        "Носій отримує бонус +1 до кидків атаки й шкоди зброєю.",
    "When the bearer makes a Constitution saving throw to maintain concentration, a roll of 9 or lower on the d20 is treated as a 10.":
        "Коли носій виконує кидок протидії статурою для підтримання концентрації, результат 9 або менше на d20 вважається 10.",
    "The bearer ignores difficult terrain and can’t be paralyzed or restrained.":
        "Носій ігнорує складний рельєф і не може бути паралізованим або знерухомленим.",
    "The bearer gains a +1 bonus to AC and saving throws.":
        "Носій отримує бонус +1 до РЗ і кидків протидії.",
    "The bearer’s spell save DC and spell attack rolls each increase by 1.":
        "МС протидії закляттям носія та його кидки атаки закляттями збільшуються на 1.",
    "The bearer gains a +1 bonus to attack rolls and damage rolls with unarmed strikes.":
        "Носій отримує бонус +1 до кидків атаки й шкоди Ударами голіруч.",
    "You choose a number of allies within a 30-foot emanation originating from you, up to a number of allies equal to your Charisma modifier. Each of those allies gains the benefit of your Action Surge.":
        "Виберіть союзників у 30-футовій еманації від вас у кількості, що не перевищує ваш модифікатор харизми. Кожен із них отримує перевагу вашого Внутрішнього резерву.",
    "Summon a black bear that can maul enemies with its <LSTag Type=\"Spell\" Tooltip=\"Target_Claws_Bear_Black_Summon\">Claws</LSTag> and knock them down with a <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">Charge</LSTag>.":
        "Прикличте чорного ведмедя, який шматує ворогів <LSTag Type=\"Spell\" Tooltip=\"Target_Claws_Bear_Black_Summon\">кігтями</LSTag> і збиває їх з ніг <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">натиском</LSTag>.",
    "Summon a boar that can gore enemies with its <LSTag Type=\"Spell\" Tooltip=\"Target_Tusk_Boar_Summon\">Tusk</LSTag> and knock them down with a <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">Charge</LSTag>.":
        "Прикличте кабана, який проштрикує ворогів <LSTag Type=\"Spell\" Tooltip=\"Target_Tusk_Boar_Summon\">іклом</LSTag> і збиває їх з ніг <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">натиском</LSTag>.",
    "Summon a wolf spider that can lunge at enemies with its <LSTag Type=\"Spell\" Tooltip=\"Target_Bite_GiantSpider_Summon\">Bite</LSTag> and knock them down with a <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">Charge</LSTag>.":
        "Прикличте вовчого павука, який кидається на ворогів із <LSTag Type=\"Spell\" Tooltip=\"Target_Bite_GiantSpider_Summon\">укусом</LSTag> і збиває їх з ніг <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">натиском</LSTag>.",
    "Summon a dire raven that can fly and strike at enemies with its <LSTag Type=\"Spell\" Tooltip=\"Target_Beak_Raven_Summon_BeastMaster\">Beak</LSTag>. It doesn’t provoke <LSTag Tooltip=\"OpportunityAttack\">Opportunity Attacks</LSTag> when it flies out of an enemy’s reach.":
        "Прикличте лютоворона, який літає й атакує ворогів <LSTag Type=\"Spell\" Tooltip=\"Target_Beak_Raven_Summon_BeastMaster\">дзьобом</LSTag>. Вилітаючи з досяжності ворога, він не провокує <LSTag Tooltip=\"OpportunityAttack\">принагідних атак</LSTag>.",
    "Summon a wolf that can tear into enemies with its <LSTag Type=\"Spell\" Tooltip=\"Target_Bite_Wolf_Summon\">Bite</LSTag> and knock them down with a <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">Charge</LSTag>.":
        "Прикличте вовка, який шматує ворогів <LSTag Type=\"Spell\" Tooltip=\"Target_Bite_Wolf_Summon\">укусом</LSTag> і збиває їх з ніг <LSTag Type=\"Spell\" Tooltip=\"Rush_Rush_Boar_Summon\">натиском</LSTag>.",
    "The target is pushed [1] straight away from you. You can then move up to half your Speed straight toward the target without provoking Opportunity Attacks.":
        "Ціль відштовхується від вас по прямій на [1]. Потім ви можете переміститися прямо до неї на відстань до половини своєї швидкості, не провокуючи принагідних атак.",
    "The target’s Speed is reduced by [1] until the start of your next turn. A target can be affected by only one Hamstring Blow at a time—the most recent one.":
        "Швидкість цілі зменшується на [1] до початку вашого наступного ходу. Одночасно на ціль може діяти лише один Удар по сухожиллю — найновіший.",
    "Immediately after you teleport, you and one creature you can see within 10 feet of yourself gains 1d10 Temporary Hit Points.":
        "Одразу після телепортації ви й одна видима істота в межах 10 футів отримуєте 1d10 тимчасових очок здоров’я.",
    """You learn the arcane plans of magic items, allowing you to create replicas of them and grant those items to yourself or your allies. A replicated magic item loses its magic when you finish a Long Rest.

You can create only one instance of each replicated item when you finish a Long Rest. A creature can benefit from only one replicated item at a time.

Creating each replicated magic item requires you to have reached a certain Artificer level.""":
        """Ви вивчаєте містичні креслення магічних предметів, щоб створювати їхні копії та надавати їх собі або союзникам. Відтворений магічний предмет втрачає магію після завершення вашого довгого відпочинку.

Після кожного довгого відпочинку можна створити лише один екземпляр кожного відтворюваного предмета. Істота може одночасно отримувати користь лише від одного такого предмета.

Для створення кожного відтворюваного магічного предмета потрібен певний рівень винахідника.""",
    "Place one Illrigger Seal on the target.":
        "Накладіть на ціль одну печатку ілриґера.",
    "You can use your Channel Divinity to turn a creature’s shadow against them. As an action, choose one creature that you can see within 30 feet of you. It is restrained by its shadow until the end of your next turn. You can use this feature even if the target is in an area where it casts no shadow.":
        "Ви можете скористатися Божим наснаженням, щоб обернути тінь істоти проти неї. Дією виберіть одну видиму істоту в межах 30 футів. Її власна тінь знерухомлює її до кінця вашого наступного ходу. Цю особливість можна використати, навіть якщо ціль перебуває в місці, де не відкидає тіні.",
    "You can expend a seal as a bonus action to weave a mantle of semisolid shadows around yourself or a creature you touch. The target gains a +2 bonus to AC for 1 minute.":
        "Вторинною дією ви можете витратити печатку й сплести мантію з напівматеріальних тіней навколо себе або істоти, якої торкаєтеся. Ціль отримує бонус +2 до РЗ на 1 хвилину.",
    """As an action, you can shape-shift to change your appearance and your voice. You determine the specifics of the changes, including your coloration, hair length, and sex. You can also adjust your height and weight and can change your size between Medium and Small. You can make yourself appear as a member of another playable species, though none of your game statistics change. You can’t duplicate the appearance of an individual you’ve never seen, and you must adopt a form that has the same basic arrangement of limbs that you have. This trait doesn’t change your clothing and equipment.

While shape-shifted with this trait, you have Advantage on Charisma checks.

You stay in the new form until you take an action to revert to your true form.""":
        """Дією ви можете змінити подобу, зовнішність і голос. Ви визначаєте всі подробиці змін, зокрема забарвлення, довжину волосся та стать, можете змінити зріст і вагу, а також розмір між середнім і малим. Ви можете набути вигляду представника іншого ігрового виду, але ваші ігрові характеристики не змінюються. Ви не можете відтворити зовнішність особи, якої ніколи не бачили, а нова подоба повинна мати таке саме основне розташування кінцівок. Ця риса не змінює одяг і спорядження.

У зміненій подобі ви маєте перевагу для перевірок харизми.

Ви зберігаєте нову подобу, доки дією не повернетеся до справжньої.""",
    "Trip a target with your shield, knocking it Prone.":
        "Підсічіть ціль щитом і поваліть її.",
    "Each creature of your choice in a 5-foot-radius Sphere centered on a point within range must succeed on a Wisdom saving throw or have the Incapacitated condition until the end of its next turn, at which point it must repeat the save. If the target fails the second save, the target has the <LSTag Type=\"Status\" Tooltip=\"SLEEP\">Unconscious</LSTag> condition for the duration. The spell ends on a target if it takes damage or someone within 5 feet of it takes an action to shake it out of the spell’s effect.":
        "Кожна вибрана вами істота у сфері радіусом 5 футів із центром у точці в межах досяжності повинна успішно виконати кидок протидії мудрістю, інакше набуде стану недієздатності до кінця свого наступного ходу, після чого повторить кидок. Якщо другий кидок теж невдалий, ціль перебуває в стані <LSTag Type=\"Status\" Tooltip=\"SLEEP\">Непритомність</LSTag> протягом дії закляття. Ефект на цілі завершується, якщо вона зазнає шкоди або якщо хтось у межах 5 футів витратить дію, щоб розбудити її.",
    "Once per turn when you hit a creature with your pact weapon, you can expend a Pact Magic spell slot to deal an extra 1d8 Force damage to the target, plus another 1d8 per level of the spell slot, and you can give the target the Prone condition if it is Huge or smaller.":
        "Раз за хід, коли ви влучаєте в істоту зброєю договору, можете витратити чарунку Магії договору, щоб завдати цілі додатково 1d8 силової шкоди + ще 1d8 за кожен рівень чарунки. Якщо ціль величезна або менша, ви також можете повалити її.",
    "When you deal Sneak Attack damage, you can forgo your Sneak Attack's extra damage. If you do, the target must succeed on a Constitution saving throw or be Paralyzed until the end of your next turn.":
        "Коли ви завдаєте шкоди Підступним ударом, можете відмовитися від його додаткової шкоди. Тоді ціль повинна успішно виконати кидок протидії статурою, інакше буде паралізована до кінця вашого наступного ходу.",
    "Heal a creature within range that has 0 Hit Points and isn’t dead.":
        "Зціліть істоту в межах досяжності, яка має 0 очок здоров’я, але ще не померла.",
    "You can choose a space within 30 feet of yourself that is occupied by a creature. If that creature is willing, you both teleport, swapping places.":
        "Виберіть простір у межах 30 футів, зайнятий істотою. Якщо вона згодна, ви обоє телепортуєтеся й міняєтеся місцями.",
    """You send forth a spectral copy of yourself to strike down your foe. Make a melee spell attack against a creature within 20 feet of you. On a hit, the target takes [1] damage of your weapon’s damage type.

You can then spend your action to move up to 20 feet in a straight line towards the target, streaking through a spectral trail, and take the Attack action against it. To use this action, you must attack with the melee weapon used for the casting of this spell.""":
        """Ви посилаєте вперед свою примарну копію, щоб уразити ворога. Виконайте атаку закляттям ближнього бою проти істоти в межах 20 футів. У разі влучання ціль зазнає [1] шкоди того самого типу, що й ваша зброя.

Потім ви можете витратити дію, щоб промайнути примарним слідом до 20 футів по прямій до цілі й виконати проти неї дію «Атака». Для цієї атаки потрібно використати зброю ближнього бою, якою проказано закляття.""",
    "When you spend at least 1 Sorcery Point as part of a Magic action or a Bonus Action on your turn, you can unleash one of the following magical effects of your choice. You can do so only once per turn.":
        "Коли у свій хід ви витрачаєте щонайменше 1 очко чародійства як частину магічної або вторинної дії, можете вивільнити один із наведених нижче магічних ефектів на свій вибір. Це можна зробити лише раз за хід.",
    "You or one creature you can see within 30 feet of yourself gains Temporary Hit Points equal to 1d4 plus your Charisma modifier.":
        "Ви або одна видима істота в межах 30 футів отримуєте тимчасові очки здоров’я в кількості 1d4 + ваш модифікатор харизми.",
    "One creature you can see within 30 feet of yourself takes 1d4 Fire damage.":
        "Одна видима істота в межах 30 футів зазнає 1d4 вогняної шкоди.",
    "One creature you can see within 30 feet of yourself takes 1d4 Radiant damage.":
        "Одна видима істота в межах 30 футів зазнає 1d4 променевої шкоди.",
    """You conjure a pillar of spellfire in a 20-foot-radius, 20-foot-high Cylinder centered on a point within range. The area of the Cylinder is Bright Light, and each creature in it when it appears makes a Constitution saving throw, taking Radiant damage on a failed save or half as much damage on a successful one. A creature also makes this save when it enters the spell’s area for the first time on a turn or ends its turn there. A creature makes this save only once per turn.

In addition, whenever a creature in the Cylinder casts a spell, that creature makes a Constitution saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted.

When you cast this spell, you can designate creatures to be unaffected by it.""":
        """Ви прикликаєте стовп чаровогню в циліндрі радіусом 20 футів і заввишки 20 футів із центром у вибраній точці в межах досяжності. Циліндр наповнений яскравим світлом. Коли він з’являється, кожна істота в ньому виконує кидок протидії статурою. У разі невдачі вона зазнає променевої шкоди, а в разі успіху — вдвічі менше. Істота також виконує цей кидок, коли вперше за хід входить до зони закляття або завершує там хід, але не більше одного разу за хід.

Крім того, щоразу, коли істота в циліндрі проказує закляття, вона виконує кидок протидії статурою. У разі невдачі закляття розсіюється без ефекту, а витрачені на нього дія, вторинна дія або реагування марнуються.

Проказуючи це закляття, ви можете визначити істот, на яких воно не діятиме.""",
    "Teleport up to 30 feet to an unoccupied space it can see.":
        "Телепортуватися на відстань до 30 футів у видимий вільний простір.",
    "Your tinkering has borne you a companion, a Steel Defender.":
        "Ваше майстрування подарувало вам супутника — Сталевого захисника.",
    "You can invoke the Stone Rune to force a creature into a hypnotic state for 1 minute.":
        "Ви можете активувати руну каменю й увести істоту в гіпнотичний стан на 1 хвилину.",
    "When you take damage from a creature within 60 feet of you, you can take a Reaction to deal 1d8 Thunder damage to that creature.":
        "Коли істота в межах 60 футів завдає вам шкоди, ви можете реагуванням завдати їй 1d8 громової шкоди.",
    "You understand the power of striking from the shadows. Once per turn, when you hit an interdicted creature with a melee weapon attack and you have advantage on the attack roll, you can roll a number of d4s equal to your proficiency bonus and deal extra damage equal to the total you rolled.":
        "Ви опанували мистецтво удару з тіней. Раз за хід, коли ви з перевагою для кидка атаки влучаєте зброєю ближнього бою в істоту, позначену інтердиктом, можете кинути стільки кісток d4, скільки становить ваш бонус спеціалізації, і завдати додаткової шкоди в кількості, що дорівнює сумі результатів.",
    "You call forth a Celestial spirit. It manifests in an angelic form in an unoccupied space that you can see within range and uses the Celestial Spirit stat block.":
        "Ви прикликаєте духа небесника. Він з’являється в ангельській подобі у видимому вільному просторі в межах досяжності й використовує блок характеристик Небесного духа.",
    "The chosen creature gains 1d10 Temporary Hit Points.":
        "Вибрана істота отримує 1d10 тимчасових очок здоров’я.",
    "The spirit touches another creature. The target regains Hit Points equal to 2d8 + 5.":
        "Дух торкається іншої істоти. Ціль відновлює 2d8 + 5 очок здоров’я.",
    "You call forth a Dragon spirit. It manifests in an unoccupied space that you can see within range and uses the Draconic Spirit stat block. The creature disappears when it drops to 0 Hit Points or when the spell ends.":
        "Ви прикликаєте духа дракона. Він з’являється у видимому вільному просторі в межах досяжності й використовує блок характеристик Драконічного духа. Істота зникає, коли її очки здоров’я зменшуються до 0 або коли закляття завершується.",
    """You cause psychic energy to erupt at a point within range. Each creature in a  [1] radius Sphere centered on that point makes an Intelligence saving throw, taking Psychic damage on a failed save or half as much damage on a successful one.

On a failed save, a target also has muddled thoughts for 1 minute. During that time, it subtracts 1d6 from all its attack rolls and ability checks, as well as any Constitution saving throws to maintain Concentration. The target makes an Intelligence saving throw at the end of each of its turns, ending the effect on itself on a success.""":
        """Ви вивільняєте психічну енергію в точці в межах досяжності. Кожна істота у сфері радіусом [1] із центром у цій точці виконує кидок протидії інтелектом. У разі невдачі вона зазнає психічної шкоди, а в разі успіху — вдвічі менше.

У разі невдачі думки цілі також сплутуються на 1 хвилину. У цей час вона віднімає 1d6 від усіх кидків атаки, перевірок характеристик і кидків протидії статурою для підтримання концентрації. Наприкінці кожного свого ходу ціль повторює кидок протидії інтелектом, у разі успіху припиняючи ефект на собі.""",
    "When you cast this spell, a flexible exoskeleton covered in thorns appears around a willing target within range. The target gains [1] Temporary Hit Points. If a creature hits the target with a melee attack roll before the spell ends, that creature takes Piercing damage equal to the number of Temporary Hit Points lost as a result of the attack. This spell ends early if the target has no remaining Temporary Hit Points granted by this spell.":
        "Коли ви проказуєте це закляття, навколо згодної цілі в межах досяжності з’являється гнучкий екзоскелет, укритий шипами. Ціль отримує [1] тимчасових очок здоров’я. Якщо до завершення закляття істота влучає в ціль атакою ближнього бою, нападник зазнає колотої шкоди в кількості тимчасових очок здоров’я, втрачених ціллю від цієї атаки. Закляття достроково завершується, коли в цілі не залишається наданих ним тимчасових очок здоров’я.",
    "A creature hit by the pulse has Disadvantage on attack rolls against targets other than you until the start of your next turn.":
        "Істота, в яку влучив імпульс, має заваду для кидків атаки проти всіх цілей, крім вас, до початку вашого наступного ходу.",
    "Whenever you take the Bonus Action to create or move the illusion of your Invoke Duplicity, you can teleport, swapping places with the illusion.":
        "Щоразу, коли ви вторинною дією створюєте або переміщуєте ілюзію Дволикості, можете телепортуватися й помінятися з нею місцями.",
    "A creature you touch is magically infused with the regenerative properties of troll blood. For the duration of the spell, the target regains 5 Hit Points at the start of each of its turns, if it has at least 1 Hit Point, and automatically succeeds on Death Saving Throws.":
        "Істота, якої ви торкаєтеся, магічно переймає відновні властивості крові троля. На час дії закляття, якщо ціль має щонайменше 1 очко здоров’я, вона відновлює 5 очок здоров’я на початку кожного свого ходу й автоматично досягає успіху в кидках протидії смерті.",
    "Guided by a flash of magical insight, you make one attack with the weapon used in the spell’s casting. The attack uses your spellcasting ability for the attack and damage rolls instead of using Strength or Dexterity. If the attack deals damage, it can be Radiant damage or the weapon’s normal damage type (your choice).":
        "Керуючись спалахом магічного осяяння, ви виконуєте одну атаку зброєю, використаною для проказування закляття. Для кидків атаки й шкоди використовується ваша базова характеристика проказування замість сили чи спритності. У разі влучання атака завдає променевої шкоди або шкоди звичайного типу зброї на ваш вибір.",
    """You create a long, life-stealing tendril of shadow that lashes out at a creature you can see within range.

Make a ranged spell attack against the target. On a hit, the target takes Necrotic damage. Roll the spell's damage dice again and gain Temporary Hit Points equal to the result.
""":
        """Ви створюєте довге тіньове щупальце, що висмоктує життя й б’є видиму істоту в межах досяжності.

Виконайте атаку закляттям дальнього бою проти цілі. У разі влучання ціль зазнає некротичної шкоди. Знову киньте кістки шкоди закляття й отримайте тимчасові очки здоров’я в кількості, що дорівнює результату.
""",
    "When you burn one or more seals on an interdicted creature, you can use your reaction to unleash an explosion of hellish energy around them. Each creature of your choice within 10 feet of the target must make a Dexterity saving throw. On a failed save, a creature takes the same amount and type of damage as the seals dealt to the interdicted creature. On a successful save, a creature takes half as much damage.":
        "Коли ви спалюєте одну або більше печаток на істоті, позначеній інтердиктом, можете реагуванням вивільнити навколо неї вибух пекельної енергії. Кожна вибрана вами істота в межах 10 футів від цілі повинна виконати кидок протидії спритністю. У разі невдачі вона зазнає стільки ж шкоди того самого типу, скільки печатки завдали позначеній істоті, а в разі успіху — вдвічі менше.",
    "As a Magic action, you can unleash one of your channeled spirits. Choose one creature you can see within 30 feet of yourself as the spirit’s target. The spirit then takes effect; if a spirit’s effect requires a saving throw, the DC equals your Bard spell save DC. This action allows you to actually use the spirit.":
        "Магічною дією ви можете вивільнити одного зі спрямованих духів. Виберіть видиму істоту в межах 30 футів як ціль духа, після чого його ефект спрацює. Якщо ефект вимагає кидка протидії, його МС дорівнює вашій МС протидії закляттям барда. Саме цією дією ви застосовуєте духа.",
    "The target makes a Dexterity saving throw, taking Fire damage equal to four rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die on a failed save or half as much damage on a successful one.":
        "Ціль виконує кидок протидії спритністю. У разі невдачі вона зазнає вогняної шкоди в кількості, що дорівнює чотирьом кидкам кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>, а в разі успіху — вдвічі менше.",
    "Until the end of your next turn, any creature that hits the target with a melee attack roll takes Force damage equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die.":
        "До кінця вашого наступного ходу кожна істота, яка влучає в ціль атакою ближнього бою, зазнає силової шкоди в кількості, що дорівнює кидку кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>.",
    "The target regains Hit Points equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die plus your Charisma modifier.":
        "Ціль відновлює очки здоров’я в кількості, що дорівнює кидку кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> + ваш модифікатор харизми.",
    "The target and each creature of your choice in a 30-foot Emanation originating from the target must succeed on a Wisdom saving throw or have the Frightened condition until the start of your next turn. While a creature is Frightened, its Speed is halved (round down), and it can take either an action or a Bonus Action, not both.":
        "Ціль і кожна вибрана вами істота в 30-футовій еманації від неї повинні успішно виконати кидок протидії мудрістю, інакше перебуватимуть у стані переляку до початку вашого наступного ходу. Швидкість наляканої істоти зменшена вдвічі з округленням донизу, і вона може виконувати або дію, або вторинну дію, але не обидві.",
    "The target has Advantage on D20 Tests until the start of your next turn.":
        "Ціль має перевагу для перевірок d20 до початку вашого наступного ходу.",
    "Until the end of its turn, the target can use its Reaction to teleport up to 30 feet to an unoccupied space it can see.":
        "До кінця свого ходу ціль може реагуванням телепортуватися на відстань до 30 футів у видимий вільний простір.",
    "The target has the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition until the end of its next turn or until the target makes an attack roll, deals damage, or casts a spell. When the invisibility ends, each creature in a 5-foot Emanation originating from the target must succeed on a Constitution saving throw or take Necrotic damage equal to two rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die.":
        "Ціль перебуває в стані <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Невидимість</LSTag> до кінця свого наступного ходу або доки не виконає кидок атаки, не завдасть шкоди чи не прокаже закляття. Коли невидимість завершується, кожна істота в 5-футовій еманації від цілі повинна успішно виконати кидок протидії статурою, інакше зазнає некротичної шкоди в кількості, що дорівнює двом кидкам кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>.",
    "The target takes Force damage equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die plus your Charisma modifier.":
        "Ціль зазнає силової шкоди в кількості, що дорівнює кидку кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> + ваш модифікатор харизми.",
    "The target makes a Wisdom saving throw. On a failed save, the target takes Psychic damage equal to two rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die and has the Charmed condition until the start of your next turn. On a successful save, the target takes half as much damage only.":
        "Ціль виконує кидок протидії мудрістю. У разі невдачі вона зазнає психічної шкоди в кількості, що дорівнює двом кидкам кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>, і перебуває в стані зачарування до початку вашого наступного ходу. У разі успіху ціль зазнає лише половини шкоди.",
    "The target gains Temporary Hit Points equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die plus your Bard level. While the target has these Temporary Hit Points, its Speed increases by 10 feet.":
        "Ціль отримує тимчасові очки здоров’я в кількості, що дорівнює кидку кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> + ваш рівень барда. Доки ціль має ці тимчасові очки здоров’я, її швидкість збільшена на 10 футів.",
    "You brandish the weapon used in the spell’s casting and make a melee attack with it against one creature within 5 feet of you. On a hit, the target suffers the weapon attack’s normal effects and then radiates a dark aura of energy until the start of your next turn. If the target makes an attack or casts a spell before then, the target takes [1] and the spell ends.":
        "Ви замахуєтеся зброєю, використаною для проказування закляття, і виконуєте нею атаку ближнього бою проти істоти в межах 5 футів. У разі влучання ціль зазнає звичайних ефектів атаки зброєю, а потім до початку вашого наступного ходу випромінює темну ауру енергії. Якщо до того часу ціль атакує або проказує закляття, вона зазнає [1], а закляття завершується.",
    "The night has taught you to be vigilant. As an action, you give one creature you touch (including possibly yourself) a +5 bonus to its next Initiative roll. This benefit ends immediately if you use this feature again.":
        "Ніч навчила вас пильності. Дією ви надаєте одній істоті, якої торкаєтеся, зокрема собі, бонус +5 до її наступного кидка ініціативи. Ця перевага негайно припиняється, якщо ви скористаєтеся особливістю знову.",
    "You gain the ability to foretell a creature’s doom. As a Bonus Action, choose a creature you can see within 120 feet of yourself. Until the start of your next turn, attack rolls against that creature have Advantage.":
        "Ви навчаєтеся провіщати загибель істоти. Вторинною дією виберіть видиму істоту в межах 120 футів. Кидки атаки проти неї мають перевагу до початку вашого наступного ходу.",
    "You can use your Channel Oath to invest your presence with the warding power of your faith. You can choose a number of creatures you can see within 30 feet of you, up to a number equal to your Charisma modifier (minimum of one creature). For 1 minute, you and the chosen creatures have advantage on Intelligence, Wisdom, and Charisma saving throws.":
        "Ви можете скористатися Обітним наснаженням, щоб сповнити свою присутність захисною силою віри. Виберіть видимих істот у межах 30 футів у кількості, що не перевищує ваш модифікатор харизми (щонайменше одну). Протягом 1 хвилини ви й вибрані істоти маєте перевагу для кидків протидії інтелектом, мудрістю та харизмою.",
    "The target must succeed on a Constitution saving throw against your spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from you. To determine this damage, roll a number of d6s equal to your Wisdom modifier.":
        "Ціль повинна успішно виконати кидок протидії статурою проти вашої МС протидії закляттям, інакше зазнає холодової шкоди, а якщо вона велика або менша — її відштовхне від вас на відстань до 15 футів. Щоб визначити шкоду, киньте стільки кісток d6, скільки становить ваш модифікатор мудрості.",
    "Creatures within 10 feet of the space you left or the space you appear in (your choice) must succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage.":
        "Істоти в межах 10 футів від простору, який ви залишили або в якому з’явилися на ваш вибір, повинні успішно виконати кидок протидії мудрістю проти вашої МС протидії закляттям, інакше зазнають 2d10 психічної шкоди.",
    "When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.":
        "Використовуючи Фейський крок, ви можете торкнутися однієї згодної істоти в межах 5 футів. Замість вас телепортується вона й з’являється у вибраному вами видимому вільному просторі в межах 30 футів.",
    "When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.":
        "Використовуючи Фейський крок, перед телепортацією виберіть одну видиму істоту в межах 5 футів. Вона повинна успішно виконати кидок протидії мудрістю, інакше боятиметься вас до кінця вашого наступного ходу.",
    "As a Bonus Action, you can move the illusion.":
        "Вторинною дією ви можете перемістити ілюзію.",
    "Creatures within 10 feet of the space you left must succeed on a Wisdom saving throw against your spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your next turn.":
        "Істоти в межах 10 футів від простору, який ви залишили, повинні успішно виконати кидок протидії мудрістю проти вашої МС протидії закляттям, інакше матимуть заваду для кидків атаки проти всіх істот, крім вас, до початку вашого наступного ходу.",
    "You can move an object or a creature with your mind. As a Magic action, choose one target you can see within 30 feet of yourself; the target must be a loose object that is Large or smaller or one willing creature other than you. You transport the target up to 30 feet to an unoccupied space you can see. Alternatively, if the target is a Tiny object, you can transport it to or from your hand.":
        "Ви можете рухати предмет або істоту силою думки. Магічною дією виберіть одну видиму ціль у межах 30 футів: незафіксований предмет великого або меншого розміру чи одну згодну істоту, крім себе. Перемістіть ціль на відстань до 30 футів у видимий вільний простір. Якщо ціль — крихітний предмет, натомість можете перенести його до своєї руки або з неї.",
    "A line of roaring flame 30 feet long and 5 feet wide emanates from you in a direction you choose. Each creature in the line must make a Dexterity saving throw. A creature takes fire damage on a failed save, or half as much damage on a successful one.":
        "Від вас у вибраному напрямку виривається смуга ревучого полум’я завдовжки 30 футів і завширшки 5 футів. Кожна істота в смузі виконує кидок протидії спритністю. У разі невдачі вона зазнає вогняної шкоди, а в разі успіху — вдвічі менше.",
    """You channel energy from the Astral Sea to unleash a torrent of magic from yourself. Choose Cold or Radiant for the type of energy channeled. Each creature in a 30-foot Cone originating from you makes a Dexterity saving throw. On a failed save, the target takes damage of the chosen type and suffers an additional effect determined by the damage type:

Cold Damage. The target has Disadvantage on the next D20 Test it makes before the end of your next turn.
Radiant Damage. The target has the Blinded condition until the end of your next turn.

On a successful save, the target takes half as much damage only.""":
        """Ви спрямовуєте енергію Астрального моря й вивільняєте потік магії. Виберіть холодову або променеву енергію. Кожна істота у 30-футовому конусі від вас виконує кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу та додаткового ефекту:

Холодова шкода. Ціль має заваду для наступної перевірки d20, яку виконає до кінця вашого наступного ходу.
Променева шкода. Ціль перебуває в стані сліпоти до кінця вашого наступного ходу.

У разі успіху ціль зазнає лише половини шкоди.""",
    "You can use an action to exhale a plume of powerful energy from inside of you. Each creature in a 15-foot cone must make a Dexterity saving throw against your spell save DC. A creature takes Fire damage on a failed save, or half as much on a successful one.":
        "Дією ви можете видихнути потік потужної енергії. Кожна істота у 15-футовому конусі виконує кидок протидії спритністю проти вашої МС протидії закляттям. У разі невдачі вона зазнає вогняної шкоди, а в разі успіху — вдвічі менше.",
    "Your breath weapon improves at certain levels. At 6th level, your breath weapon deals 3d6 damage. At 10th level, it deals 4d6 damage.":
        "Ваша Дихальна зброя посилюється на певних рівнях: завдає 3d6 шкоди на 6-му рівні й 4d6 на 10-му.",
    "You launch a dazzling array of flashing, colorful light. Each creature in a 15-foot Cone originating from you must succeed on a Constitution saving throw or have the Blinded condition until the end of your next turn.":
        "Ви випускаєте сліпучий потік мерехтливого різнобарвного світла. Кожна істота у 15-футовому конусі від вас повинна успішно виконати кидок протидії статурою, інакше перебуватиме в стані сліпоти до кінця вашого наступного ходу.",
    "The cannon blasts fire in a 15-foot Cone. Each creature in that area makes a Dexterity saving throw against your spell save DC, taking Fire damage on a failed save or half as much damage on a successful one. Flammable objects in the Cone that aren’t being worn or carried start burning.":
        "Гармата вивергає вогонь у 15-футовому конусі. Кожна істота в зоні виконує кидок протидії спритністю проти вашої МС протидії закляттям. У разі невдачі вона зазнає вогняної шкоди, а в разі успіху — вдвічі менше. Займисті предмети в конусі, які ніхто не носить і не тримає, спалахують.",
    """When you cast this spell, choose one of the following effects that determine the spell’s damage type:

Air. The damage type is Thunder. Each creature that fails the saving throw is pushed 10 feet away from you.

Coldfire. The damage type is Cold. Each creature that fails the saving throw has the Frightened condition until the start of your next turn.

Earth. The damage type is Bludgeoning. Each creature that fails the saving throw has its Speed reduced to 0 until the end of its next turn.

Fire. The damage type is Fire. Each creature that fails the saving throw is engulfed in flames and takes Fire damage at the end of its next turn. As an action, it can extinguish fire on itself by giving itself the Prone condition and rolling on the ground. The fire also goes out if it is doused, submerged, or suffocated.

Water. The damage type is Acid. Each creature that fails the saving throw has the Prone condition.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Проказуючи це закляття, виберіть один із наведених ефектів, що визначає тип його шкоди:

Повітря. Громова шкода. Кожна істота, яка провалила кидок протидії, відштовхується від вас на 10 футів.

Холодне полум’я. Холодова шкода. Кожна істота, яка провалила кидок протидії, перебуває в стані переляку до початку вашого наступного ходу.

Земля. Дробильна шкода. Швидкість кожної істоти, яка провалила кидок протидії, зменшується до 0 до кінця її наступного ходу.

Вогонь. Вогняна шкода. Кожну істоту, яка провалила кидок протидії, охоплює полум’я, і наприкінці свого наступного ходу вона зазнає вогняної шкоди. Дією істота може повалитися й покотитися землею, щоб загасити вогонь на собі. Вогонь також гасне, якщо його залити, занурити у воду або перекрити доступ повітря.

Вода. Кислотна шкода. Кожна істота, яка провалила кидок протидії, набуває стану повалення.

Кожна істота у 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.""",
    """Air. The damage type is Thunder. Each creature that fails the saving throw is pushed 10 feet away from you.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Повітря. Громова шкода. Кожна істота, яка провалила кидок протидії, відштовхується від вас на 10 футів.

Кожна істота у 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.""",
    """Coldfire. The damage type is Cold. Each creature that fails the saving throw has the Frightened condition until the start of your next turn.

Earth. The damage type is Bludgeoning. Each creature that fails the saving throw has its Speed reduced to 0 until the end of its next turn.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Холодне полум’я. Холодова шкода. Кожна істота, яка провалила кидок протидії, перебуває в стані переляку до початку вашого наступного ходу.

Земля. Дробильна шкода. Швидкість кожної істоти, яка провалила кидок протидії, зменшується до 0 до кінця її наступного ходу.

Кожна істота у 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.""",
    """Earth. The damage type is Bludgeoning. Each creature that fails the saving throw has its Speed reduced to 0 until the end of its next turn.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Земля. Дробильна шкода. Швидкість кожної істоти, яка провалила кидок протидії, зменшується до 0 до кінця її наступного ходу.

Кожна істота у 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.""",
    """Fire. The damage type is Fire. Each creature that fails the saving throw is engulfed in flames and takes Fire damage at the end of its next turn. As an action, it can extinguish fire on itself by giving itself the Prone condition and rolling on the ground. The fire also goes out if it is doused, submerged, or suffocated.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Вогонь. Вогняна шкода. Кожну істоту, яка провалила кидок протидії, охоплює полум’я, і наприкінці свого наступного ходу вона зазнає вогняної шкоди. Дією істота може повалитися й покотитися землею, щоб загасити вогонь на собі. Вогонь також гасне, якщо його залити, занурити у воду або перекрити доступ повітря.

Кожна істота у 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.""",
    """Water. The damage type is Acid. Each creature that fails the saving throw has the Prone condition.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Вода. Кислотна шкода. Кожна істота, яка провалила кидок протидії, набуває стану повалення.

Кожна істота у 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — вдвічі менше.""",
    "You can expend 2 Divine Points to call down radiant blades in a 45-foot-long, 5-foot-wide Line. Each creature in the Line must make a Dexterity saving throw, taking Radiant damage equal to your Sneak Attack damage on a failed save, or half as much damage on a successful one.":
        "Ви можете витратити 2 божественні очки й прикликати променеві клинки в смузі завдовжки 45 футів і завширшки 5 футів. Кожна істота в смузі виконує кидок протидії спритністю. У разі невдачі вона зазнає променевої шкоди в кількості, що дорівнює шкоді вашого Підступного удару, а в разі успіху — вдвічі менше.",
    "Silver energy bursts out from you in a 120-foot-long, 5-foot-wide Line. Each creature of your choice in the Line makes a Strength saving throw. On a failed save, a creature takes Force damage and has the Prone condition. On a successful save, a creature takes half as much damage only.":
        "Від вас виривається срібна енергія у смузі завдовжки 120 футів і завширшки 5 футів. Кожна вибрана вами істота в смузі виконує кидок протидії силою. У разі невдачі вона зазнає силової шкоди й набуває стану повалення, а в разі успіху — лише половини шкоди.",
    "You can take a Magic action to unleash a concentrated beam of lightning from the blade in a Line that is 60 feet long and 5 feet wide. Each creature in the Line must make a DC 15 Dexterity saving throw, taking 4d6 Lightning damage on a failed save or half as much damage on a successful one.":
        "Магічною дією ви можете випустити з клинка зосереджений промінь блискавки у смузі завдовжки 60 футів і завширшки 5 футів. Кожна істота в смузі виконує кидок протидії спритністю з МС 15. У разі невдачі вона зазнає 4d6 блискавкової шкоди, а в разі успіху — вдвічі менше.",
    "You summon and unleash a murder of deadly crows. Each creature of your choice in a 30-foot Cone originating from you makes a Dexterity saving throw. On a failed save, the target takes 5d6 Force damage and has the <LSTag Type=\"Status\" Tooltip=\"BLINDED\">Blinded</LSTag> condition. On a successful save, it takes half as much damage only. A Blinded creature repeats the save at the end of each of its turns, ending the effect on itself on a success.":
        "Ви прикликаєте й випускаєте зграю смертоносних ворон. Кожна вибрана вами істота у 30-футовому конусі від вас виконує кидок протидії спритністю. У разі невдачі ціль зазнає 5d6 силової шкоди й набуває стану <LSTag Type=\"Status\" Tooltip=\"BLINDED\">Сліпота</LSTag>, а в разі успіху — лише половини шкоди. Засліплена істота повторює кидок наприкінці кожного свого ходу, у разі успіху припиняючи ефект на собі.",
    "A burst of cold energy emanates from you in a 30-foot cone. Each creature in that area must make a Constitution saving throw. On a failed save, a creature takes cold damage and is hindered by ice formations for 1 turn. A creature hindered by ice has its speed reduced to 0. On a successful save, a creature takes half as much damage and isn’t hindered by ice.":
        "Від вас у 30-футовому конусі виривається спалах холодової енергії. Кожна істота в зоні виконує кидок протидії статурою. У разі невдачі вона зазнає холодової шкоди, а крижані нарости зменшують її швидкість до 0 на 1 хід. У разі успіху істота зазнає вдвічі менше шкоди й не скута льодом.",
    "Channel your ki into a searing wave of energy. Expel fire from your outstretched hands, hitting each target with [1] and igniting anything flammable.":
        "Спрямуйте кі в пекучу хвилю енергії. Вивільніть полум’я з простягнутих рук, завдаючи кожній цілі [1] і підпалюючи все займисте.",
    "You conjure up a wave of water that crashes down on an area within range. The area can be up to 30 feet long, up to 10 feet wide, and up to 10 feet tall. Each creature in that area must make a Dexterity saving throw. On a failed save, a creature takes 4d8 bludgeoning damage and is knocked prone. On a successful save, a creature takes half as much damage and isn’t knocked prone":
        "Ви прикликаєте хвилю, що обрушується на зону в межах досяжності завдовжки до 30 футів, завширшки до 10 футів і заввишки до 10 футів. Кожна істота в зоні виконує кидок протидії спритністю. У разі невдачі вона зазнає 4d8 дробильної шкоди й падає, а в разі успіху — вдвічі менше шкоди й не падає.",
    # Core progression and species descriptions.
    "You gain an Origin feat of your choice, or you can choose a trait from a non-Human species.":
        "Ви отримуєте рису походження на свій вибір або можете вибрати одну рису нелюдського виду.",
    "Your archdevil grants you uncanny skill in a certain form of combat. Choose one of the following illrigger combat masteries:":
        "Ваш архідиявол дарує вам надзвичайну вправність у певному виді бою. Виберіть одну з наведених нижче бойових майстерностей ілріґера:",
    """Aasimar (pronounced AH-sih-mar) are mortals who carry a spark of the Upper Planes within their souls. Whether descended from an angelic being or infused with celestial power, they can fan that spark to bring light, healing, and heavenly fury.

Aasimar can arise among any population of mortals. They resemble their parents, but they live for up to 160 years and have features that hint at their celestial heritage, such as metallic freckles, luminous eyes, a halo, or the skin color of an angel (silver, opalescent green, or coppery red). These features start subtle and become obvious when the aasimar learns to reveal their full celestial nature.""":
        """Асимари (вимовляється «а-си-мар») — смертні, у чиїх душах жевріє іскра Верхніх планів. Успадкувавши її від ангельської істоти чи отримавши разом із небесною силою, вони здатні роздмухати цю іскру, несучи світло, зцілення й небесну лють.

Асимар може народитися серед будь-якого народу смертних. Асимари схожі на своїх батьків, але живуть до 160 років і мають ознаки небесної спадщини: металеві веснянки, сяйливі очі, німб або шкіру ангельського кольору — сріблясту, опалово-зелену чи мідно-червону. Спершу ці ознаки ледь помітні, але проявляються виразніше, коли асимар учиться розкривати свою істинну небесну природу.""",
    """Dhampirs are living people who possess vampiric prowess but are cursed with macabre hunger. Most dhampirs thirst for blood, but some gain sustenance from dreams, life energy, or other vital sources. Dhampirs must choose whether to fight to control their hunger or give in to predatory urges.

Dhampirs often arise from encounters with vampires; some are the descendants of a powerful vampire, while others are partially transformed by a vampire’s bite. All manner of macabre bargains and necromantic influences might also give rise to a dhampir. Regardless of their origins, dhampirs exhibit their vampiric nature in various ways, including increased speed and a life-draining bite.""":
        """Дампіри — живі люди з вампірськими здібностями, прокляті моторошним голодом. Більшість із них жадає крові, хоча дехто живиться снами, життєвою енергією чи іншими джерелами життєвої сили. Кожен дампір мусить вирішити, чи приборкувати свій голод, чи віддатися хижацьким поривам.

Дампіри часто з’являються після зустрічей із вампірами: одні є нащадками могутнього вампіра, а інших частково перетворив вампірський укус. Причиною також можуть стати моторошна угода або некромантичний вплив. Хоч би яким було їхнє походження, вампірська природа дампірів проявляється по-різному — зокрема надзвичайною швидкістю та укусом, що висмоктує життєву силу.""",
    "You gain proficiency in one skill of your choice.":
        "Ви отримуєте володіння однією навичкою на свій вибір.",
    """Your training with weapons allows you to use weapon mastery properties.

As you reach certain levels in your class, you gain the ability to use the mastery properties of additional weapon types.""":
        """Бойова підготовка дає вам змогу застосовувати властивості майстерності зброї.

На певних рівнях класу ви опановуєте властивості майстерності додаткових типів зброї.""",
    """The other major lineage of elves in the Northlands roams the tundra and icy hills of the Bleak Expanse in small bands, hunting caribou and mammoths from the backs of reindeer and white-furred saber-toothed tigers. Ice elves are largely insular and fiercely self-sufficient. This has given them the reputation of being secretive, while the truth is more that they have little interest in the larger world. They expect no aid from outsiders, nor do they freely give it. Yet, the ice elves are sometimes willing to trade with humans, dwarves, and trollkin. Despite what ignorant outsiders believe, only a few ice elf communities worship Boreas and do his bidding, and most wish nothing to do with the malevolent deity.""":
        """Інша велика гілка ельфів Північних земель невеликими гуртами мандрує тундрою та крижаними пагорбами Похмурого простору. Вони полюють на карібу й мамонтів верхи на північних оленях і білошерстих шаблезубих тиграх. Крижані ельфи живуть відособлено й покладаються лише на себе. Через це їх вважають потайними, хоча насправді вони просто мало цікавляться зовнішнім світом. Вони не чекають допомоги від чужинців і самі не поспішають її надавати, проте іноді торгують із людьми, карликами й тролекровними. Усупереч уявленням необізнаних чужинців, лише деякі громади крижаних ельфів поклоняються Борею та виконують його волю; більшість не бажає мати нічого спільного із цим лихим божеством.""",
    "You are descended from Giants. Choose one of the following benefits—a supernatural boon from your ancestry; you can use the chosen benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest:":
        "Ви — нащадок велетнів. Виберіть одне з наведених нижче надприродних благ, успадкованих від предків. Ви можете застосувати вибране благо кількість разів, що дорівнює вашому бонусу спеціалізації, і відновлюєте всі витрачені застосування після довгого відпочинку:",
    "You have proficiency in the <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Perception\">Perception</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Survival\">Survival</LSTag> skill.":
        "Ви отримуєте володіння навичкою <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Perception\">Відчуття</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Survival\">Виживання</LSTag>.",
    """You gain the ability to twist your spells to suit your needs. Choose from the following Metamagic options.

You gain two more options at Sorcerer level 10.""":
        """Ви набуваєте здатності змінювати свої закляття відповідно до потреб. Виберіть один із наведених нижче варіантів метамагії.

На 10-му рівні чародія ви отримуєте ще два варіанти.""",
    """Towering over most folk, goliaths are distant descendants of giants. Each goliath bears the favors of the first giants—favors that manifest in various supernatural boons, including the ability to quickly grow and temporarily approach the height of goliaths’ gigantic kin.

Goliaths have physical characteristics that are reminiscent of the giants in their family lines. For example, some goliaths look like stone giants, while others resemble fire giants. Whatever giants they count as kin, goliaths have forged their own path in the multiverse—unencumbered by the internecine conflicts that have ravaged giantkind for ages—and seek heights above those reached by their ancestors.""":
        """Голіафи височіють над більшістю народів і є далекими нащадками велетнів. Кожен голіаф має дари прадавніх велетнів, що проявляються різноманітними надприродними благами — зокрема здатністю стрімко виростати й на короткий час наближатися зростом до своїх велетенських родичів.

Зовнішність голіафів нагадує велетнів із їхнього родоводу: одні схожі на кам’яних велетнів, інші — на вогняних. Хоч би кого вони вважали ріднею, голіафи проклали власний шлях у мультивсесвіті, не обтяжений міжусобицями, що споконвіку спустошують велетенський рід, і прагнуть перевершити здобутки своїх предків.""",
    """Kalashtar (pronounced kal-ASH-tar) are created from the union of humanity and renegade spirits called quori from the plane of dreams. Kalashtar appear human, but their spiritual connection affects them in a variety of ways. They have symmetrical, slightly angular features, and their eyes often glow when they are concentrating or expressing strong emotions.

Kalashtar can’t communicate directly with their quori spirits. Rather, kalashtar might experience them as a source of instinct and inspiration, drawing on the spirits’ memories when the kalashtar sleep. This connection grants kalashtar minor psionic abilities, as well as protection from psionic attacks.""":
        """Калаштари (вимовляється «кал-АШ-тар») постали із союзу людей і бунтівних духів кворі з Плану снів. Вони мають людську подобу, проте духовний зв’язок позначається на них по-різному. Їхні риси обличчя симетричні й дещо кутасті, а очі часто світяться під час зосередження або сильних емоцій.

Калаштари не можуть безпосередньо спілкуватися зі своїми духами кворі. Натомість вони відчувають їх як джерело інстинктів і натхнення та уві сні черпають зі спогадів духів. Цей зв’язок дарує калаштарам незначні псіонічні здібності й захищає від псіонічних атак.""",
    """You can infuse your seals with hellish magical power, enhancing their effects.

Some boons require a minimum Illrigger level. When you reach level 7, you gain one additional boon.""":
        """Ви можете насичувати свої печаті пекельною магією, посилюючи їхню дію.

Деякі блага потребують певного рівня ілріґера. Досягнувши 7-го рівня, ви отримуєте ще одне благо.""",
    "You may change your cantrip by selecting another one from the Wizard spell list below. This cantrip doesn't use <LSTag Tooltip=\"SpellSlot\">spell slots</LSTag> and can be cast at will.":
        "Ви можете замінити це замовляння, вибравши інше з наведеного нижче списку заклять чарівника. Це замовляння не витрачає <LSTag Tooltip=\"SpellSlot\">чарунок заклять</LSTag>, і його можна проказувати за бажанням.",
    """Found throughout the multiverse, humans are as varied as they are numerous, and they endeavor to achieve as much as they can in the years they are given. Their ambition and resourcefulness are commended, respected, and feared on many worlds.

Humans are as diverse in appearance as the people of Earth, and they have many gods. Scholars dispute the origin of humanity, but one of the earliest known human gatherings is said to have occurred in Sigil, the torus-shaped city at the center of the multiverse and the place where the Common language was born. From there, humans could have spread to every part of the multiverse, bringing the City of Doors’ cosmopolitanism with them.""":
        """Люди трапляються в усьому мультивсесвіті й так само численні, як і різноманітні. За відведені їм роки вони прагнуть досягти якомога більшого. У багатьох світах їхні честолюбство й винахідливість водночас шанують і побоюються.

Зовнішністю люди не менш різноманітні, ніж мешканці Землі, і поклоняються багатьом богам. Науковці сперечаються про походження людства, але кажуть, що одне з перших відомих людських поселень виникло в Сиґілі — тороподібному місті в центрі мультивсесвіту, де зародилася Загальна мова. Звідти люди могли розселитися по всьому мультивсесвіту, несучи із собою космополітизм Міста Дверей.""",
    # Background descriptions, editorial batch 1.
    """Feat: Savage Attacker

You are trained in battlefield tactics and combat, having served in a militia, mercenary company, or officer corps. Show smart tactics and bravery on the battlefield to enhance your prowess.""":
        """Риса: Лютий нападник

Ви опанували бойову тактику, служачи в ополченні, загоні найманців або офіцерському корпусі. Виявляйте на полі бою кмітливість і відвагу, щоб удосконалювати свою майстерність.""",
    """Feat: Tavern Brawler

You lived as a seafarer, wind at your back and decks swaying beneath your feet. You’ve perched on barstools in more ports of call than you can remember, faced mighty storms, and swapped stories with folk who live beneath the waves.""":
        """Риса: Забіяка

Ви жили мореплавством: вітер дув у спину, а палуба гойдалася під ногами. Ви засиджувалися в шинках стількох портів, що всіх і не злічити, долали могутні бурі й обмінювалися оповідками з народами, що живуть під хвилями.""",
    """Feat: Cult of the Dragon Initiate

You are an initiate of the Cult of the Dragon. You discovered or were brought to a cell cult, where you exemplified the values honored by dragon cultists: duplicity, secrecy, and determination. In exchange for your oath to serve the cult, the cult offered you the company of fellow dragon worshipers, plus access to resources that might help further your studies in the realms of arcana and occultism.

Dragon's Terror. You can take a Magic action to instill terror in a creature you can see within 30 feet of yourself. The target must succeed on a Wisdom saving throw or have the Frightened condition until the end of your next turn.

Inspired by Fear. When you cause a creature to gain the Frightened condition and you are the source of its fear, you gain Heroic Inspiration. Once you use this benefit, you can’t use it again until you finish a Short or Long Rest.""":
        """Риса: Посвячений Культу Дракона

Ви — посвячений Культу Дракона. Ви знайшли осередок культу або вас привели до нього, і там ви втілили чесноти, які шанують драконопоклонники: лукавство, потайність і рішучість. В обмін на присягу служити культові ви отримали товариство однодумців і доступ до засобів, що допомагають глибше пізнавати містику й окультизм.

Драконячий жах. Магічною дією ви можете нажахати істоту, яку бачите в межах 30 футів від себе. Ціль повинна успішно виконати кидок протидії мудрістю, інакше набуде стану переляку до кінця вашого наступного ходу.

Натхнення страхом. Коли через вас істота набуває стану переляку, ви отримуєте героїчне натхнення. Після застосування цієї переваги ви не зможете скористатися нею знову до завершення короткого або довгого відпочинку.""",
    """Feat: Alert

A wicked moment, person, or thing that cannot be slain by sword or spell haunts your mind and flickers in your peripheral vision. You carry it wherever your adventure takes you - or perhaps it carries you.""":
        """Риса: Пильність

Лиховісна мить, особа чи сутність, яку не здолати ані мечем, ані закляттям, переслідує ваші думки й мерехтить на краю зору. Ви несете її із собою, куди б не завели пригоди, — а може, це вона веде вас.""",
    """Feat: Musician

You live to sway and subvert your audience, engaging common crowds and high society alike. Preserving art and bringing joy to the hapless and downtrodden heightens your charismatic aura.""":
        """Риса: Музикант

Ви живете заради того, щоб захоплювати й бентежити публіку — від простого люду до вищого світу. Зберігаючи мистецтво та даруючи радість знедоленим і пригнобленим, ви посилюєте свою харизматичну ауру.""",
    """Feat: Magic Initiate (Druid)

Like many who hail from the Moonshae Isles, you grew up revering the blessed land, its unique gods, and the mysterious shrines called the moonwells. As a moonwell pilgrim, you undertook a quest to visit and commune with every moonwell on (or off) the map. Along your idyllic journeys, you collected a repertoire of Moonshavian folk songs, painted landscapes of enchanting vistas, and even learned how to wield a bit of primal magic.""":
        """Риса: Магічний хист: друїд

Як і багато уродженців островів Мунша, ви змалку шанували благословенну землю, її самобутніх богів і таємничі святилища — місячні криниці. Ставши прочанином місячних криниць, ви вирушили відвідати кожну з них і поспілкуватися з її силами — позначену на мапі чи приховану від світу. У цих мальовничих мандрах ви зібрали чимало муншайських народних пісень, змалювали безліч чарівних краєвидів і навіть навчилися володіти дещицею первісної магії.""",
    """Feat: Savage Attacker

You trained your whole life to become a member of the Shadowmasters, the mysterious thieves’ guild that controls the realm of Thesk from behind the scenes. Stealth and quick reflexes were just the start of your Shadowmaster education; you also needed to hone your ruthlessness to ensure the safety of the guild’s secrets. But one wrong move led to your expulsion from the order. Now you must walk your own path.""":
        """Риса: Лютий нападник

Усе життя ви готувалися вступити до Володарів тіней — таємничої гільдії злодіїв, яка нишком править Теском. Непомітність і швидкі рефлекси були лише початком навчання: вам також довелося плекати безжальність, щоб берегти таємниці гільдії. Та через один хибний крок вас вигнали з ордену. Тепер ви мусите торувати власний шлях.""",
    """Feat: Lucky

You grew up in a land of living god-kings, and as a child you were told countless stories of ancient empires and buried cities. In these tales, Mulhorand was a land overflowing with forgotten riches—priceless treasures awaiting anyone cunning and brave enough to seek them out. You’ve taken it upon yourself to explore your homeland’s crypts, tombs, and pyramids to reclaim your people’s relics.""":
        """Риса: Удача

Ви виросли в країні живих царів-богів і змалку чули незліченні оповіді про стародавні імперії та поховані міста. У них Мулгоранд поставав краєм забутих багатств — безцінних скарбів, що чекають на досить хитрих і відважних шукачів. Ви взялися досліджувати склепи, гробниці й піраміди батьківщини, щоб повернути реліквії свого народу.""",
    """Feat: Skilled

Though most youths in Chondath accept their four-year term of compulsory military service, you bristled at that authoritarian attempt to control your life. You forsook your nationhood, discarded your given name, and worked as a freebooter with the first ship that would have you. Since then, you’ve traveled the Vilhon Reach. Though you’ve never sailed more than a few dozen leagues from land, you make up for it with deep local connections and the breadth of your experiences.""":
        """Риса: Обдарований

Більшість юнаків Чондату покірно відбуває чотири роки обов’язкової військової служби, але вас обурила ця владна спроба розпоряджатися вашим життям. Ви зреклися підданства й даного при народженні імені та найнялися флібустьєром на перше судно, що погодилося вас узяти. Відтоді ви мандруєте Вілгонським краєм. Хоч ви й не відпливали від суходолу далі ніж на кілька десятків ліг, зате маєте широке коло місцевих знайомств і неабиякий життєвий досвід.""",
    """Feat: Tough

You grew up in the wilds, learning to survive far from the comforts of civilisation. Surviving unusual hazards of the wild will enhance your prowess and understanding.""":
        """Риса: Гартований

Ви виросли серед дикої природи й навчилися виживати далеко від благ цивілізації. Долайте незвичайні небезпеки пущі, щоб гартувати майстерність і поглиблювати знання.""",
    # Background descriptions, editorial batch 2.
    """Feat: Grave Keeper

In a place closer to the lands of the dead than the living, those who tend the eternal rest and disposition of the deceased are held in a mixture of high esteem and apprehension. You have plied the trade of the gravedigger, the mortician, and the embalmer. There are times when you have been the only one to say a kind word in honor of those who passed. The depredations of the Undead are well-known to you, and you don’t suffer their meddling in the rest of your charges.

Grave Keeper. You gain one use of the Channel Divinity feature from the Cleric class, and you can create the Turn Undead effect with it. If you already have Channel Divinity, you add this use to the feature from one class of your choice.""":
        """Риса: Хранитель могил

У краях, ближчих до земель мертвих, ніж живих, тих, хто дбає про вічний спокій і поховання померлих, водночас глибоко шанують і побоюються. Ви працювали могильником, трунарем і бальзамувальником. Часом лише від вас небіжчик чув останнє добре слово. Ви добре знаєте про безчинства невмерлих і не дозволяєте їм тривожити спокій своїх підопічних.

Хранитель могил. Ви отримуєте одне застосування класової особливості клірика «Боже наснаження» й можете витратити його на «Вигнання невмерлих». Якщо ви вже маєте «Боже наснаження», це застосування додається до однойменної особливості одного класу на ваш вибір.""",
    """Feat: Magic Initiate (Cleric)

You have spent your life in service to a temple, learning sacred rites and providing sacrifices to the god or gods you worship. Serving the gods and discovering their sacred works will guide you to greatness.""":
        """Риса: Магічний хист: клірик

Ви присвятили життя служінню в храмі, де вивчали священні обряди й приносили жертви богові чи богам, яким поклоняєтеся. Служіння богам і пізнання їхніх священних діянь приведе вас до величі.""",
    """Feat: Magic Initiate (Wizard)

Although genies no longer rule Calimshan, genie magic is still common in your homeland. Perhaps you inadvertently summoned a djinni from a magic lamp, or maybe you came upon an oasis guarded by a marid. A dao might have saved you from a landslide, or you bargained with an efreeti for fleeting wealth. However your fate intersected with that of a genie, the experience left you with a keen eye, a silver tongue, and more than a touch of magic.""":
        """Риса: Магічний хист: чарівник

Хоча джини більше не правлять Калімшаном, на вашій батьківщині й досі поширена їхня магія. Можливо, ви ненароком викликали джина з чарівної лампи або натрапили на оазу під охороною марида. Можливо, дао врятував вас від зсуву, а може, ви уклали угоду з іфритом заради швидкоплинного багатства. Хоч би як ваша доля перетнулася з долею джина, ця зустріч подарувала вам гостре око, красномовство й неабияку частку магії.""",
    """Feat: Lucky

You grew up on the streets surrounded by similarly ill-fated castoffs, a few of them friends and a few of them rivals. You slept where you could and did odd jobs for food. At times, when the hunger became unbearable, you resorted to theft. Still, you never lost your pride and never abandoned hope. Fate is not yet finished with you.""":
        """Риса: Удача

Ви виросли на вулиці серед таких самих знедолених вигнанців — одні стали вашими друзями, інші суперниками. Ви ночували де доведеться й перебивалися випадковими заробітками заради їжі. Коли голод ставав нестерпним, часом доводилося красти. Та ви ніколи не втрачали гідності й не полишали надії. Доля ще має на вас плани.""",
    """Feat: Zhentarim Ruffian

Maybe you needed the money. Maybe you longed for a family, no matter how dubious. Or maybe you’re just good at getting the job done by any means necessary. Whatever your reason, you enlisted with the Zhentarim, the most notorious mercenary guild in the Realms. Though the Zhentarim’s leaders insist the organization is more like a family than a shadowy syndicate, few families exhibit as much dishonesty, nepotism, and corruption as this one. You’ve honed your cunning, reflexes, and blade to climb the guild’s ranks.

Exploit Opening. When you roll damage for an Opportunity Attack, you can roll the damage dice twice and use either roll against the target.

Family First. Once per Long Rest, you grant yourself and allies within 30 feet of you Advantage on Initiative rolls.""":
        """Риса: Зентаримський головоріз

Можливо, вам були потрібні гроші. Можливо, ви прагнули мати родину — хоч би й сумнівну. А може, ви просто вмієте виконувати роботу за будь-яку ціну. Хай там як, ви вступили до Зентариму — найлиховіснішої гільдії найманців у Королівствах. Її ватажки запевняють, що організація радше родина, ніж таємний синдикат, хоча мало яка родина може похвалитися такою кількістю брехні, кумівства й корупції. Щоб піднятися в лавах гільдії, ви відточували хитрість, реакцію та свій клинок.

Скористатися нагодою. Визначаючи шкоду від Принагідної атаки, ви можете двічі кинути кістки шкоди й вибрати один із результатів проти цілі.

Родина понад усе. Один раз за довгий відпочинок ви надаєте собі та союзникам у межах 30 футів від вас перевагу на кидки ініціативи.""",
    """Feat: Alert

You come from a proud line of ice fishers out of Ten-Towns in Icewind Dale. Catching knucklehead trout isn’t the most glorious trade in the North, but it’s an honest living. You’ve trained your senses for the slightest tug on the line, wrestled big trout out of ice-covered lakes, and gutted enough knucklehead trout to feed your village many times over. These experiences have toughened your body and mind for a life of adventuring.

Stand as One. When an ally within 5 feet of you is subjected to an effect that would push or pull it, you can take a Reaction to prevent that ally from being pushed or pulled. To receive this benefit, the ally can’t have the Incapacitated condition.""":
        """Риса: Пильність

Ви походите зі славетного роду підлідних рибалок із Десятимістя в Долині Крижаного Вітру. Ловити лобату форель — не найпочесніше заняття на Півночі, зате чесне. Ви навчилися відчувати найменший рух волосіні, витягали величезних риб із укритих кригою озер і випатрали стільки форелі, що нею можна було б не раз нагодувати все селище. Цей досвід загартував ваше тіло й дух для життя шукача пригод.

Стояти разом. Коли союзник у межах 5 футів від вас зазнає ефекту, що має штовхнути або притягнути його, ви можете застосувати реагування, щоб завадити цьому переміщенню. Союзник не повинен перебувати в стані недієздатності.""",
    """Feat: Skilled

You're an expert in manipulation, prone to exaggeration and more than happy to profit from it. Bending the truth and turning allies against each other will lead to greater success down the road.""":
        """Риса: Обдарований

Ви майстер маніпуляцій, схильний до перебільшень і завжди готовий на цьому нажитися. Перекручуйте правду й нацьковуйте союзників одне на одного, щоб відкрити шлях до ще більших успіхів.""",
    """Feat: Magic Initiate (Druid)

You came of age outdoors, far from settled lands. Your home was anywhere you chose to spread your bedroll. There are wonders in the wilderness—strange monsters, pristine forests and streams, overgrown ruins of great halls once trod by giants—and you learned to fend for yourself as you explored them. From time to time, you guided friendly nature priests who instructed you in the fundamentals of channeling the magic of the wild.""":
        """Риса: Магічний хист: друїд

Ви подорослішали просто неба, далеко від обжитих земель, і домом вам було кожне місце, де можна розстелити спальник. Дика природа сповнена див: дивних чудовиськ, незайманих лісів і струмків, порослих руїн величних зал, якими колись ходили велетні. Досліджуючи їх, ви навчилися покладатися на себе. Час від часу ви супроводжували приязних жерців природи, а вони навчали вас основ спрямування магії пущі.""",
    """Feat: Skilled

You were raised in a family among the social elite, accustomed to power and privilege. Accumulating renown, power, and loyalty will raise your status.""":
        """Риса: Обдарований

Ви виросли в родині, що належала до суспільної верхівки й звикла до влади та привілеїв. Здобувайте славу, вплив і відданих прибічників, щоб підвищувати свій статус.""",
    """Feat: Healer

You spent your early years secluded in a hut or monastery located well beyond the outskirts of the nearest settlement. In those days, your only companions were the creatures of the forest and those who would occasionally visit to bring news of the outside world and supplies. The solitude allowed you to spend many hours pondering the mysteries of creation.""":
        """Риса: Цілитель

Ранні роки ви провели на самоті в хатині чи монастирі далеко за межами найближчого поселення. Тоді вашим товариством були лише лісові створіння та рідкісні відвідувачі, які приносили припаси й новини із зовнішнього світу. Самотність подарувала вам безліч годин для роздумів над таємницями творіння.""",
    # Background descriptions, editorial batch 3.
    """Feat: Magic Initiate (Wizard)

You are curious and well-read, with an unending thirst for knowledge. Learning about rare lore of the world will inspire you to put this knowledge to greater purpose.""":
        """Риса: Магічний хист: чарівник

Ви допитливі, начитані й маєте невситиму жагу до знань. Пізнаючи рідкісні таємниці світу, ви надихаєтеся застосовувати ці знання заради вищої мети.""",
    """Feat: Tough

You spent years wandering the highlands of Rashemen, a dangerous windswept heath that’s dotted with ancient obelisks enchanted to imprison Fiends and home to dragons, gnolls, and other deadly creatures. Friendships are hard to find in such an isolated land, and you’ve learned to keep strangers at a distance.""":
        """Риса: Гартований

Роками ви мандрували високогір’ям Рашемену — небезпечними вітряними пустищами, де стародавні зачаровані обеліски ув’язнюють нечистих, а поміж ними живуть дракони, гноли та інші смертоносні створіння. У такому відлюдному краї нелегко знайти друзів, тож ви навчилися не підпускати чужинців надто близько.""",
    """Feat: Tough

The chief law enforcement branch of Baldur’s Gate is the Flaming Fist, a brawny mercenary guild led by the city’s grand duke. You once served as a Flaming Fist, where you learned how to preempt trouble with your intimidating stare and, when necessary, absorb deadly blows. Flaming Fist mercenaries, active or retired, are known as some of the toughest, most resilient warriors along the Sword Coast, and you seek to maintain that reputation.""":
        """Риса: Гартований

Головна правоохоронна сила Брами Балдура — «Полум’яний кулак», могутня гільдія найманців під проводом великого герцога міста. Колись ви служили в її лавах і навчилися відвертати лихо одним грізним поглядом, а за потреби — витримувати смертоносні удари. Чинні й колишні найманці «Полум’яного кулака» відомі як одні з найвитриваліших воїнів Узбережжя Мечів, і ви прагнете бути гідними цієї слави.""",
    """Feat: Savage Attacker

After surviving a poor and bleak childhood, you know how to make the most out of very little. Using your street smarts bolsters your spirit for the journey ahead.""":
        """Риса: Лютий нападник

Переживши злиденне й похмуре дитинство, ви навчилися здобувати максимум із мізерних можливостей. Вулична кмітливість додає вам духу в прийдешніх мандрах.""",
    """Feat: Healer

The dead magic zones of the Anauroch desert are anathema to spellcasters and monsters that rely on magic—which is exactly why you made your life there. Perhaps you’re on the run from Red Wizards, or you ran afoul of a powerful djinni in Calimshan. Whatever the case, you decided that living in Anauroch was your best option. After long months or years, you’re stronger, wiser, and armed with hard-earned knowledge of desert medicine and wasteland survival.""":
        """Риса: Цілитель

Зони мертвої магії в пустелі Анаурох згубні для заклиначів і чудовиськ, що покладаються на магію, — саме тому ви там оселилися. Можливо, ви переховуєтеся від Червоних чарівників або перейшли дорогу могутньому джинові в Калімшані. Хай там як, життя в Анауроху було найкращим із доступних варіантів. За довгі місяці чи роки ви стали сильнішими й мудрішими та важкою працею здобули знання пустельної медицини й виживання на пустищах.""",
    """Feat: Skilled

You spent formative years in a scriptorium, a monastery dedicated to the preservation of knowledge, or a government agency, where you learned to write with a clear hand and produce finely written texts. Perhaps you scribed government documents or copied tomes of literature. You might have some skill as a writer of poetry, narrative, or scholarly research. Above all, you have a careful attention to detail, helping you avoid introducing mistakes to the documents you copy and create.""":
        """Риса: Обдарований

Роки становлення ви провели в скрипторії, монастирі, присвяченому збереженню знань, або державній установі. Там ви виробили чіткий почерк і навчилися складати вишукані тексти. Можливо, ви переписували урядові документи чи літературні фоліанти, а також маєте хист до поезії, прози або наукових праць. Передусім ви надзвичайно уважні до подробиць, тому рідко припускаєтеся помилок у документах, які переписуєте чи створюєте.""",
    """Feat: Tyro of the Gauntlet

Not all who answer the call of a higher power are content to pore over scripture in a stuffy temple apse. You chose the path of the holy warrior by joining the Order of the Gauntlet. As a knight of the Gauntlet, you exercise righteous scorn for the forces of evil, unswerving camaraderie for your siblings in arms, and heartfelt compassion for the survivors of war. With weapon and holy symbol in hand, you’ve sworn not to rest until the light of justice has vanquished the shadow of chaos across Faerûn.""":
        """Риса: Неофіт Рукавиці

Не всі, хто відгукнувся на поклик вищої сили, ладні вдовольнятися вивченням писань у задушливій храмовій апсиді. Вступивши до Ордену Рукавиці, ви обрали шлях святого воїна. Як лицар Рукавиці, ви праведно зневажаєте сили зла, непохитно підтримуєте побратимів і щиро співчуваєте жертвам війни. Зі зброєю та святим символом у руках ви заприсяглися не спочивати, доки світло справедливості не здолає тінь хаосу в усьому Фаеруні.""",
    """Feat: Purple Dragon Rook

You’ve pledged your life to the safety of Cormyr and sought admission to that realm’s order of elite warriors: the Purple Dragon Knights. But before you have the chance to join the ranks officially, you must first serve as a knight’s squire. You’ve found a liege willing to take you on and teach you the order’s ways. Will you uphold the Purple Dragon Knights’ ideals of glory, honor, and strength and prove yourself worthy of knighthood?

Entreat. You gain proficiency in <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>.

Rallying Cry. You can choose a number of creatures equal to your Proficiency Bonus that you can see within 30 feet of yourself. Those creatures gain Heroic Inspiration. Once you use this benefit, you can’t do so again until you finish a Long Rest.""":
        """Риса: Тура Пурпурного Дракона

Ви присвятили життя безпеці Корміру й прагнете вступити до ордену його добірних воїнів — Лицарів Пурпурного Дракона. Та перш ніж офіційно долучитися до їхніх лав, ви мусите послужити лицарським зброєносцем. Ви знайшли зверхника, готового взяти вас на службу й навчити звичаїв ордену. Чи збережете ви вірність ідеалам слави, честі й сили та доведете, що гідні лицарського звання?

Прохання. Ви отримуєте володіння навичкою <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag>.

Бойовий клич. Виберіть видимих вам істот у межах 30 футів від себе в кількості, що дорівнює вашому бонусу спеціалізації. Вони отримують героїчне натхнення. Після застосування цієї переваги ви не зможете скористатися нею знову до завершення довгого відпочинку.""",
    """Feat: Charm Twister

You know the ancient rites kept alive by secretive druids and hedge practitioners in the shadowed groves of the primordial forests. Remedies and hexes woven into wicker charms can stave off misfortune and ward away evil. They could just as likely invite gloom and the ire of the old spirits.

Charm Twister. You always have the Bless and Hex spells prepared. In addition, you gain one 1st-level spell slot that can be used to cast them.""":
        """Риса: Плетільник оберегів

Ви знаєте стародавні обряди, які потайні друїди й сільські знахарі зберігають у тінистих гаях прадавніх лісів. Цілющі чари й прокляття, вплетені в плетені обереги, здатні відвернути лихо й відігнати зло. Утім, вони так само легко можуть накликати морок і гнів давніх духів.

Плетільник оберегів. У вас завжди підготовлені закляття «Благословення» та «Прокляття». Крім того, ви отримуєте одну чарунку заклять 1-го рівня, яку можете витратити на проказування цих заклять.""",
    """Feat: Spellfire Spark

You bear the gift of spellfire: a rare form of magic that channels the raw power of the Weave. Wielding spellfire takes a heavy toll on the body. You’ve trained both mind and body to efficiently wield this sacred power.

Magic Absorption. Once per turn, when you take damage from a spell or magical effect, you reduce the total damage taken by 1d4.

Spellfire Flame. You learn the Sacred Flame cantrip. You can also cast this cantrip as a Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.""":
        """Риса: Іскра чаровогню

Ви несете дар чаровогню — рідкісної магії, що спрямовує первісну силу Плетіння. Чаровогонь виснажує тіло, тому ви загартували тіло й розум, щоб вправно володіти цією священною силою.

Поглинання магії. Один раз за хід, коли ви зазнаєте шкоди від закляття чи магічного ефекту, зменште загальну отриману шкоду на 1d4.

Полум’я чаровогню. Ви вивчаєте замовляння «Священний вогонь». Крім того, ви можете проказати його вторинною дією кількість разів, що дорівнює вашому бонусу спеціалізації. Усі витрачені застосування відновлюються після довгого відпочинку.""",
    # Background descriptions, editorial batch 4.
    """Feat: Emerald Enclave Fledgling

As a Caretaker with the Emerald Enclave, you take care of those who care for the world. Either alongside your fellow Emerald Enclave members or by yourself, you’ve learned essential skills for living with the land: how to track game, where to forage for useful herbs, and even how to forecast the weather. You use these talents to maintain the balance between civilization and the wilds and to rid the world of unnatural creatures.

Speak with Animals. You always have the Speak with Animals spell prepared and can cast it with any spell slots you have.

Tag Team. When you take the Help action, you can switch places with a willing ally within 5 feet of yourself as part of that same action. This movement doesn’t provoke Opportunity Attacks.""":
        """Риса: Початківець Смарагдового Анклаву

Як доглядач Смарагдового Анклаву ви піклуєтеся про тих, хто береже світ. Разом з іншими членами Анклаву чи самотужки ви опанували життєво важливі вміння: вистежувати дичину, знаходити корисні трави й навіть передбачати погоду. Завдяки цим талантам ви підтримуєте рівновагу між цивілізацією та пущею й очищаєте світ від неприродних створінь.

Розмова з тваринами. У вас завжди підготовлене закляття «Розмова з тваринами», і ви можете проказувати його, витрачаючи будь-які наявні чарунки заклять.

Злагоджена пара. Виконуючи дію «Допомога», ви можете в межах цієї самої дії помінятися місцями з охочим союзником у межах 5 футів від вас. Таке переміщення не провокує Принагідних атак.""",
    """Feat: Altered

You are forever altered in some drastic, physical way, perhaps even made monstrous. A blasphemous fusion of science, alchemy, and magic changed you, possibly to mend some unrecoverable malady, or to test the limits of your biology. The process was a success, at least to a point, but the change left its mark on you. The indelible warping of your form can be a source of fear for those who do not understand what they see.

Altered. You gain natural armor (AC 10 + Dexterity and Constitution modifiers), natural weapons (1d6 unarmed strikes), and darkvision out to 60 feet (or +30 feet if you already have it).""":
        """Риса: Змінений

Ваше тіло назавжди зазнало докорінної зміни, яка, можливо, навіть зробила вас чудовиськом. Блюзнірське поєднання науки, алхімії й магії перетворило вас — чи то задля лікування невиліковної недуги, чи то для випробування меж вашої природи. Принаймні почасти дослід удався, але залишив на вас незгладимий слід. Незворотне спотворення подоби може лякати тих, хто не розуміє побаченого.

Змінений. Ви отримуєте природний захист (РЗ 10 + модифікатори спритності й статури), природну зброю (1d6 шкоди від беззбройних ударів) і темнозір на 60 футів (або ще на 30 футів, якщо вже його маєте).""",
    """Feat: Lords’ Alliance Agent

You’ve pledged your loyalty to a member-city of the Lords’ Alliance. As an Alliance agent, you must uphold the tenets of the Alliance and seek to increase safety and prosperity along the Sword Coast. You’re sworn to bring honor and glory to your lord’s house, whether that means securing trade roads for a merchant-lord of Waterdeep or vanquishing monsters upriver of Daggerford. You’ve trained in the arts of swordplay and statecraft and are as deft with a blade as you are with a quill.

Inspiring Strike. Once per turn when you score a Critical Hit against a creature, you gain Heroic Inspiration.

Reassert Honor. When an enemy you can see deals damage to you, you have Advantage on your next attack roll against that enemy before the end of your next turn.""":
        """Риса: Агент Альянсу лордів

Ви присягнули на вірність одному з міст Альянсу лордів. Як агент Альянсу ви мусите дотримуватися його засад і зміцнювати безпеку та добробут Узбережжя Мечів. Ви заприсяглися принести честь і славу дому свого лорда — чи то охороняючи торгові шляхи вотердіпського купця-лорда, чи то винищуючи чудовиськ вище за течією від Дагерфорда. Ви опанували фехтування й державне ремесло, тож однаково вправно володієте клинком і пером.

Надихальний удар. Один раз за хід, коли ви завдаєте істоті критичного влучання, ви отримуєте героїчне натхнення.

Відновлення честі. Коли видимий вам ворог завдає вам шкоди, ви отримуєте перевагу на свій наступний кидок атаки проти нього до кінця свого наступного ходу.""",
    """Feat: Alert

You have a history of breaking the law and survive by leveraging less-than-legal connections. Profiting from criminal enterprise will lead to greater opportunities in the future.""":
        """Риса: Пильність

Ви не раз порушували закон і виживаєте завдяки сумнівним зв’язкам. Наживайтеся на злочинних оборудках, щоб у майбутньому відкривати ще ширші можливості.""",
    """Feat: Skilled

Your skill in a particular craft has earned you membership in a mercantile guild, offering privileges and protection while engaging in your art. Repairing and discovering rare crafts will bring new inspiration.""":
        """Риса: Обдарований

Майстерність у певному ремеслі принесла вам членство в купецькій гільдії, а разом із ним — привілеї та захист під час роботи. Відновлюйте рідкісні вироби й відкривайте забуті ремесла, щоб черпати нове натхнення.""",
    """Feat: Tough

You're a champion of the common people, challenging tyrants and monsters to protect the helpless. Saving innocents in imminent danger will make your legend grow.""":
        """Риса: Гартований

Ви — захисник простого люду, який кидає виклик тиранам і чудовиськам заради безпорадних. Рятуйте невинних від неминучої загибелі, щоб примножувати свою славу.""",
    """Feat: Harper Agent

You accepted an invitation to join the Harpers, pledging an oath to uphold the Harper code and act in service to the common good. Like all Harpers, you understand the value of teamwork as well as when it’s best to go it alone. Harper veterans have taught you the order’s secrets—magical melodies, special watchwords, and legerdemain—and have entrusted you to use such knowledge to surveil and undermine the forces of evil.

Instrument Training. You gain proficiency with Musical Instruments.

Distracting Melody. When you take the Distract action to assist an ally’s attack roll, the enemy you’re distracting can be within 30 feet of you, rather than within 5 feet of you, provided the enemy can see or hear you.""":
        """Риса: Агент Арфістів

Ви прийняли запрошення вступити до Арфістів, присягнувши дотримуватися їхнього кодексу й служити спільному благу. Як і всі Арфісти, ви розумієте цінність командної роботи та знаєте, коли краще діяти самотужки. Ветерани відкрили вам таємниці ордену — магічні мелодії, особливі паролі й хитромудрі трюки — та доручили застосовувати ці знання для стеження за силами зла й підриву їхніх планів.

Гра на інструментах. Ви отримуєте володіння музичними інструментами.

Відволікальна мелодія. Коли ви виконуєте дію «Відволікти», щоб допомогти союзникові з кидком атаки, ворог може перебувати в межах 30 футів від вас замість 5 футів, якщо бачить або чує вас.""",
    """Feat: Lucky

You were apprenticed to a trader, caravan master, or shopkeeper, learning the fundamentals of commerce. You traveled broadly, and you earned a living by buying and selling the raw materials artisans need to practice their craft or finished works from such crafters. You might have transported goods from one place to another (by ship, wagon, or caravan) or bought them from traveling traders and sold them in your own shop.""":
        """Риса: Удача

Ви були учнем купця, караванника чи крамаря й опановували основи торгівлі. Ви багато мандрували й заробляли на життя, купуючи та продаючи сировину для ремісників і готові вироби майстрів. Можливо, ви перевозили товари кораблем, возом або караваном чи купували їх у мандрівних торговців, а потім продавали у власній крамниці.""",
    """Feat: Lucky

Mythals are sources of great magical power that can alter the Weave or even the very nature of reality. Most were constructed in antiquity, and many have since been damaged or gone dormant. As a mythalkeeper from the Dalelands, your first experience with a mythal was likely in the ruins of Myth Drannor. You roam Faerûn in search of other ruined places of power, hoping to learn more about the history and powers of mythals—or even restore a malfunctioning one.""":
        """Риса: Удача

Міфали — джерела величезної магічної сили, здатні змінювати Плетіння й навіть саму природу реальності. Більшість із них створили в давнину, а згодом чимало пошкодили або вони згасли. Як хранитель міфалів із Долинних земель, ви, найімовірніше, вперше зустріли міфал серед руїн Міф-Драннора. Ви мандруєте Фаеруном у пошуках інших зруйнованих осередків сили, сподіваючись більше дізнатися про історію й могутність міфалів або навіть відновити один із пошкоджених.""",
    """Feat: Tough

You grew up close to the land. Years tending animals and cultivating the earth rewarded you with patience and good health. You have a keen appreciation for nature’s bounty alongside a healthy respect for nature’s wrath.""":
        """Риса: Гартований

Ви виросли в тісному зв’язку із землею. Роки догляду за тваринами й обробітку ґрунту подарували вам терпіння та міцне здоров’я. Ви щиро цінуєте щедрість природи й водночас належно поважаєте її гнів.""",
    # Class and subclass descriptions, editorial batch 1.
    """An alien influence has wrapped its tendrils around your mind, giving you psionic power. You can now touch other minds with that power and alter the world around you. Will this power shine from you as a hopeful beacon to others? Or will you be a terror to those who feel the stab of your mind?

Perhaps a psychic wind from the Astral Plane carried psionic energy to you, or you were exposed to the Far Realm’s warping influence. Alternatively, you were implanted with a mind flayer tadpole, but your transformation into a mind flayer never occurred; now the tadpole’s psionic power is yours. However you acquired this power, your mind is aflame with it.""":
        """Чужинний вплив обплів ваш розум і наділив вас псіонічною силою. Тепер нею ви можете торкатися чужих думок і змінювати світ довкола. Чи засяє ця сила маяком надії для інших? Або ви станете жахом для кожного, хто відчує укол вашої свідомості?

Можливо, псіонічну енергію приніс вам ментальний вітер з Астрального плану або вас спотворив вплив Далекої царини. А може, у вас підселили пуголовка мізкожера, але перетворення так і не сталося — і тепер псіонічна сила паразита належить вам. Хоч би як ви здобули цей дар, ваш розум палає ним.""",
    "Your study of magic is focused on spells that block, banish, or protect—ending harmful effects, banishing evil influences, and protecting the weak. Abjurers are sought when baleful spirits require exorcism, when locations must be guarded against magical spying, and when portals to other planes of existence must be closed. Adventuring parties value Abjurers for the protection they provide against a variety of hostile magic and other attacks.":
        "Ви зосередилися на закляттях, що блокують, виганяють і захищають: припиняють шкідливі ефекти, віднаджують злі сили та боронять слабких. Віднаджувачів кличуть, коли треба вигнати згубних духів, убезпечити місце від магічного стеження або закрити портал до іншого плану буття. Загони шукачів пригод цінують їх за захист від ворожої магії та інших нападів.",
    "An Alchemist is an expert at combining reagents to produce magical effects. Alchemists use their creations to give life and to leech it away.":
        "Алхіміки вправно поєднують реагенти, створюючи магічні ефекти. Своїми витворами вони можуть як дарувати життя, так і висмоктувати його.",
    """Few gods embrace the Apocalypse Domain, yet in times of war, disease, or social upheaval, its Clerics appear at the head of grim cults that proclaim the world’s imminent demise. Devotes of the Apocalypse Domain are usually apostates and heretics cast from religious orders for their fanatical conviction to the end of all things.

The exact origin of their divine power confounds the elders of established religions. Sometimes, these Clerics derive their powers from the gods of fate, doom, or change. More often, though, they seem to draw their power from the collective gloom of a population facing disaster. Perhaps the world’s demise is truly imminent, and these visionaries have found some way to tap into the apocalypse as it grows near.""":
        """Мало хто з богів визнає Домен апокаліпсису, проте за часів війни, мору чи суспільних потрясінь його клірики очолюють похмурі культи, що провіщають близьку загибель світу. Прибічники цього домену зазвичай є відступниками та єретиками, вигнаними з релігійних орденів за фанатичну віру в кінець усього сущого.

Старійшини усталених релігій не можуть збагнути походження їхньої божественної сили. Іноді ці клірики отримують її від богів долі, загибелі чи змін, але частіше, здається, черпають із колективного відчаю народу перед катастрофою. Можливо, кінець світу й справді близько, а ці провидці навчилися торкатися сили прийдешнього апокаліпсиса.""",
    "Your pact draws on the power of the Feywild. When you choose this subclass, you might make a deal with an archfey, such as the Prince of Frost; the Queen of Air and Darkness, ruler of the Gloaming Court; Titania of the Summer Court; or an ancient hag. Or you might call on a spectrum of Fey, weaving a web of favors and debts. Whoever they are, your patron is often inscrutable and whimsical.":
        "Сила вашого договору походить із Феєлону. Обравши цей підклас, ви могли укласти угоду з архіфеєю — наприклад, Принцом Морозу, Королевою Повітря і Темряви з Похмурого двору, Титанією з Літнього двору або прадавньою каргою. А може, ви звернулися до багатьох фей, сплівши павутину послуг і боргів. Хай ким є ваш покровитель, його наміри здебільшого незбагненні, а вдача — примхлива.",
    """Architects of Ruin are cool and calculating arcane knights who serve Asmodeus, deploying spells, steel, and subterfuge to win at any cost.

Asmodeus rules Acheron, the City of Fear. His illriggers scour the timescape, collecting secrets and spells designed to deceive and terrify his opponents. The war he fights against the other archdevils is one of deception and information.

His Architects of Ruin work to make Hell’s enemies seem outnumbered and outmaneuvered. These illriggers are skillful spellblades on the battlefield, though some employ tactics such as research, infiltration, and propaganda to play mind games with their quarry. When an Architect of Ruin finally confronts an enemy, the advantage is theirs—they have studied, prepared, and gripped fate within their gauntlet, forcing it to favor them. They hungrily seek the dark arts to arm both themselves and Asmodeus with the impossible.""":
        """Архітектори Руїни — холоднокровні й розважливі містичні лицарі Асмодея, які заради перемоги за будь-яку ціну застосовують закляття, сталь та обман.

Асмодей править Ахероном, Містом Страху. Його ілріґери нишпорять часовими просторами, збираючи таємниці й закляття, покликані ошукувати та жахати супротивників. Його війна з іншими архідияволами — це війна брехні та відомостей.

Архітектори Руїни прагнуть, щоб вороги Пекла почувалися оточеними й переграними. На полі бою ці ілріґери вправно поєднують клинок із чарами, а дехто вдається до досліджень, проникнення й пропаганди, щоб вести психологічну гру зі здобиччю. Коли Архітектор Руїни нарешті постає перед ворогом, перевага вже на його боці: він усе вивчив, підготувався і стиснув долю в латній рукавиці, змусивши її сприяти собі. Вони жадібно шукають темних мистецтв, щоб озброїти себе й Асмодея неможливим.""",
    "An Armorer modifies armor to function almost like a second skin. The armor is enhanced to hone the Armorer’s magic, unleash potent attacks, and generate a formidable defense.":
        "Броняр переробляє обладунки так, щоб вони стали майже другою шкірою. Посилений обладунок зосереджує магію броняра, дає змогу здійснювати потужні атаки й забезпечує надійний захист.",
    "Masters of invention, Artificers use ingenuity and magic to unlock extraordinary capabilities in objects. They see magic as a complex system waiting to be decoded and then harnessed in their spells and inventions.":
        "Винахідники — майстри новаторства, які завдяки кмітливості й магії відкривають надзвичайні можливості звичайних предметів. Вони сприймають магію як складну систему, що чекає на розшифрування й застосування у закляттях і винаходах.",
    "An Artillerist specializes in using magic to hurl energy, projectiles, and explosions on a battlefield.":
        "Артилерист спеціалізується на магії, що обрушує на поле бою енергію, снаряди й вибухи.",
    "Gods of the Astral Plane are as lost to time and space as the realm they reign over. The Astral Plane fills the gaps between the planes of existence and is an important balancing force in the cosmic ecosystem of the multiverse. Practitioners of this domain see the absence of anything as something and consider the Astral Plane as the ultimate destination of all things. These acolytes follow the ultimate path to their destination, and help shepherd others along their way in a grand mission of entropy. Clerics of the Astral Domain are chaotic by nature, but typically choose to destroy evil where they find it and hasten its inevitable journey to the Astral Plane.":
        "Боги Астрального плану так само загублені в часі й просторі, як і царство, яким вони правлять. Астральний план заповнює проміжки між планами буття й підтримує рівновагу в космічній екосистемі мультивсесвіту. Прихильники цього домену вбачають присутність у самій відсутності й вважають Астральний план остаточним призначенням усього сущого. Вони йдуть до цієї кінцевої мети й супроводжують інших у величній місії ентропії. Клірики Астрального домену хаотичні за природою, але зазвичай винищують зло, де б його не зустріли, прискорюючи його неминучу подорож до Астрального плану.",
    # Class and subclass descriptions, editorial batch 2.
    """Bannerets are paragons of valor and leadership who protect the innocent and rally fellow adventurers to the causes of justice and freedom. Many are knights serving in Cormyr, the Silver Marches, Damara, Chessenta, or other lands across Faerûn. They wander the realms as knights errant, taking the fight against evil beyond their kingdom’s borders.

A Banneret relies on judgment, bravery, and fidelity to the code of chivalry to guide them in defeating evildoers. A lone Banneret is a skilled warrior, but when leading a band of allies one of these warriors can transform even a poorly equipped militia into a ferocious war band.""":
        """Банерети — взірці звитяги й провідництва, які захищають невинних і згуртовують шукачів пригод заради справедливості та свободи. Багато з них служать лицарями в Кормірі, Срібних Маршах, Дамарі, Чессенті та інших землях Фаеруну. Вони мандрують світом як лицарі без володінь і б’ються зі злом далеко за межами рідних королівств.

У боротьбі з лиходіями банерет покладається на розсудливість, відвагу й вірність лицарському кодексу. Наодинці це вправний воїн, але на чолі союзників він здатний перетворити навіть погано споряджене ополчення на грізний бойовий загін.""",
    "A Battle Smith is a combination of protector and medic, an expert at defending others and repairing both materiel and personnel. To aid in their work, Battle Smiths are accompanied by a Steel Defender, a protective companion of their own creation.":
        "Бойовий коваль поєднує ролі захисника й цілителя: боронить інших і лагодить як спорядження, так і живих соратників. У цьому йому допомагає Сталевий захисник — створений власноруч вірний охоронець.",
    "Barbarians who walk the Path of the Berserker direct their <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> primarily toward violence. Their path is one of untrammeled fury, and they thrill in the chaos of battle as they allow their <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> to seize and empower them.":
        "Варвари Шляху берсерка спрямовують свою <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag> передусім на насильство. Це шлях неприборканої ярості: вони впиваються хаосом битви й дозволяють <LSTag Type=\"Status\" Tooltip=\"RAGE\">Люті</LSTag> опанувати та зміцнити їх.",
    """The Blades of Radiance, also known as Steel Saints, are among the most lethal orders of the Church. To become a blade, one must be a devout follower of the faith, for only those willing to die for the cause are deemed worthy. Prospective members are trained within the Church’s walls, taking the clergy as their new kin and discarding whatever familial bonds they once held. Their zealous fervor grants them unrivaled power on the battlefield, wielding massive weapons as if they were toys, infusing their blades with divine energy, and breaking their foes one by one.

The Blades of Radiance undertake an incredibly diverse range of missions. The most brutal members handle gruesome matters with lethal precision, while those of a more empathetic temperament protect their fellows. Despite their differences, all share a single goal: safeguarding the Church and its members, no matter the cost.""":
        """Клинки Сяйва, відомі також як Сталеві святі, належать до найсмертоносніших орденів Церкви. Клинком може стати лише ревний послідовник віри, готовий померти за її справу. Майбутніх членів навчають у стінах Церкви; духовенство стає їхньою новою родиною, а всі колишні родинні зв’язки вони відкидають. Фанатичний запал дарує їм неперевершену міць у бою: вони орудують велетенською зброєю, наче іграшкою, насичують клинки божественною енергією й ламають ворогів одного за одним.

Клинки Сяйва виконують найрізноманітніші доручення. Найжорстокіші з них зі смертоносною точністю беруться за криваві справи, а співчутливіші захищають побратимів. Попри відмінності, усіх єднає одна мета: за будь-яку ціну боронити Церкву та її вірян.""",
    """Bladesingers master a tradition of wizardry that incorporates swordplay and dance. In combat, a Bladesinger uses intricate, elegant maneuvers that fend off harm and allow the Bladesinger to channel magic into devastating attacks and a cunning defense. Many who have observed a Bladesinger at work remember the display as one of the more beautiful experiences in their life—a glorious dance accompanied by a singing blade.

Bladesinging is associated with the ancient elven societies that first mastered the art and coined the term. Even today, most Bladesingers still hail from old elven realms, such as Myth Drannor, or from non-elven societies that share land and history with elves, such as the Silver Marches. Wherever they hail from, Bladesingers take their talents all across the Realms to help common people and perform heroic deeds. Most communities greet the arrival of a Bladesinger as a good omen.""":
        """Співці клинка опановують чарівницьку традицію, що поєднує фехтування й танець. У бою вони виконують складні та вишукані рухи, які відвертають шкоду й спрямовують магію в нищівні атаки та хитромудрий захист. Багато хто з очевидців називає цей величний танець під спів клинка одним із найпрекрасніших видовищ у своєму житті.

Спів клинка пов’язаний із прадавніми ельфійськими народами, що першими опанували й назвали це мистецтво. Навіть нині більшість його майстрів походить зі старих ельфійських царств на кшталт Міф-Драннора або з неельфійських земель, які поділяють з ельфами історію, як-от Срібні Марші. Хоч би де вони народилися, співці клинка мандрують Королівствами, допомагають простим людям і чинять героїчні діяння. У більшості громад їхню появу вважають доброю прикметою.""",
    """Since the beginning of time, the brave glared into danger’s ferocious eyes and fought monsters. Those who survived were the ones smart enough to arm themselves properly and know precisely where to strike—or those who knew when to flee and return with a new plan.

Members of the Carver Guild are the Monster Hunters typically called upon when immediate danger threatens a settlement and there is no army or militia available. Carvers stride unflinchingly toward death, armed with years of training and the knowledge passed down from those before them.""":
        """Від початку часів сміливці вдивлялися в люті очі небезпеки й билися з чудовиськами. Виживали ті, кому ставало розуму належно озброїтися й точно знати, куди бити, — або вчасно відступити й повернутися з новим планом.

Членів Гільдії різьбярів зазвичай кличуть, коли поселення опиняється в безпосередній небезпеці, а війська чи ополчення поблизу немає. Ці мисливці на чудовиськ незворушно крокують назустріч смерті, озброєні роками підготовки та знаннями попередників.""",
    "Cavalier excels at mounted combat. Usually born among the nobility and raised at court, a Cavalier is equally at home leading a cavalry charge or exchanging repartee at a state dinner. Cavaliers also learn how to guard those in their charge from harm, often serving as the protectors of their superiors and of the weak. Compelled to right wrongs or earn prestige, many of these fighters leave their lives of comfort to embark on glorious adventure.":
        "Кавалер неперевершений у кінному бою. Зазвичай народжений у шляхетній родині й вихований при дворі, він однаково впевнено очолює кавалерійську атаку й обмінюється дотепами на державній вечері. Кавалери також учаться захищати своїх підопічних, часто стаючи охоронцями можновладців і слабких. Прагнучи виправити кривду чи здобути славу, багато таких бійців полишають затишне життя заради величних пригод.",
    "Your pact draws on the Upper Planes, the realms of everlasting bliss. You might enter an agreement with an empyrean, a couatl, a sphinx, a unicorn, or another heavenly entity. Or you might call on numerous such beings as you pursue goals aligned with theirs. Your pact allows you to experience a hint of the holy light that illuminates the multiverse.":
        "Сила вашого договору походить із Верхніх планів — царств вічного блаженства. Ви могли укласти угоду з емпіреєм, куатлем, сфінксом, єдинорогом чи іншим небесником або звернутися одразу до багатьох таких істот заради спільної мети. Завдяки договору ви відчуваєте частку святого світла, що осяває мультивсесвіт.",
    """The Circle of Dragons is an old order of druids steeped in rigid tradition. These honor-bound wardens of nature and draconic heritage are members of a secret society that have influenced governance, war, and culture across the world. High-standing members of this Circle have ties to royal bloodlines that date back generations, a connection that’s subtly showcased in royal family crests and insignia.

Druids from this Circle know that dragons, and draconic magic, are as connected to the world as plants or beasts, and utilize that connection to transform into a unique and powerful draconic form all their own.""":
        """Коло Драконів — стародавній орден друїдів, відданий суворим традиціям. Ці зв’язані честю вартові природи й драконячої спадщини належать до таємного товариства, яке впливало на владу, війни й культуру в усьому світі. Високопоставлені члени Кола мають давні зв’язки з королівськими родами, непомітно відображені в їхніх гербах і відзнаках.

Друїди цього Кола знають, що дракони та їхня магія пов’язані зі світом не менше за рослини чи звірів. Завдяки цьому зв’язку кожен із них набуває власної неповторної та могутньої драконячої подоби.""",
    "Druids who are members of the Circle of Dreams hail from regions that have strong ties to the Feywild and its dreamlike realms. The druids’ guardianship of the natural world makes for a natural alliance between them and good-aligned fey. These druids seek to fill the world with dreamy wonder. Their magic mends wounds and brings joy to downcast hearts, and the realms they protect are gleaming, fruitful places, where dream and reality blur together and where the weary can find rest.":
        "Друїди Кола Мрій походять із країв, тісно пов’язаних із Феєлоном та його сновидними царствами. Захист природи природно зближує їх із доброзичливими феями. Ці друїди прагнуть сповнити світ дивами, подібними до снів. Їхня магія загоює рани й приносить радість засмученим серцям, а підзахисні землі сяють і квітнуть — там сон зливається з дійсністю, а стомлені знаходять спочинок.",
    # Class and subclass descriptions, editorial batch 3.
    "Druids of the Circle of the Sea draw on the tempestuous forces of oceans and storms. Some view themselves as embodiments of nature’s wrath, seeking vengeance against those who despoil nature. Others seek mystical unity with nature by attuning themselves to the ebb and flow of the tides, following the rush of currents and waves and listening to the inscrutable whispers and roars of the winds.":
        "Друїди Кола Моря черпають із бурхливої сили океанів і штормів. Дехто вважає себе втіленням гніву природи й мститься тим, хто її спаплюжує. Інші прагнуть містичної єдності з природою: налаштовуються на ритм припливів і відпливів, ідуть за течіями та хвилями й дослухаються до незбагненних шепоту та ревіння вітрів.",
    """The Unbroken Circle is an order of Druids who have abandoned the patient teachings of their predecessors, deciding instead to take up arms in defense of the wilderness. These combative Druids form militias and harness the fury of nature itself to forcefully remove any encroaching evil that threatens their sacred lands.

While the chaotic bend of nature is found within these Druids, their bodies and impulses are tamed through training and discipline. Originally from the unforgiving Festerwood, this circle’s teachings are as rigorous as the forest, blending a mixture of offense and defense to stand up to all of the world’s challenges.""":
        """Коло Незламних — орден друїдів, які відкинули терплячі настанови попередників і взялися за зброю на захист пущі. Ці войовничі друїди створюють ополчення й спрямовують лють самої природи, силою викорінюючи будь-яке зло, що зазіхає на їхні священні землі.

У них живе хаотична вдача природи, але тіло й пориви приборкані підготовкою та дисципліною. Це Коло походить із безжального Фестервуду, і його вчення таке ж суворе, як сам ліс: воно поєднує напад і захист, щоб протистояти всім випробуванням світу.""",
    "The cosmic force of order has suffused you with magic. That power arises from Mechanus or a realm like it—a plane of existence shaped entirely by clockwork efficiency. You or someone from your lineage might have become entangled in the machinations of modrons, the orderly beings who inhabit Mechanus. Perhaps your ancestor even took part in the Great Modron March. Whatever its origin within you, the power of order can seem strange to others, but for you, it’s part of a vast and glorious system.":
        "Космічна сила порядку наситила вас магією. Вона походить із Механуса або подібного царства — плану буття, цілком підпорядкованого бездоганній роботі механізмів. Ви чи хтось із вашого роду могли опинитися втягнутими в задуми модронів, упорядкованих мешканців Механуса. Можливо, ваш предок навіть брав участь у Великому марші модронів. Хоч би яким було джерело, сила порядку може здаватися іншим дивною, але для вас вона — частина величної та всеосяжної системи.",
    "Bards of the College of Dance know that the Words of Creation can’t be contained within speech or song; the words are uttered by the movements of celestial bodies and flow through the motions of the smallest creatures. These Bards practice a way of being in harmony with the whirling cosmos that emphasizes agility, speed, and grace.":
        "Барди Колегії Танцю знають, що Слів Творіння не вмістити ані в мову, ані в пісню: їх промовляє рух небесних тіл, і вони струменять у порухах найменших створінь. Ці барди живуть у гармонії з вирливим космосом, плекуючи спритність, швидкість і грацію.",
    """A Scion of the Three draws power from a group of malevolent gods known in Baldur’s Gate as the Dead Three: Bane, a god of tyranny; Bhaal, a god of violence and murder; and Myrkul, a god of death. While some Rogues of this subclass pledge themselves ardently to those three macabre gods, others are thrust on this path by a curse. Either way, a scion’s power manifests as various occult gifts, as well as an uncanny talent for striking and terrifying foes.

Scions of the Three are most common in Baldur’s Gate, where the Dead Three lived as mortals before ascending to godhood. Underground cults to Bane, Bhaal, and Myrkul often count Scions of the Three among their most useful agents. Outside Baldur’s Gate, secular thieves’ guilds such as the Shadow Thieves of Amn or the Xanathar Guild in Waterdeep might call on a Scion of the Three to undertake an especially violent contract.""":
        """Нащадок Трійці черпає силу від зловісних богів, відомих у Брамі Балдура як Мертва Трійця: Бейна, бога тиранії; Баала, бога насильства й убивства; та Меркула, бога смерті. Одні пройдисвіти цього підкласу ревно служать трьом моторошним богам, а інших штовхає на цей шлях прокляття. У будь-якому разі сила нащадка проявляється окультними дарами й надприродним хистом уражати та жахати ворогів.

Найчастіше Нащадки Трійці трапляються в Брамі Балдура, де боги Мертвої Трійці жили смертними до свого обожнення. Підпільні культи Бейна, Баала й Меркула часто використовують їх як найцінніших агентів. За межами міста світські злодійські гільдії на кшталт Тіньових злодіїв Амну чи Гільдії Ксанатара в Глибоководді можуть доручити Нащадкові Трійці особливо кривавий контракт.""",
    """Folk in Etharis don’t always speak highly of Monster Hunters, and many consider them to be just as depraved and inhuman as the evils they vanquish. Many of the appalling tales about Monster Hunters can be attributed, directly or indirectly, to the Devourer Guild, who are accused of being monstrous cannibals.

The truth is barely any better. Devourers have spent their days consuming the flesh and blood of the monsters they slay, and, over time, their metabolism has changed to tolerate this disgusting practice. Devourers adopt mutations shortly after consuming their prey.""":
        """В Етарісі про мисливців на чудовиськ не завжди говорять добре: багато хто вважає їх не менш розбещеними й нелюдськими за винищуване ними зло. Чимало моторошних оповідей про мисливців прямо чи опосередковано пов’язані з Гільдією Пожирачів, членів якої звинувачують у жахливому канібалізмі.

Насправді все ненабагато краще. Пожирачі роками споживали плоть і кров убитих чудовиськ, і з часом їхній обмін речовин пристосувався до цієї огидної практики. Після пожирання здобичі вони набувають мутацій.""",
    "The counsel of a Diviner is sought by those who want a clearer understanding of the past, present, and future. As a Diviner, you strive to part the veils of space, time, and consciousness. You work to master spells of discernment, remote viewing, supernatural knowledge, and foresight.":
        "До ворожбитів звертаються ті, хто прагне краще осягнути минуле, сучасне й майбутнє. Як ворожбит, ви розсуваєте завіси простору, часу та свідомості й опановуєте закляття прозріння, далекобачення, надприродного знання та передчуття.",
    "Your studies focus on magic that creates powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid. Some Evokers find employment in military forces, serving as artillery to blast armies from afar. Others use their power to protect others, while some seek their own gain.":
        "Ви вивчаєте магію, що породжує могутні стихійні явища: лютий холод, пекуче полум’я, гуркіт грому, тріск блискавки й їдку кислоту. Деякі втілювачі служать у військах живою артилерією та нищать армії здалеку. Інші спрямовують силу на захист ближніх, а дехто — на власну вигоду.",
    "A fey mystique surrounds you, thanks to the boon of an archfey or a location in the Feywild that transformed you. However you gained fey magic, you are now a Fey Wanderer. Your joyful laughter brightens the hearts of the downtrodden, and your martial prowess strikes terror in your foes, for great is the mirth of the fey and dreadful is their fury.":
        "Вас огортає фейська загадковість — дар архіфеї або наслідок перебування в куточку Феєлону, що змінив вас. Хоч би як ви здобули цю магію, тепер ви — Фейський мандрівник. Ваш веселий сміх зігріває серця пригноблених, а бойова майстерність жахає ворогів, бо безмежні веселощі фей і страшна їхня лють.",
    # Class and subclass descriptions, editorial batch 4.
    "Barbarians are defined by their rage, channeling it to unleash brief but potent destruction. Few are brave or unwise enough to study esoteric psychological techniques that split their rage from the rest of their psyche, dividing their identity into two parts: ego and id. When their ego is in control, the Fractured—as these Barbarians are known—possess self-control and cunning beyond most other Barbarians. When they allow their id to take control, their countenance turns monstrous and their bodies swell with the power of rage made physically manifest.":
        "Варварів визначає їхня лють, яку вони спрямовують у короткі, але нищівні спалахи. Мало кому вистачає сміливості чи нерозважливості вивчати езотеричні психологічні техніки, що відокремлюють лють від решти психіки й розділяють особистість на дві частини: Я та Воно. Коли гору бере Я, Розколоті — так називають цих варварів — виявляють незвичайні для своїх побратимів самовладання й хитрість. Коли ж вони випускають Воно, їхня подоба стає чудовиською, а тіла наливаються силою втіленої люті.",
    "Your magic is created by pieces of the Everheart, the center and driving force behind the expanding Everglacier wastelands. This power within you might be passed down through ancestors who protected the glacier’s magical core, or it might have been forced upon you through a chance encounter with the enchanted ice itself. Regardless of the source of your power, you are a creature of cold incarnate.":
        "Ваша магія породжена уламками Евергарта — серця й рушійної сили пусток Еверґлейшера, що невпинно ширяться. Цей дар могли передати предки, які захищали магічне ядро льодовика, або ж він оселився у вас після випадкової зустрічі із зачарованою кригою. Хоч би яким було джерело сили, ви — втілення холоду.",
    "Barbarians who walk the Path of the Giant draw strength from the same primal forces as giants. As they <LSTag Type=\"Status\" Tooltip=\"RAGE\">rage</LSTag>, these barbarians surge with elemental power and grow in size, taking on forms that evoke the glory of giants. Some barbarians look like oversized versions of themselves, perhaps with a hint of elemental energy flaring in their eyes and around their weapons. Others transform more dramatically, taking on the appearance of an actual giant or a form similar to an Elemental, wreathed in fire, frost, or lightning.":
        "Варвари Шляху Велетня черпають силу з тих самих первісних джерел, що й велетні. У стані <LSTag Type=\"Status\" Tooltip=\"RAGE\">Люті</LSTag> їх сповнює стихійна міць, а тіла збільшуються, набуваючи подоб, гідних слави велетнів. Одні стають просто велетенськими версіями себе, хіба що в очах і довкола зброї спалахує стихійна енергія. Інші змінюються докорінно, набуваючи вигляду справжнього велетня або стихійника, оповитого вогнем, морозом чи блискавкою.",
    "Paladins who take the Oath of Glory believe they and their companions are destined to achieve glory through deeds of heroism. They train diligently and encourage their companions, so they’re all ready when destiny calls.":
        "Паладини Обіту Слави вірять, що їм і їхнім супутникам судилося здобути славу героїчними діяннями. Вони невтомно тренуються й підбадьорюють товаришів, щоб усі були готові, коли покличе доля.",
    """The Grave Domain concerns itself with the boundary between life and death. To those who tap into this domain’s power, death is a natural and inevitable part of the multiverse. Such Clerics seek to destroy undead and shepherd spirits.

The magic of this domain also allows these Clerics to stave off death for a time. But this is merely a delay of death, not a denial of it, for the grave will always claim its due.""":
        """Могильний домен опікується межею між життям і смертю. Для тих, хто черпає з нього силу, смерть є природною та неминучою частиною мультивсесвіту. Такі клірики винищують невмерлих і проводжають душі померлих.

Магія домену також дає їм змогу на певний час відвернути смерть. Та це лише відстрочка, а не заперечення смерті, бо могила завжди забере належне.""",
    "When you choose this subclass, you might bind yourself to an unspeakable being from the Far Realm or an elder god—a being such as Tharizdun, the Chained God; Zargon, the Returner; Hadar, the Dark Hunger; or Great Cthulhu. Or you might invoke several entities without yoking yourself to one. The motives of these beings are incomprehensible, and the Great Old One might be indifferent to your existence. But the secrets you’ve learned nevertheless allow you to draw strange magic from it.":
        "Обравши цей підклас, ви могли пов’язати себе з невимовною істотою з Далекої царини або прадавнім богом — наприклад, Таріздуном, Прикутим Богом; Зарґоном, Поверненим; Гадаром, Темним Голодом; чи Великим Ктулху. А може, ви закликаєте кількох сутностей, не служачи жодній із них. Їхні мотиви незбагненні, а Величний Древній може навіть не зважати на ваше існування. Та пізнані вами таємниці однаково дають змогу черпати від нього дивну магію.",
    """Risk is in a Gunslinger’s blood. They are bold renegades, bucking tradition and forging a new path with dangerous and inelegant firearms. Gunslingers are infamous for surviving by their wits and relying on split-second timing and a considerable amount of luck to survive.

Black powder isn’t for the faint of heart. Its thunderous applause is volatile and imprecise—a barely controlled explosion directed at an enemy. Only the truly fearless seek to master it. But Gunslingers have nerves of steel, hurling death from their guns in a roaring cacophony. Adapted for shootouts, gunslingers are mobile and daring, knowing that life or death hangs on snap decision-making and one’s own mettle.

A Gunslinger’s explosive lifestyle lends well to wandering and adventuring. Gunslingers often shoot first and ask questions later, an attitude which earns them few friends and bountiful enemies. In their travels, most gunslingers are secretive and take great lengths to go unnoticed, lest they be spotted by old foes with scores to settle.""":
        """Ризик у стрільця в крові. Це зухвалі відступники, які відкидають традиції й прокладають новий шлях із небезпечною та незграбною вогнепальною зброєю в руках. Стрільці славляться вмінням виживати завдяки кмітливості, миттєвій реакції та чималій удачі.

Чорний порох не для полохливих. Його громові оплески непередбачувані й неточні — це ледь приборканий вибух, спрямований у ворога. Лише справді безстрашні наважуються його опанувати. Та стрільці мають сталеві нерви й сіють смерть із рушниць у ревучій какофонії. Рухливі й відчайдушні, вони знають: у перестрілці життя залежить від миттєвих рішень і власної стійкості.

Вибуховий спосіб життя спонукає стрільців до мандрів і пригод. Вони часто спершу стріляють, а вже потім ставлять запитання, через що мають мало друзів і безліч ворогів. У дорозі більшість із них приховує себе й докладає всіх зусиль, аби не потрапити на очі давнім недругам, які прагнуть звести рахунки.""",
    """The charismatic and manipulative Hellspeakers serve Moloch as they slip about the battlefield, coercing enemies into becoming unwitting allies.

Moloch rules Styx, the City of Lies, but his reach extends far beyond it. Hell’s greatest politicians and diplomats rise to prominence through Moloch’s subtle manipulations. They follow him with great loyalty, for they know they are nothing without him—and thus his power echoes through all of Hell.

Moloch’s illriggers are silver-tongued enchanters, lulling his foes to complacency with sorcery and subterfuge until they wake and find themselves under the command of the Order of Desolation. These Hellspeakers train in the art known as the Red Cant or Hell’s Cant. By understanding their enemy and through weaving subtle sorceries into normal speech, Hellspeakers can make their foes feel, think, or do nearly anything to accelerate Hell’s victory.

Across the timescape, Hellspeakers enjoy a reputation as smiling rogues and swashbuckling villains. An asset in any negotiation, Hellspeakers know that in a world of lies, the truth can be as potent a weapon as steel.""":
        """Харизматичні й маніпулятивні Пекломовці служать Молоху, ковзають полем бою та примушують ворогів мимоволі ставати союзниками.

Молох править Стіксом, Містом Брехні, але його вплив сягає далеко за його межі. Найвидатніші політики й дипломати Пекла підносяться завдяки тонким маніпуляціям Молоха. Вони безмежно віддані йому, бо знають: без нього вони ніщо. Так його сила відлунює в усьому Пеклі.

Ілріґери Молоха — красномовні чарівники, які чаклунством і хитрощами заколисують ворогів до самовдоволення, аж доки ті не опиняться під владою Ордену Спустошення. Пекломовці вивчають мистецтво, відоме як Червона говірка, або Говірка Пекла. Розуміючи ворога й непомітно вплітаючи чари у звичайну мову, вони здатні змусити його відчувати, думати чи робити майже будь-що задля перемоги Пекла.

У часових просторах Пекломовці мають славу усміхнених пройдисвітів і хвацьких лиходіїв. Вони безцінні на будь-яких переговорах і знають, що у світі брехні правда може бути не менш могутньою зброєю, ніж сталь.""",
    "You've made a pact with a sentient magic weapon and the cursed forces contained within its blade. Such a weapon could be the sword sheathed at a Warlock's side, or it could be an infamous magic weapon stored elsewhere, projecting its power across the multiverse to further its cunning plans. To those willing to follow its whims, these inscrutable patrons grant the power to bestow malignant curses, deliver punishing blows, and bolster their wielders.":
        "Ви уклали договір із розумною магічною зброєю та проклятими силами, замкненими в її клинку. Це може бути меч при боці чаклуна або сумнозвісна зброя, що зберігається десь далеко й спрямовує свою силу крізь мультивсесвіт заради хитрих задумів. Тим, хто ладен коритися її примхам, такий незбагненний покровитель дарує змогу накладати згубні прокляття, завдавати каральних ударів і зміцнювати свого носія.",
    "Fortune is a fickle thing—unless you’re a High Roller. These Gunslingers are master card sharps and dice throwers that mix their love of risk with their talent for gunplay. High Rollers push their luck until it runs out, then push harder. Why settle for a win when you could bet it all and win big?":
        "Фортуна мінлива — якщо тільки ви не Великий гравець. Ці стрільці майстерно шахраюють у карти й кидають кості, поєднуючи любов до ризику з талантом до вогнепальної зброї. Вони випробовують удачу, доки та не вичерпається, а тоді тиснуть іще дужче. Навіщо вдовольнятися звичайною перемогою, якщо можна поставити все й зірвати куш?",
    # Class and subclass descriptions, editorial batch 5.
    "Stalking the backroads, the Highway Rider strikes fear into the heart of every traveler and penny-pinching merchant. They run down their prize astride a swift and loyal steed— and then make a quick getaway.":
        "Чатуючи на манівцях, Дорожній вершник наганяє страх на мандрівників і скнар-купців. На прудкому й вірному коні він наздоганяє здобич — а тоді блискавично зникає.",
    "Legends tell that the most ancient and bloodthirsty terrors lurk deep within the old places of the earth. Hollow Wardens venerate and draw power from such beings, transforming themselves into merciless and monstrous guardians that stalk jagged coastlines, steep mountain crags, and other dark and wild places.":
        "За легендами, найдавніші й найкровожерливіші жахіття чатують у прадавніх глибинах землі. Порожні вартові шанують цих істот і черпають із них силу, перетворюючись на безжальних чудовиських охоронців зубчастих узбереж, стрімких гірських бескидів та інших темних і диких місць.",
    """The archdevils who rule the Seven Cities of Hell scheme endlessly. Each eternally plots to bring the others to heel—to ascend to the Throne of Hell, unite the Seven Cities and every infernal being living there, and lead an inexhaustible army of devils across the timescape until all worlds burn.

These archdevils’ elite operatives are the illriggers. Knights, assassins, mages, and terror-commandos of Hell, illriggers command the battlefield, disrupt enemy factions, and carry out their archdevil’s infernal will.""":
        """Архідияволи, що правлять Сімома Містами Пекла, безупинно плетуть інтриги. Кожен вічно намагається підкорити решту, зійти на Престол Пекла, об’єднати Сім Міст і всіх їхніх пекельних мешканців та повести незліченне військо бісів крізь часові простори, доки не запалають усі світи.

Елітні агенти архідияволів — ілріґери. Ці лицарі, убивці, маги й пекельні командос панують на полі бою, розколюють ворожі угруповання та виконують пекельну волю свого володаря.""",
    "You specialize in magic that dazzles the senses and tricks the mind, and the illusions you craft make the impossible seem real.":
        "Ви спеціалізуєтеся на магії, що приголомшує чуття й ошукує розум, а створені вами ілюзії надають неможливому подоби реальності.",
    """Monks of the Way of the Kensei train relentlessly with their weapons, to the point where the weapon becomes an extension of the body. Founded on a mastery of sword fighting, the tradition has expanded to include many different weapons.

A kensei sees a weapon in much the same way a calligrapher or painter regards a pen or brush. Whatever the weapon, the kensei views it as a tool used to express the beauty and precision of the martial arts. That such mastery makes a kensei a peerless warrior is but a side effect of intense devotion, practice, and study.""":
        """Монахи Шляху кенсея невтомно вправляються зі зброєю, доки та не стає продовженням їхнього тіла. Традиція виникла з майстерності фехтування, але згодом охопила безліч інших видів зброї.

Кенсей дивиться на зброю так само, як каліграф або художник на перо чи пензель. Хоч би що він тримав у руках, це знаряддя для вираження краси й точності бойового мистецтва. Те, що така майстерність робить кенсея незрівнянним воїном, — лише побічний наслідок глибокої відданості, вправ і навчання.""",
    "Warriors of Mercy manipulate the life force of others. These Monks are wandering physicians, but they bring a swift end to their enemies. They often wear masks, presenting themselves as faceless bringers of life and death.":
        "Воїни Милосердя керують життєвою силою інших. Ці монахи мандрують як цілителі, але швидко кладуть край життю ворогів. Вони часто носять маски й постають безликими провісниками життя та смерті.",
    "The Mind Domain celebrates the power of the mortal mind, channeling psychic energy to protect the faithful and smite your enemies. While this is most often associated with the Path of Light or the Riedran Path of Inspiration, followers of the daelkyr can also master this power. Visions of Xoriat can drive a priest to madness, but they can also reveal deadly secrets of the mind.":
        "Домен Розуму звеличує силу смертної свідомості й спрямовує психічну енергію на захист вірних і покарання ворогів. Найчастіше цю силу пов’язують зі Шляхом Світла або рідранським Шляхом Натхнення, проте її можуть опанувати й послідовники даелкірів. Видіння Ксоріату здатні звести жерця з розуму, але водночас відкривають смертоносні таємниці свідомості.",
    """Monster Hunters are skilled professionals, specializing in identifying, tracking, and slaying monsters that threaten the lives and the livelihoods of the people of Etharis.

Each Monster Hunter trains in a different method for these tasks. Some hunters don heavy armor and carry shields to protect against crushing jaws and scything claws, others deploy cunning traps to keep a safe distance from the horrors they hunt, some assume the traits and powers of their enemies to better slay them, and others dabble in magic to supplement martial prowess with arcane wrath.""":
        """Мисливці на чудовиськ — досвідчені фахівці з розпізнавання, вистежування та винищення потвор, що загрожують життю й добробуту мешканців Етарісу.

Кожен мисливець має власний підхід. Одні вдягають важкі обладунки й беруть щити, щоб захиститися від нищівних щелеп і серпоподібних пазурів. Інші розставляють хитромудрі пастки й тримаються подалі від жахіть, на яких полюють. Дехто переймає риси та сили ворогів, а дехто доповнює бойову майстерність містичною люттю.""",
    "The College of the Moon traces its origins to the ancient druidic circles of the Moonshae Isles, who entrusted the first Bards of this tradition with chronicling the stories of the islands and their people. Bards of this college draw from the isles’ fey magic and the primal power of the moonwells to bolster their allies, protect the natural world, and inspire their bardic works.":
        "Колегія Місяця бере початок від стародавніх друїдських кіл островів Мунша, які доручили першим бардам цієї традиції літописати історії островів та їхніх народів. Барди Колегії черпають із фейської магії островів і первісної сили місячних криниць, щоб зміцнювати союзників, захищати природу й знаходити натхнення для своїх творів.",
    "Paladins sworn to the Oath of the Noble Genies revere the forces of the Elemental Planes. Through taking this oath, Paladins draw power from the four different types of genies—dao, masters of earth; djinn, masters of air; efreet, masters of fire; and marids, masters of water. In Faerûn, many Paladins who swear this oath hail from Calimshan, a land teeming with genies.":
        "Паладини Обіту Шляхетних Джинів шанують сили Стихійних планів. Склавши цей обіт, вони черпають силу від чотирьох видів джинів: дао, володарів землі; джинів, володарів повітря; іфритів, володарів вогню; та маридів, володарів води. На Фаеруні багато паладинів цього обіту походять із Калімшану — краю, сповненого джинів.",
    # Class and subclass descriptions, editorial batch 6.
    "In Etharis, there are those who fear magic, and those who seek to understand it. Monster Hunters from the Occultist Guild know folk from both sides are equally dangerous. An Occultist investigates the arcane, the supernatural, and the uncanny, while avoiding the influence of superstition or ideology. Despite their reputation as mage hunters, Occultists don’t burn their enemies at the stake—Occultists put them to the sword, as that’s what swords are for. Knowledge and magic give Occultists an edge over their mystical adversaries. Their spells are used to detect and defend against dangerous arcana, and, above all, magic is used to destroy monsters that can’t be harmed by steel.":
        "В Етарісі одні бояться магії, а інші прагнуть її осягнути. Мисливці на чудовиськ із Гільдії окультистів знають: обидві сторони однаково небезпечні. Окультист досліджує містичне, надприродне й незбагненне, не піддаючись забобонам та ідеологіям. Попри славу мисливців на магів, окультисти не палять ворогів на вогнищі — вони вражають їх мечем, адже мечі саме для цього. Знання й магія дають їм перевагу над містичними супротивниками. Закляття допомагають виявляти небезпечні чари й захищатися від них, а головне — знищувати чудовиськ, яким не шкодить сталь.",
    """The heavily armored death troopers of Hell, Painkillers serve Dispater, leading from the front of every major infernal battle.

Dispater rules Dis, the City of War. When Hell invades another world, Dispater’s army does the fighting and dying. His Painkillers are master strategists who lead from the front, inspiring terror and awe in their soldiers. The imperious Painkillers are full of pride and hubris, and they often obsess over their personal appearance.

Though among the most chivalrous of the illriggers, a Painkiller’s gallantry is twisted. They accept and honor challenges to single combat, and swiftly punish any who try to interfere—but if losing, they don’t hesitate to cheat, and if winning, they arrogantly toy with an enemy before finishing them.

In a moment of weakness or desperation, a ruler in another world might see their army facing certain defeat and call on Dispater. Ever eager to sow strife and discord, Dispater often responds to these pleas by sending a Painkiller to lead the desperate ruler’s armies.""":
        """Знеболювачі — важкоозброєні пекельні штурмовики Диспатера, які очолюють наступ у кожній великій інфернальній битві.

Диспатер править Дісом, Містом Війни. Коли Пекло вторгається до іншого світу, саме його військо б’ється й гине. Знеболювачі — майстерні стратеги, які ведуть із передової та вселяють у своїх солдатів жах і благоговіння. Вони владні, сповнені гордині й часто одержимі власною зовнішністю.

Хоч Знеболювачі належать до найлицарськіших ілріґерів, їхня шляхетність спотворена. Вони приймають виклики на двобій і швидко карають кожного, хто втрутиться. Та коли програють — без вагань шахрують, а коли перемагають — пихато граються з ворогом перед смертельним ударом.

У мить слабкості чи відчаю правитель іншого світу може побачити неминучу поразку свого війська й звернутися до Диспатера. Той завжди прагне сіяти чвари й розбрат, тож часто відгукується, посилаючи Знеболювача очолити армію зневіреного володаря.""",
    "Psi Warriors awaken the power of their minds to augment their physical might. They harness this psionic power to infuse their weapon strikes, lash out with telekinetic energy, and create barriers of mental force.":
        "Пси-воїни пробуджують силу розуму, щоб зміцнити тіло. Вони спрямовують псіонічну міць у удари зброєю, атакують телекінетичною енергією та створюють заслони ментальної сили.",
    "Rune Knights enhance their martial prowess using the supernatural power of runes, an ancient practice that originated with giants. Rune cutters can be found among any family of giants, and you likely learned your methods first or second hand from such a mystical artisan. Whether you found the giant’s work carved into a hill or cave, learned of the runes from a sage, or met the giant in person, you studied the giant’s craft and learned how to apply magic runes to empower your equipment.":
        "Рунні лицарі підсилюють бойову майстерність надприродною силою рун — стародавнім мистецтвом велетнів. Різьбярі рун трапляються серед усіх велетенських родів, і ви, найімовірніше, перейняли прийоми безпосередньо від такого містичного майстра або від його учня. Можливо, ви знайшли велетенські письмена на схилі чи в печері, почули про руни від мудреця або зустріли самого велетня. Так чи інакше, ви вивчили це ремесло й навчилися посилювати спорядження магічними рунами.",
    """The blood-knights of Hell, Sanguine Knights serve Sutekh, Lord of Blood. Their sorceries drain their enemies’ life force, pouring this stolen vitality into infernal rituals to turn the tide of battle.

Sutekh rules Naraka, the City of Blood. Recognized as the greatest sorcerer in hell, he carries the title of High Sanguinary and rules from the Temple of Vitality. He is a master of blood magic, and his inner circle of priests and wizards are the Bloodliches, undead spellcasters whose corporeal forms turned to ash centuries ago and whose bodies are crafted from solid blood.

Sutekh’s illriggers all belong to a cult known as the Chalice of Vitality. Knights of the Chalice drink deeply of their enemies’ essence, draining it to power their magics. Other members of the Order of Desecration fear that the Sanguine Knights seek more than Sutekh’s mere ascension to the Throne of Hell; some whisper that the Chalice secretly schemes to make Sutekh a god. This would, of course, be treason.""":
        """Криваві лицарі Пекла служать Сутеху, Володарю Крові. Їхнє чаклунство висмоктує життєву силу ворогів і вливає викрадену снагу в пекельні ритуали, змінюючи перебіг битви.

Сутех править Наракою, Містом Крові. Його визнають найвеличнішим чародієм Пекла; він носить титул Вищого Кровника й володарює з Храму Життєвості. Сутех — майстер магії крові, а його найближче коло жерців і чарівників складають кроволічі: невмерлі заклиначі, чиї тілесні оболонки століття тому обернулися на попіл, а нові тіла створено із застиглої крові.

Усі ілріґери Сутеха належать до культу Чаші Життєвості. Лицарі Чаші п’ють сутність ворогів, живлячи нею свою магію. Інші члени Ордену Осквернення підозрюють, що Криваві лицарі прагнуть не лише піднести Сутеха на Престол Пекла: подейкують, ніби Чаша таємно замислила зробити його богом. Звісно, це було б зрадою.""",
    "The Shadow domain embraces the darkness that surrounds all things and manipulates the transitory gray that separates light from dark. Shadow domain clerics walk a subtle path, frequently changing allegiances and preferring to operate unseen.":
        "Тіньовий домен приймає темряву, що огортає все суще, і керує мінливою сірістю на межі світла й мороку. Його клірики ступають непримітним шляхом, часто змінюють союзників і воліють діяти невидимо.",
    """Dark energy infuses the Shadow Realm, corrupting and corroding everything it touches. Some barbarians intentionally consume this raw shadow, infusing their bodies with shadow energy to manifest potent magical abilities.

Many of the barbarians who walk this path do so to absorb harmful shadow magic into themselves in order to protect others from its influence. A smaller group consumes shadow simply because they cannot resist its ever-present temptation.""":
        """Темна енергія пронизує Царство Тіней, спотворюючи й роз’їдаючи все, чого торкається. Деякі варвари свідомо поглинають необроблену тінь і насичують тіло її енергією, щоб пробудити могутні магічні здібності.

Багато послідовників цього шляху приймають у себе згубну тіньову магію, аби захистити інших від її впливу. Інші ж пожирають тінь лише тому, що не здатні опиратися її невпинній спокусі.""",
    "Your innate magic comes from the most nebulous and inscrutable forces of the Shadowfell or from other regions of supernatural darkness. You might trace your lineage to an entity from such a place, or perhaps you were exposed to the sinister energy of a shadow dragon and were transformed by it. Your shadowy magic allows you to command darkness, undeath, and woe.":
        "Ваша вроджена магія походить від найпримарніших і незбагненних сил Тінепаду або інших царств надприродного мороку. Можливо, у вашому родоводі є істота з такого краю, а може, вас перетворила зловісна енергія тіньового дракона. Ця магія дає вам владу над темрявою, невмертям і стражданням.",
    # Class and subclass descriptions, editorial batch 7.
    """The hidden assassins of Hell, Shadowmasters serve Belial and excel at stealth and disguise.

Belial rules Gehennom, the City of Darkness. He strives to rule Hell through poison, torture, and assassination. His illriggers strike from the shadows or use deception to earn high-ranking positions close to powerful rulers. Many Shadowmasters run networks of spies and assassins who have no idea of the infernal provenance of their leader.

Shadowmasters are sworn not to reveal their true allegiance, and if need be, they must take their own lives to fulfill this oath. Many Shadowmasters prepare elaborate plans for their own assassination so that, should they risk discovery, their assassination obscures the truth. Of course, these killers never learn they were hired by their deceased target.""":
        """Володарі Тіней — потаємні вбивці Пекла, що служать Беліалу й неперевершено володіють мистецтвом непомітності та маскування.

Беліал править Геенномом, Містом Темряви. Він прагне панувати над Пеклом за допомогою отрут, тортур і вбивств. Його ілріґери б’ють із тіні або обманом здобувають високі посади біля могутніх володарів. Багато Володарів Тіней керують мережами шпигунів і вбивць, які навіть не здогадуються про пекельне походження свого ватажка.

Володарі Тіней присягаються ніколи не викривати справжньої вірності й за потреби мусять накласти на себе руки. Багато з них заздалегідь розробляють складний план власного вбивства, щоб у разі викриття смерть приховала правду. Звісно, наймані вбивці так і не дізнаються, що їх винайняла майбутня жертва.""",
    "A Soulknife strikes with the mind, cutting through barriers both physical and psychic. These Rogues discover psionic power within themselves and channel it to do their roguish work. As a Soulknife, your psionic abilities might have haunted you since childhood, revealing their full potential only as you experienced the stress of adventure. Or you might have sought out an order of psychic adepts and spent years learning how to manifest your power.":
        "Клинок Душі вражає силою розуму й прорізає як фізичні, так і психічні перешкоди. Ці пройдисвіти відкривають у собі псіонічну міць і спрямовують її на своє ремесло. Можливо, здібності переслідували вас із дитинства, але повністю розкрилися лише під тиском пригод. А може, ви розшукали орден психічних адептів і роками вчилися втілювати свою силу.",
    """Your innate power stems from the source of magic itself: the Weave. This connection manifests as a rare ability known as spellfire, and you surge with radiant bursts of this raw magic. Your talent with spellfire allows you to heal allies, sear enemies, and absorb powerful spells.

Wielders of spellfire tend to have a penchant for wandering. Many travel between cosmopolitan settlements, such as those along the Sword Coast, and wield their magic in service of the common good. Others realize their own strange powers by roaming equally strange lands, from the magic-blasted wastes of the desert of Anauroch to the god-touched wilds of the Old Empires. Wherever they go in the Realms, spellfire Sorcerers are courted by factions with interests in the arcane arts, such as the Harpers, Cult of the Dragon, and Red Wizards.""":
        """Ваша вроджена сила походить із самого джерела магії — Плетіння. Цей зв’язок проявляється рідкісною здатністю, відомою як чаровогонь, а ваше тіло пульсує променевими спалахами первісної магії. Завдяки чаровогню ви можете зцілювати союзників, обпалювати ворогів і поглинати могутні закляття.

Носії чаровогню зазвичай мають жагу до мандрів. Багато хто подорожує між багатолюдними поселеннями Узбережжя Мечів і служить магією спільному благу. Інші відкривають власні дивні сили в не менш дивних краях — від спустошених магією пусток Анауроху до благословенних богами земель Старих Імперій. Де б у Королівствах не з’явилися чародії чаровогню, їх прихильності домагаються Арфісти, Культ Дракона, Червоні чарівники та інші угруповання, зацікавлені в містичних мистецтвах.""",
    "Magic and guns aren’t so different—arcane power is like gunpowder, a spell is like a bullet, and you are like a gun, directing your spells with precision at unfortunate targets. Spellslingers mix the disciplines of gunplay and spellcasting, sometimes loading arcane charges with your shots and firing bullets enhanced with lightning, frost, or flame.":
        "Магія та рушниці не такі вже й різні: містична сила подібна до пороху, закляття — до кулі, а ви — до зброї, що точно спрямовує чари в нещасну ціль. Чаростріли поєднують стрілецьке мистецтво з проказуванням заклять, вкладають у постріли містичні заряди й випускають кулі, посилені блискавкою, морозом або полум’ям.",
    "Bards of the College of Spirits conjure legendary spirits to change the world. But such entities are capricious, and what a Bard summons isn’t always entirely under their control.":
        "Барди Колегії Духів прикликають легендарних духів, щоб змінювати світ. Та ці сутності примхливі, й викликане бардом не завжди цілком йому підкоряється.",
    "Barbarians who follow the Path of the Wild Heart view themselves as kin to animals. These Barbarians learn magical means to communicate with animals, and their <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> heightens their connection to animals as it fills them with supernatural might.":
        "Варвари Шляху Дикого Серця вважають себе ріднею звірів. Вони вивчають магічні способи спілкування з тваринами, а <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag> поглиблює цей зв’язок і сповнює їх надприродною міццю.",
    "You’ve made a pact with a creature that defies the cycle of life and death: a powerful lich, a vampire, or another entity of undeath. Having once been mortal, these ancient patrons know firsthand the paths of ambition and the routes past the doors of death. They eagerly share this profane knowledge and other secrets with those who work their will among the living.":
        "Ви уклали договір з істотою, що заперечує коло життя і смерті: могутнім лічем, вампіром чи іншою невмерлою сутністю. Колись смертні, ці прадавні покровителі з власного досвіду знають шлях честолюбства й дороги за дверима смерті. Вони охоче діляться нечестивими знаннями та іншими таємницями з тими, хто вершить їхню волю серед живих.",
    "Vikings are battle-hardened warriors and sailors who ply the seas of the Northlands for glory and plunder. As followers of the Reaver’s Way, they have their own sense of honor, yet they can be merciless in times of raiding and war. Vikings are known for their prowess with the spear and axe, and for their belief that they can earn a special place in the halls of the dead through their deeds of valor in battle.":
        "Вікінги — загартовані боями воїни й мореплавці, що борознять моря Північних земель заради слави та здобичі. Послідовники Шляху Нальотчика мають власне уявлення про честь, але в набігах і війнах бувають безжальними. Вони славляться вправністю зі списом і сокирою та вірять, що бойовою звитягою здобудуть особливе місце в чертогах мертвих.",
    "Some Gunslingers live by a code and expect others to do the same. These Gunslingers, known as White Hats, sometimes serve as officers of the law but never hesitate to do what’s right when the law says otherwise. Despite their affinity for deadly weapons, White Hats prefer to keep their friends safe and subdue their enemies nonviolently—a preference their enemies don’t often oblige.":
        "Деякі стрільці живуть за кодексом і вимагають того самого від інших. Їх називають Білими Капелюхами. Часом вони служать закону, але ніколи не вагаються вчинити правильно, навіть якщо закон велить інакше. Попри любов до смертоносної зброї, Білі Капелюхи воліють берегти друзів і приборкувати ворогів без кровопролиття — хоча вороги рідко дають їм таку можливість.",
    "Your innate magic stems from the forces of chaos that underlie the order of creation. You or an ancestor might have endured exposure to raw magic, perhaps through a planar portal leading to Limbo or the Elemental Planes. Perhaps you were blessed by a fey being or marked by a demon. Or your magic could be a fluke with no apparent cause. Whatever its source, this magic churns within you, waiting for any outlet.":
        "Ваша вроджена магія походить із сил хаосу, що лежать в основі впорядкованого творіння. Ви чи ваш предок могли зазнати впливу первісної магії — наприклад, крізь планарний портал до Лімбо або Стихійних планів. Можливо, вас благословила фейська істота чи позначив демон. А може, магія виникла випадково, без видимої причини. Хоч би яким було джерело, вона вирує всередині й шукає виходу.",
    # Class and subclass descriptions, editorial batch 8.
    "Many places in the multiverse abound with beauty, intense emotion, and rampant magic; the Feywild, the Upper Planes, and other realms of supernatural power radiate with such forces and can profoundly influence people. As folk of deep feeling, barbarians are especially susceptible to these wild influences, with some barbarians being transformed by the magic. These magic-suffused barbarians walk the Path of Wild Magic. Elf, tiefling, aasimar, and genasi barbarians often seek this path, eager to manifest the otherworldly magic of their ancestors.":
        "У мультивсесвіті є чимало місць, сповнених краси, сильних почуттів і нестримної магії. Феєлон, Верхні плани й інші царства надприродної сили випромінюють могутні енергії, здатні докорінно змінювати людей. Варвари живуть глибокими почуттями, тож особливо вразливі до такого дикого впливу, а декого магія перетворює назавжди. Насичені нею варвари ступають Шляхом Дикої Магії. Ельфи, бісини, асимари й дженазі часто обирають цей шлях, прагнучи проявити потойбічну магію предків.",
    "Winter Walkers hone their craft in the bleak and frozen wilds of places like Icewind Dale. These ruthless, rimed Rangers hunt monsters that haunt arctic wastelands, eventually becoming frigid terrors themselves. Winter Walkers are well versed in the phenomena of Icewind Dale, including the latent magic of fallen Netherese cities, endemic monsters like yetis and crag cats, and the rising threat of Underdark invaders. Due to their cold pragmatism, terrifying magic, and mastery of the region, Winter Walkers are regarded with equal parts respect and fear. Ten-Towns citizens say that Winter Walkers’ frequent exposure to malignant entities gives them their fearsome powers. Many Reghed nomads, on the other hand, believe that nature spirits bestow on Winter Walkers a unique curse.":
        "Зимові Мандрівники відточують ремесло в похмурих крижаних пущах на кшталт Долини Крижаного Вітру. Ці безжальні, вкриті памороззю слідопити полюють на чудовиськ арктичних пустищ і зрештою самі стають морозними жахіттями. Вони добре знають усі дива й небезпеки Долини: приховану магію загиблих нетерезьких міст, місцевих потвор на кшталт єті та скельних котів і дедалі більшу загрозу нападників із Підмор’я. Через холодний прагматизм, страшну магію та знання краю їх однаково поважають і бояться. Мешканці Десятимістя кажуть, що жахливу силу Мандрівникам дарують часті зустрічі зі зловісними сутностями. Натомість багато регедських кочовиків вірять, що це особливе прокляття духів природи.",
    "Barbarians who follow the Path of the World Tree connect with the cosmic tree Yggdrasil through their <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag>. This tree grows among the Outer Planes, connecting them to each other and the Material Plane. These Barbarians draw on the tree’s magic for vitality and as a means of dimensional travel.":
        "Варвари Шляху Світового Дерева через свою <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag> єднаються з космічним деревом Іґґдрасілем. Воно росте поміж Зовнішніми планами й пов’язує їх між собою та з Матеріальним планом. Варвари черпають із його магії життєву силу й використовують її для подорожей між вимірами.",
    "Barbarians who walk the Path of the Zealot receive boons from a god or pantheon. These Barbarians experience their <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> as an ecstatic episode of divine union that infuses them with power. They are often allies to the priests and other followers of their god or pantheon.":
        "Варвари Шляху Ревнителя отримують блага від бога чи пантеону. Вони переживають свою <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag> як екстатичну мить єднання з божеством, що сповнює їх силою. Часто вони стають союзниками жерців та інших послідовників свого бога чи пантеону.",
    # Feat descriptions, editorial batch 1.
    """You have been changed through magic, science, or a volatile blend of the two. You have a blatant physical augmentation of your choice from the options below. The augmentation is obvious—such as with stitches, grafts of other creature’s body parts, or implants—unless disguised.

Natural Armor. You have scales, plates, or thick hide that grants you an AC of 10 + your Dexterity and Constitution modifier.

Natural Weapons. You have claws, fangs, horns, or some other natural weapon that you can use to make Unarmed Strikes that deal 1d6 damage on a hit.

Night Vision. You have Darkvision with a range of 60 feet. If you already have Darkvision, its range increases by 30 feet.""":
        """Магія, наука або їхня нестабільна суміш змінили вас. Виберіть одне з наведених нижче помітних фізичних удосконалень. Якщо його не замаскувати, шви, пересаджені частини чужого тіла чи імпланти видно неозброєним оком.

Природний захист. Луска, пластини або товста шкура дають вам РЗ 10 + модифікатори спритності й статури.

Природна зброя. Ваші кігті, ікла, роги чи інша природна зброя дають змогу здійснювати Беззбройні удари, що в разі влучання завдають 1d6 шкоди.

Нічний зір. Ви отримуєте темнозір на 60 футів. Якщо ви вже маєте темнозір, його дальність збільшується на 30 футів.""",
    """Hop Up. While you have the Prone condition, you can stand up by spending only 5 feet of movement.

Jumping. Once per turn, you can make a Jump by spending only 10 feet of movement.""":
        """Підхопитися. У стані повалення ви можете підвестися, витративши лише 5 футів переміщення.

Стрибок. Один раз за хід ви можете стрибнути, витративши лише 10 футів переміщення.""",
    """Improved Dash. When you take the Dash action, your Speed increases by 10 feet for that action.

Charge Attack. If you move at least 10 feet in a straight line toward a target immediately before hitting it with a melee attack roll as part of the Attack action, choose one of the following effects: gain a 1d8 bonus to the attack’s damage roll, or push the target up to 10 feet away if it is no more than one size larger than you. You can use this benefit only once on each of your turns.""":
        """Покращений ривок. Коли ви виконуєте дію «Ривок», ваша швидкість для цієї дії збільшується на 10 футів.

Атака з розгону. Якщо безпосередньо перед влучанням атакою ближнього бою в межах дії «Атака» ви перемістилися до цілі щонайменше на 10 футів по прямій, виберіть один ефект: додайте 1d8 до кидка шкоди або відштовхніть ціль на відстань до 10 футів, якщо вона не більш ніж на один розмір більша за вас. Цю перевагу можна застосувати лише раз за хід.""",
    """You know hedge remedies and hexes passed down through Old Ways teachings, and you can impart them into small wicker charms you weave. You gain the following benefits.

You always have the Bless and Hex spells prepared. In addition, you gain one 1st-level spell slot that can be used to cast them.""":
        """Ви знаєте сільські ліки й прокляття, передані у вченні Старих Шляхів, і вмієте вплітати їх у невеликі плетені обереги. Ви отримуєте такі переваги.

У вас завжди підготовлені закляття «Благословення» та «Прокляття». Крім того, ви отримуєте одну чарунку заклять 1-го рівня, яку можете витратити на проказування цих заклять.""",
    """Cantrip. You learn the Ray of Frost cantrip.

Frostbite. Once per turn when you hit a creature with an attack roll and deal Cold damage, you can temporarily negate the creature’s defenses. The creature subtracts 1d4 from the next saving throw it makes before the end of your next turn.""":
        """Замовляння. Ви вивчаєте замовляння «Морозний промінь».

Обмороження. Один раз за хід, коли ви влучаєте в істоту кидком атаки й завдаєте холодової шкоди, ви можете тимчасово послабити її захист. Істота віднімає 1d4 від наступного кидка протидії, здійсненого до кінця вашого наступного ходу.""",
    """Firing in Melee. Being within 5 feet of an enemy doesn’t impose Disadvantage on your attack rolls with crossbows.

Wounding Bolt. When you hit a creature with a ranged attack, it has a chance to gain the <LSTag Type=\"Status\" Tooltip=\"GAPING_WOUND\">Gaping Wounds</LSTag> condition.""":
        """Стрільба в ближньому бою. Перебування в межах 5 футів від ворога не накладає завади на ваші кидки атаки з арбалета.

Ранливий болт. Коли ви влучаєте в істоту дальньою атакою, вона може набути стану <LSTag Type=\"Status\" Tooltip=\"GAPING_WOUND\">Глибокі рани</LSTag>.""",
    """Push. Once per turn, when you hit a creature with an attack that deals Bludgeoning damage, you can move it 5 feet to an unoccupied space if the target is no more than one size larger than you.

Enhanced Critical. When you score a Critical Hit that deals Bludgeoning damage to a creature, attack rolls against that creature have Advantage until the start of your next turn.""":
        """Поштовх. Один раз за хід, коли ви влучаєте в істоту атакою з дробильною шкодою, можете перемістити її на 5 футів у вільне місце, якщо ціль не більш ніж на один розмір більша за вас.

Посилене критичне влучання. Коли ви завдаєте істоті критичного влучання з дробильною шкодою, кидки атаки проти неї мають перевагу до початку вашого наступного ходу.""",
    """Dragon's Terror. You can take a Magic action to instill terror in a creature you can see within 30 feet of yourself. The target must succeed on a Wisdom saving throw or have the Frightened condition until the end of your next turn.

Inspired by Fear. When you cause a creature to gain the Frightened condition and you are the source of its fear, you gain Heroic Inspiration. Once you use this benefit, you can’t use it again until you finish a Short or Long Rest.""":
        """Драконячий жах. Магічною дією ви можете нажахати істоту, яку бачите в межах 30 футів від себе. Ціль повинна успішно виконати кидок протидії мудрістю, інакше набуде стану переляку до кінця вашого наступного ходу.

Натхнення страхом. Коли через вас істота набуває стану переляку, ви отримуєте героїчне натхнення. Після застосування цієї переваги ви не зможете скористатися нею знову до завершення короткого або довгого відпочинку.""",
    """Elves possess a natural talent for hitting the mark when using their bows. You have honed this talent almost to perfection, and your arrows find their target with uncanny precision.

As a bonus action, you can give yourself advantage on your ranged weapon attack roll on the current turn. You can use this bonus action only if you haven’t moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn.""":
        """Ельфи мають природний хист до влучної стрільби з лука. Ви довели цей талант майже до досконалості, й ваші стріли знаходять ціль із надприродною точністю.

Вторинною дією ви можете надати собі перевагу на кидок атаки далекобійною зброєю в поточному ході. Цю дію можна виконати, лише якщо цього ходу ви ще не переміщувалися; після неї ваша швидкість дорівнює 0 до кінця поточного ходу.""",
    "If an effect would kill you outright without Death Saving Throws or would reduce you directly to 0 Hit Points without dealing damage, you are instead reduced to a number of Hit Points equal to your level. You can’t use this benefit again until you finish a Long Rest.":
        "Якщо ефект мав би миттєво вбити вас без кидків протидії смерті або зменшити ваші очки здоров’я безпосередньо до 0, не завдаючи шкоди, натомість у вас залишається кількість очок здоров’я, що дорівнює вашому рівню. Після цього ви не зможете скористатися цією перевагою знову до завершення довгого відпочинку.",
    # Feat descriptions, editorial batch 2.
    "Parry. If you’re holding a Finesse weapon and another creature hits you with a melee attack, you can take a Reaction to add your Proficiency Bonus to your Armor Class, potentially causing the attack to miss you. You gain this bonus to your AC against melee attacks until the start of your next turn.":
        "Парирування. Якщо ви тримаєте фехтувальну зброю й інша істота влучає у вас атакою ближнього бою, ви можете застосувати реагування та додати свій бонус спеціалізації до РЗ, що може перетворити влучання на промах. Цей бонус до РЗ проти атак ближнього бою діє до початку вашого наступного ходу.",
    """Prerequisite: Dragonborn

When angered, you can radiate menace.

You gain one use of your Breath Weapon.

You can expend one use of your Breath Weapon to roar, forcing each creature of your choice within 30 feet of you to make a Wisdom saving throw. On a failed save, a target becomes frightened of you for 1 minute.""":
        """Необхідна умова: драконич

У гніві ви випромінюєте загрозу.

Ви отримуєте одне додаткове застосування Дихальної зброї.

Ви можете витратити застосування Дихальної зброї, щоб заревіти. Кожна вибрана вами істота в межах 30 футів повинна виконати кидок протидії мудрістю. У разі невдачі ціль боїться вас протягом 1 хвилини.""",
    """Prerequisite: Dragonborn

You manifest scales and claws reminiscent of your draconic ancestors.

Your scales harden. While you aren’t wearing armor, you can calculate your AC as 13 + your Dexterity modifier. You can use a shield and still gain this benefit.

You grow retractable claws from the tips of your fingers. Extending or retracting the claws requires no action. The claws are natural weapons, which you can use to make unarmed strikes. When you hit with an unarmed strike using these claws, the attack deals an additional 1d4 slashing damage.""":
        """Необхідна умова: драконич

У вас виростають луска й кігті, подібні до ознак драконячих предків.

Ваша луска твердішає. Коли ви не носите обладунків, ваш РЗ дорівнює 13 + модифікатор спритності. Щит не позбавляє вас цієї переваги.

На кінчиках пальців виростають утяжні кігті. Випустити або сховати їх можна без дії. Кігті є природною зброєю для Беззбройних ударів. Влучивши таким ударом, ви завдаєте додатково 1d4 рубаної шкоди.""",
    """The legend of Bard the Bowman has inspired many young men and women from Dale, so much that they long to prove their worth with the killing of a great monster. As many more before you, you have long pondered on the ways to deal with creatures of size, hoping one day to gain renown defeating them.

You have Advantage on Attack Rolls against Large or larger creatures. In addition, you deal additional damage equal to your Strength modifier when you hit such creatures.""":
        """Легенда про Барда Лучника надихнула багатьох юнаків і дівчат із Долу, які прагнуть довести свою вправність, убивши велике чудовисько. Як і численні попередники, ви довго вивчали способи боротьби з велетенськими істотами, сподіваючись одного дня уславитися перемогою над ними.

Ви маєте перевагу на кидки атаки проти Великих або більших істот. Крім того, влучаючи в таку істоту, ви завдаєте додаткової шкоди в кількості, що дорівнює вашому модифікатору сили.""",
    """Damage Resistance. When you gain this feat, choose Acid, Cold, Fire, Lightning, or Poison. You have Resistance to the chosen damage type.

Fearsome Power. When you deal damage to a creature as part of the Attack or Magic action on your turn, you can use the Dragon’s Terror benefit of the Cult of the Dragon Initiate feat as a Bonus Action this turn.""":
        """Стійкість до шкоди. Отримавши цю рису, виберіть кислоту, холод, вогонь, блискавку або отруту. Ви отримуєте стійкість до вибраного типу шкоди.

Грізна сила. Коли у свій хід ви завдаєте істоті шкоди в межах дії «Атака» чи «Магія», цього самого ходу можете вторинною дією застосувати перевагу «Драконячий жах» риси «Посвячений Культу Дракона».""",
    "You can use Two-Weapon Fighting even if your weapons aren't <LSTag Tooltip=\"Light\">Light</LSTag>. You cannot dual-wield <LSTag Tooltip=\"TwoHanded\">Two-Handed</LSTag> weapons.<br><br>When you take the Attack action on your turn and attack with a melee weapon, you can make one Off-Hand Attack as a Bonus Action later on the same turn. If you have mastered the Nick property and have a Nick weapon equipped in your off hand, you can make up to two Off-Hand Attacks per turn.":
        "Ви можете битися двома видами зброї, навіть якщо вони не <LSTag Tooltip=\"Light\">легкі</LSTag>. Водночас не можна одночасно використовувати дві <LSTag Tooltip=\"TwoHanded\">дворучні</LSTag> зброї.<br><br>Коли у свій хід ви виконуєте дію «Атака» й атакуєте зброєю ближнього бою, пізніше цього самого ходу можете вторинною дією здійснити одну Атаку другою рукою. Якщо ви опанували властивість «Нік» і тримаєте в другій руці зброю з нею, то можете здійснювати до двох Атак другою рукою за хід.",
    """You gain <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on <LSTag Type=\"Skills\" Tooltip=\"Perception\">Perception</LSTag> <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> made to detect hidden objects and on <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag> made to avoid or resist traps.

You gain <LSTag Tooltip=\"Resistant\">Resistance</LSTag> to the damage dealt by traps.

You can see in the dark.""":
        """Ви отримуєте <LSTag Tooltip=\"Advantage\">перевагу</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> <LSTag Type=\"Skills\" Tooltip=\"Perception\">Відчуття</LSTag> для виявлення прихованих предметів і на <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> для уникнення пасток або спротиву їм.

Ви отримуєте <LSTag Tooltip=\"Resistant\">стійкість</LSTag> до шкоди від пасток.

Ви можете бачити в темряві.""",
    """Defy Death. You have Advantage on Death Saving Throws.

Speedy Recovery. You regains the maximum <LSTag Tooltip=\"HitPoints\">hit points</LSTag> possible when healed.""":
        """Кинути виклик смерті. Ви маєте перевагу на кидки протидії смерті.

Швидке відновлення. Під час зцілення ви відновлюєте найбільшу можливу кількість <LSTag Tooltip=\"HitPoints\">очок здоров’я</LSTag>.""",
    """Prerequisite: Dwarf

You have the blood of dwarf heroes flowing through your veins.

Whenever you take the Dodge action in combat, you can spend one Hit Die to heal yourself. Roll the die, add your Constitution modifier, and regain a number of hit points equal to the total (minimum of 1).""":
        """Необхідна умова: карлик

У ваших жилах тече кров карлицьких героїв.

Коли в бою ви виконуєте дію «Ухилення», то можете витратити одну кістку здоров’я, щоб зцілитися. Киньте її, додайте модифікатор статури й відновіть отриману кількість очок здоров’я (щонайменше 1).""",
    "Studying occult lore, you learn one Eldritch Invocation option of your choice from the warlock class. If the invocation has a prerequisite of any kind, you can choose that invocation only if you’re a warlock who meets the prerequisite.":
        "Вивчаючи окультні знання, ви опановуєте одну Древню інвокацію чаклуна на свій вибір. Якщо вона має будь-яку необхідну умову, ви можете вибрати її лише як чаклун, що відповідає цій умові.",
    # Feat descriptions, editorial batch 3.
    """Prerequisite: Elf or half-elf

The accuracy of elves is legendary, especially that of elf archers and spellcasters. You have uncanny aim with attacks that rely on precision rather than brute force.

Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once.""":
        """Необхідна умова: ельф або напівельф

Ельфійська влучність легендарна, особливо серед лучників і заклиначів. Ви надприродно точні в атаках, що покладаються на вправність, а не грубу силу.

Коли ви маєте перевагу на кидок атаки зі спритністю, інтелектом, мудрістю чи харизмою, можете один раз перекинути одну з кісток.""",
    """Speak with Animals. You always have the Speak with Animals spell prepared and can cast it with any spell slots you have.

Tag Team. When you take the Help action, you can switch places with a willing ally within 5 feet of yourself as part of that same action. This movement doesn’t provoke Opportunity Attacks.""":
        """Розмова з тваринами. У вас завжди підготовлене закляття «Розмова з тваринами», і ви можете проказувати його, витрачаючи будь-які наявні чарунки заклять.

Злагоджена пара. Виконуючи дію «Допомога», ви можете в межах цієї самої дії помінятися місцями з охочим союзником у межах 5 футів від вас. Таке переміщення не провокує Принагідних атак.""",
    "You always have the Spike Growth spell prepared. You can cast it once without expending a spell slot, and you regain the ability to do so when you finish a Short Rest. When you cast the spell in this way, it doesn’t require Concentration.":
        "У вас завжди підготовлене закляття «Приріст шипів». Ви можете один раз проказати його, не витрачаючи чарунки заклять, і відновлюєте цю можливість після короткого відпочинку. Проказане в такий спосіб закляття не потребує зосередження.",
    """Prerequisite: Gnome

Your people are clever, with a knack for illusion magic. You have learned a magical trick for fading away when you suffer harm.

Immediately after you take damage, you can use a reaction to magically become invisible until the end of your next turn or until you attack, deal damage, or force someone to make a saving throw. Once you use this ability, you can’t do so again until you finish a short or long rest.""":
        """Необхідна умова: гном

Ваш народ кмітливий і має хист до магії ілюзій. Ви вивчили магічний трюк, що дає змогу зникати після поранення.

Одразу після отримання шкоди ви можете застосувати реагування й магічно стати невидимим до кінця свого наступного ходу або доки не атакуєте, не завдасте шкоди чи не змусите когось виконати кидок протидії. Після цього здатність відновиться лише по завершенні короткого або довгого відпочинку.""",
    """Faerie Trod Trotter. When you take the Disengage action on your turn, Difficult Terrain doesn’t cost you extra movement for the rest of that turn.

Flustering Strike. When you hit a creature with an attack roll, you can attempt to fluster the target. The target must succeed on a Wisdom saving throw (DC 8 plus the ability modifier of the score increased by this feat and your Proficiency Bonus) or have Disadvantage on saving throws until the end of your next turn.

You can use this benefit a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.""":
        """Мандрівник фейськими стежками. Після виконання дії «Відступ» складний рельєф не потребує від вас додаткового переміщення до кінця цього ходу.

Бентежний удар. Влучивши в істоту кидком атаки, ви можете спробувати збентежити її. Ціль повинна успішно виконати кидок протидії мудрістю (МС 8 + модифікатор характеристики, підвищеної цією рисою, + ваш бонус спеціалізації), інакше матиме заваду на кидки протидії до кінця вашого наступного ходу.

Цю перевагу можна застосувати кількість разів, що дорівнює вашому бонусу спеціалізації. Усі витрачені застосування відновлюються після довгого відпочинку.""",
    "Choose one 1st-level spell from the Divination or Enchantment school. You always have that spell and Misty Step prepared. You also gain one 1st-level spell slot and one 2nd-level spell slot.":
        "Виберіть одне закляття 1-го рівня зі школи віщування або зачарування. Це закляття та «Маревний крок» завжди підготовлені. Ви також отримуєте одну чарунку заклять 1-го рівня й одну чарунку 2-го рівня.",
    """The Black Arrow that brought down Smaug the Dragon may have been fated to do so, but the hand that sent it flying so fiercely was exceedingly strong. When you throw a spear or bend your bow, you make sure that your grip is steady and your aim true.

When making an attack with a ranged weapon, you use your Strength modifier for the attack and damage rolls. You must use the same modifier for both rolls. If you move no more than half your speed on the same turn and you hit a creature with a ranged weapon attack, you can use a bonus action to cause the attack to deal 1d4 extra damage of the weapon’s type.""":
        """Можливо, Чорній Стрілі судилося повалити дракона Смоґа, але рука, що випустила її з такою силою, була надзвичайно міцною. Кидаючи спис або напинаючи лук, ви твердо тримаєте зброю й точно цілитеся.

Атакуючи далекобійною зброєю, ви використовуєте модифікатор сили для кидків атаки та шкоди; для обох кидків слід застосовувати той самий модифікатор. Якщо цього ходу ви перемістилися не більш ніж на половину своєї швидкості й влучили в істоту далекобійною зброєю, то можете вторинною дією завдати цією атакою ще 1d4 шкоди того самого типу.""",
    "Your martial training has helped you develop a particular style of fighting. As a result, you learn one Fighting Style option of your choice from the fighter class.":
        "Бойова підготовка допомогла вам виробити власний стиль. Ви опановуєте один Бойовий стиль бійця на свій вибір.",
    """Prerequisite: Tiefling

You learn to call on hellfire to serve your commands.

When you roll fire damage for a spell you cast, you can reroll any 1 on the fire damage dice.

Whenever you cast a spell that deals fire damage, you can cause flames to wreathe you until the end of your next turn. While these flames are present, any creature that hits you with a melee attack takes 1d4 fire damage.""":
        """Необхідна умова: бісин

Ви вчитеся підкоряти пекельний вогонь своїй волі.

Коли ви кидаєте кістки вогняної шкоди проказаного закляття, то можете перекинути кожну 1.

Щоразу, коли ви проказуєте закляття з вогняною шкодою, можете оповити себе полум’ям до кінця наступного ходу. Поки воно палає, кожна істота, що влучає у вас атакою ближнього бою, зазнає 1d4 вогняної шкоди.""",
    "You gain two 1st-level spell slot and one 2nd-level spell slot.":
        "Ви отримуєте дві чарунки заклять 1-го рівня й одну чарунку 2-го рівня.",
    # Feat descriptions, editorial batch 4.
    """Your folk have seen many defeats, and many fruitless victories in their wars against the Shadow. The deadly rage that your kindred harbour for the Enemy infuses your weapons with a gleam of chill flame.

As a bonus action, you can cause a melee weapon you are wielding to emit dim light in a 10-foot radius for 10 turns. The light is sunlight. While the weapon gleams, it deals radiant damage instead of its normal damage type.

When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it.""":
        """Ваш народ зазнав багатьох поразок і здобув чимало марних перемог у війнах проти Тіні. Смертоносна лють вашого роду до Ворога насичує зброю відблиском холодного полум’я.

Вторинною дією ви можете змусити зброю ближнього бою у своїх руках протягом 10 ходів випромінювати тьмяне сонячне світло в радіусі 10 футів. Поки зброя сяє, вона завдає променевої шкоди замість звичайного типу.

Коли ви завдаєте критичного влучання атакою зброєю ближнього бою, то можете ще раз кинути одну кістку шкоди зброї й додати результат.""",
    """Studying funeral rites and tending the dead’s rest has made you a conduit between the worlds of the living and the dead. You gain the following benefits.

Divine Channel. You gain one use of the Channel Divinity feature from the Cleric class, and you can create the Turn Undead effect with it. If you already have Channel Divinity, you add this use to the feature from one class of your choice.""":
        """Вивчення поховальних обрядів і турбота про спокій померлих зробили вас провідником між світами живих і мертвих. Ви отримуєте такі переваги.

Божественний канал. Ви отримуєте одне застосування класової особливості клірика «Боже наснаження» й можете витратити його на «Вигнання невмерлих». Якщо ви вже маєте «Боже наснаження», це застосування додається до однойменної особливості одного класу на ваш вибір.""",
    """Heavy Weapon Mastery. When you hit a creature with a weapon that has the Heavy property as part of the Attack action on your turn, you can cause the weapon to deal extra damage to the target. The extra damage equals your Proficiency Bonus.

Hew. Immediately after you score a Critical Hit with a Melee weapon or reduce a creature to 0 Hit Points with one, you can make one attack with the same weapon as a Bonus Action.""":
        """Майстерність важкої зброї. Коли у свій хід ви влучаєте в істоту зброєю з властивістю «Важка» в межах дії «Атака», можете завдати цілі додаткової шкоди в кількості, що дорівнює вашому бонусу спеціалізації.

Розсікання. Одразу після критичного влучання зброєю ближнього бою або зменшення нею очок здоров’я істоти до 0 ви можете вторинною дією здійснити ще одну атаку тією самою зброєю.""",
    """Instrument Training. You gain proficiency with Musical Instruments.

Distracting Melody. When you take the Distract action to assist an ally’s attack roll, the enemy you’re distracting can be within 30 feet of you, rather than within 5 feet of you, provided the enemy can see or hear you.""":
        """Гра на інструментах. Ви отримуєте володіння музичними інструментами.

Відволікальна мелодія. Коли ви виконуєте дію «Відволікти», щоб допомогти союзникові з кидком атаки, ворог може перебувати в межах 30 футів від вас замість 5 футів, якщо бачить або чує вас.""",
    """Withering Wordplay. When you take the Distract action to assist an ally’s attack roll against an enemy, that enemy also has Disadvantage on the first saving throw it makes before the start of your next turn.

Inspiring Willpower. You have Advantage on saving throws against the Frightened and Paralyzed conditions.""":
        """Убивча гра слів. Коли ви виконуєте дію «Відволікти», щоб допомогти кидку атаки союзника проти ворога, цей ворог також має заваду на перший кидок протидії до початку вашого наступного ходу.

Натхненна сила волі. Ви маєте перевагу на кидки протидії станам переляку й паралічу.""",
    """Battle Medic. You gain the ability to restore Hit Points to a creature equal to 1d8. You can use this ability a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.

Healing. Each time you restore Hit Points to a creature, it regains additional Hit Points equal to your Proficiency Bonus.""":
        """Бойовий медик. Ви отримуєте здатність відновити істоті 1d8 очок здоров’я. Здатність можна застосувати кількість разів, що дорівнює вашому бонусу спеціалізації. Усі витрачені застосування відновлюються після довгого відпочинку.

Зцілення. Щоразу, коли ви відновлюєте істоті очки здоров’я, вона додатково відновлює їх у кількості, що дорівнює вашому бонусу спеціалізації.""",
    "You gain <LSTag Tooltip=\"ArmourProficiency\">Armour Proficiency</LSTag> with Heavy Armour.":
        "Ви отримуєте <LSTag Tooltip=\"ArmourProficiency\">володіння</LSTag> важкими обладунками.",
    "Damage Reduction. When you’re hit by an attack while you’re wearing Heavy armor, any Bludgeoning, Piercing, and Slashing damage dealt to you by that attack is reduced by an amount equal to your Proficiency Bonus.":
        "Зменшення шкоди. Коли атака влучає у вас, поки ви носите важкі обладунки, завдана нею дробильна, колюча й рубана шкода зменшується на ваш бонус спеціалізації.",
    """Prerequisite: Tiefling

Fiendish blood runs strong in you, unlocking a resilience akin to that possessed by some fiends.

You have resistance to cold damage and poison damage.
You have advantage on saving throws against being poisoned.""":
        """Необхідна умова: бісин

У ваших жилах вирує кров нечистих, даруючи стійкість, властиву деяким із них.

Ви маєте стійкість до холодової шкоди та шкоди отрутою.
Ви маєте перевагу на кидки протидії отруєнню.""",
    "When you finish a Short or Long Rest, you can give an inspiring performance: a speech, song, or dance. You can use this feature once per Short Rest. When you do so, each ally within 30 feet of you gains Temporary Hit Points equal to your character level plus your Proficiency Bonus.":
        "Завершивши короткий або довгий відпочинок, ви можете влаштувати натхненний виступ — виголосити промову, заспівати чи станцювати. Цю особливість можна застосувати один раз за короткий відпочинок. Кожен союзник у межах 30 футів від вас отримує тимчасові очки здоров’я в кількості, що дорівнює вашому рівню персонажа + бонус спеціалізації.",
    # Feat descriptions, editorial batch 5.
    "Armor Training. You gain training with Light armor and Shields.":
        "Володіння обладунками. Ви отримуєте володіння легкими обладунками та щитами.",
    "Standard Bearer. You are immune to the Prone, Charmed, and Frightened conditions.":
        "Прапороносець. Ви маєте імунітет до станів повалення, причарування та переляку.",
    """Inspiring Strike. Once per turn when you score a Critical Hit against a creature, you gain Heroic Inspiration.

Reassert Honor. When an enemy you can see deals damage to you, you have Advantage on your next attack roll against that enemy before the end of your next turn.""":
        """Надихальний удар. Один раз за хід, коли ви завдаєте істоті критичного влучання, ви отримуєте героїчне натхнення.

Відновлення честі. Коли видимий вам ворог завдає вам шкоди, ви отримуєте перевагу на свій наступний кидок атаки проти нього до кінця свого наступного ходу.""",
    "You gain a number of <LSTag Type=\"ActionResource\" Tooltip=\"LuckPoint\">Luck Points</LSTag> equal to your proficiency bonus. You can use these points to gain <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag>, <LSTag Tooltip=\"AbilityCheck\">Ability Checks</LSTag>, or <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>, or to make an enemy reroll an <LSTag Tooltip=\"AttackRoll\">Attack Roll</LSTag>.":
        "Ви отримуєте <LSTag Type=\"ActionResource\" Tooltip=\"LuckPoint\">очки удачі</LSTag> в кількості, що дорівнює вашому бонусу спеціалізації. Їх можна витрачати, щоб отримувати <LSTag Tooltip=\"Advantage\">перевагу</LSTag> на <LSTag Tooltip=\"AttackRoll\">кидки атаки</LSTag>, <LSTag Tooltip=\"AbilityCheck\">перевірки характеристик</LSTag> чи <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> або змушувати ворога перекинути <LSTag Tooltip=\"AttackRoll\">кидок атаки</LSTag>.",
    """Concentration Breaker. When you damage a creature that is concentrating, it has Disadvantage on the saving throw it makes to maintain Concentration.

Guarded Mind. If you fail an Intelligence, a Wisdom, or a Charisma saving throw, you can cause yourself to succeed instead. Once you use this benefit, you can’t use it again until you finish a Short or Long Rest.""":
        """Порушення зосередження. Коли ви завдаєте шкоди істоті, що зосереджується, вона має заваду на кидок протидії для збереження зосередження.

Захищений розум. Проваливши кидок протидії інтелектом, мудрістю чи харизмою, ви можете натомість досягти успіху. Після застосування цієї переваги ви не зможете скористатися нею знову до завершення короткого або довгого відпочинку.""",
    "You learn 2 <LSTag Tooltip=\"Cantrip\">cantrips</LSTag> and a Level 1 spell from the cleric spell list.":
        "Ви вивчаєте 2 <LSTag Tooltip=\"Cantrip\">замовляння</LSTag> та одне закляття 1-го рівня зі списку заклять клірика.",
    "You learn 2 <LSTag Tooltip=\"Cantrip\">cantrips</LSTag> and a Level 1 spell from the druid spell list.":
        "Ви вивчаєте 2 <LSTag Tooltip=\"Cantrip\">замовляння</LSTag> та одне закляття 1-го рівня зі списку заклять друїда.",
    # Feat descriptions, editorial batch 6.
    "You learn 2 <LSTag Tooltip=\"Cantrip\">cantrips</LSTag> and a Level 1 spell from the wizard spell list.":
        "Ви вивчаєте 2 <LSTag Tooltip=\"Cantrip\">замовляння</LSTag> та одне закляття 1-го рівня зі списку заклять чарівника.",
    """You learn two Metamagic options of your choice from the sorcerer class. You can use only one Metamagic option on a spell when you cast it, unless the option says otherwise.
You gain 2 sorcery points to spend on Metamagic (these points are added to any sorcery points you have from another source but can be used only on Metamagic). You regain all spent sorcery points when you finish a long rest.""":
        """Ви вивчаєте два варіанти метамагії чародія на свій вибір. Під час проказування закляття можна застосувати лише один варіант метамагії, якщо в його описі не зазначено інакше.
Ви отримуєте 2 очки чародійства, які можна витрачати лише на метамагію. Вони додаються до очок чародійства з інших джерел. Усі витрачені очки відновлюються після довгого відпочинку.""",
    """Speed Increase. Your Speed increases by 10 feet.

Dash over <LSTag Type=\"Status\" Tooltip=\"DIFFICULT_TERRAIN\">Difficult Terrain</LSTag>. When you take the Dash action on your turn, Difficult Terrain doesn't cost you extra movement for the rest of that turn.

Agile Movement. Opportunity Attacks have Disadvantage against you.""":
        """Збільшення швидкості. Ваша швидкість збільшується на 10 футів.

Ривок крізь <LSTag Type=\"Status\" Tooltip=\"DIFFICULT_TERRAIN\">складний рельєф</LSTag>. Коли у свій хід ви виконуєте дію «Ривок», складний рельєф не потребує додаткового переміщення до кінця цього ходу.

Спритне переміщення. Принагідні атаки проти вас мають заваду.""",
    "While you are mounted on the steed, you have Advantage on melee attack rolls against creatures of Small size or smaller. In addition, while mounted, you can’t be dismounted or knocked prone as a result of taking damage.":
        "Перебуваючи верхи, ви маєте перевагу на кидки атаки ближнього бою проти Малих або менших істот. Крім того, отримана шкода не може скинути вас із сідла чи повалити.",
    "Your spellcasting can unleash surges of untamed magic. Once per turn, you can roll 1d20 immediately after you cast a spell with a spell slot. If you roll a 20, roll on the Wild Magic Surge table to create a magical effect.":
        "Ваші закляття здатні вивільняти сплески неприборканої магії. Один раз за хід, одразу після проказування закляття з витратою чарунки, ви можете кинути 1d20. Якщо випаде 20, киньте кістку за таблицею «Сплеск дикої магії», щоб створити магічний ефект.",
    """Your skill (or fortune?) in battle has increased with your growth in experience.

You gain a +1 bonus to AC. You lose this bonus if you are incapacitated or wielding a shield.""":
        """З досвідом зросла ваша бойова вправність — чи, може, удача?

Ви отримуєте бонус +1 до РЗ. У стані недієздатності або зі щитом у руках ви втрачаєте цей бонус.""",
    """Prerequisite: Half-orc

When you land a <LSTag Tooltip=\"CriticalHit\">Critical Hit</LSTag> with a melee weapon attack, you deal an extra dice of weapon damage. """:
        """Необхідна умова: напіворк

Коли ви завдаєте <LSTag Tooltip=\"CriticalHit\">критичного влучання</LSTag> атакою зброєю ближнього бою, то кидаєте одну додаткову кістку шкоди зброї. """,
    "While you are using Stand as One (Tyro of the Gauntlet), allies within 5 feet of you are immune to the Prone condition and have Advantage on Strength saving throws.":
        "Поки ви застосовуєте «Стояти разом» («Неофіт Рукавиці»), союзники в межах 5 футів від вас мають імунітет до стану повалення й перевагу на кидки протидії силою.",
    """Instrument Training. You gain proficiency with three Musical Instruments.

Encouraging Song. As you finish a Short or Long Rest, you can play a song on a Musical Instrument with which you have proficiency and give Heroic Inspiration to allies who hear the song. The number of allies you can affect in this way equals your Proficiency Bonus.""":
        """Гра на інструментах. Ви отримуєте володіння трьома музичними інструментами.

Підбадьорлива пісня. Завершивши короткий або довгий відпочинок, ви можете виконати пісню на музичному інструменті, яким володієте, і надати героїчне натхнення союзникам, що її почують. Кількість таких союзників дорівнює вашому бонусу спеціалізації.""",
    # Feat descriptions, editorial batch 7.
    """Puncture. Once per turn, when you hit a creature with an attack that deals Piercing damage, you can reroll one of the attack’s damage dice, and you must use the new roll.

Enhanced Critical. When you score a Critical Hit that deals Piercing damage to a creature, you can roll one additional damage die when determining the extra Piercing damage the target takes.""":
        """Прокол. Один раз за хід, коли ви влучаєте в істоту атакою з колючою шкодою, можете перекинути одну кістку шкоди цієї атаки й мусите використати новий результат.

Посилене критичне влучання. Коли ви завдаєте істоті критичного влучання з колючою шкодою, можете кинути ще одну кістку, визначаючи додаткову колючу шкоду цілі.""",
    """Potent Poison. Spells you cast and attacks you make ignore <LSTag Tooltip=\"Resistant\">Resistance</LSTag> to Poison damage. In addition, when you deal Poison damage with a spell, you cannot roll a 1. 

Brew Poison. You gain a Poisoner’s Kit, and you have proficiency with them. When you deal poison damage to a creature, it must succeed on a Constitution saving throw or become Poisoned.""":
        """Могутня отрута. Ваші закляття й атаки ігнорують <LSTag Tooltip=\"Resistant\">стійкість</LSTag> до шкоди отрутою. Крім того, кістки шкоди отрутою від ваших заклять не можуть дати результат 1. 

Варіння отрути. Ви отримуєте набір отруйника й володіння ним. Коли ви завдаєте істоті шкоди отрутою, вона повинна успішно виконати кидок протидії статурою, інакше набуде стану отруєння.""",
    """Pole Strike. Immediately after you take the Attack action and attack with a Quarterstaff, a Spear, or a weapon that has the Heavy and Reach properties, you can use a Bonus Action to make a melee attack with the opposite end of the weapon. The weapon deals Bludgeoning damage, and the weapon’s damage die for this attack is a d4.

Reactive Strike. While you’re holding a Quarterstaff, a Spear, or a weapon that has the Heavy and Reach properties, you can take a Reaction to make one melee attack against a creature that enters the reach you have with that weapon.""":
        """Удар держаком. Одразу після дії «Атака» з палицею, списом або зброєю з властивостями «Важка» й «Досяжність» ви можете вторинною дією атакувати в ближньому бою протилежним кінцем зброї. Така атака завдає дробильної шкоди, а її кістка шкоди — d4.

Випереджальний удар. Тримаючи палицю, спис або зброю з властивостями «Важка» й «Досяжність», ви можете застосувати реагування й атакувати в ближньому бою істоту, що входить у межі досяжності цієї зброї.""",
    """Encourage Ally. As a Bonus Action, you bolster one ally you can see within 30 feet. That ally gains Temporary Hit Points equal to 2d6 plus your Proficiency Bonus. You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.

Last Stand. You have Advantage on attack rolls while Bloodied.""":
        """Підбадьорити союзника. Вторинною дією ви зміцнюєте одного видимого союзника в межах 30 футів. Він отримує тимчасові очки здоров’я в кількості 2d6 + ваш бонус спеціалізації. Цю вторинну дію можна застосувати кількість разів, що дорівнює вашому бонусу спеціалізації. Усі витрачені застосування відновлюються після довгого відпочинку.

Останній рубіж. У закривавленому стані ви маєте перевагу на кидки атаки.""",
    """Entreat. You gain proficiency in <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>.

Rallying Cry. You can choose a number of creatures equal to your Proficiency Bonus that you can see within 30 feet of yourself. Those creatures gain Heroic Inspiration. Once you use this benefit, you can’t do so again until you finish a Long Rest.""":
        """Прохання. Ви отримуєте володіння навичкою <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag>.

Бойовий клич. Виберіть видимих вам істот у межах 30 футів від себе в кількості, що дорівнює вашому бонусу спеціалізації. Вони отримують героїчне натхнення. Після застосування цієї переваги ви не зможете скористатися нею знову до завершення довгого відпочинку.""",
    "Rune Magic. You know two runes of your choice from the Rune Spells table. You learn the 1st-level spells associated with those runes, as shown in the Rune Spells table. You gain one 1st-level spell slot, which can be used only to cast these spells. You can also cast the spells associated with your runes using any other spell slots you have.":
        "Магія рун. Виберіть дві руни з таблиці «Рунні закляття». Ви вивчаєте пов’язані з ними закляття 1-го рівня, зазначені в таблиці, й отримуєте одну чарунку 1-го рівня, яку можна витрачати лише на ці закляття. Крім того, їх можна проказувати з будь-яких інших наявних чарунок.",
    "When making weapon attacks, you roll your damage dice twice and use the highest result.":
        "Атакуючи зброєю, ви двічі кидаєте кістки шкоди й використовуєте вищий результат.",
    """When an enemy within melee range attacks an ally, you can use a <LSTag Type=\"ActionResource\" Tooltip=\"ReactionActionPoint\">reaction</LSTag> to make a weapon attack against that enemy. Target ally must not have the Sentinel Feat.

You gain <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on <LSTag Tooltip=\"OpportunityAttack\">Opportunity Attacks</LSTag>, and when you hit a creature with an Opportunity Attack, it can no longer move for the rest of its turn.""":
        """Коли ворог у межах ближнього бою атакує союзника, ви можете застосувати <LSTag Type=\"ActionResource\" Tooltip=\"ReactionActionPoint\">реагування</LSTag> і атакувати цього ворога зброєю. Союзник не повинен мати рису «Вартовий».

Ви отримуєте <LSTag Tooltip=\"Advantage\">перевагу</LSTag> на <LSTag Tooltip=\"OpportunityAttack\">Принагідні атаки</LSTag>. Коли ви влучаєте Принагідною атакою, істота більше не може переміщуватися до кінця свого ходу.""",
    "Choose one 1st-level spell from the Illusion or Necromancy school. You always have that spell and <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility\">Invisibility</LSTag> prepared. You also gain one 1st-level spell slot and one 2nd-level spell slot.":
        "Виберіть одне закляття 1-го рівня зі школи ілюзій або некромантії. Це закляття та <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility\">Невидимість</LSTag> завжди підготовлені. Ви також отримуєте одну чарунку заклять 1-го рівня й одну чарунку 2-го рівня.",
    """Bypass Cover. Your <LSTag Tooltip=\"RangedWeaponAttack\">ranged weapon attacks</LSTag> do not receive penalties from <LSTag Tooltip=\"HighGroundRules\">High Ground Rules</LSTag>.

Firing in Melee. Being within 5 feet of an enemy doesn’t impose Disadvantage on your attack rolls with Ranged weapons.

Long Shots. Attacking with a two-handed ranged weapon increases its normal range to 90 feet.""":
        """Обхід укриття. Ваші <LSTag Tooltip=\"RangedWeaponAttack\">атаки далекобійною зброєю</LSTag> не зазнають штрафів від <LSTag Tooltip=\"HighGroundRules\">правил височини</LSTag>.

Стрільба в ближньому бою. Перебування в межах 5 футів від ворога не накладає завади на кидки атаки далекобійною зброєю.

Далекі постріли. Звичайна дальність атак дворучною далекобійною зброєю збільшується до 90 футів.""",
    # Feat descriptions, editorial batch 8.
    """Shield Bash. If you attack a creature within 5 feet of you as part of the Attack action and hit with a Melee weapon, you can immediately bash the target with your Shield if it’s equipped, forcing the target to make a Strength saving throw (DC 8 plus your Strength modifier and Proficiency Bonus). On a failed save, you either push the target 5 feet from you or cause it to have the Prone condition (your choice). You can use this benefit only once on each of your turns.

Interpose Shield. If you’re subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you can take a Reaction to take no damage if you succeed on the saving throw and are holding a Shield.""":
        """Удар щитом. Якщо в межах дії «Атака» ви атакуєте істоту в межах 5 футів і влучаєте зброєю ближнього бою, то можете негайно вдарити ціль спорядженим щитом. Вона повинна виконати кидок протидії силою (МС 8 + ваш модифікатор сили + бонус спеціалізації). У разі невдачі на ваш вибір відштовхніть ціль на 5 футів або надайте їй стан повалення. Цю перевагу можна застосувати лише раз за хід.

Підставити щит. Якщо ефект дає вам змогу виконати кидок протидії спритністю, щоб зазнати лише половини шкоди, ви можете застосувати реагування: у разі успішного кидка ви не зазнаєте шкоди, якщо тримаєте щит.""",
    """Skill Proficiency. You gain proficiency in one skill of your choice.

Expertise. Choose one skill in which you have proficiency but lack Expertise. You gain Expertise with that skill.""":
        """Володіння навичкою. Ви отримуєте володіння однією навичкою на свій вибір.

Вправність. Виберіть одну навичку, якою володієте, але в якій іще не маєте Вправності. Ви отримуєте Вправність у цій навичці.""",
    """Blindsight. You have Blindsight with a range of 10 feet.

Fog of War. The DC to become Invisible when you take the Hide action is 15 instead of 20.""":
        """Сліпозір. Ви отримуєте сліпозір на 10 футів.

Туман війни. МС для набуття невидимості під час дії «Сховатися» дорівнює 15 замість 20.""",
    """Hamstring. Once per turn when you hit a creature with an attack that deals Slashing damage, you can reduce the Speed of that creature by 10 feet until the start of your next turn.

Enhanced Critical. When you score a Critical Hit that deals Slashing damage to a creature, it has Disadvantage on attack rolls until the start of your next turn.""":
        """Підрізання сухожилля. Один раз за хід, коли ви влучаєте в істоту атакою з рубаною шкодою, можете зменшити її швидкість на 10 футів до початку свого наступного ходу.

Посилене критичне влучання. Коли ви завдаєте істоті критичного влучання з рубаною шкодою, вона має заваду на кидки атаки до початку вашого наступного ходу.""",
    """Bypass Cover. Your ranged spell attacks do not receive penalties from <LSTag Tooltip=\"HighGroundRules\">High Ground Rules</LSTag>.

Casting in Melee. Being within 5 feet of an enemy doesn’t impose Disadvantage on your attack rolls with spells.

Increased Range. Increase the range of spells by 50%.""":
        """Обхід укриття. Ваші далекобійні атаки закляттями не зазнають штрафів від <LSTag Tooltip=\"HighGroundRules\">правил височини</LSTag>.

Проказування в ближньому бою. Перебування в межах 5 футів від ворога не накладає завади на ваші кидки атаки закляттями.

Збільшена дальність. Дальність заклять збільшується на 50%.""",
    "Spells you cast and attacks you make ignore <LSTag Tooltip=\"Resistant\">Resistance</LSTag> to Radiant damage. In addition, when you deal Radiant damage with a spell, you cannot roll a 1. ":
        "Ваші закляття й атаки ігнорують <LSTag Tooltip=\"Resistant\">стійкість</LSTag> до променевої шкоди. Крім того, кістки променевої шкоди від ваших заклять не можуть дати результат 1. ",
    """Magic Absorption. Once per turn, when you take damage from a spell or magical effect, you reduce the total damage taken by 1d4.

Spellfire Flame. You learn the Sacred Flame cantrip. You can also cast this cantrip as a Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Long Rest.""":
        """Поглинання магії. Один раз за хід, коли ви зазнаєте шкоди від закляття чи магічного ефекту, зменште загальну отриману шкоду на 1d4.

Полум’я чаровогню. Ви вивчаєте замовляння «Священний вогонь». Крім того, ви можете проказати його вторинною дією кількість разів, що дорівнює вашому бонусу спеціалізації. Усі витрачені застосування відновлюються після довгого відпочинку.""",
    """Prerequisite: Dwarf or a Small race

You are uncommonly nimble for your race.

Increase your walking speed by 5 feet.
You gain proficiency in the <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Acrobatics</LSTag> or <LSTag Type=\"Skills\" Tooltip=\"Athletics\">Athletics</LSTag> skill (your choice).
You have advantage on any Strength (Athletics) or Dexterity (Acrobatics) check you make to escape from being restrained.""":
        """Необхідна умова: карлик або Малий вид

Ви надзвичайно спритні як на свій зріст.

Ваша швидкість ходьби збільшується на 5 футів.
Ви отримуєте володіння навичкою <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Акробатика</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Athletics\">Атлетизм</LSTag> на свій вибір.
Ви маєте перевагу на перевірки сили (Атлетизм) або спритності (Акробатика), щоб звільнитися зі стану знерухомлення.""",
    "You can cast more than one spell that uses a spell slot on your turn. Once you use this benefit, you can’t do so again until you finish a Long Rest.":
        "У свій хід ви можете проказати більш ніж одне закляття, що витрачає чарунку. Після застосування цієї переваги ви не зможете скористатися нею знову до завершення довгого відпочинку.",
    "When making unarmed attacks, you roll your damage dice twice and use the highest result.":
        "Атакуючи без зброї, ви двічі кидаєте кістки шкоди й використовуєте вищий результат.",
    # Feat descriptions, editorial batch 9.
    "Stand as One. When an ally within 5 feet of you is subjected to an effect that would push or pull it, you can take a Reaction to prevent that ally from being pushed or pulled. To receive this benefit, the ally can’t have the Incapacitated condition.":
        "Стояти разом. Коли союзник у межах 5 футів від вас зазнає ефекту, що має штовхнути або притягнути його, ви можете застосувати реагування, щоб завадити цьому переміщенню. Союзник не повинен перебувати в стані недієздатності.",
    """You gain <LSTag Tooltip="Advantage">Advantage</LSTag> on <LSTag Tooltip="SavingThrow">Saving Throws</LSTag> to maintain <LSTag Tooltip="Concentration">Concentration</LSTag> on a spell.

You can also use a <LSTag Type="ActionResource" Tooltip="ReactionActionPoint">reaction</LSTag> to cast <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Shocking Grasp</LSTag> at a target moving out of melee range.""":
        """Ви отримуєте <LSTag Tooltip="Advantage">перевагу</LSTag> на <LSTag Tooltip="SavingThrow">кидки протидії</LSTag> для збереження <LSTag Tooltip="Concentration">зосередження</LSTag> на заклятті.

Крім того, ви можете застосувати <LSTag Type="ActionResource" Tooltip="ReactionActionPoint">реагування</LSTag>, щоб проказати <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Шоковий хват</LSTag> на ціль, яка виходить із меж ближнього бою.""",
    """You gain <LSTag Tooltip="Proficiency">Proficiency</LSTag> with martial weapons.

You gain two weapon mastery properties of your choice.""":
        """Ви отримуєте <LSTag Tooltip="Proficiency">володіння</LSTag> бойовою зброєю.

Ви отримуєте дві властивості майстерності зброї на свій вибір.""",
    """Exploit Opening. When you roll damage for an Opportunity Attack, you can roll the damage dice twice and use either roll against the target.

Family First. Once per Long Rest, you grant yourself and allies within 30 feet of you Advantage on Initiative rolls.""":
        """Скористатися нагодою. Визначаючи шкоду від Принагідної атаки, ви можете двічі кинути кістки шкоди й вибрати один із результатів проти цілі.

Родина понад усе. Один раз за довгий відпочинок ви надаєте собі та союзникам у межах 30 футів від вас перевагу на кидки ініціативи.""",
    """Retaliate. Immediately after a creature within 5 feet of you hits you with a melee attack, you can make an Opportunity Attack against that creature.

Versatile Merc. Choose a skill in which you have proficiency. You have Expertise in that skill.""":
        """Відплата. Одразу після того, як істота в межах 5 футів влучає у вас атакою ближнього бою, ви можете здійснити проти неї Принагідну атаку.

Універсальний найманець. Виберіть навичку, якою володієте. Ви отримуєте Вправність у цій навичці.""",
    # Core display names: backgrounds.
    "Dragon Cultist": "Культист Дракона",
    "Moonwell Pilgrim": "Прочанин місячних криниць",
    "Shadowmasters Exile": "Вигнанець Володарів Тіней",
    "Mulhorandi Tomb Raider": "Мулхорандський розкрадач гробниць",
    "Chondathan Freebooter": "Чондатанський флібустьєр",
    "Rest Warden": "Вартовий спочинку",
    "Genie Touched": "Торкнутий джином",
    "Wayfarer": "Мандрівник",
    "Zhentarim Mercenary": "Найманець Зентариму",
    "Guide": "Провідник",
    "Rashemi Wanderer": "Рашеменський мандрівник",
    "Dead Magic Dweller": "Мешканець зони мертвої магії",
    "Knight of the Gauntlet": "Лицар Панцерної Рукавиці",
    "Purple Dragon Squire": "Зброєносець Пурпурового Дракона",
    "Wicker Weaver": "Плетільник оберегів",
    "Emerald Enclave Caretaker": "Доглядач Смарагдового анклаву",
    "Experiment": "Піддослідний",
    "Lords' Alliance Vassal": "Васал Альянсу Лордів",
    "Harper": "Арфіст",
    "Farmer": "Фермер",
    # Core display names: classes and subclasses.
    "Aberrant Sorcery": "Аберрантне чаклунство",
    "Archfey Patron": "Покровитель-Архіфея",
    "Architect of Ruin": "Архітектор руїни",
    "Banneret": "Знаменосець",
    "Celestial Patron": "Покровитель-Небесник",
    "Circle of Dragons": "Коло драконів",
    "Circle of Dreams": "Коло мрій",
    "Clockwork Sorcery": "Механічне чаклунство",
    "Scion of the Three": "Нащадок Трійці",
    "Devourer Guild": "Гільдія пожирачів",
    "Fiend Patron": "Покровитель-Нечистий",
    "Path of the Fractured": "Шлях Розколотого",
    "Path of the Giant": "Шлях Велетня",
    "Oath of Glory": "Обіт Слави",
    "Great Old One Patron": "Покровитель-Величний древній",
    "Hellspeaker": "Пекломовець",
    "Hexblade Patron": "Покровитель-Відьомський клинок",
    "Warrior of Mercy": "Воїн Милосердя",
    "Mind Domain": "Домен Розуму",
    "College of the Moon": "Колегія Місяця",
    "Oath of the Noble Genies": "Обіт Шляхетних Джинів",
    "Spellfire Sorcery": "Чаклунство чаровогню",
    "College of Spirits": "Колегія Духів",
    "Path of the Wild Heart": "Шлях Дикого Серця",
    "Undead Patron": "Покровитель-Невмерлий",
    "Path of the World Tree": "Шлях Світового Дерева",
    "Path of the Zealot": "Шлях Ревнителя",
    # Core display names: progression choices.
    "Giant Ancestry": "Велетенське походження",
    # Core display names: feats.
    "Altered": "Змінений",
    "Charm Twister": "Плетільник оберегів",
    "Cold Caster": "Заклинач холоду",
    "Cult of the Dragon Initiate": "Посвячений Культу Дракона",
    "Death Defier": "Непідвладний смерті",
    "Dragon-Slayer": "Драконоборець",
    "Dragonscarred": "Позначений драконами",
    "Dwarven Fortitude": "Карлицька стійкість",
    "Emerald Enclave Fledgling": "Новак Смарагдового анклаву",
    "Fairy Trickster": "Фейський штукар",
    "Fey Touched": "Торкнутий феями",
    "Fighting Initiate": "Бойовий адепт",
    "Flames of Phlegethos": "Полум’я Флеґетосу",
    "Harper Agent": "Агент Арфістів",
    "Harper Teamwork": "Злагодженість Арфістів",
    "Infernal Constitution": "Пекельна статура",
    "Lordly Resolve": "Лордська рішучість",
    "Mounted Combatant": "Кінний боєць",
    "Mythal Touched": "Торкнутий міфалом",
    "Orders Resilience": "Стійкість Ордену",
    "Piercer": "Проколювач",
    "Purple Dragon Commandant": "Комендант Пурпурових Драконів",
    "Purple Dragon Rook": "Тура Пурпурового Дракона",
    "Rune Shaper": "Творець рун",
    "Skulker": "Скрадник",
    "Slasher": "Рубака",
    "Spellfire Adept": "Адепт чаровогню",
    "Squat Nimbleness": "Спритність малих народів",
    "Tyro of the Gauntlet": "Неофіт Панцерної Рукавиці",
    "Zhentarim Ruffian": "Зентаримський головоріз",
    "Zhentarim Tactics": "Тактика Зентариму",
    # QA follow-up: short labels and status text outside the core tables.
    "Feat: Spell Sniper (Ranged)": "Риса: Влучний заклинач (далекобійні атаки)",
    "Gain Temporary Hit Points equal to the spellcaster’s level plus their Proficiency Bonus.":
        "Отримайте тимчасові очки здоров’я в кількості, що дорівнює рівню заклинача + його бонусу спеціалізації.",
    "Gain Temporary Hit Points equal to 2d6 plus the spellcaster’s Proficiency Bonus.":
        "Отримайте тимчасові очки здоров’я в кількості 2d6 + бонус спеціалізації заклинача.",
    "This creature's mind has been bent to its caster's will and obeys their commands without question. The effect ends when the caster finishes a <LSTag Tooltip=\"LongRest\">Long Rest</LSTag>.":
        "Розум цієї істоти підкорено волі заклинача, і вона беззаперечно виконує його накази. Ефект завершується, коли заклинач закінчує <LSTag Tooltip=\"LongRest\">довгий відпочинок</LSTag>.",
    "Caught in the Emanation of <LSTag Type=\"Spell\" Tooltip=\"Target_ConjureElementals_Minor_Container\">Conjure Minor Elemental</LSTag>: the ground beneath this creature is Difficult Terrain, and it takes extra damage from the caster's attacks.":
        "Істота перебуває в еманації <LSTag Type=\"Spell\" Tooltip=\"Target_ConjureElementals_Minor_Container\">Прикликання малих стихійників</LSTag>: земля під нею є складним рельєфом, і вона зазнає додаткової шкоди від атак заклинача.",
    # Expanded mechanics QA: core conditions and weapon masteries.
    """While you have the Prone condition, you experience the following effects:

Restricted Movement: You must spend an amount of movement equal to half your Speed to stand up and end the condition. If your Speed is 0, you can’t stand up.

Attacks Affected: An attack roll against you has Advantage if the attacker is within [1] of you. Otherwise, that attack roll has Disadvantage.""":
        """Поки ви маєте стан повалення, на вас діють такі ефекти:

Обмежене переміщення. Щоб підвестися й завершити цей стан, ви мусите витратити переміщення в обсязі половини своєї швидкості. Якщо ваша швидкість дорівнює 0, ви не можете підвестися.

Зміна атак. Кидок атаки проти вас має перевагу, якщо нападник перебуває в межах [1] від вас. Інакше цей кидок має заваду.""",
    "If you hit a creature with a melee attack roll using this weapon, you can make a melee attack roll with the weapon against a second creature within [1] of the first that is also within your reach. On a hit, the second creature takes the weapon’s damage, but don’t add your ability modifier to that damage unless that modifier is negative. You can make this extra attack only once per turn.":
        "Якщо ви влучаєте в істоту атакою ближнього бою цією зброєю, то можете атакувати нею в ближньому бою другу істоту, що перебуває в межах [1] від першої та в межах вашої досяжності. У разі влучання друга істота зазнає шкоди зброї, але ви не додаєте до цієї шкоди модифікатор характеристики, якщо він не від’ємний. Цю додаткову атаку можна здійснити лише раз за хід.",
    "If your attack roll with this weapon misses a creature, you can deal damage to that creature equal to the ability modifier you used to make the attack roll. This damage is the same type dealt by the weapon, and the damage can be increased only by increasing the ability modifier.":
        "Якщо атака цією зброєю не влучає в істоту, ви можете завдати їй шкоди в кількості, що дорівнює модифікатору характеристики, використаному для кидка атаки. Тип цієї шкоди збігається з типом шкоди зброї, а збільшити її можна лише збільшивши модифікатор характеристики.",
    "If you hit a creature with this weapon, you can force the creature to make a Constitution saving throw (DC 8 plus the ability modifier used to make the attack roll and your Proficiency Bonus). On a failed save, the creature has the Prone condition.":
        "Якщо ви влучаєте в істоту цією зброєю, то можете змусити її виконати кидок протидії статурою (МС 8 + модифікатор характеристики, використаний для кидка атаки, + ваш бонус спеціалізації). У разі невдачі істота набуває стану повалення.",
    """You gain proficiency in another skill of your choice from the skill list available to Barbarians at level 1.

In addition, while your <LSTag Type="Status" Tooltip="RAGE">Rage</LSTag> is active, you can channel primal power when you attempt certain tasks; whenever you make an ability check using one of the following skills, you can make it as a Strength check even if it normally uses a different ability: <LSTag Type="Skills" Tooltip="Acrobatics">Acrobatics</LSTag>, <LSTag Type="Skills" Tooltip="Intimidation">Intimidation</LSTag>, <LSTag Type="Skills" Tooltip="Perception">Perception</LSTag>, <LSTag Type="Skills" Tooltip="Stealth">Stealth</LSTag>, or <LSTag Type="Skills" Tooltip="Survival">Survival</LSTag>. When you use this ability, your Strength represents primal power coursing through you, honing your agility, bearing, and senses.""":
        """Ви отримуєте володіння ще однією навичкою на свій вибір зі списку навичок, доступних варварам на 1-му рівні.

Крім того, поки діє ваша <LSTag Type="Status" Tooltip="RAGE">Лють</LSTag>, ви можете спрямовувати первісну силу на виконання певних завдань. Здійснюючи перевірку однієї з наведених навичок, ви можете виконати її як перевірку сили, навіть якщо зазвичай вона використовує іншу характеристику: <LSTag Type="Skills" Tooltip="Acrobatics">Акробатика</LSTag>, <LSTag Type="Skills" Tooltip="Intimidation">Залякування</LSTag>, <LSTag Type="Skills" Tooltip="Perception">Відчуття</LSTag>, <LSTag Type="Skills" Tooltip="Stealth">Непомітність</LSTag> або <LSTag Type="Skills" Tooltip="Survival">Виживання</LSTag>. У такому разі ваша сила уособлює первісну міць, що струменить крізь вас і загострює спритність, поставу та чуття.""",
    "You have a mind for tactics on and off the battlefield. You can expend a use of your Second Wind to push yourself toward success. You roll 1d10 and add the number rolled to the ability check, potentially turning it into a success.":
        "Ви вправні в тактиці як на полі бою, так і поза ним. Ви можете витратити застосування «Другого дихання», щоб збільшити свої шанси на успіх: киньте 1d10 і додайте результат до перевірки характеристики, потенційно перетворивши невдачу на успіх.",
    "Gain <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on your <LSTag Tooltip=\"AttackRoll\">Attack Roll</LSTag> or <LSTag Tooltip=\"SavingThrow\">Saving Throw</LSTag>.":
        "Отримайте <LSTag Tooltip=\"Advantage\">перевагу</LSTag> на свій <LSTag Tooltip=\"AttackRoll\">кидок атаки</LSTag> або <LSTag Tooltip=\"SavingThrow\">кидок протидії</LSTag>.",
    "You gain the Extra Attack feature for your pact weapon only. With that feature, you can attack twice with the weapon instead of once when you take the Attack action on your turn.":
        "Ви отримуєте особливість «Додаткова атака», але лише для своєї зброї договору. Завдяки цій особливості, виконуючи дію «Атака» у свій хід, ви можете атакувати цією зброєю двічі замість одного разу.",
    "Once per turn, when you hit a creature with your pact weapon, you can deal an extra 1d6 Necrotic damage to that creature. You also regain a number of Hit Points equal to 1d6 plus your Constitution modifier.":
        "Один раз за хід, коли ви влучаєте в істоту своєю зброєю договору, можете завдати їй додаткової некротичної шкоди 1d6. Ви також відновлюєте очки здоров’я в кількості 1d6 + ваш модифікатор статури.",
    "Gain Advantage on attack rolls and saving throws until the start of Barbarian's next turn.":
        "Отримайте перевагу на кидки атаки та кидки протидії до початку наступного ходу варвара.",
    """Affected entity is in the Ethereal Plane, where it can't be harmed, seen, or affected.

While in the Ethereal Plane, the entity can't move or interact with anything in the world. It can only choose to teleport up to [1].

At the end of each turn, there is a chance it reappears in the Material Plane.""":
        """Уражена істота перебуває на Ефірному плані, де її неможливо поранити, побачити чи піддати будь-якому впливу.

На Ефірному плані істота не може переміщуватися чи взаємодіяти зі світом. Вона може лише телепортуватися на відстань до [1].

Наприкінці кожного ходу істота може знову з’явитися на Матеріальному плані.""",
    # Expanded mechanics QA: Psi Warrior and Soulknife resource text.
    """You harbor a wellspring of psionic energy within yourself, represented by your Psionic Energy Dice, which fuel the powers granted by this subclass. As you gain levels in Fighter, both the size and number of these dice increase: at 3rd level, you have four d6s; at 5th level, six d8s; at 9th level, eight d8s; at 11th level, eight d10s.

Any features in this subclass that use a Psionic Energy Die use only the dice from this subclass. Some of your powers expend the Psionic Energy Die, as specified in a power’s description, and you can’t use a power if it requires you to use a die when all your Psionic Energy Dice are expended.

You regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them when you finish a Long Rest.

Protective Field. When you or another creature you can see within 30 feet of you takes damage, you can take a Reaction to expend one Psionic Energy Die, roll the die, and reduce the damage taken by the number rolled plus your Intelligence modifier (minimum reduction of 1), as you create a momentary shield of telekinetic force.

Psionic Strike. You can propel your weapons with psionic force. Once on each of your turns, immediately after you hit a target within 30 feet of yourself with an attack and deal damage to it with a weapon, you can expend one Psionic Energy Die, rolling it and dealing Force damage to the target equal to the number rolled plus your Intelligence modifier.

Telekinetic Movement. You can move an object or a creature with your mind. As a Magic action, choose one target you can see within 30 feet of yourself; the target must be a loose object that is Large or smaller or one willing creature other than you. You transport the target up to 30 feet to an unoccupied space you can see. Alternatively, if the target is a Tiny object, you can transport it to or from your hand.""":
        """У вас міститься джерело псіонічної енергії, уособлене кістками псіонічної енергії, які живлять сили цього підкласу. Зі здобуттям рівнів бійця кількість і розмір цих кісток зростають: на 3-му рівні ви маєте чотири d6, на 5-му — шість d8, на 9-му — вісім d8, а на 11-му — вісім d10.

Усі особливості цього підкласу, що використовують кістку псіонічної енергії, використовують лише кістки, отримані від цього підкласу. Деякі сили витрачають таку кістку, як зазначено в їхніх описах. Якщо сила потребує кістки, а ви витратили їх усі, застосувати цю силу неможливо.

Завершивши короткий відпочинок, ви відновлюєте одну витрачену кістку псіонічної енергії, а завершивши довгий — усі.

Захисне поле. Коли ви або інша видима вам істота в межах 30 футів зазнаєте шкоди, ви можете застосувати реагування й витратити одну кістку псіонічної енергії. Киньте її та зменште отриману шкоду на результат + ваш модифікатор інтелекту (щонайменше на 1), створивши миттєвий щит телекінетичної сили.

Псіонічний удар. Ви можете сповнювати зброю псіонічною силою. Один раз за кожен свій хід, одразу після того, як ваша атака влучає в ціль у межах 30 футів і завдає їй шкоди зброєю, ви можете витратити одну кістку псіонічної енергії. Киньте її та завдайте цілі силової шкоди в кількості, що дорівнює результату + ваш модифікатор інтелекту.

Телекінетичне переміщення. Ви можете рухати предмети й істот силою думки. Магічною дією виберіть одну видиму ціль у межах 30 футів: не закріплений предмет Великого або меншого розміру чи одну згодну істоту, крім себе. Перемістіть ціль на відстань до 30 футів у видимий вільний простір. Якщо ціль — Крихітний предмет, натомість можете перемістити його до своєї руки або з неї.""",
    "When you or another creature you can see within 30 feet of you takes damage, you can take a Reaction to expend one Psionic Energy Die, roll the die, and reduce the damage taken by the number rolled plus your Intelligence modifier (minimum reduction of 1), as you create a momentary shield of telekinetic force.":
        "Коли ви або інша видима вам істота в межах 30 футів зазнаєте шкоди, ви можете застосувати реагування й витратити одну кістку псіонічної енергії. Киньте її та зменште отриману шкоду на результат + ваш модифікатор інтелекту (щонайменше на 1), створивши миттєвий щит телекінетичної сили.",
    "You can propel your weapons with psionic force. Once on each of your turns, immediately after you hit a target within 30 feet of yourself with an attack and deal damage to it with a weapon, you can expend one Psionic Energy Die, rolling it and dealing Force damage to the target equal to the number rolled plus your Intelligence modifier.":
        "Ви можете сповнювати зброю псіонічною силою. Один раз за кожен свій хід, одразу після того, як ваша атака влучає в ціль у межах 30 футів і завдає їй шкоди зброєю, ви можете витратити одну кістку псіонічної енергії. Киньте її та завдайте цілі силової шкоди в кількості, що дорівнює результату + ваш модифікатор інтелекту.",
    "If you fail an ability check using a skill or tool with which you have proficiency, you can roll one Psionic Energy Die and add the number rolled to the check, potentially turning failure into success. The die is expended only if the roll then succeeds.":
        "Проваливши перевірку характеристики з навичкою чи інструментом, якими володієте, ви можете кинути одну кістку псіонічної енергії та додати результат до перевірки, потенційно перетворивши невдачу на успіх. Кістка витрачається лише тоді, коли перевірка після цього стає успішною.",
    "If you make an attack roll with your Psychic Blade and miss the target, you can roll one Psionic Energy Die and add the number rolled to the attack roll.":
        "Якщо ваша атака Психічним клинком не влучає в ціль, ви можете кинути одну кістку псіонічної енергії та додати результат до кидка атаки.",
    "Gain <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on your <LSTag Tooltip=\"AttackRoll\">Attack Roll</LSTag>.":
        "Отримайте <LSTag Tooltip=\"Advantage\">перевагу</LSTag> на свій <LSTag Tooltip=\"AttackRoll\">кидок атаки</LSTag>.",
    "Gain <LSTag Tooltip=\"Advantage\">Advantage</LSTag> on your <LSTag Tooltip=\"SavingThrow\">Saving Throw</LSTag>.":
        "Отримайте <LSTag Tooltip=\"Advantage\">перевагу</LSTag> на свій <LSTag Tooltip=\"SavingThrow\">кидок протидії</LSTag>.",
    # Expanded mechanics QA: Gunslinger and short combat effects.
    "Gain 1d10 Temporary Hit Points.":
        "Отримайте 1d10 тимчасових очок здоров’я.",
    "Gain Temporary Hit Points equal to 1d4 plus spell caster's Charisma modifier.":
        "Отримайте тимчасові очки здоров’я в кількості 1d4 + модифікатор харизми заклинача.",
    "When you deal damage with a Ranged weapon that doesn’t add your ability modifier to the roll, you add your ability modifier nonetheless. If you already add your modifier to the damage roll, the target takes an extra 1d8 damage of the weapon’s type.":
        "Коли ви завдаєте шкоди далекобійною зброєю, яка не додає модифікатора характеристики до кидка шкоди, ви однаково додаєте цей модифікатор. Якщо він уже додається, ціль зазнає додаткової шкоди 1d8 того самого типу, що й шкода зброї.",
    "Gain Temporary Hit Points equal to the number rolled on the Risk die plus your Gunslinger level.":
        "Отримайте тимчасові очки здоров’я в кількості, що дорівнює результату кидка кістки ризику + ваш рівень стрільця.",
    "You can take a Bonus Action and expend one Risk Die to gain Blindsight with a range of 30 feet until the end of the current turn.":
        "Вторинною дією ви можете витратити одну кістку ризику й отримати сліпозір на 30 футів до кінця поточного ходу.",
    "When you miss with a ranged attack roll using a weapon, you can expend one Risk Die (no action required) to deal damage to that creature equal to a roll of the die plus your Dexterity modifier (minimum of 1). This damage is the same type dealt by the weapon, and the damage can be increased only by increasing the ability modifier. You can only use this maneuver once per turn.":
        "Коли ваша далекобійна атака зброєю не влучає в істоту, ви можете без витрати дії витратити одну кістку ризику й завдати цій істоті шкоди в кількості, що дорівнює результату кидка кістки + ваш модифікатор спритності (щонайменше 1). Тип шкоди збігається з типом шкоди зброї, а збільшити її можна лише збільшивши модифікатор характеристики. Цей маневр можна застосувати лише раз за хід.",
    "When you fail an Intelligence, Wisdom, or Charisma ability check or saving throw, you can expend one Risk Die to add it to the roll, potentially turning it into a success. You can only use this maneuver once per turn.":
        "Проваливши перевірку інтелекту, мудрості чи харизми або відповідний кидок протидії, ви можете витратити одну кістку ризику й додати її результат до кидка, потенційно перетворивши невдачу на успіх. Цей маневр можна застосувати лише раз за хід.",
    "When a creature you can see hits you with an attack roll, you can take a Reaction and expend one Risk Die to dodge out of harm’s way. Roll the die and add the number rolled to your AC against this attack, potentially causing it to miss. You can only use this maneuver once per turn.":
        "Коли видима вам істота влучає у вас атакою, ви можете застосувати реагування й витратити одну кістку ризику, щоб ухилитися від небезпеки. Киньте кістку й додайте результат до своєї РЗ проти цієї атаки, що може перетворити влучання на промах. Цей маневр можна застосувати лише раз за хід.",
    "If you lack the Firearm Expert property, you don’t add your ability modifier to this weapon’s damage rolls.":
        "Якщо ви не маєте властивості «Експерт з вогнепальної зброї», то не додаєте модифікатор характеристики до кидків шкоди цієї зброї.",
    "You are a firearm expert. You can add your ability modifier to the damage rolls of weapon attacks made with firearms.":
        "Ви — експерт з вогнепальної зброї. Ви можете додавати модифікатор характеристики до кидків шкоди атак вогнепальною зброєю.",
    "Gain a +2 bonus to all ability checks and saving throws that use Strength or Constitution.":
        "Отримайте бонус +2 до всіх перевірок характеристик і кидків протидії, що використовують силу або статуру.",
    "When you or another creature you can see within 60 feet of you makes an attack roll, a saving throw, or an ability check, you can use your reaction to cause the roll to have disadvantage.":
        "Коли ви або інша видима вам істота в межах 60 футів здійснює кидок атаки, кидок протидії чи перевірку характеристики, ви можете застосувати реагування й надати цьому кидку заваду.",
    "When you or another creature you can see within 60 feet of you makes an attack roll, a saving throw, or an ability check, you can use your reaction to cause the roll to have advantage.":
        "Коли ви або інша видима вам істота в межах 60 футів здійснює кидок атаки, кидок протидії чи перевірку характеристики, ви можете застосувати реагування й надати цьому кидку перевагу.",
    "Pact Weapon: Necrotic Damage": "Зброя договору: некротична шкода",
    "Pact Weapon: Psychic Damage": "Зброя договору: психічна шкода",
    "Pact Weapon: Radiant Damage": "Зброя договору: променева шкода",
    "Finger Guns": "Пальці-пістолети",
    "When you hit a target with a Finger Guns attack, you can expend one Risk Die and add it to the damage roll.":
        "Коли ви влучаєте в ціль атакою «Пальці-пістолети», можете витратити одну кістку ризику й додати її результат до кидка шкоди.",
    """You can use magic in place of guns.

Finger Guns. You learn the Finger Guns cantrip.

Arcane Shot. When you hit a target with a Finger Guns attack, you can expend one Risk Die and add it to the damage roll.""":
        """Ви можете замінити вогнепальну зброю магією.

Пальці-пістолети. Ви вивчаєте замовляння «Пальці-пістолети».

Містичний постріл. Коли ви влучаєте в ціль атакою «Пальці-пістолети», можете витратити одну кістку ризику й додати її результат до кидка шкоди.""",
    "You can take a Reaction when an ally you can see within 60 feet of you is hit by an attack. Expend one Risk Die to make a ranged weapon attack against the attacker. On use, the ally gains Temporary Hit Points equal to the number rolled on the Risk Die.":
        "Коли атака влучає у видимого вам союзника в межах 60 футів, ви можете застосувати реагування й витратити одну кістку ризику, щоб атакувати нападника далекобійною зброєю. Після цього союзник отримує тимчасові очки здоров’я в кількості, що дорівнює результату кидка кістки ризику.",
    "Gain Temporary Hit Points equal to the number rolled on the Risk die.":
        "Отримайте тимчасові очки здоров’я в кількості, що дорівнює результату кидка кістки ризику.",
    "Gain temporary hit points equal to your illrigger level.":
        "Отримайте тимчасові очки здоров’я в кількості, що дорівнює вашому рівню ілріґера.",
    # Expanded mechanics QA: shadow, curse, and spell-adjacent statuses.
    """Shadows are your companion, aiding you in your exploits. You gain the following benefits:

You gain darkvision out to 60 feet. If you already have darkvision, its range increases by 60 feet.
Your movement speed increases by 10 feet.
You have advantage on Dexterity (<LSTag Type="Skills" Tooltip="Stealth">Stealth</LSTag>) checks made to hide. Whenever you make a Dexterity saving throw to take only half damage from an effect, you instead take no damage if you succeed on the saving throw, and half damage if you fail.""":
        """Тіні — ваші супутники й помічники у звершеннях. Ви отримуєте такі переваги:

Ви отримуєте темнозір на 60 футів. Якщо ви вже маєте темнозір, його дальність збільшується на 60 футів.
Ваша швидкість переміщення збільшується на 10 футів.
Ви маєте перевагу на перевірки спритності (<LSTag Type="Skills" Tooltip="Stealth">Непомітність</LSTag>) для переховування. Коли ефект дає змогу виконати кидок протидії спритністю, щоб зазнати лише половини шкоди, у разі успіху ви натомість не зазнаєте шкоди, а в разі невдачі зазнаєте половини.""",
    """Shadows are your companion, aiding you in your exploits. You gain the following benefits:

You gain darkvision out to 60 feet. If you already have darkvision, its range increases by 60 feet.
You can see normally in darkness, both magical and non-magical.
Your movement speed increases by 10 feet.
You have advantage on Dexterity (<LSTag Type="Skills" Tooltip="Stealth">Stealth</LSTag>) checks made to hide. Whenever you make a Dexterity saving throw to take only half damage from an effect, you instead take no damage if you succeed on the saving throw, and half damage if you fail.""":
        """Тіні — ваші супутники й помічники у звершеннях. Ви отримуєте такі переваги:

Ви отримуєте темнозір на 60 футів. Якщо ви вже маєте темнозір, його дальність збільшується на 60 футів.
Ви нормально бачите як у магічній, так і у звичайній темряві.
Ваша швидкість переміщення збільшується на 10 футів.
Ви маєте перевагу на перевірки спритності (<LSTag Type="Skills" Tooltip="Stealth">Непомітність</LSTag>) для переховування. Коли ефект дає змогу виконати кидок протидії спритністю, щоб зазнати лише половини шкоди, у разі успіху ви натомість не зазнаєте шкоди, а в разі невдачі зазнаєте половини.""",
    "Affected entity is being strangled by a garrotte. It is <LSTag Type=\"Status\" Tooltip=\"SILENCED\">Silenced</LSTag> and takes [1] per turn.":
        "Уражену істоту душить гарота. Вона перебуває в стані <LSTag Type=\"Status\" Tooltip=\"SILENCED\">Стишення</LSTag> і зазнає [1] за хід.",
    "Affected entity will take [1] when it makes an attack or casts a spell.":
        "Уражена істота зазнає [1], коли атакує або проказує закляття.",
    "You gain a bonus to <LSTag Tooltip=\"SpellDifficultyClass\">Spell Save DC</LSTag> and spell <LSTag Tooltip=\"AttackRoll\">attack rolls</LSTag>.":
        "Ви отримуєте бонус до <LSTag Tooltip=\"SpellDifficultyClass\">МС протидії закляттям</LSTag> і до <LSTag Tooltip=\"AttackRoll\">кидків атаки</LSTag> закляттями.",
    "You can take a Bonus Action to magically create icy terrain on up to five spaces. The ice-covered spaces become Difficult Terrain and remain until the end of your next turn. When you take this Bonus Action, you may spend one or more Sorcery Points to freeze an additional five spaces for each Sorcery Point spent.":
        "Вторинною дією ви можете магічно вкрити льодом до п’яти ділянок. Вони стають складним рельєфом до кінця вашого наступного ходу. Виконуючи цю вторинну дію, ви можете витратити одне або більше очок чародійства, щоб за кожне очко заморозити ще п’ять ділянок.",
    "Gain a +2 bonus to Intelligence, Wisdom, and Charisma saving throws.":
        "Отримайте бонус +2 до кидків протидії інтелектом, мудрістю та харизмою.",
    "You gain proficiency in the <LSTag Type=\"Skills\" Tooltip=\"Stealth\">Stealth</LSTag> skill and darkvision. In addition, you can use a bonus action to <LSTag Type=\"Spell\" Tooltip=\"Shout_Hide\">Hide</LSTag>.":
        "Ви отримуєте володіння навичкою <LSTag Type=\"Skills\" Tooltip=\"Stealth\">Непомітність</LSTag> і темнозір. Крім того, ви можете вторинною дією <LSTag Type=\"Spell\" Tooltip=\"Shout_Hide\">сховатися</LSTag>.",
    "Gain Temporary Hit Points equal to 2d6 + the Cleric's Wisdom modifier.":
        "Отримайте тимчасові очки здоров’я в кількості 2d6 + модифікатор мудрості клірика.",
    "Conjure Woodland Beings": "Прикликання лісових істот",
    "Conjure Woodland Beings Aura": "Аура Прикликання лісових істот",
    "You can call on your fiendish patron to alter fate in your favor. When you make an ability check or a saving throw, you can use this feature to add 1d10 to your roll. You can do so after seeing the roll but before any of the roll’s effects occur.":
        "Ви можете закликати свого нечистого покровителя змінити долю на вашу користь. Коли ви виконуєте перевірку характеристики або кидок протидії, можете застосувати цю особливість і додати 1d10 до кидка. Це можна зробити після того, як ви побачили результат, але до застосування його наслідків.",
    "Gain Temporary Hit Points equal to 1d6 plus your Sorcerer level.":
        "Отримайте тимчасові очки здоров’я в кількості 1d6 + ваш рівень чародія.",
    "Gain 1d10 temporary hit points.":
        "Отримайте 1d10 тимчасових очок здоров’я.",
    "Gain temporary hit points equal to 1d6 plus cleric level.":
        "Отримайте тимчасові очки здоров’я в кількості 1d6 + рівень клірика.",
    "Gain a number of Temporary Hit Points equal to your Proficiency Bonus.":
        "Отримайте тимчасові очки здоров’я в кількості, що дорівнює вашому бонусу спеціалізації.",
    """You conjure spirits from the Elemental Planes that flit around you in a 15-foot Emanation for the duration. Until the spell ends, any attack you make deals an extra [1] damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack).

In addition, the ground in the Emanation is Difficult Terrain for your enemies.""":
        """На час дії ви прикликаєте духів зі Стихійних планів, які пурхають навколо вас у 15-футовій еманації. До завершення закляття кожна ваша атака, що влучає в істоту в еманації, завдає додатково [1] кислотної, холодової, вогняної або блискавкової шкоди — тип ви вибираєте під час атаки.

Крім того, поверхня в еманації є складним рельєфом для ваших ворогів.""",
    "Conjure Minor Elementals: Acid": "Прикликання малих стихійників: кислота",
    "Conjure Minor Elementals: Cold": "Прикликання малих стихійників: холод",
    "Conjure Minor Elementals: Fire": "Прикликання малих стихійників: вогонь",
    "Conjure Minor Elementals: Lightning": "Прикликання малих стихійників: блискавка",
    "Until the spell ends, any attack you make deals an extra acid damage when you hit a creature in the Emanation.":
        "До завершення закляття кожна ваша атака, що влучає в істоту в еманації, завдає додаткової кислотної шкоди.",
    "Until the spell ends, any attack you make deals an extra cold damage when you hit a creature in the Emanation.":
        "До завершення закляття кожна ваша атака, що влучає в істоту в еманації, завдає додаткової холодової шкоди.",
    "Until the spell ends, any attack you make deals an extra fire damage when you hit a creature in the Emanation.":
        "До завершення закляття кожна ваша атака, що влучає в істоту в еманації, завдає додаткової вогняної шкоди.",
    "Until the spell ends, any attack you make deals an extra lightning damage when you hit a creature in the Emanation.":
        "До завершення закляття кожна ваша атака, що влучає в істоту в еманації, завдає додаткової блискавкової шкоди.",
    "Conjure Minor Elementals Target": "Ціль Прикликання малих стихійників",
    "Affected entity is haunted by its worst nightmares.<br><br>It takes [1] per turn, has <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on <LSTag Tooltip=\"AbilityCheck\">Ability Checks</LSTag> and <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag>.":
        "Уражену істоту переслідують її найгірші кошмари.<br><br>Вона зазнає [1] за хід і має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки характеристик</LSTag> та <LSTag Tooltip=\"AttackRoll\">кидки атаки</LSTag>.",
    """You can hurl searing bolts of magical radiance.

You gain a new attack option that you can use with the Attack action. This special attack is a ranged spell attack with a range of 30 feet. You are proficient with it, and you add your Dexterity modifier to its attack and damage rolls. Its damage is radiant, and its damage die is a d6. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.

When you take the Attack action on your turn and use this special attack as part of it, you can spend 1 ki point to make the special attack twice as a bonus action.

When you gain the Extra Attack feature, this special attack can be used for any of the attacks you make as part of the Attack action.""":
        """Ви можете метати пекучі заряди магічного сяйва.

Ви отримуєте новий варіант атаки, доступний під час дії «Атака». Це особлива далекобійна атака закляттям із дальністю 30 футів. Ви володієте нею й додаєте свій модифікатор спритності до її кидків атаки та шкоди. Вона завдає променевої шкоди, а її кістка шкоди — d6. Ця кістка змінюється зі здобуттям рівнів монаха, як указано у стовпці «Бойові мистецтва» таблиці монаха.

Коли у свій хід ви виконуєте дію «Атака» й застосовуєте в її межах цю особливу атаку, можете витратити 1 очко кі, щоб двічі здійснити цю атаку вторинною дією.

Отримавши особливість «Додаткова атака», ви можете використати цю особливу атаку для будь-якої атаки в межах дії «Атака».""",
    # Expanded mechanics QA: terminology and malformed machine prose.
    "The creature subtracts 1d6 from all its attack rolls and ability checks, as well as from any Constitution saving throws it makes to maintain Concentration. At the end of each of its turns, the target makes an Intelligence saving throw, ending the effect on a success.":
        "Істота віднімає 1d6 від усіх своїх кидків атаки та перевірок характеристик, а також від кидків протидії статурою для збереження зосередження. Наприкінці кожного свого ходу ціль виконує кидок протидії інтелектом і в разі успіху завершує цей ефект.",
    "The creature subtracts 1d6 from its attack rolls and ability checks, as well as from any Constitution saving throws it makes to maintain Concentration. At the end of each of its turns, it makes an Intelligence saving throw, ending the effect on a success.":
        "Істота віднімає 1d6 від своїх кидків атаки та перевірок характеристик, а також від кидків протидії статурою для збереження зосередження. Наприкінці кожного свого ходу вона виконує кидок протидії інтелектом і в разі успіху завершує цей ефект.",
    """You have learned to draw on the power of the Shadowfell, gaining the following benefits.

Darkness. You can expend 1 Focus Point to cast the Darkness spell without spell components. You can see within the spell’s area when you cast it with this feature. While the spell persists, you can move its area of Darkness to a space within [1] of yourself at the start of each of your turns.
Darkvision. You gain Darkvision with a range of [1]. If you already have Darkvision, its range increases by 60 feet.

Shadowy Figments. You know the <LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Minor Illusion</LSTag> spell. Wisdom is your spellcasting ability for it.""":
        """Ви навчилися черпати силу з Тінепаду й отримуєте такі переваги.

Пітьма. Ви можете витратити 1 очко зосередження, щоб проказати «Пітьму» без складників. Проказавши закляття за допомогою цієї особливості, ви можете бачити в зоні його дії. Поки закляття триває, на початку кожного свого ходу ви можете перемістити зону Пітьми в простір у межах [1] від себе.
Темнозір. Ви отримуєте темнозір із дальністю [1]. Якщо ви вже маєте темнозір, його дальність збільшується на 60 футів.

Тіньові образи. Ви знаєте закляття <LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Мала ілюзія</LSTag>. Його базова характеристика проказування для вас — мудрість.""",
    """You gain Expertise in two of your skill proficiencies of your choice. <LSTag Type="Skills" Tooltip="SleightOfHand">Sleight of Hand</LSTag> and <LSTag Type="Skills" Tooltip="Stealth">Stealth</LSTag> are recommended if you have proficiency in them.

At Rogue level 6, you gain Expertise in two more of your skill proficiencies of your choice.""":
        """Виберіть дві навички, якими володієте. Ви отримуєте Вправність у цих навичках. Якщо ви ними володієте, радимо вибрати <LSTag Type="Skills" Tooltip="SleightOfHand">Спритність рук</LSTag> і <LSTag Type="Skills" Tooltip="Stealth">Непомітність</LSTag>.

На 6-му рівні пройдисвіта виберіть іще дві навички, якими володієте. Ви отримуєте Вправність у цих навичках.""",
    """You have <LSTag Tooltip="Advantage">Advantage</LSTag> on <LSTag Type="Skills" Tooltip="Perception">Perception</LSTag> <LSTag Tooltip="AbilityCheck">Checks</LSTag> made to detect hidden objects.

You have <LSTag Tooltip="Advantage">Advantage</LSTag> on <LSTag Tooltip="SavingThrow">Saving Throws</LSTag> made to avoid traps and <LSTag Tooltip="Resistant">Resistance</LSTag> to trap damage.

You can see in the dark up to [1].""":
        """Ви маєте <LSTag Tooltip="Advantage">перевагу</LSTag> на <LSTag Tooltip="AbilityCheck">перевірки</LSTag> <LSTag Type="Skills" Tooltip="Perception">Відчуття</LSTag> для виявлення прихованих предметів.

Ви маєте <LSTag Tooltip="Advantage">перевагу</LSTag> на <LSTag Tooltip="SavingThrow">кидки протидії</LSTag> пасткам і <LSTag Tooltip="Resistant">стійкість</LSTag> до шкоди від пасток.

Ви бачите в темряві на відстані до [1].""",
    "You can augment your weapon strikes with mind-scarring magic drawn from the murky hollows of the Feywild. When you hit a creature with a weapon, you can deal an extra 1d4 Psychic damage to the target, which can take this extra damage only once per turn. The extra damage increases to 1d6 when you reach Ranger level 11.":
        "Ви можете посилювати удари зброєю магією з похмурих глибин Феєлону, що лишає шрами на розумі. Коли ви влучаєте в істоту зброєю, можете завдати цілі додаткової психічної шкоди 1d4. Одна ціль може зазнати цієї додаткової шкоди лише раз за хід. На 11-му рівні слідопита додаткова шкода збільшується до 1d6.",
    "When you score a Critical Hit against a creature, you can call for the target to surrender. The target must succeed on a Wisdom saving throw against your Maneuver save DC or gain the Frightened conditions for 1 minute. The creature can repeat the Wisdom saving throw at the end of each of its turns, ending the conditions on a success.":
        "Коли ви завдаєте істоті критичного влучання, то можете закликати ціль здатися. Вона повинна успішно виконати кидок протидії мудрістю проти вашої МС протидії маневру, інакше набуде стану переляку на 1 хвилину. Наприкінці кожного свого ходу істота може повторити кидок і в разі успіху завершити цей стан.",
    """Dark energy infuses the Shadow Realm, corrupting and corroding everything it touches. Some barbarians intentionally consume this raw shadow, infusing their bodies with shadow energy to manifest potent magical abilities.

Many of the barbarians who walk this path do so to absorb harmful shadow magic into themselves in order to protect others from its influence. A smaller group consumes shadow simply because they cannot resist its ever-present temptation.""":
        """Темна енергія пронизує Тіньове царство, спотворюючи й роз’їдаючи все, чого торкається. Деякі варвари свідомо поглинають чисту тінь і насичують тіло її енергією, щоб пробудити могутні магічні здібності.

Чимало послідовників цього шляху приймають у себе згубну тіньову магію, аби захистити інших від її впливу. Інші ж поглинають тінь лише тому, що не здатні опиратися її невпинній спокусі.""",
    "Until you complete your next short or long rest, you and your allies gain a +5 bonus to Dexterity (<LSTag Type=\"Skills\" Tooltip=\"Stealth\">Stealth</LSTag>) and Wisdom (<LSTag Type=\"Skills\" Tooltip=\"Perception\">Perception</LSTag>) checks.":
        "До завершення вашого наступного короткого або довгого відпочинку ви та ваші союзники отримуєте бонус +5 до перевірок спритності (<LSTag Type=\"Skills\" Tooltip=\"Stealth\">Непомітність</LSTag>) і мудрості (<LSTag Type=\"Skills\" Tooltip=\"Perception\">Відчуття</LSTag>).",
    "You have Advantage on any ability check you make to end the restrained condition. Your carrying capacity is increased by a quarter.":
        "Ви маєте перевагу на всі перевірки характеристик для завершення стану знерухомлення. Ваша вантажопідйомність збільшується на 25 відсотків.",
    """When you activate your <LSTag Type="Status" Tooltip="RAGE">Rage</LSTag>, your countenance distorts and your body swells. Creatures that haven’t witnessed your transformation, now or previously, don’t recognize you. In addition, while your Rage is active, you gain the following benefits:

You can roll 1d8 in place of the normal damage of your Unarmed Strike.

When you hit a creature with an Unarmed Strike, you can push it 10 feet or force the creature to make a Constitution saving throw (DC 8 plus your Strength modifier and your Proficiency Bonus). On a failed save, the creature has the Prone condition.

When you make an Unarmed Strike, your reach is 5 feet greater than normal.""":
        """Коли ви входите в <LSTag Type="Status" Tooltip="RAGE">Лють</LSTag>, ваше обличчя спотворюється, а тіло набрякає. Істоти, які не бачили вашого перетворення раніше чи зараз, не впізнають вас. Крім того, поки діє Лють, ви отримуєте такі переваги:

Ви можете кинути 1d8 замість звичайної кістки шкоди свого Удару голіруч.

Коли ви влучаєте в істоту Ударом голіруч, можете відштовхнути її на 10 футів або змусити виконати кидок протидії статурою (МС 8 + ваш модифікатор сили + бонус спеціалізації). У разі невдачі істота набуває стану повалення.

Коли ви здійснюєте Удар голіруч, ваша досяжність на 5 футів більша за звичайну.""",
    "When you activate your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag>, when you hit a creature with an Unarmed Strike, you can force the creature to make a Constitution saving throw (DC 8 plus your Strength modifier and your Proficiency Bonus). On a failed save, the creature has the Prone condition.":
        "Поки діє ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, коли ви влучаєте в істоту Ударом голіруч, можете змусити її виконати кидок протидії статурою (МС 8 + ваш модифікатор сили + бонус спеціалізації). У разі невдачі істота набуває стану повалення.",
    "A life-changing event, such as being cursed by a drider or being bitten by a dangerously transmuted arachnid, has imbued you with the abilities of a spider. This transformation might have left you physically unchanged, or you may have developed a half-dozen eyes, lanky and hairy limbs, or a set of inhuman mandibles. Whatever the side effects, you can now produce deadly poison and ropes of silken web from your palms, and even scale walls with your fingertips.":
        "Подія, що змінила ваше життя, — наприклад, прокляття драйдера чи укус небезпечно перетвореного павукоподібного — наділила вас павучими здібностями. Зовні ви могли не змінитися, а могли й отримати пів дюжини очей, довгі волохаті кінцівки чи нелюдські мандибули. Хай якими були побічні наслідки, тепер ви здатні виробляти смертельну отруту, випускати з долонь мотузки шовкової павутини й навіть дертися стінами за допомогою кінчиків пальців.",
    "Eladrin are elves of the Feywild, a realm of perilous beauty and boundless magic. Using that magic, eladrin can step from one place to another in the blink of an eye, and each eladrin resonates with emotions captured in the Feywild in the form of seasons—affinities that affect the eladrin’s mood and appearance. An eladrin’s season can change, though some remain in one season forever. Choose your season or roll on the Eladrin Seasons table. Your Trance trait lets you change your season.":
        "Еладріни — ельфи Феєлону, царини небезпечної краси й безмежної магії. Завдяки цій магії вони здатні вмить переходити з місця на місце. Кожен еладрін співзвучний з емоціями, утіленими у Феєлоні як пори року, і ця спорідненість впливає на його настрій та зовнішність. Пора року еладріна може змінюватися, хоча дехто назавжди зберігає одну. Виберіть свою пору року або киньте кістку за таблицею «Пори року еладрінів». Ваша риса «Транс» дає змогу змінювати пору року.",
    # Full prose QA: class features, feats, conditions, and spell-adjacent statuses.
    "Until the start of your next turn, any attack roll made against you has Disadvantage, and you make Dexterity saving throws with Advantage.":
        "До початку вашого наступного ходу всі кидки атаки проти вас мають заваду, а ви маєте перевагу на кидки протидії спритністю.",
    """When a creature that you can see within [1] of yourself makes an attack roll, you can take a Reaction to impose Disadvantage on the attack roll, causing light to flare before it hits or misses.

You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a Long Rest.""":
        """Коли видима вам істота в межах [1] виконує кидок атаки, ви можете застосувати реагування й накласти на цей кидок заваду: перед ціллю атаки спалахує світло, перш ніж атака влучить чи схибить.

Ви можете застосувати цю особливість стільки разів, скільки становить ваш модифікатор мудрості (щонайменше один раз). Усі витрачені застосування відновлюються після довгого відпочинку.""",
    """You regain all expended uses of your Warding Flare when you finish a Short or Long Rest.

In addition, whenever you use Warding Flare, you can give the target of the triggering attack a number of Temporary Hit Points equal to 2d6 plus your Wisdom modifier.""":
        """Ви відновлюєте всі витрачені застосування «Охоронного спалаху» після короткого або довгого відпочинку.

Крім того, щоразу, коли ви застосовуєте «Охоронний спалах», ціль атаки, що спричинила це реагування, може отримати тимчасові очки здоров’я в кількості 2d6 + ваш модифікатор мудрості.""",
    """You can supernaturally inspire others through words, music, or dance. This inspiration is represented by your Bardic Inspiration die, which is a d6.

Using Bardic Inspiration. As a Bonus Action, you can inspire another creature within 60 feet of yourself who can see or hear you. That creature gains one of your Bardic Inspiration dice. A creature can have only one Bardic Inspiration die at a time.

Once within the next hour when the creature fails a D20 Test, the creature can roll the Bardic Inspiration die and add the number rolled to the d20, potentially turning the failure into a success. A Bardic Inspiration die is expended when it’s rolled.

Number of Uses. You can confer a Bardic Inspiration die a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.

At Higher Levels. Your Bardic Inspiration die changes when you reach certain Bard levels, as shown in the Bardic Die column of the Bard Features table. The die becomes a d8 at level 5, a d10 at level 10, and a d12 at level 15.""":
        """Ви можете надприродно надихати інших словами, музикою чи танцем. Це натхнення уособлює кістка Бардівського натхнення — спочатку d6.

Застосування Бардівського натхнення. Вторинною дією ви можете надихнути іншу істоту в межах 60 футів, яка вас бачить або чує. Ця істота отримує одну вашу кістку Бардівського натхнення. Істота може мати лише одну таку кістку за раз.

Один раз протягом наступної години, коли істота провалить перевірку D20, вона може кинути кістку Бардівського натхнення й додати результат до d20, що може перетворити невдачу на успіх. Після кидка кістка витрачається.

Кількість застосувань. Ви можете дати кістку Бардівського натхнення стільки разів, скільки становить ваш модифікатор харизми (щонайменше один раз). Усі витрачені застосування відновлюються після довгого відпочинку.

На вищих рівнях. Ваша кістка Бардівського натхнення змінюється зі зростанням рівня барда, як указано у стовпці «Бардівська кістка» таблиці особливостей барда. На 5-му рівні вона стає d8, на 10-му — d10, а на 15-му — d12.""",
    """You can regain all expended Focus Points. When you do so, roll your Martial Arts die, and regain a number of Hit Points equal to your Monk level plus the number rolled.

Once you use this feature, you can’t use it again until you finish a Long Rest.""":
        """Ви можете відновити всі витрачені очки зосередження. Зробивши це, киньте свою кістку Бойових мистецтв і відновіть очки здоров’я в кількості, що дорівнює вашому рівню монаха + результат кидка.

Застосувавши цю особливість, ви не зможете зробити це знову до завершення довгого відпочинку.""",
    "If a creature wielding this Heavy weapon has a Strength score lower than [1], it has Disadvantage on attack rolls made with this weapon.":
        "Якщо показник сили істоти, що тримає цю важку зброю, менший за [1], її кидки атаки цією зброєю мають заваду.",
    "If a creature wielding this Heavy weapon has a Dexterity score lower than [1], it has Disadvantage on attack rolls made with this weapon.":
        "Якщо показник спритності істоти, що тримає цю важку зброю, менший за [1], її кидки атаки цією зброєю мають заваду.",
    """You have <LSTag Tooltip="Advantage">Advantage</LSTag> on <LSTag Tooltip="SavingThrow">Saving Throws</LSTag> to maintain <LSTag Tooltip="Concentration">Concentration</LSTag> on a spell.

You can use a <LSTag Type="ActionResource" Tooltip="ReactionActionPoint">reaction</LSTag> to cast <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Shocking Grasp</LSTag> at a target moving out of melee range.""":
        """Ви маєте <LSTag Tooltip="Advantage">перевагу</LSTag> на <LSTag Tooltip="SavingThrow">кидки протидії</LSTag> для збереження <LSTag Tooltip="Concentration">зосередження</LSTag> на заклятті.

Ви можете застосувати <LSTag Type="ActionResource" Tooltip="ReactionActionPoint">реагування</LSTag>, щоб проказати <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">«Шоковий хват»</LSTag> на ціль, що виходить з вашої зони досяжності.""",
    "Has Disadvantage on Strength-based D20 Tests for the duration. During that time, it also subtracts 1d8 from all its damage rolls. The target repeats the save at the end of each of its turns, ending the spell on a success.":
        "На час дії має заваду на перевірки D20, засновані на силі, і віднімає 1d8 від усіх своїх кидків шкоди. Наприкінці кожного свого ходу ціль повторює кидок протидії й у разі успіху завершує дію закляття.",
    """Push. When you hit a creature with an attack that deals Bludgeoning damage, you can move it 5 feet to an unoccupied space if the target is no more than one size larger than you.

Enhanced Critical. When you score a Critical Hit that deals Bludgeoning damage to a creature, attack rolls against that creature have Advantage until the start of your next turn.""":
        """Поштовх. Коли ви влучаєте в істоту атакою, що завдає дробильної шкоди, ви можете перемістити її на 5 футів у вільний простір, якщо ціль не більш ніж на одну категорію розміру більша за вас.

Посилене критичне влучання. Коли ви завдаєте істоті критичного влучання з дробильною шкодою, кидки атаки проти неї мають перевагу до початку вашого наступного ходу.""",
    """Puncture. When you hit a creature with an attack that deals Piercing damage, you can reroll one of the attack’s damage dice, and you must use the new roll.

Enhanced Critical. When you score a Critical Hit that deals Piercing damage to a creature, you can roll one additional damage die when determining the extra Piercing damage the target takes.""":
        """Прокол. Коли ви влучаєте в істоту атакою, що завдає колотої шкоди, ви можете перекинути одну з кісток шкоди цієї атаки й мусите використати новий результат.

Посилене критичне влучання. Коли ви завдаєте істоті критичного влучання з колотою шкодою, ви можете кинути додаткову кістку шкоди, визначаючи додаткову колоту шкоду цілі.""",
    """Hamstring. When you hit a creature with an attack that deals Slashing damage, you can reduce the Speed of that creature by 10 feet until the start of your next turn.

Enhanced Critical. When you score a Critical Hit that deals Slashing damage to a creature, it has Disadvantage on attack rolls until the start of your next turn.""":
        """Підсічення. Коли ви влучаєте в істоту атакою, що завдає рубаної шкоди, ви можете зменшити швидкість цієї істоти на 10 футів до початку вашого наступного ходу.

Посилене критичне влучання. Коли ви завдаєте істоті критичного влучання з рубаною шкодою, вона має заваду на кидки атаки до початку вашого наступного ходу.""",
    "The magic of the Feywild guards your mind. You are immune to the Charmed and Frightened conditions.":
        "Магія Феєлону оберігає ваш розум. Ви маєте імунітет до станів причарування та переляку.",
    "You have Advantage on saving throws you make to avoid or end the Charmed condition.":
        "Ви маєте перевагу на кидки протидії, щоб уникнути або завершити стан причарування.",
    "You gain expertise in all of the following skills: <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Intimidation</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>, and <LSTag Type=\"Skills\" Tooltip=\"Performance\">Performance</LSTag>.":
        "Ви отримуєте Вправність у таких навичках: <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Залякування</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag> і <LSTag Type=\"Skills\" Tooltip=\"Performance\">Виступ</LSTag>.",
    """Your experience surviving harrowing environments allows you to bolster your allies in addition to yourself. As a Magic action, choose a number of creatures you can see equal to your Wisdom modifier (minimum of one). Each chosen creature regains Hit Points equal to 1d10 plus your Ranger level and has Advantage on saving throws to avoid or end the Frightened condition for 1 hour.

Once you use this feature, you can’t use it again until you finish a Long Rest.""":
        """Ваш досвід виживання в жахливих умовах дає змогу підтримати не лише себе, а й союзників. Магічною дією виберіть видимих вам істот у кількості, що дорівнює вашому модифікатору мудрості (щонайменше одну). Кожна вибрана істота відновлює очки здоров’я в кількості 1d10 + ваш рівень слідопита і на 1 годину отримує перевагу на кидки протидії, щоб уникнути або завершити стан переляку.

Застосувавши цю особливість, ви не зможете зробити це знову до завершення довгого відпочинку.""",
    "Have Advantage on saving throws to avoid or end the Frightened condition":
        "Перевага на кидки протидії, щоб уникнути або завершити стан переляку",
    """Immediately after you cast Smite Spell, you can expend one use of your Channel Oath and invoke one of the following effects.

Dao’s Crush. Earth rises up around the target. The target has the Restrained condition.

Djinni’s Escape. You teleport to an unoccupied space you can see within 30 feet of yourself and take on a semi-incorporeal form, which lasts until the end of your next turn. While in this form, you have Resistance to Bludgeoning, Piercing, and Slashing damage, and you have Immunity to the Prone, and Restrained conditions.

Efreeti’s Fury. The target takes an extra 2d4 Fire damage, and flames leap from the target to all enemies you can see within 30 feet of yourself. Each of those creatures also takes 2d4 Fire damage.

Marid’s Surge. The target and each creature of your choice in a 10-foot Emanation originating from you make a Strength saving throw against your spell save DC. On a failed save, a creature is pushed 15 feet straight away from you and has the Prone condition.""":
        """Одразу після того, як ви проказуєте закляття Кари, ви можете витратити одне застосування Обітного наснаження й викликати один із таких ефектів.

Тиск дао. Земля здіймається навколо цілі. Ціль набуває стану знерухомлення.

Втеча джина. Ви телепортуєтеся у видимий вам вільний простір у межах 30 футів і набуваєте напівбезтілесної форми до кінця вашого наступного ходу. У цій формі ви маєте стійкість до дробильної, колотої та рубаної шкоди, а також імунітет до станів повалення та знерухомлення.

Лють іфрита. Ціль зазнає додаткової вогняної шкоди 2d4, а полум’я перескакує від неї до всіх видимих вам ворогів у межах 30 футів. Кожен із них також зазнає 2d4 вогняної шкоди.

Натиск марида. Ціль і кожна вибрана вами істота у 10-футовій еманації від вас виконує кидок протидії силою проти вашої МС протидії закляттям. У разі невдачі істоту відштовхує на 15 футів прямо від вас, і вона набуває стану повалення.""",
    "When you reach certain Paladin levels, the magic of the genie ensures you always have specific spells prepared. At 3rd level, you always have Chromatic Orb and Thunderous Smite prepared. At 5th level, you additionally have Mirror Image and Phantasmal Force prepared. At 9th level, you additionally have Fly and Gaseous Form prepared.":
        "На певних рівнях паладина магія джина завжди тримає для вас підготовленими певні закляття. На 3-му рівні ви завжди маєте підготовлені «Хроматичну кулю» та «Громову кару». На 5-му рівні до них додаються «Віддзеркалення» і «Примарна сила», а на 9-му — «Політ» і «Газоподібність».",
    """You form a Dread Allegiance by choosing one of the Dead Three: Bane, Bhaal, or Myrkul. Your choice grants you Resistance to a specific damage type and the ability to cast an associated cantrip, using Intelligence as your spellcasting ability.

If you choose Bane, you gain Resistance to Psychic damage and can cast <LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">Minor Illusion</LSTag>.

If you choose Bhaal, you gain Resistance to Poison damage and can cast <LSTag Type="Spell" Tooltip="Shout_BladeWard">Blade Ward</LSTag>.

If you choose Myrkul, you gain Resistance to Necrotic damage and can cast Chill Touch.

You can change your chosen deity whenever you finish a Long Rest.""":
        """Ви укладаєте Моторошну вірність, обираючи одного з Мертвої Трійці: Бейна, Баала або Меркула. Ваш вибір дає стійкість до певного типу шкоди і змогу проказувати відповідне замовляння, базовою характеристикою проказування якого є інтелект.

Обравши Бейна, ви отримуєте стійкість до психічної шкоди й можете проказувати <LSTag Type="Spell" Tooltip="Target_ImprovedMinorIllusion">«Малу ілюзію»</LSTag>.

Обравши Баала, ви отримуєте стійкість до отруйної шкоди й можете проказувати <LSTag Type="Spell" Tooltip="Shout_BladeWard">«Оберіг від зброї»</LSTag>.

Обравши Меркула, ви отримуєте стійкість до некротичної шкоди й можете проказувати «Крижаний дотик».

Ви можете змінити обране божество після кожного довгого відпочинку.""",
    """Your ability to channel spirits improves. You gain the following benefits.

Power from Beyond. Once per turn, when you cast a Bard spell with a spell slot that deals damage or restores Hit Points, roll 1d6. Add the number rolled to one of the spell's damage rolls or to the total Hit Points it restores.

Spiritual Manifestation. You always have the Spirit Guardians spell prepared. In addition, you gain one 3rd-level spell slot that can be used only to cast Spirit Guardians. You regain this spell slot when you finish a Long Rest.""":
        """Ваша здатність проводити духів удосконалюється. Ви отримуєте такі переваги.

Сила з-поза меж. Один раз за хід, коли ви проказуєте закляття барда за допомогою чарунки й це закляття завдає шкоди або відновлює очки здоров’я, киньте 1d6. Додайте результат до одного з кидків шкоди закляття або до загальної кількості відновлених ним очок здоров’я.

Духовний прояв. Ви завжди маєте підготовленою «Духовну сторожу». Крім того, ви отримуєте одну чарунку 3-го рівня, яку можна використати лише для проказування «Духовної сторожі». Ця чарунка відновлюється після довгого відпочинку.""",
    "Whenever you score a Critical Hit against a Large or smaller creature with a ranged attack using a weapon, the projectile lodges itself in the target. For 3 turns, its Speed is halved and it has Disadvantage on attack rolls.":
        "Щоразу, коли ви завдаєте критичного влучання істоті великого або меншого розміру далекобійною атакою зброєю, снаряд застрягає в цілі. На 3 ходи її швидкість зменшується вдвічі, а кидки атаки мають заваду.",
    "Its Speed is halved and it has Disadvantage on attack rolls.":
        "Її швидкість зменшена вдвічі, а кидки атаки мають заваду.",
    "You gain proficiency with all Gaming Sets and in one of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"Deception\">Deception</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Perception\">Perception</LSTag>.":
        "Ви отримуєте володіння всіма ігровими наборами та однією з таких навичок на ваш вибір: <LSTag Type=\"Skills\" Tooltip=\"Deception\">Обман</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Perception\">Відчуття</LSTag>.",
    "You gain expertise in <LSTag Type=\"Skills\" Tooltip=\"History\">History</LSTag> checks.":
        "Ви отримуєте Вправність у перевірках <LSTag Type=\"Skills\" Tooltip=\"History\">Історії</LSTag>.",
    "You learn to fend off strikes directed at you, your mount, or other creatures nearby. If you or a creature you can see within 5 feet of you is hit by an attack, you can use your reaction to roll 1d8 if you’re wielding a melee weapon or a shield. Add the number rolled to the target’s AC against that attack, potentially causing it to miss.":
        "Ви вчитеся відбивати удари, спрямовані на вас, вашого скакуна чи інших істот поблизу. Коли атака влучає у вас або у видиму вам істоту в межах 5 футів, ви можете застосувати реагування й кинути 1d8, якщо тримаєте зброю ближнього бою або щит. Додайте результат до РЗ цілі проти цієї атаки, що може перетворити влучання на промах.",
    "You can strengthen your defenses at the cost of your vitality. Whenever you fail a saving throw, you can spend one of your Hit Dice, rolling it and adding the number rolled to the result of the save.":
        "Ви можете зміцнити свій захист ціною життєвих сил. Щоразу, коли ви провалюєте кидок протидії, можете витратити одну свою кістку здоров’я, кинути її й додати результат до цього кидка протидії.",
    "Interdicted creatures have disadvantage on Wisdom and Charisma saving throws for 2 turns.":
        "Істоти під дією Заборони на 2 ходи мають заваду на кидки протидії мудрістю та харизмою.",
    "Vampiric hunger has been temporarily sated. +1 to all <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag>, <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>, and most <LSTag Tooltip=\"AbilityCheck\">Ability Checks</LSTag>.":
        "Вампірський голод тимчасово вгамовано. +1 до всіх <LSTag Tooltip=\"AttackRoll\">кидків атаки</LSTag>, <LSTag Tooltip=\"SavingThrow\">кидків протидії</LSTag> і більшості <LSTag Tooltip=\"AbilityCheck\">перевірок характеристик</LSTag>.",
    """Your skill in close combat enables you to inflict crushing blows while keeping your opponent off balance. When you hit a creature with an attack roll using a Melee weapon, you can take a Reaction to deal an extra 2d6 damage of the same type dealt by the weapon. That creature has Disadvantage on its next attack roll before the start of your next turn.

The damage becomes 4d6 when you reach Monster Hunter level 11.""":
        """Ваша майстерність у ближньому бою дає змогу завдавати нищівних ударів і виводити супротивника з рівноваги. Коли ви влучаєте в істоту атакою зброєю ближнього бою, ви можете застосувати реагування, щоб завдати додаткової шкоди 2d6 того самого типу, що й зброя. Наступний кидок атаки цієї істоти до початку вашого наступного ходу має заваду.

На 11-му рівні мисливця на чудовиськ додаткова шкода збільшується до 4d6.""",
    "When you hit a creature with an attack roll using a Melee weapon, you can take a Reaction to deal an extra [1]. That creature has Disadvantage on its next attack roll before the start of your next turn.":
        "Коли ви влучаєте в істоту атакою зброєю ближнього бою, ви можете застосувати реагування, щоб завдати додаткової [1]. Наступний кидок атаки цієї істоти до початку вашого наступного ходу має заваду.",
    "This creature has disadvantage on its next saving throw against spells.":
        "Ця істота має заваду на наступний кидок протидії проти закляття.",
    "You regain a number of Hit Points equal to 1d10 plus your Wisdom modifier.":
        "Ви відновлюєте очки здоров’я в кількості 1d10 + ваш модифікатор мудрості.",
    "The target has Disadvantage on the next saving throw it makes before the start of your next turn.":
        "Наступний кидок протидії цілі до початку вашого наступного ходу має заваду.",
    "When you score a Critical Hit that deals Slashing damage to a creature, it has Disadvantage on attack rolls until the start of your next turn.":
        "Коли ви завдаєте істоті критичного влучання з рубаною шкодою, вона має заваду на кидки атаки до початку вашого наступного ходу.",
    "While your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is not active, you have Resistance to Psychic damage. While your Rage is active, you have Resistance to every damage type except Force and Psychic.":
        "Поки ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag> неактивна, ви маєте стійкість до психічної шкоди. Поки діє ваша Лють, ви маєте стійкість до всіх типів шкоди, крім силової та психічної.",
    "While your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is not active, you can take the Disengage or Help action as a Bonus Action. While your Rage is active, your attack rolls with Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on the d20.":
        "Поки ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag> неактивна, ви можете виконати дію «Відступ» або «Допомога» як вторинну дію. Поки діє ваша Лють, кидки атаки Ударами голіруч завдають критичного влучання, якщо на d20 випадає 19 або 20.",
    "Creatures have Disadvantage on saving throws against the next spell you cast before the end of your next turn that involves a saving throw.":
        "Істоти мають заваду на кидки протидії проти наступного вашого закляття, проказаного до кінця вашого наступного ходу, якщо той вимагає кидка протидії.",
    "Advantage on Intelligence, Wisdom, and Charisma <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Перевага на <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> інтелектом, мудрістю та харизмою.",
    "Has Disadvantage on the next D20 Test it makes.":
        "Має заваду на свою наступну перевірку D20.",
    "Has disadvantage on attack rolls.":
        "Має заваду на кидки атаки.",
    "If you hit a creature with this weapon, that creature has Disadvantage on its next attack roll before the start of your next turn.":
        "Якщо ви влучите в істоту цією зброєю, її наступний кидок атаки до початку вашого наступного ходу матиме заваду.",
    "Once per <LSTag Tooltip=\"ShortRest\">Short Rest</LSTag>, when you would drop to [1] <LSTag Tooltip=\"HitPoints\">hit points</LSTag> while <LSTag Type=\"Status\" Tooltip=\"RAGE\">Enraged</LSTag>, you instead regain hit points equal to twice your Barbarian level and avoid being <LSTag Type=\"Status\" Tooltip=\"DOWNED\">Downed</LSTag>.":
        "Один раз за <LSTag Tooltip=\"ShortRest\">короткий відпочинок</LSTag>, коли під час <LSTag Type=\"Status\" Tooltip=\"RAGE\">Люті</LSTag> ваші <LSTag Tooltip=\"HitPoints\">очки здоров’я</LSTag> мали б знизитися до [1], ви натомість відновлюєте їх у кількості, що вдвічі перевищує ваш рівень варвара, і уникаєте стану <LSTag Type=\"Status\" Tooltip=\"DOWNED\">падіння</LSTag>.",
    "When a creature that you can see within 30 feet of yourself makes an attack roll, you can take a Reaction to impose Disadvantage on the attack roll, causing light to flare before it hits or misses.":
        "Коли видима вам істота в межах 30 футів виконує кидок атаки, ви можете застосувати реагування й накласти на цей кидок заваду: перед ціллю атаки спалахує світло, перш ніж атака влучить чи схибить.",
    """When an attack hits you and deals bludgeoning, piercing, or slashing damage, you can take a Reaction to reduce the total damage you take. The reduction equals 1d10 + your Dexterity modifier + your monk level.

If this reduces the damage to 0, you can spend 1 Ki Point to use Redirect Attacks.""":
        """Коли атака влучає у вас і завдає дробильної, колотої або рубаної шкоди, ви можете застосувати реагування, щоб зменшити загальну зазнану шкоду на 1d10 + ваш модифікатор спритності + ваш рівень монаха.

Якщо це зменшує шкоду до 0, ви можете витратити 1 очко кі, щоб застосувати «Перенаправлення атаки».""",
    """Reduce the bludgeoning, piercing, or slashing damage you take by 1d10 + your Dexterity <LSTag Tooltip="AbilityModifier">modifier</LSTag> + your monk level.

If this reduces the damage to 0, you can spend 1 Ki Point to use Redirect Attacks.""":
        """Зменште зазнану дробильну, колоту або рубану шкоду на 1d10 + ваш <LSTag Tooltip="AbilityModifier">модифікатор</LSTag> спритності + ваш рівень монаха.

Якщо це зменшує шкоду до 0, ви можете витратити 1 очко кі, щоб застосувати «Перенаправлення атаки».""",
    "Rule: Strength Requirement (Heavy Melee Weapon)": "Правило: вимога до сили (важка зброя ближнього бою)",
    "Performance": "Виступ",
    """When a creature you can see attacks a target other than you that is within [1] of you, you can take a Reaction to interpose your Shield if you’re holding one. You impose Disadvantage on the triggering attack roll and all other attack rolls against the target until the start of your next turn if you remain within [1] of the target.""":
        "Коли видима вам істота атакує не вас, а іншу ціль у межах [1] від вас, ви можете застосувати реагування й підставити щит, якщо тримаєте його. Кидок атаки, що спричинив це реагування, і всі інші кидки атаки проти цілі мають заваду до початку вашого наступного ходу, якщо ви залишаєтеся в межах [1] від неї.",
    """You summon an otherworldly steed and immediately mount it.

The steed can take one of the following actions of your choice on each of its turns: <LSTag Type="Spell" Tooltip="Shout_Dash">Dash</LSTag>, Disengage, Dodge, or Attack.

While mounted on the steed, when you take damage of 4 or higher, you must make a DC 8 Dexterity saving throw. On a failed save, you fall off the steed and have the Prone condition for 1 turn.""":
        """Ви прикликаєте потойбічного скакуна й одразу сідаєте на нього.

У кожен свій хід скакун може виконати одну з таких дій на ваш вибір: <LSTag Type="Spell" Tooltip="Shout_Dash">Ривок</LSTag>, Відступ, Ухилення або Атака.

Перебуваючи в сідлі, коли ви зазнаєте щонайменше 4 шкоди, ви повинні виконати кидок протидії спритністю з МС 8. У разі невдачі ви падаєте зі скакуна й на 1 хід набуваєте стану повалення.""",
    """Focusing on avoiding attacks.

<LSTag Tooltip="AttackRoll">Attack Rolls</LSTag> against the affected entity have <LSTag Tooltip="Disadvantage">Disadvantage</LSTag>, and the entity has <LSTag Tooltip="Advantage">Advantage</LSTag> on Dexterity <LSTag Tooltip="SavingThrow">Saving Throws</LSTag>.""":
        """Зосередження на уникненні атак.

<LSTag Tooltip="AttackRoll">Кидки атаки</LSTag> проти ураженої істоти мають <LSTag Tooltip="Disadvantage">заваду</LSTag>, а сама вона має <LSTag Tooltip="Advantage">перевагу</LSTag> на <LSTag Tooltip="SavingThrow">кидки протидії</LSTag> спритністю.""",
    """Speed Increase. Your Speed increases by 10 feet.

<LSTag Type="Spell" Tooltip="Shout_Dash">Dash</LSTag> over <LSTag Type="Status" Tooltip="DIFFICULT_TERRAIN">Difficult Terrain</LSTag>. When you take the Dash action on your turn, Difficult Terrain doesn't cost you extra movement for the rest of that turn.

Agile Movement. Opportunity Attacks have Disadvantage against you.""":
        """Збільшення швидкості. Ваша швидкість збільшується на 10 футів.

<LSTag Type="Spell" Tooltip="Shout_Dash">Ривок</LSTag> <LSTag Type="Status" Tooltip="DIFFICULT_TERRAIN">складним рельєфом</LSTag>. Коли у свій хід ви виконуєте дію «Ривок», до кінця ходу складний рельєф не потребує від вас додаткових витрат руху.

Спритний рух. Принагідні атаки проти вас мають заваду.""",
    """You learn Druidic and one cantrip from the Druid spell list. It counts as a Bard spell for you but doesn’t count against the number of cantrips you know. 

Additionally, choose one of the following skills: <LSTag Type="Skills" Tooltip="AnimalHandling">Animal Handling</LSTag>, <LSTag Type="Skills" Tooltip="Insight">Insight</LSTag>, <LSTag Type="Skills" Tooltip="Medicine">Medicine</LSTag>, <LSTag Type="Skills" Tooltip="Nature">Nature</LSTag>, <LSTag Type="Skills" Tooltip="Perception">Perception</LSTag>, or <LSTag Type="Skills" Tooltip="Survival">Survival</LSTag>. You have proficiency in that skill.""":
        """Ви вивчаєте друїдську мову й одне замовляння зі списку заклять друїда. Для вас воно вважається закляттям барда, але не враховується до кількості відомих вам замовлянь.

Крім того, виберіть одну з таких навичок: <LSTag Type="Skills" Tooltip="AnimalHandling">Догляд за тваринами</LSTag>, <LSTag Type="Skills" Tooltip="Insight">Проникливість</LSTag>, <LSTag Type="Skills" Tooltip="Medicine">Медицина</LSTag>, <LSTag Type="Skills" Tooltip="Nature">Природа</LSTag>, <LSTag Type="Skills" Tooltip="Perception">Відчуття</LSTag> або <LSTag Type="Skills" Tooltip="Survival">Виживання</LSTag>. Ви отримуєте володіння вибраною навичкою.""",
    "The target and each creature of your choice in a 10-foot Emanation originating from you make a Strength saving throw against your spell save DC. On a failed save, a creature is pushed 15 feet straight away from you and has the Prone condition.":
        "Ціль і кожна вибрана вами істота у 10-футовій еманації від вас виконує кидок протидії силою проти вашої МС протидії закляттям. У разі невдачі істоту відштовхує на 15 футів прямо від вас, і вона набуває стану повалення.",
    "Whenever a target fails the saving throw against a Counterspell you cast, you regain 1d4 Sorcery Points.":
        "Щоразу, коли ціль провалює кидок протидії проти проказаного вами «Контрзакляття», ви відновлюєте 1d4 очок чародійства.",
    """You can use magic runes to enhance your gear. At 3rd level, you learn the Cloud, Fire, Frost, and Stone runes. At 7th level, you learn the Hill and Storm runes.

You can use your runes a number of times based on your Fighter level: 3 uses at 3rd level, 4 uses at 7th level, and 5 uses at 10th level. You regain all expended uses when you finish a Short Rest.

If a rune requires a saving throw, its save DC equals 8 + your proficiency bonus + your Constitution modifier.""":
        """Ви можете посилювати спорядження магічними рунами. На 3-му рівні ви вивчаєте руни Хмари, Вогню, Морозу та Каменю, а на 7-му — руни Пагорба і Бурі.

Кількість застосувань рун залежить від вашого рівня бійця: 3 на 3-му рівні, 4 на 7-му і 5 на 10-му. Усі витрачені застосування відновлюються після короткого відпочинку.

Якщо руна вимагає кидка протидії, його МС дорівнює 8 + ваш бонус спеціалізації + ваш модифікатор статури.""",
    """Requires attunement by a Druid or Ranger.

When you cast a spell that restores hit points, you can roll a d4 and add the number rolled to the amount of hit points restored.""":
        """Потребує налаштування друїдом або слідопитом.

Коли ви проказуєте закляття, що відновлює очки здоров’я, ви можете кинути d4 й додати результат до кількості відновлених очок здоров’я.""",
    """Your patron's might allows you to drain vitality from those you curse, granting you the following benefits.

Hungering Hex. Whenever a target cursed by your Hex drops to 0 Hit Points as a result of your actions, you regain Hit Points equal to 1d8 plus your Charisma modifier.

Inevitable Blade. Once per turn, when you make an attack roll against a target cursed by your Hex and miss, you can deal 1d6 Necrotic damage.""":
        """Могутність вашого покровителя дає змогу висмоктувати життєву силу з проклятих вами істот. Ви отримуєте такі переваги.

Голодне прокляття. Щоразу, коли внаслідок ваших дій очки здоров’я цілі під дією вашого «Прокляття» знижуються до 0, ви відновлюєте 1d8 + ваш модифікатор харизми очок здоров’я.

Невідворотний клинок. Один раз за хід, коли ви промахуєтеся кидком атаки проти цілі під дією вашого «Прокляття», ви можете завдати їй 1d6 некротичної шкоди.""",
    "When a creature you can see within 30 feet of yourself succeeds on a saving throw, you can take a Reaction and expend a use of your Channel Divinity to impose Disadvantage on the saving throw, prying into their mind before they succeed or fail.":
        "Коли видима вам істота в межах 30 футів успішно виконує кидок протидії, ви можете застосувати реагування, витратити одне застосування Божого наснаження й накласти на цей кидок заваду, проникаючи в розум істоти до того, як визначиться успіх чи невдача.",
    """You can call forth spirits of the dead to empower you and your allies. When you take a Bonus Action to give a creature a <LSTag Type="ActionResource" Tooltip="BardicInspiration">Bardic Inspiration</LSTag> die, you can call forth the powers of a random spirit. To determine the spirit you channel, roll the Bardic Inspiration die and refer to the Spirits from Beyond table. The spirit remains channeled until you unleash it or until you finish a Long Rest.""":
        """Ви можете прикликати духів померлих, щоб наділяти силою себе та союзників. Коли ви вторинною дією даєте істоті кістку <LSTag Type="ActionResource" Tooltip="BardicInspiration">Бардівського натхнення</LSTag>, ви можете прикликати силу випадкового духа. Щоб визначити духа, якого ви проводитимете, киньте кістку Бардівського натхнення й звіртеся з таблицею «Духи з-поза меж». Дух залишається проведеним, доки ви не вивільните його або не завершите довгий відпочинок.""",
    """You can call forth spirits of the dead to empower you and your allies. When you take a Bonus Action to give a creature a <LSTag Type="ActionResource" Tooltip="BardicInspiration">Bardic Inspiration</LSTag> die, you can call forth the powers of a random spirit. To determine the spirit you channel, roll the Bardic Inspiration die and refer to the Spirits from Beyond table. The spirit remains channeled until you unleash it or until you finish a Long Rest.

Controlled Channeling. As a Bonus Action, you can expend a use of your Bardic Inspiration and channel a specific spirit. When you do so, choose the spirit from the Spirits from Beyond table rather than rolling. The chosen spirit’s corresponding number must be less than or equal to the highest number on your Bardic Inspiration die; for example, if your Bardic Inspiration die is a d8, you can choose to channel any spirit up to (and including) the Shade.

<LSTag Type="Spell" Tooltip="Target_UnleashingASpirit">Unleashing a Spirit</LSTag>. As a Magic action, you can unleash one of your channeled spirits. Choose one creature you can see within 30 feet of yourself as the spirit’s target. The spirit then takes effect; if a spirit’s effect requires a saving throw, the DC equals your Bard spell save DC. This action allows you to actually use the spirit.""":
        """Ви можете прикликати духів померлих, щоб наділяти силою себе та союзників. Коли ви вторинною дією даєте істоті кістку <LSTag Type="ActionResource" Tooltip="BardicInspiration">Бардівського натхнення</LSTag>, ви можете прикликати силу випадкового духа. Щоб визначити духа, якого ви проводитимете, киньте кістку Бардівського натхнення й звіртеся з таблицею «Духи з-поза меж». Дух залишається проведеним, доки ви не вивільните його або не завершите довгий відпочинок.

Кероване проведення. Вторинною дією ви можете витратити одне застосування Бардівського натхнення й провести певного духа. Замість кидка виберіть духа з таблиці «Духи з-поза меж». Номер вибраного духа має бути не більшим за найбільше число на вашій кістці Бардівського натхнення. Наприклад, якщо ваша кістка — d8, ви можете провести будь-якого духа до Тіні включно.

<LSTag Type="Spell" Tooltip="Target_UnleashingASpirit">Вивільнення духа</LSTag>. Магічною дією ви можете вивільнити одного зі своїх проведених духів. Виберіть видиму вам істоту в межах 30 футів ціллю духа. Після цього дух спрацьовує; якщо його ефект вимагає кидка протидії, МС дорівнює вашій МС протидії закляттям барда. Ця дія застосовує ефект духа.""",
    "The number of unexpended Hit Dice you can roll increases by one for each spell slot level above 2.":
        "За кожен рівень чарунки вище 2-го кількість невитрачених кісток здоров’я, які ви можете кинути, збільшується на одну.",
    "Gains [1] Temporary Hit Points. If a creature hits the target with a melee attack roll before the spell ends, that creature takes Piercing damage equal to the number of Temporary Hit Points lost as a result of the attack. This spell ends early if the target has no remaining Temporary Hit Points granted by this spell.":
        "Отримує [1] тимчасових очок здоров’я. Якщо до завершення закляття істота влучає в ціль атакою ближнього бою, нападник зазнає колотої шкоди в кількості, що дорівнює втраченим унаслідок атаки тимчасовим очкам здоров’я. Закляття завершується достроково, якщо в цілі не лишилося наданих ним тимчасових очок здоров’я.",
    "When you cast a spell that forces a creature to make a saving throw, you can spend 2 Sorcery Points to give one target of the spell Disadvantage on saves against the spell.":
        "Коли ви проказуєте закляття, що змушує істоту виконати кидок протидії, ви можете витратити 2 очки чародійства, щоб одна ціль мала заваду на кидки протидії проти цього закляття.",
    "Your Speed increases by 10 feet. It increases by another 5 feet when you reach Bard levels 6 (total increase of 15 feet).":
        "Ваша швидкість збільшується на 10 футів. На 6-му рівні барда вона збільшується ще на 5 футів (загалом на 15 футів).",
    "Has disadvantage on the next weapon attack roll it makes before the end of its next turn.":
        "Її наступний кидок атаки зброєю до кінця наступного ходу має заваду.",
    "You can call on the forces of nature to reveal certain strengths and weaknesses of your prey. While a creature is marked by your Hunter's Mark, your weapon attacks ignore that creature's Resistance to Bludgeoning, Piercing, and Slashing damage.":
        "Ви можете закликати сили природи, щоб виявити певні сильні та слабкі сторони здобичі. Поки істота позначена вашою «Міткою мисливця», ваші атаки зброєю ігнорують її стійкість до дробильної, колотої та рубаної шкоди.",
    """You learn how to use the universal language of dance. As a Bonus Action, you can expend one use of your <LSTag Type="ActionResource" Tooltip="BardicInspiration">Bardic Inspiration</LSTag> to dance and reinvigorate another creature of your choice who can see you.

When you do, roll your Bardic Inspiration die; that creature gains a number of Temporary Hit Points equal to the number rolled plus your Charisma modifier (minimum of 2 Temporary Hit Points). When a creature gains Temporary Hit Points in this way, it can immediately take a Reaction to move up to its Speed without provoking Opportunity Attacks or take the Dodge action.""":
        """Ви опановуєте універсальну мову танцю. Вторинною дією ви можете витратити одне застосування <LSTag Type="ActionResource" Tooltip="BardicInspiration">Бардівського натхнення</LSTag>, щоб танцем підбадьорити іншу видиму вам істоту на ваш вибір.

Киньте свою кістку Бардівського натхнення. Істота отримує тимчасові очки здоров’я в кількості, що дорівнює результату кидка + ваш модифікатор харизми (щонайменше 2 очки). Отримавши таким чином тимчасові очки здоров’я, істота може негайно застосувати реагування, щоб переміститися на відстань до своєї швидкості, не провокуючи принагідних атак, або виконати дію «Ухилення».""",
    """Your patron grants you the ability to move between the boundaries of the planes. You can cast Misty Step without expending a spell slot a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.

In addition, whenever you cast that spell, you can choose one of the following additional effects.

Refreshing Step. Immediately after you teleport, you and one creature you can see within 10 feet of yourself gains 1d10 Temporary Hit Points.

Taunting Step. Creatures within 10 feet of the space you left must succeed on a Wisdom saving throw against your spell save DC or have Disadvantage on attack rolls against creatures other than you until the start of your next turn.""":
        """Ваш покровитель дає вам змогу перетинати межі планів. Ви можете проказувати «Маревний крок», не витрачаючи чарунки. Кількість застосувань дорівнює вашому модифікатору харизми (щонайменше один раз), а всі витрачені застосування відновлюються після довгого відпочинку.

Крім того, щоразу, коли ви проказуєте це закляття, ви можете вибрати один з таких додаткових ефектів.

Освіжний крок. Одразу після телепортації ви й одна видима вам істота в межах 10 футів отримуєте 1d10 тимчасових очок здоров’я.

Глузливий крок. Істоти в межах 10 футів від простору, який ви залишили, повинні успішно виконати кидок протидії мудрістю проти вашої МС протидії закляттям, інакше їхні кидки атаки проти всіх істот, крім вас, матимуть заваду до початку вашого наступного ходу.""",
    """Your connection to undeath saturates your body. You gain the following benefits.

Necrotic Resilience. You have Resistance to Necrotic damage. While using your Form of Dread, you have Immunity to Necrotic damage.

Unholy Resuscitation. If you drop to 0 Hit Points and don’t die outright, you can cause your body to erupt with deathly energy. Each creature of your choice in a 30-foot Emanation originating from you makes a Constitution saving throw against your spell save DC, taking Necrotic damage equal to 2d10 plus your Charisma modifier on a failed save or half as much damage on a successful one. Your Hit Points then change to twice your Warlock level, and you gain 1 Exhaustion level.

Once you use this benefit, you can’t use it again until you finish a Short or Long Rest.""":
        """Зв’язок із нежиттю насичує ваше тіло. Ви отримуєте такі переваги.

Некротична стійкість. Ви маєте стійкість до некротичної шкоди. Поки діє ваша «Форма жаху», ви маєте імунітет до некротичної шкоди.

Нечестиве відродження. Якщо ваші очки здоров’я знижуються до 0, але ви не помираєте одразу, ви можете змусити своє тіло вибухнути смертельною енергією. Кожна вибрана вами істота у 30-футовій еманації від вас виконує кидок протидії статурою проти вашої МС протидії закляттям. У разі невдачі вона зазнає 2d10 + ваш модифікатор харизми некротичної шкоди, а в разі успіху — половину. Після цього ваші очки здоров’я становлять подвійний рівень чаклуна, а ви отримуєте 1 рівень виснаження.

Застосувавши цю перевагу, ви не зможете зробити це знову до завершення короткого або довгого відпочинку.""",
    "If you drop to 0 Hit Points and don’t die outright, you can cause your body to erupt with deathly energy. Each creature of your choice in a 30-foot Emanation originating from you makes a Constitution saving throw against your spell save DC, taking Necrotic damage equal to 2d10 plus your Charisma modifier on a failed save or half as much damage on a successful one. Your Hit Points then change to twice your Warlock level, and you gain 1 Exhaustion level.":
        "Якщо ваші очки здоров’я знижуються до 0, але ви не помираєте одразу, ви можете змусити своє тіло вибухнути смертельною енергією. Кожна вибрана вами істота у 30-футовій еманації від вас виконує кидок протидії статурою проти вашої МС протидії закляттям. У разі невдачі вона зазнає 2d10 + ваш модифікатор харизми некротичної шкоди, а в разі успіху — половину. Після цього ваші очки здоров’я становлять подвійний рівень чаклуна, а ви отримуєте 1 рівень виснаження.",
    """Eladrin are elves of the Feywild, a realm of perilous beauty and boundless magic. Using that magic, eladrin can step from one place to another in the blink of an eye, and each eladrin resonates with emotions captured in the Feywild in the form of seasons—affinities that affect the eladrin’s mood and appearance. An eladrin’s season can change, though some remain in one season forever. Choose your season or roll on the Eladrin Seasons table. Your Trance trait lets you change your season.

Like other elves, eladrin can live to be over 750 years old.""":
        """Еладріни — ельфи Феєлону, царини небезпечної краси й безмежної магії. Завдяки цій магії вони здатні вмить переходити з місця на місце. Кожен еладрін співзвучний з емоціями, утіленими у Феєлоні як пори року, і ця спорідненість впливає на його настрій та зовнішність. Пора року еладріна може змінюватися, хоча дехто назавжди зберігає одну. Виберіть свою пору року або киньте кістку за таблицею «Пори року еладрінів». Ваша риса «Транс» дає змогу змінювати пору року.

Як і інші ельфи, еладріни можуть жити понад 750 років.""",
    """You gain one of the following feature options of your choice. Whenever you finish a Short or Long Rest, you can replace the chosen option with the other one.

Escape the Horde
Opportunity Attacks have Disadvantage against you.

Multiattack Defense
When a creature hits you with an attack roll, that creature has Disadvantage on all other attack rolls against you this turn.""":
        """Виберіть один із таких варіантів особливості. Після кожного короткого або довгого відпочинку ви можете замінити обраний варіант іншим.

Втеча від орди
Принагідні атаки проти вас мають заваду.

Захист від множинних атак
Коли істота влучає у вас атакою, усі інші її кидки атаки проти вас у цей хід мають заваду.""",
    "When you reduce an enemy to 0 Hit Points, you gain Temporary Hit Points equal to your Charisma modifier plus your Warlock level (minimum of 1 Temporary Hit Point). You also gain this benefit if someone else reduces an enemy within 10 feet of you to 0 Hit Points.":
        "Коли ви знижуєте очки здоров’я ворога до 0, ви отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому модифікатору харизми + ваш рівень чаклуна (щонайменше 1 очко). Ви також отримуєте цю перевагу, якщо хтось інший знижує до 0 очки здоров’я ворога в межах 10 футів від вас.",
    "When you score a Critical Hit that deals Bludgeoning damage to a creature, attack rolls against that creature have Advantage until the start of your next turn.":
        "Коли ви завдаєте істоті критичного влучання з дробильною шкодою, кидки атаки проти неї мають перевагу до початку вашого наступного ходу.",
    """Weapon Mastery: Slow

If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by 10 feet until the start of your next turn.""":
        """Володіння зброєю: Уповільнення

Якщо ви влучите в істоту цією зброєю й завдасте їй шкоди, ви можете зменшити її швидкість на 10 футів до початку вашого наступного ходу.""",
    """Weapon Mastery: Vex

If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.""":
        """Володіння зброєю: Доймання

Якщо ви влучите в істоту цією зброєю й завдасте їй шкоди, ви матимете перевагу на свій наступний кидок атаки проти цієї істоти до кінця вашого наступного ходу.""",
    "Requires attunement by a Paladin": "Потребує налаштування паладином",
    "Requires attunement by a Paladin.": "Потребує налаштування паладином.",
    "Requires attunement by a Druid or Ranger": "Потребує налаштування друїдом або слідопитом",
    """Your movements become so graceful that even the most cold-hearted enemies are filled with remorse for having stopped your dance. Whenever a creature hits you with an Opportunity Attack or hits you with an attack roll while you’re benefiting from the Dodge action, that creature takes Psychic damage equal to your Charisma modifier plus half your Bard level (round down).

In addition, you always have the Charm Person spell prepared, and you can cast it without a Verbal component. With this feature, you can cast it without expending a spell slot; when you do, it is cast as a level 3 spell, and the targets don’t make their saving throws with Advantage as a result of you or your allies fighting them. Once you cast the spell with this feature, you can’t do so in this way again until you finish a Long Rest.""":
        """Ваші рухи стають такими граційними, що навіть найбезжальніші вороги шкодують, що перервали ваш танець. Щоразу, коли істота влучає у вас принагідною атакою або будь-якою атакою, поки ви користуєтеся дією «Ухилення», вона зазнає психічної шкоди в кількості, що дорівнює вашому модифікатору харизми + половина вашого рівня барда (з округленням униз).

Крім того, ви завжди маєте підготовленим закляття «Причарування особи» і можете проказувати його без словесного складника. За допомогою цієї особливості ви можете проказати його, не витрачаючи чарунки; у такому разі воно проказується як закляття 3-го рівня, а цілі не отримують переваги на кидки протидії лише через те, що вони б’ються з вами чи вашими союзниками. Застосувавши таким чином це закляття, ви не зможете зробити це знову до завершення довгого відпочинку.""",
    """You can imbue yourself with a primal power called <LSTag Type="Status" Tooltip="RAGE">Rage</LSTag>, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren’t wearing Heavy armor.

You can enter your Rage the number of times shown for your Barbarian level in the Rages column of the Barbarian Features table. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.""":
        """Ви можете сповнитися первісною силою, що зветься <LSTag Type="Status" Tooltip="RAGE">Люттю</LSTag> і наділяє надзвичайною міццю та витривалістю. Якщо на вас немає важких обладунків, ви можете увійти в Лють вторинною дією.

Кількість входжень у Лють указано для вашого рівня варвара у стовпці «Лють» таблиці особливостей варвара. Ви відновлюєте одне витрачене застосування після короткого відпочинку і всі витрачені — після довгого.""",
    """You can weave fey magic into a song or dance to fill others with vigor. As a Bonus Action, you can expend one use of Bardic Inspiration and roll your Bardic Inspiration die. When you do so, choose a number of other creatures within [1] of yourself, up to your Charisma modifier (minimum of one creature).

Each of those creatures gains Temporary Hit Points equal to twice the number rolled on the Bardic Inspiration die, and each can move without provoking Opportunity Attacks until the end of its next turn.""":
        """Ви можете вплітати фейську магію в пісню чи танець, наповнюючи інших снагою. Вторинною дією ви можете витратити одне застосування Бардівського натхнення й кинути його кістку. Виберіть інших істот у межах [1] у кількості, що не перевищує вашого модифікатора харизми (щонайменше одну).

Кожна отримує тимчасові очки здоров’я в кількості, що вдвічі перевищує результат кидка, і може переміщуватися, не провокуючи принагідних атак, до кінця свого наступного ходу.""",
    "Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Cleric cantrip.":
        "Могутнє проказування. Додайте свій модифікатор мудрості до шкоди, яку ви завдаєте будь-яким замовлянням клірика.",
    "Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Druid cantrip.":
        "Могутнє проказування. Додайте свій модифікатор мудрості до шкоди, яку ви завдаєте будь-яким замовлянням друїда.",
}


EXACT_OVERRIDES.update(_MISPLACED_EXACT_OVERRIDES)

EXACT_OVERRIDES.update({
    "If you fail a saving throw, you can instead treat it as a success. ":
        "Коли ви провалюєте кидок протидії, ви можете натомість вважати його успішним. ",
    """You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.

You can use this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

When you reach certain Fighter levels, you gain more uses of this feature.""":
        """Ви маєте обмежений запас фізичної та духовної снаги. Вторинною дією ви можете скористатися ним і відновити 1d10 + ваш рівень бійця очок здоров’я.

Цю особливість можна застосувати двічі. Одне витрачене застосування відновлюється після короткого відпочинку, а всі — після довгого.

На певних рівнях бійця ви отримуєте додаткові застосування.""",
    "You have Resistance to Psychic damage. Moreover, you are immune to the Charmed and Frightened conditions.":
        "Ви маєте стійкість до психічної шкоди та імунітет до станів причарування й переляку.",
    "Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once.":
        "Щоразу, коли ви маєте перевагу на кидок атаки зі спритністю, інтелектом, мудрістю або харизмою, ви можете один раз перекинути одну з кісток.",
    "Whenever you take the Dodge action in combat, you can spend one Hit Die to heal yourself. Roll the die, add your Constitution modifier, and regain a number of hit points equal to the total (minimum of 1).":
        "Щоразу, коли в бою ви виконуєте дію «Ухилення», ви можете витратити одну кістку здоров’я, щоб зцілитися. Киньте її, додайте свій модифікатор статури й відновіть очки здоров’я в кількості, що дорівнює сумі (щонайменше 1).",
})

EXACT_OVERRIDES.update({
    "While in Dragon Shape, your attacks count as magical for the purpose of overcoming <LSTag Tooltip=\"Resistant\">Resistance</LSTag> and <LSTag Tooltip=\"Immune\">Immunity</LSTag> to nonmagical damage, and your AC increases by 1.":
        "Перебуваючи в Драконячій подобі, ви отримуєте +1 до РЗ, а ваші атаки вважаються магічними для подолання <LSTag Tooltip=\"Resistant\">стійкості</LSTag> та <LSTag Tooltip=\"Immune\">імунітету</LSTag> до немагічної шкоди.",
    "When you make the extra attack of the Light property, you can make it as part of the Attack action instead of as a Bonus Action. You can make this extra attack only once per turn.":
        "Додаткову атаку властивості «Легка» можна виконати як частину дії «Атака», а не вторинною дією. Таку додаткову атаку можна виконати лише один раз за хід.",
    "You can make an Unarmed Strike as a Bonus Action.":
        "Вторинною дією ви можете виконати удар голіруч.",
    "You can use Throw as a Bonus Action. You can use a Spell Scroll as a Bonus Action. The requirements to use a Spell Scroll are unchanged.":
        "Вторинною дією ви можете виконати «Кидок» або скористатися сувоєм закляття. Вимоги до використання сувою не змінюються.",
    "As a bonus action, you can give yourself advantage on your ranged weapon attack roll on the current turn. You can use this bonus action only if you haven’t moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn.":
        "Вторинною дією ви можете надати собі перевагу в кидку атаки далекобійною зброєю протягом поточного ходу. Застосувати цю дію можна лише до переміщення; після неї ваша швидкість дорівнює 0 до кінця ходу.",
    "You draw power from the strange and ancient horrors of the land, causing you to sprout unnatural growths, such as bloody antlers or putrid fangs, or causing your shadow to lengthen or twist around you. As a Bonus Action, you can expend a use of Favored Enemy to transform into a ghastly form, gaining the following benefits for 1 minute or until you have the Incapacitated condition, die, or end the transformation (no action required).":
        "Ви черпаєте силу з дивних прадавніх жахів землі: на вас виростають неприродні криваві роги чи гнилі ікла, а тінь видовжується й звивається довкола. Вторинною дією ви можете витратити одне використання «Обраного ворога» й набути моторошної подоби. Наведені нижче переваги діють 1 хвилину, доки ви не набудете стану недієздатності, не помрете або не завершите перетворення без витрати дії.",
    "For the next minute, you can teleport up to 30 feet as a Bonus Action on each of your turns.":
        "Протягом наступної хвилини ви можете щохідно телепортуватися вторинною дією на відстань до 30 футів.",
    "You can make an additional Off-Hand Attack as a Bonus Action this turn.":
        "Цього ходу вторинною дією ви можете виконати додаткову Атаку другою рукою.",
    "When you cast Mage Hand, you can cast it as a Bonus Action, and you can make the spectral hand Invisible. The hand can also attempt to pick pockets, making a Dexterity (<LSTag Type=\"Skills\" Tooltip=\"SleightOfHand\">Sleight of Hand</LSTag>) check using your own modifier as the Arcane Trickster.":
        "Ви можете проказувати «Магічну руку» вторинною дією та робити примарну руку невидимою. Рука також може обкрадати кишені, виконуючи перевірку спритності (<LSTag Type=\"Skills\" Tooltip=\"SleightOfHand\">Спритність рук</LSTag>) із вашим модифікатором Містичного штукаря.",
    "Immediately after a creature within 5 feet of you hits you with a melee attack, you can make an Opportunity Attack against that creature.":
        "Одразу після того, як істота в межах 5 футів влучає у вас атакою ближнього бою, ви можете виконати проти неї принагідну атаку.",
    "On a turn, you can expend only one spell slot to cast a spell. This rule means you can’t, for example, cast a spell with a spell slot using the Magic action and another one using a Bonus Action on the same turn.":
        "За один хід ви можете витратити лише одну чарунку на проказування закляття. Наприклад, протягом одного ходу не можна проказати одне закляття з чарункою магічною дією, а інше — вторинною дією.",
    "For the next minute, all your spells with a casting time of an action have a casting time of a Bonus Action.":
        "Протягом наступної хвилини час проказування ваших заклять із часом «одна дія» змінюється на «вторинна дія».",
})

EXACT_OVERRIDES.update({
    "You have honed your ability to resist mind-altering powers. You gain proficiency in Wisdom saving throws.":
        "Ви загартували розум проти сил, що змінюють свідомість. Ви отримуєте спеціалізацію в кидках протидії мудрістю.",
    "You gain proficiency in two of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"Arcana\">Arcana</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">History</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Nature\">Nature</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Religion\">Religion</LSTag>. You have Expertise in those two skills.":
        "Ви отримуєте спеціалізацію та майстерність у двох навичках на свій вибір: <LSTag Type=\"Skills\" Tooltip=\"Arcana\">Таїнства</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">Історія</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Nature\">Природа</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Religion\">Релігія</LSTag>.",
    "You gain proficiency in the <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag> and <LSTag Type=\"Skills\" Tooltip=\"Medicine\">Medicine</LSTag> skills. You can brew two alchemical solutions instead of one when combining extracts, if you succeed a <LSTag Tooltip=\"DifficultyClass\">DC</LSTag> 15 Medicine <LSTag Tooltip=\"AbilityCheck\">Check</LSTag>.":
        "Ви отримуєте спеціалізацію в навичках <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag> і <LSTag Type=\"Skills\" Tooltip=\"Medicine\">Медицина</LSTag>. Поєднуючи екстракти, ви можете зварити два алхімічні розчини замість одного, якщо успішно виконаєте <LSTag Tooltip=\"AbilityCheck\">перевірку</LSTag> Медицини з <LSTag Tooltip=\"DifficultyClass\">МС</LSTag> 15.",
    "Thanks to your connection to the fey realm, you gain proficiency in two of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"Deception\">Deception</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Intimidation</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Performance</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>.":
        "Завдяки зв’язку із царством фей ви отримуєте спеціалізацію у двох навичках на свій вибір: <LSTag Type=\"Skills\" Tooltip=\"Deception\">Обман</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Залякування</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Артистичність</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag>.",
    "If you have Heroic Inspiration, you can expend it to reroll any die immediately after rolling it.":
        "Маючи Героїчне натхнення, ви можете витратити його, щоб негайно перекинути будь-яку щойно кинуту кістку.",
    "Scroll of Faerie Fire": "Сувій Чарівного посвіту",
    "Once on each of your turns when you hit a creature with an attack roll using a weapon, you can cause the target to take an extra [1]":
        "Один раз протягом кожного свого ходу, коли ви влучаєте в істоту атакою зброєю, то можете додатково завдати цілі [1]",
    "Once on each of your turns when you hit a creature with an attack roll using a weapon, you can cause the target to take an extra 1d8 Necrotic.":
        "Один раз протягом кожного свого ходу, коли ви влучаєте в істоту атакою зброєю, то можете додатково завдати цілі 1d8 некротичної шкоди.",
    "During your turn, your reach is 10 feet greater with any Melee weapon that has the Heavy or Versatile property, as tendrils of the World Tree extend from you. When you hit with such a weapon on your turn, you can activate the <LSTag Type=\"Passive\" Tooltip=\"WeaponMasteryPush\">Push</LSTag> or Topple mastery property in addition to a different mastery property you’re using with that weapon.":
        "Протягом вашого ходу відростки Світового дерева збільшують на 10 футів досяжність зброї ближнього бою з властивістю «Важка» або «Універсальна». Влучивши такою зброєю у свій хід, ви можете застосувати властивість майстерності <LSTag Type=\"Passive\" Tooltip=\"WeaponMasteryPush\">«Поштовх»</LSTag> або «Повалення» на додачу до іншої властивості майстерності цієї зброї.",
    "When you hit with a ranged attack roll using a weapon that has the Thrown property, you gain a +2 bonus to the damage roll.":
        "Коли ви влучаєте дальньою атакою зброєю з властивістю «Метальна», то отримуєте бонус +2 до кидка шкоди.",
    "When you hit a creature with an attack roll, you can attempt to fluster the target. The target must succeed on a Wisdom saving throw or have Disadvantage on saving throws until the end of your next turn.":
        "Коли ви влучаєте атакою в істоту, то можете спробувати збентежити її. Ціль має успішно виконати кидок протидії мудрістю, інакше матиме заваду в кидках протидії до кінця вашого наступного ходу.",
    "You have Advantage on Attack Rolls against Large or larger creatures. In addition, you deal additional damage equal to your Strength modifier when you hit such creatures.":
        "Ви маєте перевагу в атаках проти істот великого чи більшого розміру. Крім того, влучаючи в таку істоту, ви завдаєте додаткової шкоди в кількості, що дорівнює вашому модифікатору сили.",
    "When you hit a creature with a melee weapon attack, you can move without provoking opportunity attacks.":
        "Коли ви влучаєте в істоту атакою зброєю ближнього бою, то можете рухатися, не провокуючи принагідних атак.",
    "Deal additional Acid damage equal to your <LSTag Tooltip=\"ProficiencyBonus\">Proficiency Bonus</LSTag>. On a hit, create a pool of acid around the target which reduces <LSTag Tooltip=\"ArmourClass\">Armour Class</LSTag> by [1].":
        "Завдайте додаткової шкоди кислотою в кількості, що дорівнює вашому <LSTag Tooltip=\"ProficiencyBonus\">бонусу спеціалізації</LSTag>. У разі влучання довкола цілі утворюється калюжа кислоти, яка зменшує <LSTag Tooltip=\"ArmourClass\">РЗ</LSTag> на [1].",
    "Attacks made by the invoked weapon deal an extra 1d8 Fire damage on a hit.":
        "У разі влучання атаки прикликаною зброєю додатково завдають 1d8 вогняної шкоди.",
    "The weapon emits bright light in a 30-foot radius and dim light for an additional 30 feet. In addition, weapon attacks made with it deal an extra 2d8 radiant damage on a hit. If the weapon isn’t already a magic weapon, it becomes one for the duration.":
        "Зброя випромінює яскраве світло в радіусі 30 футів і тьмяне світло ще на 30 футів. У разі влучання атаки нею додатково завдають 2d8 променевої шкоди. Якщо зброя ще не магічна, то стає магічною на час дії ефекту.",
    "When you are not in combat, you can spend 1 minute grooming and caring for your mount, at the end of which it gains a number of Temporary Hit Points equal to twice your Rogue level.":
        "Поза боєм ви можете витратити 1 хвилину на догляд за своїм скакуном. Після цього він отримує тимчасові очки здоров’я в кількості, що вдвічі перевищує ваш рівень пройдисвіта.",
    "When a creature you can see damages you or an ally within 30 feet of you, you can expend a seal as a reaction to reduce the damage taken by the target by an amount equal to 1d10 + half of your illrigger level (rounded down).":
        "Коли видима істота завдає шкоди вам або союзнику в межах 30 футів від вас, ви можете реагуванням витратити печатку й зменшити цю шкоду на 1d10 + половина вашого рівня ілріґера (з округленням униз).",
    "Requires Illrigger level 7 or higher.\n\nYou can expend a seal as a bonus action to teleport up to 30 feet to an unoccupied space you can see.":
        "Потребує 7-го або вищого рівня ілріґера.\n\nВторинною дією ви можете витратити печатку й телепортуватися на відстань до 30 футів у видиме вільне місце.",
    "Requires Illrigger level 7 or higher.\n\nWhen a creature makes a ranged attack against you or an ally you can see within 30 feet of you, you can expend a seal as a reaction to make a ranged weapon attack against the attacker. If your attack hits, it deals extra damage equal to half your illrigger level (rounded down).":
        "Потребує 7-го або вищого рівня ілріґера.\n\nКоли істота виконує дальню атаку проти вас або видимого союзника в межах 30 футів, ви можете реагуванням витратити печатку й атакувати нападника далекобійною зброєю. У разі влучання атака додатково завдає шкоди в кількості, що дорівнює половині вашого рівня ілріґера (з округленням униз).",
    "When a creature makes a ranged attack against you or an ally you can see within 30 feet of you, you can expend a seal as a reaction to make a ranged weapon attack against the attacker. If your attack hits, it deals extra damage equal to half your illrigger level (rounded down).":
        "Коли істота виконує дальню атаку проти вас або видимого союзника в межах 30 футів, ви можете реагуванням витратити печатку й атакувати нападника далекобійною зброєю. У разі влучання атака додатково завдає шкоди в кількості, що дорівнює половині вашого рівня ілріґера (з округленням униз).",
    "Once per Short Rest, you regain a Seal of Illrigger when you kill a creature with the True Name.":
        "Один раз за короткий відпочинок, коли ви вбиваєте істоту з Істинним ім’ям, то відновлюєте одну Печатку ілріґера.",
})

EXACT_OVERRIDES.update({
    "The ward is represented by a number of d8s equal to the number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice.":
        "Запас оберега містить по одній d8 за кожне очко чародійства, витрачене на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.",
    "When Dispater accepts you as his illrigger, you gain proficiency with heavy armor.":
        "Коли Диспатер приймає вас своїм ілріґером, ви отримуєте вишкіл із важкими обладунками.",
})

EXACT_OVERRIDES.update({
    "Scroll of Cloak of Shadow": "Сувій Плаща тіні",
    "Scroll of Spellfire Flare": "Сувій Чаровогняного спалаху",
    "Scroll of Wardaway": "Сувій Відгону",
    "Scroll of Aganazzar's Scorcher": "Сувій Пекучого струменя Аґанаццара",
    "Scroll of Darkbolt": "Сувій Темної стріли",
    "Scroll of Dazing Blast": "Сувій Ошелешливого вибуху",
    "Scroll of Death Armor": "Сувій Смертельних обладунків",
    "Scroll of Elminster's Elusion": "Сувій Вислизу Ельмінстера",
    "Scroll of Find Steed": "Сувій закляття «Знайти скакуна»",
    "Scroll of Fire Rune": "Сувій Вогняної руни",
    "Scroll of Searing Orb": "Сувій Пекучої кулі",
    "Scroll of Snilloc's Snowball Swarm": "Сувій Сніжкового рою Снілока",
    "Scroll of Tasha's Mind Whip": "Сувій Батога розуму Таші",
    "Scroll of Astral Flood": "Сувій Астрального потопу",
    "Scroll of Murmurs of Doom": "Сувій Шепоту приречення",
    "Scroll of Tidal Wave": "Сувій Припливної хвилі",
    "Scroll of Trollblood Infusion": "Сувій Вливання тролячої крові",
    "Scroll of Void Strike": "Сувій Удару порожнечі",
    "Scroll of Fount of Moonlight": "Сувій Джерела місячного сяйва",
    "Scroll of Spellfire Storm": "Сувій Чаровогняної бурі",
    "Scroll of Steel Wind Strike": "Сувій Удару сталевого вітру",
    "Scroll of Tide of Darkness": "Сувій Припливу темряви",
    "Scroll of Ballistic Smite": "Сувій Балістичної кари",
    "Scroll of Spectral Slash": "Сувій Примарного розтину",
    "Scroll of Thorn Armor": "Сувій Тернових обладунків",
    "Scroll of Umbral Tendril": "Сувій Тіньового щупальця",
    "Scroll of Laeral's Silver Lance": "Сувій Срібного списа Лаераля",
    "Scroll of Dream": "Сувій Сну",
    "Scroll of Enervation": "Сувій Виснаження",
    "Scroll of Circle of Power": "Сувій Кола сили",
    "Scroll of Finger Guns": "Сувій Пальців-пістолетів",
    "Scroll of Frightful Start": "Сувій Жахливого початку",
    "Scroll of Holy Word": "Сувій Святого слова",
    "Scroll of Mind Sliver": "Сувій Скалки розуму",
    "Scroll of Sword Burst": "Сувій Вибуху меча",
    "Scroll of Phantom Steed": "Сувій Примарного скакуна",
    "Scroll of Sorcerous Burst": "Сувій Чародійського спалаху",
    "Scroll of Holy Weapon": "Сувій Святої зброї",
    "Scroll of Rime's Binding Ice": "Сувій Сковувального льоду Райма",
    "Scroll of Blood Bolt": "Сувій Кривавого заряду",
    "Scroll of Summon Dragon": "Сувій Викликання дракона",
    "The Shadow Domain grants the following spells as you gain Cleric levels: Bane, False Life, <LSTag Type=\"Spell\" Tooltip=\"Target_Blindness\">Blindness</LSTag>, and Darkness at 3rd level; Blink and Fear at 5th level; Black Tentacles and <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Greater Invisibility</LSTag> at 7th level; and Cone of Cold and Dream at 9th level.":
        "Тіньовий домен надає такі закляття: на 3-му рівні клірика — «Бейн», «Удаване життя», <LSTag Type=\"Spell\" Tooltip=\"Target_Blindness\">«Сліпота»</LSTag> та «Пітьма»; на 5-му — «Миготіння» й «Страх»; на 7-му — «Чорні мацаки» та <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">«Велика невидимість»</LSTag>; на 9-му — «Конус холоду» й «Сон».",
    "When you reach certain Cleric levels, you always have the following spells prepared: Faerie Fire, Sleep, Moonbeam, and See Invisibility at level 3; Aura of Vitality and Void Strike at level 5; Freedom of Movement and <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Greater Invisibility</LSTag> at level 7; and Circle of Power and Dawn at level 9. These spells don't count against the number of spells you can prepare.":
        "На певних рівнях клірика ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — «Чарівний посвіт», «Сон», «Місячний промінь» і «Бачення невидимого»; на 5-му — «Аура життєвості» та «Удар порожнечі»; на 7-му — «Свобода руху» й <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">«Велика невидимість»</LSTag>; на 9-му — «Коло сили» та «Світанок». Ці закляття не враховуються до кількості заклять, які ви можете підготувати.",
})

EXACT_OVERRIDES.update({
    "Mind Sliver": "Скалка розуму",
    "True Strike (Melee)": "Певний удар (ближній бій)",
    "True Strike (Ranged)": "Певний удар (дальній бій)",
    "Magic Initiate: Prestidigitation": "Магічний хист: Фокуси",
    "Magic Initiate: Sword Burst": "Магічний хист: Вибух меча",
    "Magic Initiate: Frightful Start": "Магічний хист: Жахливий початок",
    "Magic Initiate: Cloak of Shadow": "Магічний хист: Плащ тіні",
    "Magic Initiate: Wardaway": "Магічний хист: Відгін",
    "Magic Initiate: Tide of Darkness": "Магічний хист: Приплив темряви",
    "Magic Initiate: Sorcerous Burst": "Магічний хист: Чародійський спалах",
    "Shadow Touched: Cloak of Shadow": "Торкнутий тінню: Плащ тіні",
    "Shadow Touched: Hungering Blade": "Торкнутий тінню: Голодний клинок",
    "Shadow Magic: Hungering Blade": "Тіньова магія: Голодний клинок",
    "Spellfire Storm: Spell Disruption": "Чаровогняна буря: зрив закляття",
    "Spellfire Storm: Radiant Damage": "Чаровогняна буря: променева шкода",
    "Hungering Blade: Temporary Hit Points": "Голодний клинок: тимчасові очки здоров’я",
    "Spectral Slash Target": "Ціль Примарного розтину",
    "Spectral Slash Attack": "Атака Примарного розтину",
    "Circle of Power Aura": "Аура Кола сили",
    "Cloud’s Jaunt (Cloud Giant). As a Bonus Action, you magically teleport up to 30 feet to an unoccupied space you can see.":
        "Хмарна мандрівка (хмарний велетень). Вторинною дією ви магічно телепортуєтеся на відстань до 30 футів у видиме вільне місце.",
    "Guiding Whispers. You know the Guidance cantrip. It has a range of 60 feet when you cast it.":
        "Спрямувальний шепіт. Ви знаєте замовляння «Направляння». Коли ви його проказуєте, дальність становить 60 футів.",
    "Wrathful Smite at 3rd level, Death Armor at 5th level, and Phantom Steed at 9th level.":
        "На 3-му рівні — «Гнівна кара», на 5-му — «Смертельні обладунки», а на 9-му — «Примарний скакун».",
    "When you reach a Ranger level specified in the Hollow Warden Spells table, you thereafter always have the listed spell prepared. Wrathful Smite at 3rd level, Death Armor at 5th level, and Phantom Steed at 9th level.":
        "На рівнях слідопита, указаних у таблиці «Закляття Порожнього вартового», ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — «Гнівна кара», на 5-му — «Смертельні обладунки», а на 9-му — «Примарний скакун».",
})

UID_OVERRIDES.update({
    "h5844527eg5bc7g6d08gb8bdg836fe861ad65":
        "Підмінки з їхньою мінливою зовнішністю непомітно живуть у багатьох суспільствах. Кожен підмінок може надприродно набувати будь-якого бажаного обличчя, а для декого нове обличчя відкриває нову грань душі.\n\nПерші підмінки мультивсесвіту з’явилися у Феєлоні. Дивовижна мінлива сутність цього плану й досі живе в них — навіть у тих, хто ніколи не ступав до царства фей.\n\nУ справжній подобі підмінки мають блідий вигляд і майже позбавлені виразних рис. Побачити їх такими випадає рідко, адже звичайний підмінок змінює подобу так само легко, як інші змінюють одяг. Проте багато підмінків створюють глибокі особистості з власною історією та переконаннями для кожної подоби. Підмінок-мандрівник може мати окремі особистості для переговорів, розслідувань і бою.\n\nКілька підмінків можуть поділяти одну особистість. Такі особистості навіть передаються в родині, даючи молодшому підмінкові змогу скористатися зв’язками, які налагодили її попередні носії.",
    "h00779e8dg1144g5eecg3f98g33292e8dea42":
        "Підмінки з їхньою мінливою зовнішністю непомітно живуть у багатьох суспільствах. Кожен підмінок може надприродно набувати будь-якого бажаного обличчя, а для декого нове обличчя відкриває нову грань душі.\n\nПерші підмінки мультивсесвіту з’явилися у Феєлоні. Дивовижна мінлива сутність цього плану й досі живе в них — навіть у тих, хто ніколи не ступав до царства фей.\n\nУ справжній подобі підмінки мають блідий вигляд і майже позбавлені виразних рис. Побачити їх такими випадає рідко, адже звичайний підмінок змінює подобу так само легко, як інші змінюють одяг. Проте багато підмінків створюють глибокі особистості з власною історією та переконаннями для кожної подоби. Підмінок-мандрівник може мати окремі особистості для переговорів, розслідувань і бою.\n\nКілька підмінків можуть поділяти одну особистість. Такі особистості навіть передаються в родині, даючи молодшому підмінкові змогу скористатися зв’язками, які налагодили її попередні носії.",
    "hc0cff11age80fgb13fgfd62g598157b9f427":
        "Важкі ударні загони Диспатера мають уміло командувати на полі бою й швидко знищувати ворогів. Знеболювачі дотримуються засад, які велять їм вести пекельні війська та воювати проти Добра крізь усі епохи.\n\nПопереду війська. Я йду в авангарді кожної битви, надихаючи своїх воїнів і жахаючи ворогів.\n\nКомандир. Де б я не був, командую я. Я не виконую наказів тих, кому бракує волі вести за собою.\n\nПеремога за будь-яку ціну. Я поважаю ворожого ватажка й ставлюся до нього гідно. Та коли мечі оголено, я застосовую все, що маю, аби перемогти, й очікую від нього того самого.\n\nСолдати гинуть. Життя моїх солдатів мене не турбують: це ресурси, які я витрачаю заради перемоги.",
    "h3c31b801g72c4g4016g8dbagc376fb17c919":
        "Вступаючи до Ордену Спустошення, Архітектори руїни присягають Асмодеєві. Ці засади велять їм нищити його ворогів могутньою магією, страхом і недовірою.\n\nПоле битви розуму. Коли мої війська зустрінуться з твоїми, тебе вже сповнюватиме жах і сумнів у власній силі. Мені не доведеться й пальцем ворухнути, щоб здолати тебе.\n\nНалежна таємниця. Дізнавшись твої таємниці, я пізнаю твою слабкість.\n\nЗнання — сила. Знання не менш могутнє за сталь. Я вивчаю кожну подробицю про ворога й передбачаю кожен його рух, ставлячи мат іще до початку гри.\n\nМагія кориться мені. Хитрість не менш могутня за сталь. Темними магічними мистецтвами я затьмарюю твої чуття, послаблюю волю та зміцнюю свій клинок. Твої солдати тремтітимуть, не знаючи, яка темна магія наступною огорне мою зброю.",
})

# The shipped Ukrainian BG3 text for these reused rows contains clear
# grammatical calques, so the corrected wording intentionally wins by handle.
UID_OVERRIDES.update({
    "h5d57e46bg1ebeg7a15g45a1g5dee2e76459e":
        "Запас оберега містить по одній d8 за кожне очко чародійства, витрачене на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.",
    "h3e1aea80g4740gaa01gfe95g3cd0d19d1bdd":
        "Запас оберега містить по одній d8 за кожне очко чародійства, витрачене на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.",
    "h2ee98c20g6713gb372g573dgca45f15d691f":
        "Запас оберега містить по одній d8 за кожне очко чародійства, витрачене на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.",
    "hbbfab3begf9cdg6052g4ac5g7eaf747c1f9a":
        "Запас оберега містить по одній d8 за кожне очко чародійства, витрачене на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.",
    "h063372f4g1033g08f6g55abgb32a96fe2615":
        "Запас оберега містить по одній d8 за кожне очко чародійства, витрачене на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити шкоду на суму результатів.",
    "ha5a58153g6cc6g4715g75c2ge276ca741c83":
        "Проклята істота зазнає додаткової шкоди від ваших атак і має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> вибраної вами <LSTag Tooltip=\"Ability\">характеристики</LSTag>.",
    "hfda85d46g3626g88f8gecffg03e1abc1eb12":
        "Проклята істота зазнає додаткової шкоди від ваших атак і має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> вибраної вами <LSTag Tooltip=\"Ability\">характеристики</LSTag>.",
})

EXACT_OVERRIDES.update({
    "Can’t take a reaction until the end of its next turn. Moreover, on its next turn, it must choose whether it gets an action, or a bonus action; it gets only one of two.":
        "Не може застосовувати реагування до кінця свого наступного ходу. Крім того, наступного ходу мусить вибрати між дією та вторинною дією — виконати можна лише одну з них.",
    "Your connection to the plane of absolute order allows you to equalize chaotic moments. When a creature you can see within 60 feet of yourself is about to roll a d20 with Advantage or Disadvantage, you can take a Reaction to prevent the roll from being affected by Advantage and Disadvantage.":
        "Ваш зв’язок із планом абсолютного порядку дає змогу врівноважувати миті хаосу. Коли істота, яку ви бачите в межах 60 футів, збирається кинути d20 із перевагою чи завадою, ви можете реагуванням скасувати вплив переваги й завади на цей кидок.",
    "Each of your attacks in a Wild Shape form can deal its normal damage type or Radiant damage. You make this choice each time you hit with those attacks.":
        "Кожна ваша атака в Дикій подобі може завдавати шкоди звичайного типу або променевої шкоди. Ви вибираєте тип щоразу, коли влучаєте такою атакою.",
    "As a Magic action, you touch a creature and roll a number of d4s equal to your Proficiency Bonus. The creature regains a number of Hit Points equal to the total rolled. Once you use this trait, you can’t use it again until you finish a Long Rest.":
        "Магічною дією ви торкаєтеся істоти й кидаєте стільки d4, скільки становить ваш бонус спеціалізації. Істота відновлює очки здоров’я в кількості, що дорівнює сумі результатів. Скориставшись цією рисою, ви не зможете застосувати її знову до завершення тривалого відпочинку.",
    "You gain proficiency in Intelligence saving throws.\n\nAdd half of your Wisdom Modifier to <LSTag Tooltip=\"AbilityCheck\">Ability Checks</LSTag> that you are not <LSTag Tooltip=\"Proficiency\">Proficient</LSTag> in.":
        "Ви отримуєте спеціалізацію в кидках протидії інтелектом.\n\nДодавайте половину свого модифікатора мудрості до <LSTag Tooltip=\"AbilityCheck\">перевірок характеристик</LSTag>, у яких ви не маєте <LSTag Tooltip=\"Proficiency\">спеціалізації</LSTag>.",
    "Magician. You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature gives you a bonus to your Intelligence (<LSTag Type=\"Skills\" Tooltip=\"Arcana\">Arcana</LSTag> or <LSTag Type=\"Skills\" Tooltip=\"Nature\">Nature</LSTag>) checks. The bonus equals your Wisdom modifier (minimum bonus of +1).":
        "Маг. Ви знаєте одне додаткове замовляння зі списку заклять друїда. Крім того, містичний зв’язок із природою дає вам бонус до перевірок інтелекту (<LSTag Type=\"Skills\" Tooltip=\"Arcana\">Таїнства</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Nature\">Природа</LSTag>) у кількості, що дорівнює вашому модифікатору мудрості (щонайменше +1).",
    "Warlock cantrips that require an attack roll: when you hit a Large or smaller creature with such a cantrip, you can push the creature up to [1] directly away from you.":
        "Коли ви влучаєте замовлянням чаклуна, яке потребує кидка атаки, в істоту великого або меншого розміру, то можете відштовхнути її від себе на відстань до [1].",
    "You’ve developed cunning ways to use your Sneak Attack. When you deal Sneak Attack damage, you can add one of the following Cunning Strike effects.\n\nIf a Cunning Strike effect requires a saving throw, the DC equals 8 plus your Dexterity modifier and Proficiency Bonus.":
        "Ви опанували хитромудрі способи застосування Підступного удару. Завдаючи ним шкоди, ви можете додати один із наведених нижче ефектів Хитрого удару.\n\nЯкщо ефект Хитрого удару потребує кидка протидії, його МС дорівнює 8 + ваш модифікатор спритності + ваш бонус спеціалізації.",
    "If you fail an Intelligence, a Wisdom, or a Charisma saving throw, you can cause yourself to succeed instead. Once you use this benefit, you can’t use it again until you finish a Short or Long Rest.":
        "Коли ви провалюєте кидок протидії інтелектом, мудрістю чи харизмою, то можете натомість зробити його успішним. Скориставшись цією перевагою, ви не зможете застосувати її знову до завершення короткого чи тривалого відпочинку.",
    "While your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is active, the first creature you hit on each of your turns with a weapon or an Unarmed Strike takes extra Radiant damage equal to 1d6 plus half your Barbarian level (rounded down).":
        "Поки діє ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, перша істота, у яку ви влучаєте зброєю чи ударом голіруч протягом кожного свого ходу, додатково зазнає 1d6 + половина вашого рівня варвара (з округленням униз) променевої шкоди.",
    "While your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is active, the first creature you hit on each of your turns with a weapon or an Unarmed Strike takes extra Necrotic damage equal to 1d6 plus half your Barbarian level (rounded down).":
        "Поки діє ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, перша істота, у яку ви влучаєте зброєю чи ударом голіруч протягом кожного свого ходу, додатково зазнає 1d6 + половина вашого рівня варвара (з округленням униз) некротичної шкоди.",
})

EXACT_OVERRIDES.update({
    """Air. The damage type is Thunder. Each creature that fails the saving throw is pushed 10 feet away from you.

Coldfire. The damage type is Cold. Each creature that fails the saving throw has the Frightened condition until the start of your next turn.

Earth. The damage type is Bludgeoning. Each creature that fails the saving throw has its Speed reduced to 0 until the end of its next turn.

Fire. The damage type is Fire. Each creature that fails the saving throw is engulfed in flames and takes Fire damage at the end of its next turn. As an action, it can extinguish fire on itself by giving itself the Prone condition and rolling on the ground. The fire also goes out if it is doused, submerged, or suffocated.

Water. The damage type is Acid. Each creature that fails the saving throw has the Prone condition.

Each creature within a 30-foot Cone of destructive elemental energy must make a Dexterity saving throw. On a failed save, a target takes damage of the chosen type. On a successful save, the target takes half as much damage only.""":
        """Повітря. Тип шкоди — громова. Кожну істоту, що провалила кидок протидії, відштовхує від вас на 10 футів.

Морозне полум’я. Тип шкоди — холодова. Кожна істота, що провалила кидок протидії, набуває стану переляку до початку вашого наступного ходу.

Земля. Тип шкоди — дробильна. Швидкість кожної істоти, що провалила кидок протидії, знижується до 0 до кінця її наступного ходу.

Вогонь. Тип шкоди — вогняна. Кожну істоту, що провалила кидок протидії, охоплює полум’я, і наприкінці свого наступного ходу вона зазнає вогняної шкоди. Дією істота може загасити полум’я на собі, набувши стану повалення й качаючись по землі. Вогонь також гасне, якщо його облити, занурити чи перекрити доступ повітря.

Вода. Тип шкоди — кислотна. Кожна істота, що провалила кидок протидії, набуває стану повалення.

Кожна істота в 30-футовому конусі руйнівної стихійної енергії повинна виконати кидок протидії спритністю. У разі невдачі ціль зазнає шкоди вибраного типу, а в разі успіху — лише половину.""",
    """You gain the ability to create an orb of light that erupts into a devastating explosion. As an action, you magically create an orb and hurl it at a point you choose within 150 feet, where it erupts into a sphere of radiant light for a brief but deadly instant.

Each creature in that 20-foot-radius sphere must succeed on a Constitution saving throw or take 2d6 radiant damage. A creature doesn’t need to make the save if the creature is behind total cover that is opaque.

You can increase the sphere’s damage by spending ki points. Each point you spend, to a maximum of 3, increases the damage by 2d6.""":
        """Ви навчаєтеся створювати сферу світла, що вибухає руйнівним спалахом. Дією ви магічно створюєте сферу й метаєте її у вибрану точку в межах 150 футів, де вона на коротку, але смертоносну мить вибухає сферою променевого світла.

Кожна істота у цій сфері радіусом 20 футів повинна успішно виконати кидок протидії статурою, інакше зазнає 2d6 променевої шкоди. Істоті не потрібно виконувати кидок, якщо вона перебуває за повним непрозорим укриттям.

Ви можете збільшити шкоду сфери, витрачаючи очки кі. Кожне витрачене очко, щонайбільше 3, збільшує шкоду на 2d6.""",
})

EXACT_OVERRIDES.update({
    """As a bonus action, you can cause a melee weapon you are wielding to emit dim light in a 10-foot radius for 10 turns. The light is sunlight. While the weapon gleams, it deals radiant damage instead of its normal damage type.

When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it.""":
        """Вторинною дією ви можете змусити зброю ближнього бою, яку тримаєте, випромінювати тьмяне сонячне світло в радіусі 10 футів протягом 10 ходів. Поки зброя сяє, вона завдає променевої шкоди замість шкоди звичайного типу.

Коли ви завдаєте критичного влучання атакою зброєю ближнього бою, ви можете ще раз кинути одну з кісток шкоди зброї й додати результат.""",
    """As an action, you invoke the authority of Dispater. You make a weapon attack and choose a number of willing creatures up to your proficiency bonus who you can see within 30 feet of you. Each creature you choose can use a reaction to make a weapon attack or cast a damage-dealing cantrip with a casting time of 1 action.

Once you use this action, you can’t use it again until you finish a short or long rest.""":
        """Дією ви закликаєте владу Диспатера. Виконайте атаку зброєю й виберіть видимих вам охочих істот у межах 30 футів у кількості, що не перевищує вашого бонусу спеціалізації. Кожна вибрана істота може застосувати реагування, щоб атакувати зброєю або проказати замовляння, що завдає шкоди й має час проказування 1 дія.

Застосувавши цю дію, ви не зможете зробити це знову до завершення короткого або довгого відпочинку.""",
    "You can burst into a mist of raw shadow and then reassemble yourself somewhere else. As an action, you magically teleport, along with any equipment you are wearing or carrying, up to 30 feet to an unoccupied and obscured space you can see. Before or after teleporting, you can make one attack.":
        "Ви можете розчинитися в тумані сирої тіні, а потім зібратися в іншому місці. Дією ви магічно телепортуєтеся разом з усім спорядженням, яке носите або тримаєте, на відстань до 30 футів у видимий вам вільний і затінений простір. До або після телепортації ви можете виконати одну атаку.",
    "Whenever a target cursed by your Hex drops to 0 Hit Points, you regain Hit Points equal to 1d8 plus your Charisma modifier.":
        "Щоразу, коли очки здоров’я цілі під дією вашого «Прокляття» знижуються до 0, ви відновлюєте 1d8 + ваш модифікатор харизми очок здоров’я.",
})

EXACT_OVERRIDES.update({
    """Instrument Training. You gain proficiency with three Musical Instruments.

Encouraging Song. As you finish a Short or Long Rest, you can play a song on a Musical Instrument with which you have proficiency and give Bardic Inspiration to allies who hear the song. The number of allies you can affect in this way equals your Proficiency Bonus.""":
        """Навчання гри на інструментах. Ви отримуєте володіння трьома музичними інструментами.

Підбадьорлива пісня. Завершивши короткий або довгий відпочинок, ви можете зіграти пісню на музичному інструменті, яким володієте, і дати Бардівське натхнення союзникам, які її чують. Кількість союзників, яких ви можете надихнути таким чином, дорівнює вашому бонусу спеціалізації.""",
    """While you aren’t wearing armor or wielding a Shield, you gain the following benefits.

Dance Virtuoso. You have Advantage on any Charisma (<LSTag Type="Skills" Tooltip="Performance">Performance</LSTag>) check you make that involves you dancing.

Unarmored Defense. Your base Armor Class equals 10 plus your Dexterity and Charisma modifiers.

Agile Strikes. When you expend a use of your Bardic Inspiration as part of an action, a Bonus Action, or a Reaction, you can make one Unarmed Strike as part of that action, Bonus Action, or Reaction.

Bardic Damage. You can use Dexterity instead of Strength for the attack rolls of your Unarmed Strikes. When you deal damage with an Unarmed Strike, you can deal Bludgeoning damage equal to a roll of your Bardic Inspiration die plus your Dexterity modifier, instead of the strike’s normal damage. This roll doesn’t expend the die.""":
        """Поки ви не носите обладунків і не тримаєте щита, ви отримуєте такі переваги.

Віртуоз танцю. Ви маєте перевагу на будь-яку перевірку харизми (<LSTag Type="Skills" Tooltip="Performance">Артистичність</LSTag>), пов’язану з танцем.

Захист без обладунків. Ваш базовий РЗ дорівнює 10 + ваші модифікатори спритності та харизми.

Спритні удари. Коли ви витрачаєте одне застосування Бардівського натхнення як частину дії, вторинної дії чи реагування, ви можете виконати один Удар голіруч як частину тієї самої дії або реагування.

Бардівська шкода. Для кидків атаки Ударом голіруч ви можете використовувати спритність замість сили. Завдаючи шкоди Ударом голіруч, ви можете замінити звичайну шкоду удару на дробильну шкоду, що дорівнює результату кидка вашої кістки Бардівського натхнення + ваш модифікатор спритності. Цей кидок не витрачає кістку.""",
    "When you hit with your Unarmed Strike and deal damage, you can deal Bludgeoning damage equal to 1d6 plus your Strength modifier instead of the normal damage of an Unarmed Strike.":
        "Коли ви влучаєте Ударом голіруч і завдаєте шкоди, замість звичайної шкоди удару ви можете завдати дробильної шкоди в кількості 1d6 + ваш модифікатор сили.",
    """As a Bonus Action, you can expend a use of your Wild Shape to manifest a 5-foot Emanation that takes the form of ocean spray that surrounds you. It ends early if you dismiss it (no action required), manifest it again, or have the Incapacitated condition.

When you manifest the Emanation and as a Bonus Action on your subsequent turns, you can choose another creature you can see in the Emanation. The target must succeed on a Constitution saving throw against your spell save DC or take Cold damage and, if the creature is Large or smaller, be pushed up to 15 feet away from you. To determine this damage, roll a number of d6s equal to your Wisdom modifier.""":
        """Вторинною дією ви можете витратити одне застосування Дикої подоби, щоб створити довкола себе 5-футову еманацію у вигляді океанських бризок. Еманація завершується достроково, якщо ви припиняєте її (дія не потрібна), створюєте її знову або набуваєте стану недієздатності.

Коли ви створюєте еманацію, а також вторинною дією в кожен свій наступний хід, ви можете вибрати іншу видиму вам істоту в межах еманації. Ціль повинна успішно виконати кидок протидії статурою проти вашої МС протидії закляттям, інакше зазнає холодової шкоди та, якщо вона великого або меншого розміру, буде відштовхнута від вас на відстань до 15 футів. Щоб визначити шкоду, киньте стільки d6, скільки становить ваш модифікатор мудрості.""",
    """You can cast Misty Step as a Reaction in response to taking damage.

In addition, the following effects are now among your Steps of the Fey options.

Disappearing Step. You have the <LSTag Type="Status" Tooltip="INVISIBLE">Invisible</LSTag> condition until the start of your next turn or until immediately after you make an attack roll, deal damage, or cast a spell.

Dreadful Step. Creatures within 10 feet of the space you left or the space you appear in (your choice) must succeed on a Wisdom saving throw against your spell save DC or take 2d10 Psychic damage.""":
        """Зазнавши шкоди, ви можете проказати «Маревний крок» реагуванням.

Крім того, до варіантів вашого «Кроку фей» додаються такі ефекти.

Зникливий крок. Ви набуваєте стану <LSTag Type="Status" Tooltip="INVISIBLE">невидимості</LSTag> до початку свого наступного ходу або до миті одразу після того, як виконаєте кидок атаки, завдасте шкоди чи прокажете закляття.

Жахливий крок. Істоти в межах 10 футів від покинутого вами простору або простору, у якому ви з’явилися (на ваш вибір), повинні успішно виконати кидок протидії мудрістю проти вашої МС протидії закляттям, інакше зазнають 2d10 психічної шкоди.""",
    """Agility. You gain a bonus to your AC equal to your Intelligence modifier (minimum of +1), and your Speed increases by 10 feet. In addition, you have Advantage on Dexterity (<LSTag Type="Skills" Tooltip="Acrobatics">Acrobatics</LSTag>) checks.

Bladework. Whenever you attack with a weapon with which you have proficiency, you can use your Intelligence modifier for the attack and damage rolls instead of using Strength or Dexterity.

Focus. When you make a Constitution saving throw to maintain Concentration, you can add your Intelligence modifier to the total.""":
        """Спритність. Ви отримуєте бонус до РЗ, що дорівнює вашому модифікатору інтелекту (щонайменше +1), а ваша швидкість збільшується на 10 футів. Крім того, ви маєте перевагу на перевірки спритності (<LSTag Type="Skills" Tooltip="Acrobatics">Акробатика</LSTag>).

Майстерність клинка. Атакуючи зброєю, якою володієте, ви можете використовувати свій модифікатор інтелекту замість сили чи спритності для кидків атаки й шкоди.

Зосередження. Виконуючи кидок протидії статурою для підтримання концентрації, ви можете додати до результату свій модифікатор інтелекту.""",
    "Whenever you attack with a weapon with which you have proficiency, you can use your Intelligence modifier for the attack and damage rolls instead of using Strength or Dexterity.":
        "Атакуючи зброєю, якою володієте, ви можете використовувати свій модифікатор інтелекту замість сили чи спритності для кидків атаки й шкоди.",
    "When you cast Shillelagh, you can cause any Melee weapon you are holding to be imbued with nature’s power; you can choose for the weapon to retain its normal damage die instead of becoming a d8. In addition, you can use any weapon with which you have proficiency as a Spellcasting Focus for your Druid spells.":
        "Коли ви проказуєте «Ґирлиґу», ви можете наділити силою природи будь-яку зброю ближнього бою, яку тримаєте; ви можете залишити її звичайну кістку шкоди замість того, щоб замінити її на d8. Крім того, будь-яку зброю, якою володієте, ви можете використовувати як фокус проказування для своїх заклять друїда.",
    """Your combat training and your experiments with magic have paid off in two ways.

Arcane Empowerment. When you attack with a magic weapon, you can use your Intelligence modifier, instead of your Strength or Dexterity modifier, for the attack and damage rolls.
Weapon Knowledge. You gain proficiency with Martial weapons. You can use a weapon with which you have proficiency as a Spellcasting Focus for your Artificer spells.""":
        """Бойова підготовка й досліди з магією дають вам дві переваги.

Містичне посилення. Атакуючи магічною зброєю, ви можете використовувати свій модифікатор інтелекту замість модифікатора сили чи спритності для кидків атаки й шкоди.
Знання зброї. Ви отримуєте володіння бойовою зброєю. Зброю, якою володієте, ви можете використовувати як фокус проказування для своїх заклять винахідника.""",
    """Heavenly Wings. Two spectral wings sprout from your back temporarily. Until the transformation ends, you have a Fly Speed equal to your Speed.

Inner Radiance. Searing light temporarily radiates from your eyes and mouth. For the duration, you shed Bright Light in a 10-foot radius and Dim Light for an additional 10 feet, and at the end of each of your turns, each creature within 10 feet of you takes Radiant damage equal to your Proficiency Bonus.

Necrotic Shroud. Your eyes briefly become pools of darkness, and flightless wings sprout from your back temporarily. Creatures other than your allies within 10 feet of you must succeed on a Charisma saving throw (DC 8 plus your Charisma modifier and Proficiency Bonus) or have the Frightened condition until the end of your next turn.""":
        """Небесні крила. З вашої спини на деякий час виростають два примарні крила. До завершення перетворення ваша швидкість польоту дорівнює звичайній швидкості.

Внутрішнє сяйво. З ваших очей і рота на деякий час струменить палюче світло. Ви випромінюєте яскраве світло в радіусі 10 футів і тьмяне світло ще на 10 футів. Наприкінці кожного вашого ходу всі істоти в межах 10 футів зазнають променевої шкоди в кількості, що дорівнює вашому бонусу спеціалізації.

Некротичний покров. Ваші очі на мить стають безоднями темряви, а зі спини виростають непридатні до польоту крила. Істоти в межах 10 футів, окрім ваших союзників, повинні успішно виконати кидок протидії харизмою з МС 8 + ваш модифікатор харизми + ваш бонус спеціалізації, інакше набувають стану переляку до кінця вашого наступного ходу.""",
    """Heroic Soul. At the start of each of your turns, you can spend 1 Sorcery Point to gain Temporary Hit Points equal to 1d6 plus your Sorcerer level (no action required).

Innate Bladework. Whenever you attack with a weapon with which you have proficiency while your Innate Sorcery feature is active, you can use your Charisma modifier for the attack and damage rolls instead of using Strength or Dexterity.

Martial Training. You gain proficiency with Martial weapons and training with Light armor, Medium armor, and Shields.""":
        """Героїчна душа. На початку кожного свого ходу ви можете витратити 1 очко чародійства, щоб отримати 1d6 + ваш рівень чародія тимчасових очок здоров’я (дія не потрібна).

Вроджена майстерність клинка. Поки діє ваша особливість «Вроджене чаклунство», атакуючи зброєю, якою володієте, ви можете використовувати свій модифікатор харизми замість сили чи спритності для кидків атаки й шкоди.

Бойова підготовка. Ви отримуєте володіння бойовою зброєю та вміння носити легкі й середні обладунки і користуватися щитами.""",
    "Whenever you attack with a weapon with which you have proficiency while your Innate Sorcery feature is active, you can use your Charisma modifier for the attack and damage rolls instead of using Strength or Dexterity.":
        "Поки діє ваша особливість «Вроджене чаклунство», атакуючи зброєю, якою володієте, ви можете використовувати свій модифікатор харизми замість сили чи спритності для кидків атаки й шкоди.",
    "You have proficiency in the Insight, Perception, or Survival skill.":
        "Ви володієте однією з таких навичок: «Проникливість», «Відчуття» або «Виживання».",
})

EXACT_OVERRIDES.update({
    """You always have the Charm Person and Mirror Image spells prepared.

In addition, immediately after you cast an Enchantment or Illusion spell using a spell slot, you can cause a creature you can see within [1] of yourself to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the Charmed or Frightened condition (your choice) for 1 minute""":
        """Ви завжди маєте підготовленими закляття «Причарування особи» та «Віддзеркалення».

Крім того, одразу після проказування закляття школи зачарування чи ілюзії з використанням чарунки ви можете змусити видиму вам істоту в межах [1] виконати кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі ціль на 1 хвилину набуває стану причарування або переляку (на ваш вибір).""",
    "You can expend a use of your Channel Divinity to cast Shield of Faith or Spiritual Weapon rather than expending a spell slot. When you cast either spell in this way, the spell doesn’t require Concentration. Instead the spell lasts for 1 minute, but it ends early if you cast that spell again, have the Incapacitated condition, or die.":
        "Ви можете витратити одне застосування Божого наснаження, щоб проказати «Щит віри» або «Духовну зброю» замість витрачання чарунки. Проказане таким чином закляття не потребує концентрації та діє 1 хвилину, але завершується достроково, якщо ви прокажете його знову, набудете стану недієздатності або помрете.",
    "As a Magic action, you can expend one use of your Channel Divinity to manifest your magical knowledge. Choose one spell from the Knowledge Domain or the Divination school. As part of the same action, you cast the chosen spell without expending a spell slot.":
        "Магічною дією ви можете витратити одне застосування Божого наснаження, щоб утілити свої магічні знання. Виберіть одне закляття домену знань або школи віщування. Тією самою дією ви проказуєте вибране закляття, не витрачаючи чарунки.",
    "When you cast any level 1+ spell from your Psionic Spells feature, you can cast it by expending a spell slot as normal or by spending a number of Sorcery Points equal to the spell’s level. If you cast the spell using Sorcery Points, it requires no Verbal or Somatic components, and it requires no Material components unless they are consumed by the spell or have a cost specified in it.":
        "Коли ви проказуєте закляття рівня 1+ зі своєї особливості «Псіонічні закляття», то можете як зазвичай витратити чарунку або натомість витратити кількість очок чародійства, що дорівнює рівню закляття. Якщо ви проказуєте його за очки чародійства, воно не потребує словесного чи тілесного складника, а також матеріального складника, якщо тільки закляття не поглинає його або не вказує його вартість.",
    """You can manipulate chaos itself to give yourself Advantage on one D20 Test before you roll the d20. Once you do so, you must cast a Sorcerer spell with a spell slot or finish a Long Rest before you can use this feature again.

If you do cast a Sorcerer spell with a spell slot before you finish a Long Rest, you automatically roll on the Wild Magic Surge table.""":
        """Ви можете підкорити сам хаос, щоб отримати перевагу на одне випробування d20 до кидка d20. Після цього ви не зможете знову застосувати цю особливість, доки не прокажете закляття чародія з використанням чарунки або не завершите довгий відпочинок.

Якщо до завершення довгого відпочинку ви прокажете закляття чародія з використанням чарунки, то автоматично кидаєте за таблицею «Сплеск дикої магії».""",
    "Your spellcasting can unleash surges of untamed magic. Once per turn, you can roll 1d20 immediately after you cast a Sorcerer spell with a spell slot. If you roll a 20, roll on the Wild Magic Surge table to create a magical effect.":
        "Ваше проказування може вивільняти сплески неприборканої магії. Один раз за хід, одразу після проказування закляття чародія з використанням чарунки, ви можете кинути 1d20. Якщо випаде 20, киньте за таблицею «Сплеск дикої магії», щоб створити магічний ефект.",
    "When you use Smite spells, you gain <LSTag Tooltip=\"TemporaryHitPoints\">temporary hit points</LSTag> equal to your Charisma <LSTag Tooltip=\"AbilityModifier\">Modifier</LSTag>.":
        "Коли ви проказуєте закляття кари, то отримуєте <LSTag Tooltip=\"TemporaryHitPoints\">тимчасові очки здоров’я</LSTag> в кількості, що дорівнює вашому <LSTag Tooltip=\"AbilityModifier\">модифікатору</LSTag> харизми.",
    """When you roll fire damage for a spell you cast, you can reroll any 1 on the fire damage dice.

Whenever you cast a spell that deals fire damage, you can cause flames to wreathe you until the end of your next turn. While these flames are present, any creature that hits you with a melee attack takes 1d4 fire damage.""":
        """Кидаючи кістки вогняної шкоди проказаного вами закляття, ви можете перекинути кожну кістку, на якій випало 1.

Щоразу, коли ви проказуєте закляття, яке завдає вогняної шкоди, ви можете огорнутися полум’ям до кінця свого наступного ходу. Поки це полум’я палає, кожна істота, що влучає у вас атакою ближнього бою, зазнає 1d4 вогняної шкоди.""",
    "Whenever you cast a spell that deals fire damage, you can cause flames to wreathe you until the end of your next turn. While these flames are present, any creature that hits you with a melee attack takes 1d4 fire damage.":
        "Щоразу, коли ви проказуєте закляття, яке завдає вогняної шкоди, ви можете огорнутися полум’ям до кінця свого наступного ходу. Поки це полум’я палає, кожна істота, що влучає у вас атакою ближнього бою, зазнає 1d4 вогняної шкоди.",
    """The primal and ever-changing power of the moon flows through you, granting you the following benefits.

Inspired Eclipse. When you take a Bonus Action to give a creature a <LSTag Type="ActionResource" Tooltip="BardicInspiration">Bardic Inspiration</LSTag> die, you can have the <LSTag Type="Status" Tooltip="INVISIBLE">Invisible</LSTag> condition and teleport up to 30 feet to an unoccupied space you can see as part of that Bonus Action. This invisibility lasts until the start of your next turn and ends early immediately after you make an attack roll, deal damage, or cast a spell.

Lunar Vitality. Once per turn when you restore Hit Points to a creature with a spell, you can expend a Bardic Inspiration die and increase the amount of Hit Points restored by a number equal to a roll of the Bardic Inspiration die. The creature’s Speed also increases by 10 feet until the end of its next turn.""":
        """Крізь вас тече первісна й мінлива сила місяця, надаючи такі переваги.

Натхненне затемнення. Коли ви вторинною дією даєте істоті кістку <LSTag Type="ActionResource" Tooltip="BardicInspiration">Бардівського натхнення</LSTag>, то тією самою дією можете набути стану <LSTag Type="Status" Tooltip="INVISIBLE">невидимості</LSTag> й телепортуватися на відстань до 30 футів у видимий вам вільний простір. Невидимість триває до початку вашого наступного ходу й завершується достроково одразу після того, як ви виконаєте кидок атаки, завдасте шкоди чи прокажете закляття.

Місячна життєва сила. Один раз за хід, коли ви відновлюєте істоті очки здоров’я закляттям, ви можете витратити кістку Бардівського натхнення й збільшити кількість відновлених очок на результат її кидка. Швидкість істоти також збільшується на 10 футів до кінця її наступного ходу.""",
    "While in Dragon Shape, you can cast your prepared Druid spells, and your AC increases by 2.":
        "Перебуваючи в драконячій подобі, ви можете проказувати підготовлені закляття друїда, а ваш РЗ збільшується на 2.",
    "When you cast an illrigger spell you know, you can burn two seals on an interdicted creature (no action required) to impose disadvantage on their saving throw against the spell.":
        "Коли ви проказуєте відоме вам закляття ілріґера, то можете спалити дві печатки на істоті під забороною (дія не потрібна), щоб накласти заваду на її кидок протидії проти цього закляття.",
    "You can cast Illusion spells without providing Verbal components. In addition, when you cast an Illusion spell with a range of 10 feet or greater, its range increases by 50%. You can cast <LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Minor Illusion</LSTag> as a bonus action.":
        "Ви можете проказувати закляття ілюзії без словесного складника. Крім того, дальність закляття ілюзії з дальністю щонайменше 10 футів збільшується на 50%. <LSTag Type=\"Spell\" Tooltip=\"Target_ImprovedMinorIllusion\">Малу ілюзію</LSTag> ви можете проказувати вторинною дією.",
    "You can create and reach through brief holes in the fabric of reality. When you cast a spell that has a range of Touch, you can make the spell’s range 30 feet instead. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Ви можете створювати короткочасні отвори в тканині реальності й діяти крізь них. Коли ви проказуєте закляття з дальністю «Дотик», то можете змінити його дальність на 30 футів. Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "Whenever you cast a spell using your Alchemist’s Supplies as the Spellcasting Focus, you gain a bonus to one roll of the spell. That roll must restore Hit Points or be a damage roll that deals Acid, Fire, or Poison damage. The bonus equals your Intelligence modifier (minimum bonus of +1).":
        "Щоразу, коли ви проказуєте закляття, використовуючи приладдя алхіміка як фокус проказування, ви отримуєте бонус до одного кидка цього закляття. Це має бути кидок, що відновлює очки здоров’я або визначає кислотну, вогняну чи отруйну шкоду. Бонус дорівнює вашому модифікатору інтелекту (щонайменше +1).",
    "You can cast Lesser Restoration without expending a spell slot and without preparing the spell, provided you use Alchemist’s Supplies as the Spellcasting Focus. You can do so a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Ви можете проказувати «Мале відновлення», не витрачаючи чарунки й не готуючи закляття, якщо використовуєте приладдя алхіміка як фокус проказування. Кількість таких застосувань дорівнює вашому модифікатору інтелекту (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "You can use your Arcane Firearm as a Spellcasting Focus for your Artificer spells. When you cast an Artificer spell through the firearm, roll 1d8, and you gain a bonus to one of the spell’s damage rolls equal to the number rolled.":
        "Ви можете використовувати свою містичну вогнепальну зброю як фокус проказування для заклять винахідника. Коли ви проказуєте через неї закляття винахідника, киньте 1d8: ви отримуєте бонус до одного кидка шкоди цього закляття, що дорівнює результату кидка.",
})

EXACT_OVERRIDES.update({
    "During the first round of each combat, you have Advantage on attack rolls against any creature that hasn’t taken a turn. If your Sneak Attack hits any target during that round, the target takes extra damage of the weapon’s type equal to your Rogue level.":
        "У першому раунді кожного бою ви маєте перевагу на кидки атаки проти всіх істот, які ще не виконали свого ходу. Якщо в цьому раунді ви влучаєте в ціль Підступним ударом, вона додатково зазнає шкоди типу зброї в кількості, що дорівнює вашому рівню пройдисвіта.",
    """Your patron teaches you how to guard your mind and body. You are immune to the Charmed condition.

In addition, immediately after a creature you can see hits you with an attack roll, you can take a Reaction to reduce the damage you take by half (round down), and you can force the attacker to take Psychic damage equal to the damage you take.""":
        """Ваш покровитель навчає вас захищати розум і тіло. Ви маєте імунітет до стану причарування.

Крім того, одразу після того, як видима вам істота влучає у вас атакою, ви можете застосувати реагування, щоб удвічі зменшити отриману шкоду (з округленням униз) і змусити нападника зазнати психічної шкоди в кількості, що дорівнює отриманій вами шкоді.""",
    "Immediately after a creature you can see hits you with an attack roll, you can take a Reaction to reduce the damage you take by half (round down), and you can force the attacker to take Psychic damage equal to the damage you take.":
        "Одразу після того, як видима вам істота влучає у вас атакою, ви можете застосувати реагування, щоб удвічі зменшити отриману шкоду (з округленням униз) і змусити нападника зазнати психічної шкоди в кількості, що дорівнює отриманій вами шкоді.",
    "Immediately after you take damage, you can use a reaction to magically become invisible until the end of your next turn or until you attack, deal damage, or force someone to make a saving throw. Once you use this ability, you can’t do so again until you finish a short or long rest.":
        "Одразу після того, як ви зазнаєте шкоди, ви можете застосувати реагування, щоб магічно стати невидимим до кінця свого наступного ходу або доки не атакуєте, не завдасте шкоди чи не змусите когось виконати кидок протидії. Застосувавши цю здібність, ви не зможете зробити це знову до завершення короткого або довгого відпочинку.",
    """Biting Cold. Damage from your weapon attacks, Ranger spells, and Ranger features ignores Resistance to Cold damage.

Frost Resistance. You have Resistance to Cold damage.

Polar Strikes. When you hit a creature with an attack roll using a weapon, you can deal an extra 1d4 Cold damage to the target, which can take this extra damage only once per turn. When you reach Ranger level 11, this extra damage increases to 1d6.""":
        """Кусючий холод. Шкода від ваших атак зброєю, заклять і особливостей слідопита ігнорує стійкість до холодової шкоди.

Морозостійкість. Ви маєте стійкість до холодової шкоди.

Полярні удари. Коли ви влучаєте в істоту атакою зброєю, то можете завдати цілі додатково 1d4 холодової шкоди. Ціль може зазнати цієї додаткової шкоди лише один раз за хід. На 11-му рівні слідопита додаткова шкода збільшується до 1d6.""",
    "As your attack hits or misses the target, the weapon or ammunition transforms into a 5-foot-wide Line of magical energy that extends out to the weapon’s normal range. The Line includes the attack’s original target. Each creature within the Line makes a Dexterity saving throw, taking Force damage equal to the weapon’s normal damage on a failed save or half as much damage on a successful one.":
        "Незалежно від того, влучила атака чи промахнулася, зброя або боєприпас перетворюється на лінію магічної енергії завширшки 5 футів, що простягається на звичайну дальність зброї та охоплює початкову ціль атаки. Кожна істота в лінії виконує кидок протидії спритністю. У разі невдачі вона зазнає силової шкоди в кількості звичайної шкоди зброї, а в разі успіху — лише половину.",
    """The Eldritch Cannon you create is now more destructive, granting the following benefits.

Detonate. When you take damage, you can use your Reaction to command the cannon to detonate. Each enemy creature within 20 feet of you must make a Dexterity saving throw against your spell save DC, taking 3d10 Force damage on a failed save, or half as much damage on a successful one. You can use this ability once per short rest.

Firepower. The cannon’s damage rolls, as well as the number of Temporary Hit Points granted by Protector, increase by 1d8.""":
        """Створена вами Потойбічна гармата стає руйнівнішою й надає такі переваги.

Детонація. Коли ви зазнаєте шкоди, то можете застосувати реагування, щоб наказати гарматі вибухнути. Кожна ворожа істота в межах 20 футів повинна виконати кидок протидії спритністю проти вашої МС протидії закляттям. У разі невдачі вона зазнає 3d10 силової шкоди, а в разі успіху — лише половину. Цю здібність можна застосувати один раз за короткий відпочинок.

Вогнева міць. Кидки шкоди гармати й кількість тимчасових очок здоров’я, які надає «Захисник», збільшуються на 1d8.""",
    "When you take damage, you can use your Reaction to command the cannon to detonate. Each enemy creature within 20 feet of you must make a Dexterity saving throw against your spell save DC, taking 3d10 Force damage on a failed save, or half as much damage on a successful one. You can use this ability once per short rest.":
        "Коли ви зазнаєте шкоди, то можете застосувати реагування, щоб наказати гарматі вибухнути. Кожна ворожа істота в межах 20 футів повинна виконати кидок протидії спритністю проти вашої МС протидії закляттям. У разі невдачі вона зазнає 3d10 силової шкоди, а в разі успіху — лише половину. Цю здібність можна застосувати один раз за короткий відпочинок.",
    "Shade. The target has the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition until the end of its next turn or until the target makes an attack roll, deals damage, or casts a spell. When the invisibility ends, each creature in a 5-foot Emanation originating from the target must succeed on a Constitution saving throw or take Necrotic damage equal to two rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die.":
        "Тінь. Ціль набуває стану <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">невидимості</LSTag> до кінця свого наступного ходу або доки не виконає кидок атаки, не завдасть шкоди чи не прокаже закляття. Коли невидимість завершується, кожна істота у 5-футовій еманації від цілі повинна успішно виконати кидок протидії статурою, інакше зазнає некротичної шкоди в кількості двох кидків вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>.",
    "Has the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition. When the invisibility ends, each creature in a 5-foot Emanation originating from the character must succeed on a Constitution saving throw or take Necrotic damage equal to two rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die.":
        "Має стан <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">невидимості</LSTag>. Коли невидимість завершується, кожна істота у 5-футовій еманації від персонажа повинна успішно виконати кидок протидії статурою, інакше зазнає некротичної шкоди в кількості двох кидків вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>.",
    """The billowing flames of a dragon blast from your feet, granting you explosive speed. For the duration, your Speed increases by 20 feet, and moving doesn't provoke Opportunity Attacks. Whenever you move within 5 feet of a creature, it takes Fire damage from your trail of heat. A creature can take this damage only once during a turn.

At Higher Levels: your Speed increases by an additional 5 feet, and the Fire damage increases by 1d6, for each spell slot level above 3rd.""":
        """З-під ваших ніг виривається бурхливе драконяче полум’я, надаючи вибухової швидкості. Поки діє закляття, ваша швидкість збільшується на 20 футів, а переміщення не провокує принагідних атак. Щоразу, коли ви проходите в межах 5 футів від істоти, вона зазнає вогняної шкоди від вашого жаркого сліду. Істота може зазнати цієї шкоди лише раз за хід.

На вищих рівнях: за кожен рівень чарунки вище 3-го ваша швидкість збільшується ще на 5 футів, а вогняна шкода — на 1d6.""",
})

EXACT_OVERRIDES.update({
    "When you deal one of these types with it, you can also force the target to make a Strength saving throw. On a failed save, you can move the target up to 10 feet toward or away from you, as elemental energy swirls around it.":
        "Коли ви завдаєте нею шкоди одного з цих типів, то можете також змусити ціль виконати кидок протидії силою. У разі невдачі ви можете перемістити ціль на відстань до 10 футів до себе або від себе, оповивши її стихійною енергією.",
    """The Psychic damage of your Dreadful Strike becomes 2d8. The target must make a Wisdom saving throw against your spell save DC. On a failed save, a creature has the Frightened condition until the start of your next turn.

You are swift enough to turn a miss into a new strike. When you miss with a weapon attack, you can make another weapon attack for free.""":
        """Психічна шкода вашого «Страшного удару» збільшується до 2d8. Ціль повинна виконати кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі вона набуває стану переляку до початку вашого наступного ходу.

Ви досить швидкі, щоб перетворити промах на новий удар. Промахнувшись атакою зброєю, ви можете виконати ще одну атаку зброєю, не витрачаючи дії.""",
    "You add a toxin to your strike, forcing the target to make a Constitution saving throw. On a failed save, the target has the Poisoned condition for 1 minute. At the end of each of its turns, the Poisoned target repeats the save, ending the effect on itself on a success.":
        "Ви додаєте до удару токсин, змушуючи ціль виконати кидок протидії статурою. У разі невдачі ціль на 1 хвилину набуває стану отруєння. Наприкінці кожного свого ходу отруєна ціль повторює кидок і в разі успіху припиняє дію ефекту на собі.",
    "When you deal damage to a target with your Psionic Strike, you can force the target to make a Strength saving throw (DC 8 plus your Intelligence modifier and Proficiency Bonus). On a failed save, you can give the target the Prone condition or transport it up to 10 feet horizontally.":
        "Коли ви завдаєте цілі шкоди «Псіонічним ударом», то можете змусити її виконати кидок протидії силою з МС 8 + ваш модифікатор інтелекту + ваш бонус спеціалізації. У разі невдачі ви можете повалити ціль або перемістити її по горизонталі на відстань до 10 футів.",
    """You gain one use of your Breath Weapon.

You can expend one use of your Breath Weapon to roar, forcing each creature of your choice within 30 feet of you to make a Wisdom saving throw. On a failed save, a target becomes frightened of you for 1 minute.""":
        """Ви отримуєте одне застосування Дихальної зброї.

Ви можете витратити одне застосування Дихальної зброї, щоб заревіти й змусити кожну вибрану вами істоту в межах 30 футів виконати кидок протидії мудрістю. У разі невдачі ціль боїться вас протягом 1 хвилини.""",
    """When a creature hits you with an attack roll, you can take a Reaction to force the creature to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the <LSTag Type="Status" Tooltip="STUNNED">Stunned</LSTag> condition for 2 turns.

You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.""":
        """Коли істота влучає у вас атакою, ви можете застосувати реагування, щоб змусити її виконати кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі ціль на 2 ходи набуває стану <LSTag Type="Status" Tooltip="STUNNED">приголомшення</LSTag>.

Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.""",
    "When a creature hits you with an attack roll, you can take a Reaction to force the creature to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the <LSTag Type=\"Status\" Tooltip=\"STUNNED\">Stunned</LSTag> condition until the end of your next turn.":
        "Коли істота влучає у вас атакою, ви можете застосувати реагування, щоб змусити її виконати кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі ціль набуває стану <LSTag Type=\"Status\" Tooltip=\"STUNNED\">приголомшення</LSTag> до кінця вашого наступного ходу.",
    "When a creature hits you with an attack roll, you can take a Reaction to force the creature to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the <LSTag Type=\"Status\" Tooltip=\"STUNNED\">Stunned</LSTag> condition for 2 turns.":
        "Коли істота влучає у вас атакою, ви можете застосувати реагування, щоб змусити її виконати кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі ціль на 2 ходи набуває стану <LSTag Type=\"Status\" Tooltip=\"STUNNED\">приголомшення</LSTag>.",
    "Once per turn when you make an attack roll against an enemy and the roll doesn’t have Disadvantage, you can choose to make the roll with Disadvantage. When you do, you regain one expended Risk Die.":
        "Один раз за хід, виконуючи кидок атаки проти ворога без завади, ви можете вирішити виконати його із завадою. У такому разі ви відновлюєте одну витрачену кістку ризику.",
    "Once per turn when you hit a creature with a ranged weapon attack, you can force the target to make a Strength saving throw. On a failed save, the target has the Restrained condition for 2 turns.":
        "Один раз за хід, коли ви влучаєте в істоту дистанційною атакою зброєю, то можете змусити ціль виконати кидок протидії силою. У разі невдачі ціль на 2 ходи набуває стану знерухомлення.",
    """Requires Illrigger level 7 or higher.

When you use a bonus action to place or move a seal on a Large or smaller creature, you can activate this boon (no action required). You conjure infernal chains to grasp the target, forcing them to make a Strength saving throw. On a failed save, you can either pull the creature 10 feet toward you or cause them to be grappled until the end of your next turn.""":
        """Потребує 7-го рівня ілріґера або вищого.

Коли ви вторинною дією накладаєте чи переміщуєте печатку на істоту великого або меншого розміру, то можете активувати цей дар (дія не потрібна). Ви прикликаєте пекельні ланцюги, що хапають ціль і змушують її виконати кидок протидії силою. У разі невдачі ви можете підтягнути істоту на 10 футів до себе або надати їй стан схоплення до кінця свого наступного ходу.""",
    """Requires Illrigger level 7 or higher.

When you burn one or more seals on an interdicted creature, you can use your reaction to unleash an explosion of hellish energy around them. Each creature of your choice within 10 feet of the target must make a Dexterity saving throw. On a failed save, a creature takes the same amount and type of damage as the seals dealt to the interdicted creature. On a successful save, a creature takes half as much damage.""":
        """Потребує 7-го рівня ілріґера або вищого.

Коли ви спалюєте одну чи кілька печаток на істоті під забороною, то можете застосувати реагування, щоб вивільнити довкола неї вибух пекельної енергії. Кожна вибрана вами істота в межах 10 футів від цілі повинна виконати кидок протидії спритністю. У разі невдачі вона зазнає стільки ж шкоди того самого типу, скільки печатки завдали істоті під забороною; у разі успіху — лише половину.""",
    "When a creature the defender can see within 5 feet of it makes an attack roll against a target other than the defender, the triggering creature makes the attack roll with disadvantage.":
        "Коли видима захиснику істота в межах 5 футів атакує іншу ціль, ця істота виконує кидок атаки із завадою.",
    "Your reputation has become such that monsters preying on the fearful have come to fear you. When you hit a creature with an attack as part of a Reaction, you can force the creature to make a Wisdom saving throw or have the Frightened condition until the end of your next turn. The DC for the saving throw equals 8 plus your Intelligence modifier and your Proficiency Bonus.":
        "Ваша слава зростає настільки, що чудовиська, які полюють на наляканих, самі починають вас боятися. Коли ви влучаєте в істоту атакою як частиною реагування, то можете змусити її виконати кидок протидії мудрістю, інакше вона набуде стану переляку до кінця вашого наступного ходу. МС кидка дорівнює 8 + ваш модифікатор інтелекту + ваш бонус спеціалізації.",
    "When you transform and at the start of each of your subsequent turns, each creature of your choice in a 10-foot Emanation originating from you makes a Wisdom saving throw against your spell save DC. On a failed save, a creature has the Frightened condition until the start of your next turn.":
        "Коли ви перетворюєтеся, а також на початку кожного свого наступного ходу, кожна вибрана вами істота у 10-футовій еманації від вас виконує кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі істота набуває стану переляку до початку вашого наступного ходу.",
})

EXACT_OVERRIDES.update({
    "You can nimbly dodge out of the way of certain dangers. When you’re subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. You can’t use this feature if you have the Incapacitated condition.":
        "Ви вмієте спритно уникати певних небезпек. Коли ефект дає вам змогу виконати кидок протидії спритністю, щоб зазнати лише половини шкоди, ви натомість не зазнаєте шкоди в разі успіху й зазнаєте лише половини в разі невдачі. Ви не можете застосувати цю особливість у стані недієздатності.",
    """When you’re subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail.

You don’t benefit from this feature if you have the Incapacitated condition.""":
        """Коли ефект дає вам змогу виконати кидок протидії спритністю, щоб зазнати лише половини шкоди, ви натомість не зазнаєте шкоди в разі успіху й зазнаєте лише половини в разі невдачі.

Ця особливість не діє на вас у стані недієздатності.""",
    "When you’re subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail.":
        "Коли ефект дає вам змогу виконати кидок протидії спритністю, щоб зазнати лише половини шкоди, ви натомість не зазнаєте шкоди в разі успіху й зазнаєте лише половини в разі невдачі.",
    "The target makes a Constitution saving throw against your spell save DC. On a failed save, it can't make Opportunity Attacks, and its Speed is halved until the start of your next turn.":
        "Ціль виконує кидок протидії статурою проти вашої МС протидії закляттям. У разі невдачі вона не може виконувати принагідні атаки, а її швидкість зменшується вдвічі до початку вашого наступного ходу.",
    "The target makes a Wisdom saving throw against your spell save DC. On a failed save, the next time it makes an attack roll against a creature other than you before the start of your next turn, it takes 1d6 Necrotic damage.":
        "Ціль виконує кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі, коли до початку вашого наступного ходу вона вперше атакуватиме іншу істоту, то зазнає 1d6 некротичної шкоди.",
    "If you attack a creature within 5 feet of you as part of the Attack action and hit with a Melee weapon, you can immediately bash the target with your Shield if it’s equipped, forcing the target to make a Strength saving throw (DC 8 plus your Strength modifier and Proficiency Bonus). On a failed save, you either push the target 5 feet from you or cause it to have the Prone condition (your choice). You can use this benefit only once on each of your turns.":
        "Якщо дією «Атака» ви атакуєте істоту в межах 5 футів і влучаєте зброєю ближнього бою, то можете одразу вдарити ціль спорядженим щитом, змусивши її виконати кидок протидії силою з МС 8 + ваш модифікатор сили + ваш бонус спеціалізації. У разі невдачі ви на свій вибір або відштовхуєте ціль від себе на 5 футів, або повалюєте її. Цю перевагу можна застосувати лише раз за кожен свій хід.",
    "Whenever a creature in the Cylinder casts a spell, that creature makes a Constitution saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted.":
        "Щоразу, коли істота в циліндрі проказує закляття, вона виконує кидок протидії статурою. У разі невдачі закляття розсіюється без ефекту, а витрачені на його проказування дія, вторинна дія чи реагування втрачаються.",
    "Trickster. The target makes a Wisdom saving throw. On a failed save, the target takes Psychic damage equal to two rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die and has the Charmed condition until the start of your next turn. On a successful save, the target takes half as much damage only.":
        "Штукар. Ціль виконує кидок протидії мудрістю. У разі невдачі вона зазнає психічної шкоди в кількості двох кидків вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> і набуває стану причарування до початку вашого наступного ходу. У разі успіху ціль зазнає лише половини шкоди.",
    "Arsonist. The target makes a Dexterity saving throw, taking Fire damage equal to four rolls of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die on a failed save or half as much damage on a successful one.":
        "Палій. Ціль виконує кидок протидії спритністю. У разі невдачі вона зазнає вогняної шкоди в кількості чотирьох кидків вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>, а в разі успіху — лише половину.",
    "As a Reaction when a creature targets you with an attack, you can expend 1 Divine Point to force it to make a Wisdom saving throw. On a failed save, the attacker must choose a new target or the attack has no effect, and it can’t target you again until the start of your next turn. This feature does not protect you from areas of effect.":
        "Коли істота обирає вас ціллю атаки, ви можете реагуванням витратити 1 божественне очко й змусити її виконати кидок протидії мудрістю. У разі невдачі нападник повинен вибрати нову ціль, інакше атака не матиме ефекту; до початку вашого наступного ходу він не зможе знову обрати вас ціллю. Ця особливість не захищає від зональних ефектів.",
    "For the duration, you can choose one creature in it to make a Constitution saving throw. On a failure, the creature takes 3d8 Necrotic damage.":
        "Поки діє ефект, ви можете вибрати одну істоту в цій області й змусити її виконати кидок протидії статурою. У разі невдачі істота зазнає 3d8 некротичної шкоди.",
    "You have the <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">Invisible</LSTag> condition for 1 minute. This invisibility ends on a creature immediately after it makes an attack roll, deals damage, or casts a spell.":
        "Ви набуваєте стану <LSTag Type=\"Status\" Tooltip=\"INVISIBLE\">невидимості</LSTag> на 1 хвилину. Для істоти невидимість завершується одразу після того, як вона виконає кидок атаки, завдасть шкоди чи прокаже закляття.",
    """If you make an attack roll for a spell and miss, you can spend 1 Sorcery Point to reroll the d20, and you must use the new roll.

You can use Seeking Spell even if you’ve already used a different Metamagic option during the casting of the spell.""":
        """Якщо ви промахуєтеся кидком атаки закляття, то можете витратити 1 очко чародійства, щоб перекинути d20; потрібно використати новий результат.

Ви можете застосувати «Пошукове закляття», навіть якщо під час проказування цього закляття вже застосували іншу опцію метамагії.""",
    "You can use your Channel Oath to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll.":
        "Ви можете скористатися Обітним наснаженням, щоб ударити з надприродною точністю. Виконуючи кидок атаки, ви можете застосувати Боже наснаження й отримати бонус +10 до кидка.",
    "Once per turn, when you hit a creature with an attack roll, you can force it to make a Wisdom saving throw against your spell save DC. On a failed save, the target has the Frightened condition until the end of your next turn.":
        "Один раз за хід, коли ви влучаєте в істоту атакою, то можете змусити її виконати кидок протидії мудрістю проти вашої МС протидії закляттям. У разі невдачі ціль набуває стану переляку до кінця вашого наступного ходу.",
})

EXACT_OVERRIDES.update({
    "If you hit a creature with this weapon and deal damage to it, you can reduce its Speed by [1] until the start of your next turn. If the creature is hit more than once by weapons that have this property, the Speed reduction doesn’t exceed [1].":
        "Якщо ви влучаєте в істоту цією зброєю й завдаєте їй шкоди, то можете зменшити її швидкість на [1] до початку свого наступного ходу. Якщо істота зазнає кількох влучань зброєю з цією властивістю, загальне зменшення швидкості не перевищує [1].",
    "If you hit a creature with this weapon and deal damage to the creature, you have Advantage on your next attack roll against that creature before the end of your next turn.":
        "Якщо ви влучаєте в істоту цією зброєю й завдаєте їй шкоди, то маєте перевагу на свій наступний кидок атаки проти неї до кінця свого наступного ходу.",
    "Creatures gains Temporary Hit Points equal to twice the number rolled on the Bardic Inspiration die, and each can move without provoking Opportunity Attacks until the end of its next turn.":
        "Істоти отримують тимчасові очки здоров’я в кількості, що вдвічі перевищує результат кидка кістки Бардівського натхнення, і до кінця свого наступного ходу можуть переміщуватися, не провокуючи принагідних атак.",
    "When you hit a creature with a ranged attack, it has a chance to gain the <LSTag Type=\"Status\" Tooltip=\"GAPING_WOUND\">Gaping Wounds</LSTag> condition.":
        "Коли ви влучаєте в істоту дистанційною атакою, вона може набути стану <LSTag Type=\"Status\" Tooltip=\"GAPING_WOUND\">глибоких ран</LSTag>.",
    """Your <LSTag Type="Status" Tooltip="RAGE">Rage</LSTag> taps into the life force of the World Tree. You gain the following benefits.

Vitality Surge. When you activate your Rage, you gain a number of Temporary Hit Points equal to your Barbarian level.

Life-Giving Force. At the start of each of your turns while your Rage is active, you can choose another creature within 10 feet of yourself to gain Temporary Hit Points. To determine the number of Temporary Hit Points, roll a number of d6s equal to your <LSTag Type="Status" Tooltip="RAGE">Rage</LSTag> Damage bonus, and add them together. If any of these Temporary Hit Points remain when your Rage ends, they vanish.""":
        """Ваша <LSTag Type="Status" Tooltip="RAGE">Лють</LSTag> черпає життєву силу Світового Дерева. Ви отримуєте такі переваги.

Приплив життєвої сили. Коли ви входите в Лють, то отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому рівню варвара.

Життєдайна сила. На початку кожного свого ходу, поки триває Лють, ви можете вибрати іншу істоту в межах 10 футів, щоб надати їй тимчасові очки здоров’я. Киньте стільки d6, скільки становить ваш бонус шкоди <LSTag Type="Status" Tooltip="RAGE">Люті</LSTag>, і додайте результати. Надані таким чином тимчасові очки зникають, коли ваша Лють завершується.""",
    "A creature affected by this feature gains Temporary Hit Points. To determine the number of Temporary Hit Points, roll a number of d6s equal to Barbarian's <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> Damage bonus and add them together.":
        "Істота, на яку діє ця особливість, отримує тимчасові очки здоров’я. Щоб визначити їх кількість, киньте стільки d6, скільки становить бонус шкоди <LSTag Type=\"Status\" Tooltip=\"RAGE\">Люті</LSTag> варвара, і додайте результати.",
    """Inspiring Strike. Once per turn when you score a Critical Hit against a creature, you gain <LSTag Type="Status" Tooltip="HEROIC_INSPIRATION_TEMP">Heroic Inspiration</LSTag>.

Reassert Honor. When an enemy you can see deals damage to you, you have Advantage on your next attack roll against that enemy before the end of your next turn.""":
        """Надихальний удар. Один раз за хід, коли ви завдаєте істоті критичного влучання, то отримуєте <LSTag Type="Status" Tooltip="HEROIC_INSPIRATION_TEMP">Героїчне натхнення</LSTag>.

Відновлення честі. Коли видимий вам ворог завдає вам шкоди, ви маєте перевагу на свій наступний кидок атаки проти нього до кінця свого наступного ходу.""",
    """Entreat. You gain proficiency in <LSTag Type="Skills" Tooltip="Persuasion">Persuasion</LSTag>.

Rallying Cry. You can choose a number of creatures equal to your Proficiency Bonus that you can see within 30 feet of yourself. Those creatures gain <LSTag Type="Status" Tooltip="HEROIC_INSPIRATION_TEMP">Heroic Inspiration</LSTag>. Once you use this benefit, you can’t do so again until you finish a Long Rest.""":
        """Умовляння. Ви отримуєте володіння навичкою <LSTag Type="Skills" Tooltip="Persuasion">Переконливість</LSTag>.

Закличний клич. Виберіть видимих вам істот у межах 30 футів у кількості, що дорівнює вашому бонусу спеціалізації. Вони отримують <LSTag Type="Status" Tooltip="HEROIC_INSPIRATION_TEMP">Героїчне натхнення</LSTag>. Скориставшись цією перевагою, ви не зможете зробити це знову до завершення довгого відпочинку.""",
    """When you spend at least 1 Sorcery Point as part of a Magic action or a Bonus Action on your turn, you can unleash one of the following magical effects of your choice. You can do so only once per turn.

Bolstering Flames. You or one creature you can see within 30 feet of yourself gains Temporary Hit Points equal to 1d4 plus your Charisma modifier.

Radiant Fire. One creature you can see within 30 feet of yourself takes 1d4 Fire or Radiant damage (your choice).""":
        """Коли у свій хід ви витрачаєте щонайменше 1 очко чародійства як частину магічної чи вторинної дії, то можете вивільнити один із таких магічних ефектів на свій вибір. Це можна зробити лише раз за хід.

Зміцнювальне полум’я. Ви або одна видима вам істота в межах 30 футів отримує 1d4 + ваш модифікатор харизми тимчасових очок здоров’я.

Променевий вогонь. Одна видима вам істота в межах 30 футів зазнає 1d4 вогняної або променевої шкоди (на ваш вибір).""",
    "When the creature takes damage before the spell ends, the creature reduces the total damage taken by 1d4. A creature can benefit from this spell only once per turn.":
        "Коли істота зазнає шкоди до завершення закляття, вона зменшує загальну отриману шкоду на 1d4. Істота може скористатися цим закляттям лише раз за хід.",
    "When you heal another creature, it gains the following effect: whenever a creature makes an attack roll against it before the spell ends, the attacker subtracts 1d4 from the roll.":
        "Коли ви зцілюєте іншу істоту, вона отримує такий ефект: щоразу, коли до завершення закляття хтось атакує її, нападник віднімає 1d4 від кидка атаки.",
    "Undead creatures that hit the wearer take [1]. Beasts that hit the wearer become <LSTag Type=\"Status\" Tooltip=\"CHARMED\">Charmed</LSTag>.":
        "Невмерлі істоти, які влучають у власника, зазнають [1]. Звірі, які влучають у власника, набувають стану <LSTag Type=\"Status\" Tooltip=\"CHARMED\">причарування</LSTag>.",
    "When you make a weapon attack against a Charmed creature, you can gain Advantage on the attack roll (no action required). If the attack hits, it becomes a Critical Hit.":
        "Атакуючи зброєю причаровану істоту, ви можете отримати перевагу на кидок атаки (дія не потрібна). Якщо атака влучає, вона стає критичним влучанням.",
    "Your attacks against interdicted creatures score a critical hit on a roll of 19 through 20.":
        "Ваші атаки проти істот під забороною стають критичними влучаннями, якщо на кістці випадає 19 або 20.",
    "When you use your bonus action to place an illrigger’s seal on a creature, or when you burn a seal placed on a creature, you gain the effects of <LSTag Type=\"Spell\" Tooltip=\"Shout_BladeWard\">Blade Ward</LSTag> for 2 turns.":
        "Коли ви вторинною дією накладаєте на істоту печатку ілріґера або спалюєте накладену печатку, то на 2 ходи отримуєте ефект <LSTag Type=\"Spell\" Tooltip=\"Shout_BladeWard\">«Оберегу від зброї»</LSTag>.",
    "You have Advantage on saving throws against spells. Additionally, when you damage a creature that is concentrating, it has Disadvantage on the saving throw it makes to maintain its Concentration.":
        "Ви маєте перевагу на кидки протидії закляттям. Крім того, коли ви завдаєте шкоди істоті, що підтримує концентрацію, вона має заваду на кидок протидії для її підтримання.",
    """Your mental power increases, allowing you to project a sense of calm in a 10-foot Emanation that originates from you. The projection is inactive if you have the Incapacitated condition.

You and your allies in the projection gain a +2 bonus to Intelligence, Wisdom, and Charisma saving throws.

If another Mind Domain Cleric is present, a creature can only benefit from one Gestalt Anchor at a time.""":
        """Ваша сила розуму зростає, даючи змогу випромінювати спокій у 10-футовій еманації від вас. Проєкція не діє, якщо ви маєте стан недієздатності.

Ви й ваші союзники в межах проєкції отримуєте бонус +2 до кидків протидії інтелектом, мудрістю та харизмою.

Якщо поруч є інший клірик домену розуму, істота може одночасно користуватися лише одним «Гештальт-якорем».""",
    "You can use your Channel Divinity to refresh your allies with soothing twilight.\n\nAs an action, you present your holy symbol, and a sphere of twilight emanates from you. The sphere is centered on you, has a 30-foot radius, and is filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature ends its turn in the sphere, it gains temporary hit points equal to 1d6 plus your Cleric level and ends one effect causing it to be charmed or frightened.":
        "Ви можете застосувати Боже наснаження, щоб огорнути союзників заспокійливими сутінками.\n\nДією ви здіймаєте свій священний символ, і від вас поширюється сфера сутінків радіусом 30 футів, наповнена тьмяним світлом. Сфера рухається разом із вами й існує 1 хвилину або доки ви не станете недієздатним чи не помрете. Щоразу, коли істота завершує свій хід у сфері, вона отримує 1d6 + ваш рівень клірика тимчасових очок здоров’я та припиняє один ефект, що спричиняє її причарування або переляк.",
    "Whenever a creature ends its turn in the sphere, it gains temporary hit points equal to 1d6 plus Cleric level and ends one effect causing it to be charmed or frightened.":
        "Щоразу, коли істота завершує свій хід у сфері, вона отримує 1d6 + рівень клірика тимчасових очок здоров’я та припиняє один ефект, що спричиняє її причарування або переляк.",
})

EXACT_OVERRIDES.update({
    "You can channel divine energy to create special effects such as <LSTag Type=\"Spell\" Tooltip=\"Target_DivineSpark\">Divine Spark</LSTag> and Turn Undead, choosing one each time you use Channel Divinity. Additional effects and uses are gained at higher Cleric levels. You regain one use on a Short Rest and all uses on a Long Rest. Saving throw DCs use your Spellcasting DC.":
        "Ви можете спрямовувати божественну енергію для створення особливих ефектів, як-от <LSTag Type=\"Spell\" Tooltip=\"Target_DivineSpark\">«Божественна іскра»</LSTag> та «Вигнання невмерлих», вибираючи один із них щоразу, коли застосовуєте Боже наснаження. На вищих рівнях клірика ви отримуєте додаткові ефекти й застосування. Одне застосування відновлюється після короткого відпочинку, а всі — після довгого. Для кидків протидії використовується ваша МС протидії закляттям.",
    "Click the spell slot icon on the hotbar to use your prepared spells.":
        "Натисніть значок чарунки на панелі швидкого доступу, щоб проказати підготовлені закляття.",
    "You can cast the spell once per Short Rest without expending an action.":
        "Ви можете проказати це закляття один раз за короткий відпочинок, не витрачаючи дії.",
    "When a creature you can see within 60 feet of you casts a spell or makes a spell attack, you can use Studied Response against that creature.":
        "Коли видима вам істота в межах 60 футів проказує закляття або виконує атаку закляттям, ви можете застосувати проти неї «Вивчену відповідь».",
    """You can manipulate the balance between life and death, granting you the following benefits.

Pull of Death. Once per turn, when you deal damage to a creature that’s missing any Hit Points by casting a spell or by hitting with an attack roll, that creature takes an extra 1d4 Necrotic damage. This extra damage increases to 1d6 when you reach Cleric level 11.

Return to Life. You can cast Spare the Dying as a Bonus Action.

Additionally, when you would normally roll one or more dice to restore Hit Points to a creature at 0 Hit Points with a spell or Channel Divinity, you don't roll those dice. Instead, the creature regains Hit Points equal to your Cleric level.""":
        """Ви можете керувати рівновагою між життям і смертю та отримуєте такі переваги.

Поклик смерті. Один раз за хід, коли ви завдаєте шкоди істоті, що втратила хоча б одне очко здоров’я, проказавши закляття або влучивши атакою, вона додатково зазнає 1d4 некротичної шкоди. На 11-му рівні клірика ця додаткова шкода збільшується до 1d6.

Повернення до життя. Ви можете проказувати «Пощаду» вторинною дією.

Крім того, коли закляттям або Божим наснаженням ви мали б кинути одну чи кілька кісток, щоб відновити очки здоров’я істоті з 0 очок, не кидайте їх. Натомість істота відновлює очки здоров’я в кількості, що дорівнює вашому рівню клірика.""",
    "When you cast Warlock Cantrip, add your <LSTag Tooltip=\"Charisma\">Charisma</LSTag> <LSTag Tooltip=\"AbilityModifier\">Modifier</LSTag> to the damage it deals, unless it is negative.":
        "Коли ви проказуєте замовляння чаклуна, додайте свій <LSTag Tooltip=\"AbilityModifier\">модифікатор</LSTag> <LSTag Tooltip=\"Charisma\">харизми</LSTag> до завданої ним шкоди, якщо модифікатор не від’ємний.",
    "You learn to buffet your foes with mental power. When you cast a Cleric spell that deals Radiant or Psychic damage, each target of that spell takes extra Psychic damage equal to your Charisma modifier.":
        "Ви навчаєтеся вражати ворогів силою розуму. Коли ви проказуєте закляття клірика, що завдає променевої або психічної шкоди, кожна його ціль додатково зазнає психічної шкоди в кількості, що дорівнює вашому модифікатору харизми.",
    """A spell scroll can be used only if the spell on the scroll appears on the spell list of one of your classes or subclasses.

In addition, your highest spell slot level must be at least one level lower than the level of the spell on the scroll. When determining spell slot levels for a multiclass character, only levels in classes and subclasses that have the spell on their spell list are counted.

Scrolls of Revivify are always exempt from this restriction and can be used by any character.""":
        """Ви можете скористатися сувоєм закляття, лише якщо це закляття є у списку заклять одного з ваших класів або підкласів.

Крім того, рівень закляття на сувої не може перевищувати рівень вашої найвищої чарунки більш ніж на один. Для мультикласового персонажа під час визначення рівнів чарунок враховуються лише класи й підкласи, до списків яких входить це закляття.

Це обмеження ніколи не поширюється на сувої «Повернення до життя»: їх може використати будь-який персонаж.""",
    "When you cast a Divination spell using a spell slot of 2nd level or higher, you regain one expended spell slot that is one level lower than the slot used to cast the spell. You can't regain spell slots higher than 5th level with this feature.":
        "Коли ви проказуєте закляття віщування, використовуючи чарунку щонайменше 2-го рівня, то відновлюєте одну витрачену чарунку на один рівень нижчу за використану. За допомогою цієї особливості не можна відновити чарунку вище 5-го рівня.",
    """You can weave magic around yourself for protection. When you cast an Abjuration spell with a spell slot, you can simultaneously use a strand of the spell’s magic to create a magical ward on yourself that lasts until you finish a Long Rest. The ward has a Hit Point maximum equal to twice your Wizard level plus your Intelligence modifier. Whenever you take damage, the ward takes the damage instead, and if you have any Resistances or Vulnerabilities, apply them before reducing the ward’s Hit Points. If the damage reduces the ward to 0 Hit Points, you take any remaining damage. While the ward has 0 Hit Points, it can’t absorb damage, but its magic remains.

Whenever you cast an Abjuration spell with a spell slot, the ward regains a number of Hit Points equal to twice the level of the spell slot. Alternatively, as a Bonus Action, you can expend a spell slot, and the ward regains a number of Hit Points equal to twice the level of the spell slot expended.""":
        """Ви можете огортати себе захисною магією. Коли ви проказуєте закляття віднадження з використанням чарунки, то можете водночас створити на собі Магічний оберіг, що існує до завершення довгого відпочинку. Максимум очок здоров’я оберега дорівнює подвійному рівню чарівника + ваш модифікатор інтелекту. Коли ви зазнаєте шкоди, її натомість зазнає оберіг; стійкості та вразливості застосовуються до зменшення його очок здоров’я. Якщо шкода знижує очки оберега до 0, решти шкоди зазнаєте ви. За 0 очок здоров’я оберіг не поглинає шкоди, але його магія зберігається.

Щоразу, коли ви проказуєте закляття віднадження з використанням чарунки, оберіг відновлює очки здоров’я в кількості, що вдвічі перевищує рівень чарунки. Або ж вторинною дією ви можете витратити чарунку, щоб оберіг відновив удвічі більше очок здоров’я, ніж рівень витраченої чарунки.""",
    "You can manipulate your own shadow to extend your reach. When you cast a cleric spell with a range of touch, your shadow can deliver the spell as if you had cast the spell. Your target must be within 15 feet of you, and you must be able to see the target. You can use this feature even if you are in an area where you cast no shadow.":
        "Ви можете керувати власною тінню, щоб збільшити досяжність. Коли ви проказуєте закляття клірика з дальністю «Дотик», ваша тінь може передати його так, наче це зробили ви. Ціль має бути видимою вам і перебувати в межах 15 футів. Цю особливість можна застосовувати навіть там, де ви не відкидаєте тіні.",
    "When you cast this spell using a spell slot of 4th level or higher, increase your speed by [1] for each spell slot level above 3rd. The spell deals an additional [2] for each slot level above 3rd.":
        "Коли ви проказуєте це закляття чарункою щонайменше 4-го рівня, за кожен рівень чарунки вище 3-го ваша швидкість збільшується на [1], а закляття додатково завдає [2].",
    "When you cast a spell that has a casting time of an action, you can spend 2 Sorcery Points to change the casting time to a Bonus Action for this casting. You can’t modify a spell in this way if you’ve already cast a level 1+ spell on the current turn, nor can you cast a level 1+ spell on this turn after modifying a spell in this way.":
        "Коли ви проказуєте закляття з часом проказування 1 дія, то можете витратити 2 очки чародійства й цього разу проказати його вторинною дією. Ви не можете змінити закляття таким чином, якщо в поточному ході вже проказали закляття рівня 1+; після такої зміни ви також не можете проказати інше закляття рівня 1+ у цьому ході.",
    "When you cast a spell that has a range of at least 5 feet, you can spend 1 Sorcery Point to double the spell’s range. Or when you cast a spell that has a range of Touch, you can spend 1 Sorcery Point to make the spell’s range 30 feet.":
        "Коли ви проказуєте закляття з дальністю щонайменше 5 футів, то можете витратити 1 очко чародійства й подвоїти його дальність. Або ж, проказуючи закляття з дальністю «Дотик», ви можете витратити 1 очко чародійства й змінити його дальність на 30 футів.",
    "When you cast a spell, you can spend 1 Sorcery Point to cast it without any Verbal, Somatic, or Material components, except Material components that are consumed by the spell or that have a cost specified in the spell.":
        "Проказуючи закляття, ви можете витратити 1 очко чародійства, щоб обійтися без словесного, тілесного й матеріального складників, окрім матеріального складника, який закляття поглинає або для якого вказано вартість.",
    "When you cast a spell, such as Charm Person, that can be cast with a higher-level spell slot to target an additional creature, you can spend 1 Sorcery Point to increase the spell’s effective level by 1.":
        "Коли ви проказуєте закляття на кшталт «Причарування особи», яке за використання чарунки вищого рівня може вразити додаткову ціль, то можете витратити 1 очко чародійства й підвищити ефективний рівень закляття на 1.",
    "When you cast a Warlock spell that deals damage, you can change its damage type to Psychic. In addition, when you cast a Warlock spell that is an Enchantment or Illusion, you can do so without Verbal or Somatic components.":
        "Коли ви проказуєте закляття чаклуна, що завдає шкоди, то можете змінити її тип на психічну. Крім того, закляття чаклуна школи зачарування чи ілюзії ви можете проказувати без словесного й тілесного складників.",
    """You can magically produce sticky, silken spider webs from your hands. As a Bonus Action, you can use them to do one of the following.

<LSTag Type="Spell" Tooltip="Target_ArachnoidStalker_Pull">Pulling Web</LSTag>. Strike a creature or object within [1] with a skin-adhering web and pull it up to [1] closer to you. Only a target of Large size or smaller can be moved, and a creature resists with a successful Dexterity saving throw. An ally is always pulled.

<LSTag Type="Spell" Tooltip="Target_ArachnoidStalker_WebSwing">Web Swing</LSTag>. Project a line of web at a point you can see within [1] and pull yourself to that point without provoking Opportunity Attacks.

Web. You cast Web without a spell slot as a part of the Bonus Action used for this feature. The webs fill a [2] radius and dissolve after 1 minute, and a creature caught inside must succeed on a Dexterity saving throw or become <LSTag Type="Status" Tooltip="WEB">Enwebbed</LSTag>. You can cast this spell using this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.

The saving throw DC equals 8 plus your Dexterity modifier and Proficiency Bonus.""":
        """Ви можете магічно випускати з рук липке шовкове павутиння. Вторинною дією використайте його одним із таких способів.

<LSTag Type="Spell" Tooltip="Target_ArachnoidStalker_Pull">Потяг павутини</LSTag>. Влучте павутиною в істоту чи предмет у межах [1] і підтягніть ціль до себе на відстань до [1]. Перемістити можна лише ціль великого або меншого розміру; істота чинить опір успішним кидком протидії спритністю. Союзник завжди підтягується.

<LSTag Type="Spell" Tooltip="Target_ArachnoidStalker_WebSwing">Гойдання на павутині</LSTag>. Випустіть павутину у видиму точку в межах [1] і підтягніться до неї, не провокуючи принагідних атак.

Павутина. Тією самою вторинною дією ви проказуєте «Павутину», не витрачаючи чарунки. Павутиння заповнює область радіусом [2] і розчиняється через 1 хвилину; істота, що потрапила всередину, повинна успішно виконати кидок протидії спритністю, інакше стане <LSTag Type="Status" Tooltip="WEB">обплутаною</LSTag>. За допомогою цієї особливості закляття можна проказати двічі. Одне витрачене застосування відновлюється після короткого відпочинку, а всі — після довгого.

МС кидка протидії дорівнює 8 + ваш модифікатор спритності + ваш бонус спеціалізації.""",
    "You cast Web without a spell slot as a part of the Bonus Action used for this feature (DC equals 8 plus your Dexterity modifier and Proficiency Bonus). You can cast this spell using this feature twice. You regain one expended use when you finish a Short Rest, and you regain all expended uses when you finish a Long Rest.":
        "Тією самою вторинною дією ви проказуєте «Павутину», не витрачаючи чарунки; МС дорівнює 8 + ваш модифікатор спритності + ваш бонус спеціалізації. За допомогою цієї особливості закляття можна проказати двічі. Одне витрачене застосування відновлюється після короткого відпочинку, а всі — після довгого.",
    "On its turn, can cast one of the cleric's prepared spells with the expended spell slot, using the cleric's spell save DC and spell attack bonus.":
        "У свій хід може витратити чарунку й проказати одне з підготовлених заклять клірика, використовуючи його МС протидії закляттям і бонус атаки закляттям.",
    "On its turn, can cast one of the cleric's cantrips, using the cleric's spell save DC and spell attack bonus.":
        "У свій хід може проказати одне із замовлянь клірика, використовуючи його МС протидії закляттям і бонус атаки закляттям.",
    """You gain the ability to channel your ki into searing waves of energy. Immediately after you take the Attack action on your turn, you can spend 2 ki points to cast the burning hands spell as a bonus action.

You can spend additional ki points to cast burning hands as a higher-level spell. Each additional ki point you spend increases the spell’s level by 1. The maximum number of ki points (2 plus any additional points) that you can spend on the spell equals half your monk level.""":
        """Ви навчаєтеся спрямовувати кі в пекучі хвилі енергії. Одразу після виконання дії «Атака» у свій хід ви можете витратити 2 очки кі, щоб проказати «Палючі руки» вторинною дією.

Ви можете витратити додаткові очки кі, щоб проказати «Палючі руки» як закляття вищого рівня. Кожне додаткове очко підвищує рівень закляття на 1. Максимальна загальна кількість очок кі, яку можна витратити на закляття, дорівнює половині вашого рівня монаха.""",
})

EXACT_OVERRIDES.update({
    """Improved <LSTag Type="Spell" Tooltip="Shout_Dash">Dash</LSTag>. When you take the Dash action, your Speed increases by 10 feet for that action.

Charge Attack. If you move at least 10 feet in a straight line toward a target immediately before hitting it with a melee attack roll as part of the Attack action, choose one of the following effects: gain a 1d8 bonus to the attack’s damage roll, or push the target up to 10 feet away if it is no more than one size larger than you. You can use this benefit only once on each of your turns.""":
        """Покращений <LSTag Type="Spell" Tooltip="Shout_Dash">Ривок</LSTag>. Коли ви виконуєте дію «Ривок», ваша швидкість для цієї дії збільшується на 10 футів.

Атака з розгону. Якщо безпосередньо перед влучанням атакою ближнього бою в межах дії «Атака» ви перемістилися щонайменше на 10 футів по прямій до цілі, виберіть один ефект: отримати бонус 1d8 до кидка шкоди атаки або відштовхнути ціль на відстань до 10 футів, якщо вона більша за вас не більш ніж на одну категорію розміру. Цю перевагу можна застосувати лише раз за кожен свій хід.""",
    "The ward is represented by a number of d8s equal to the number of Sorcery Points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice.":
        "Оберіг має кількість d8, що дорівнює кількості очок чародійства, витрачених на його створення. Коли захищена істота зазнає шкоди, вона може витратити будь-яку кількість цих кісток, кинути їх і зменшити отриману шкоду на суму результатів.",
    "When an enemy you can see within 30 feet of yourself takes damage and is Bloodied after taking that damage but not killed outright, you can take a Reaction and teleport to an unoccupied space you can see within 5 feet of that enemy. You can then make one melee attack. You can use this feature a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Коли видимий вам ворог у межах 30 футів зазнає шкоди, після якої стає закривавленим, але не гине одразу, ви можете застосувати реагування й телепортуватися у видимий вам вільний простір у межах 5 футів від нього. Після цього ви можете виконати одну атаку ближнього бою. Кількість застосувань цієї особливості дорівнює вашому модифікатору інтелекту (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
})

EXACT_OVERRIDES.update({
    "Once per Short Rest, as a Bonus Action, you unleash a <LSTag Type=\"Spell\" Tooltip=\"Shout_ZealousPresence\">battle cry</LSTag> infused with divine energy; creatures of your choice within 60 feet of you gain Advantage on attack rolls and saving throws until the start of your next turn.":
        "Один раз за короткий відпочинок ви можете вторинною дією здійняти сповнений божественної енергії <LSTag Type=\"Spell\" Tooltip=\"Shout_ZealousPresence\">бойовий клич</LSTag>. Вибрані вами істоти в межах 60 футів отримують перевагу на кидки атаки й протидії до початку вашого наступного ходу.",
    "Curse a creature with your touch. It suffers <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Strength <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> and <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> сили та <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> силою.",
    "Curse a creature with your touch. It suffers <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Dexterity <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> and <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> спритності та <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> спритністю.",
    "Curse a creature with your touch. It suffers <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Constitution <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> and <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> статури та <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> статурою.",
    "Curse a creature with your touch. It suffers <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Intelligence <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> and <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> інтелекту та <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> інтелектом.",
    "Curse a creature with your touch. It suffers <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Wisdom <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> and <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> мудрості та <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> мудрістю.",
    "Curse a creature with your touch. It suffers <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on Charisma <LSTag Tooltip=\"AbilityCheck\">Checks</LSTag> and <LSTag Tooltip=\"SavingThrow\">Saving Throws</LSTag>.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AbilityCheck\">перевірки</LSTag> харизми та <LSTag Tooltip=\"SavingThrow\">кидки протидії</LSTag> харизмою.",
    "Curse a creature with your touch. It has <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on <LSTag Tooltip=\"AttackRoll\">Attack Rolls</LSTag> against you.":
        "Проклясти істоту дотиком. Вона має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> на <LSTag Tooltip=\"AttackRoll\">кидки атаки</LSTag> проти вас.",
    "Requires Illrigger level 7 or higher.\n\nYou can expend a seal as a bonus action to weave a mantle of semisolid shadows around yourself or a creature you touch. The target gains a +2 bonus to AC for 1 minute.":
        "Потребує 7-го рівня ілріґера або вищого.\n\nВторинною дією ви можете витратити печатку, щоб огорнути себе або істоту, якої торкаєтеся, мантією напівтілесних тіней. Ціль отримує бонус +2 до РЗ на 1 хвилину.",
    "Your hunger for your enemy allows you to partake of its essence during battle. When you deal damage to a creature with a melee attack using a weapon, you gain 6 Temporary Hit Points.":
        "Жага до ворога дає вам змогу живитися його сутністю в бою. Коли ви завдаєте істоті шкоди атакою зброєю ближнього бою, то отримуєте 6 тимчасових очок здоров’я.",
})

EXACT_OVERRIDES.update({
    "Whenever you deal damage with your Unarmed Strike, it can deal your choice of Force damage or its normal damage type.":
        "Щоразу, коли ви завдаєте шкоди Ударом голіруч, то можете вибрати: завдати силової шкоди або шкоди звичайного типу.",
    "Deals Psychic damage and has the <LSTag Tooltip=\"Thrown\">Thrown</LSTag> property.\n\nThe weapon can’t be knocked out of the wielder’s hand, and it automatically returns to the wielder when <LSTag Type=\"Spell\" Tooltip=\"Throw_Throw\">Thrown</LSTag>.":
        "Завдає психічної шкоди й має властивість <LSTag Tooltip=\"Thrown\">«Метальна»</LSTag>.\n\nЗброю неможливо вибити з руки власника; після <LSTag Type=\"Spell\" Tooltip=\"Throw_Throw\">метання</LSTag> вона автоматично повертається до нього.",
    "Whenever an ally takes damage from an interdicted creature, that interdicted creature takes necrotic damage equal to your proficiency bonus.":
        "Щоразу, коли союзник зазнає шкоди від істоти під забороною, та істота зазнає некротичної шкоди в кількості, що дорівнює вашому бонусу спеціалізації.",
    "Whenever you take radiant damage, your attacker takes force damage equal to their proficiency bonus.":
        "Щоразу, коли ви зазнаєте променевої шкоди, нападник зазнає силової шкоди в кількості, що дорівнює його бонусу спеціалізації.",
    "Avenger. Until the end of your next turn, any creature that hits the target with a melee attack roll takes Force damage equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die.":
        "Месник. До кінця вашого наступного ходу кожна істота, що влучає в ціль атакою ближнього бою, зазнає силової шкоди в кількості кидка вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>.",
    "The target is trapped in a dream, gaining no benefit from rest. When the target wakes up, it takes 3d6 Psychic damage.":
        "Ціль опиняється в пастці сновидіння й не отримує користі від відпочинку. Прокинувшись, вона зазнає 3d6 психічної шкоди.",
    "Whenever you take Radiant damage, your attacker takes fire damage equal to twice their own Proficiency Bonus.":
        "Щоразу, коли ви зазнаєте променевої шкоди, нападник зазнає вогняної шкоди в кількості, що вдвічі перевищує його бонус спеціалізації.",
})

EXACT_OVERRIDES.update({
    "You can rely on your knowledge to anticipate a monster’s actions and muster your best defense.\n\nWhenever a creature forces you to make a saving throw, you can add your Intelligence modifier to that saving throw.":
        "Спираючись на знання, ви передбачаєте дії чудовиськ і готуєте найкращий захист.\n\nЩоразу, коли істота змушує вас виконати кидок протидії, ви можете додати до нього свій модифікатор інтелекту.",
})

EXACT_OVERRIDES.update({
    "When you attack a creature and hit it with a weapon, you can deal an extra 2d6 Psychic damage. You can use this benefit only once per turn, you can use it a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Коли ви атакуєте істоту й влучаєте зброєю, то можете додатково завдати 2d6 психічної шкоди. Цю перевагу можна застосувати лише раз за хід; кількість її застосувань дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "You can cast <LSTag Type=\"Spell\" Tooltip=\"Target_AnimateDead\">Animate Dead</LSTag>, <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">Haste</LSTag>, and <LSTag Type=\"Spell\" Tooltip=\"Target_CallLightning\">Call Lightning</LSTag> once each per Long Rest.":
        "Ви можете по одному разу за довгий відпочинок проказати <LSTag Type=\"Spell\" Tooltip=\"Target_AnimateDead\">«Пробудження мерця»</LSTag>, <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">«Поспіх»</LSTag> і <LSTag Type=\"Spell\" Tooltip=\"Target_CallLightning\">«Заклик блискавки»</LSTag>.",
    "You can use this feature a number of times equal to your Charisma modifier (minimum of once), but you can use it no more than once per roll. You regain all expended uses when you finish a Long Rest.":
        "Кількість застосувань цієї особливості дорівнює вашому модифікатору харизми (щонайменше одне), але її можна застосувати не більш ніж раз до одного кидка. Усі витрачені застосування відновлюються після довгого відпочинку.",
    "Divine power guards your destiny. If you fail a saving throw or miss with an attack roll, you can roll 2d4 and add it to the total, possibly changing the outcome. Once you use this feature, you can’t use it again until you finish a short or long rest.":
        "Божественна сила оберігає вашу долю. Коли ви провалюєте кидок протидії або промахуєтеся кидком атаки, то можете кинути 2d4 й додати результат до кидка, можливо змінивши наслідок. Застосувавши цю особливість, ви не зможете зробити це знову до завершення короткого або довгого відпочинку.",
    """You gain one of the following feature options of your choice. Whenever you finish a Short or Long Rest, you can replace the chosen option with the other one.

Colossus Slayer
Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon, the weapon deals an extra 1d8 damage to the target if it’s missing any of its Hit Points. You can deal this extra damage only once per turn.

Horde Breaker
Once on each of your turns when you make an attack with a weapon, you can make another attack with the same weapon against a different creature that is within 5 feet of the original target, that is within the weapon’s range, and that you haven’t attacked this turn.""":
        """Виберіть один із таких варіантів особливості. Після кожного короткого або довгого відпочинку ви можете замінити вибраний варіант іншим.

Убивця колосів
Ваша завзятість виснажує навіть найстійкіших ворогів. Коли ви влучаєте в істоту зброєю, вона додатково завдає цілі 1d8 шкоди, якщо та втратила хоча б одне очко здоров’я. Цю додаткову шкоду можна завдати лише раз за хід.

Стримання навали
Один раз у кожен свій хід, коли ви атакуєте зброєю, то можете виконати ще одну атаку тією самою зброєю проти іншої істоти, яка перебуває в межах 5 футів від початкової цілі, у межах досяжності зброї та яку ви ще не атакували цього ходу.""",
    "As a Bonus Action, you transform into an avatar of your patron’s dreadful power, gaining the benefits below for 1 minute, until you have the Incapacitated condition, or until you end the form (no action required). You can transform a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Вторинною дією ви перетворюєтеся на втілення жахливої сили свого покровителя й отримуєте наведені нижче переваги на 1 хвилину, доки не набудете стану недієздатності або не припините подобу (дія не потрібна). Кількість перетворень дорівнює вашому модифікатору харизми (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
})

EXACT_OVERRIDES.update({
    "If you use Reckless Attack while your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> is active, you deal extra damage to the first target you hit on your turn with a Strength-based attack. To determine the extra damage, roll a number of d6s equal to your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag> Damage bonus, and add them together. The damage has the same type as the weapon or Unarmed Strike used for the attack.":
        "Якщо ви застосовуєте «Зухвалу атаку», поки триває ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, то завдаєте додаткової шкоди першій цілі, у яку влучаєте у свій хід атакою на основі сили. Щоб визначити додаткову шкоду, киньте стільки d6, скільки становить ваш бонус шкоди <LSTag Type=\"Status\" Tooltip=\"RAGE\">Люті</LSTag>, і додайте результати. Тип шкоди збігається з типом шкоди зброї або Удару голіруч, використаного для атаки.",
    "You harbor a wellspring of psionic energy within yourself, represented by your Psionic Energy Dice, which fuel certain powers granted by this subclass. As you gain Rogue levels, the number and size of these dice change: at 3rd level, you have four d6 dice; at 5th level, six d8 dice; at 9th level, eight d8 dice; and at 11th level, eight d10 dice.\n\nYou regain one of your expended Psionic Energy Dice when you finish a Short Rest, and you regain all of them when you finish a Long Rest.":
        "У вас вирує джерело псіонічної енергії, представлене кістками псіонічної енергії, які живлять сили цього підкласу. Зі зростанням рівня пройдисвіта змінюються кількість і розмір кісток: на 3-му рівні ви маєте чотири d6, на 5-му — шість d8, на 9-му — вісім d8, а на 11-му — вісім d10.\n\nОдну витрачену кістку псіонічної енергії ви відновлюєте після короткого відпочинку, а всі — після довгого.",
    "When you inspire an ally using <LSTag Type=\"Spell\" Tooltip=\"Target_BardicInspiration\">Bardic Inspiration</LSTag>, they also regain [1], equal to the result of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die.":
        "Коли ви надихаєте союзника за допомогою <LSTag Type=\"Spell\" Tooltip=\"Target_BardicInspiration\">Бардівського натхнення</LSTag>, він також відновлює [1] у кількості, що дорівнює результату кидка вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag>.",
    "Once per turn when you restore Hit Points to a creature with a spell, you can expend a <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die and increase the amount of Hit Points restored by a number equal to a roll of the Bardic Inspiration die. The creature’s Speed also increases by 10 feet until the end of its next turn.":
        "Один раз за хід, коли ви відновлюєте істоті очки здоров’я закляттям, то можете витратити кістку <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> й збільшити кількість відновлених очок на результат її кидка. Швидкість істоти також збільшується на 10 футів до кінця її наступного ходу.",
    "Beloved. The target regains Hit Points equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die plus your Charisma modifier.":
        "Коханий. Ціль відновлює очки здоров’я в кількості, що дорівнює результату кидка вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> + ваш модифікатор харизми.",
    "Sharpshooter. The target takes Force damage equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die plus your Charisma modifier.":
        "Снайпер. Ціль зазнає силової шкоди в кількості, що дорівнює результату кидка вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> + ваш модифікатор харизми.",
    "Wayfarer. The target gains Temporary Hit Points equal to a roll of your <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Bardic Inspiration</LSTag> die plus your Bard level. While the target has these Temporary Hit Points, its Speed increases by 10 feet.":
        "Мандрівник. Ціль отримує тимчасові очки здоров’я в кількості, що дорівнює результату кидка вашої кістки <LSTag Type=\"ActionResource\" Tooltip=\"BardicInspiration\">Бардівського натхнення</LSTag> + ваш рівень барда. Поки ціль має ці тимчасові очки, її швидкість збільшується на 10 футів.",
})

EXACT_OVERRIDES.update({
    """Whenever you finish a Long Rest, you choose one type of land: arid, polar, temperate, or tropical. Based on your choice, you consult the corresponding table and have all listed spells for your Druid level and lower prepared.

If you choose Arid Land, you have Blur, Burning Hands, and Fire Bolt prepared at 3rd level; Fireball at 5th level; Blight at 7th level; and Wall of Stone at 9th level.

If you choose Polar Land, you have Fog Cloud, Hold Person, and Ray of Frost prepared at 3rd level; Sleet Storm at 5th level; Ice Storm at 7th level; and Cone of Cold at 9th level.

If you choose Temperate Land, you have Misty Step, <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">Shocking Grasp</LSTag>, and Sleep prepared at 3rd level; Lightning Bolt at 5th level; Freedom of Movement at 7th level; and Tree Stride at 9th level.

If you choose Tropical Land, you have Acid Splash, Ray of Sickness, and Web prepared at 3rd level; Stinking Cloud at 5th level; Polymorph at 7th level; and Insect Plague at 9th level.""":
        """Після кожного довгого відпочинку виберіть один тип місцевості: посушливу, полярну, помірну чи тропічну. Ви маєте підготовленими всі закляття з відповідної таблиці, призначені для вашого або нижчого рівня друїда.

Посушлива місцевість: на 3-му рівні — «Розмиття», «Палючі руки» й «Вогняний заряд»; на 5-му — «Вогняна куля»; на 7-му — «Гниль»; на 9-му — «Стіна каменю».

Полярна місцевість: на 3-му рівні — «Хмара туману», «Утримання особи» й «Струмінь морозу»; на 5-му — «Хуртовина»; на 7-му — «Крижана буря»; на 9-му — «Конус холоду».

Помірна місцевість: на 3-му рівні — «Маревний крок», <LSTag Type="Spell" Tooltip="Target_ShockingGrasp">«Шоковий хват»</LSTag> і «Сон»; на 5-му — «Розряд блискавки»; на 7-му — «Свобода руху»; на 9-му — «Крок крізь дерева».

Тропічна місцевість: на 3-му рівні — «Кислотні бризки», «Струмінь хвороби» й «Павутина»; на 5-му — «Смердюча хмара»; на 7-му — «Перетворення»; на 9-му — «Комашина чума».""",
    "When you reach a Ranger level specified in the Fey Wanderer Spells table, you thereafter always have the listed spells prepared. At 3rd level, you always have Charm Person prepared; at 5th level, Misty Step; and at 9th level, Summon Fey.":
        "Досягнувши рівня слідопита, указаного в таблиці «Закляття фейського мандрівника», ви завжди маєте підготовленими відповідні закляття: на 3-му рівні — «Причарування особи», на 5-му — «Маревний крок», а на 9-му — «Прикликання феї».",
    "You can cast Misty Step without expending a spell slot. You can do so a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Ви можете проказувати «Маревний крок», не витрачаючи чарунки. Кількість таких застосувань дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    """The magic of your patron ensures that you always have certain spells ready. Upon reaching specific Warlock levels, you gain additional spells as shown in the Archfey Spells table, and you always have those spells prepared thereafter. 

At 3rd level, you gain Calm Emotions, Faerie Fire, Misty Step, Phantasmal Force, and Sleep. At 5th level, you gain Blink and Plant Growth. At 7th level, you gain Dominate Beast and <LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">Greater Invisibility</LSTag>. At 9th level, you gain Dominate Person and Seeming.""":
        """Магія покровителя гарантує, що ви завжди маєте напоготові певні закляття. На відповідних рівнях чаклуна ви отримуєте додаткові закляття з таблиці «Закляття Архіфеї», які завжди вважаються підготовленими.

На 3-му рівні ви отримуєте «Гамування емоцій», «Чарівний посвіт», «Маревний крок», «Примарну силу» й «Сон»; на 5-му — «Миготіння» та «Приріст рослин»; на 7-му — «Підкорення звіра» й <LSTag Type="Spell" Tooltip="Target_Invisibility_Greater">«Велику невидимість»</LSTag>; на 9-му — «Підкорення особи» та «Підміну».""",
    """You can expend a use of your Wild Shape as a Bonus Action to transform into a unique form: your Dragon Shape. While in this form, you become a Medium dragon that stands on all fours, but you retain your normal game statistics and senses.

When you assume Dragon Shape, you gain Temporary Hit Points equal to three times your Druid level. While in Dragon Shape, you can use claw attacks and a breath weapon. You gain a flying speed equal to twice your Speed, and you have Resistance to Acid, Cold, Fire, Lightning, and Poison damage.""":
        """Вторинною дією ви можете витратити одне застосування Дикої подоби й перетворитися на особливу Драконячу подобу. У ній ви стаєте драконом середнього розміру, що стоїть на чотирьох лапах, але зберігаєте звичайні ігрові показники й чуття.

Набуваючи Драконячої подоби, ви отримуєте тимчасові очки здоров’я в кількості, що втричі перевищує ваш рівень друїда. У цій подобі ви можете атакувати кігтями й користуватися дихальною зброєю. Ваша швидкість польоту вдвічі перевищує звичайну швидкість, а також ви маєте стійкість до кислотної, холодової, вогняної, блискавичної та отруйної шкоди.""",
    "You always have the Misty Step spell prepared. You can cast it by expending a use of your Channel Divinity rather than a spell slot. When you cast it in this way, you can choose a space within 30 feet of yourself that is occupied by a creature. If that creature is willing, you both teleport, swapping places; this effect fails if there isn’t enough room for you or the creature to teleport there.":
        "Ви завжди маєте підготовленим закляття «Маревний крок». Замість чарунки ви можете витратити одне застосування Божого наснаження, щоб проказати його. У такому разі ви можете вибрати простір у межах 30 футів, зайнятий істотою. Якщо істота згодна, ви телепортуєтеся й міняєтеся місцями; ефект не спрацьовує, якщо для вас або істоти бракує місця.",
    "Level 3: Improved Shillelagh":
        "Рівень 3: Покращена ґирлиґа",
    "Level 6: Shillelagh mastery":
        "Рівень 6: Майстерність ґирлиґи",
    "When you reach a Sorcerer level specified in the Frost Spells table, you thereafter always have the listed spells prepared. At 3rd level, you learn Blindness, Ice Knife, Misty Step, and Sleep. At 5th level, you add Sleet Storm and Slow. At 7th level, you gain Fire Shield and Ice Storm. Finally, at 9th level, you can cast Cone of Cold and Conjure Elemental.":
        "Досягнувши рівня чародія, указаного в таблиці «Морозні закляття», ви завжди маєте підготовленими відповідні закляття. На 3-му рівні ви вивчаєте «Сліпоту», «Льодяний ніж», «Маревний крок» і «Сон»; на 5-му — «Хуртовину» та «Сповільнення»; на 7-му — «Вогняний щит» і «Крижану бурю»; на 9-му — «Конус холоду» та «Прикликання елементаля».",
})

EXACT_OVERRIDES.update({
    "As a Bonus Action, you can make one attack with a weapon or an Unarmed Strike. You can use this Bonus Action a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a Short or Long Rest.":
        "Вторинною дією ви можете виконати одну атаку зброєю або Удар голіруч. Кількість застосувань цієї вторинної дії дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після короткого або довгого відпочинку.",
    "You magically transport yourself, reappearing amid a burst of moonlight. As a Bonus Action, you teleport up to [1] to an unoccupied space you can see. You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Ви магічно переноситеся й з’являєтеся у спалаху місячного сяйва. Вторинною дією ви телепортуєтеся на відстань до [1] у видимий вам вільний простір. Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "Primal forces now help fuel you on your journeys. As a Magic action, you can give yourself a number of Temporary Hit Points equal to 1d8 plus your Wisdom modifier (minimum of 1). You can use this action a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Первісні сили живлять вас у мандрах. Магічною дією ви можете отримати 1d8 + ваш модифікатор мудрості тимчасових очок здоров’я (щонайменше 1). Кількість застосувань цієї дії дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "As a Magic action, you can give yourself a number of Temporary Hit Points equal to 1d8 plus your Wisdom modifier (minimum of 1). You can use this action a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Магічною дією ви можете отримати 1d8 + ваш модифікатор мудрості тимчасових очок здоров’я (щонайменше 1). Кількість застосувань цієї дії дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    """You have mastered the art of creating fearsome ambushes, granting you the following benefits.

Ambusher’s Leap. At the start of your first turn of each combat, your Speed increases by [1] until the end of that turn.

Dreadful Strike. When you attack a creature and hit it with a weapon, you can deal an extra [2]. You can use this benefit only once per turn, you can use it a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.

Initiative Bonus. When you roll Initiative, you can add your Wisdom modifier to the roll.""":
        """Ви досконало опанували мистецтво страхітливих засідок і отримуєте такі переваги.

Стрибок із засідки. На початку вашого першого ходу в кожному бою швидкість збільшується на [1] до кінця цього ходу.

Жахливий удар. Коли ви атакуєте істоту й влучаєте зброєю, то можете додатково завдати [2]. Цю перевагу можна застосувати лише раз за хід; кількість її застосувань дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.

Бонус до ініціативи. Коли ви кидаєте ініціативу, то можете додати до кидка свій модифікатор мудрості.""",
    "You can use <LSTag Type=\"Spell\" Tooltip=\"Target_FlurryOfHealing\">Flurry of Healing</LSTag> and <LSTag Type=\"Spell\" Tooltip=\"Target_FlurryOfHarm\">Flurry of Harm</LSTag>.\n\nYou can use these benefits a total number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a Long Rest.":
        "Ви можете застосовувати <LSTag Type=\"Spell\" Tooltip=\"Target_FlurryOfHealing\">«Шквал зцілення»</LSTag> і <LSTag Type=\"Spell\" Tooltip=\"Target_FlurryOfHarm\">«Шквал шкоди»</LSTag>.\n\nЗагальна кількість застосувань обох переваг дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    """Your connection to the plane of absolute order allows you to equalize chaotic moments. When a creature you can see within 60 feet of yourself is about to roll a d20 with Advantage or Disadvantage, you can take a Reaction to prevent the roll from being affected by Advantage and Disadvantage.

You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.""":
        """Ваш зв’язок із планом абсолютного порядку дає змогу врівноважувати хаотичні миті. Коли видима вам істота в межах 60 футів збирається кинути d20 із перевагою чи завадою, ви можете застосувати реагування, щоб на кидок не впливали ані перевага, ані завада.

Кількість застосувань цієї особливості дорівнює вашому модифікатору харизми (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.""",
    "You can take the <LSTag Type=\"Spell\" Tooltip=\"Shout_Dash\">Dash</LSTag> action as a Bonus Action. When you do so, you gain a number of Temporary Hit Points equal to your Proficiency Bonus.\n\nYou can use this trait a number of times equal to your Proficiency Bonus, and you regain all expended uses when you finish a Short or Long Rest.":
        "Ви можете виконувати дію <LSTag Type=\"Spell\" Tooltip=\"Shout_Dash\">«Ривок»</LSTag> вторинною дією. У такому разі ви отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому бонусу спеціалізації.\n\nКількість застосувань цієї риси дорівнює вашому бонусу спеціалізації, а всі витрачені застосування відновлюються після короткого або довгого відпочинку.",
    "You can cast Sacred Flame as a Bonus Action a number of times equal to your Proficiency Bonus.":
        "Ви можете проказувати «Священний вогонь» вторинною дією. Кількість таких застосувань дорівнює вашому бонусу спеціалізації.",
    """As a Bonus Action, you invoke an elven magic called the Bladesong, provided you aren’t wearing armor or using a Shield.

The Bladesong lasts for 1 minute and ends early if you have the Incapacitated condition, if you don armor or a Shield, or if you use two hands to make an attack with a weapon. You can dismiss the Bladesong at any time (no action required).

You can invoke the Bladesong a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a Long Rest. You regain one expended use when you use Arcane Recovery.""":
        """Якщо ви не носите обладунків і не користуєтеся щитом, вторинною дією можете закликати ельфійську магію «Клинковий спів».

Клинковий спів триває 1 хвилину й завершується достроково, якщо ви набуваєте стану недієздатності, надягаєте обладунки чи щит або атакуєте зброєю обіруч. Ви можете припинити Клинковий спів будь-коли (дія не потрібна).

Кількість застосувань Клинкового співу дорівнює вашому модифікатору інтелекту (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку. Одне витрачене застосування також відновлюється, коли ви використовуєте Магічне відновлення.""",
    "You always have the Hunter’s Mark spell prepared. You can cast it a number of times equal to your Strength modifier (minimum of once), and you regain all expended uses when you finish a long rest.":
        "Ви завжди маєте підготовленим закляття «Мітка мисливця». Кількість його проказувань дорівнює вашому модифікатору сили (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    """When you or a creature you can see within 30 feet of you fails a saving throw, you can take a Reaction to add a bonus to the roll, potentially causing it to succeed. The bonus equals your Intelligence modifier (minimum of +1).

You can take this Reaction a number of times equal to your Intelligence modifier (minimum of once). You regain all expended uses when you finish a Long Rest.""":
        """Коли ви або видима вам істота в межах 30 футів провалюєте кидок протидії, ви можете застосувати реагування й додати до кидка бонус, можливо перетворивши невдачу на успіх. Бонус дорівнює вашому модифікатору інтелекту (щонайменше +1).

Кількість застосувань цього реагування дорівнює вашому модифікатору інтелекту (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.""",
    """You can use the hidden, magical pathways that some fey use to traverse space in the blink of an eye. As a bonus action on your turn, you can teleport up to 30 feet to an unoccupied space you can see. Alternatively, you can use your action to teleport one willing creature you touch up to 30 feet to an unoccupied space you can see.

You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.""":
        """Ви можете користуватися прихованими магічними шляхами, якими деякі феї миттєво долають відстань. Вторинною дією у свій хід ви можете телепортуватися на відстань до 30 футів у видимий вам вільний простір. Або ж дією можете телепортувати охочу істоту, якої торкаєтеся, на відстань до 30 футів у видимий вам вільний простір.

Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.""",
    "You can use this energy a number of times equal to your Intelligence modifier (minimum of once), but you can do so no more than once per turn. You regain all expended uses when you finish a Long Rest.":
        "Кількість застосувань цієї енергії дорівнює вашому модифікатору інтелекту (щонайменше одне), але не більш ніж одне за хід. Усі витрачені застосування відновлюються після довгого відпочинку.",
    "You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a long rest.":
        "Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне). Усі витрачені застосування відновлюються після довгого відпочинку.",
    "You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a Long Rest.":
        "Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне). Усі витрачені застосування відновлюються після довгого відпочинку.",
    "You always have Hunter’s Mark prepared. You can cast it without expending a spell slot a number of times equal to the value shown in the Favored Enemy column of the Ranger Features table. You regain all expended uses when you finish a Long Rest.":
        "Ви завжди маєте підготовленою «Мітку мисливця». Ви можете проказати її, не витрачаючи чарунки, стільки разів, скільки вказано у стовпці «Улюблений ворог» таблиці особливостей слідопита. Усі витрачені застосування відновлюються після довгого відпочинку.",
    """Hexblade's Curse. You can cast Hex without expending a spell slot a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest. When you cast Hex, a spectral weapon resembling your patron orbits the cursed target.

Hexblade's Maneuvers. Once per turn, when you hit a target cursed by your Hex with an attack roll, you can cause one of the following additional effects:

Draining Slash, Harrowing Blade, Stymying Mark""":
        """Прокляття відьомського клинка. Ви можете проказувати «Прокляття», не витрачаючи чарунки. Кількість застосувань дорівнює вашому модифікатору харизми (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку. Коли ви проказуєте «Прокляття», довкола проклятої цілі кружляє примарна зброя, подібна до вашого покровителя.

Маневри відьомського клинка. Один раз за хід, коли ви влучаєте атакою в ціль під дією вашого «Прокляття», то можете спричинити один із таких додаткових ефектів:

Виснажливий розтин, Болісний клинок, Сковувальна мітка""",
    "When you take damage from a target cursed by your Hex, you can take a Reaction to reduce that damage by 2d8 plus your Charisma modifier. You can use this feature a number of times equal to your Charisma modifier, and you regain all expended uses when you finish a Long Rest.":
        "Коли ви зазнаєте шкоди від цілі під дією вашого «Прокляття», то можете застосувати реагування й зменшити шкоду на 2d8 + ваш модифікатор харизми. Кількість застосувань цієї особливості дорівнює вашому модифікатору харизми, а всі витрачені застосування відновлюються після довгого відпочинку.",
    "You can cast Hex without expending a spell slot a number of times equal to your Charisma modifier (minimum of once), and you regain all expended uses when you finish a Long Rest.":
        "Ви можете проказувати «Прокляття», не витрачаючи чарунки. Кількість застосувань дорівнює вашому модифікатору харизми (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "You have absorbed primeval magic that gives you an echo of the might of giants. Once per turn, when you hit a target with a melee weapon attack or a ranged weapon attack using a thrown weapon, you can imbue the attack with an additional effect depending on the benefit you chose. You can use this feat a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.":
        "Ви увібрали первісну магію, що дарує відлуння могутності велетнів. Один раз за хід, коли ви влучаєте в ціль атакою зброєю ближнього бою або дистанційною атакою метальною зброєю, то можете наділити атаку додатковим ефектом відповідно до вибраної переваги. Кількість застосувань цієї риси дорівнює вашому бонусу спеціалізації, а всі витрачені застосування відновлюються після довгого відпочинку.",
    "As a bonus action, you can magically become invisible for 1 minute. You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a long rest.":
        "Вторинною дією ви можете магічно стати невидимим на 1 хвилину. Кількість застосувань цієї особливості дорівнює вашому модифікатору мудрості (щонайменше одне), а всі витрачені застосування відновлюються після довгого відпочинку.",
    "You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.":
        "Кількість застосувань цієї риси дорівнює вашому бонусу спеціалізації, а всі витрачені застосування відновлюються після довгого відпочинку.",
})

EXACT_OVERRIDES.update({
    """Your intense training bears fruit. You gain proficiency with martial weapons and training with medium armor.

Whenever you finish a Short Rest, you can perform a ritual on a melee weapon you are proficient with that deals Piercing or Slashing damage, sanctifying it. It becomes your sanctified blade, and you can only have one such blade at a time. The blade gains the Finesse property for you, and attacks made with it against Aberrations, Fiends, and Undead ignore Resistance to damage.""":
        """Наполегливі тренування дають плоди. Ви отримуєте володіння бойовою зброєю та вміння носити середні обладунки.

Після кожного короткого відпочинку ви можете провести ритуал над зброєю ближнього бою, якою володієте та яка завдає колотої або рубаної шкоди, освятивши її. Вона стає вашим освяченим клинком; одночасно ви можете мати лише один такий клинок. Для вас клинок набуває властивості «Фехтувальна», а атаки ним проти покручів, нечисті й невмерлих ігнорують стійкість до шкоди.""",
    "The gods of the forge are patrons of artisans who work with metal, from a humble blacksmith who keeps a village in horseshoes and plow blades to the mighty elf artisan whose diamond-tipped arrows of mithral have felled demon lords. The gods of the forge teach that, with patience and hard work, even the most intractable metal can be transformed from a lump of ore to a beautifully wrought object. Clerics of these deities search for objects lost to the forces of darkness, liberate mines overrun by orcs, and uncover rare and wondrous materials necessary to create potent magic items. Followers of these gods take great pride in their work, and they are willing to craft and use heavy armor and powerful weapons to protect them. Deities of this domain include Gond, Reorx, Onatar, Moradin, Hephaestus, and Goibhniu.":
        "Боги кузні опікуються майстрами металу — від скромного коваля, що постачає село підковами й лемешами, до могутнього ельфійського ремісника, чиї мітралові стріли з діамантовими вістрями валили володарів демонів. Боги кузні навчають, що терпінням і важкою працею навіть найнепіддатливіший метал можна перетворити з грудки руди на прекрасний виріб. Клірики цих божеств розшукують речі, втрачені через сили темряви, звільняють захоплені орками копальні та знаходять рідкісні дивовижні матеріали, потрібні для створення могутніх магічних предметів. Послідовники цих богів пишаються своєю працею й охоче кують та використовують важкі обладунки й потужну зброю для власного захисту. До божеств цього домену належать Ґонд, Реоркс, Онатар, Морадін, Гефест і Ґойбніу.",
})

EXACT_OVERRIDES.update({
    "Thaumaturge: You know one extra cantrip from the Cleric spell list. In addition, your mystical connection to the divine gives you a bonus to your Intelligence (<LSTag Type=\"Skills\" Tooltip=\"Arcana\">Arcana</LSTag> or <LSTag Type=\"Skills\" Tooltip=\"Religion\">Religion</LSTag>) checks. The bonus equals your Wisdom modifier (minimum of +1).":
        "Чудотворець. Ви знаєте одне додаткове замовляння зі списку заклять клірика. Крім того, містичний зв’язок із божественним дає вам бонус до перевірок інтелекту (<LSTag Type=\"Skills\" Tooltip=\"Arcana\">Таїнства</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Religion\">Релігія</LSTag>). Бонус дорівнює вашому модифікатору мудрості (щонайменше +1).",
    "When you activate your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag>, you gain a number of Temporary Hit Points equal to your Barbarian level.":
        "Коли ви входите в <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, то отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому рівню варвара.",
    "Once per turn when you hit a creature with an Unarmed Strike and deal damage, you can expend 1 Focus Point to deal extra Necrotic damage equal to one roll of your Martial Arts die plus your Wisdom modifier.":
        "Один раз за хід, коли ви влучаєте в істоту Ударом голіруч і завдаєте шкоди, то можете витратити 1 очко зосередження й додатково завдати некротичної шкоди в кількості кидка вашої кістки бойових мистецтв + ваш модифікатор мудрості.",
    "Whenever you make a Charisma check, you gain a bonus to the check equal to your Wisdom modifier.":
        "Щоразу, коли ви виконуєте перевірку харизми, то отримуєте бонус до неї в кількості, що дорівнює вашому модифікатору мудрості.",
    "Your link to your patron allows you to serve as a conduit for radiant energy. You have Resistance to Radiant damage. Once per turn, when a spell you cast deals Radiant or Fire damage, you can add your Charisma modifier to that spell’s damage against one of the spell’s targets.":
        "Зв’язок із покровителем перетворює вас на провідник променевої енергії. Ви маєте стійкість до променевої шкоди. Один раз за хід, коли проказане вами закляття завдає променевої або вогняної шкоди, ви можете додати свій модифікатор харизми до шкоди цього закляття проти однієї з його цілей.",
    "If a creature within 10 feet of you is reduced to 0 Hit Points by someone other than you, you gain Temporary Hit Points equal to your Charisma modifier plus your Warlock level (minimum of 1 Temporary Hit Point).":
        "Якщо хтось інший знижує до 0 очки здоров’я істоти в межах 10 футів від вас, ви отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому модифікатору харизми + ваш рівень чаклуна (щонайменше 1 очко).",
    "When you use your Second Wind to regain Hit Points, you can choose a number of allies within a 30-foot emanation originating from you, up to a number of allies equal to your Charisma modifier. Each of those allies regains Hit Points equal to 1d10 + your Fighter level.":
        "Коли ви застосовуєте «Другий подих», щоб відновити очки здоров’я, то можете вибрати союзників у 30-футовій еманації від вас у кількості, що не перевищує вашого модифікатора харизми. Кожен із них відновлює 1d10 + ваш рівень бійця очок здоров’я.",
    "When you use your Action Surge, you can choose a number of allies within a 30-foot emanation originating from you, up to a number of allies equal to your Charisma modifier. Each of those allies gains the benefit of Action Surge.":
        "Коли ви застосовуєте Внутрішній резерв, то можете вибрати союзників у 30-футовій еманації від вас у кількості, що не перевищує вашого модифікатора харизми. Кожен із них також отримує перевагу Внутрішнього резерву.",
    "When you take damage, you can take a Reaction to roll 1d12. Add your Constitution modifier to the number rolled and reduce the damage by that total.":
        "Коли ви зазнаєте шкоди, то можете застосувати реагування й кинути 1d12. Додайте до результату свій модифікатор статури й зменште шкоду на отриману суму.",
    "You use your Charisma modifier in place of Strength or Dexterity for attack and damage rolls you make with melee weapons.":
        "Для кидків атаки й шкоди зброєю ближнього бою ви використовуєте модифікатор харизми замість сили чи спритності.",
    "You are immune to the charmed condition. When you make a Charisma check, you can expend a seal to treat a d20 roll of 9 or lower as a 10.":
        "Ви маєте імунітет до стану причарування. Виконуючи перевірку харизми, ви можете витратити печатку й вважати результат 9 або менше на d20 за 10.",
    "Asmodeus’s secrets allow you to infuse your seals with manifest power. When you burn one or more seals to deal damage to a creature, you can activate this boon (no action required) to add your Charisma modifier (minimum of 1) to each seal’s damage roll.":
        "Таємниці Асмодея дають змогу наповнювати печатки явленою силою. Коли ви спалюєте одну чи кілька печаток, щоб завдати істоті шкоди, то можете активувати цей дар (дія не потрібна) й додати свій модифікатор харизми (щонайменше 1) до кидка шкоди кожної печатки.",
    "Your skin takes on a faintly ice-like, crystalline glow. Your Hit Point maximum increases by 3, and it increases by 1 whenever you gain another Sorcerer level. In addition, Difficult Terrain composed of ice or snow doesn’t cost you extra movement, and when you walk on ice, you only spend 1 foot of movement for every 2 feet you move.":
        "Ваша шкіра набуває слабкого крижаного кристалічного блиску. Максимум очок здоров’я збільшується на 3 й надалі ще на 1 з кожним рівнем чародія. Крім того, складний рельєф із льоду чи снігу не потребує додаткових витрат руху, а під час ходіння по льоду кожен 1 фут руху дає змогу переміститися на 2 фути.",
    "When you deal Cold damage to a Large or smaller creature with a spell, you can attempt to freeze it in place. If you do, that creature’s speed is reduced by 15 feet. When you deal Cold damage with a spell, you add your Charisma modifier to the damage. You have Resistance to Cold damage.":
        "Коли ви завдаєте закляттям холодової шкоди істоті великого або меншого розміру, то можете спробувати приморозити її до місця, зменшивши швидкість на 15 футів. Завдаючи холодової шкоди закляттям, ви додаєте до неї свій модифікатор харизми. Ви маєте стійкість до холодової шкоди.",
    "Stone’s Endurance (Stone Giant). When you take damage, you can take a Reaction to roll 1d12. Add your Constitution modifier to the number rolled and reduce the damage by that total.":
        "Кам’яна витривалість (кам’яний велетень). Коли ви зазнаєте шкоди, то можете застосувати реагування й кинути 1d12. Додайте до результату свій модифікатор статури й зменште шкоду на отриману суму.",
    "Your mental power increases, allowing you to project a sense of calm in a 10-foot Emanation that originates from you. The projection is inactive if you have the Incapacitated condition.\n\nYou and your allies in the projection gain a +2 bonus to Intelligence, Wisdom, and Charisma saving throws.":
        "Ваша сила розуму зростає, даючи змогу випромінювати спокій у 10-футовій еманації від вас. Проєкція не діє, якщо ви маєте стан недієздатності.\n\nВи й ваші союзники в межах проєкції отримуєте бонус +2 до кидків протидії інтелектом, мудрістю та харизмою.",
    "When you make an Intelligence (<LSTag Type=\"Skills\" Tooltip=\"History\">History</LSTag> or <LSTag Type=\"Skills\" Tooltip=\"Religion\">Religion</LSTag>) or Wisdom (<LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>) check, you gain a bonus to the roll equal to your Wisdom modifier.":
        "Коли ви виконуєте перевірку інтелекту (<LSTag Type=\"Skills\" Tooltip=\"History\">Історія</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Religion\">Релігія</LSTag>) чи мудрості (<LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag>), то отримуєте бонус до кидка в кількості, що дорівнює вашому модифікатору мудрості.",
    "After you take the Attack action with your sanctified blade, you can take a Bonus Action and expend 1 Divine Point to make an additional attack with it, gaining a bonus to the attack roll equal to your Wisdom modifier (minimum 1).":
        "Після виконання дії «Атака» освяченим клинком ви можете вторинною дією витратити 1 божественне очко й виконати ним додаткову атаку, отримавши бонус до кидка атаки в кількості вашого модифікатора мудрості (щонайменше 1).",
    "You can take a Bonus Action and expend 1 Divine Point to make an additional attack with it, gaining a bonus to the attack roll equal to your Wisdom modifier (minimum 1).":
        "Вторинною дією ви можете витратити 1 божественне очко й виконати ним додаткову атаку, отримавши бонус до кидка атаки в кількості вашого модифікатора мудрості (щонайменше 1).",
    "As a Reaction when a creature damages you with a melee attack, you can expend 1 Divine Point to make a melee attack against it. You gain a bonus to the damage roll equal to your Wisdom modifier.":
        "Коли істота завдає вам шкоди атакою ближнього бою, ви можете реагуванням витратити 1 божественне очко й атакувати її в ближньому бою. Ви отримуєте бонус до кидка шкоди в кількості, що дорівнює вашому модифікатору мудрості.",
    "Until you leave the form, your AC equals 13 plus your Wisdom modifier if that total is higher than the Beast’s AC.":
        "Доки ви не залишите подобу, ваш РЗ дорівнює 13 + ваш модифікатор мудрості, якщо ця сума перевищує РЗ звіра.",
})

EXACT_OVERRIDES.update({
    "You can channel lunar magic when you assume a Wild Shape form, granting you the benefits below.\n\nArmor Class: Until you leave the form, your AC equals 13 plus your Wisdom modifier if that total is higher than the Beast’s AC.\n\nTemporary Hit Points: You gain a number of Temporary Hit Points equal to three times your Druid level.":
        "Коли ви набуваєте Дикої подоби, то можете спрямувати місячну магію й отримати такі переваги.\n\nРівень захисту. Доки ви не залишите подобу, ваш РЗ дорівнює 13 + ваш модифікатор мудрості, якщо ця сума перевищує РЗ звіра.\n\nТимчасові очки здоров’я. Ви отримуєте тимчасові очки здоров’я в кількості, що втричі перевищує ваш рівень друїда.",
    "While in a Wild Shape form, you gain the following benefits.\n\nLunar Radiance. Each of your attacks in a Wild Shape form can deal its normal damage type or Radiant damage. You make this choice each time you hit with those attacks.\n\nIncreased Toughness. You can add your Wisdom modifier to your Constitution saving throws.":
        "Перебуваючи в Дикій подобі, ви отримуєте такі переваги.\n\nМісячне сяйво. Кожна ваша атака в Дикій подобі може завдавати шкоди звичайного типу або променевої шкоди. Ви вибираєте тип щоразу, коли влучаєте такою атакою.\n\nПідвищена витривалість. Ви можете додавати свій модифікатор мудрості до кидків протидії статурою.",
    "You’ve learned secrets from various magical traditions. Whenever you reach a Bard level (including this level) and the Prepared Spells number in the Bard Features table increases, you can choose any of your new prepared spells from the Bard, Cleric, Druid, and Wizard spell lists, and the chosen spells count as Bard spells for you (see a class’s section for its spell list). In addition, whenever you replace a spell prepared for this class, you can replace it with a spell from those lists.":
        "Ви опанували таємниці різних магічних традицій. Щоразу, коли з отриманням рівня барда (зокрема цього) у таблиці особливостей барда зростає кількість підготовлених заклять, ви можете вибрати нові підготовлені закляття зі списків барда, клірика, друїда чи чарівника. Вибрані закляття вважаються для вас закляттями барда (списки наведено в розділах відповідних класів). Крім того, замінюючи підготовлене закляття цього класу, ви можете вибрати заміну з будь-якого з цих списків.",
    "Two Cantrips. You learn two cantrips of your choice from the Cleric, Druid, or Wizard spell lists. When you select this feat, choose Intelligence, Wisdom, or Charisma as your spellcasting ability for these spells.\n\nLevel 1 Spell. Choose one 1st-level spell from the same list you selected for your cantrips. You always have this spell prepared, and you gain one 1st-level spell slot to cast it.":
        "Два замовляння. Ви вивчаєте два замовляння на свій вибір зі списку заклять клірика, друїда чи чарівника. Вибираючи цю рису, визначте інтелект, мудрість або харизму базовою характеристикою проказування цих заклять.\n\nЗакляття 1-го рівня. Виберіть одне закляття 1-го рівня з того самого списку, з якого вибрали замовляння. Ви завжди маєте це закляття підготовленим і отримуєте одну чарунку 1-го рівня для його проказування.",
    "When you reach certain Sorcerer levels specified in the Psionic Spells table, you always have the listed spells prepared.\n\nAt Sorcerer level 3, you have Arms of Hadar, Calm Emotions, Detect Thoughts, Dissonant Whispers, and Mind Sliver prepared. At level 5, you additionally have Hunger of Hadar prepared. At level 7, you gain Evard’s Black Tentacles. At level 9, you gain Telekinesis, all of which are always prepared.":
        "На рівнях чародія, указаних у таблиці «Псіонічні закляття», ви отримуєте закляття, які надалі завжди вважаються підготовленими.\n\nНа 3-му рівні — «Руки Гадара», «Гамування емоцій», «Виявлення думок», «Нерозбірливий шепіт» і «Скалка розуму»; на 5-му — «Голод Гадара»; на 7-му — «Чорні мацаки Еварда»; на 9-му — «Телекінез».",
    "When you reach certain Sorcerer levels specified in the Clockwork Spells table, you always have the listed spells prepared. At Sorcerer level 3, you have Aid, Cure Wounds, Lesser Restoration, and Protection from Evil and Good prepared. At level 5, you additionally have Dispel Magic and Protection from Energy prepared. At level 7, you gain Freedom of Movement. At level 9, you gain Greater Restoration, all of which are always prepared.":
        "На рівнях чародія, указаних у таблиці «Заводні закляття», ви отримуєте закляття, які надалі завжди вважаються підготовленими. На 3-му рівні — «Поміч», «Зцілення ран», «Мале відновлення» та «Захист від зла й добра»; на 5-му — «Розвіяння чарів» і «Захист від енергії»; на 7-му — «Свобода руху»; на 9-му — «Велике відновлення».",
    "You gain a bonus to Constitution saving throws equal to your Wisdom modifier (minimum of +1).\n\nIn addition, once per turn when you hit a creature with an attack roll while you are transformed using <LSTag Type=\"Passive\" Tooltip=\"HollowWarden_3_WrathOfTheWild\">Wrath of the Wild</LSTag>, you regain a number of Hit Points equal to 1d10 plus your Wisdom modifier, provided you are Bloodied when you hit.":
        "Ви отримуєте бонус до кидків протидії статурою в кількості, що дорівнює вашому модифікатору мудрості (щонайменше +1).\n\nКрім того, один раз за хід, коли під дією <LSTag Type=\"Passive\" Tooltip=\"HollowWarden_3_WrathOfTheWild\">«Гніву дикої природи»</LSTag> ви влучаєте в істоту атакою, то відновлюєте 1d10 + ваш модифікатор мудрості очок здоров’я, якщо на мить влучання ви закривавлені.",
    "Your dedication to wild eldritch beings alters you further. When transformed using <LSTag Type=\"Passive\" Tooltip=\"HollowWarden_3_WrathOfTheWild\">Wrath of the Wild</LSTag>, you gain the following additional benefits.\n\nMenacing Aura. When a creature fails its saving throw against your <LSTag Type=\"Status\" Tooltip=\"UNNERVING_AURA\">Unnerving Aura</LSTag>, it also can’t regain Hit Points or take Reactions until the start of your next turn.\n\nOminous Strikes. When you hit a creature that has the Frightened condition with an attack roll, that attack deals extra damage equal to your Wisdom modifier.":
        "Відданість диким потойбічним істотам змінює вас іще більше. Перетворившись за допомогою <LSTag Type=\"Passive\" Tooltip=\"HollowWarden_3_WrathOfTheWild\">«Гніву дикої природи»</LSTag>, ви отримуєте такі додаткові переваги.\n\nЗагрозлива аура. Істота, яка провалює кидок протидії проти вашої <LSTag Type=\"Status\" Tooltip=\"UNNERVING_AURA\">Бентежної аури</LSTag>, також не може відновлювати очки здоров’я чи застосовувати реагування до початку вашого наступного ходу.\n\nЗловісні удари. Коли ви влучаєте атакою в істоту зі станом переляку, атака додатково завдає шкоди в кількості, що дорівнює вашому модифікатору мудрості.",
    "When you reach a Sorcerer level specified in the Shadow Spells table, you thereafter always have the listed spells prepared. Shadow Magic sorcerers gain additional spells at certain levels: <LSTag Type=\"Spell\" Tooltip=\"Target_Bane\">Bane</LSTag>, Darkness, Inflict Wounds, and Pass Without Trace at 3rd level; Hunger of Hadar and Fear at 5th level; <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Greater Invisibility</LSTag> and Phantasmal Killer at 7th level; and <LSTag Type=\"Spell\" Tooltip=\"Target_Contagion\">Contagion</LSTag> and Cloudkill at 9th level.":
        "На рівнях чародія, указаних у таблиці «Тіньові закляття», ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — <LSTag Type=\"Spell\" Tooltip=\"Target_Bane\">«Бейн»</LSTag>, «Пітьма», «Завдання ран» і «Безслідна хода»; на 5-му — «Голод Гадара» та «Страх»; на 7-му — <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">«Велика невидимість»</LSTag> і «Примарний убивця»; на 9-му — <LSTag Type=\"Spell\" Tooltip=\"Target_Contagion\">«Зараза»</LSTag> та «Убивча хмара».",
    "When you reach certain Sorcerer levels, you always have the following spells prepared: Green-Flame Blade, True Strike, Heroism, Magic Weapon, Mirror Image, and Shield at level 3; <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">Haste</LSTag> and Phantom Steed at level 5; Death Ward and Stoneskin at level 7; and Hold Monster at level 9. These spells don't count against the number of spells you can prepare.":
        "На певних рівнях чародія ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — «Клинок зеленого полум’я», «Певний удар», «Героїзм», «Магічна зброя», «Віддзеркалення» та «Щит»; на 5-му — <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">«Поспіх»</LSTag> і «Примарний скакун»; на 7-му — «Оберіг від смерті» та «Кам’яна шкіра»; на 9-му — «Утримання чудовиська». Ці закляття не враховуються до кількості заклять, які ви можете підготувати.",
    "Your link to the divine allows you to learn spells from the Cleric class. Each time you reach Sorcerer level 3, 5, 7, and 9, you learn additional spells from the Cleric spell list. They become Sorcerer spells for you, but they don’t count against the number of Sorcerer spells you know.\n\nLevel 3: two <LSTag Tooltip=\"Cantrip\">cantrips</LSTag>, two Level 1 spells, and two Level 2 spells.\nLevel 5: two Level 3 spells.\nLevel 7: two Level 4 spells.\nLevel 9: two Level 5 spells.":
        "Ваш зв’язок із божественним дає змогу вивчати закляття клірика. На 3-му, 5-му, 7-му та 9-му рівнях чародія ви вивчаєте додаткові закляття зі списку клірика. Для вас вони вважаються закляттями чародія, але не враховуються до кількості відомих вам заклять чародія.\n\nРівень 3: два <LSTag Tooltip=\"Cantrip\">замовляння</LSTag>, два закляття 1-го рівня й два закляття 2-го рівня.\nРівень 5: два закляття 3-го рівня.\nРівень 7: два закляття 4-го рівня.\nРівень 9: два закляття 5-го рівня.",
})

EXACT_OVERRIDES.update({
    "You can use musical notes or words of power to disrupt mind-influencing effects. If you or a creature within 30 feet of you fails a saving throw against an effect that applies the Charmed or Frightened condition, you can take a Reaction to cause the save to be rerolled, and the new roll has Advantage.":
        "Ви можете музичними нотами чи словами сили руйнувати впливи на розум. Коли ви або істота в межах 30 футів від вас провалює кидок протидії ефекту, що спричиняє стан причарування чи переляку, ви можете реагуванням дати цій істоті повторити кидок із перевагою.",
    "If the target is Large or smaller, it must succeed on a Dexterity saving throw or have the Prone condition.":
        "Якщо ціль великого або меншого розміру, вона має успішно виконати кидок протидії спритністю, інакше набуває стану повалення.",
    "Your eyes briefly become pools of darkness, and flightless wings sprout from your back temporarily. Creatures other than your allies within 10 feet of you must succeed on a Charisma saving throw or have the Frightened condition until the end of your next turn.":
        "Ваші очі на мить стають темними безоднями, а зі спини виростають тимчасові нелітаючі крила. Усі істоти, крім ваших союзників, у межах 10 футів від вас мають успішно виконати кидок протидії харизмою, інакше набувають стану переляку до кінця вашого наступного ходу.",
    "When you hit a Large or smaller creature with an attack roll and deal damage to it, you can give that target the Prone condition.":
        "Коли ви влучаєте атакою в істоту великого або меншого розміру й завдаєте їй шкоди, то можете надати цілі стан повалення.",
    "You are used to being aboard rocking ships and other vehicles. You have Advantage on all Strength and Dexterity saving throws and checks to avoid being pushed, having the Prone condition, or otherwise being moved against your will.":
        "Ви звикли до хитавиці на кораблях та інших засобах пересування. Ви маєте перевагу в усіх перевірках і кидках протидії силою та спритністю, щоб уникнути штовхання, стану повалення чи іншого примусового переміщення.",
    "Hill’s Tumble (Hill Giant). When you hit a Large or smaller creature with an attack roll and deal damage to it, you can give that target the Prone condition.":
        "Пагорбовий перекид (пагорбовий велетень). Коли ви влучаєте атакою в істоту великого або меншого розміру й завдаєте їй шкоди, то можете надати цілі стан повалення.",
    "Coward. The target and each creature of your choice in a 30-foot Emanation originating from the target must succeed on a Wisdom saving throw or have the Frightened condition until the start of your next turn. While a creature is Frightened, its Speed is halved (round down), and it can take either an action or a Bonus Action, not both.":
        "Боягуз. Ціль і кожна вибрана вами істота в 30-футовій еманації від неї мають успішно виконати кидок протидії мудрістю, інакше набувають стану переляку до початку вашого наступного ходу. Швидкість наляканої істоти зменшується вдвічі (з округленням униз), і вона може виконати або дію, або вторинну дію, але не обидві.",
    "You have the Frightened condition until the end of your next turn.":
        "Ви перебуваєте в стані переляку до кінця свого наступного ходу.",
    "You gain a stoic confidence that bolsters your resolve. You are immune to the Frightened condition. This benefit is inactive while you have the Incapacitated condition.":
        "Стоїчна впевненість зміцнює вашу рішучість. Ви маєте імунітет до стану переляку. Ця перевага не діє, поки ви перебуваєте в стані недієздатності.",
    "You are immune to the Frightened condition.":
        "Ви маєте імунітет до стану переляку.",
    "Dragon's Terror. You can take a Magic action to instill terror in a creature you can see within 30 feet of yourself. The target must succeed on a Wisdom saving throw or have the Frightened condition until the end of your next turn.\n\nInspired by Fear. When you cause a creature to gain the Frightened condition and you are the source of its fear, you gain <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Heroic Inspiration</LSTag>. Once you use this benefit, you can’t use it again until you finish a Short or Long Rest.":
        "Жах дракона. Магічною дією ви вселяєте жах у видиму істоту в межах 30 футів. Ціль має успішно виконати кидок протидії мудрістю, інакше набуває стану переляку до кінця вашого наступного ходу.\n\nНатхнення страхом. Коли через вас істота набуває стану переляку, ви отримуєте <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Героїчне натхнення</LSTag>. Скориставшись цією перевагою, ви не зможете застосувати її знову до завершення короткого чи тривалого відпочинку.",
    "Your scales harden. While you aren’t wearing armor, you can calculate your AC as 13 + your Dexterity modifier. You can use a shield and still gain this benefit.\n\nYou grow retractable claws from the tips of your fingers. Extending or retracting the claws requires no action. The claws are natural weapons, which you can use to make unarmed strikes. When you hit with an unarmed strike using these claws, the attack deals an additional 1d4 slashing damage.":
        "Ваша луска твердне. Поки ви не носите обладунків, ваш РЗ дорівнює 13 + ваш модифікатор спритності. Щит не позбавляє вас цієї переваги.\n\nНа кінчиках ваших пальців виростають утяжні кігті. Випускати чи втягувати їх можна без дії. Кігті є природною зброєю, якою ви можете виконувати удари голіруч. Влучивши таким ударом, ви додатково завдаєте 1d4 рубаної шкоди.",
    "Increase your walking speed by 5 feet.\nYou gain proficiency in the <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Acrobatics</LSTag> or <LSTag Type=\"Skills\" Tooltip=\"Athletics\">Athletics</LSTag> skill (your choice).\nYou have advantage on any Strength (Athletics) or Dexterity (Acrobatics) check you make to escape from being restrained.":
        "Ваша швидкість ходьби збільшується на 5 футів.\nВи отримуєте спеціалізацію в <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Акробатиці</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Athletics\">Атлетиці</LSTag> на свій вибір.\nВи маєте перевагу в перевірках сили (Атлетика) чи спритності (Акробатика), які виконуєте, щоб звільнитися зі стану знерухомлення.",
    "Ice rimes you and your prey, protecting you and hindering them. When you cast Hunter’s Mark, you gain Temporary Hit Points equal to 1d10 plus your Ranger level.\n\nAdditionally, while a creature is marked by your Hunter’s Mark, it can’t take the Disengage action.":
        "Крига огортає вас і вашу здобич, захищаючи вас та сковуючи її. Коли ви проказуєте «Знак мисливця», ви отримуєте 1d10 + ваш рівень слідопита тимчасових очок здоров’я.\n\nКрім того, позначена вашим «Знаком мисливця» істота не може виконувати дію «Відступ».",
    "At 3rd level, you gain the Winter Walker Spells feature. The magic of your path ensures you always have certain spells prepared; when you reach specific Ranger levels, you automatically have the associated spells prepared. At 3rd level, you have Ice Knife prepared, at 5th level you gain Hold Person, and at 9th level you gain Remove Curse.":
        "На 3-му рівні ви отримуєте особливість «Закляття зимового мандрівника». Магія вашого шляху завжди тримає певні закляття підготовленими: на 3-му рівні — «Льодяний ніж», на 5-му — «Утримання особи», а на 9-му — «Зняття прокляття».",
    "The magic of your patron ensures that you always have certain spells ready. When you reach specific Warlock levels, you automatically have the associated spells prepared.\n\nAt Warlock level 3, you always have Aid, Cure Wounds, Guiding Bolt, Lesser Restoration, Light, and Sacred Flame prepared. At level 5, you additionally have Daylight and Revivify prepared. At level 7, you gain Guardian of Faith and Wall of Fire. At level 9, you gain Greater Restoration.":
        "Магія вашого покровителя завжди тримає певні закляття підготовленими. На 3-му рівні чаклуна це «Поміч», «Зцілення ран», «Вказівний заряд», «Мале відновлення», «Світло» та «Священний вогонь»; на 5-му — також «Денне світло» й «Оживлення»; на 7-му — «Страж віри» та «Стіна вогню»; на 9-му — «Велике відновлення».",
    "When you aren’t wearing any armor, your base Armor Class equals 10 plus your Dexterity and Charisma modifiers. You can use a Shield and still gain this benefit.\n\nYou also gain proficiency in one of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Acrobatics</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Intimidation</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Performance</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>.":
        "Поки ви не носите обладунків, ваш базовий РЗ дорівнює 10 + ваші модифікатори спритності й харизми. Щит не позбавляє вас цієї переваги.\n\nВи також отримуєте спеціалізацію в одній навичці на свій вибір: <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Акробатика</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Intimidation\">Залякування</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Артистичність</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag>.",
    "You can attack twice instead of once whenever you take the Attack action on your turn.\n\nIn addition, you can cast one of your cantrips that has a casting time of an action in place of one of those attacks.":
        "Виконуючи у свій хід дію «Атака», ви можете атакувати двічі замість одного разу.\n\nКрім того, одну з цих атак можна замінити проказуванням замовляння, час проказування якого становить одну дію.",
    "You can attack three times instead of once whenever you take the Attack action on your turn.\n\nIn addition, you can cast one of your cantrips that has a casting time of an action in place of one of those attacks.":
        "Виконуючи у свій хід дію «Атака», ви можете атакувати тричі замість одного разу.\n\nКрім того, одну з цих атак можна замінити проказуванням замовляння, час проказування якого становить одну дію.",
    "You can cast one of your cantrips that has a casting time of an action in place of one of those attacks.":
        "Одну з цих атак можна замінити проказуванням замовляння, час проказування якого становить одну дію.",
    "Warlock cantrips that deal damage and have a range have their range increased by 1.5 times when you cast them.":
        "Коли ви проказуєте замовляння чаклуна, що завдає шкоди й має дальність, його дальність збільшується в півтора раза.",
    "Can use a reaction to make a weapon attack or cast a damage-dealing cantrip with a casting time of 1 action.":
        "Може реагуванням атакувати зброєю або проказати замовляння, яке завдає шкоди й має час проказування 1 дія.",
    "Once on each of your turns, you can cast one of your illrigger cantrips in place of one of your attacks granted by your Extra Attack feature.":
        "Один раз протягом кожного свого ходу ви можете замінити одну з атак, наданих особливістю «Додаткова атака», проказуванням одного зі своїх замовлянь ілріґера.",
    "When you take the Attack action on your turn, you can replace one of the attacks with a casting of one of your Druid cantrips that has a casting time of an action.":
        "Коли ви виконуєте у свій хід дію «Атака», то можете замінити одну з атак проказуванням замовляння друїда, час проказування якого становить одну дію.",
    "You know the Light cantrip.":
        "Ви знаєте замовляння «Світло».",
    "Choose three cantrips. The cantrips can be from any class’s spell list, you have the chosen spells prepared, and they function as Warlock spells for you.":
        "Виберіть три замовляння зі списку заклять будь-якого класу. Вибрані замовляння завжди підготовлені й вважаються для вас закляттями чаклуна.",
    "Scroll of Shillelagh":
        "Сувій Ґирлиґи",
    "Primal Strike. Once on each of your turns when you hit a creature with an attack roll using a weapon or a Beast form’s attack in Wild Shape, you can cause the target to take an extra [1].":
        "Первісний удар. Один раз протягом кожного свого ходу, коли ви влучаєте в істоту зброєю чи атакою звіриної форми в Дикій подобі, то можете додатково завдати цілі [1].",
    "Magic Initiate (Cleric): You have learned two cantrips. Well chosen.":
        "Магічний хист (клірик): ви вивчили два замовляння. Гарний вибір.",
    "Magic Initiate (Cleric): You have learned the selected cantrip.":
        "Магічний хист (клірик): ви вивчили вибране замовляння.",
    "Magic Initiate (Druid): You have learned two cantrips. Well chosen.":
        "Магічний хист (друїд): ви вивчили два замовляння. Гарний вибір.",
    "Magic Initiate (Druid): You have learned the selected cantrip.":
        "Магічний хист (друїд): ви вивчили вибране замовляння.",
    "Pact of the Tome: You have learned the selected cantrip.":
        "Договір тому: ви вивчили вибране замовляння.",
    "Pact of the Tome: You have learned three cantrips. Well chosen.":
        "Договір тому: ви вивчили три замовляння. Гарний вибір.",
    "If you reach 0 hit points, you fall Unconscious and must make Death Saving Throws. On 3 successes, you stop bleeding out and become Stable. On 3 failures, you die. If you roll a 20 on the d20, you regain 1 Hit Point.\n\nIf you regain any hit points, the condition is removed. If an ally <LSTag Type=\"Spell\" Tooltip=\"Target_Help\">Helps</LSTag> you, you regain 1 hit point.":
        "Коли ваші очки здоров’я знижуються до 0, ви непритомнієте й мусите виконувати кидки Протидії смерті. Три успіхи стабілізують вас і зупиняють кровотечу, а три провали спричиняють смерть. Результат 20 на d20 відновлює вам 1 очко здоров’я.\n\nСтан зникає, щойно ви відновлюєте будь-яку кількість очок здоров’я. Якщо союзник <LSTag Type=\"Spell\" Tooltip=\"Target_Help\">Допомагає</LSTag> вам, ви відновлюєте 1 очко здоров’я.",
    "As a Bonus Action, you gain giant-like power for 1 minute. You become Large, have advantage on Strength checks and Strength saving throws, and your weapon or unarmed attacks deals an extra 1d6 damage on a hit.":
        "Вторинною дією ви на 1 хвилину набуваєте сили велетня. Ваш розмір стає великим, ви отримуєте перевагу в перевірках сили й кидках протидії силою, а ваші атаки зброєю та удари голіруч у разі влучання додатково завдають 1d6 шкоди.",
    "For example, a Scroll of Wall of Fire (4th-level spell) requires access to 3rd-level spell slots. A character could meet this requirement with 5 levels in Wizard, or with a combination such as 4 levels in Wizard and 3 levels in Arcane Trickster. However, a character with 4 levels in Cleric and 3 levels in Arcane Trickster would not qualify, since Wall of Fire does not appear on the Cleric spell list.":
        "Наприклад, для Сувою стіни вогню (закляття 4-го рівня) потрібен доступ до чарунок 3-го рівня. Цій вимозі відповідає персонаж із 5 рівнями чарівника або, наприклад, із 4 рівнями чарівника й 3 рівнями Містичного штукаря. Однак персонаж із 4 рівнями клірика та 3 рівнями Містичного штукаря не відповідає їй, оскільки «Стіни вогню» немає у списку заклять клірика.",
    "You become imbued with the blessings of the Summer Court. You are a font of energy that offers respite from injuries. You have a pool of fey energy represented by a number of d6s equal to your druid level.\n\nAs a bonus action, you can choose one creature you can see within 60 feet of you and spend a number of those dice equal to half your druid level or less. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent.\n\nYou regain all expended dice when you finish a long rest.":
        "Вас сповнюють благословення Літнього двору, перетворюючи на джерело цілющої енергії. Ви маєте запас фейської енергії у вигляді d6 в кількості, що дорівнює вашому рівню друїда.\n\nВторинною дією ви можете вибрати видиму істоту в межах 60 футів і витратити не більше половини свого рівня друїда цих кісток. Киньте витрачені кістки й підсумуйте результати: ціль відновлює стільки очок здоров’я та отримує по 1 тимчасовому очку здоров’я за кожну витрачену кістку.\n\nЗавершивши тривалий відпочинок, ви відновлюєте всі витрачені кістки.",
    "The steed can take one of the following actions of your choice on each of its turns: Dash, Disengage, Dodge, or Attack.":
        "Протягом кожного свого ходу скакун може виконати одну з вибраних вами дій: «Ривок», «Відступ», «Ухилення» або «Атака».",
    "It can’t take the Disengage action.":
        "Не може виконувати дію «Відступ».",
    "You always have the Find Steed spell prepared. With this feature, you can cast it without a spell slot or components, and your spellcasting ability for it is Intelligence.\n\nOnce you cast the spell with this feature, you can’t do so in this way again until you finish a Short Rest.":
        "Закляття «Пошук скакуна» завжди підготовлене для вас. Завдяки цій особливості ви можете проказати його без чарунки й складників, використовуючи інтелект як базову характеристику проказування.\n\nПроказавши закляття в такий спосіб, ви не зможете повторити це до завершення короткого відпочинку.",
    "Summoner’s Spellcasting Ability Bonus":
        "Бонус базової характеристики проказування заклинача",
    "Can immediately move up to its speed without provoking opportunity attacks.":
        "Може негайно переміститися на відстань до своєї швидкості, не провокуючи принагідних атак.",
    "Your Arcane Armor gains additional benefits based on its model, as detailed below.\n\nDreadnaught. The damage die of your Force Demolisher increases to 2d6 Force damage. In addition, your reach increases by 10 feet.\n\nGuardian. The damage die of your Thunder Pulse increases to 1d10 Thunder damage. In addition, whenever a creature you can see moves to within 5 feet of you, you can make an opportunity attack against it.\n\nInfiltrator. The damage die of your Lightning Launcher increases to 2d6 Lightning damage. Any creature that takes Lightning damage from your Lightning Launcher become Shocked.":
        "Ваш Магічний обладунок отримує додаткові переваги залежно від моделі.\n\nДредноут. Кістка шкоди вашого Силового руйнівника збільшується до 2d6 силової шкоди, а досяжність — на 10 футів.\n\nОхоронець. Кістка шкоди вашого Громового імпульсу збільшується до 1d10 громової шкоди. Крім того, коли видима істота підходить до вас на 5 футів, ви можете виконати проти неї принагідну атаку.\n\nІнфільтратор. Кістка шкоди вашого Блискавкомета збільшується до 2d6 шкоди блискавкою. Істота, що зазнає від нього шкоди блискавкою, отримує Шок.",
    "Bloodthirst Sneak Attack (1/2)":
        "Кровожерний підступний удар (1/2)",
    "Bloodthirst Sneak Attack (1/4)":
        "Кровожерний підступний удар (1/4)",
    "Bloodthirst Sneak Attack (1/10)":
        "Кровожерний підступний удар (1/10)",
    "When you deal Sneak Attack damage to a creature, you can choose for the Sneak Attack to deal d8s of Poison damage instead of d6s of the same type dealt by the weapon.":
        "Коли ви завдаєте істоті шкоди Підступним ударом, то можете завдати d8 шкоди отрутою замість d6 шкоди того самого типу, що й у зброї.",
    "As a Bonus Action, you can expend one use of your Channel Divinity to create a perfect visual illusion of yourself in an unoccupied space you can see within [1]. The illusion lasts for 1 minute. As a Bonus Action, you can move the illusion up to [1] to another unoccupied space you can see.":
        "Вторинною дією ви можете витратити одне використання Божого наснаження, щоб створити досконалу зорову ілюзію себе у видимому вільному місці в межах [1]. Ілюзія існує 1 хвилину. Вторинною дією ви можете перемістити її на відстань до [1] в інше видиме вільне місце.",
    "When you or a creature within 30 feet of you misses with an attack roll, you can expend one use of your Channel Divinity and give that roll a +10 bonus, potentially causing it to hit. When you use this feature to benefit another creature’s attack roll, you must take a Reaction to do so.":
        "Коли ви або істота в межах 30 футів від вас промахується атакою, ви можете витратити одне використання Божого наснаження й надати кидку бонус +10, потенційно перетворивши промах на влучання. Якщо ви допомагаєте так атакувати іншій істоті, то мусите застосувати реагування.",
    "You can use your Channel Oath to try to <LSTag Type=\"Status\" Tooltip=\"TURNED\">banish</LSTag> an extraplanar creature. Each aberration, celestial, elemental, fey, or fiend within 30 feet of you must succeed on a Wisdom saving throw or be Turned for 1 minute. A Turned creature is forced to flee and cannot come close to you.":
        "Ви можете використати Обітне наснаження, щоб спробувати <LSTag Type=\"Status\" Tooltip=\"TURNED\">прогнати</LSTag> позапланарну істоту. Кожна аберація, небесник, елементаль, фея чи біс у межах 30 футів від вас має успішно виконати кидок протидії мудрістю, інакше зазнає Прогнання на 1 хвилину. Прогнана істота мусить тікати й не може наближатися до вас.",
    "Pact Weapon":
        "Зброя договору",
    "If you’re holding a Finesse weapon and another creature hits you with a melee attack, you can take a Reaction to add your Proficiency Bonus to your Armor Class, potentially causing the attack to miss you. You gain this bonus to your AC against melee attacks until the start of your next turn.":
        "Коли ви тримаєте фехтувальну зброю й інша істота влучає у вас атакою ближнього бою, ви можете реагуванням додати свій бонус спеціалізації до РЗ, потенційно перетворивши влучання на промах. Цей бонус до РЗ проти атак ближнього бою діє до початку вашого наступного ходу.",
    "You conjure spirits from the Elemental Planes that flit around you in a 15-foot Emanation for the duration. Until the spell ends, any attack you make deals an extra damage when you hit a creature in the Emanation. This damage is Acid, Cold, Fire, or Lightning (your choice when you make the attack).\n\nIn addition, the ground in the Emanation is Difficult Terrain for your enemies.":
        "Ви прикликаєте духів зі Стихійних планів, які літають довкола вас у 15-футовій еманації протягом дії закляття. Доки воно не скінчиться, ваші атаки додатково завдають істотам в еманації шкоди кислотою, холодом, вогнем або блискавкою — тип ви вибираєте під час атаки.\n\nКрім того, земля в еманації є складним рельєфом для ваших ворогів.",
    "This weapon grants a +[1] bonus to attack rolls, damage rolls, <LSTag Tooltip=\"SpellDifficultyClass\">Spell Save DC</LSTag>, and spell <LSTag Tooltip=\"AttackRoll\">attack rolls</LSTag>.":
        "Ця зброя дає бонус +[1] до кидків атаки й шкоди, <LSTag Tooltip=\"SpellDifficultyClass\">МС протидії закляттям</LSTag> та <LSTag Tooltip=\"AttackRoll\">кидків атаки</LSTag> закляттями.",
    "Protector: Trained for battle, you gain proficiency with Martial weapons and training with Heavy armor.":
        "Захисник. Завдяки бойовій підготовці ви отримуєте володіння бойовою зброєю та вишкіл із важкими обладунками.",
    "Warden. Trained for battle, you gain proficiency with Martial weapons and training with Medium armor.":
        "Охоронець. Завдяки бойовій підготовці ви отримуєте володіння бойовою зброєю та вишкіл із середніми обладунками.",
    "You gain proficiency with all Melee Martial weapons that don’t have the Two-Handed or Heavy property. You can use a Melee weapon with which you have proficiency as a Spellcasting Focus for your Wizard spells.\n\nYou also gain proficiency in one of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Acrobatics</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Athletics\">Athletics</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Performance</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>.":
        "Ви отримуєте володіння всією бойовою зброєю ближнього бою без властивостей «Дворучна» й «Важка». Зброю ближнього бою, якою ви володієте, можна використовувати як магічний осередок для заклять чарівника.\n\nВи також отримуєте спеціалізацію в одній навичці на свій вибір: <LSTag Type=\"Skills\" Tooltip=\"Acrobatics\">Акробатика</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Athletics\">Атлетика</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Артистичність</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag>.",
    "You gain proficiency in one of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"AnimalHandling\">Animal Handling</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">History</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Insight</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Performance</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Persuasion</LSTag>.":
        "Ви отримуєте спеціалізацію в одній навичці на свій вибір: <LSTag Type=\"Skills\" Tooltip=\"AnimalHandling\">Догляд за тваринами</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">Історія</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Insight\">Проникливість</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Performance\">Артистичність</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Persuasion\">Переконливість</LSTag>.",
    "When Asmodeus accepts you as an Architect of Ruin, he grants you access to his infernal knowledge. You gain proficiency in one of the following skills of your choice: <LSTag Type=\"Skills\" Tooltip=\"Arcana\">Arcana</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">History</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Nature\">Nature</LSTag>, or <LSTag Type=\"Skills\" Tooltip=\"Religion\">Religion</LSTag>.":
        "Прийнявши вас Архітектором руїни, Асмодей відкриває вам пекельні знання. Ви отримуєте спеціалізацію в одній навичці на свій вибір: <LSTag Type=\"Skills\" Tooltip=\"Arcana\">Таїнства</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"History\">Історія</LSTag>, <LSTag Type=\"Skills\" Tooltip=\"Nature\">Природа</LSTag> або <LSTag Type=\"Skills\" Tooltip=\"Religion\">Релігія</LSTag>.",
    "The Cursed creature takes additional damage whenever you attack it and has <LSTag Tooltip=\"Disadvantage\">Disadvantage</LSTag> on <LSTag Tooltip=\"AbilityCheck\">Ability Checks</LSTag> with an <LSTag Tooltip=\"Ability\">Ability</LSTag> of your choosing.":
        "Проклята істота зазнає додаткової шкоди від ваших атак і має <LSTag Tooltip=\"Disadvantage\">заваду</LSTag> для <LSTag Tooltip=\"AbilityCheck\">перевірок</LSTag> вибраної вами <LSTag Tooltip=\"Ability\">характеристики</LSTag>.",
    "Risk Dice starts as four d8 dice. A Risk Die is expended when you use it, and you regain all expended Risk Dice when you finish a Short or Long Rest.\n\nAs you gain levels, both the number of dice and their size increase. From level 2 to level 5, you have four d8 dice. From level 6 to level 9, you have five d8 dice. From level 10 to level 12, you have five d10 dice.":
        "Ваш початковий запас Кісток ризику становить чотири d8. Використана Кістка ризику витрачається, а завершення короткого чи тривалого відпочинку відновлює всі витрачені кістки.\n\nІз підвищенням рівня зростають їхня кількість і розмір: на рівнях 2–5 ви маєте чотири d8, на рівнях 6–9 — п’ять d8, а на рівнях 10–12 — п’ять d10.",
    "Retreat safely: moving won't provoke <LSTag Tooltip=\"OpportunityAttack\">Opportunity Attacks</LSTag>.":
        "Безпечний відступ: рух не провокує <LSTag Tooltip=\"OpportunityAttack\">принагідних атак</LSTag>.",
    "When you take the Attack action on your turn, you can replace one of the attacks with a casting of one of your Wizard cantrips that has a casting time of an action.":
        "Коли ви виконуєте у свій хід дію «Атака», то можете замінити одну з атак проказуванням замовляння чарівника, час проказування якого становить одну дію.",
    "Your alien patron grants you a powerful curse. You always have the Hex spell prepared. When you cast Hex and choose an ability, the target also has Disadvantage on saving throws of the chosen ability for the duration of the spell.":
        "Ваш чужоплановий покровитель дарує вам могутнє прокляття. Закляття «Прокльон» завжди підготовлене для вас. Коли ви проказуєте його й вибираєте характеристику, ціль до завершення дії закляття також має заваду в кидках протидії цією характеристикою.",
    "You always have the Moonbeam spell prepared.\n\nWhile you cast Moonbeam, a creature of your choice that you can see within 60 feet of yourself regains 2d4 Hit Points.\n\nOnce you use this feature to modify a casting of Moonbeam, you can’t use it again until you finish a Long Rest.\n":
        "Закляття «Місячний промінь» завжди підготовлене для вас.\n\nКоли ви проказуєте «Місячний промінь», вибрана вами видима істота в межах 60 футів відновлює 2d4 очки здоров’я.\n\nСкориставшись цією особливістю для зміни «Місячного променя», ви не зможете застосувати її знову до завершення тривалого відпочинку.\n",
    "You always have the Summon Beast and Summon Fey spells prepared. You can cast the Illusion version of each spell without expending a spell slot. Once you cast either spell without a spell slot, you must finish a Long Rest before you can cast the spell in that way again.":
        "Закляття «Прикликання звіра» й «Прикликання феї» завжди підготовлені для вас. Ілюзорну версію кожного з них можна проказати без витрати чарунки. Після такого проказування одного із заклять ви мусите завершити тривалий відпочинок, перш ніж зможете знову проказати його в цей спосіб.",
    "When you reach certain Sorcerer levels, you thereafter always have specific spells prepared. At 3rd level, you always have Cure Wounds, Guiding Bolt, Lesser Restoration, and Scorching Ray prepared. At 5th level, you also have Aura of Vitality and Counterspell prepared. At 7th level, you also have Fire Shield and Wall of Fire prepared. At 9th level, you also have Greater Restoration and Flame Strike prepared.":
        "На певних рівнях чародія ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — «Зцілення ран», «Вказівний заряд», «Мале відновлення» та «Палюче проміння»; на 5-му — «Аура життєвості» й «Чароспин»; на 7-му — «Вогняний щит» і «Стіна вогню»; на 9-му — «Велике відновлення» та «Вогняний стовп».",
    "Your connection to the Astral Domain ensures that you always have certain spells prepared. When you reach specific Cleric levels, as shown in the Astral Domain Spells table, you automatically gain the listed spells and they are always prepared for you. At 3rd level, you gain Blur, Guiding Bolt, <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility\">Invisibility</LSTag>, Longstrider, and Starry Wisp. At 5th level, you gain Blink and Slow. At 7th level, you gain Banishment and Dimension Door. At 9th level, you gain Dispel Evil and Good and Wall of Stone.":
        "На рівнях клірика, указаних у таблиці «Закляття Астрального домену», ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — «Розмиття», «Вказівний заряд», <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility\">«Невидимість»</LSTag>, «Скороходець» і «Зоряний вогник»; на 5-му — «Миготіння» та «Сповільнення»; на 7-му — «Вигнання» й «Міжвимірні двері»; на 9-му — «Розвіяння зла й добра» та «Стіна каменю».",
    "Your connection to the Unbroken Circle ensures that you always have certain spells prepared. When you reach a Druid level specified in the Unbroken Circle Spells table, you thereafter always have the listed spells prepared.\n\nAt 3rd level, you always have Ensnaring Strike, Shillelagh, Shining Smite, and True Strike prepared. At 5th level, you always have <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">Haste</LSTag> prepared. At 7th level, you always have Fire Shield prepared. At 9th level, you always have Flame Strike prepared.\n":
        "На рівнях друїда, указаних у таблиці «Закляття Нерозривного кола», ви отримуєте закляття, які надалі завжди вважаються підготовленими.\n\nНа 3-му рівні — «Обвивальний приступ», «Ґирлиґа», «Сяйна кара» та «Певний удар»; на 5-му — <LSTag Type=\"Spell\" Tooltip=\"Target_Haste\">«Поспіх»</LSTag>; на 7-му — «Вогняний щит»; на 9-му — «Вогняний стовп».\n",
    "You gain the ability to recover using the wild, bestial magic that courses through you. As a Bonus Action, you can expend a use of your Wild Shape to regain a number of Hit Points equal to 2d6 plus your Druid level. This healing increases by 1d6 when you reach Druid levels 5 (3d6 plus your Druid level) and 10 (4d6 plus your Druid level).":
        "Ви вчитеся відновлюватися завдяки дикій звіриній магії, що вирує у вас. Вторинною дією ви можете витратити одне використання Дикої подоби й відновити 2d6 + ваш рівень друїда очок здоров’я. На 5-му рівні друїда кісток стає на 1d6 більше, тож зцілення зростає до 3d6 + ваш рівень друїда, а на 10-му — до 4d6 + ваш рівень друїда.",
    "When you make a <LSTag Tooltip=\"SavingThrow\">Saving Throw</LSTag> to maintain <LSTag Tooltip=\"Concentration\">Concentration</LSTag> on a spell, a roll result of 9 or lower is considered a 10.":
        "Коли ви виконуєте <LSTag Tooltip=\"SavingThrow\">кидок протидії</LSTag>, щоб утримати <LSTag Tooltip=\"Concentration\">зосередження</LSTag> на заклятті, результат 9 або менше вважається за 10.",
    "Casting in Melee. Being within 5 feet of an enemy doesn’t impose Disadvantage on your attack rolls with spells.":
        "Проказування в ближньому бою. Перебування в межах 5 футів від ворога не дає завади вашим кидкам атаки закляттями.",
    "Restore Balance: Negate Disadvantage":
        "Відновлення рівноваги: скасування завади",
    "You gain <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Heroic Inspiration</LSTag> whenever you finish a Long Rest. If you have Heroic Inspiration, you can expend it to reroll any die immediately after rolling it.":
        "Завершивши тривалий відпочинок, ви отримуєте <LSTag Type=\"Status\" Tooltip=\"HEROIC_INSPIRATION_TEMP\">Героїчне натхнення</LSTag>. Маючи Героїчне натхнення, ви можете витратити його, щоб негайно перекинути будь-яку щойно кинуту кістку.",
    "You gain Heroic Inspiration whenever you finish a Long Rest. If you have Heroic Inspiration, you can expend it to reroll any die immediately after rolling it.":
        "Завершивши тривалий відпочинок, ви отримуєте Героїчне натхнення. Маючи його, ви можете витратити натхнення, щоб негайно перекинути будь-яку щойно кинуту кістку.",
    "You can transform as a Bonus Action using one of the options below (choose the option each time you transform). The transformation lasts for 1 minute or until you end it (no action required). Once you transform, you can’t do so again until you finish a Long Rest.\n\nOnce on each of your turns before the transformation ends, you can deal extra damage to one target when you deal damage to it with an attack or a spell. The extra damage equals your Proficiency Bonus, and the extra damage’s type is either Necrotic for Necrotic Shroud or Radiant for Heavenly Wings and Inner Radiance.":
        "Вторинною дією ви можете перетворитися, щоразу вибираючи один із наведених нижче варіантів. Перетворення триває 1 хвилину або доки ви не завершите його без витрати дії. Після перетворення ви не зможете зробити це знову до завершення тривалого відпочинку.\n\nОдин раз протягом кожного свого ходу, перш ніж перетворення завершиться, ви можете додатково завдати шкоди одній цілі своєю атакою чи закляттям. Додаткова шкода дорівнює вашому бонусу спеціалізації та є некротичною для Некротичного савана або променевою для Небесних крил і Внутрішнього сяйва.",
    " You can change your size to Large as a Bonus Action if you’re in a big enough space. This transformation lasts for 10 minutes or until you end it (no action required). For that duration, you have Advantage on Strength checks, and your Speed increases by 10 feet. Once you use this trait, you can’t use it again until you finish a Long Rest.":
        "Якщо навколо достатньо місця, вторинною дією ви можете набути великого розміру. Перетворення триває 10 хвилин або доки ви не завершите його без витрати дії. Протягом цього часу ви маєте перевагу в перевірках сили, а ваша швидкість зростає на 10 футів. Скориставшись цією рисою, ви не зможете застосувати її знову до завершення тривалого відпочинку.",
    "You have learned arcane plans that you use to make magic items.\n\nCreating an Item. When you finish a Long Rest, you can create one or two different magic items.\n\nWhen you reach 6th and 10th level in this class, the number of magic items you can create at the end of a Long Rest increases to three and four, respectively.":
        "Ви опанували магічні креслення, за якими створюєте магічні предмети.\n\nСтворення предмета. Завершивши тривалий відпочинок, ви можете створити один або два різні магічні предмети.\n\nНа 6-му рівні цього класу їхня кількість після тривалого відпочинку зростає до трьох, а на 10-му — до чотирьох.",
    "When you finish a Long Rest, you gain proficiency in one skill of your choice. This proficiency lasts until you finish another Long Rest.":
        "Завершивши тривалий відпочинок, ви отримуєте спеціалізацію в одній навичці на свій вибір. Вона діє до завершення наступного тривалого відпочинку.",
    "When you use your Baleful Interdict to place or burn a seal, its range is 60 feet instead of 30 feet. When you gain the Infernal Conduit feature at 6th level, its range is 30 feet instead of touch.\n\nIn addition, making a ranged attack while within 5 feet of a hostile creature does not impose disadvantage on the attack roll.":
        "Коли ви застосовуєте «Згубний інтердикт», щоб накласти чи спалити печатку, його дальність становить 60 футів замість 30. Після отримання особливості «Пекельний провідник» на 6-му рівні її дальність становить 30 футів замість дотику.\n\nКрім того, перебування в межах 5 футів від ворожої істоти не дає завади вашим дальнім атакам.",
    "Requires attunement by a Paladin.\n\nWhen you hit a Fiend or an Undead with it, that creature takes an extra 1d10 Radiant damage. While you hold the drawn weapon, it creates a 10-foot Emanation originating from you. You and all creatures Friendly to you in the Emanation have <LSTag Tooltip=\"Resistant\">Resistance</LSTag> to damage from spells.":
        "Потребує налаштування паладином.\n\nКоли ви влучаєте цією зброєю в біса чи невмерлого, істота додатково зазнає 1d10 променевої шкоди. Поки ви тримаєте зброю оголеною, вона створює 10-футову еманацію від вас. Ви й усі дружні до вас істоти в еманації маєте <LSTag Tooltip=\"Resistant\">стійкість</LSTag> до шкоди від заклять.",
    "When you assume a Wild Shape form, you gain a number of Temporary Hit Points equal to your Druid level.":
        "Коли ви набуваєте Дикої подоби, то отримуєте тимчасові очки здоров’я в кількості, що дорівнює вашому рівню друїда.",
    "Whenever you activate your Second Wind with a Bonus Action, you can move up to half your Speed without provoking Opportunity Attacks.":
        "Щоразу, коли ви вторинною дією застосовуєте «Другий подих», то можете переміститися на відстань до половини своєї швидкості, не провокуючи принагідних атак.",
    "You can use your Maverick Spirit and Skin of Your Teeth maneuvers without expending a Risk Die. When you do so, roll a d6 instead of a Risk Die.":
        "Ви можете застосовувати маневри «Дух одинака» та «На волосині» без витрати Кістки ризику. У такому разі кидайте d6 замість Кістки ризику.",
    "When you activate your <LSTag Type=\"Status\" Tooltip=\"RAGE\">Rage</LSTag>, when you hit a creature with an Unarmed Strike, you can push it 10 feet.":
        "Поки діє ваша <LSTag Type=\"Status\" Tooltip=\"RAGE\">Лють</LSTag>, влучивши в істоту ударом голіруч, ви можете відштовхнути її на 10 футів.",
    "Whenever you hit with your Unarmed Strike, you can cause it to deal your choice of Acid, Cold, Fire, Lightning, or Thunder damage rather than its normal damage type.":
        "Щоразу, коли ви влучаєте ударом голіруч, то можете завдати ним шкоди кислотою, холодом, вогнем, блискавкою чи громом на свій вибір замість звичайного типу шкоди.",
    "Whenever you roll a 1 or 2 on a die to determine the damage of your weapon attacks against interdicted creatures, you can reroll the die.":
        "Коли кістка шкоди вашої зброї проти істоти під інтердиктом дає результат 1 або 2, ви можете перекинути цю кістку.",
    "When you burn a seal on an interdicted creature, you can activate this boon (no action required) to gain temporary hit points equal to your illrigger level.":
        "Коли ви спалюєте печатку на істоті під інтердиктом, то можете без витрати дії активувати цей дар і отримати тимчасові очки здоров’я в кількості, що дорівнює вашому рівню ілріґера.",
    "Each time you take a <LSTag Tooltip=\"ShortRest\">Short Rest</LSTag>, your <LSTag Type=\"Passive\" Tooltip=\"ArcaneWard\">Arcane Ward</LSTag> is fully restored.":
        "Після кожного <LSTag Tooltip=\"ShortRest\">короткого відпочинку</LSTag> ваш <LSTag Type=\"Passive\" Tooltip=\"ArcaneWard\">Магічний оберіг</LSTag> повністю відновлюється.",
})

UID_OVERRIDES.update({
    "h848282acg476egf71fgd7feg17ed2acf814f":
        "На певних рівнях чародія ви отримуєте закляття, які надалі завжди вважаються підготовленими: на 3-му рівні — «Зцілення ран», «Вказівний заряд», «Мале відновлення» та «Палюче проміння»; на 5-му — «Аура життєвості» й «Чароспин»; на 7-му — «Вогняний щит» і «Стіна вогню»; на 9-му — «Велике відновлення» та «Вогняний стовп».",
})

EXACT_OVERRIDES.update({
    "Magic Initiate: Booming Blade": "Магічний хист: Гуркітливе лезо",
    "War Caster: Booming Blade": "Бойовий заклинач: Гуркітливе лезо",
    "Shadow Touched: Colour Spray": "Торкнутий тінню: Барвистий пирск",
    "Shadow Magic: Colour Spray": "Тіньова магія: Барвистий пирск",
    "Shadow Magic: False Life": "Тіньова магія: Удаване життя",
    "Fey Touched: Command": "Торкнутий феями: Наказ",
    "Fey Magic: Command": "Фейська магія: Наказ",
    "Rune Magic: Command": "Рунічна магія: Наказ",
    "Invocation: False Life": "Інвокація: Удаване життя",
    "Scroll of Mind Spike": "Сувій Проколу розуму",
    "Scroll of Spare the Dying": "Сувій Пощади",
    "Scroll of Thunderclap": "Сувій Рокоту грому",
    "Scroll of Booming Blade": "Сувій Гуркітливого леза",
    "Scroll of Command": "Сувій Наказу",
    "Affected entity's <LSTag Tooltip=\"MovementSpeed\">movement speed</LSTag> is halved.<br><br>The entity can only take either an action or a bonus action.":
        "<LSTag Tooltip=\"MovementSpeed\">Швидкість руху</LSTag> ураженої істоти зменшується вдвічі.<br><br>Істота може виконувати лише дію або вторинну дію.",
    "Paladins who swear the Oath of Conquest gain access to Armor of Agathys and Command at 3rd level, Hold Person and Spiritual Weapon at 5th level, and Bestow Curse and Fear at 9th level.":
        "Паладини Обіту завоювання отримують такі закляття: на 3-му рівні — «Обладунок Агатіс» і «Наказ»; на 5-му — «Утримання особи» та «Духовна зброя»; на 9-му — «Накладання прокляття» й «Страх».",
    "Shadow Magic sorcerers gain additional spells at certain levels: Bane, Darkness, Inflict Wounds, and Pass Without Trace at 3rd level; Hunger of Hadar and Fear at 5th level; <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Greater Invisibility</LSTag> and Phantasmal Killer at 7th level; and Contagion and Cloudkill at 9th level.":
        "Чародії Тіньової магії отримують додаткові закляття: на 3-му рівні — «Бейн», «Пітьма», «Завдання ран» і «Безслідна хода»; на 5-му — «Голод Гадара» та «Страх»; на 7-му — <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">«Велика невидимість»</LSTag> і «Примарний убивця»; на 9-му — «Зараза» та «Убивча хмара».",
    "The Grave Domain grants the following spells as you gain Cleric levels: Protection from Evil and Good, False Life, Lesser Restoration, Ray of Enfeeblement, and Spare the Dying at 3rd level; Revivify and Vampiric Touch at 5th level; Blight and Death Ward at 7th level; and Dispel Evil and Good and Mass Cure Wounds at 9th level.":
        "Могильний домен надає такі закляття: на 3-му рівні клірика — «Захист від зла й добра», «Удаване життя», «Мале відновлення», «Промінь слабкості» та «Пощада»; на 5-му — «Оживлення» й «Вампірський дотик»; на 7-му — «Гниль» та «Оберіг від смерті»; на 9-му — «Розвіяння зла й добра» й «Масове зцілення ран».",
    "Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the Grave Domain Spells table, you thereafter always have the listed spells prepared. The Grave Domain grants the following spells as you gain Cleric levels: Protection from Evil and Good, False Life, Lesser Restoration, Ray of Enfeeblement, and Spare the Dying at 3rd level; Revivify and Vampiric Touch at 5th level; Blight and Death Ward at 7th level; and Dispel Evil and Good and Mass Cure Wounds at 9th level.":
        "Ваш зв’язок із Могильним доменом завжди тримає певні закляття підготовленими. На рівнях клірика, указаних у таблиці «Закляття Могильного домену», ви отримуєте такі закляття: на 3-му рівні — «Захист від зла й добра», «Удаване життя», «Мале відновлення», «Промінь слабкості» та «Пощада»; на 5-му — «Оживлення» й «Вампірський дотик»; на 7-му — «Гниль» та «Оберіг від смерті»; на 9-му — «Розвіяння зла й добра» й «Масове зцілення ран».",
    "Your connection to this divine domain ensures you always have certain spells ready. When you reach a Cleric level specified in the Shadow Domain Spells table, you thereafter always have the listed spells prepared. The Shadow Domain grants the following spells as you gain Cleric levels: <LSTag Type=\"Spell\" Tooltip=\"Target_Bane\">Bane</LSTag>, False Life, <LSTag Type=\"Spell\" Tooltip=\"Target_Blindness\">Blindness</LSTag>, and Darkness at 3rd level; Blink and Fear at 5th level; Black Tentacles and <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">Greater Invisibility</LSTag> at 7th level; and Cone of Cold and Dream at 9th level.":
        "Ваш зв’язок із Тіньовим доменом завжди тримає певні закляття підготовленими. На рівнях клірика, указаних у таблиці «Закляття Тіньового домену», ви отримуєте такі закляття: на 3-му рівні — <LSTag Type=\"Spell\" Tooltip=\"Target_Bane\">«Бейн»</LSTag>, «Удаване життя», <LSTag Type=\"Spell\" Tooltip=\"Target_Blindness\">«Сліпота»</LSTag> та «Пітьма»; на 5-му — «Миготіння» й «Страх»; на 7-му — «Чорні мацаки» та <LSTag Type=\"Spell\" Tooltip=\"Target_Invisibility_Greater\">«Велика невидимість»</LSTag>; на 9-му — «Конус холоду» й «Сон».",
})
