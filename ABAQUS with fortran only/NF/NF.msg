1

   Abaqus 6.13-1                                  Date 09-Feb-2016   Time 17:59:06
   For use by  under license from Dassault Systemes or its subsidiary.

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     C A L C U L A T I O N   O F   E I G E N V A L U E S

                                            F O R   N A T U R A L   F R E Q U E N C I E S



                                                                                          

     THE LANCZOS EIGENSOLVER IS USED FOR THIS ANALYSIS
     Abaqus WILL COMPUTE UNCOUPLED
      STRUCTURAL AND ACOUSTIC MODES
     NUMBER OF EIGENVALUES                     20
     HIGHEST FREQUENCY OF INTEREST                  1.00000E+18
     MAXIMUM NUMBER OF STEPS WITHIN RUN               35
     BLOCK SIZE FOR LANCZOS PROCEDURE                  7
     THE EIGENVECTORS ARE SCALED SO THAT 
      THE LARGEST DISPLACEMENT ENTRY IN EACH VECTOR
      IS UNITY

     THIS IS A LINEAR PERTURBATION STEP.
     ALL LOADS ARE DEFINED AS CHANGE IN LOAD TO THE REFERENCE STATE

     EXTRAPOLATION WILL NOT BE USED

     CHARACTERISTIC ELEMENT LENGTH     2.528E-02

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     EQUATIONS ARE BEING REORDERED TO MINIMIZE WAVEFRONT

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     CHECK POINT   START OF SOLVER    
  
 COMPUTER PRECISION USED BY ABAQUS      2.22045e-016
 CONVERGENCE CRITERION FOR LANCZOS RUN  1.81899e-012
  
 NUMBER OF EQUATIONS                                                           13645
 NUMBER OF UNRESTRAINED DEGREES OF FREEDOM                                     10440
 HEURISTIC SCALE FOR THE FIRST NONZERO EIGENVALUES (PROBLEM SCALE)  2.14407e+003
 INITIAL SHIFT VALUE                                                0.00000e+000
  
 NUMBER OF CPUS USED BY DIRECT SOLVER     1
  
 NUMBER OF NEGATIVE EIGENVALUES  1611
 NUMBER OF POSITIVE EIGENVALUES     12034
 NUMBER OF NEGATIVE EIGENVALUES NOT ASSOCIATED WITH LAGRANGE MULTIPLIERS     0
 NUMBER OF NEGATIVE EIGENVALUES ASSOCIATED WITH LAGRANGE MULTIPLIERS      1611
  
 COMPUTATIONAL INTERVAL FOR THE INITIAL LANCZOS RUN
 
 EIGENVALUES NEEDED TO THE RIGHT OF SHIFT VALUE   20
 EIGENVALUES NEEDED TO THE LEFT OF SHIFT VALUE     0
 RIGHT BOUNDARY OF THE COMPUTATIONAL INTERVAL  3.95574e+037
 LEFT BOUNDARY OF THE COMPUTATIONAL INTERVAL  -3.95574e+037
  
 LANCZOS RUN TERMINATED. NUMBER OF STEPS:   19
 ALL THE EIGENVALUES REQUESTED ON THIS LANCZOS RUN ARE FOUND
  
 NUMBER OF ACCEPTED EIGENVALUES   24
  
 ACCEPTED EIGENVALUES
  8.47770e+007 9.37571e+007 1.00071e+008 1.32581e+008 1.34831e+008 1.93600e+008
  1.99463e+008 3.00204e+008 3.03561e+008 3.26902e+008 3.66554e+008 3.87675e+008
  3.91678e+008 3.92999e+008 4.42507e+008 4.72671e+008 4.79616e+008 5.17136e+008
  5.48493e+008 5.51764e+008 5.87989e+008 5.93970e+008 6.04125e+008 6.43761e+008
  
 FACTORIZATION WITH NEW SHIFT VALUE IS REQUIRED
  
 TRUST INTERVALS AFTER LANCZOS RUN AND COMPRESSION
  
 NUMBER OF TRUST INTERVALS    1
  
 -------------------------------------------------------------------------------------
 | KEY | INSIDE |      INERTIAS     |  SENTINELS  |   OUTSIDE   |  NEED TO FIND      |
 |      ENDS OF INTERVAL     |     ENDS OF SENTINEL      |   COMPUTATIONAL INTERVAL  |
 -------------------------------------------------------------------------------------
 |  +  |      0 |     1611     1611 |     0     0 |     0     0 |      0    20       |
 |-3.95574e+037 0.00000e+000 |-3.95574e+037 0.00000e+000 |-3.95574e+037 3.95574e+037 |
 -------------------------------------------------------------------------------------
  
 DATA FOR CHOOSING SHIFT
  
 NUMBER OF EIGENVALUES NEEDED IN THE PRIMARY TRUST INTERVAL   20
  
 NUMBER OF MODES FORMING SENTINEL TO THE RIGHT   21
 SHIFT RIGHT        5.69877e+008
  
 NUMBER OF MODES FORMING SENTINEL TO THE LEFT     0
 SHIFT LEFT         0.00000e+000
  
 SHIFTING TO THE RIGHT DIRECTION
 NEW SHIFT          5.69877e+008
  
 NUMBER OF NEGATIVE EIGENVALUES  1631
 NUMBER OF POSITIVE EIGENVALUES     12014
 NUMBER OF NEGATIVE EIGENVALUES NOT ASSOCIATED WITH LAGRANGE MULTIPLIERS    20
 NUMBER OF NEGATIVE EIGENVALUES ASSOCIATED WITH LAGRANGE MULTIPLIERS      1611
  
 THE REQUIRED NUMBER OF EIGENVALUES IS FOUND
  
 FINAL TRUST INTERVAL
  
 -------------------------------------------------------------------------------------
 | KEY | INSIDE |      INERTIAS     |  SENTINELS  |   OUTSIDE   |  NEED TO FIND      |
 |      ENDS OF INTERVAL     |     ENDS OF SENTINEL      |   COMPUTATIONAL INTERVAL  |
 -------------------------------------------------------------------------------------
 |  +  |     20 |     1611     1631 |     0     0 |     0     0 |      0     0       |
 |-3.95574e+037 5.69877e+008 |-3.95574e+037 5.69877e+008 |-3.95574e+037 5.69877e+008 |
 -------------------------------------------------------------------------------------
  
 FIRST EIGENVALUE REQUESTED BY THE USER     1
  
 EIGENVALUES REQUESTED BY THE USER
  8.47770e+007 9.37571e+007 1.00071e+008 1.32581e+008 1.34831e+008 1.93600e+008
  1.99463e+008 3.00204e+008 3.03561e+008 3.26902e+008 3.66554e+008 3.87675e+008
  3.91678e+008 3.92999e+008 4.42507e+008 4.72671e+008 4.79616e+008 5.17136e+008
  5.48493e+008 5.51764e+008
  
 EIGENVALUE EXTRACTION USING THE LANCZOS EIGENSOLVER IS COMPLETE
 NUMBER OF LANCZOS RUNS       :   1
 NUMBER OF LANCZOS STEPS      :  19
 NUMBER OF FACTORIZATIONS     :   2
 NUMBER OF BACK SUBSTITUTIONS :  20

     CHECK POINT  END OF SOLVER       

       ELAPSED USER TIME (SEC)      =   2.1000    
       ELAPSED SYSTEM TIME (SEC)    =  0.20000    
       ELAPSED TOTAL CPU TIME (SEC) =   2.3000    
       ELAPSED WALLCLOCK TIME (SEC) =          2


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF          1  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                       0  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      22  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                       2  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       6  WARNING MESSAGES DURING USER INPUT PROCESSING
                       0  WARNING MESSAGES DURING ANALYSIS
                       0  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =   2.6000    
       SYSTEM TIME (SEC)    =  0.20000    
       TOTAL CPU TIME (SEC) =   2.8000    
       WALLCLOCK TIME (SEC) =          3
