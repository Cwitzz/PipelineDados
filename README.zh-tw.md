# 數據流程管道 - 產品推薦系統

該專案代表了一個複雜的數據流程管道，旨在建立一個以數據工程實踐、機器學習和自動化測試為重點的產品推薦系統。

## 🧱 管道組件

### 1. 數據庫建立

`create_database.py`腳本創建了一個名為`DBFIC.db`的SQLite數據庫。該數據庫包含了一個虛構數據的園藝產品交易集合，使用了Faker庫生成，包括姓名、地址、價格、數量等等。

### 2. 數據清理和轉換

`data_cleaning_transform.py`腳本執行了各種數據清理和轉換操作，包括處理缺失值、格式轉換以及使用Pandas、Scikit-learn和NumPy進行數值特徵的正規化。

### 3. 推薦模型訓練

`model_training_product_recomm.py`負責訓練一個用於產品推薦的機器學習模型。模型和編碼器被序列化為`.pkl`文件以便重複使用。

### 4. 推薦結果插入數據庫

`insert_recommendations.py`腳本應用訓練好的模型生成個性化推薦，並將其插入到`DBFIC.db`數據庫中。

### 5. 效能評估

`evaluate_perfomance_model.py`腳本計算與推薦系統相關的效能指標，如準確率、召回率、F1得分等。

### 6. 自動化測試

該專案還包括`Test_model_training_product_recomm.py`和`test_data_cleaning_transform.py`腳本的自動化測試，用於驗證函數和結果的完整性。

### 7. 文件說明

`README.md`文件提供了有關配置、專案目標、執行指示以及管道組件的說明。

## ⚙️ 擴展性與效能

該專案專注於擴展性和效能，能夠處理更大的數據集並與雲端數據平台集成。

## 🚀 總結

該管道是構建產品推薦系統的堅實解決方案。從數據庫建立到模型效能評估，它涵蓋了所有步驟，確保質量、可測試性和擴展性。由於該專案的重點不在數據分析階段，因此尚未開發相關內容。

## 👨‍💻 執行方式

### 先決條件
請確保在您的計算機上安裝了Python 3.11。此外，您還需要一些Python庫。您可以使用pip安裝它們：
`pip install pandas scikit-learn sqlite3 joblib faker numpy random`

可能並不需要所有庫，因此建議使用一個集成開發環境（IDE）打開專案。

### 步驟 1：設置數據庫
首先，需要創建並填充數據庫以包含虛構數據。使用`create_database.py`腳本進行操作。
`python create_database.py`

### 步驟 2：數據清理、預處理和轉換
設置好數據庫後，運行`data_cleaning_transform.py`腳本對數據進行清理和轉換。
`python data_cleaning_transform.py`

### 步驟 3：訓練推薦模型
現在數據已準備好，可以訓練推薦模型了。執行`model_training_product_recomm.py`腳本。
`python model_training_product_recomm.py`

### 步驟 4：評估模型效能
使用`evaluate_performance_model.py`腳本評估模型的效能。這將提供有用的指標，以了解模型的實際價值。
`python evaluate_performance_model.py`

### 步驟 5：將推薦結果插入數據庫
最後，使用`insert_recommendations.py`腳本將生成的推薦結果插入數據庫。
`python insert_recommendations.py`

此步驟可能與實際情況無關，因為更新後，此功能已直接整合到模型訓練腳本中。

### 執行結論
按照指定的順序運行這些腳本後，您將擁有一個已訓練好並可立即使用的產品推薦模型。推薦結果將存儲在SQLite數據庫中，並可以根據需要進行訪問。

## 注意事項
請注意，如果您要將此管道用於學習目的，則需要根據自己的情況調整代碼的各個方面。例如，數據庫名稱、路徑甚至選擇的數據庫管理系統（DBMS），或者甚至不使用數據庫而改為使用Excel數據等。

此外，這些腳本是專門針對初始腳本創建的表格編寫的。如果您要使用不同的具有不同特徵的表格，則需要調整整個腳本鏈。

## 📄 授權

本專案根據MIT許可證進行許可。詳細信息請參閱[LICENSE](LICENSE)文件。
