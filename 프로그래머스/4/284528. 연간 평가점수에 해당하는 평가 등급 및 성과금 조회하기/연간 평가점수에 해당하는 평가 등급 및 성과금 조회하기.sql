# HR_DEPARTMENT 테이블
# HR_EMPLOYEES 테이블
# HR_GRADE 테이블

WITH AVG_SCORE_INFO AS (
    SELECT EMP_NO, 
            AVG(SCORE) AS AVG_SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
),
EMP_INFO AS (
    SELECT HR_EMPLOYEES.EMP_NO,
            HR_EMPLOYEES.EMP_NAME,
            HR_EMPLOYEES.SAL,
            AVG_SCORE_INFO.AVG_SCORE,
            CASE
                WHEN AVG_SCORE_INFO.AVG_SCORE >= 96
                THEN 'S'
                WHEN AVG_SCORE_INFO.AVG_SCORE >= 90
                THEN 'A'
                WHEN AVG_SCORE_INFO.AVG_SCORE >= 80
                THEN 'B'
                ELSE 'C' 
            END AS GRADE,
            CASE
                WHEN AVG_SCORE_INFO.AVG_SCORE >= 96
                THEN 20
                WHEN AVG_SCORE_INFO.AVG_SCORE >= 90
                THEN 15
                WHEN AVG_SCORE_INFO.AVG_SCORE >= 80
                THEN 10
                ELSE 0
            END AS BONUS_PERCENT
    FROM HR_EMPLOYEES, AVG_SCORE_INFO
    WHERE HR_EMPLOYEES.EMP_NO = AVG_SCORE_INFO.EMP_NO
)

SELECT EMP_NO, 
        EMP_NAME, 
        GRADE,
        SAL * (BONUS_PERCENT / 100) AS BONUS
FROM EMP_INFO
ORDER BY EMP_NO