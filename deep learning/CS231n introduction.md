# History of computer vision and deep learning

## computer vision

Senses promoted creatures' evolution. Evolution of vision is the evolution of intelligence. Vision drove the development of nervous system and the development of intelligence.

Understanding how visual intelligence happens is the crux of this course.

### Hubel and Wiesel, 1959

They used electrodes to put into live cats anesthetized.

Visual pathway is hierarchical.

### Larry Roberts, 1963

the first PhD thesis of computer vision

### Larry Roberts created a summer project in MIT, 1966

A few smart undergrads hired to study vision. The goal was pretty much solve computer vision or solve vision for one summer.

[The Summer Vision Project-Seymour Papert](https://dspace.mit.edu/handle/1721.1/6125)

### David Barr wrote a seminal book, 1970s

He wanted to study vision systematically and start to consider how visual processing happens.

It is difficult to rebuild 3-D representation from 2-D images.

### 1980s

Photos start to appear and people had digitized them a little bit.

There were some great work in edge detection.

#### AI winter(now we are in AI global warming period)

The enthusiasm and hence funding for AI research had really dwindled.

But a lot of researches started to grow from different fields

#### cognitive and neural science

It points to us the North Star problems.

AI worked and was taken in the industry early 21st century

Internet started to happen and data started to proliferate 

## deep learning

Data are important.

### back propagation,1986: Rumelhart,Hinton and Williams

They took neural network architecture and introduced an error correcting objective function.

input $\rightarrow$ output $\rightarrow$ input. Thus, the parameters along the neural network will be improved.

### deep learning explosion: 2012 to present

Computer vision's main annual research conference is called CVPR.

Many new algorithms have been invented to participate in the Image Net challenge in the following years.

# topics around computer vision in use of deep learning in this space

## deep learning basics

The core of computer vision: enabling machines to see and understand images( most fundamental task is image classification).

How to let machines do the task: one of the most simplest approaches is to use linear classification.

go deep into the details of how AI work, how AI are trained, and how to debug and improve AI.

## perceiving and understanding the visual world

a complex process that involves interpreting a vast area of visual information.

tasks: specific challenges or problems 

aims: have some functions like object detection, scene understanding motion detection and so on.

models: different, computational and theoretical. One of the examples is neural net.

align models and with tasks $\rightarrow$ create systems that can see and interpret the world.

### computer vision

push the model to do more than just recognizing categories

#### first: semantic segmentation

not just labeling the object or the entire image as objects but looking for labels for every single pixel in the image.

every single pixel can be an object. We don't distinguish between individual objects.

#### then: object detection

pinpoint the location $\rightarrow$ create bounding boxes around the objects and associate them with specific labels.

#### finally: instant segmentation

the most granular of all objects.

combine the ideas of detection and segmentation together.

every object instance gets its own mask.

### convolution neural networks( CNN)

a number of operations: get the details from an image.

a number of convolution sampling and fully connected operations.

create the output.

## generative and interactive visual intelligence

### self-supervised learning

make models learn to understand and represent data by getting some training signals from the data itself.

### generative modeling

Style Transfer: a classic application of neural generative techniques.

genetic models can translate language into images.

generative vision models blend understanding, creativity and control.

### vision language models

they connect text and images in a shared representation space and give a caption or image.

### 3-D vision

reconstruct and generate 3-D representations from images.

it is crucial for robotics and AI AR VR applications

## human-centered applications and implications

1. formalize computer vision applications into tasks
2. develop and train vision models
3. gain an understanding of where the field is and where it is headed