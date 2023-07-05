# ⚔️ Challenges Faced

## Data Creation:
Initially, the idea was to create a super simple database in a txt file, but I immediately realized that it would make the process much more difficult.
The first change was to create data about books in Excel format, with few columns such as publication date, author, etc...

However, after moving on to the next steps, I encountered several problems, and the main one was the lack of complexity in this data. Basically, applying the things I wanted to apply in the future wouldn't make sense because there was nothing to extract from it.
#### 🏁 Finally, after dedicating more time, I created a database, nothing complex, but already in a database format, a table with columns, 1000 customer names using a library that generates fake data. This table had 1000 rows with 8 columns. Immediately, many possibilities opened up.

## 🧹 Data Cleaning, Pre-processing, and Transformation
Initially, everything was working smoothly, but this stage depends a lot on the next one. While developing the training models, I realized additional needs for complexity. For example, when running the model, the initial data format was causing the process to be very slow, very slow indeed!

After some time struggling, I came to some conclusions. I modified the values in the `sex` column to binary, which considerably improved the training speed of the model. Additionally, I encoded the `customer_name` and `product` columns, which greatly facilitated the use of machine learning methods.

Using the k-means method, I applied clustering to the data, further simplifying future processes. To learn more, you can research the k-means method and data clustering.

There were many other adaptations that resulted in a significant increase in training speed. I monitored the speed increase, and the numbers were astonishing.
#### Initial Execution Time: 48 min 50 s
#### Final Execution Time: 22.56 s
#### Total time reduction of 99.2% and a 128x increase in speed

## 🤖 Model Training for Product Recommendation
Surprisingly, this stage was one of the smoothest. All the necessary implications to ensure smooth execution were applied in the previous stage. I encountered some syntax and indentation problems, but they were quickly resolved. One of the challenges I faced was with a library called `surprise`, as I wasn't able to use it as effectively and encountered compatibility issues, so I reverted back to using `scikit-learn`. This stage went through many changes, but the most significant one was breaking down the scripts into microfunctions to facilitate the implementation of Test Driven Development (TDD).

Breaking down the script into microfunctions was one of the biggest challenges.

## ✔️ Model Performance Evaluation
I didn't encounter any issues with this script. I was pleased with the applications used, and it became much easier after running the model script. The considerations for this stage are more focused on the results themselves.

#### Comparing the metrics:

#### First Evaluation (Model 1):

#### MSE: 103.782312548213  MAE: 27.321351528391  R-squared (R2): -1.2131267381625
#### To better understand, research the 3 methods: MSE, MAE, R2. However, the first evaluation indicated that the model was TERRIBLE.
#### Second Evaluation:
#### MSE: 23.85376567930002  MAE: 3.605650000000001  R-squared (R2): 0.7809557859075236

##### In the second evaluation, both MSE and MAE decreased significantly compared to the first evaluation. MSE is a metric that measures the mean squared error, so a lower value is better. MAE is a metric that measures the mean absolute error, and a lower value is also desirable.

##### Additionally, the R-squared (R2) value increased in the second evaluation. R2 is a metric that indicates the proportion of the variance in the target data captured by the model. A value closer to 1 is considered a good fit of the model to the data.
