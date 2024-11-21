# eVTOL-AirfoilModel

This project uses Element Spatial Convolutional Neural Networks (ESCNN) to predict aerodynamic coefficients—lift (Cl) and drag (Cd)—based on airfoil geometry.
The model is trained on data from the UIUC Airfoil Database (~40000 datasets).

The initial architecture is inspired by the work of Peng et al. [1], which introduced ESCNN for efficient aerodynamic predictions by directly using airfoil coordinates. 
This lightweight model achieves real-time predictions with minimal computational cost.
The architecture has been further customized to improve accuracy and integrate with the larger eVTOL aerodynamic model.

## Performance
1. Cl Predictions: Highly accurate results.
2. Cd Predictions: Needs improvement. This issue has been addressed in eVTOL-WingModel repository using transfer learning.

## Integration
This model serves as a key component of a larger data-driven framework for eVTOL aerodynamics.

## References
W. Peng, Y. Zhang, and M. Desmarais, "Spatial Convolution Neural Network for Efficient Prediction of Aerodynamic Coefficients," AIAA SciTech Forum, 2021. DOI: 10.2514/6.2021-0277.