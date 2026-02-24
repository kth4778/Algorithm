SELECT 
    E.EMP_NO, E.EMP_NAME, G.GRADE, G.PERCENT * E.SAL AS BONUS
FROM 
    HR_EMPLOYEES E
JOIN (
    SELECT
        CASE
            WHEN AVG(SCORE) >= 96 THEN 'S'
            WHEN AVG(SCORE) >= 90 THEN 'A'
            WHEN AVG(SCORE) >= 80 THEN 'B'
            ELSE 'C'
            END AS GRADE,
        CASE
            WHEN AVG(SCORE) >= 96 THEN 0.2
            WHEN AVG(SCORE) >= 90 THEN 0.15
            WHEN AVG(SCORE) >= 80 THEN 0.1
            ELSE 0
            END AS PERCENT,
        EMP_NO
    FROM HR_GRADE
    GROUP BY EMP_NO
) G ON E.EMP_NO = G.EMP_NO
ORDER BY
    EMP_NO ASC;