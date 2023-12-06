---
title: "BMES 621: Homework 1"
author: "Tony Kabilan Okeke"
date: "2023-10-24"
---

Please see the questions below and submit your answers to BBLearn as a Word-file (with 
equations included) or as a pdf of scanned handwritten solutions (needs to be clearly 
readable). It is recommended to review the “Modern Microscopies” paper to answer some 
of the questions. 

1. **What are the two types of optical aberrations noticed by the YouTubers (see posted 
   video under week 2) for the Leica Noctilux 0.95? What do these aberrations cause to 
   the quality of the image (in approx. 4 sentences)? [10]**

   - **Field Curvature** -  This makes it difficult to precisely focus the lens across
     the entire image plane, resulting in a curved focal plane. This causes the edges
     and corners of the image to appear blurry and out of focus even when the center is
     sharply focused.
   - **Color Fringing** - This is a form of chromatic aberration caused by the failure
     of a lens system to focus all colors on the same point. It causes colored artifacts
     and halos along high-contrast edges in the image. This ultimately reduced the 
     sharpness of the images taken.

2. **What are the practical benefits for a user to be able to adjust the size of the 
   pinhole in a confocal microscope? Describe each benefit with 2-3 sentences, name at
   least two benefits. [10]**

   - **Improved Signal-to-Noise Ratio** - By adjusting the pinhole, users can change the
     signal-to-noise ratio of the images they take. Larger pinholes permit more out of
     focus light to reach the sensor which tends to produce brighter images. On the 
     other hand, smaller pinholes produce sharper, more dim, images.

   - **Improved Resolution** - A smaller pinhole  allows less out-of-focus light to 
     reach the sensor, which improves the optical resolution. 

3. **How does the numerical aperture and magnification impact the brightness of 
   fluorescence in a confocal microscope? Discuss/explain using an equation. [10]**

   - **Numerical Aperture, NA**
     - The brightness *b* of fluorescent images increases proportionally to the squqare
       of the numerical aperture of the lens *L* and condenser *C*, and decreases 
       inversely with the square of the total magnification *M*:

       $b \sim \left(\ \text{NA}_L^2 \times \text{NA}_C^2 \right)^2 \times \frac{1}{M^2}$

     - The NA determines the amount of light that can be collected from a specimen, thus
       a higher NA gathers more light, resulting in brighter images.

   - **Magnification, M**
     - At epi-illumination the brightness depends on the fourth power of the numerical
       aperture, since the lens acts as the condenser as well:

       $b \sim \frac{\text{NA}^4}{M^2}$

     - At higher magnification, the same amount of fluorescence is concentrated onto a
       smaller area on the detector, increasing the number of photons per pixel. This
       creates a brighter image

4. **For a wavelength of 500 nm and a numerical aperture of NA 1.0, what is the 
   (lateral/xy) resolution of a fluorescence microscope? Compare to the (lateral) 
   resolution of a confocal microscope. How much is it improved? Include applicable 
   equations. [20]**
   \begin{align*}
      \lambda &= 500~\text{nm} \\
      NA &= 1.0 \\
      \text{For Fluorescence Microscope:}& \\
      d &= 0.5\cdot\frac{\lambda}{\text{NA}^2} \\
        &= 0.5\cdot\frac{500~\text{nm}}{1.0} \\
        &= 250~\text{nm} \\
      \text{For Confocal Microscope:}& \\
      d &= 0.46\cdot\frac{\lambda}{\text{NA}^2} \\
        &= 0.46\cdot\frac{500~\text{nm}}{1.0} \\
        &= 230~\text{nm} \\
      \text{\% Improvement:}& \\
      &= \frac{|250 - 230|}{250} \cdot 100\% \\
      &= 8\%
   \end{align*}

   - The lateral resolution of the confocal microscope shows an 8% improvement over
     the fluorescence microscope.

5. **What is the axial (z) resolution of a confocal microscope with a wavelength of 500 
   nm, NA 1.0? Provide the equation and solution. [20]**
   \begin{align*}
      d &= 1.4\cdot\frac{\lambda}{\text{NA}^2} \\
        &= 1.4\cdot\frac{500~\text{nm}}{1.0^2} \\
        &= 700~\text{nm}
   \end{align*}

\newpage

6. a. **You adjust a digital camera to a microscope. We assume a wavelength of 500 nm 
   and a lens with an NA =1.0,  what needs the sampling rate/pixel size of the 
   sensor/CCD camera to be? (Remark: For simplicity we ignore the effect of 
   magnification). [20]**
   \begin{align*}
      \lambda &= 500~\text{nm} \\
      \text{NA} &= 1.0 \\
      d &= \frac{\lambda}{2\cdot\text{NA}} \\
        &= \frac{500~\text{nm}}{2\cdot1} \\
        &= 250~\text{nm} \\
      \text{Nyquist sampling }&\text{theorem:}\\
      \text{pixel size} &\leq \frac{d}{2} \\
      \implies \text{pixel size} &\leq 125~\text{nm}
   \end{align*}

   b. **(BMES 621 only) You purchase a cell phone with a 61 megapixel (MP) camera, 
   which has a CCD chip of 5.4 x 3.6 mm in size.  You also know that the optics of this 
   cellphone has an opening of f/2.0. Is this CCD too good (meaning too many pixels) 
   for the resolution delivered by the optics (assume 500 nm green light)? 
   Explain. Hint: you would need to determine (or look up) the pixel size for such a 
   CCD chip. [10]**
   \begin{align*}
      \text{resolution} &= 61~\text{MP} \\
      \text{CCD size}   &= 5.4\times3.6~\text{mm} \\
      \text{aperture, f/\#}   &= \text{f/2.0} \\
      \lambda &= 500~nm \\
      \\
      \text{aspect ratio} &= 
         \frac{\text{number of pixels (width)}}{\text{number of pixels (height)}} \\
                          &= \frac{5.4~\text{mm}}{3.6~\text{mm}} = 1.5 \\
      \text{number of pixels (width)} \times \text{number of pixels (height)} &= 61~\text{MP} \\
      \text{number of pixels (width)} &= \sqrt{61\times10^6\cdot1.5} \\
                                      &= 9566 \\
      \text{number of pixels (height)} &= \frac{61\times10^6}{9566} \\
                                       &= 6377 \\
      \text{pixel size (w)} &= \frac{5.4}{9566} \\ &= 564~\text{nm} \\
      \text{pixel size (h)} &= \frac{3.6}{6377} \\ &= 565~\text{nm} \\
      d &= \frac{\lambda}{2\cdot\text{NA}} \\
        &= \frac{\lambda}{2\cdot\frac{1}{\text{f/\#}}} \\
        &= \frac{500~nm}{2\cdot0.5} \\
        &= 500~\text{nm}
   \end{align*}

   - Comparing the pixel sizes (564nm, 565nm) with the resolution (500), we see that
     the pixel size is slightly larger than the diffreaction-limited resolution. Thus,
     the CCD resolution is higher than what the optics can produce.

   c. **(BMES 421 only). Show that your cell phone becomes “noisy” at low light levels. 
   Document with an image taken under normal light conditions, and the same scene under 
   low light. You can crop the images before you integrate them into your word/pdf 
   file. [10]**

Max points: 100

