# Rotation is subset of affine transformation.
Rotation of image is subse of affine transformation. <br>
`Affine transformation` is the form of a vector addition with a matrix multiplication. <br>
```
* Matrix multiplication is `linear transformation`. <br>
* Vector addition is `translation`.<br>
```

Affine transformation can be applied to: <br>
```
* Rotations (l.t.)
* Translations (v.a.)
* Scale operations (l.t.)
```

Fundamentally, affine transformation indicates a relationship between two images. <br>
Basic Form of affine transformation is 2x3 matrix. <br>
```
A = [[a00, a01],[a10, a11]], B=[[b00],[b10]] <br>
M = [A B] = [[a00, a01, b00],[a10, a11, b10]] <br>
```

If x = [[x],[y]], <br>
```
T = A[[x],[y]] + B or T = M[[x],[y],[1]]<br>
T = [[a00x+a01y+b00],[a10x+a11y+b10]]<br>
```

# About rotation
Rotation has its own matrix M: <br>
```
[[cos, -sin],[sin, cos]]
```
After that, the other thing is the same as affine transformation.<br>
I'll add the example after. <br>

# Reference
[Affine Transformations](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/warp_affine/warp_affine.html)
