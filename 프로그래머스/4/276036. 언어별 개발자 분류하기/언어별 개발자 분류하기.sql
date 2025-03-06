# SKILLCODES 테이블
# DEVELOPERS 테이블

WITH FE_SKILLS AS (
    SELECT SUM(CODE) AS CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
), 
CSHARP_SKILLS AS (
    SELECT CODE
    FROM SKILLCODES
    WHERE NAME = 'C#'
), 
PYTHON_SKILLS AS (
    SELECT CODE
    FROM SKILLCODES
    WHERE NAME = 'Python'
),
DEVELOPERS_GRADE AS (
    SELECT CASE
                WHEN (SKILL_CODE & (SELECT CODE FROM FE_SKILLS)) != 0
                    AND (SKILL_CODE & (SELECT CODE FROM PYTHON_SKILLS)) != 0
                THEN 'A'
                WHEN (SKILL_CODE & (SELECT CODE FROM CSHARP_SKILLS)) != 0
                THEN 'B'
                WHEN (SKILL_CODE & (SELECT CODE FROM FE_SKILLS)) != 0
                THEN 'C'
            END AS GRADE,
            ID,
            EMAIL
    FROM DEVELOPERS
    ORDER BY GRADE ASC, ID ASC
)

SELECT * FROM DEVELOPERS_GRADE
WHERE GRADE IS NOT NULL

