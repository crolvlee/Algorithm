SELECT A_O.ANIMAL_ID, A_O.NAME
FROM ANIMAL_INS A_I
RIGHT JOIN ANIMAL_OUTS A_O
ON A_I.ANIMAL_ID = A_O.ANIMAL_ID
WHERE A_I.ANIMAL_ID is NULL
ORDER BY A_O.ANIMAL_ID