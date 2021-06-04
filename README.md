# softcomp
Finetuning mobilenet v2 for face mask detection task, the classes in this work are:
 - Masked (correct)
 - Masked (incorrect)
 - Unmasked
<br>
Two step classification method is used, opencv nn ssd face detector is used to detect the location of faces in an images and the mobilenet v2 classifier trained is used to classify the faces into one of the three categories above.
<br>
Dataset used are from two sources:
 - https://github.com/cabani/MaskedFace-Net (correctly masked faces, incorrectly masked faces)
 - https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset (correctly masked faces, unmasked faces)
