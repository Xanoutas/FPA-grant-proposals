// src/Adaptive/AdaptiveToolpath.cpp

#include "AdaptiveToolpath.h"
#include "AdaptiveUtils.h"

namespace Adaptive {

void AdaptiveToolpath::generateToolpath() {
    // Existing code...

    // Improve algorithm to enable successful generation at small stepovers
    if (stepover < 1.0) {
        // Adjust parameters for small stepovers
        maxStepover = stepover * 1.5;
        minStepover = stepover * 0.5;
    }

    // Improved automatic diameter selection for entry helix
    if (helixMaxDiameter == 0.0) {
        // Calculate automatic helix diameter based on tool diameter
        helixMaxDiameter = toolDiameter * 0.75;
    }

    // Ensure the helix diameter fits at the desired start location
    if (helixMaxDiameter > startLocationDiameter) {
        helixMaxDiameter = startLocationDiameter;
    }

    // Existing code...
}

} // namespace Adaptive