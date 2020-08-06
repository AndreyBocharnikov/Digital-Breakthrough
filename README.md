# Digital-Breakthrough
Machine learning contest.  
[Original task](https://cups.mail.ru/tasks/1030).  
English description: you are given 261 train examples of 6 classes of different pictures of bacteria and a description for each where exactly the bacteria are located, the task is to predict classes and do data segmentation.

#### My approach:
Note: the classes in the description are ordered in that way - `[c_kefir, ent_cloacae, klebsiella_pneumoniae, moraxella_catarrhalis, staphylococcus_aureus, staphylococcus_epidermidis]`.  

Firstly I did data augmentation to increase the size of the dataset. Then I trained a separate network for classification task. There are two types of images of the first class, and to improve performance of the segmentation on that class, I trained these types on two distinctive netwokrs.  
First class:![blue bacterium](https://github.com/AndreyBocharnikov/Digital-Breakthrough/tree/master/images/first_class_blue.png), ![black bacterium](https://github.com/AndreyBocharnikov/Digital-Breakthrough/tree/master/images/first_class_black.png)

Following the same goal I trained all last 3 classes in the same netwokr, following this method performance was higher than if these 3 classes were treated separately. Second and third class had their own networks.  

I used U-Net for all networks described above.
