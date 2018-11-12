#include<bits/stdc++.h>

using namespace std;

int Population_size = 100;
const string GENES = "01";

int get_random(int start, int end){
	return (start + (rand())%(end-start+1));
}

char mutate_gene(){
	return GENES[get_random(0,GENES.size()-1)];
}

int create_gene(){
	return (get_random(-100,100));
	/*string gene = "";
	for(int i = 0 ; i < GOAL.size() ; i++)
		gene += mutate_gene(); 
	return gene;*/
}

class Human{
	public:
		bool flag;
		int v; 
		string chromosome; 
		int fitness; 
		Human(int x); 
		Human mate(Human parent2); 
		int get_fitness(); 
}; 
  
string get_binary(int v){
    string binary = "";
    int mask = 1;
    for(int i = 0; i < 40; i++)
    {
        if((mask&v) >= 1)
            binary = "1"+binary;
        else
            binary = "0"+binary;
        mask<<=1;
    }
    return binary;
}

Human::Human(int v){//string chromosome) 
	if (v>=0)
		flag = true;
	else 
		flag = false;
	this->v = v;
    this->chromosome = get_binary(abs(v));//chromosome; 
    fitness = get_fitness();  
}; 

int f1(int x){
	return x*x;
}

int f2(int x){
	return (x-2)*(x-2);
}

int Human::get_fitness(){ 
    int fitness = 0;
    fitness = f1(v) + f2(v); 
    /*for(int i = 0 ; i < GOAL.size() ; i++)
        if(chromosome[i] != GOAL[i]) 
            fitness++; */
    return fitness;     
};

int toint(string s , bool flag){
	int num = 0;
	for(int i = 0 ; i < 40 ; i++){
		if (s[40-i-1] == '1')
			num += pow(2,i);
	}
	if (!flag)
		num = num * -1;
	return num;
}

Human Human::mate(Human par2){ 
    string c_chromosome = ""; 
    for(int i = 0 ; i < 40 ; i++){ 
        float p = get_random(0, 100)/100; 
        if(p < 0.47) 
            c_chromosome += chromosome[i];
        else if(p < 0.94) 
            c_chromosome += par2.chromosome[i]; 
        else
            c_chromosome += mutate_gene(); 
    }
    if(get_random(0,1))
	    return Human(toint(c_chromosome,flag)); 
	else
		return Human(toint(c_chromosome,par2.flag));
}; 

bool operator<(const Human &first, const Human &second){ 
    return first.fitness < second.fitness; 
} 

int main(){
	//cout << toint("0000000101",true) << endl;
	srand((unsigned)(time(0)));
	bool done = false;
	int generation = 0;
	vector<Human> population;
	for(int i = 0 ; i < Population_size ; i++){
		int gene = create_gene();
		population.push_back(Human(gene));
		//cout << gene << " " << population[i].chromosome << endl;
	}
	//return 0;
	while (!done){
		if (generation == 1000)
			break;
		sort(population.begin(),population.end());
		if(population[0].fitness <= 0){
			done = true;
			break;
		}		
		vector<Human> new_gen;
		int s = (1*Population_size)/10; 
        for(int i = 0 ; i < s ; i++) 
            new_gen.push_back(population[i]); 
        
        s = (9*Population_size)/10; 
        for(int i = 0 ; i < s ; i++){ 
            int len = population.size(); 
            int r = get_random(0, 50); 
            Human parent1 = population[r]; 
            r = get_random(0, 50); 
            Human parent2 = population[r]; 
            Human offspring = parent1.mate(parent2); 
            new_gen.push_back(offspring);  
        } 
		population = new_gen; 
        cout<< "Generation: " << generation << "\t"; 
        cout<< "String: "<< population[0].chromosome <<"\t"; 
        cout<< "Fitness: "<< population[0].fitness << "\n"; 
  
        generation++; 
     } 
    cout<< "Generation: " << generation << "\t"; 
    cout<< "String: "<< population[0].chromosome <<"\t"; 
    cout<< "Fitness: "<< population[0].fitness << "\n"; 
	return 0;
}
