import torch
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from utils import sample_noise, show_images, deprocess_img, preprocess_img

def train(D, G, D_solver, G_solver, discriminator_loss, generator_loss, show_every=250, 
              batch_size=128, noise_size=100, num_epochs=10, train_loader=None, device=None, MNIST=False):
    """
    Train loop for GAN.
    
    The loop will consist of two steps: a discriminator step and a generator step.
    
    (1) In the discriminator step, you should zero gradients in the discriminator 
    and sample noise to generate a fake data batch using the generator. Calculate 
    the discriminator output for real and fake data, and use the output to compute
    discriminator loss. Call backward() on the loss output and take an optimizer
    step for the discriminator.
    
    (2) For the generator step, you should once again zero gradients in the generator
    and sample noise to generate a fake data batch. Get the discriminator output
    for the fake data batch and use this to compute the generator loss. Once again
    call backward() on the loss and take an optimizer step.
    
    You will need to reshape the fake image tensor outputted by the generator to 
    be dimensions (batch_size x input_channels x img_size x img_size).
    
    Use the sample_noise function to sample random noise, and the discriminator_loss
    and generator_loss functions for their respective loss computations.
    
    
    Inputs:
    - D, G: PyTorch models for the discriminator and generator
    - D_solver, G_solver: torch.optim Optimizers to use for training the
      discriminator and generator.
    - discriminator_loss, generator_loss: Functions to use for computing the generator and
      discriminator loss, respectively.
    - show_every: Show samples after every show_every iterations.
    - batch_size: Batch size to use for training.
    - noise_size: Dimension of the noise to use as input to the generator.
    - num_epochs: Number of epochs over the training dataset to use for training.
    - train_loader: image dataloader
    - device: PyTorch device
    """
    iter_count = 0
	
    # For running on GPU
    dtype = torch.cuda.FloatTensor
	
    for epoch in range(num_epochs):
        print('EPOCH: ', (epoch+1))
        for x, _ in train_loader:
            _, input_channels, img_size, _ = x.shape
            
            real_images = preprocess_img(x).to(device)  # normalize
            
            # Store discriminator loss output, generator loss output, and fake image output
            # in these variables for logging and visualization below
            d_error = None
            g_error = None
            fake_images = None
            
            ####################################
            #          YOUR CODE HERE          #
            ####################################
            ######## Discriminator Step ########
            # maximize log(D(x)) + log(1 - D(G(z))) 
            ####### Train with real batch ######
            ####################################
            # Zero out optimizer gradients
            #	Discussion: https://stackoverflow.com/questions/48001598/why-do-we-need-to-call-zero-grad-in-pytorch
            D_solver.zero_grad()
            real_data = torch.tensor(x).type(dtype)
            logits_real = D(2* (real_data - 0.5)).type(dtype)
            #print("\n\nlogits_real: " + str(logits_real))

            ####################################
            ####### Train with fake batch ######
            ####################################
            g_fake_seed = torch.tensor(sample_noise(batch_size, noise_size, MNIST=MNIST)).type(dtype)
            #print("\n\ng_fake_seed shape: " + str(g_fake_seed.shape))
            fake_images = G(g_fake_seed).detach()
            logits_fake = D(fake_images.view(batch_size, input_channels, img_size, img_size))
            #print("logits_fake: " + str(logits_fake))

            d_error = discriminator_loss(logits_real, logits_fake)
            #print("\n\nd_error: " + str(d_error))
            # 
            # Call backward() on the loss output and take an optimizer step for the discriminator.
            # 
            d_error.backward()        
            D_solver.step()

            ####################################
            ########## Generator Step ##########
            ####### maximize log(D(G(z))) ######
            ####################################
            G_solver.zero_grad()
            g_fake_seed = torch.tensor(sample_noise(batch_size, noise_size, MNIST=MNIST)).type(dtype)
            fake_images = G(g_fake_seed)

            gen_logits_fake = D(fake_images.view(batch_size, input_channels, img_size, img_size))
            g_error = generator_loss(gen_logits_fake)
            #print("\n\ng_error: " + str(g_error))
            # 
            # Call backward() on the loss output and take an optimizer step for the generator.
            # 
            g_error.backward()
            G_solver.step()
            
            ##########       END      ##########
            
            # Logging and output visualization
            if (iter_count % show_every == 0):
                print('Iter: {}, D: {:.4}, G:{:.4}'.format(iter_count,d_error.item(),g_error.item()))
                disp_fake_images = deprocess_img(fake_images.data)  # denormalize
                imgs_numpy = (disp_fake_images).cpu().numpy()
                show_images(imgs_numpy[0:16], color=input_channels!=1)
                plt.show()
                print()
            iter_count += 1