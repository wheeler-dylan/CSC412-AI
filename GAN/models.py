import torch
from torch.nn import ConvTranspose2d, Conv2d, ReLU, Tanh, LeakyReLU, Sequential, BatchNorm2d, MaxPool2d

class Discriminator(torch.nn.Module):
    """
    Discriminator:

    convolutional layer with in_channels=3, out_channels=128, kernel=4, stride=2
    convolutional layer with in_channels=128, out_channels=256, kernel=4, stride=2
    batch norm
    convolutional layer with in_channels=256, out_channels=512, kernel=4, stride=2
    batch norm
    convolutional layer with in_channels=512, out_channels=1024, kernel=4, stride=2
    batch norm
    convolutional layer with in_channels=1024, out_channels=1, kernel=4, stride=1
    Instead of Relu we LeakyReLu throughout the discriminator (we use a negative slope value of 0.2).

    The output of your discriminator should be a single value score corresponding to each input sample. 
    See torch.nn.LeakyReLU.
    """
    def __init__(self, input_channels=3):
        super(Discriminator, self).__init__()
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        
        self.hidden0 = Sequential(
            # input is (3) x 64 x 64
            Conv2d(input_channels, 128, kernel_size=4, stride=2, padding=1, bias=False),
            LeakyReLU(0.2, inplace=True)
        )
        self.hidden1 = Sequential(     
            # state size (128) x 32 x 32  
            #  without padding (128) x 31 x 31
            # Formula (W - K + 2P / S) + 1;  W is input size, K is kernel size, P is padding, S is stride
            Conv2d(128, 256, kernel_size=4, stride=2, padding=1, bias=False),
            BatchNorm2d(256),
            LeakyReLU(0.2, inplace=True)
        )
        self.hidden2 = Sequential(
            # state size (256) x 16 x 16 
            #  without padding (256) x 14 x 14 - note that dividing 27 by 2 yields fraction, which gets rounded down
            Conv2d(256, 512, kernel_size=4, stride=2, padding=1, bias=False),
            BatchNorm2d(512),
            LeakyReLU(0.2, inplace=True)
        )
        self.hidden3 = Sequential(
            # state size (512) x 8 x 8 
            # without padding  (512) x 6 x 6
			Conv2d(512, 1024, kernel_size=4, stride=2, padding=1, bias=False),
            BatchNorm2d(1024),
            LeakyReLU(0.2, inplace=True)

        )        
        self.out = Sequential(
            # state size (1024) x 4 x 4
            # without padding (1024) x 3 x 3
			Conv2d(1024, 1, kernel_size=4, stride=1, padding=1, bias=False),
            #BatchNorm2d(256),
            LeakyReLU(0.2, inplace=True)

        )
        
        ##########       END      ##########
    
    def forward(self, x):
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.hidden0(x)
        x = self.hidden1(x)
        x = self.hidden2(x)
        x = self.hidden3(x)
        x = self.out(x)
        
        ##########       END      ##########
        
        return x


class Generator(torch.nn.Module):
    """
    Generator:

    Note: In the generator, you will need to use transposed convolution (sometimes known as fractionally-strided convolution or 
    deconvolution). This function is implemented in pytorch as torch.nn.ConvTranspose2d.

    transpose convolution with in_channels=NOISE_DIM, out_channels=1024, kernel=4, stride=1
    batch norm
    transpose convolution with in_channels=1024, out_channels=512, kernel=4, stride=2
    batch norm
    transpose convolution with in_channels=512, out_channels=256, kernel=4, stride=2
    batch norm
    transpose convolution with in_channels=256, out_channels=128, kernel=4, stride=2
    batch norm
    transpose convolution with in_channels=128, out_channels=3, kernel=4, stride=2
    The output of the final layer of the generator network should have a tanh nonlinearity to output values between -1 and 1. 
    The output should be a 3x64x64 tensor for each sample (equal dimensions to the images from the dataset).
    """
    def __init__(self, noise_dim, output_channels=3):
        super(Generator, self).__init__()    
        self.noise_dim = noise_dim
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        
        self.hidden0 = Sequential( 
            # input size noise dimension, which for PA3 is 100
            ConvTranspose2d(noise_dim, 1024, kernel_size=4, stride=1, padding=0, bias=False),
            BatchNorm2d(1024),
            ReLU(True)
        )
        self.hidden1 = Sequential(
            # state size (1024) x 4 x 4      
            # Inverse of Formula (W - K + 2P / S) + 1 for up-sampling
            # W is input size, K is kernel size, P is padding, S is stride
			ConvTranspose2d(1024, 512, kernel_size=4, stride=1, padding=0, bias=False),
            BatchNorm2d(512),
            ReLU(True)

        )
        self.hidden2 = Sequential(
            # state size (512) x 8 x 8 
			ConvTranspose2d(512, 256, kernel_size=4, stride=1, padding=0, bias=False),
            BatchNorm2d(256),
            ReLU(True)

        )
        self.hidden3 = Sequential(
            # state size (256) x 16 x 16 
			ConvTranspose2d(256, 128, kernel_size=4, stride=1, padding=0, bias=False),
            BatchNorm2d(128),
            ReLU(True)

        )
        self.out = Sequential(
            # state size (128) x 32 x 32 
            ConvTranspose2d(128, output_channels, kernel_size=4, stride=2, padding=1, bias=False),
            # output size (3) x 64 x 64 
            Tanh()
        )

        
        ##########       END      ##########
    
    def forward(self, x):
        
        ####################################
        #          YOUR CODE HERE          #
        ####################################
        x = self.hidden0(x)
        x = self.hidden1(x)
        x = self.hidden2(x)
        x = self.hidden3(x)
        x = self.out(x)
        
        ##########       END      ##########
        
        return x
    

