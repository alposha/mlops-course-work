import pandas as pd

data = pd.read_csv('Anime_reviews_RU.csv')
print(f"Исходный датасет: {data.shape}")

data = data.drop(data.columns[[0, 1]], axis=1)
print(f"После удаления столбцов: {data.shape}")

data = data.dropna(subset=['Text'])
print(f"После удаления пропущенных: {data.shape}")

data = data.drop_duplicates(subset=['Text'])
print(f"После удаления дубликатов: {data.shape}")

data.to_csv('data/processed/cleaned_data.csv', index=False, encoding='utf-8-sig')
print("Очищенная версия датасета сохранена")

data['formatted'] = '__label__' + data['Rate'] + ' ' + data['Text']
data[['formatted']].to_csv('data/processed/fasttext_format.txt', index=False, header=False, sep='\t')
print("Версия датасета для fasttext сохранена")