# Notes
- Approximate_Scattering.pdf - Draft of paper where I discuss corrected methods.

# Python Notebooks/Files:
- State-Prep-Givens.ipynb - The primary notebook for qiskit simulations.
- givens_angles.py - Contains the functions to generate Givens angles for simulation. Called in State-Prep-Givens.ipynb. givens_angles.ipynb is for testing and copying into Julia simulations.
- vqe.ipnb - VQE code for our modified Ising model ground state preparation. So far I have only run classical simulations. Will need quantum or more efficient classical VQE simulation for $N>12$. After determining the number of ansatz layers needed to minimize $\Delta E$, it saves the angles to a file that is called in State-Prep-Givens.ipynb. Make sure $N,J,g,h$ match in State-Prep-Givens.ipynb.
- approx-trunc-compare.ipynb - Notebook with numpy simulations.
- tebd-analysis.ipynb - Used to plot Julia data.
- Old files- State-Prep-ibm_rensseelaer.ipynb, State-Prep_backend_run.ipynb, State-Prep_noise_model.ipynb, qft_ferris.ipynb.

# Julia Notebooks:
- ising-tebd-trunc.ipynb - TEBD simulations of our truncated wavepackets. I copy and paste the necessary Givens angles from givens-angles.ipynb.
- ising-tebd-approx.ipnb - Nearly identical to file above, just with $\sigma^- \rightarrow \sigma^x$ in the state preparation. No longer needed, but it was enlightening to see the effect.
