# BOOK 테이블
# AUTHOR 테이블
# BOOK_SALES 테이블

SELECT NEW_BOOK.AUTHOR_ID,
        AUTHOR.AUTHOR_NAME,
        NEW_BOOK.CATEGORY,
        SUM(NEW_BOOK.TOTAL_PRICE) AS TOTAL_SALES
FROM (
        SELECT BOOK.BOOK_ID, 
            BOOK.CATEGORY, 
            BOOK.AUTHOR_ID, 
            BOOK.PRICE * BOOK_CNT.TOTAL_CNT AS TOTAL_PRICE
        FROM BOOK
        LEFT JOIN (
            SELECT BOOK_ID, SUM(SALES) AS TOTAL_CNT
            FROM BOOK_SALES
            WHERE SALES_DATE LIKE '2022-01%'
            GROUP BY BOOK_ID
        ) AS BOOK_CNT
        ON BOOK.BOOK_ID = BOOK_CNT.BOOK_ID
    ) AS NEW_BOOK,
    AUTHOR
WHERE NEW_BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
GROUP BY NEW_BOOK.CATEGORY, NEW_BOOK.AUTHOR_ID
ORDER BY NEW_BOOK.AUTHOR_ID ASC, NEW_BOOK.CATEGORY DESC