#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)
class Box{
    public:
    int l,b,h;
    
    int getLength(){return l;}
    int getBreadth(){return b;}
    int getHeight(){return h;}
    unsigned long long CalculateVolume(){
        unsigned long long V=(unsigned long long)l*b*h;
        return V;}
    Box(){
        l=0;b=0;h=0;
    }
    Box(int length,int breadth,int height){
        l=length;b=breadth;h=height;
    }
    Box(const Box& B){
        l=B.l;b=B.b;h=B.h;
    }
    
    bool operator<(Box& B){
        if(l<B.l)return 1;
        else if(b<B.b)return 1;
        else if(h<B.h)return 1;
        else
        return 0;
    }
    friend ostream& operator<<(ostream& out,Box& B);
};
ostream& operator<<(ostream& out,Box& B){
        return out<<B.l<<" "<<B.b<<" "<<B.h;
    }

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}