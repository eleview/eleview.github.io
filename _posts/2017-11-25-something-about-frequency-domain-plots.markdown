---
layout: post
title: Something about Frequency-Domain Plots
use_math: true
---

When we are having lessons such as [***Signals and Systems***][1], or [***Digital Signal Processing***][2], teacher will always mention something called [***Fourier Transformation***][3]. Now we are going to leave Fourier Transformation alone ~~because I did quite bad in the two lessons~~ and focus on another awful thing called [***Frequency-Domain***][4] ***Plot***. Something I faced in my Digital Image Processing class just showed the cuteness of the Plot.

**Frequency-Domain Plot** shows frequency features of signals, instead of temporal features showed in [Time-Domain][5] Plots, or position features showed in Space-Domain Plots. Usually it is quite easy for us to understand Time-Domain or Space-Domain Plots. For example, below is an image showed in my DIP class:

<div align="center">
    <img src="SDP_ori.gif" width = "120" height = "120" alt="DIP Image" />
</div>

And the corresponding FDP is as follows:

<div align="center">
    <img src="FDP_ori.png" width = "120" height = "120" alt="DIP Image FDP" />
</div>

At least, I felt one face confused when facing this strange FDP. I can't even tell what the image is about according to it. Well, maybe every ordinary person will find it impossible to tell it on his first glance. However, computers can find much valuable information in it.

## Where are FDPs from?

The answer is: **Fourier Transformation.** ~~Oh f**k, Fourier again!~~ And as for images, 2D Fourier Transformation.

The transformation formula is as follows. Turn elsewhere if any other problems.

<font size=4>
    $$F(u,v) =\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}f(x,y)e^{-j2\pi(ux+vy)}dxdy$$
</font>

The 2DFT is to perform FT twice, respectively on the two different axes. Since the *x* and *y* axes are independent, sequence doesn't count.

## Please be Detailed!

OK. The MATLAB program of the process is listed as follows:

```
clear;clc;
I=imread('SDP_ori.gif');
I1=double(I);
fftI=fft2(I1);
sfftI=fftshift(fftI);
[N1,N2]=size(sfftI);
n=2;
RR=real(sfftI);
II=imag(sfftI);
A=sqrt(RR.^2+II.^2);
A=(A-min(min(A)))/(max(max(A))-min(min(A)))*255;
subplot(2,1,2);
imshow(A);
B2=ifftshift(sfftI);
B1=ifft2(B2);
B=uint8(B1);
subplot(2,1,1);
imshow(B);
```

And an FDP is generated. Function [<code>fft2</code>][8] is to perform 2DFT on the image, and function [<code>fftshift</code>][9] is to make the initial point the center of the FDP. Process <code>A=(A-min(min(A)))/(max(max(A))-min(min(A)))*255</code> is to make the FDP a grayscale with pixel values ranging from 0-255.

## And So What?

We do not get the FDP just to look at it.

Take filting as an example. The original image has some background noise on it. We are trying to erase it by filting. At the beginning, we have [band-pass][6] filter and [band-stop][7] filters. Note that now we only know that band-pass filter is to let pass only a specific range of frequency values and blocks others, while band-stop filter is to block a specific range of frequency values and let others pass. We don't know if the noise is related to anything about frequency and the two kinds of filters.

After countless of trials and errors, we decide to use band-stop filter with 13 and 18 as boundary frequency values. Then we get the new FDP as follows:

<div align="center">
    <img src="FDP_bandstop.png" width = "120" height = "120" alt="Band stop FDP" />
</div>

and the new image as follows:

<div align="center">
    <img src="SDP_bandstop.png" width = "120" height = "120" alt="Band stop SDP" />
</div>

Seems like it is better. But why?

We should start with the information of the FDP.

## FDP Represents What?

Take the FDP below as an example.

<div align="center">
    <img src="FDP_ori.png" width = "120" height = "120" alt="DIP Image FDP" />
</div>

In fact, FDP represents frequency and the rapidness of frequency changes in specific directions, i.e. gradient of the pixels in the image.

A white point on the FDP shows that there is existence of pixel gradient satisfying condition **A** and **B**. **A** is *the direction is the same as that from the initial point to the selected white point*, and **B** is *the gradient value equals the distance from the initial point to the selected white point*.

Therefore, it is easy to understand why the image 
has a large white area at the center. The image is mostly covered by pure-color areas.

We can see that there are two diagonal white lines in the FDP. Believe it or not, these represent the gradient of the roof.

You say **NO** ?! OK. Here is the FDP left only the two lines. This means that we only preserve the gradient with diagonal directions.

<div align="center">
    <img src="FDP_roof.png" width = "120" height = "120" alt="Gradient FDP" />
</div>

And the new image is as follows:

<div align="center">
    <img src="SDP_roof.png" width = "120" height = "120" alt="Gradient SDP" />
</div>

OK you should believe it.

When it comes to band-stop filters, it blocks a specific range of frequency values \(for example 13 to 18\). Then on the FDP, it looks like blocking a circle of frequency points by making them black.

<div align="center">
    <img src="FDP_bandstop.png" width = "120" height = "120" alt="Band stop FDP" />
</div>

## Brain Hurricaning

Wait. If we only use band-stop filters, why should we still trying to obtain FDP? We want something better than band-stop filters, even though it may be impossible in reality. Fortunately, it can be realised by FDP.

Take a closer look, and you will discover that the noise only has horizontal gradient. At this time, you, intelligent and creative, certainly have an idea. Why not only remove the horizontal lines in the FDP?

<div align="center">
    <img src="FDP_modified.png" width = "120" height = "120" alt="Modified FDP" />
</div>

Fortunately we receive better results.

<div align="center">
    <img src="SDP_modified.png" width = "120" height = "120" alt="Modified SDP" />
</div>

## In Conclusion,

FDP is a powerful tool for frequency analyses and filting. It breaks the limit of band-stop or band-pass. With an FDP, you can remove whatever you want, and even build an impossible-in-reality powerful filter.

Remember that all of these owe everything to

<div align="center">
<font size=6>
    Baron Jean Baptiste Joseph Fourier
</font>
</div>

<div align="center">
    <img src="Fourier.jpg" width = "315" height = "207" alt="Fourier" />
</div>

By [zcc31415926][10].

[1]: https://en.wikipedia.org/wiki/Signal#Signals_and_systems
[2]: https://en.wikipedia.org/wiki/Digital_signal_processing
[3]: https://en.wikipedia.org/wiki/Fourier_transform
[4]: https://en.wikipedia.org/wiki/Frequency_domain
[5]: https://en.wikipedia.org/wiki/Time_domain
[6]: https://en.wikipedia.org/wiki/Band-pass_filter
[7]: https://en.wikipedia.org/wiki/Band-stop_filter
[8]: https://cn.mathworks.com/help/matlab/ref/fft2.html?lang=en
[9]: https://cn.mathworks.com/help/matlab/ref/fftshift.html?lang=en
[10]: https://github.com/zcc31415926