NOTE: IT'S FOR EXTRACT THE REVIEWS FROM THE AMAZON.
---------------------------------------------------

Step 1: open https://www.soax.com and create account.
soax.com will provide you proxy which will keep changing the IP address and server itself.
------------------------------------------------------------------------------------------
Step 2: Replace the proxy with "xxxx-->paste Proxy<--xxxx" on line no. 10 & 11.
-------------------------------------------------------------------------------
Step 3: Get on the review page of the product and copy link till question mark('?') excluding question mark('?') and replace it with "xxxx-->paste Link<--xxxx" on line no. 38.
for example:
if the whole link is: "https://www.amazon.in/Apple-iPhone-Mini-128GB-Starlight/product-reviews/B09G91Q79X/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
then, we need to replace "xxxx-->paste Link<--xxxx" with "https://www.amazon.in/Apple-iPhone-Mini-128GB-Starlight/product-reviews/B09G91Q79X/ref=cm_cr_dp_d_show_all_btm"
-----------------------------------------------
Step 4: Run the Code
--------------------
Step 5:
	a)check html folder, a excel file would be there named "file.html".
	b)uncomment the code from line no. 29 to 38.
	c)now we need to find the data-hook of Review Title, Rating and Review Body from the excel file on output folder and replace it on the line no. 32, 33, 34 respectively.
	d)now we need to find the review-title, review-star-rating and review-body of Review Title, Rating and Review Body from the excel file on output folder and replace it on the line no. 32, 33, 34 respectively.
------------------------
step 6: uncomment the code from line no. 54 to 58 and Run the Code Again, and the work is done let the code take time to run (extract reviews). once the code is executed completely check a excel file name "output.xlsx" on the same folder where the code is placed that excel file contains all the reviews of the product.
