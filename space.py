import pymunk

import data

class create_space:

    def __init__(self):

        self.space=pymunk.Space()
        self.space.gravity=(0,data.gravity)
        self.space.damping=data.damping

        self.edge()

    def edge(self):

        line_body_top=pymunk.Body(body_type=pymunk.Body.STATIC)
        line_body_left=pymunk.Body(body_type=pymunk.Body.STATIC)
        line_body_right=pymunk.Body(body_type=pymunk.Body.STATIC)
            
        line_shape_top=pymunk.Segment(line_body_top,(0,0),(data.win_w,0),5)
        line_shape_left=pymunk.Segment(line_body_left,(0,0),(0,data.win_h),5)
        line_shape_right=pymunk.Segment(line_body_right,(data.win_w,0),(data.win_w,data.win_h),5)

        self.space.add(line_body_top,line_shape_top)
        self.space.add(line_body_left,line_shape_left)
        self.space.add(line_body_right,line_shape_right)

    def close(self):

        del self.space
