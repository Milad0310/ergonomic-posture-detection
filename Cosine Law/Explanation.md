 Calculates the angle between two arm segments in degrees using the Law of Cosines.

  This function takes the coordinates of three joints (shoulder, elbow, and wrist)
  and calculates the angle between the upper arm (shoulder-elbow) and the lower arm
  (elbow-wrist). It leverages the Law of Cosines, a fundamental formula in trigonometry
  used to find missing angles or side lengths in triangles.

  **Steps:**

  1. **Vector Length Calculations:**
     - The function first calculates the lengths of the upper arm (`upper_arm_length`)
       and lower arm (`lower_arm_length`) using the Euclidean distance formula. This
       formula measures the straight-line distance between two points based on their
       coordinate differences.

  2. **Input Validation:**
     - A crucial check is performed to ensure the upper arm length is not zero. A zero
       length would indicate that the shoulder and elbow points coincide, which is
       physically impossible. If this condition is met, a `ValueError` is raised to
       prevent errors in downstream calculations.

  3. **Normalized Dot Product:**
     - The function calculates the dot product of the normalized (unit-length) vectors
       representing the upper and lower arm segments. Normalization ensures that vector
       lengths don't influence the calculation, focusing solely on their directional
       relationship. The dot product itself measures the extent to which two vectors point
       in the same direction.

  4. **Law of Cosines:**
     - The Law of Cosines is applied to find the angle between the two arm segments.
       This formula relates the side lengths of a triangle (in this case, the upper and
       lower arm lengths) and the cosine of the angle opposite the known side length
       (the angle between the two arms). The dot product calculated earlier serves
       as the cosine value in this context.

  5. **Conversion to Degrees:**
     - The angle obtained from the Law of Cosines is in radians. The function converts
       this value to degrees for a more user-friendly interpretation.

  6. **Return Value:**
     - The function returns the calculated angle between the two arm segments in degrees
       as an integer.

  **Applications:**
   - This function can be used in various applications requiring arm posture analysis,
     such as ergonomics assessments, human-computer interaction studies, and motion
     capture systems. By calculating the angles between different arm segments,
     information about posture and movement patterns can be obtained.