# Importação das bibliotecas necessárias
from sklearn.datasets import load_breast_cancer  # Dataset do câncer de mama
from sklearn.ensemble import RandomForestClassifier  # Algoritmo Random Forest
from sklearn.model_selection import train_test_split  # Divisão de dados
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score  # Métricas de avaliação

# Carregando o dataset
data = load_breast_cancer()

# Características: data.data (matriz com 30 atributos para cada amostra)
# Rótulos: data.target (0 = maligno, 1 = benigno)

# Dividindo os dados: 70% treino, 30% teste — com random_state para reprodutibilidade
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

# Inicializando o modelo Random Forest com parâmetros padrão
model = RandomForestClassifier()

# Treinando o modelo
model.fit(X_train, y_train)

# Realizando as previsões
y_pred = model.predict(X_test)               # Previsões de classe (0 ou 1)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probabilidades para a classe 1

# Calculando as métricas de avaliação
precision = precision_score(y_test, y_pred)          # Precisão: TP / (TP + FP)
recall = recall_score(y_test, y_pred)                # Recall (Sensibilidade): TP / (TP + FN)
f1 = f1_score(y_test, y_pred)                        # F1-Score: harmônico entre precisão e recall
auc = roc_auc_score(y_test, y_pred_proba)            # AUC-ROC: capacidade de discriminação

# Exibindo os resultados
print(f"""
Métricas de Avaliação do Modelo Random Forest:

Precisão  : {precision:.2f} 
Recall    : {recall:.2f}
F1-Score  : {f1:.2f}
AUC-ROC   : {auc:.2f}
""")
