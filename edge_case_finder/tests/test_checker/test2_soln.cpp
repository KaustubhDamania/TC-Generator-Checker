#include <bits/stdc++.h>
#define li long int
#define ll long long
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define srt(arr) sort(arr.begin(),arr.end())
#define srtr(arr) sort(arr.rbegin(),arr.rend())
#define fori(i,a,b) for(ll i=a; i<b; i++)
#define ford(i,a,b) for(ll i=a; i>b; i--)
#define FAST_IO ios::sync_with_stdio(false); cin.tie(NULL);
using namespace std;

ll mul(ll x, ll y, ll z)
{
    ll res = 1;
    x = x%z;
    while(y>0){
        if(y&1)
            res = ((res%z)+(x%z))%z;
        x = (x<<1)%z;
        y >>= 1;
    }
    return res%z;
}

ll fast_expo(ll x, ll y, ll z){
    ll res = 1;
    while(y>0){
        if(y & 1){
            res = ((res%z)*(x%z))%z;
        }
        y >>= 1;
        x = ((x%z)*(x%z))%z;
    }
    return res;
}

void printVec(vector<ll>res){
    for(auto itr : res){
        cout<<(itr)<<" ";
    }
    cout<<"\n";
}

unordered_map<ll, vector<ll>> constructTree(pair<ll,ll> edges[], ll n){
    unordered_map<ll, vector<ll>> res;
    fori(i,0,n){
        auto pairs = edges[i];
        res[pairs.f].pb(pairs.s);
        res[pairs.s].pb(pairs.f);
    }
    return res;
}

void dfs(unordered_map<ll, vector<ll>> &tree, bool visited[], int start){
    visited[start]=true;
    for(auto itr : tree[start]){
        if (!visited[itr]){
            dfs(tree,visited,itr);
        }
    }
}

ll gcdExtended(ll a, ll b, ll *x, ll *y) {
    if (a == 0) {
        *x = 0, *y = 1;
        return b;
    }

    ll x1, y1;
    ll gcd = gcdExtended(b%a, a, &x1, &y1);

    *x = y1 - (b/a) * x1;
    *y = x1;
    return gcd;
}

// Function to find modulo inverse of a
ll modInverse(ll a, ll m) {
    ll x, y;
    ll g = gcdExtended(a, m, &x, &y);
    if (g != 1)
        return -1;
    else
    {
        ll res = (x%m + m) % m;
        return res;
    }
}

const ll SZ = 5*(1e5) + 1;

ll fac[SZ];
ll twoPower[SZ];

ll ncr(ll n, ll r, ll p = MOD) {
    // Base case
    if(r > n)   return 0;
    if(r == 1)  return n;
    if (r == 0 || r == n) return 1;
    return (fac[n] * modInverse(fac[r], p) % p * modInverse(fac[n - r], p) % p) % p;
}

void solve(){
    ll n;
    cin>>n;
    ll arr[n];
    ll res = 0;
    for(ll i=0; i<n; i++){
       cin>>arr[i];
       res += max(arr[i], 0LL);
    }
    cout<<res<<"\n";
    ll mini = *min_element(arr, arr+n), maxi = *max_element(arr, arr+n);
    if(maxi <= 0 || mini > 0){ // no +ve or all +ve
        cout<<"0\n";
        return;
    }
    set<ll>swaps;
    ll i=0, j=n-1;
    while(arr[j] < 0)   j--;
    while(arr[i] > 0)   i++;
    while(i < j){
        // cout<<i<<" "<<j<<"\n";
        if(arr[i] >= 0)  i++;
        else swaps.insert(i++);
        if(arr[j] > 0)  swaps.insert(j--);
        else j--;
    }
    cout<<swaps.size()<<" ";
    for(ll idx : swaps) cout<<idx+1<<" ";
    cout<<"\n";
}

int main(){
    FAST_IO
    ll t;
    cin>>t;
    while(t--){
        solve();
    }
}
