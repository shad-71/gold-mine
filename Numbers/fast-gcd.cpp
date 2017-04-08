#include <iostream>
#include <vector>
#include <list>
using namespace std;

class Graph
{
	int V;
	int count=0;
	list<int> *adj;
		public :
	Graph(int v)
	{
		V=v;
		adj = new list<int>[V];
	};
	void dfs(int s,bool visited[])
	{
			//cout<<s<<" ";
			visited[s]=true;
			count++;
				for(list<int>::iterator it=adj[s].begin();it!=adj[s].end();++it)
					{
						if(!visited[*it])
							dfs(*it,visited);
					}
 
	};
 
	int check(int s)
	{
			bool visited[V];
		for(int i=0;i<V;i++)
			visited[i]=false;
		dfs(s, visited);
		return count;
		
	};
	
	void edge(int u,int v)
	{
		adj[u].push_back(v);
	};
	
	bool edgecheck(int u , int v)
	{	
			for(list<int>::iterator it=adj[v].begin();it!=adj[v].end();++it)
					{
						if(*it == u)
						return true;
					}
		return false;
	}

};

int main() {
	// your code goes 
	long T,N,M,u,v;
	bool loop = false;
	cin>>T;
	vector<pair<int,int>> prereq;
	while(T--)
	{
		loop = false;
		cin>>N>>M;
		Graph g(N+1);
		for(int i = 0;i<M;i++)
			{
				cin>>u>>v;
				g.edge(u,v);
				if (g.edgecheck(u,v))
				{
					cout<<"0\n";
					loop = true;
					break;
				}
				
				//prereq.push_back(make_pair(u,v));
			//	check(N,prereq);
			}
		if(g.check(1)==N  )
		{
			if(!loop)
			cout<<"1\n";
		}
		else
			cout<<"0\n";
	}
	return 0;
}