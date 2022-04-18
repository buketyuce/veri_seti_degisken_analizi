#Bir veri setindeki KATAGORİK ve SAYISAL değişkenlere göz atma

import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset("titanic") #Yazdığım fonksiyonları gözlemlemek için titanic veri seti üzerinde çalışmak istiyorum.
df.head()

# Katagorik Değişken Analizi #
#Veri seti içindeki kategorik değişkenleri seçtim.
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

#"int" tipli gözüken ama katagorik olan değişkenler mevcut, hayatta kalma durumu gibi. Onları da seçtim.
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

#sınıf sayısı çok fazla olduğu için ölçülemeyecek değişkenler olabilir, bunları belirledim.
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

#kategorik değişkenlere "int" tipli gözüken katagorikleri ekledim.
cat_cols = cat_cols + num_but_cat

#kategorik değişkenlerin içinde sınıf sayısı fazla olduğu için ölçülemeyecek olan sınıfları çıkardım.
cat_cols = [col for col in cat_cols if col not in cat_but_car]

#Genelleştirmek için bir fonksiyon yazdım. Fonksiyon sınıf sayısını ve oran bilgisini verecek.
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts()/len(dataframe)}))
    print("####################################################################")

for col in cat_cols:
    cat_summary(df,col)

# Sayısal değişken analizi #
#Sayısal değişkenleri seçtim.
num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

#Sayısal görünümlü katagorikleri sayısalların içinden çıkarttım.
num_cols = [col for col in num_cols if col not in cat_cols]

#Genelleştirmek için bir fonksiyon yazdım. Fonksiyon sayısal değişkenlere göz atmamı sağlayacak.
def num_summary(dataframe, numarical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numarical_col].describe(quantiles).T)

for col in num_cols:
    num_summary(df, col)











