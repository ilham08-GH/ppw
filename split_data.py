import os
import pandas as pd
from sklearn.model_selection import train_test_split

def split_tfidf_datasets():
    # Direktori input & output
    base_output_dir = 'Output'
    notebooks_output_dir = os.path.join('Notebooks', 'Output')
    
    os.makedirs(base_output_dir, exist_ok=True)
    os.makedirs(notebooks_output_dir, exist_ok=True)
    
    # Path file sumber
    path_full = os.path.join(base_output_dir, 'tfidf_berita.csv')
    path_500 = os.path.join(base_output_dir, 'tfidf_berita_500.csv')
    
    print(f"Membaca {path_full}...")
    df_full = pd.read_csv(path_full, index_col=0)
    
    print(f"Membaca {path_500}...")
    df_500 = pd.read_csv(path_500, index_col=0)
    
    # Melakukan split 60% training dan 40% testing secara berimbang (stratified)
    train_idx, test_idx = train_test_split(
        df_full.index,
        test_size=0.40,
        random_state=42,
        stratify=df_full['label']
    )
    
    # 1. Dataset TF-IDF Penuh
    full_train = df_full.loc[train_idx]
    full_test = df_full.loc[test_idx]
    
    # 2. Dataset TF-IDF 500 Fitur
    p500_train = df_500.loc[train_idx]
    p500_test = df_500.loc[test_idx]
    
    datasets = {
        'tfidf_berita_train.csv': full_train,
        'tfidf_berita_test.csv': full_test,
        'tfidf_berita_500_train.csv': p500_train,
        'tfidf_berita_500_test.csv': p500_test,
    }
    
    # Simpan ke Output/ dan Notebooks/Output/
    for filename, df_split in datasets.items():
        out_base = os.path.join(base_output_dir, filename)
        out_nb = os.path.join(notebooks_output_dir, filename)
        
        df_split.to_csv(out_base)
        df_split.to_csv(out_nb)
        print(f"Tersimpan: {out_base} & {out_nb} | Dimensi: {df_split.shape}")
        
    print("\nRingkasan Split (60% Train, 40% Test):")
    print(f"- Total dokumen: {len(df_full)}")
    print(f"- Data Training (60%): {len(train_idx)} dokumen -> {dict(full_train['label'].value_counts())}")
    print(f"- Data Testing  (40%): {len(test_idx)} dokumen -> {dict(full_test['label'].value_counts())}")

if __name__ == '__main__':
    split_tfidf_datasets()
