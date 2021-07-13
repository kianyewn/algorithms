##
def dna(seq):
    # DP to keep track of the number of possible base pairs from the sub-interval from i to j
    # The reason why we used the outer loop as the distance from i to j is so that we can use dynamic programming
    # Consider the following solution:
    # Note that to satisfy the condition of no sharp turn, we want to have that (i -j < -4) thus <==> (i < j - 4)
    # for i in range(len(seq)):
    # for j in range(len(seq)):
    # compute OPT(I,J) = MAX(
    #           OPT(I,J-1), ## this is one of the base case when the jth base is is not involved in a pair
    #           OPT(I, T-1) + 1 + OPT (T+1, J-1) ) ## this is the base case when the jth base is involved in a pair, and it pairs with a base represented by index t,
    #                                              ##  and this t ranges from (i <= t < j - 4). Notice the equality sign from i and t, which is to show that
    #                                              ## base j can pair up with bases up to i, i.e the entire subinterval.
    # Okay, so now we have established the formulation above, why does the above solution not work?
    # When we calculate OPT(I,J), OPT(I, J-1) must be calculated already. This is true because we are doing a bottom down approach
    # We also need OPT(I, T-1) to be calculated, and this is also true because we know that t < j, so T-1 must be calculated
    # However, the issue comes with OPT(T+1, J-1). Since i <= t, i < t + 1, and therefore we do not have access to OPT(T+1, any J)
    # For more information, watch minute 32:05 of https://www.youtube.com/watch?v=h60raqnvm0s
    # This is the reason why although the above representation of the problem looks okay, it is not possible to be used.
    #
    # Thus, to ensure that we are using a bottom down approach, and that we have access to the information OPT(T+1, J-1), we want to
    # make it such that we can calculate the all the iths in advance for OPT(I's, J's).
    # To do this, we look at the distance between i and j.
    # so now all of our values of i (example T-1, T, T+1, T+2) will be calculated for a smaller value of j(example J-1, J, J+1),
    # which means that at i = I and j = J, we can access our OPT(T+1, J-1), since it has already been calculated beforehand!

    ##
    M = [[0] * len(seq) for _ in range(len(seq))]
    for distance in range(len(seq)):
        # it is possible for the distance to be 0, so in this case, we do not pair bases i and bases j
        for i in range(len(seq)):
            j = i + distance
            if distance <= 4:
                # this handles the no turn condition
                M[i][j] = 0
            else:
                # if base j is not involved in the pair
                M[i][j] = M[i][j - 1]
                # if base j is involved in the pair
                # for t in range(i, j - 4):
                for t in range(i, j - 4):
                    # for every possible base from index i to j - 4. (remember that i <= t < j -4), so we want our j to end at (j - 5)
                    M[i][j] = max(M[i][j - 1], 1 + M[i][t-1] + M[t+1][j-1])

    # when we find the solution, we want from the start of the seq to the end of the sequence, thus index 0 as the row index and len(seq)-1 as the col index
    return M[0][len(seq)-1]
