# CAR_RENTAL_COMPANY_RENTAL_HISTORY 

SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID in (
                    SELECT CAR_ID
                    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                    WHERE YEAR(START_DATE) = '2022'
                        AND MONTH(START_DATE) >= '8' AND MONTH(START_DATE) <= '10'
                    GROUP BY CAR_ID
                    HAVING COUNT(*) >= 5
                )
        AND MONTH(START_DATE) >= '8' AND MONTH(START_DATE) <= '10'
GROUP BY MONTH, CAR_ID
HAVING RECORDS > 0
ORDER BY MONTH ASC, CAR_ID DESC
