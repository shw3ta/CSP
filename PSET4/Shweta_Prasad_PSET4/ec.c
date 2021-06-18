#include<stdlib.h>
#include<gmp.h>
#include<stdio.h>
#include<math.h>

// globals 
int P, A, B;

//struct to handle points of the form (x, y)
typedef struct Point
{
	int x;
	int y;

}point;

//reads into passed variable locations
void read_params(int* p, int* a, int* b){

	FILE *ptr;

	ptr = fopen("params.txt", "r");

	if (ptr == NULL){
		printf("Entered file does not exist.\n");

		//exit program
		exit(1);
	}

	int ret;
	ret = fscanf(ptr, "%d", p);
	ret = fscanf(ptr, "%d", a);
	ret = fscanf(ptr, "%d", b);
	
}


void ec_point_read(point *p){

	printf("\nEnter an EC point below in this format : \"x y\" (without the \"\")\n");
	scanf("%d %d", &p->x, &p->y); //DONT CHANGE THISSS

}


void ec_point_write(point p){
  
  //printf("\nThe point is:\n");
  printf("%d %d\n", p.x, p.y);

}

// Extended Euclidean Algorithm
int ex_gcd(int a, int b, int* x, int* y)
{
    // Base Case
    if (a == 0)
    {
        *x = 0, *y = 1;
        return b;
    }
 
    int x1, y1; // To store results of recursive call
    int gcd = ex_gcd(b % a, a, &x1, &y1);
 
    // Update x and y using results of recursive
    // call
    *x = y1 - (b / a) * x1;
    *y = x1;
 
    return gcd;

}

// Function to find modulo inverse of a
int mod_inverse(int a, int m)
{
    int x, y;
    int g = ex_gcd(a, m, &x, &y);
    if (g != 1){
        printf("Inverse doesn't exist for the denominator of lambda during calculation. The entered point cannot be doubled.\n");
        exit(1);
    }

    else
    {
        // m is added to handle negative x
        int res = (x % m + m) % m;
        return res;

    }
}

point add(point p1, point p2){
	printf("\nADDING ");

	int lambda, denom_inv;
	point res;

	//at least one of the points is the point at infinity
	if ((p1.x == -1 && p1.y == -1) || (p2.x == -1 && p2.y == -1)){
		
		//handle the case when both are at infinty
		if (p1.x == p2.x && p2.x == p1.y && p1.y == p2.y){
			res.x = -1;
			res.y = -1;
		}

		//if p1 is the point at infinity, then res = p2 + inf = p2
		else if (p1.x == -1 && p2.x == -1){
			res.x = p2.x;
			res.y = p2.y;
		}

		//if p2 is the point at infinity, then res = p1 + inf = p1
		else{
			res.x = p1.x;
			res.y = p1.y;
		}


	}

	// when the x coordinates of the 2 points are the same
	else if (p1.x == p2.x){

		printf("POINTS %d, %d and %d, %d WITH THE SAME X COORD", p1.x, p1.y, p2.x, p2.y);

		if (p1.y == p2.y){

			printf(" AND Y COORD: POINT DOUBLING\n");
			// the point is being doubled

			denom_inv = mod_inverse((2 * p1.y), P);
			lambda = (((3 * p1.x * p1.x  +  A) % P) * denom_inv) % P;

			res.x = (lambda * lambda  -  2 * p1.x) % P;
			res.y = (lambda * (p1.x - res.x) - p1.y) % P;
		}

		else{
			printf(" BUT DIFF Y COORDS\n");
			// return inf (-1 -1)
			res.x = -1;
			res.y = -1;
		}
	}

	else{
		// finally, two points that aren't too edgy
		printf("2 DIFF POINTS\n");

		denom_inv = mod_inverse((p1.y - p2.y), P);
		lambda = (((p1.x - p2.x) % P) * denom_inv) % P;

		res.x = (lambda * lambda  -  2 * p1.x) % P;
		res.y = (lambda * (p1.x - res.x) - p1.y) % P;
	}


	return res;

}


point negate(point p){

	printf("\nNEGATING %d, %d\n", p.x, p.y);
	// if P = x, y then -P = x, -y
	point p_neg;
	p_neg.x = p.x;
	p_neg.y = -p.y;
	
	return p_neg;

}

point subtract(point p1, point p2){

	printf("\nSUBTRACTING %d, %d  from %d, %d. \n", p2.x, p2.y, p1.x, p1.y);

	point res;

	p2 = negate(p2);
	//ec_point_write(p2);
	res = add(p1, p2);

	return res;

}

point multiply(point p, int k){	

	// similar to square and multiply,
	// DOUBLE AND ADD
	point res, temp;

	temp.x = p.x;
	temp.y = p.y;

	res.x = -1;
	res.y = -1;

	while (k > 0){
		if (k&1 == 1){
			//add
			res = add(res, p);
		}

		//double
		temp = add(temp, temp);
		k = k/2;
	}

	return res;


}

int main(){

	//need to check for valid pointssssssss

	point p;
	point p_added, p_negated, p_subtracted;
	
	//4-4 (a)
	read_params(&P, &A, &B);

	printf("\nThe parameters read are: \n\n");	
	printf("p : %d\n",P);
	printf("a : %d\n",A);
	printf("b : %d\n",B);

	//4-4 (b)
	ec_point_read(&p);
	
	//4-4 (c)
	ec_point_write(p);

	//4-4 (d)
	point p2;
	p2.x = 9;
	p2.y = 0;


	p_added = add(p, p2);
	ec_point_write(p_added);
	//printf("p_add[0] %d  p_add[1] %d\n",&p_added[0], &p_added[1] );

	//4-4 (e)
	p_negated = negate(p);
	ec_point_write(p_negated);

	//4-4 (f)
	p_subtracted = subtract(p, p2);
	ec_point_write(p_subtracted);

}