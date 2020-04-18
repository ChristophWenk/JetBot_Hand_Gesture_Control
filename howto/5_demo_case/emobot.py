from jetbot import Robot
import time

class Emobot(Robot):
    """ The Emobot class that defines the robot actions for the demo case.
    
    The Emobot extends the Robot class of the example projects and defines additional more complex movements.    
    """

    def __init__(self, *args, **kwargs):
        """ Initialize the Emobot class
    
        The settings have been empirically set by executing 10 spins. 
        Be aware that these settings might differ from JetBot to JetBot as no two motors are exactly the same.
        Therefore all units have to be considered as approximations.
        """
        super(Emobot, self).__init__(*args, **kwargs)
        self.rotation_speed = 0.3
        self.rotation_time_1_degree = 2.39 / 360
        self.max_degrees_sight = 80 # 160 / 2

    def rotate_left_by_sight(self, distance_from_center):
        """ Rotate to the left by a specified margin to match the center of the camera frame 
                        
        Input:
            distance_from_center: Amount of degrees the JetBot should turn
        """
        assert 0 <= distance_from_center <= 1, "distance_from_center must be between 0 and 1"
        self.left(self.rotation_speed)
        time.sleep(self.rotation_time_1_degree * self.max_degrees_sight * distance_from_center)
        self.stop()

    def rotate_right_by_sight(self, distance_from_center):
        """ Rotate to the right by a specified margin to match the center of the camera frame 
                
        Input:
            distance_from_center: Amount of degrees the JetBot should turn
        """
        assert 0 <= distance_from_center <= 1, "distance_from_center must be between 0 and 1"
        self.right(self.rotation_speed)
        time.sleep(self.rotation_time_1_degree * self.max_degrees_sight * distance_from_center)
        self.stop()
        
    def rotate_left(self, degree=60):
        """ Rotate to the left by a specified margin 
                
        Input:
            degree: Amount of degrees the JetBot should turn
        """
        self.left(self.rotation_speed)
        time.sleep(self.rotation_time_1_degree * degree)
        self.stop()

    def rotate_right(self, degree=60):
        """ Rotate to the right by a specified margin 
        
        Input:
            degree: Amount of degrees the JetBot should turn
        """
        self.right(self.rotation_speed)
        time.sleep(self.rotation_time_1_degree * degree)
        self.stop()

    def run_away(self):
        """ Turn around and drive away for a short distance """
        self.left(0.6)
        time.sleep(0.50)
        self.forward(0.6)
        time.sleep(0.5)
        self.stop()

    def shake_it(self, number_of_shakes=1):
        """ Shake it off a number of times
        
        Input
            number_of_shakes: Number of times the JetBot should shake
        """
        for x in range(number_of_shakes):
            self.left(0.5)
            time.sleep(0.10)
            self.right(0.5)
            time.sleep(0.10)
            self.left(0.5)
            time.sleep(0.10)
        self.stop()