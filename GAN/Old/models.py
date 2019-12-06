import torch


class Discriminator(torch.nn.Module):
    def __init__(self, input_channels=3):
        super(Discriminator, self).__init__()
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        # Filters [256, 512, 1024]
        # Input_dim = input_channels (Cx64x64)
        # Output_dim = 1
        self.main_module = torch.nn.Sequential(
            # Image (Cx32x32)
            torch.nn.Conv2d(in_channels = input_channels, out_channels=256, kernel_size=4, stride=2, padding=1),
            torch.nn.BatchNorm2d(num_features=256),
            torch.nn.LeakyReLU(0.2, inplace=True),

            # State (256x16x16)
            torch.nn.Conv2d(in_channels=256, out_channels=512, kernel_size=4, stride=2, padding=1),
            torch.nn.BatchNorm2d(num_features=512),
            torch.nn.LeakyReLU(0.2, inplace=True),

            # State (512x8x8)
            torch.nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=4, stride=2, padding=1),
            torch.nn.BatchNorm2d(num_features=1024),
            torch.nn.LeakyReLU(0.2, inplace=True))
            # output of main module --> State (1024x4x4)

        self.output = torch.nn.Sequential(
            # The output of D is no longer a probability, we do not apply sigmoid at the output of D.
            torch.nn.Conv2d(in_channels=1024, out_channels=1, kernel_size=4, stride=1, padding=0))
        
        ##########       END      ##########
    
    def forward(self, x):
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.main_module(x)
        x = self.output(x)
        
        ##########       END      ##########
        
        return x


class Generator(torch.nn.Module):
    def __init__(self, noise_dim, output_channels=3):
        super(Generator, self).__init__()    
        self.noise_dim = noise_dim
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        # Filters [1024, 512, 256]
        # Input_dim = 100
        # Output_dim = C (number of channels)
        self.main_module = torch.nn.Sequential(
            # Z latent vector 100
            torch.nn.ConvTranspose2d(in_channels=100, out_channels=1024, kernel_size=4, stride=1, padding=0),
            torch.nn.BatchNorm2d(num_features=1024),
            torch.nn.ReLU(True),

            # State (1024x4x4)
            torch.nn.ConvTranspose2d(in_channels=1024, out_channels=512, kernel_size=4, stride=2, padding=1),
            torch.nn.BatchNorm2d(num_features=512),
            torch.nn.ReLU(True),

            # State (512x8x8)
            torch.nn.ConvTranspose2d(in_channels=512, out_channels=256, kernel_size=4, stride=2, padding=1),
            torch.nn.BatchNorm2d(num_features=256),
            torch.nn.ReLU(True),

            # State (256x16x16)
            torch.nn.ConvTranspose2d(in_channels=256, out_channels = output_channels, kernel_size=4, stride=2, padding=1))
            # output of main module --> Image (Cx32x32)

        self.output = torch.nn.Tanh()

        ##########       END      ##########
    
    def forward(self, x):
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.main_module(x)
        x = self.output(x)
        
        ##########       END      ##########
        
        return x
    

