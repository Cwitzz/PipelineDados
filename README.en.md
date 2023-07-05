# Data Pipeline for Product Recommendation System

This project represents a sophisticated data pipeline aimed at building a product recommendation system with a focus on data engineering practices, machine learning, and automated testing.

## 🧱 Pipeline Components

### 1. Database Creation

The `create_database.py` script creates a SQLite database called `DBFIC.db`. The database contains a collection of gardening product transactions with fictional data, generated using the Faker library, including names, addresses, prices, quantities, and more.

### 2. Data Cleaning and Transformation

The `data_cleaning_transform.py` script performs various data cleaning and transformation operations, including handling missing values, format conversion, and normalization of numerical features using pandas, scikit-learn, and NumPy.

### 3. Recommendation Model Training

The `model_training_product_recomm.py` is responsible for training a machine learning model for product recommendation. The model and encoders are serialized into `.pkl` files for reuse.

### 4. Inserting Recommendations into the Database

The `insert_recommendations.py` script applies the trained model to generate personalized recommendations that are inserted into the `DBFIC.db` database.

### 5. Performance Evaluation

The `evaluate_perfomance_model.py` script calculates performance metrics relevant to recommendation systems, such as precision, recall, F1 score, among others.

### 6. Automated Testing

The project includes automated tests in the `Test_model_training_product_recomm.py` and `test_data_cleaning_transform.py` scripts to verify the integrity of functions and results.

### 7. Documentation

The `README.md` file provides information about the configuration, project objectives, execution instructions, and explanations of the pipeline components.

## ⚙️ Scalability and Performance

The project is designed with a focus on scalability and performance, with the ability to handle larger datasets and integrate with cloud data platforms.

## 🚀 Conclusion

This pipeline is a robust solution for building a product recommendation system. It encompasses everything from database creation to model performance evaluation, ensuring quality, testability, and scalability. Data analysis stages have not been developed yet, as the project's focus was not on that.

## 👨‍💻 How to Run

### Prerequisites
Make sure you have Python 3.11 installed on your machine. Additionally, you will need a few Python libraries. You can install them using pip:
`pip install pandas scikit-learn sqlite3 joblib faker numpy random`

Not all libraries may be required, so it is recommended to use an Integrated Development Environment (IDE) to open the project.

### Step 1: Setting up the Database
First, you need to create and populate the database with fictional data. Use the `create_database.py` script for this.
`python create_database.py`

### Step 2: Data Cleaning, Preprocessing, and Transformation
After setting up the database, run the `data_cleaning_transform.py` script to clean and transform the data.
`python data_cleaning_transform.py`

### Step 3: Training the Recommendation Model
Now that the data is ready, you can train the recommendation model. Execute the `model_training_product_recomm.py` script.
`python model_training_product_recomm.py`

### Step 4: Evaluating Model Performance
Evaluate the model's performance using the `evaluate_performance_model.py` script. This will provide useful metrics for understanding the actual value of the model.
`python evaluate_performance_model.py`

### Step 5: Inserting Recommendations into the Database
Finally, use the `insert_recommendations.py` script to insert the generated recommendations into the database.
`python insert_recommendations.py`

This step may be irrelevant as, with updates, this functionality has been incorporated into the model training script.

### Execution Conclusion
After running these scripts in the specified order, you will have a trained product recommendation model ready to use. The recommendations will be stored in the SQLite database and can be accessed as needed.

## Considerations
I want to make it clear that if you want to use this pipeline for study purposes, you need to adapt all aspects of the code to your own conditions. For example, the database name, paths, and even the DBMS used for the database, or even not using a database and changing it to Excel data, for example.

Furthermore, the scripts are written specifically for the table created by the initial script. If you want to use different tables with different characteristics, you will need to adapt the entire chain of scripts.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
