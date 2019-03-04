# Windowing (CT)
The intensity of CT image does not correspond with RGB image. <br>
It has own intensity level called [hounsfield unit(HU)](https://en.wikipedia.org/wiki/Hounsfield_scale). <br>
Windowing is kind of grey-level mapping, contrast stretching, histogram modification or contrast enhancement with respect to HU. <br>
There are some terms in windowing: <br>
* window width (WW) : the measure of the range of CT numbers that an image contains. (wider : 2000 HU, narrow: < 1000 HU) <br>
* wide window : 400-2000 HU best at lungs or cortical tissue <br>
* narrow window : 50-350 HU best for soft tissue that looks like similar neighborhood <br>
* window level(WL)/center : midpoint of HU range. <br>
Else : Follow reference.
# Reference
[Windowing (CT)](https://radiopaedia.org/articles/windowing-ct)
