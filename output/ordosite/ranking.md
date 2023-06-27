---
layout: rubric_layout
category: rubrics
title: "Rubrics"
back: /rubrics
---

This numbering system is essential to the proper working of the ranking system.

# Occurance

1. Sunday of 1st class
2. Primary Feasts D1 throughout the Church Universal
3. The Circumcision of Our Lord -- Ash Wednesday -- All the Ferial Days in Holy Week -- The days within the octaves of Easter and Pentecost -- The Vigils of Christmas and Pentecost,
4. The Octave Day of an Octave of the Second Rank
5. The Dedication and Titular Feasts of One's Own Church -- The Principal Patron of the Place -- The Titular Feast, and the Feast of the Holy Founder of the Order or Religious Congregation,
6. Other Feasts, if there be any, which are Primary of Double Rite of the First Class for the Place, 
7. Other Feasts, if there be any, which are Secondary of Double Rite of the First Class for the Place, 
8. Sunday of 2nd class
9.  The Days within the Octaves of the Second Rank,
10. D2
11. DM Feasts of Our Lord,
12. Minor Sundays, and the Vigil of the Epiphany,
13. The Octave Day of an Octave of the Third Rank, or of a Common Octave, which is of Major Double Rite
14. DM, not of Our Lord,
15. D,
16. SD,
17. The Days within the Octaves of Christmas and the Ascension,
18. The days within Common Octaves,
19. The Major Ferial Days and Vigils,
20. The Octave Day of a Simple Octave, *i.e.,* of a Feast of the Second Class,
21. The Saturday Office of the Blessed Virgin Mary,
22. Feasts of Simple Rite.
23. De ea

# Rules for transfer

These are placed in a tuple `(x, x, x, x, x,)`, which is used to determine the exact nobility of a feast.

### Rite

Placed at index `0`.

1. d I cl
2. d II cl
3. dm
4. d
5. sd
8. s (v)
9. feria

### Solemnity

Placed at index `1`.

1. day of rest of precept
2. not day of rest

Placed at index `2`.

1. 1st order
2. 2nd order
3. 3rd order
4. common
5. simple
6. none

### Person

Placed at index `3`.

1. God
2. Blessed Virgin
3. Angels
4. Prophets and Patriarchs
5. Apostles and Evangelists
6. Disciples
7. Martyrs
8. Bishops and Confessors
9. Doctors
10. Priests and Levites
11. Monks and Hermits
12. Virgins and Widows
13. False

### Quality of Primary or Secondary Feasts

Placed at index `4`.

1. Primary feast
2. Secondary feast
3. Neither primary nor secondary

### Quality of the Proper

Placed at index `5`.

Just put `0` for now. This will be used farther down the pipeline.
<!-- complicated... p. 306 in Matters Liturgical -->

### Some common rankings: 

- Feria     `(9, 2, 6, 13, 3, 0,)`,
- Confessor `(4, 2, 6,  8, 3, 0,)`,
- Martyr    `(5, 2, 6,  7, 3, 0,)`
