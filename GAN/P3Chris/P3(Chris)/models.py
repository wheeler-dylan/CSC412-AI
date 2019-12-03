#CHRIS

import torch


class Discriminator(torch.nn.Module):
    def __init__(self, input_channels=3):
        super(Discriminator, self).__init__()
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        n_features = 784
        n_out = 1
        
        self.hidden0 = torch.nn.Sequential( 
            torch.nn.Linear(n_features, 1024),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Dropout(0.3)
        )
        self.hidden1 = torch.nn.Sequential(
            torch.nn.Linear(1024, 512),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Dropout(0.3)
        )
        self.hidden2 = torch.nn.Sequential(
            torch.nn.Linear(512, 256),
            torch.nn.LeakyReLU(0.2),
            torch.nn.Dropout(0.3)
        )
        self.out = torch.nn.Sequential(
            torch.nn.Linear(256, n_out),
            torch.nn.Sigmoid()
        )

        
        ##########       END      ##########
    
    def forward(self, x):
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.hidden0(x)
        x = self.hidden1(x)
        x = self.hidden2(x)
        x = self.out(x)
        
        ##########       END      ##########
        
        return x


class Generator(torch.nn.Module):
    def __init__(self, noise_dim, output_channels=3):
        super(Generator, self).__init__()    
        self.noise_dim = noise_dim
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        n_features = 100
        n_out = 784
        
        self.hidden0 = torch.nn.Sequential(
            torch.nn.Linear(n_features, 256),
            torch.nn.LeakyReLU(0.2)
        )
        self.hidden1 = torch.nn.Sequential(            
            torch.nn.Linear(256, 512),
            torch.nn.LeakyReLU(0.2)
        )
        self.hidden2 = torch.nn.Sequential(
            torch.nn.Linear(512, 1024),
            torch.nn.LeakyReLU(0.2)
        )
        
        self.out = torch.nn.Sequential(
            torch.nn.Linear(1024, n_out),
            torch.nn.Tanh()
        )
        
        ##########       END      ##########
    
    def forward(self, x):
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.hidden0(x)
        x = self.hidden1(x)
        x = self.hidden2(x)
        x = self.out(x)
        
        ##########       END      ##########
        
        return x
    


