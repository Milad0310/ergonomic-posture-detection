import math

def calculate_angle(x1, y1, x2, y2, x3, y3):
  
        '''Calculates the angle between two arm segments in degrees using the Law of Cosines.
        This function takes the coordinates of three joints (shoulder, elbow, and wrist)
        and calculates the angle between the upper arm (shoulder-elbow) and the lower arm
        (elbow-wrist). It leverages the Law of Cosines, a fundamental formula in trigonometry
        used to find missing angles or side lengths in triangles. '''

        # Calculate the vector lengths for each arm segment
        upper_arm_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        lower_arm_length = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)

        # Ensure we don't have division by zero (shoulders and elbow can't coincide)
        if upper_arm_length == 0:
            return 0

        # Calculate the dot product of the normalized arm segment vectors
        dot_product = ((x2 - x1) / upper_arm_length) * ((x3 - x2) / lower_arm_length) + \
                        ((y2 - y1) / upper_arm_length) * ((y3 - y2) / lower_arm_length)

        # Apply the law of cosines to find the angle
        angle_rad = math.acos(dot_product)

        # Convert from radians to degrees
        angle_deg = int(180 / math.pi) * angle_rad

        return angle_deg