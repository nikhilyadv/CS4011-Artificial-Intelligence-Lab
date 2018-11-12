#include<bits/stdc++.h>

using namespace std;

int Population_size = 200;
const string GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
const string GOAL = "Nikhil loves genetic algorithm";
//const string START = "xxxxxx xxxx xxxxxxx xxxxxxxxx"

int get_random(int start, int end){
	return (start + (rand())%(end-start+1));
}

char mutate_gene(){
	return GENES[get_random(0,GENES.size()-1)];
}

string create_gene(){
	string gene = "";
	for(int i = 0 ; i < GOAL.size() ; i++)
		gene += mutate_gene(); 
	return gene;
}

class Human{
	public: 
		string chromosome; 
		int fitness; 
		Human(string chromosome); 
		Human mate(Human parent2); 
		int get_fitness(); 
}; 
  
Human::Human(string chromosome) 
{ 
    this->chromosome = chromosome; 
    fitness = get_fitness();  
}; 

int Human::get_fitness(){ 
    int fitness = 0; 
    for(int i = 0 ; i < GOAL.size() ; i++)
        if(chromosome[i] != GOAL[i]) 
            fitness++; 
    return fitness;     
};

Human Human::mate(Human par2){ 
    string c_chromosome = ""; 
    for(int i = 0 ; i < chromosome.size() ; i++){ 
        float p = get_random(0, 100)/100; 
        if(p < 0.47) 
            c_chromosome += chromosome[i];
        else if(p < 0.94) 
            c_chromosome += par2.chromosome[i]; 
        else
            c_chromosome += mutate_gene(); 
    } 
    return Human(c_chromosome); 
}; 

bool operator<(const Human &first, const Human &second){ 
    return first.fitness < second.fitness; 
} 

int main(){
	srand((unsigned)(time(0)));
	bool done = false;
	int generation = 0;
	vector<Human> population;
	for(int i = 0 ; i < Population_size ; i++){
		string gene = create_gene();
		population.push_back(Human(gene));
	}
	while (!done){
		sort(population.begin(),population.end());
		if(population[0].fitness <= 0){
			done = true;
			break;
		}		
		vector<Human> new_gen;
		int s = (30*Population_size)/100; 
        for(int i = 0 ; i < s ; i++) 
            new_gen.push_back(population[i]); 
        
        s = (70*Population_size)/100; 
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
