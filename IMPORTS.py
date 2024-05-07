'''Redes Neural'''

class NeuralNetworkRegressor(nn.Module):
    def __init__(self, input_size, hidden_size1, hidden_size2, learning_rate=0.1, dropout_prob=0.3, momentum=0.8):
        super(NeuralNetworkRegressor, self).__init__()
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.dropout_prob = dropout_prob
        self.momentum = momentum
        
        # Primeira camada oculta
        self.hidden_layer1 = nn.Linear(input_size, hidden_size1)
        self.hidden_activation1 = nn.ReLU()
        
        # Segunda camada oculta
        self.hidden_layer2 = nn.Linear(hidden_size1, hidden_size2)
        self.hidden_activation2 = nn.ReLU()
        
        # Camada de saída
        self.output_layer = nn.Linear(hidden_size2, 1)
        
        # Dropout
        self.dropout = nn.Dropout(p=dropout_prob)
        
        # Otimizador com Momento
        self.optimizer = optim.SGD(self.parameters(), lr=learning_rate, momentum=momentum)
        
        # Função de perda (Mean Squared Error)
        self.criterion = nn.MSELoss()
    
    def forward(self, x):
        # Primeira camada oculta
        hidden_output1 = self.hidden_layer1(x)
        hidden_output1 = self.hidden_activation1(hidden_output1)
        
        # Dropout (apenas durante o treinamento)
        if self.training:
            hidden_output1 = self.dropout(hidden_output1)
        
        # Segunda camada oculta
        hidden_output2 = self.hidden_layer2(hidden_output1)
        hidden_output2 = self.hidden_activation2(hidden_output2)
        
        # Dropout (apenas durante o treinamento)
        if self.training:
            hidden_output2 = self.dropout(hidden_output2)
        
        # Camada de saída
        output = self.output_layer(hidden_output2)
        return output
    
    def train_model(self, X_train, y_train, epochs):
        for epoch in range(epochs):
            # Ativa o modo de treinamento
            self.train()
            
            # Realiza a propagação direta
            outputs = self(X_train)
            
            # Calcula a perda
            loss = self.criterion(outputs, y_train)
            
            # Retropropagação e atualização dos pesos
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            
            # Mostra a perda a cada 100 épocas
            if (epoch + 1) % 100 == 0:
                print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item()}')
                
    def predict(self, X, num_samples=10, ):
        """
        Realiza a previsão com base nos dados de entrada fornecidos usando Monte Carlo Dropout.

        Args:
            X (torch.Tensor): Os dados de entrada para prever.
            num_samples (int): O número de amostras de dropout a serem usadas (default 10).

        Returns:
            torch.Tensor: A média das previsões feitas com diferentes amostras de dropout.
        """
        # Ativa o modo de avaliação
        self.eval()
        
        # Lista para armazenar as previsões
        self.predictions = []
        
        # Realiza múltiplas previsões com diferentes amostras de dropout
        for _ in range(num_samples):
            with torch.no_grad():
                outputs = self(X)
                self.predictions.append(outputs)
        
        # Calcula a média das previsões
        predictions_mean = torch.stack(self.predictions).mean(dim=0)
        return predictions_mean


'''Neural Reticulados'''

def neural_reticulados():
    
    # Parâmetros da rede neural
    input_size = 8
    hidden_size1 = 32
    hidden_size2 = 16
    epochs = 2000
    learning_rate = 0.01

    # Criação e treinamento da rede neural
    neural_net = NeuralNetworkRegressor(input_size, hidden_size1, hidden_size2, learning_rate)
    neural_net.train_model(X_test_scaled_tensor, Y_test_tensor_dimensionado, epochs)
    
    
    return prediction