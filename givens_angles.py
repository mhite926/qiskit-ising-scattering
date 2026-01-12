import numpy as np

# Create Given's rotation matrix
def Giv_Mat(N_s, theta, s):
    mat = np.identity(N_s, dtype=float)
    mat[s-1, s-1] = np.cos(theta)
    mat[s-1, s] = -np.sin(theta)
    mat[s, s-1] = np.sin(theta)
    mat[s, s] = np.cos(theta)
    return mat


# Get Given's Angles
## N_s: Size of system
## n_s: Size of subsystem
## x: position center
## n_k: momentum number (+ right moving, - left moving)
##      - For Ising PBC: odd # particles, even mom number;
##      - even # particles, odd mom number
##      - For Ising OBC: Always even mom number
## sigma: packet width in position space
## r: For N_s > n_s, provide |j-j_A| for all j in n_s
def giv_angles(N_s, n_s, x, n_k, sigma, r=None):
    # Momentum
    k = n_k * np.pi / N_s
    
    if N_s == n_s:
        r = np.arange(-N_s/2 + 1, N_s/2 + 1, 1)
        roll = int(x - (N_s/2 - 1))
        r = np.roll(r, roll)

        GWP_coeffs = []
        for i in range(N_s):
            coeff = np.exp(-1j * k * i) * np.exp(-r[i]**2 / sigma**2)
            GWP_coeffs.append(coeff)
        GWP_coeffs = np.array(GWP_coeffs)
        GWP_coeffs /= np.linalg.norm(GWP_coeffs)

        betas = [-np.angle(coeff) for coeff in GWP_coeffs]
        p = np.diag(np.exp(1j * np.array(betas)))

        GWP_coeffs = p @ GWP_coeffs
        thetas = []
        for i in range(N_s - 1):
            j = N_s - 1 - i
            theta = np.arctan(-np.abs(GWP_coeffs[j]) / np.abs(GWP_coeffs[j-1]))
            thetas.append(theta)
            GWP_coeffs = Giv_Mat(N_s, theta, j) @ GWP_coeffs
        print(np.round(GWP_coeffs, 3))
        return betas, thetas
    elif N_s > n_s:
        if r == None:
            return("Please provide r")
        else:
            GWP_coeffs = []
            for i in range(n_s):
                coeff = np.exp(-1j * k * (x + i)) * np.exp(-r[i]**2 / sigma**2)
                GWP_coeffs.append(coeff)
            GWP_coeffs = np.array(GWP_coeffs)
            GWP_coeffs /= np.linalg.norm(GWP_coeffs)

            betas = [-np.angle(coeff) for coeff in GWP_coeffs]
            p = np.diag(np.exp(1j * np.array(betas)))

            GWP_coeffs = p @ GWP_coeffs
            thetas = []
            for i in range(n_s - 1):
                j = n_s - 1 - i
                theta = np.arctan(-np.abs(GWP_coeffs[j]) / np.abs(GWP_coeffs[j-1]))
                thetas.append(theta)
                GWP_coeffs = Giv_Mat(n_s, theta, j) @ GWP_coeffs
            return betas, thetas
    else:
        return print("Incorrect: N_s must be greater than n_s. Try again!")


