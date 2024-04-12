from ordotools.tools.liturgical_dates import integer_to_roman
from ordotools.tools.liturgical_dates import nth
# When adding translations, use the ISO 639-1 codes
# that can be found in this article:
#
# https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
#
# We will have latin here and in the feast database,
# but eventually we will port everything over.
#
# Feasts are given two digits of padding at the end
# so that we can take care of duplicate feasts with
# different variations.
#
# All of the feats are 100 digits apart. Of these 100
# digits, we will use the odds for the octaves of the
# preceeding feast. This should be plenty.


class Translations:

    def __init__(self):

        self.easy_data = {

            100: {
                "la": "S Hilarii Episcopi ECD",
                "en": "St. Hilary, BpCD",
            },

            200: {
                "la": "S Pauli Primi Eremitæ C",
                "en": "St. Paul the First Hermit, C",
            },

            300: {
                "la": "S Marcelli PM",
                "en": "St. Marcellus, PM",
            },

            400: {
                "la": "S Antonii Abb",
                "en": "St. Anthony, Abbot",
            },

            500: {
                "la": "Cathedræ S Petri Ap Romæ",
                "en": "St. Peter's Chair in Rome",
            },

            600: {
                "la": "Ss Marii, Marthæ, Audifacis & Abachum Mm",
                "en": "",
            },

            700: {
                "la": "Ss Fabiani P et Sebastiani Mm",
                "en": "St.s Fabian, Priest, and Sebastian, Mm",
            },

            800: {
                "la": "S Agnetis VM",
                "en": "St. Agnes, VM",
            },

            900: {
                "la": "Ss Vincentii & Anastasii Mm",
                "en": "",
            },

            1000: {
                "la": "S Raymundi de Peñafort C",
                "en": "St. Raymond of Penafort, C",
            },

            1100: {
                "la": "S Timothei EM",
                "en": "St. Timothy, BpM",
            },

            1200: {
                "la": "Conversio S Pauli Ap",
                "en": "Conversion of St. Paul, Ap",
            },

            1300: {
                "la": "S Polycarpi EM",
                "en": "St. Polycarp, BpM",
            },

            1400: {
                "la": "S Joannis Chrysostomi ECD",
                "en": "St. John Chrysostom, BpCD",
            },

            1500: {
                "la": "S Petri Nolasci C",
                "en": "St. Peter Nolasco, C",
            },

            1600: {
                "la": "S Francisci Salesii ECD",
                "en": "St. Francis de Sales, BpCD",
            },

            1700: {
                "la": "S Martinæ VM",
                "en": "St. Martina, VM",
            },

            1800: {
                "la": "S Joannis Bosco C",
                "en": "St. John Bosco, C",
            },

            1900: {
                "la": "S Ignatii EM",
                "en": "St. Ignatius, BpM",
            },

            2000: {
                "la": "In Purificatione BMV",
                "en": "Purification of the Blessed Virgin Mary",
            },

            2100: {
                "la": "S Blasii EM",
                "en": "St. Blaise, BpM",
            },

            2200: {
                "la": "S Andreæ Corsini EC",
                "en": "St. Andrew Corsini, BpC",
            },

            2300: {
                "la": "S Agathæ VM",
                "en": "St. Agatha, VM",
            },

            2400: {
                "la": "S Titi EC",
                "en": "St. Titus, BpC",
            },

            2500: {
                "la": "S Romualdi Abb",
                "en": "St. Romuald, Abbot",
            },

            2600: {
                "la": "S Joannis de Matha C",
                "en": "St. John of Matha, C",
            },

            2700: {
                "la": "S Cyrilli Alexandrini ECD",
                "en": "St. Cyril of Alexandria, BpCD",
            },

            2800: {
                "la": "S Scholasticæ V",
                "en": "St. Scholastica, V",
            },

            2900: {
                "la": "In Apparitione BVM Immaculatæ",
                "en": "Apparation of Our Lady at Lourdes",
            },

            3000: {
                "la": "Ss Septem Fundatores Ordinis Servorum BMV C",
                "en": "Seven Holy Founders",
            },

            3100: {
                "la": "S Valentini PM",
                "en": "St. Valentine, PM",
            },

            3200: {
                "la": "",
                "en": "",
            },

            3300: {
                "la": "S Simeonis EM",
                "en": "St. Simeon, BpM",
            },

            3400: {
                "la": "In Cathedra S Petri Ap",
                "en": "St. Peter's Chair in Rome",
            },

            3500: {
                "la": "S Petri Damiani ECD",
                "en": "St. Peter Damian, BpCD",
            },

            3600: {
                "la": "S Matthiæ Ap",
                "en": "St. Matthew, Ap",
            },

            3700: {
                "la": "S Gabrielis a Virgine Perdolente C",
                "en": "",
            },

            3800: {
                "la": "S Casimiri C",
                "en": "St. Casmir, C",
            },

            3900: {
                "la": "Ss Perpetuæ et Felicitatiis Mm",
                "en": "Sts. Perpetua and Felicity, Mm",
            },

            4000: {
                "la": "S Thomæ de Aquino CD",
                "en": "St. Thomas Aquinas, CD",
            },

            4100: {
                "la": "S Joannis a Deo C",
                "en": "St. John of God, C",
            },

            4200: {
                "la": "S Franciscæ Romanæ V",
                "en": "St. Frances of Rome, V",
            },

            4300: {
                "la": "Ss Quadragintarum Mm",
                "en": "Forty Holy Martyrs",
            },

            4400: {
                "la": "S Gregorii I PCD",
                "en": "St. Gregory I, PCD",
            },

            4500: {
                "la": "S Patricii EC",
                "en": "St. Patrick, BpC",
            },

            4600: {
                "la": "S Cyrilii Hierosolymitani ECD",
                "en": "St. Cyril of Jerusalem, BCD",
            },

            4700: {
                "la": "S Josephi Sponsi BMV C",
                "en": "",
            },

            4800: {
                "la": "S Benedicti Abb",
                "en": "",
            },

            4900: {
                "la": "S Gabrielis Arch",
                "en": "",
            },

            5000: {
                "la": "In Annuntiatione BMV",
                "en": "",
            },

            5100: {
                "la": "S Joannis Damasceni CD",
                "en": "",
            },

            5200: {
                "la": "S Joannis a Capistrano C",
                "en": "",
            },

            5300: {
                "la": "S Francisci de Paula C",
                "en": "",
            },

            5400: {
                "la": "S Isidori ECD",
                "en": "",
            },

            5500: {
                "la": "S Vincentii Ferrerii C",
                "en": "",
            },

            5600: {
                "la": "S Leonis PCD",
                "en": "",
            },

            5700: {
                "la": "S Hermenegildi M",
                "en": "",
            },

            5800: {
                "la": "S Justini M",
                "en": "",
            },

            5900: {
                "la": "S Aniceti PM",
                "en": "",
            },

            6000: {
                "la": "S Anselmi ECD",
                "en": "",
            },

            6100: {
                "la": "Ss Soteris et Caii PpMm",
                "en": "",
            },

            6200: {
                "la": "S Georgii M",
                "en": "",
            },

            6300: {
                "la": "S Fidelis a Sigmaringa M",
                "en": "",
            },

            6400: {
                "la": "S Marci Ev",
                "en": "",
            },

            6500: {
                "la": "Ss Cleti et Marcellini PpMm",
                "en": "",
            },

            6600: {
                "la": "S Petri Canisii CD",
                "en": "",
            },

            6700: {
                "la": "S Pauli a Cruce C",
                "en": "",
            },

            6800: {
                "la": "S Petri M",
                "en": "",
            },

            6900: {
                "la": "S Catharinæ Senensis v",
                "en": "",
            },

            7000: {
                "la": "Ss Philippi et Jacobi App",
                "en": "",
            },

            7100: {
                "la": "S Athanasii ECD",
                "en": "",
            },

            7200: {
                "la": "In Inventione S Crucis",
                "en": "",
            },

            7300: {
                "la": "S Monicæ V",
                "en": "",
            },

            7400: {
                "la": "S Pii V PC",
                "en": "",
            },

            7500: {
                "la": "S Joannis ApEv ante Portam Latinam",
                "en": "",
            },

            7600: {
                "la": "S Stanislai EM",
                "en": "",
            },

            7700: {
                "la": "In Apparitione S Michaelis Arch",
                "en": "",
            },

            7800: {
                "la": "S Gregorii Nanzanzeni ECD",
                "en": "",
            },

            7900: {
                "la": "S Antonini EC",
                "en": "",
            },

            8000: {
                "la": "Ss Nerei, Achillei at Domitialæ V atque Pancratii Mm",
                "en": "",
            },

            8100: {
                "la": "S Roberti Bellarmino ECD",
                "en": "",
            },

            8200: {
                "la": "S Bonifatii M",
                "en": "",
            },

            8300: {
                "la": "S Joannis Baptistæ de la Salle C",
                "en": "",
            },

            8400: {
                "la": "S Ubaldi EC",
                "en": "",
            },

            8500: {
                "la": "S Paschalis Baylon C",
                "en": "",
            },

            8600: {
                "la": "S Venantii M",
                "en": "",
            },

            8700: {
                "la": "S Petri Cælestini PC",
                "en": "",
            },

            8800: {
                "la": "S Bernardini Senensis C",
                "en": "",
            },

            8900: {
                "la": "S Gregorii VII PC",
                "en": "",
            },

            9000: {
                "la": "S Philippi Nerii C",
                "en": "",
            },

            9100: {
                "la": "S Bedæ Venerabilis CD",
                "en": "",
            },

            9200: {
                "la": "S Augustini EC",
                "en": "",
            },

            9300: {
                "la": "S Mariæ Magdalenæ de Pazzis V",
                "en": "",
            },

            9400: {
                "la": "S Felix I PM",
                "en": "",
            },

            9500: {
                "la": "B Mariæ Virginis Reginæ",
                "en": "",
            },

            9600: {
                "la": "S Angelæ Mariciæ V",
                "en": "",
            },

            9700: {
                "la": "Ss Marcellini, Petri atque Erasmi E Mm",
                "en": "",
            },

            9800: {
                "la": "S Francisci Caracciolo C",
                "en": "",
            },

            9900: {
                "la": "S Bonifatii EM",
                "en": "",
            },

            10000: {
                "la": "S Norberti EC",
                "en": "St. Norbert, BpC",
            },

            10100: {
                "la": "Ss Primi et Feliciani Mm",
                "en": "",
            },

            10200: {
                "la": "S Margaritæ R V",
                "en": "",
            },

            10300: {
                "la": "S Barnabæ Ap",
                "en": "",
            },

            10400: {
                "la": "S Joannis a S Facundo C",
                "en": "",
            },

            10500: {
                "la": "S Antonii de Padua CD",
                "en": "",
            },

            10600: {
                "la": "S Basilii Magni ECD",
                "en": "",
            },

            10700: {
                "la": "Ss Viti, Modesti atque Crescentiæ Mm",
                "en": "",
            },

            10800: {
                "la": "S Ephræm Syri Diaconi CD",
                "en": "",
            },

            10900: {
                "la": "S Julianæ de Falconeriis V",
                "en": "",
            },

            11000: {
                "la": "S Silverii PM",
                "en": "",
            },

            11100: {
                "la": "S Aloisii Gonzagæ C",
                "en": "",
            },

            11200: {
                "la": "S Paulini EC",
                "en": "",
            },

            11300: {
                "la": "In Vigilia Natifitatis S Joannis Baptistæ",
                "en": "",
            },

            11400: {
                "la": "In Nativitate S Joannis Baptistæ",
                "en": "Nativity of St. John the Baptist",
            },

            11401: {
                "la": "Oct S Joannis Baptistæ",
                "en": "of St. John the Baptist",
            },

            11500: {
                "la": "S Gulielmi Abb",
                "en": "",
            },

            11600: {
                "la": "S Joannis et Pauli Mm",
                "en": "",
            },

            11800: {
                "la": "S Irinæi EM",
                "en": "",
            },

            11900: {
                "la": "Ss Petri et Pauli App",
                "en": "Sts. Peter and Paul, App.",
            },

            11901: {
                "la": "Oct Ss Petri et Pauli App",
                "en": "of Sts. Peter and Paul, App.",
            },

            12000: {
                "la": "In Commemoratione S Pauli Apostoli",
                "en": "",
            },

            12100: {
                "la": "In Festo Pretiosissimi Sanguinis DNJC",
                "en": "",
            },

            12200: {
                "la": "In Visitatione BMV",
                "en": "",
            },

            12300: {
                "la": "S Leonis II PC",
                "en": "",
            },

            12500: {
                "la": "S Antonii Mariæ Zaccaria C",
                "en": "",
            },

            12700: {
                "la": "Ss Cyrilli et Methodii EeCc",
                "en": "",
            },

            12800: {
                "la": "S Elisabeth R Vid",
                "en": "",
            },

            12900: {
                "la": "Ss Septem Fratrum Mm ac Rufinæ et Secundæ VvMm",
                "en": "",
            },

            13000: {
                "la": "S Pii I PM",
                "en": "",
            },

            13100: {
                "la": "S Joannis Gualberti Abb",
                "en": "",
            },

            13200: {
                "la": "A Anacleti PM",
                "en": "",
            },

            13300: {
                "la": "S Bonaventuræ ECD",
                "en": "",
            },

            13400: {
                "la": "S Henrici Imp C",
                "en": "",
            },

            13500: {
                "la": "In Commemoratione BMV de Monte Carmelo",
                "en": "Our Lady of Mount Carmel",
            },

            13600: {
                "la": "S Alexii C",
                "en": "",
            },

            13700: {
                "la": "S Camilli de Lellis C",
                "en": "",
            },

            13800: {
                "la": "S Vincentii a Paulo C",
                "en": "",
            },

            13900: {
                "la": "S Hieronymi Æmiliani C",
                "en": "",
            },

            14000: {
                "la": "S Praxedis V",
                "en": "",
            },

            14100: {
                "la": "S Mariæ Magdalenæ Pænitentis",
                "en": "",
            },

            14200: {
                "la": "S Apollinaris EM",
                "en": "",
            },

            14300: {
                "la": "In Vigilia S Jacobi Ap",
                "en": "",
            },

            14400: {
                "la": "S Jacobi Ap",
                "en": "",
            },

            14500: {
                "la": "S Annæ Matris BMV",
                "en": "",
            },

            14600: {
                "la": "S Pantaleonis M",
                "en": "",
            },

            14700: {
                "la": "Ss Nazarii et Celsi Mm, Victoris I PM, ac Innocentii I PC",
                "en": "",
            },

            14800: {
                "la": "S Marthæ V",
                "en": "",
            },

            14900: {
                "la": "Ss Abdon et Sennen Mm",
                "en": "",
            },

            15000: {
                "la": "S Ignatii C",
                "en": "",
            },

            15100: {
                "la": "S Petri Ap ad Vincula",
                "en": "",
            },

            15200: {
                "la": "S Alphonsi Mariæ de Ligorio ECD",
                "en": "",
            },

            15300: {
                "la": "In Inventione S Stephani Protomartyris",
                "en": "",
            },

            15400: {
                "la": "S Dominici C",
                "en": "",
            },

            15500: {
                "la": "In Dedicatione S Mariæ ad Nives",
                "en": "",
            },

            15600: {
                "la": "In Transfiguratione DNJC",
                "en": "",
            },

            15700: {
                "la": "S Cajetani C",
                "en": "",
            },

            15800: {
                "la": "Ss Cyriaci, Largi atque Smaragdi Mm",
                "en": "",
            },

            15900: {
                "la": "S Joannis Mariæ Vianney C",
                "en": "",
            },

            16000: {
                "la": "S Laurentii M",
                "en": "",
            },

            16100: {
                "la": "Ss Tiburtii et Susannæ V, Mm",
                "en": "",
            },

            16200: {
                "la": "S Claræ V",
                "en": "",
            },

            16300: {
                "la": "Ss Hippolyti et Cassiani Mm",
                "en": "",
            },

            16400: {
                "la": "In Vigilia Assumptionis BMV",
                "en": "",
            },

            16500: {
                "la": "In Assumptione BMV",
                "en": "Assumption of the BVM",
            },

            16501: {
                "la": "Oct Assumptionis BMV",
                "en": "of the Assumption of the BVM",
            },

            16600: {
                "la": "S Joachim C, Patris BMV",
                "en": "",
            },

            16700: {
                "la": "S Hyacinthi C",
                "en": "",
            },

            16800: {
                "la": "S Agapiti M",
                "en": "",
            },

            16900: {
                "la": "S Joannis Eudes C",
                "en": "",
            },

            17000: {
                "la": "S Bernardi AbbD",
                "en": "",
            },

            17100: {
                "la": "S Joannæ Franciscæ Fremiot de Chantal V",
                "en": "",
            },

            17200: {
                "la": "In Festo Immaculati Cordis BMV",
                "en": "",
            },

            17300: {
                "la": "S Philippi Benitii C",
                "en": "",
            },

            17400: {
                "la": "S Bartholomæi Ap",
                "en": "",
            },

            17500: {
                "la": "S Ludovici RC",
                "en": "",
            },

            17600: {
                "la": "S Zephrini PM",
                "en": "",
            },

            17700: {
                "la": "S Josephi Calasanctii C",
                "en": "",
            },

            17800: {
                "la": "S Augustini ECD",
                "en": "",
            },

            17900: {
                "la": "In Decollatione S Joannis Baptistæ",
                "en": "",
            },

            18000: {
                "la": "S Rosæ a S Maria Limanæ V",
                "en": "",
            },

            18100: {
                "la": "S Raymundi Nonnati C",
                "en": "",
            },

            18200: {
                "la": "S Ægidii Abb",
                "en": "",
            },

            18300: {
                "la": "S Stephani R C",
                "en": "",
            },

            18400: {
                "la": "S Pii X PC",
                "en": "",
            },

            18500: {
                "la": "S Laurentii Justiniani EC",
                "en": "",
            },

            18600: {
                "la": "In Nativitate BMV",
                "en": "",
            },

            18700: {
                "la": "S Gorgonii M",
                "en": "",
            },

            18800: {
                "la": "S Nicolai de Tolentino C",
                "en": "",
            },

            18900: {
                "la": "Ss Proti et Hycinthi Mm",
                "en": "",
            },

            19000: {
                "la": "Ssmi Nominis BMV",
                "en": "",
            },

            19100: {
                "la": "In Exaltatione S Crucis",
                "en": "",
            },

            19200: {
                "la": "Septem Dolorum BMV",
                "en": "",
            },

            19300: {
                "la": "Ss Cornelii P et Cypriani E Mm",
                "en": "",
            },

            19400: {
                "la": "In Impressione Ss Stigmatum S Francisci C",
                "en": "",
            },

            19500: {
                "la": "S Josephi a Cupertino C",
                "en": "",
            },

            19600: {
                "la": "Ss Januarii E et Sociorum Mm",
                "en": "",
            },

            19700: {
                "la": "Ss Eustachii et Sociorum Mm",
                "en": "",
            },

            19800: {
                "la": "S Matthæi ApEv",
                "en": "",
            },

            19900: {
                "la": "S Thomæ de Villanova EC",
                "en": "",
            },

            20000: {
                "la": "S Lini PM",
                "en": "",
            },

            20100: {
                "la": "BMV de Merdece",
                "en": "",
            },

            20200: {
                "la": "Ss Cypriani et Justinæ Mm",
                "en": "",
            },

            20300: {
                "la": "Ss Cosmæ et Damiani Mm",
                "en": "",
            },

            20400: {
                "la": "S Wenceslai Ducis M",
                "en": "",
            },

            20500: {
                "la": "In Dedicatione S Michælis Arch",
                "en": "",
            },

            20600: {
                "la": "S Hieronymi SCD",
                "en": "",
            },

            20700: {
                "la": "S Remigii EC",
                "en": "",
            },

            20800: {
                "la": "Ss Angelorum Custodum",
                "en": "",
            },

            20900: {
                "la": "S Teresiæ a Jesu Infante V",
                "en": "",
            },

            21000: {
                "la": "S Francisci C",
                "en": "",
            },

            21100: {
                "la": "Ss Placidi et Sociorum Mm",
                "en": "",
            },

            21200: {
                "la": "S Brunonis C",
                "en": "",
            },

            21300: {
                "la": "Sacratissimi Rosarii BMV",
                "en": "",
            },

            21400: {
                "la": "S Birgittæ V",
                "en": "",
            },

            21500: {
                "la": "S Joannis Leonardi C",
                "en": "",
            },

            21600: {
                "la": "S Francisci Borgiæ C",
                "en": "",
            },

            21700: {
                "la": "In Maternitate BMV",
                "en": "",
            },

            21800: {
                "la": "S Eduardi R C",
                "en": "",
            },

            21900: {
                "la": "S Callisti I PM",
                "en": "",
            },

            22000: {
                "la": "S Teresiæ V",
                "en": "",
            },

            22100: {
                "la": "S Hedwigis V",
                "en": "",
            },

            22200: {
                "la": "S Margaritæ Mariæ Alacoque V",
                "en": "",
            },

            22300: {
                "la": "S Lucæ Ev",
                "en": "",
            },

            22400: {
                "la": "S Petri de Alacantara C",
                "en": "",
            },

            22500: {
                "la": "S Joannis Cantii C",
                "en": "",
            },

            22600: {
                "la": "S Hilarionis Abb",
                "en": "",
            },

            22700: {
                "la": "S Raphaelis Arch",
                "en": "",
            },

            22800: {
                "la": "Ss Chrysanthi et Dariæ Mm",
                "en": "",
            },

            22900: {
                "la": "S Evaristi PM",
                "en": "",
            },

            23000: {
                "la": "In Vigilia Ss Simonis et Judæ App",
                "en": "",
            },

            23100: {
                "la": "Ss Simonis et Judæ App",
                "en": "",
            },

            23200: {
                "la": "In Vigilia Omnium Sanctorum",
                "en": "",
            },

            23300: {
                "la": "In Festo Omnium Sanctorum",
                "en": "Feast of All Saints",
            },

            23301: {
                "la": "Oct Omnium Sanctorum",
                "en": "of All Saints",
            },

            23400: {
                "la": "In Commemoratione Omnium Fidelium Defunctorum",
                "en": "",
            },

            23500: {
                "la": "S Caroli EC",
                "en": "",
            },

            23700: {
                "la": "In Dedicatione Archibasilicæ Ssmi Salvatoris",
                "en": "",
            },

            23800: {
                "la": "S Andreæ Avellini C",
                "en": "",
            },

            23900: {
                "la": "S Martini EC",
                "en": "",
            },

            24000: {
                "la": "S Martini I PM",
                "en": "",
            },

            24100: {
                "la": "S Didaci C",
                "en": "",
            },

            24200: {
                "la": "S Josaphat EM",
                "en": "",
            },

            24300: {
                "la": "S Alberti Magni ECD",
                "en": "",
            },

            24400: {
                "la": "S Gertrudis V",
                "en": "",
            },

            24500: {
                "la": "S Gregorii Thaumaturgi EC",
                "en": "",
            },

            24600: {
                "la": "In Dedicatione Basilicarum Ss Petri et Pauli App",
                "en": "",
            },

            24700: {
                "la": "S Elisabeth V",
                "en": "",
            },

            24800: {
                "la": "S Felicis de Valois C",
                "en": "",
            },

            24900: {
                "la": "In Præsentatione BMV",
                "en": "",
            },

            25000: {
                "la": "S Cæciliæ VM",
                "en": "",
            },

            25100: {
                "la": "S Clementis I PM",
                "en": "",
            },

            25200: {
                "la": "S Joannis a Cruce CD",
                "en": "",
            },

            25300: {
                "la": "S Catharinæ VM",
                "en": "",
            },

            25400: {
                "la": "S Sylvestri Abb",
                "en": "",
            },

            25500: {
                "la": "In Vigilia S Andreæ Ap",
                "en": "",
            },

            25600: {
                "la": "S Andreæ Ap",
                "en": "",
            },

            25800: {
                "la": "S Bibianæ VM",
                "en": "",
            },

            25900: {
                "la": "S Francisci Xaverii C",
                "en": "",
            },

            26000: {
                "la": "S Petri Chrysologi ECD",
                "en": "",
            },

            26100: {
                "la": "S Sabbæ Abb",
                "en": "",
            },

            26200: {
                "la": "S Nicolai EC",
                "en": "",
            },

            26300: {
                "la": "S Ambrosii ECD",
                "en": "",
            },

            26400: {
                "la": "In Conceptione Immaculata BMV",
                "en": "Feast of the Immaculate Conception",
            },

            26401: {
                "la": "Oct Concept Immac BMV",
                "en": "of the Immaculate Conception",
            },

            26600: {
                "la": "S Melchidi PM",
                "en": "",
            },

            26700: {
                "la": "S Damasi I PC",
                "en": "",
            },

            26900: {
                "la": "S Luciæ VM",
                "en": "",
            },

            27000: {
                "la": "S Eusebii EM",
                "en": "",
            },

            27100: {
                "la": "In Vigilia S Thomæ Ap",
                "en": "",
            },

            27200: {
                "la": "S Thomæ Ap",
                "en": "",
            },

            27300: {
                "la": "In Vigilia S Matthiæ",
                "en": "Vigil of St. Matthew, Ap",
            },

            27400: {
                "la": "S Felicis SM",
                "en": "",
            },

            27500: {
                "la": "S Mauri Abb",
                "en": "",
            },

            27600: {
                "la": "S Pauli Apostoli",
                "en": "",
            },

            27700: {
                "la": "S Priscæ VM",
                "en": "",
            },

            27800: {
                "la": "S Canuti RM",
                "en": "",
            },

            27900: {
                "la": "S Emerentianæ VM",
                "en": "",
            },

            28000: {
                "la": "S Petri Apostoli",
                "en": "",
            },

            28100: {
                "la": "S Agnetis VM secundo",
                "en": "",
            },

            28200: {
                "la": "S Dorotheæ VM",
                "en": "",
            },

            28300: {
                "la": "S Apollonia VM",
                "en": "",
            },

            28400: {
                "la": "S Lucii I PM",
                "en": "",
            },

            28500: {
                "la": "Ss Tiburtii, Valeriani et Maximi Mm",
                "en": "",
            },

            28600: {
                "la": "S Vitali M",
                "en": "",
            },

            28700: {
                "la": "Ss Alexandro I Pp, Eventii et Theoduli Mm ac Juvenale Ep C",
                "en": "",
            },

            28800: {
                "la": "Ss Gordiani et Epimachi Mm",
                "en": "",
            },

            28900: {
                "la": "S Pudentianæ V",
                "en": "",
            },

            29000: {
                "la": "S Urbani I PM",
                "en": "St. Urban I, PM",
            },

            29100: {
                "la": "S Eleutherii PM",
                "en": "",
            },

            29200: {
                "la": "S Joannis I PM",
                "en": "St. John I, PM",
            },

            29300: {
                "la": "S Petronillæ V",
                "en": "",
            },

            29400: {
                "la": "Ss Basilidi, Cyrini, Nabori atq Nazarii Mm",
                "en": "",
            },

            29500: {
                "la": "Ss Marci et Marcelliani Mm",
                "en": "",
            },

            29600: {
                "la": "In Vigilia Ss Petri et Pauli App",
                "en": "",
            },

            29700: {
                "la": "S Petri Ap",
                "en": "St. Peter Ap",
            },

            29800: {
                "la": "Ss Processi et Martiniani Mm",
                "en": "",
            },

            29900: {
                "la": "Ss Noboris et Felicis Mm",
                "en": "",
            },

            30000: {
                "la": "Ss Symphorosæ et Septem Filiis ejus Mm",
                "en": "",
            },

            30100: {
                "la": "S Margaritæ VM",
                "en": "",
            },

            30200: {
                "la": "S Liborii EC",
                "en": "",
            },

            30300: {
                "la": "S Christinæ VM",
                "en": "St. Christina VM",
            },

            30400: {
                "la": "S Christophori M",
                "en": "St. Christopher M",
            },

            30500: {
                "la": "Ss Felicis II P, Simplicis, Faustinis atq Beatricae Mm",
                "en": "",
            },

            30600: {
                "la": "S Pauli Ap",
                "en": "",
            },

            30700: {
                "la": "S Stephani PM",
                "en": "",
            },

            30800: {
                "la": "Ss Xysti P, Felicissimi atq Agapiti Mm",
                "en": "",
            },

            30900: {
                "la": "S Donati EM",
                "en": "",
            },

            31000: {
                "la": "Vigilia S Laurentii M",
                "en": "",
            },

            31100: {
                "la": "S Eusebii C",
                "en": "",
            },

            31200: {
                "la": "Octava S Laurentii M",
                "en": "",
            },

            31300: {
                "la": "Ss Timothei, Hippolyti atq Symphoriani Mm",
                "en": "",
            },

            31400: {
                "la": "In Vigilia S Bartholomæi Ap",
                "en": "",
            },

            31500: {
                "la": "S Hermetis M",
                "en": "",
            },

            31600: {
                "la": "S Sabinae M",
                "en": "",
            },

            31700: {
                "la": "Ss Felicis et Adaucti Mm",
                "en": "",
            },

            31800: {
                "la": "Ss Duodecim Fratribus",
                "en": "",
            },

            31900: {
                "la": "S Hadriani M",
                "en": "",
            },

            32000: {
                "la": "S Nicomedis M",
                "en": "",
            },

            32100: {
                "la": "Ss Euphemiae V, Luciae atq Geminiani Mm",
                "en": "",
            },

            32200: {
                "la": "In Vigilia S Matthæi ApEv",
                "en": "",
            },

            32300: {
                "la": "Ss Mauritii et Sociorum Mm",
                "en": "",
            },

            32400: {
                "la": "S Theclae VM",
                "en": "",
            },

            32500: {
                "la": "S Marci PC",
                "en": "",
            },

            32600: {
                "la": "Ss Dionysii E, Rustici atq Eleutherii Mm",
                "en": "",
            },

            32700: {
                "la": "Ss Ursulae et Sociarum VM",
                "en": "",
            },

            32800: {
                "la": "Octavae Omnium Sanctorum",
                "en": "",
            },

            32900: {
                "la": "S Theodori M",
                "en": "",
            },

            33000: {
                "la": "Ss Tryphonis, Respicii atq Nymphae V Mm",
                "en": "",
            },

            33100: {
                "la": "S Mennae M",
                "en": "",
            },

            33200: {
                "la": "S Pontiani PM",
                "en": "",
            },

            33300: {
                "la": "S Felicitatis M",
                "en": "",
            },

            33400: {
                "la": "S Chrysogoni M",
                "en": "",
            },

            33500: {
                "la": "S Petri Alexandrini EM",
                "en": "",
            },

            33600: {
                "la": "S Saturnini M",
                "en": "",
            },

            33700: {
                "la": "S Barbarae VM",
                "en": "",
            },

            33800: {
                "la": "In Vigilia Conceptionis Immaculatæ BMV",
                "en": "",
            },


            34500: {
                "la": "Ss Naboris et Felicis Mm",
                "en": "",
            },

            34700: {
                "la": "Ss Machabæis Mm",
                "en": "",
            },

            34800: {
                "la": "S Romani M",
                "en": "",
            },

            34900: {
                "la": "Ss Sergii, Bacchi, Marcelli atq Apuleji Mm",
                "en": "",
            },

            ##########################
            #    TEMPORAL "FEASTS"   #
            ##########################

            "lady_saturday": {
                "la": "De Sancta Maria in Sabbato",
                "en": "Our Lady's Saturday",
            },

            "Circumcision": {
                "la": "Circumcisio DNJC et Oct. Nativitatis",
                "en": "Circumcision",
            },

            "8_Stephen": {
                "la": "Octava S Stephani Protomartyris",
                "en": "Octave day of St. Stephen, Protomartyr",
            },

            "8_John": {
                "la": "Octava S Joannis Ap Ev",
                "en": "Octave day of St. John, ApEv",
            },

            "8_Innocents": {
                "la": "Octava Ss Innocentium Mm.",
                "en": "Octave day of the Holy Innocents, Mm",
            },

            "SNameJesus": {
                "la": "Ssmi Nominis Jesu",
                "en": "Feast of the Holy Name",
            },

            "SNameJesu_8_Ste": {
                "la": "Ssmi Nominis Jesu",
                "en": "",
            },

            "V_Epiphany": {
                "la": "Vigilia Epiphaniæ",
                "en": "Vigil of the Epiphany",
            },

            "Epiphany": {
                "la": "Epiphania DNJC",
                "en": "The Epiphany",
            },

            "8_Epiphany": {
                "la": "Octava Epiphaniæ",
                "en": "Octave day of the Epiphany",
            },

            "D_Epiphany": {
                "la": "In Octava Epiphaniæ",
                "en": "Sunday within the Octave of the Epiphany",
            },

            "HolyFamily": {
                "la": "S Familiæ Jesu, Mariæ, Joseph",
                "en": "Feast of the Holy Family",
            },
            "D_HolyFamily": {
                "la": "S Familiæ Jesu, Mariæ, Joseph; Dominica I infra Oct. Epiphaniæ",
                "en": "",
            },
            "de_AshWed": {
                "la": "Dies Cinerum",
                "en": "Ash Wednesday",
            },
            "AshWed_f5": {
                "la": "Feria V post Diem Cinerum",
                "en": "Thursday after Ash Wednesday",
            },
            "AshWed_f6": {
                "la": "Feria VI post Diem Cinerum",
                "en": "Friday after Ash Wednesday",
            },
            "AshWed_fs": {
                "la": "Sabbatum post Diem Cinerum",
                "en": "Saturday after Ash Wednesday",
            },
            "D_Lent_1": {
                "la": "Dominica I in Quadragesima",
                "en": "First Sunday of Lent",
            },
            "Ember_Lent_4": {
                "la": "Feria IV Quatuor Temporum Quadragesimæ",
                "en": "Ember Wednesday in Lent",
            },
            "Ember_Lent_6": {
                "la": "Feria VI Quatuor Temporum Quadragesimæ",
                "en": "Ember Friday in Lent",
            },
            "Ember_Lent_s": {
                "la": "Sabbatum Quatuor Temporum Quadragesimæ",
                "en": "Ember Saturday in Lent",
            },

            "SevenSorrows": {
                "la": "Septem Dolorum BMV",
                "en": "Feast of the Seven Sorrows of the BVM",
            },

            "de_Palm_f2": {
                "la": "Feria II Majoris Hebd",
                "en": "Monday in Holy Week",
            },

            "de_Palm_f3": {
                "la": "Feria III Majoris Hebd",
                "en": "Tuesday in Holy Week",
            },

            "de_Palm_f4": {
                "la": "Feria IV Majoris Hebd",
                "en": "Spy Wednesday",
            },

            "de_Palm_f5": {
                "la": "Feria V in Cœna Domini",
                "en": "Maundy Thursday",
            },

            "de_Palm_f6": {
                "la": "Feria VI in Parasceve",
                "en": "Good Friday",
            },

            "de_Palm_fs": {
                "la": "Sabbatum Sanctum",
                "en": "Holy Saturday",
            },

            "Easter": {
                "la": "Dominica Resurrectionis",
                "en": "",
            },

            "8Easter_f2": {
                "la": "Feria II infra Oct. Paschæ",
                "en": "",
            },

            "8Easter_f3": {
                "la": "Feria III infra Oct. Paschæ",
                "en": "",
            },

            "8Easter_f4": {
                "la": "Feria IV infra Oct. Paschæ",
                "en": "",
            },

            "8Easter_f5": {
                "la": "Feria V infra Oct. Paschæ",
                "en": "",
            },

            "8Easter_f6": {
                "la": "Feria VI infra Oct. Paschæ",
                "en": "",
            },

            "WhitSaturday": {
                "la": "Sabbatum in Albis",
                "en": "",
            },

            # C. et Ecclesiæ Universalis Patroni",
            "StJoseph": {
                "la": "Solemnitas S Joseph, Sponsi BMV",
                "en": "Solemnity of St. Joseph, Spouse of the BVM",
            },

            "8_StJoseph": {
                "la": "Octava Solemnitatis S Joseph",
                "en": "",
            },

            "Rogation_1": {
                "la": "Feria II in Rogationibus",
                "en": "",
            },

            "Rogation_2": {
                "la": "Feria III in Rogationibus",
                "en": "",
            },

            "Rogation_3": {
                "la": "Feria IV in Rogationibus in Vigilia Ascensionis ",
                "en": "",
            },

            "Ascension": {
                "la": "Ascensio DNJC",
                "en": "",
            },

            "8_Ascension": {
                "la": "Oct. Ascensionis DNJC",
                "en": "",
            },

            # TODO: this day has special rules
            "p_Ascension_f6": {
                "la": "Oct. Ascensionis DNJC",
                "en": "",
            },

            "D_Ascension": {
                "la": "Dominica infra Oct. Ascensionis",
                "en": "",
            },

            "S_8_Ascension": {
                "la": "Sabbatum infra Oct. Ascensionis",
                "en": "",
            },

            "WhitSunday": {
                "la": "Dominica in Albis",
                "en": "",
            },

            "V_Pentecost": {
                "la": "Sabbatum Vigilia Pentecostes",
                "en": "",
            },

            "Pentecost": {
                "la": "Dominica Pentecostes",
                "en": "",
            },

            "8Pent_f2": {
                "la": "Feria II infra Oct. Pentecostes",
                "en": "",
            },

            "8Pent_f3": {
                "la": "Feria III infra Oct. Pentecostes",
                "en": "",
            },

            "8Pent_f5": {
                "la": "Feria V infra Oct. Pentecostes",
                "en": "",
            },

            "Ember_Pent_4": {
                "la": "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                "en": "",
            },

            "Ember_Pent_6": {
                "la": "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                "en": "",
            },

            "Ember_Pent_s": {
                "la": "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                "en": "",
            },

            "Trinity": {
                "la": "Festum Sanctissimæ Trinitatis",
                "en": "",
            },

            "D_Pent_2": {
                "la": "Dominica infra Oct. Ssmi Corporis Christi", #Christi (Dominica II post Pentecosten)",
                "en": "",
            },

            "D_Pent_3": {
                "la": "Dominica infra Oct. Ssmi Cordis DNJC",  # (Dominica III post Pentecosten)",
                "en": "",
            },

            "CorpusChristi": {
                "la": "Sanctissimi Corporis Christi",
                "en": "",
            },

            "8_CorpusChristi": {
                "la": "Octava Ssmi Corporis Christi",
                "en": "",
            },

            "SacredHeart": {
                "la": "Sacratissimi Cordis Jesu",
                "en": "",
            },

            "8_SacredHeart": {
                "la": "Octava Sacratissimi Cordis Jesu",
                "en": "",
            },

            "Ember_Sept_4": {
                "la": "Feria IV Quatuor Temporum Septembris",
                "en": "",
            },

            "Ember_Sept_6": {
                "la": "Feria VI Quatuor Temporum Septembris",
                "en": "",
            },

            "Ember_Sept_s": {
                "la": "Sabbatum Quatuor Temporum Septembris",
                "en": "",
            },

            "ChristKing": {
                "la": "In Festo DNJC Regis",
                "en": "",
            },

            "Ember_Advent_4": {
                "la": "Feria IV Quatuor Temporum in Adventus",
                "en": "",
            },

            "Ember_Advent_6": {
                "la": "Feria VI Quatuor Temporum in Adventus",
                "en": "",
            },

            "Ember_Advent_s": {
                "la": "Sabbatum Quatuor Temporum in Adventus",
                "en": "",
            },

            "V_Christmas": {
                "la": "Vigilia Nativitas DNJC",
                "en": "",
            },

            "DV_Christmas": {
                "la": "Vigilia Nativitas DNJC",
                "en": "",
            },

            "Christmas": {
                "la": "Nativitas DNJC",
                "en": "",
            },

            "D_Christmas_r": {
                "la": "Dominica Infra Octavam Nativitatis reposita",
                "en": "",
            },

            "D_Christmas": {
                "la": "Dominica Infra Octavam Nativitatis",
                "en": "",
            },

            "8_Chritmas_f6": {
                "la": "Feria VI infra Octavam Nativitatis",
                "en": "Firday within the Octave of the Nativity",
            },

            "StStephan": {
                "la": "S Stephani Protomartyris",
                "en": "",
            },

            "StJohn": {
                "la": "S Joannis Ap Ev",
                "en": "",
            },

            "StsInnocents": {
                "la": "Ss Innocentium Mm",
                "en": "",
            },

            "StThomas": {
                "la": "S Thomæ EM",
                "en": "",
            },

            "StSylvester": {
                "la": "S Silvestri I PC",
                "en": "",
            },

            "D_StThomas": {
                "la": "S Thomæ EM",
                "en": "",
            },

            "D_StSylvester": {
                "la": "S Silvestri I PC",
                "en": "",
            },

        }

        # TODO: to avoid excess computation, all of these have to take
        #       language as a parameter. Perhaps add a subclass?
        self.data = self.easy_data |\
            self.epiphany_time() |\
            self.epiphany_octave() |\
            self.septuagesima_time() |\
            self.lent_sundays() |\
            self.paschaltime() |\
            self.ascension_ferias() |\
            self.corpus_ferias() |\
            self.sacredheart_ferias() |\
            self.solemnity_st_joseph() |\
            self.pentecost_sundays() |\
            self.pentecost_epiphany_sundays() |\
            self.last_pentecost() |\
            self.advents() |\
            self.three_weeks_after_pentecost()

    def lent_sundays(self) -> dict:
        the_days = {}
        normal_lents = [f"D_Lent_{l+1}" for l in range(4)]
        later_lents = ["D_Passion_5", "D_Palm_6"]
        lents = [*normal_lents, *later_lents]
        for x, date in enumerate(lents):
            for feria in range(7):
                if feria == 0:
                    the_days |= {
                        date: {
                            "la": f"""Dominica {f'''infra Hebd {integer_to_roman(x+1)} in Quadragesima{' (Lætare)' if x+1 == 4 else ''}''' if x < 4 else '''Passione''' if x == 4 else '''Palmis''' }""",
                            "en": "",
                        }
                    }
                else:
                    the_days |= {
                        f"de_{'Lent' if x < 4 else 'Passion'}_f{feria+1 if feria != 6 else 's'}": {
                            "la": "De ea",
                            "en": "Feria",
                        }
                    }
        return the_days

    def ascension_ferias(self) -> dict:
        return {  # NOTE: there are duplicates, but does it matter?
            f"in_8_Ascension_{date}": {
                "la": f"De {integer_to_roman(date)} die infra Oct. Ascensionis",
                "en": "",
            } for date in range(1,8)
        }

    def corpus_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_CorpusChristi": {
                "la": f"De {integer_to_roman(date+1)} die infra Oct. Ssmi Corporis Christi",
                "en": "",
            } for date in range(1,8)
        }

    def sacredheart_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_SacredHeart": {
                "la": f"De {integer_to_roman(date+1)} die infra Oct. Sacratissimi Cordis Jesu",
                "en": "",
            } for date in range(1,8)
        }

    def pentecost_sundays(self) -> dict:
        # TODO: add the first 4 Sundays after Pentecost (excluding Trinity)
        pentecost_season = {}
        for date in range(4, 29):
            pentecost_season |= {
                f"D_Pent_{date}": {
                    "la": f"Dominica {integer_to_roman(date)} post Pentecosten",
                    "en": "",
                }
            }
            for feria in range(6):
                pentecost_season |= {
                    f"de_Pent_{date}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                    }
                }
        return pentecost_season

    def pentecost_epiphany_sundays(self) -> dict:
        # WARN: This is really rough and might not be too efficient, but 
        # it works for now.
        epiphany_pents = {}
        for pent in range(22, 29):
            for epiph in range(3, 7):
                epiphany_pents |= {
                    f"D_Epiph_{epiph}_{pent}": {
                        "la": f"Dominica {integer_to_roman(pent)} post Pentecosten, {integer_to_roman(epiph)} Epiphania",
                        "en": f"{nth(pent)} Sunday after Pentecost, {nth(epiph)} after Epiphany",
                    }
                }
        # OPTIM: maybe we can grab this only when we need it.
                for feria in range(6):
                    epiphany_pents |= {
                        f"de_Epiph_{epiph}_{pent}_f{feria+2 if feria != 5 else 's'}": {
                            "la": "De ea",
                            "en": "Feria",
                        }
                    }
        return epiphany_pents

    def last_pentecost(self) -> dict:
        last_pents = {}
        for pent in range(23, 29):
            last_pents |= {
                f"D_UltPent_{pent}": {
                    "la": f"Dominica {integer_to_roman(pent)} et ultima post Pentecosten",
                    "en": "",
                }
            }
            for feria in range(6):
                last_pents |= {
                    f"de_UltPent_{pent}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                    }
                }
        return last_pents

    def advents(self) -> dict:
        advent_season = {}
        advent_sundays = [
            "Ad te levavi",
            "Populus Sion",
            "Gaudete",
            "Rorate cæli",
        ]
        for x, introit in enumerate(advent_sundays):
            advent_season |= {
                # TODO: verify that 2-4 advents are minor sundays
                f"D_Advent_{x+1}": {
                    "la": f"Dominica {integer_to_roman(x+1)} Adventus",
                    "en": "",
                                    }
            }
            for feria in range(6):
                advent_season |= {
                    f"Advent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                    }
                }
        return advent_season

    def three_weeks_after_pentecost(self) -> dict:
        # NOTE: this is overkill, but it works, and is probably faster than a fix
        weeks = {}
        introits = [
            "Benedicta sit",
            "Factus est",
            "Respice in me",
        ]
        for x, introit in enumerate(introits):
            for feria in range(6):
                weeks |= {
                    f"de_Pent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                    },
                }
        return weeks

    def paschaltime(self) -> dict:
        paschaltime = {}
        for week in range(6):
            paschaltime |= {
                f"D_Easter_{week+1}": {
                    "la": f"Dominica {integer_to_roman(week+1)} post Resurrectionis",
                    "en": "",
                }
            }
            for feria in range(6):
                pass
                paschaltime |= {
                    f"de_Easter_{week+1}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                    }
                }
        return paschaltime

    def solemnity_st_joseph(self) -> dict:
        solemnity_ferias = {}
        for feria in range(6):
            solemnity_ferias |= {
                f"{feria+2}_in_8_StJoseph": {
                    "la": f"De {integer_to_roman(feria+2)} die infra Solemnitas S Joseph",
                    "en": "",
                }
            }
        return solemnity_ferias

    def septuagesima_time(self) -> dict:
        septuagesima = {}
        for x, sunday in enumerate(["Septuagesima", "Sexagesima", "Quinquagesima"]):
            septuagesima |= {
                sunday: {
                    "la": f"Dominica in {sunday}",
                    "en": "",
                }
            }
            for feria in range(6):
                septuagesima |= {
                    f"de_{sunday[:4]}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                    }
                }
        return septuagesima

    def epiphany_time(self) -> dict:
        epiphany = {}
        for sunday in range(6):
            epiphany |= {
                f"D_Epiph_{sunday+1}": {
                    "la": f"Dominica {integer_to_roman(sunday+1)} post Epiphaniam",
                    "en": "",
                }
            }
            for feria in range(6):
                epiphany |= {
                    f"de_Epiph_{sunday+1}_{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "Feria",
                    }
                }
        return epiphany

    def epiphany_octave(self) -> dict:
        octave = {
            "8_Epiph_fs": {
                "la": "Sabbato infra Oct Epiphaniæ",
                "en": "Saturday within the Octave of the Epiphany",
            },
        }
        for feria in range(6):
            num = feria + 2
            octave |= {
                f"8_Epiph_f{feria+2}": {
                    "la": f"De {integer_to_roman(num)} die infra Oct. Epiphaniæ",
                    "en": f"{nth(num)} day within the Octave of the Epiphany",
                }
            }
        return octave

    def translations(self) -> dict:
        return self.data

    def octave(self, lang: str, num: int, ref: int) -> str:
        """ Rather than doing this too dynamically, we
        have all of the days separated, to avoid as many grammar
        issues as possible """
        octave_days = {
            "la": [
                "De II die infra",
                "De III die infra",
                "De IV die infra",
                "De V die infra",
                "De VI die infra",
                "De VII die infra",
                "",
            ],
            "en": [
                "2nd day within the Octave",
                "3rd day within the Octave",
                "4th day within the Octave",
                "5th day within the Octave",
                "6th day within the Octave",
                "7th day within the Octave",
                "Octave day",
            ],
        }

        return octave_days[lang][num-2] + " " + self.translations()[ref+1][lang]
