# Evaluation Questions for the MedicentreV3 Stock Assistant

## Current stock questions
1. Which table stores current stock quantities?
2. Where is available stock recorded?
3. Which table contains batch and expiry information?
4. Where is reorder level information represented?
5. What kind of stock information is stored in tblitemstoragelocations?

## Stock movement questions
6. Which table represents stock movement history?
7. How is stock movement represented in the system?
8. How can I know whether stock increased or decreased?
9. Where are stock changes like opening stock or sales recorded?
10. What does tblstockchanges store?

## Stock take questions
11. Which table stores stock take sessions?
12. How does the system handle stock take sessions?
13. Which table shows whether a stock take has been committed?
14. What does tblstocktakes contain?
15. Which table should I check for stock verification workflow?

## Item and branch questions
16. Which table stores general item definitions?
17. What is the role of tblitems in the stock module?
18. Which table links items to a specific branch?
19. How are stock items linked to branches?
20. What does tblcompanybranchitems store?

## Comparison questions
21. What is the difference between tblitems and tblcompanybranchitems?
22. What is the difference between tblitemstoragelocations and tblstockchanges?
23. What is the difference between current stock and stock movement tables?
24. What is the relationship between tblitems, tblcompanybranchitems, and tblitemstoragelocations?
25. Which table is best for current stock questions and which is best for stock history questions?

## Boundary questions
26. Can I say that tblitems directly stores current stock quantities?
27. Can I say that tblstockchanges stores the current stock balance?
28. Can I say that tblstocktakes stores individual stock movement records?
29. If the schema does not clearly support a claim, how should the assistant respond?
30. If a question is outside the stock module, how should the assistant respond?