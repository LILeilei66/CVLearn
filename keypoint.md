https://docs.opencv.org/2.4/modules/features2d/doc/common_interfaces_of_feature_detectors.html
#### Data Structure
```
class KeyPoint():
    Point2f pt
        # Coordinates
    
    float size
        # diameter
    
    float angle
        # oriatation
    
    int octave
        # pytramid layer
       
    int class_id
        # object id to cluster keypoints
```
    