# 产品推荐数据管道

本项目是一个复杂的数据管道，旨在构建一个以数据工程实践、机器学习和自动化测试为重点的产品推荐系统。

## 🧱 管道组件

### 1. 创建数据库

`create_database.py`脚本创建一个名为`DBFIC.db`的SQLite数据库。该数据库包含一个包含虚构数据的园艺产品交易集合，使用Faker库生成，包括姓名、地址、价格、数量等信息。

### 2. 数据清洗和转换

`data_cleaning_transform.py`脚本执行多种数据清洗和转换操作，包括处理缺失值、格式转换以及使用Pandas、Scikit-learn和NumPy对数值特征进行规范化。

### 3. 推荐模型训练

`model_training_product_recomm.py`负责训练一个用于产品推荐的机器学习模型。模型和编码器将被序列化为`.pkl`文件以便重用。

### 4. 推荐结果插入数据库

`insert_recommendations.py`脚本应用训练好的模型生成个性化推荐，并将其插入到`DBFIC.db`数据库中。

### 5. 性能评估

`evaluate_perfomance_model.py`脚本计算与推荐系统相关的性能指标，如准确率、召回率、F1得分等。

### 6. 自动化测试

该项目还包括`Test_model_training_product_recomm.py`和`test_data_cleaning_transform.py`脚本的自动化测试，用于验证函数和结果的完整性。

### 7. 文档

`README.md`文件提供有关配置、项目目标、执行说明以及管道组件的解释。

## ⚙️ 可扩展性和性能

该项目专注于可扩展性和性能，可以处理更大的数据集并与云数据平台集成。

## 🚀 结论

该管道是构建产品推荐系统的强大解决方案。它涵盖了从数据库创建到模型性能评估的所有步骤，确保质量、可测试性和可扩展性。由于该项目的重点不在数据分析阶段，因此尚未开发数据分析阶段的内容。

## 👨‍💻 如何运行

### 先决条件
确保您的机器上安装了Python 3.11。此外，您还需要一些Python库。您可以使用pip安装它们：
`pip install pandas scikit-learn sqlite3 joblib faker numpy random`

可能不需要所有库，因此建议使用集成开发环境（IDE）打开项目。

### 步骤1：设置数据库
首先，创建并填充数据库以包含虚构数据。使用`create_database.py`脚本执行此操作。
`python create_database.py`

### 步骤2：数据清洗、预处理和转换
设置好数据库后，运行`data_cleaning_transform.py`脚本清洗和转换数据。
`python data_cleaning_transform.py`

### 步骤3：训练推荐模型
现在数据已经准备好，可以训练推荐模型了。执行`model_training_product_recomm.py`脚本。
`python model_training_product_recomm.py`

### 步骤4：评估模型性能
使用`evaluate_performance_model.py`脚本评估模型的性能。这将提供有用的指标来了解模型的实际价值。
`python evaluate_performance_model.py`

### 步骤5：将推荐结果插入数据库
最后，使用`insert_recommendations.py`脚本将生成的推荐结果插入数据库。
`python insert_recommendations.py`

这一步可能不相关，因为通过更新，该功能已直接整合到模型训练脚本中。

### 执行结论
按照指定的顺序运行这些脚本后，您将拥有一个已训练好的产品推荐模型可供使用。推荐结果将存储在SQLite数据库中，并可根据需要进行访问。

## 注意事项
请注意，如果您要将此管道用于学习目的，则需要根据自己的条件调整代码的各个方面。例如，数据库名称、路径甚至数据库管理系统（DBMS）的选择，或者甚至不使用数据库而改为使用Excel数据等。

此外，这些脚本是专门针对初始脚本创建的表编写的。如果您要使用不同的具有不同特征的表格，您将需要调整整个脚本链。

## 📄 许可证

本项目基于MIT许可证。详细信息请参阅[LICENSE](LICENSE)文件。
