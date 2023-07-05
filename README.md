
# Ordo

Traditional Catholic Ordo and Calendar.

![code size](https://img.shields.io/github/repo-size/corei8/Ordo?style=flat-square)
![language](https://img.shields.io/github/languages/top/corei8/Ordo?style=flat-square)
![frequency](https://img.shields.io/github/commit-activity/m/corei8/Ordo?style=flat-square)

## Python Specifications

Python 3.x.x 64-bit

### Dependencies:

[dateutil](https://dateutil.readthedocs.io/en/stable/)
```bash
pip install python-dateutil
```

## Overview

The temporal cycle is generated by a class as a dictionary. The sanctoral
cycle is made up of several files for country and diocese, and each file is
a "dynamic" dictionary contained in a class, which self-adjusts depending
on the year. The sanctoral cycle is the first to be compiled, then it is
added to the temporal cycle.

The output is a complex dictionary. Each key is a datetime object, and each
item contains the name of the feast together with all the data necessary to
determine the peculiarities of the office and Mass(es) of that day.

Easter is the first feast (every "event" is treated as a feast) to be
determined, since most of the liturgical year depends upon the date of
Easter. Christmas, being static with regard to its date, requires that we
only find the day of the week on which it falls. We begin building the
temporal calendar with January 1st.

## Progress

- [x] Temporal Calendar
- [x] Combined Temporal and Sanctoral Calendar
- [x] Method for adding other countries and dioceses
- [x] Colors of Mass and Office
- [x] Fasting rules
- [ ] Commemorations
- [ ] Masses
- [ ] Votives, Requiems, etc.
- [ ] Phases of the Moon
- [ ] Martyrology letter
- [ ] Vespers
- [ ] Lessons for Laudes
- [ ] Our Lady's Saturday
- [ ] Prime
- [ ] Little Hours
- [ ] Alternative Masses
- [ ] Solemnities
                        

## Sample Roman Calendar for 2023

| Day | Date | Feast |
|---|---|---|
| Dom | Jan 01 | Circumcisio DNJC et Oct. Nativitatis |
| Fer II | Jan 02 | Ssmi Nominis Jesu |
| Fer III | Jan 03 | Octava S Joannis Ap Ev |
| Fer IV | Jan 04 | Octava Ss Innocentium Mm. |
| Fer V | Jan 05 | Vigilia Epiphaniæ |
| Fer VI | Jan 06 | Epiphania DNJC |
| Sabb | Jan 07 | Sabbato infra Oct. Epiphaniæ |
| Dom | Jan 08 | S Familiæ Jesu, Mariæ, Joseph |
| Fer II | Jan 09 | De IV die infra Oct. Epiphaniæ |
| Fer III | Jan 10 | De V die infra Oct. Epiphaniæ |
| Fer IV | Jan 11 | De VI die infra Oct. Epiphaniæ |
| Fer V | Jan 12 | De VII die infra Oct. Epiphaniæ |
| Fer VI | Jan 13 | Octava Epiphaniæ |
| Sabb | Jan 14 | S Hilarii Episcopi ECD |
| Dom | Jan 15 | Dominica II post Epiphaniam |
| Fer II | Jan 16 | S Marcelli PM |
| Fer III | Jan 17 | S Antonii Abb |
| Fer IV | Jan 18 | Cathedræ S Petri Ap Romæ |
| Fer V | Jan 19 | Ss Marii, Marthæ, Audifacis et Abachum Mm |
| Fer VI | Jan 20 | Ss Fabiani P et Sebastiani Mm |
| Sabb | Jan 21 | S Agnetis VM |
| Dom | Jan 22 | Dominica III post Epiphaniam |
| Fer II | Jan 23 | S Raymundi de Peñafort C |
| Fer III | Jan 24 | S Timothei EM |
| Fer IV | Jan 25 | Conversio S Pauli Ap |
| Fer V | Jan 26 | S Polycarpi EM |
| Fer VI | Jan 27 | S Joannis Chrysostomi ECD |
| Sabb | Jan 28 | S Petri Nolasci C |
| Dom | Jan 29 | Dominica IV post Epiphaniam |
| Fer II | Jan 30 | S Martinæ VM |
| Fer III | Jan 31 | S Joannis Bosco C |
| Fer IV | Feb 01 | S Ignatii EM |
| Fer V | Feb 02 | In Purificatione BMV |
| Fer VI | Feb 03 | S Blasii EM |
| Sabb | Feb 04 | S Andreæ Corsini EC |
| Dom | Feb 05 | Dominica in Septuagesima |
| Fer II | Feb 06 | S Titi EC |
| Fer III | Feb 07 | S Romualdi Abb |
| Fer IV | Feb 08 | S Joannis de Matha C |
| Fer V | Feb 09 | S Cyrilli Alexandrini ECD |
| Fer VI | Feb 10 | S Scholasticæ V |
| Sabb | Feb 11 | In Apparitione BMV Immaculatæ |
| Dom | Feb 12 | Dominica in Sexagesima |
| Fer II | Feb 13 | De ea |
| Fer III | Feb 14 | S Valentini PM |
| Fer IV | Feb 15 | Ss Faustini & Jovitæ Mm |
| Fer V | Feb 16 | De ea |
| Fer VI | Feb 17 | De ea |
| Sabb | Feb 18 | De Sancta Maria in Sabbato |
| Dom | Feb 19 | Dominica in Quinquagesima |
| Fer II | Feb 20 | De ea |
| Fer III | Feb 21 | De ea |
| Fer IV | Feb 22 | Dies Cinerum |
| Fer V | Feb 23 | S Petri Damiani ECD |
| Fer VI | Feb 24 | S Matthiæ Ap |
| Sabb | Feb 25 | Sabbatum post Diem Cinerum |
| Dom | Feb 26 | Dominica infra Hebd I in Quadragesima |
| Fer II | Feb 27 | S Gabrielis a Virgine Perdolente C |
| Fer III | Feb 28 | De ea |
| Fer IV | Mar 01 | Feria IV Quattuor Temporum Quadragesimæ |
| Fer V | Mar 02 | De ea |
| Fer VI | Mar 03 | Feria VI Quattuor Temporum Quadragesimæ |
| Sabb | Mar 04 | S Casimiri C |
| Dom | Mar 05 | Dominica infra Hebd II in Quadragesima |
| Fer II | Mar 06 | Ss Perpetuae et Felicitatiis Mm |
| Fer III | Mar 07 | S Thomæ de Aquino CD |
| Fer IV | Mar 08 | S Joannis a Deo C |
| Fer V | Mar 09 | S Franciscae Romanae V |
| Fer VI | Mar 10 | Ss Quadragintarum Mm |
| Sabb | Mar 11 | De ea |
| Dom | Mar 12 | Dominica infra Hebd III in Quadragesima |
| Fer II | Mar 13 | De ea |
| Fer III | Mar 14 | De ea |
| Fer IV | Mar 15 | De ea |
| Fer V | Mar 16 | De ea |
| Fer VI | Mar 17 | S Patricii EC |
| Sabb | Mar 18 | S Cyrilli Hierosolymitani ECD |
| Dom | Mar 19 | Dominica infra Hebd IV in Quadragesima (Lætare) |
| Fer II | Mar 20 | S Josephi Sponsi BMV C |
| Fer III | Mar 21 | S Benedicti Abb |
| Fer IV | Mar 22 | De ea |
| Fer V | Mar 23 | De ea |
| Fer VI | Mar 24 | S Gabrielis Arch |
| Sabb | Mar 25 | In Annuntiatione BMV |
| Dom | Mar 26 | Dominica Passione |
| Fer II | Mar 27 | S Joannis Damasceni CD |
| Fer III | Mar 28 | S Joannis a Capistrano C |
| Fer IV | Mar 29 | De ea |
| Fer V | Mar 30 | De ea |
| Fer VI | Mar 31 | Septem Dolorum BMV |
| Sabb | Apr 01 | De ea |
| Dom | Apr 02 | Dominica Palmis |
| Fer II | Apr 03 | Feria II Majoris Hebd |
| Fer III | Apr 04 | Feria III Majoris Hebd |
| Fer IV | Apr 05 | Feria IV Majoris Hebd |
| Fer V | Apr 06 | Feria V in Cœna Domini |
| Fer VI | Apr 07 | Feria VI in Parasceve |
| Sabb | Apr 08 | Sabbatum Sanctum |
| Dom | Apr 09 | Dominica Resurrectionis |
| Fer II | Apr 10 | Feria II infra Oct. Paschæ |
| Fer III | Apr 11 | Feria III infra Oct. Paschæ |
| Fer IV | Apr 12 | Feria IV infra Oct. Paschæ |
| Fer V | Apr 13 | Feria V infra Oct. Paschæ |
| Fer VI | Apr 14 | Feria VI infra Oct. Paschæ |
| Sabb | Apr 15 | Sabbatum in Albis |
| Dom | Apr 16 | Dominica in Albis |
| Fer II | Apr 17 | S Aniceti PM |
| Fer III | Apr 18 | De ea |
| Fer IV | Apr 19 | De ea |
| Fer V | Apr 20 | De ea |
| Fer VI | Apr 21 | S Anselmi ECD |
| Sabb | Apr 22 | Ss Soteris et Caii PpMm |
| Dom | Apr 23 | Dominica II post Resurrectionis |
| Fer II | Apr 24 | S Fidelis a Sigmaringa M |
| Fer III | Apr 25 | S Marci Ev |
| Fer IV | Apr 26 | Solemnitas S Joseph, Sponsi BMV |
| Fer V | Apr 27 | S Petri Canisii CD |
| Fer VI | Apr 28 | S Pauli a Cruce C |
| Sabb | Apr 29 | S Petri M |
| Dom | Apr 30 | Dominica III post Resurrectionis |
| Fer II | May 01 | Ss Philippi et Iacobi App |
| Fer III | May 02 | S Athanasii ECD |
| Fer IV | May 03 | In Inventione S Crucis |
| Fer V | May 04 | S Monicae V |
| Fer VI | May 05 | S Pii V PC |
| Sabb | May 06 | S Joannis ApEv ante Portam Latinam |
| Dom | May 07 | Dominica IV post Resurrectionis |
| Fer II | May 08 | In Apparitione S Michaelis Arch |
| Fer III | May 09 | S Gregorii Nanzanzeni ECD |
| Fer IV | May 10 | S Antonini EC |
| Fer V | May 11 | De ea |
| Fer VI | May 12 | Ss Nerei, Achillei at Domitillae V atq Pancratii Mm |
| Sabb | May 13 | S Roberti Bellarmino ECD |
| Dom | May 14 | Dominica V post Resurrectionis |
| Fer II | May 15 | S Joannis Baptistae de la Salle C |
| Fer III | May 16 | S Ubaldi EC |
| Fer IV | May 17 | S Paschalis Baylon C |
| Fer V | May 18 | Ascensio DNJC |
| Fer VI | May 19 | S Petri Caelestini PC |
| Sabb | May 20 | S Bernardini Senensis C |
| Dom | May 21 | Dominica infra Oct. Ascensionis |
| Fer II | May 22 | De V die infra Oct. Ascensionis |
| Fer III | May 23 | De VI die infra Oct. Ascensionis |
| Fer IV | May 24 | De VII die infra Oct. Ascensionis |
| Fer V | May 25 | Oct. Ascensionis DNJC |
| Fer VI | May 26 | S Philippi Nerii C |
| Sabb | May 27 | Sabbatum Vigilia Pentecostes |
| Dom | May 28 | Dominica Pentecostes |
| Fer II | May 29 | Feria II infra Oct. Pentecostes |
| Fer III | May 30 | Feria III infra Oct. Pentecostes |
| Fer IV | May 31 | Feria IV Quattuor Temporum infra Oct. Pentecostes |
| Fer V | Jun 01 | Feria V infra Oct. Pentecostes |
| Fer VI | Jun 02 | Feria VI Quattuor Temporum infra Oct. Pentecostes |
| Sabb | Jun 03 | Sabbatum Quattuor Temporum infra Oct. Pentecostes |
| Dom | Jun 04 | Festum Sanctissimæ Trinitatis |
| Fer II | Jun 05 | B Mariae Virginis Reginae |
| Fer III | Jun 06 | S Norberti EC |
| Fer IV | Jun 07 | De ea |
| Fer V | Jun 08 | Sanctissimi Corporis Christi |
| Fer VI | Jun 09 | De II die infra Oct. Ssmi Corporis Christi |
| Sabb | Jun 10 | De III die infra Oct. Ssmi Corporis Christi |
| Dom | Jun 11 | Dominica infra Oct. Ssmi Corporis Christi |
| Fer II | Jun 12 | De V die infra Oct. Ssmi Corporis Christi |
| Fer III | Jun 13 | De VI die infra Oct. Ssmi Corporis Christi |
| Fer IV | Jun 14 | De VII die infra Oct. Ssmi Corporis Christi |
| Fer V | Jun 15 | Octava Ssmi Corporis Christi |
| Fer VI | Jun 16 | Sacratissimi Cordis Jesu |
| Sabb | Jun 17 | De Sancta Maria in Sabbato |
| Dom | Jun 18 | Dominica infra Oct. Ssmi Cordis DNJC |
| Fer II | Jun 19 | S Julianæ de Falconeriis V |
| Fer III | Jun 20 | De V die infra Oct. Sacratissimi Cordis Jesu |
| Fer IV | Jun 21 | S Aloisii Gonzagæ C |
| Fer V | Jun 22 | S Paulini EC |
| Fer VI | Jun 23 | Octava Sacratissimi Cordis Jesu |
| Sabb | Jun 24 | In Nativitate S Joannis Baptistæ |
| Dom | Jun 25 | Dominica IV post Pentecosten |
| Fer II | Jun 26 | S Joannis et Pauli Mm |
| Fer III | Jun 27 | De IV die infra In Nativitate S Joannis Baptistæ |
| Fer IV | Jun 28 | Irinæi EM |
| Fer V | Jun 29 | Ss Petri et Pauli App |
| Fer VI | Jun 30 | In Commemoratione S Pauli Apostoli |
| Sabb | Jul 01 | In Festo Pretiosissimi Sanguinis DNJC |
| Dom | Jul 02 | In Visitatione BMV |
| Fer II | Jul 03 | S Leonis II PC |
| Fer III | Jul 04 | De VI die infra Ss Petri et Pauli App |
| Fer IV | Jul 05 | S Antonii Mariæ Zaccaria C |
| Fer V | Jul 06 | Ss Petri et Pauli App |
| Fer VI | Jul 07 | Ss Cyrilli et Methodii EeCc |
| Sabb | Jul 08 | S Elisabeth R Vid |
| Dom | Jul 09 | Dominica VI post Pentecosten |
| Fer II | Jul 10 | Ss Septem Fratrum Mm ac Rufinæ et Secundæ VvMm |
| Fer III | Jul 11 | S Pii I PM |
| Fer IV | Jul 12 | S Joannis Gualberti Abb |
| Fer V | Jul 13 | S Anacleti PM |
| Fer VI | Jul 14 | S Bonaventuræ ECD |
| Sabb | Jul 15 | S Henrici Imp C |
| Dom | Jul 16 | Dominica VII post Pentecosten |
| Fer II | Jul 17 | S Alexii C |
| Fer III | Jul 18 | S Camilli de Lellis C |
| Fer IV | Jul 19 | S Vincentii a Paulo C |
| Fer V | Jul 20 | S Hieronymi Æmiliani C |
| Fer VI | Jul 21 | S Praxedis V |
| Sabb | Jul 22 | S Mariæ Magdalenæ Pænitentis |
| Dom | Jul 23 | Dominica VIII post Pentecosten |
| Fer II | Jul 24 | In Vigilia S Jacobi Ap |
| Fer III | Jul 25 | S Jacobi Ap |
| Fer IV | Jul 26 | S Annæ Matris BMV |
| Fer V | Jul 27 | S Pantaleonis M |
| Fer VI | Jul 28 | Ss Nazarii et Celsi Mm, Victoris I PM, ac Innocentii I PC |
| Sabb | Jul 29 | S Marthæ V |
| Dom | Jul 30 | Dominica IX post Pentecosten |
| Fer II | Jul 31 | S Ignatii C |
| Fer III | Aug 01 | S Petri Ap ad Vincula |
| Fer IV | Aug 02 | S Alphonsi Mariæ de Ligorio ECD |
| Fer V | Aug 03 | In Inventione S Stephani Protomartyris |
| Fer VI | Aug 04 | S Dominici v |
| Sabb | Aug 05 | In Dedicatione S Mariæ ad Nives |
| Dom | Aug 06 | In Transfiguratione DNJC |
| Fer II | Aug 07 | S Cajetani C |
| Fer III | Aug 08 | Ss Cyriaci, Largi atq Smaragdi Mm |
| Fer IV | Aug 09 | S Joannis Mariæ Vianney C |
| Fer V | Aug 10 | S Laurentii M |
| Fer VI | Aug 11 | Ss Tiburtii et Susannæ V, Mm |
| Sabb | Aug 12 | S Claræ V |
| Dom | Aug 13 | Dominica XI post Pentecosten |
| Fer II | Aug 14 | In Vigilia Assumptionis BMV |
| Fer III | Aug 15 | In Assumptione BMV |
| Fer IV | Aug 16 | S Joachim C, Patris BMV, |
| Fer V | Aug 17 | S Hyacinthi C |
| Fer VI | Aug 18 | De IV die infra In Assumptione BMV |
| Sabb | Aug 19 | S Joannis Eudes C |
| Dom | Aug 20 | Dominica XII post Pentecosten |
| Fer II | Aug 21 | S Joannæ Franciscæ Fremiot de Chantal V |
| Fer III | Aug 22 | In Festo Immaculati Cordis BMV |
| Fer IV | Aug 23 | S Philippi Benitii C |
| Fer V | Aug 24 | S Bartholomæi Ap |
| Fer VI | Aug 25 | S Ludovici RC |
| Sabb | Aug 26 | S Zephrini PM |
| Dom | Aug 27 | Dominica XIII post Pentecosten |
| Fer II | Aug 28 | S Augustini ECD |
| Fer III | Aug 29 | In Decollatione S Joannis Baptistæ |
| Fer IV | Aug 30 | S Rosæ a S Maria Limanae V |
| Fer V | Aug 31 | S Raymundi Nonnati C |
| Fer VI | Sep 01 | S Ægidii Abb |
| Sabb | Sep 02 | S Stephani R C |
| Dom | Sep 03 | Dominica XIV post Pentecosten |
| Fer II | Sep 04 | De ea |
| Fer III | Sep 05 | S Laurentii Justiniani EC |
| Fer IV | Sep 06 | De ea |
| Fer V | Sep 07 | De ea |
| Fer VI | Sep 08 | In Nativitate BMV |
| Sabb | Sep 09 | De Sancta Maria in Sabbato |
| Dom | Sep 10 | Dominica XV post Pentecosten |
| Fer II | Sep 11 | Ss Proti et Hycinthi Mm |
| Fer III | Sep 12 | Ssmi Nominis BMV |
| Fer IV | Sep 13 | De ea |
| Fer V | Sep 14 | In Exaltatione S Crucis |
| Fer VI | Sep 15 | Septem Dolorum BMV |
| Sabb | Sep 16 | Ss Cornelii P et Cypriani E Mm |
| Dom | Sep 17 | Dominica XVI post Pentecosten |
| Fer II | Sep 18 | S Josephi a Cupertino C |
| Fer III | Sep 19 | Ss Januarii E et Sociorum Mm |
| Fer IV | Sep 20 | Ss Eustachii et Sociorum Mm |
| Fer V | Sep 21 | S Matthæi ApEv |
| Fer VI | Sep 22 | S Thomæ de Villanova EC |
| Sabb | Sep 23 | S Lini PM |
| Dom | Sep 24 | Dominica XVII post Pentecosten |
| Fer II | Sep 25 | De ea |
| Fer III | Sep 26 | Ss Cypriani et Justinæ Mm |
| Fer IV | Sep 27 | Ss Cosmæ et Damiani Mm |
| Fer V | Sep 28 | S Wenceslai Ducis M |
| Fer VI | Sep 29 | In Dedicatione S Michaelis Arch |
| Sabb | Sep 30 | S Hieronymi SCD |
| Dom | Oct 01 | Dominica XVIII post Pentecosten |
| Fer II | Oct 02 | Ss Angelorum Custodum |
| Fer III | Oct 03 | S Teresiæ a Jesu Infante V |
| Fer IV | Oct 04 | S Francisci C |
| Fer V | Oct 05 | Ss Placidi et Sociorum Mm |
| Fer VI | Oct 06 | S Brunonis C |
| Sabb | Oct 07 | Sacratissimi Rosarii BMV |
| Dom | Oct 08 | Dominica XIX post Pentecosten |
| Fer II | Oct 09 | S Joannis Leonardi C |
| Fer III | Oct 10 | S Francisci Borgiæ C |
| Fer IV | Oct 11 | In Maternitate BMV |
| Fer V | Oct 12 | De ea |
| Fer VI | Oct 13 | S Eduardi R C |
| Sabb | Oct 14 | S Callisti I PM |
| Dom | Oct 15 | Dominica XX post Pentecosten |
| Fer II | Oct 16 | S Hedwigis V |
| Fer III | Oct 17 | S Margaritæ Mariæ Alacoque V |
| Fer IV | Oct 18 | S Lucæ Ev |
| Fer V | Oct 19 | S Petri de Alcantara C |
| Fer VI | Oct 20 | S Joannis Cantii C |
| Sabb | Oct 21 | De Sancta Maria in Sabbato |
| Dom | Oct 22 | Dominica XXI post Pentecosten |
| Fer II | Oct 23 | De ea |
| Fer III | Oct 24 | S Raphaelis Arch |
| Fer IV | Oct 25 | Ss Chrysanthi et Dariæ Mm |
| Fer V | Oct 26 | S Evaristi PM |
| Fer VI | Oct 27 | In Vigilia Ss Simonis et Judæ App |
| Sabb | Oct 28 | Ss Simonis et Judæ App |
| Dom | Oct 29 | In Festo DNJC Regis |
| Fer II | Oct 30 | De ea |
| Fer III | Oct 31 | In Vigilia Omnium Sanctorum |
| Fer IV | Nov 01 | In Festo Omnium Sanctorum |
| Fer V | Nov 02 | In Commemoratione Omnium Fidelium Defunctorum |
| Fer VI | Nov 03 | De III die infra In Festo Omnium Sanctorum |
| Sabb | Nov 04 | S Caroli EC |
| Dom | Nov 05 | Dominica XXIII post Pentecosten |
| Fer II | Nov 06 | De VI die infra In Festo Omnium Sanctorum |
| Fer III | Nov 07 | De VII die infra In Festo Omnium Sanctorum |
| Fer IV | Nov 08 | In Festo Omnium Sanctorum |
| Fer V | Nov 09 | In Dedicatione Archibasilicæ Ssmi Salvatoris |
| Fer VI | Nov 10 | S Andreæ Avellini C |
| Sabb | Nov 11 | S Martini EC |
| Dom | Nov 12 | Dominica XXIV post Pentecosten, V Epiphania |
| Fer II | Nov 13 | S Didaci C |
| Fer III | Nov 14 | S Josaphat EM |
| Fer IV | Nov 15 | S Alberti Magni ECD |
| Fer V | Nov 16 | S Gertrudis V |
| Fer VI | Nov 17 | S Gregorii Thaumaturgi EC |
| Sabb | Nov 18 | In Dedicatione Basilicarum Ss Petri et Pauli App |
| Dom | Nov 19 | Dominica XXV post Pentecosten, VI Epiphania |
| Fer II | Nov 20 | S Felicis de Valois C |
| Fer III | Nov 21 | In Præsentatione BMV |
| Fer IV | Nov 22 | S Cæciliæ VM |
| Fer V | Nov 23 | S Clementis I PM |
| Fer VI | Nov 24 | S Joannis a Cruce CD |
| Sabb | Nov 25 | S Catharinæ VM |
| Dom | Nov 26 | Dominica XXVI et ultima post Pentecosten |
| Fer II | Nov 27 | De ea |
| Fer III | Nov 28 | De ea |
| Fer IV | Nov 29 | De ea |
| Fer V | Nov 30 | S Andreæ Ap |
| Fer VI | Dec 01 | De ea |
| Sabb | Dec 02 | De ea |
| Dom | Dec 03 | Dominica I Adventus |
| Fer II | Dec 04 | S Petri Chrysologi ECD |
| Fer III | Dec 05 | S Sabbae Abb |
| Fer IV | Dec 06 | S Nicolai EC |
| Fer V | Dec 07 | S Ambrosii ECD |
| Fer VI | Dec 08 | In Conceptione Immaculata BMV |
| Sabb | Dec 09 | De II die infra In Conceptione Immaculata BMV |
| Dom | Dec 10 | Dominica II Adventus |
| Fer II | Dec 11 | S Damasi I PC |
| Fer III | Dec 12 | De V die infra In Conceptione Immaculata BMV |
| Fer IV | Dec 13 | S Luciæ VM |
| Fer V | Dec 14 | De VII die infra In Conceptione Immaculata BMV |
| Fer VI | Dec 15 | In Conceptione Immaculata BMV |
| Sabb | Dec 16 | S Eusebii EM |
| Dom | Dec 17 | Dominica III Adventus |
| Fer II | Dec 18 | De ea |
| Fer III | Dec 19 | De ea |
| Fer IV | Dec 20 | Feria IV Quattuor Temporum in Adventus |
| Fer V | Dec 21 | S Thomæ Ap |
| Fer VI | Dec 22 | Feria VI Quattuor Temporum in Adventus |
| Sabb | Dec 23 | Sabbatum Quattuor Temporum in Adventus |
| Dom | Dec 24 | Vigilia Nativitas DNJC |
| Fer II | Dec 25 | Nativitas DNJC |
| Fer III | Dec 26 | S Stephani Protomartyris |
| Fer IV | Dec 27 | S Joannis Ap Ev |
| Fer V | Dec 28 | Ss Innocentium Mm |
| Fer VI | Dec 29 | S Thomæ EM |
| Sabb | Dec 30 | S Silvestri I PC |
| Dom | Dec 31 | Dominica Infra Octavam Nativitatis |
