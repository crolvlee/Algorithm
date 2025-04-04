# FOOD_PRODUCT 테이블

SELECT FOOD_PRODUCT.CATEGORY, 
        FOOD_PRODUCT.PRICE AS MAX_PRICE,
        FOOD_PRODUCT.PRODUCT_NAME
FROM FOOD_PRODUCT
JOIN (
    SELECT CATEGORY, MAX(PRICE) AS CATEGORY_MAX
    FROM FOOD_PRODUCT
    WHERE CATEGORY = '과자' 
            OR CATEGORY = '국'
            OR CATEGORY = '김치'
            OR CATEGORY = '식용유'
    GROUP BY CATEGORY 
) AS NEW_TABLE
ON FOOD_PRODUCT.CATEGORY = NEW_TABLE.CATEGORY
    AND FOOD_PRODUCT.PRICE = NEW_TABLE.CATEGORY_MAX
ORDER BY MAX_PRICE DESC

