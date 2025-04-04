# FIRST_HALF 테이블
# JULY 테이블

SELECT FIRST_HALF.FLAVOR
FROM FIRST_HALF
JOIN (
        SELECT FLAVOR, SUM(TOTAL_ORDER) AS J_TOTAL
        FROM JULY
        GROUP BY FLAVOR
    ) AS NEW_JULY
ON FIRST_HALF.FLAVOR = NEW_JULY.FLAVOR
GROUP BY FIRST_HALF.FLAVOR
ORDER BY FIRST_HALF.TOTAL_ORDER + NEW_JULY.J_TOTAL DESC
LIMIT 3