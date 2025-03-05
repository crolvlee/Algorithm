# FOOD_PRODUCT 테이블
# FOOD_ORDER 테이블

SELECT
    FOOD_PRODUCT.PRODUCT_ID,
    FOOD_PRODUCT.PRODUCT_NAME,
    FOOD_PRODUCT.PRICE * SUM(FOOD_ORDER.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT, FOOD_ORDER
WHERE FOOD_PRODUCT.PRODUCT_ID = FOOD_ORDER.PRODUCT_ID
    AND FOOD_ORDER.PRODUCE_DATE LIKE '2022-05-%'
GROUP BY FOOD_ORDER.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC