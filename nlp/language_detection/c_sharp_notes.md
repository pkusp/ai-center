
---
`@auther: pkusp@outlook.com`  
`@date: 2018.12.18`  
`@location: Microsoft Asia`  
<!--[[check the reference for more information]](http://www.runoob.com/csharp/csharp-string.html)-->  

---
目录|
---|
[toc]|

[reference](http://www.runoob.com/csharp/csharp-data-types.html)
# C#基础 
## 一些关键字
- get & set  
[[ref]](https://www.cnblogs.com/lixiaolu/p/8214037.html)
    - 在面向对象编程（OOP）中，是不允许外界直接对类的成员变量直接访问的，既然不能访问，那定义这些成员变量还有什么意义呢？所以C#中就要用`set`和`get`方法来访问私有成员变量，它们相当于外界访问对象的一个通道，一个“接口”。

- var  
[ref](https://www.cnblogs.com/ggll611928/p/5991401.html)
    - var 是3.5新出的一个定义变量的类型 其实也就是弱化类型的定义 VAR可代替任何类型 编译器会根据上下文来判断你到底是想用什么类型的 至于什么情况下用到VAR 我想就是你无法确定自己将用的是什么类型 就可以使用VAR 类似 OBJECT 但是效率比OBJECT高点。

    - var可以理解为匿名类型，我们可以认为它是一个声明变量的占位符。它主要用于在声明变量时，无法确定数据类型时使用。
    
    - 必须在定义时初始化。也就是必须是var s = “abcd”形式，而不能是如下形式: var s; s = “abcd”;

    - 一但初始化完成，就不能再给变量赋与初始化值类型不同的值了。

    - var要求是局部变量。

    - 使用var定义变量和object不同，它在效率上和使用强类型方式定义变量完全一样。
  
  
## List
[ref](https://www.cnblogs.com/dyhao/p/9501479.html)
- 创建泛型
    ```cs
    using System.Collections.Generic
    
    List<T> ListOfT = new List<T>();
    ```
    
- List方法和属性
```cs
    Capacity( ) //用于获取或设置List可容纳元素的数量。当数量超过容量时，这个值会自动增长。您可以设置这个值以减少容量，也可以调用trin()方法来减少容量以适合实际的元素数目。
　　Count( ) //用于获取数组中当前元素数量
　　Item( ) //通过指定索引获取或设置元素。对于List类来说，它是一个索引器。
　　Add( ) //在List中添加一个对象的公有方法
　　AddRange( ) //公有方法，在List尾部添加实现了ICollection接口的多个元素
　　BinarySearch( ) //重载的公有方法，用于在排序的List内使用二分查找来定位指定元素.
　　Clear( ) //在List内移除所有元素
　　Contains( ) //测试一个元素是否在List内
　　CopyTo( ) //重载的公有方法，把一个List拷贝到一维数组内
　　Exists( ) //测试一个元素是否在List内
　　Find( ) //查找并返回List内的出现的第一个匹配元素
　　FindAll( ) //查找并返回List内的所有匹配元素
　　GetEnumerator( ) //重载的公有方法，返回一个用于迭代List的枚举器
　　Getrange( ) //拷贝指定范围的元素到新的List内
　　IndexOf( ) //重载的公有方法，查找并返回每一个匹配元素的索引
　　Insert( ) //在List内插入一个元素
　　InsertRange( ) //在List内插入一组元素
　　LastIndexOf( ) //重载的公有方法，，查找并返回最后一个匹配元素的索引
　　Remove( ) //移除与指定元素匹配的第一个元素
　　RemoveAt( ) //移除指定索引的元素
　　RemoveRange( ) //移除指定范围的元素
　　Reverse( ) //反转List内元素的顺序
　　Sort( ) //对List内的元素进行排序
　　ToArray( ) //把List内的元素拷贝到一个新的数组内
　　trimToSize( ) //将容量设置为List中元素的实际数目
```
- List常用方法 [[进阶方法 click here]](https://www.cnblogs.com/dyhao/p/9501479.html)
```cs
List<string> mList = new List<string>();

//以一个集合作为参数创建List：
string[] temArr = { "Ha", "Hunter", "Tom", "Lily", "Jay", "Jim", "Kuku", "Locu" };
List<string> testList = new List<string>(temArr);

//添加一个元素
List<string> mList = new List<string>();
mList.Add("John");

// 添加一组元素
List<string> mList = new List<string>();
string[] temArr = { "Ha","Hunter", "Tom", "Lily", "Jay", "Jim", "Kuku",  "Locu" };
mList.AddRange(temArr);

//遍历List中元素
List<string> mList = new List<string>();
...//省略部分代码
foreach (string s in mList)
{
    Console.WriteLine(s);
}

//删除一个值
mList.Remove("Hunter");

//删除下标为index的元素
mList.RemoveAt(0);

//从下标index开始，删除count个元素
mList.RemoveRange(3, 2);//index = 3, count = 2

//判断某个元素是否在该List中
if (mList.Contains("Hunter"))
{
    Console.WriteLine("There is Hunter in the list");
}
else
{
    mList.Add("Hunter");
    Console.WriteLine("Add Hunter successfully.");
}

//给List里面元素排序： 默认是元素第一个字母按升序
mList.Sort();

//给List里面元素顺序反转
mList. Reverse();

//List清空
mList.Clear();

//获得List中元素数目
int count = mList.Count();
Console.WriteLine("The num of elements in the list: " +count);
```


- 例子 -> [click](https://www.cnblogs.com/dyhao/p/9501479.html)
    ```cs
    class Person
    {
        private string _name; //姓名
        private int _age; //年龄
        //创建Person对象
        public Person(string Name, int Age)
        {
            this._name= Name;
            this._age = Age;
        }
        //姓名
        public string Name
        {
            get { return _name; }
        }
        //年龄
        public int Age
        {
            get { return _age; }
        }
    }
    
    //创建Person对象
    Person p1 = new Person("张三", 30);
    Person p2 = new Person("李四", 20);
    Person p3 = new Person("王五", 50);
    //创建类型为Person的对象集合
    List<Person> persons = new List<Person>();
    //将Person对象放入集合
    persons.Add(p1);
    persons.Add(p2);
    persons.Add(p3);
    //输出第2个人的姓名
    Console.Write(persons[1].Name);
    
    ```
- 泛型集合的排序&搜索
    - 一个对象可以有多个比较规则，但只能有一个默认规则，默认规则放在定义该对象的类中。默认比较规则在CompareTo方法中定义，该方法属于IComparable<T>泛型接口。
        ```cs
        class Person ：IComparable<Person>
        {
            //按年龄比较
            public int CompareTo(Person p)
            {
                return this.Age - p.Age;
            }
        }
        //　CompareTo方法的参数为要与之进行比较的另一个同类型对象，返回值为int类型，如果返回值大于0，表示第一个对象大于第二个对象，如果返回值小于0,表示第一个对象小于第二个对象，如果返回0,则两个对象相等。
        
        //按照默认规则对集合进行排序
        persons.Sort();
        //输出所有人姓名
        foreach (Person p in persons)
        {
            Console.WriteLine(p.Name); //输出次序为"李四"、"张三"、"王五"
        }
        
        ```
    - 搜索就是从集合中找出满足特定条件的项，可以定义多个搜索条件，并根据需要进行调用。
    ```cs
    pass
    ```



## Dictionary
[ref](https://www.cnblogs.com/jaejaking/p/5301288.html)
- namespace  
    要使用Dictionary集合，需要导入C#泛型命名空间
    ```cs
     System.Collections.Generic（程序集：mscorlib）
    ```
- 描述
    ```cs
    1、从一组键（Key）到一组值（Value）的映射，每一个添加项都是由一个值及其相关连的键组成
    
    2、任何键都必须是唯一的
    
    3、键不能为空引用null（VB中的Nothing），若值为引用类型，则可以为空值
    
    4、Key和Value可以是任何类型（string，int，custom class 等） 
    ```
- 常用方法及举例
    ```cs
      Comparer：//获取用于确定字典中的键是否相等的 IEqualityComparer。
      Count：//获取包含在 Dictionary中的键/值对的数目。
      Item：//获取或设置与指定的键相关联的值。
      Keys：//获取包含 Dictionary中的键的集合。
      Values：//获取包含 Dictionary中的值的集合。
      Add：//将指定的键和值添加到字典中。
      Clear：//从 Dictionary中移除所有的键和值。
      ContainsKey：//确定 Dictionary是否包含指定的键。
      ContainsValue：//确定 Dictionary是否包含特定值。             
      GetEnumerator：//返回循环访问 Dictionary的枚举数。
      GetType：//获取当前实例的 Type。 （从 Object 继承。）
      Remove： //从 Dictionary中移除所指定的键的值。
      ToString：//返回表示当前 Object的 String。 （从 Object 继承。）
      TryGetValue：//获取与指定的键相关联的值。
    
    //  1、创建及初始化
     Dictionary<int,string> myDictionary = newDictionary <int,string>();
    
    //  2、添加元素
    myDictionary.Add(1,"C#");
    myDictionary.Add(2,"C++");
    myDictionary.Add(3,"ASP.NET");
    myDictionary.Add(4,"MVC");
    
     // 3、通过Key查找元素
    if(myDictionary.ContainsKey(1))
    {
    Console.WriteLine("Key:{0},Value:{1}","1", myDictionary[1]);
     }
    
    //  4、通过KeyValuePair遍历元素
    foreach( KeyValuePair<int,string> kvp in myDictionary)
    {
    Console.WriteLine("Key = {0}, Value = {1}",kvp.Key, kvp.Value);
    }
    
    // 5、仅遍历键 Keys 属性
    Dictionary<int,string>.KeyCollection keyCol = myDictionary.Keys;
    foreach(int key inkeyCol)
    {
    Console.WriteLine("Key = {0}", key);
    }
    
    // 6、仅遍历值 Valus属性
    Dictionary<int,string>.ValueCollection valueCol = myDictionary.Values;
    foreach(string value in valueCol)
    {
    Console.WriteLine("Value = {0}", value);
    }
    
    // 7、通过Remove方法移除指定的键值
    myDictionary.Remove(1);
    if(myDictionary.ContainsKey(1))
    {
    　　Console.WriteLine("Key:{0},Value:{1}","1", myDictionary[1]);
    }
    else
    {
    Console.WriteLine("不存在 Key : 1"); 
     }
     
    ```

## HashSet
[ref](http://www.cnblogs.com/xiaopin/archive/2011/01/08/1930540.html)
- 定义  
.NET 3.5在System.Collections.Generic命名空间中包含一个新的集合类：HashSet<T>。这个集合类包含不重复项的无序列表。这种集合称为“集(set)”。集是一个保留字，所以该类有另一个名称HashSet<T>。这个名称很容易理解，因为这个集合基于散列值，插入元素的操作非常快，不需要像List<T>类那样重排集合。
- 方法
```cs
Add()　　　//如果某元素不在集合中，Add()方法就把该元素添加到集合中。在其返回值Boolean中，返回元素是否添加的信息
Clear()　　//方法Clear()删除集合中的所有元素
Remove()　// Remove()方法删除指定的元素
RemoveWhere()　　　//RemoveWhere()方法需要一个Predicate<T>委托作为参数。删除满足谓词条件的所有元素
CopyTo()     //CopyTo()把集合中的元素复制到一个数组中
ExceptWith()　　　//ExceptWith()方法把一个集合作为参数，从集中删除该集合中的所有元素
IntersectWith() 　//IntersectWith()修改了集，仅包含所传送的集合和集中都有的元素
UnionWith()   　　//UnionWith()方法把传送为参数的集合中的所有元素添加到集中

Contains()　//如果所传送的元素在集合中，方法Contains()就返回true
IsSubsetOf()  //如果参数传送的集合是集的一个子集，方法IsSubsetOf()就返回true
IsSupersetOf()　//如果参数传送的集合是集的一个超集，方法IsSupersetOf()就返回true
Overlaps()　　//如果参数传送的集合中至少有一个元素与集中的元素相同，Overlaps()就返回true
SetEquals()　　//如果参数传送的集合和集包含相同的元素，方法SetEquals()就返回true
```
- 例子
```cs
HashSet < string > companyTeams =new HashSet < string > (){ "Ferrari", "McLaren", "Toyota", "BMW","Renault", "Honda" };
HashSet < string > traditionalTeams =new HashSet < string > (){ "Ferrari", "McLaren" };
HashSet < string > privateTeams =new HashSet < string > (){ "Red Bull", "Toro Rosso", "Spyker","Super Aguri" };

if (privateTeams.Add("Williams"))
    Console.WriteLine("Williams added");
if (!companyTeams.Add("McLaren"))
    Console.WriteLine("McLaren was already in this set");
//Williams added
//McLaren was already in this set
```
- 特点  
[ref](http://www.cnblogs.com/refuge/p/9465466.html)
    - HashSet<T>类，主要被设计用来存储集合，做高性能集运算，例如两个集合求交集、并集、差集等。从名称可以看出，它是基于Hash的，可以简单理解为没有Value的Dictionary。
    - HashSet<T>中的值不能重复且没有顺序。
    - HashSet<T>的容量会按需自动添加。
    - HashSet<T>最大的优势是检索的性能，简单的说它的Contains方法的性能在大数据量时比List<T>好得多。在内部算法实现上，HashSet<T>的Contains方法复杂度是O(1)，List<T>的Contains方法复杂度是O(n)
    - 在3.5之前，想用哈希表来提高集合的查询效率，只有Hashtable和Dictionary两种选择，而这两种都是键-值方式的存储。但有些时候，我们只需要其中一个值，例如一个Email集合，如果用泛型哈希表来存储，往往要在Key和Value各保存一次，不可避免的要造成内存浪费。而HashSet只保存一个值，更加适合处理这种情况。
    - HashSet的Add方法返回bool值，在添加数据时，如果发现集合中已经存在，则忽略这次操作，并返回false值。而Hashtable和Dictionary碰到重复添加的情况会直接抛出错误。
    - HashSet和线性集合List更相似一些，但前者的查询效率有着极大的优势。
    - HashSet是Set集合，它只实现了ICollection接口，在单独元素访问上，有很大的限制：

    - 跟List相比，不能使用下标来访问元素，如：list[1] 。

    - 跟Dictionary相比，不能通过键值来访问元素，例如：dic[key]，因为HashSet每条数据只保存一项，并不采用Key-Value的方式，换句话说，HashSet中的Key就是Value，假如已经知道了Key，也没必要再查询去获取Value，需要做的只是检查值是否已存在。
    
## Tuple  
[ref](https://www.cnblogs.com/lavender000/p/6916157.html)  
C# 4.0引入的一个新特性，可以在..NET Framework 4.0或更高版本中使用。组元使用泛型来简化类的定义，多用于方法的返回值。在函数需要返回多个类型的时候，就不必使用out , ref等关键字了，直接定义一个Tuple类型，使用起来非常方便。
- 构造方法
    - 利用构造函数创建元组
    ```cs
    var testTuple6 = new Tuple<int, int, int, int, int, int>(1, 2, 3, 4, 5, 6);
    Console.WriteLine($"Item 1: {testTuple6.Item1}, Item 6: {testTuple6.Item6}");
    
    var testTuple10 = new Tuple<int, int, int, int, int, int, int, Tuple<int, int, int>>(1, 2, 3, 4, 5, 6, 7, new Tuple<int, int, int>(8, 9, 10));
    Console.WriteLine($"Item 1: {testTuple10.Item1}, Item 10: {testTuple10.Rest.Item3}");
    ```
    - 利用Tuple静态方法构建元组，最多支持八个元素
    ```cs
    var testTuple6 = Tuple.Create<int, int, int, int, int, int>(1, 2, 3, 4, 5, 6);
    Console.WriteLine($"Item 1: {testTuple6.Item1}, Item 6: {testTuple6.Item6}");
    
    var testTuple8 = Tuple.Create<int, int, int, int, int, int, int, int>(1, 2, 3, 4, 5, 6, 7, 8);
    Console.WriteLine($"Item 1: {testTuple8.Item1}, Item 8: {testTuple8.Rest.Item1}");
    //Note：这里构建出来的Tuple类型其实是Tuple<int, int, int, int, int, int, int, Tuple<int>>，因此testTuple8.Rest取到的数据类型是Tuple<int>，因此要想获取准确值需要取Item1属性。
    ```
- 例子
```cs
//如下创建一个元组表示一个学生的三个信息：名字、年龄和身高，而不用单独额外创建一个类。
var studentInfo = Tuple.Create<string, int, uint>("Bob", 28, 175);
Console.WriteLine($"Student Information: Name [{studentInfo.Item1}], Age [{studentInfo.Item2}], Height [{studentInfo.Item3}]");

//当一个函数需要返回多个值的时候，一般情况下可以使用out参数，这里可以用元组代替out实现返回多个值。
static Tuple<string, int, uint> GetStudentInfo(string name)
{
    return new Tuple<string, int, uint>("Bob", 28, 175);
}
static void RunTest()
{
    var studentInfo = GetStudentInfo("Bob");
    Console.WriteLine($"Student Information: Name [{studentInfo.Item1}], Age [{studentInfo.Item2}], Height [{studentInfo.Item3}]");
}

//当函数参数仅是一个Object类型时，可以使用元组实现传递多个参数值。
static void WriteStudentInfo(Object student)
{
    var studentInfo = student as Tuple<string, int, uint>;
    Console.WriteLine($"Student Information: Name [{studentInfo.Item1}], Age [{studentInfo.Item2}], Height [{studentInfo.Item3}]");
}
static void RunTest()
{
    var t = new System.Threading.Thread(new System.Threading.ParameterizedThreadStart(WriteStudentInfo));
    t.Start(new Tuple<string, int, uint>("Bob", 28, 175));
    while (t.IsAlive)
    {
        System.Threading.Thread.Sleep(50);
    }
}
```
- 缺点
    - 访问元素的时候只能通过ItemX去访问，使用前需要明确元素顺序，属性名字没有实际意义，不方便记忆；
    - 最多有八个元素，要想更多只能通过最后一个元素进行嵌套扩展；
    - Tuple是一个引用类型，不像其它的简单类型一样是值类型，它在堆上分配空间，在CPU密集操作时可能有太多的创建和分配工作。
- **ValueTuple**  
`ValueTuple`是C# 7.0的新特性之一，.Net Framework 4.7以上版本可用。值元组也是一种数据结构，用于表示特定数量和元素序列，但是是和元组类不一样的，主要区别如下：
    - 值元组是结构，是值类型，不是类，而元组（Tuple）是类，引用类型；
    - 值元组元素是可变的，不是只读的，也就是说可以改变值元组中的元素值；
    - 值元组的数据成员是字段不是属性。
    - ValueTuple支持函数返回值新语法”(,,)”，使代码更简单；
    - 能够给元素命名，方便使用和记忆，这里需要注意虽然命名了，但是实际上value tuple没有定义这样名字的属性或者字段，真正的名字仍然是ItemX，所有的元素名字都只是设计和编译时用的，不是运行时用的（因此注意对该类型的序列化和反序列化操作）；
    - 可以使用解构方法更方便地使用部分或全部元组的元素；
    - 值元组是值类型，使用起来比引用类型的元组效率高，并且值元组是有比较方法的，可以用于比较是否相等，详见：https://msdn.microsoft.com/en-us/library/system.valuetuple。
    ```cs
    //利用构造函数创建元组：
    var testTuple6 = new ValueTuple<int, int, int, int, int, int>(1, 2, 3, 4, 5, 6);
    Console.WriteLine($"Item 1: {testTuple6.Item1}, Item 6: {testTuple6.Item6}"); 
    
    var testTuple10 = new ValueTuple<int, int, int, int, int, int, int, ValueTuple<int, int, int>>(1, 2, 3, 4, 5, 6, 7, new ValueTuple <int, int, int>(8, 9, 10));
    Console.WriteLine($"Item 1: {testTuple10.Item1}, Item 10: {testTuple10.Rest.Item3}");
    //利用Tuple静态方法构建元组，最多支持八个元素：
    var testTuple6 = ValueTuple.Create<int, int, int, int, int, int>(1, 2, 3, 4, 5, 6);
    Console.WriteLine($"Item 1: {testTuple6.Item1}, Item 6: {testTuple6.Item6}"); 
    
    var testTuple8 = ValueTuple.Create<int, int, int, int, int, int, int, int>(1, 2, 3, 4, 5, 6, 7, 8);
    Console.WriteLine($"Item 1: {testTuple8.Item1}, Item 8: {testTuple8.Rest.Item1}");
    //注意这里构建出来的Tuple类型其实是Tuple<int, int, int, int, int, int, int, Tuple<int>>，因此testTuple8.Rest取到的数据类型是Tuple<int>，因此要想获取准确值需要取Item1属性。
    
    //优化区别：当构造出超过7个元素以上的值元组后，可以使用接下来的ItemX进行访问嵌套元组中的值，对于上面的例子，要访问第十个元素，既可以通过testTuple10.Rest.Item3访问，也可以通过testTuple10.Item10来访问。
    
    var testTuple10 = new ValueTuple<int, int, int, int, int, int, int, ValueTuple<int, int, int>>(1, 2, 3, 4, 5, 6, 7, new ValueTuple<int, int, int>(8, 9, 10));
    Console.WriteLine($"Item 10: {testTuple10.Rest.Item3}, Item 10: {testTuple10.Item10}");
    ```

## 参数传递
- 值传递
    ```cs
    pass
    ```
- 引用传递
    ```cs
    public void swap(ref int x,ref int y){
        int tmp;
        tmp = x; x = y; y = tmp;
    }
    int a = 1,b = 2;
    swap(ref a,ref b);
    ```
- 输出传递  
    ```cs
    public void getValue(out int x){
        x = 5;
    }
    int a = 10;
    getValue(out a); // a=5
    ```
## 类型判断
```csharp
int   i   =   5; 
Console.WriteLine( "i is an int? {0}",i.GetType()==typeof(int));
Console.WriteLine( "i is an int? {0}",typeof(int).IsInstanceOfType(i)); 
```
## 可空类型
- nullable `?`
    ```cs
    int? num1 = null;
    int? num2 = 5;
    ```
- null合并 `??`
    ```cs
    int num1 = null;
    int num2 = 314;
    int num3 = num1??666; // num3 = 666
    int num4 = num2??666; // num4 = 314
    ```
## 数组
[多维数组](http://www.runoob.com/csharp/csharp-multi-dimensional-arrays.html)
- 初始化  
数组是一个引用类型，所以需要使用 new 关键字来创建数组的实例。  
批量初始化[固定值](http://igoro.com/archive/7-tricks-to-simplify-your-programs-with-linq/)  `int[] a = Enumerable.Repeat(-1, 10).ToArray();`
    ```cs
    int[] arr = new int[10];
    double[] balance = { 2340.0, 4523.69, 3421.0};
    int [] marks = new int[5]  { 99,  98, 92, 97, 95};
    int [] marks = new int[]  { 99,  98, 92, 97, 95};
    
    int [] marks = new int[]  { 99,  98, 92, 97, 95};
    int[] score = marks; //目标和源会指向相同的内存位置
    ```

- foreach循环  
可以使用一个 foreach 语句来遍历数组
    ```cs
    int[] nums = new int[10];
    foreach (int num in nums){
        Console.WriteLine("element is:{0}",num);
    }
    ```
- Array类  
Array 类是 C# 中所有数组的基类，它是在 System 命名空间中定义。Array 类提供了各种用于数组的属性和方法
```cs
属性：
1	IsFixedSize
//获取一个值，该值指示数组是否带有固定大小。
2	IsReadOnly
//获取一个值，该值指示数组是否只读。
3	Length
//获取一个 32 位整数，该值表示所有维度的数组中的元素总数。
4	LongLength
//获取一个 64 位整数，该值表示所有维度的数组中的元素总数。
5	Rank
//获取数组的秩（维度）。

方法：
1	Clear
//根据元素的类型，设置数组中某个范围的元素为零、为 false 或者为 null。
2	Copy(Array, Array, Int32)
//从数组的第一个元素开始复制某个范围的元素到另一个数组的第一个元素位置。长度由一个 32 位整数指定。
3	CopyTo(Array, Int32)
//从当前的一维数组中复制所有的元素到一个指定的一维数组的指定索引位置。索引由一个 32 位整数指定。
4	GetLength 
//获取一个 32 位整数，该值表示指定维度的数组中的元素总数。arr.getlength(1)第一维度的长度
5	GetLongLength
//获取一个 64 位整数，该值表示指定维度的数组中的元素总数。
6	GetLowerBound
//获取数组中指定维度的下界。
7	GetType
//获取当前实例的类型。从对象（Object）继承。
8	GetUpperBound
//获取数组中指定维度的上界。
9	GetValue(Int32)
//获取一维数组中指定位置的值。索引由一个 32 位整数指定。
10	IndexOf(Array, Object)
//搜索指定的对象，返回整个一维数组中第一次出现的索引。
11	Reverse(Array)
//逆转整个一维数组中元素的顺序。
12	SetValue(Object, Int32)
//给一维数组中指定位置的元素设置值。索引由一个 32 位整数指定。
13	Sort(Array)
//使用数组的每个元素的 IComparable 实现来排序整个一维数组中的元素。
14	ToString
//返回一个表示当前对象的字符串。从对象（Object）继承。
15 ToList
// 转化为List，I ADD IT 2018.12.19
```
## string
- 初始化
    ```cs
    using System;
    
    namespace StringApplication
    {
        class Program
        {
            static void Main(string[] args)
            {
               //字符串，字符串连接
                string fname, lname;
                fname = "Rowan";
                lname = "Atkinson";
    
                string fullname = fname + lname;
                Console.WriteLine("Full Name: {0}", fullname);
    
                //通过使用 string 构造函数
                char[] letters = { 'H', 'e', 'l', 'l','o' };
                string greetings = new string(letters);
                Console.WriteLine("Greetings: {0}", greetings);
    
                //方法返回字符串
                string[] sarray = { "Hello", "From", "Tutorials", "Point" };
                string message = String.Join(" ", sarray);
                Console.WriteLine("Message: {0}", message);
    
                //用于转化值的格式化方法
                DateTime waiting = new DateTime(2012, 10, 10, 17, 58, 1);
                string chat = String.Format("Message sent at {0:t} on {0:D}", 
                waiting);
                Console.WriteLine("Message: {0}", chat);
                Console.ReadKey() ;
            }
        }
    }
    /*
    Full Name: RowanAtkinson
    Greetings: Hello
    Message: Hello From Tutorials Point
    Message: Message sent at 17:58 on Wednesday, 10 October 2012
    */
    ```
- string类的方法
    ```cs
    string.Length  // length
    
    public bool Contains( string value ) 
    //返回一个表示指定 string 对象是否出现在字符串中的值。
    
    public static string Copy( string str ) 
    //创建一个与指定字符串具有相同值的新的 String 对象。
    
    public string Trim()
    //移除当前 String 对象中的所有前导空白字符和后置空白字符
    
    public string ToUpper()
    //把字符串转换为大写并返回。
    
    public string ToLower()
    //把字符串转换为小写并返回。
    
    public static int Compare( string strA, string strB ) 
    //比较两个指定的 string 对象，并返回一个表示它们在排列顺序中相对位置的整数。该方法区分大小写。
    
    public static int Compare( string strA, string strB, bool ignoreCase ) 
    //比较两个指定的 string 对象，并返回一个表示它们在排列顺序中相对位置的整数。但是，如果布尔参数为真时，该方法不区分大小写。
    
    public static string Concat( string str0, string str1 ) 
    //连接两个 string 对象。
    
    public static string Concat( string str0, string str1, string str2, string str3 ) 
    //连接四个 string 对象。
    
    public static string Concat( string str0, string str1, string str2 ) 
    //连接三个 string 对象。
    
    
    
    public char[] ToCharArray( int startIndex, int length ) 
    //返回一个带有当前 string 对象中所有字符的 Unicode 字符数组，从指定的索引开始，直到指定的长度为止。
    
    public char[] ToCharArray()
    //返回一个带有当前 string 对象中所有字符的 Unicode 字符数组。
    
    public bool StartsWith( string value ) 
    //判断字符串实例的开头是否匹配指定的字符串。
    
    public string[] Split( char[] separator, int count ) 
    //返回一个字符串数组，包含当前的 string 对象中的子字符串，子字符串是使用指定的 Unicode 字符数组中的元素进行分隔的。int 参数指定要返回的子字符串的最大数目。
    
    public string[] Split( params char[] separator ) 
    //返回一个字符串数组，包含当前的 string 对象中的子字符串，子字符串是使用指定的 Unicode 字符数组中的元素进行分隔的。
    
    public string Replace( string oldValue, string newValue ) 
    //把当前 string 对象中，所有指定的字符串替换为另一个指定的字符串，并返回新的字符串。
    
    public string Replace( char oldChar, char newChar ) 
    //把当前 string 对象中，所有指定的 Unicode 字符替换为另一个指定的 Unicode 字符，并返回新的字符串。
    
    public string Remove( int startIndex, int count ) 
    //从当前字符串的指定位置开始移除指定数量的字符，并返回字符串。
    
    public string Remove( int startIndex ) 
    //移除当前实例中的所有字符，从指定位置开始，一直到最后一个位置为止，并返回字符串。
    
    public int LastIndexOf( string value ) 
    //返回指定字符串在当前 string 对象中最后一次出现的索引位置，索引从 0 开始。
    
    public int LastIndexOf( char value ) 
    //返回指定 Unicode 字符在当前 string 对象中最后一次出现的索引位置，索引从 0 开始。
    
    public static string Join( string separator, string[] value, int startIndex, int count ) 
    //连接接一个字符串数组中的指定位置开始的指定元素，使用指定的分隔符分隔每个元素。
    
    public static string Join( string separator, string[] value ) 
    //连接一个字符串数组中的所有元素，使用指定的分隔符分隔每个元素。
    
    public static bool IsNullOrEmpty( string value ) 
    //指示指定的字符串是否为 null 或者是否为一个空的字符串。
    
    public string Insert( int startIndex, string value ) 
    //返回一个新的字符串，其中，指定的字符串被插入在当前 string 对象的指定索引位置。
    
    public int IndexOfAny( char[] anyOf, int startIndex ) 
    //返回某一个指定的 Unicode 字符数组中任意字符从该实例中指定字符位置开始搜索第一次出现的索引，索引从 0 开始。
    
    public int IndexOfAny( char[] anyOf ) 
    //返回某一个指定的 Unicode 字符数组中任意字符在该实例中第一次出现的索引，索引从 0 开始。
    
    public int IndexOf( string value, int startIndex ) 
    //返回指定字符串从该实例中指定字符位置开始搜索第一次出现的索引，索引从 0 开始。
    
    public int IndexOf( char value, int startIndex ) 
    //返回指定 Unicode 字符从该字符串中指定字符位置开始搜索第一次出现的索引，索引从 0 开始。
    
    public int IndexOf( string value ) 
    //返回指定字符串在该实例中第一次出现的索引，索引从 0 开始。
    
    public int IndexOf( char value ) 
    //返回指定 Unicode 字符在当前字符串中第一次出现的索引，索引从 0 开始。
    
    public static string Format( string format, Object arg0 ) 
    //把指定字符串中一个或多个格式项替换为指定对象的字符串表示形式。
    
    public static bool Equals( string a, string b ) 
    //判断两个指定的 string 对象是否具有相同的值。
    
    public bool Equals( string value ) 
    //判断当前的 string 对象是否与指定的 string 对象具有相同的值。
    
    public bool EndsWith( string value ) 
    //判断 string 对象的结尾是否匹配指定的字符串。
    
    public void CopyTo( int sourceIndex, char[] destination, int destinationIndex, int count ) 
    //从 string 对象的指定位置开始复制指定数量的字符到 Unicode 字符数组中的指定位置。
    
    // example:
    string str = "Last night I dreamt of San Pedro"; 
    Console.WriteLine(str); 
    string substr = str.Substring(23); //San Pedro
    ```
- 日期相关
    ```cs
    DateTime dt = new DateTime(2017,4,1,13,16,32,108);
    string.Format("{0:y yy yyy yyyy}",dt); //17 17 2017 2017
    string.Format("{0:M MM MMM MMMM}", dt);//4  04 四月 四月
    string.Format("{0:d dd ddd dddd}", dt);//1  01 周六 星期六
    string.Format("{0:t tt}", dt);//下 下午
    string.Format("{0:H HH}", dt);//13 13
    string.Format("{0:h hh}", dt);//1  01
    string.Format("{0:m mm}", dt);//16 16
    string.Format("{0:s ss}", dt);//32 32
    string.Format("{0:F FF FFF FFFF FFFFF FFFFFF FFFFFFF}", dt);//1 1  108 108  108   108    108
    string.Format("{0:f ff fff ffff fffff ffffff fffffff}", dt);//1 10 108 1080 10800 108000 1080000
    string.Format("{0:z zz zzz}", dt);//+8 +08 +08:00
    
    string.Format("{0:yyyy/MM/dd HH:mm:ss.fff}",dt);　　//2017/04/01 13:16:32.108
    string.Format("{0:yyyy/MM/dd dddd}", dt);　　　　　　//2017/04/01 星期六
    string.Format("{0:yyyy/MM/dd dddd tt hh:mm}", dt); //2017/04/01 星期六 下午 01:16
    string.Format("{0:yyyyMMdd}", dt);　　　　　　　　　//20170401
    string.Format("{0:yyyy-MM-dd HH:mm:ss.fff}", dt);　//2017-04-01 13:16:32.108
    ```
    ```cs
    DateTime dt = new DateTime(2017,4,1,13,16,32,108);
    dt.ToString("y yy yyy yyyy");//17 17 2017 2017
    dt.ToString("M MM MMM MMMM");//4  04 四月 四月
    dt.ToString("d dd ddd dddd");//1  01 周六 星期六
    dt.ToString("t tt");//下 下午
    dt.ToString("H HH");//13 13
    dt.ToString("h hh");//1  01
    dt.ToString("m mm");//16 16
    dt.ToString("s ss");//32 32
    dt.ToString("F FF FFF FFFF FFFFF FFFFFF FFFFFFF");//1 1  108 108  108   108    108
    dt.ToString("f ff fff ffff fffff ffffff fffffff");//1 10 108 1080 10800 108000 1080000
    dt.ToString("z zz zzz");//+8 +08 +08:00
    
    dt.ToString("yyyy/MM/dd HH:mm:ss.fff");　//2017/04/01 13:16:32.108
    dt.ToString("yyyy/MM/dd dddd");　　　　　　//2017/04/01 星期六
    dt.ToString("yyyy/MM/dd dddd tt hh:mm"); //2017/04/01 星期六 下午 01:16
    dt.ToString("yyyyMMdd");　　　　　　　　　//20170401
    dt.ToString("yyyy-MM-dd HH:mm:ss.fff");　//2017-04-01 13:16:32.108
    ```
## StringBuilder
- [动态分配的string](https://www.cnblogs.com/skychen1218/p/3593678.html)

## 结构体struct
- 定义
    ```cs
    struct Books{
       public string title;
       public string author;
       public string subject;
       public int book_id;
       public void getValues(string t, string a, string s, int id){
          title = t;
          author = a;
          subject = s;
          book_id =id; 
       }
    };  
    /*
    结构可带有方法、字段、索引、属性、运算符方法和事件。
    结构可定义构造函数，但不能定义析构函数。但是，您不能为结构定义默认的构造函数。默认的构造函数是自动定义的，且不能被改变。
    与类不同，结构不能继承其他的结构或类。
    结构不能作为其他结构或类的基础结构。
    结构可实现一个或多个接口。
    结构成员不能指定为 abstract、virtual 或 protected。
    当您使用 New 操作符创建一个结构对象时，会调用适当的构造函数来创建结构。与类不同，结构可以不使用 New 操作符即可被实例化。
    如果不使用 New 操作符，只有在所有的字段都被初始化之后，字段才被赋值，对象才被使用。
    */
    ```
- struct vs class
    ```cs
    //类是引用类型，结构是值类型。
    //结构不支持继承。
    //结构不能声明默认的构造函数。
    ```
## enum
```cs
using System;

public class EnumTest
{
    enum Day { Sun, Mon, Tue, Wed, Thu, Fri, Sat };

    static void Main()
    {
        int x = (int)Day.Sun;
        int y = (int)Day.Fri;
        Console.WriteLine("Sun = {0}", x);
        Console.WriteLine("Fri = {0}", y);
    }
}
//Sun = 0
//Fri = 5

```

## 类class
- 定义  
访问标识符 `<access specifier>` 指定了对类及其成员的访问规则。如果没有指定，则使用默认的访问标识符。类的默认访问标识符是 `internal`，成员的默认访问标识符是 `private`。
```cs
<access specifier> class  class_name 
{
    // member variables
    <access specifier> <data type> variable1;
    ...
    <access specifier> <data type> variableN;
    
    // member methods
    <access specifier> <return type> methodN(parameter_list) 
    {
        // method body 
    }
}
```
- 构造函数  
默认的构造函数没有任何参数。但是如果你需要一个带有参数的构造函数可以有参数，这种构造函数叫做参数化构造函数。这种技术可以帮助你在创建对象的同时给对象赋初始值
    ```cs
    using System;
    namespace LineApplication
    {
       class Line
       {
          private double length;   // 线条的长度
          public Line(double len)  // 参数化构造函数
          {
             Console.WriteLine("对象已创建，length = {0}", len);
             length = len;
          }
    
          public void setLength( double len )
          {
             length = len;
          }
          public double getLength()
          {
             return length;
          }
    
          static void Main(string[] args)
          {
             Line line = new Line(10.0);
             Console.WriteLine("线条的长度： {0}", line.getLength()); 
             // 设置线条长度
             line.setLength(6.0);
             Console.WriteLine("线条的长度： {0}", line.getLength()); 
             Console.ReadKey();
          }
       }
    }
    ```
- 析构函数  
    - 类的析构函数是类的一个特殊的成员函数，当类的对象超出范围时执行。  
    - 析构函数的名称是在类的名称前加上一个波浪形（~）作为前缀，它不返回值，也不带任何参数。  
    - 析构函数用于在结束程序（比如关闭文件、释放内存等）之前释放资源。析构函数不能继承或重载。
    ```cs
    using System;
    namespace LineApplication
    {
       class Line
       {
          private double length;   // 线条的长度
          public Line()  // 构造函数
          {
             Console.WriteLine("对象已创建");
          }
          ~Line() //析构函数
          {
             Console.WriteLine("对象已删除");
          }
    
          public void setLength( double len )
          {
             length = len;
          }
          public double getLength()
          {
             return length;
          }
    
          static void Main(string[] args)
          {
             Line line = new Line();
             // 设置线条长度
             line.setLength(6.0);
             Console.WriteLine("线条的长度： {0}", line.getLength());           
          }
       }
    }
    ```
- 静态成员
    - 我们可以使用 static 关键字把类成员定义为静态的。当我们声明一个类成员为静态时，意味着无论有多少个类的对象被创建，只会有一个该静态成员的副本。

    - 关键字 static 意味着类中只有一个该成员的实例。静态变量用于定义常量，因为它们的值可以通过直接调用类而不需要创建类的实例来获取。静态变量可在成员函数或类的定义外部进行初始化。你也可以在类的定义内部初始化静态变量。
    - 也可以把一个成员函数声明为 static。这样的函数只能访问静态变量。静态函数在对象被创建之前就已经存在。
    ```cs
    using System;
    namespace StaticVarApplication
    {
        class StaticVar
        {
           public static int num;
            public void count()
            {
                num++;
            }
            public int getNum()
            {
                return num;
            }
        }
        class StaticTester
        {
            static void Main(string[] args)
            {
                StaticVar s1 = new StaticVar();
                StaticVar s2 = new StaticVar();
                s1.count();
                s1.count();
                s1.count();
                s2.count();
                s2.count();
                s2.count();         
                Console.WriteLine("s1 的变量 num： {0}", s1.getNum());
                Console.WriteLine("s2 的变量 num： {0}", s2.getNum());
                Console.ReadKey();
            }
        }
    }
    //s1 的变量 num： 6
    //s2 的变量 num： 6
    ```

    将类成员函数声明为public static无需实例化即可调用类成员函数
    ```cs
    using System;
    
    namespace ConsoleApp
    {
        class Program
        {
            static void Main(string[] args)
            {
                int num = AddClass.Add(2, 3);  //编译通过
                Console.WriteLine(num);
            }
        }
    
        class AddClass
        {
            public static int Add(int x,int y)
            {
                return x + y;
            }
        }
    }
    
    ```

## 继承
继承的思想实现了 属于（IS-A） 关系。例如，哺乳动物 属于（IS-A） 动物，狗 属于（IS-A） 哺乳动物，因此狗 属于（IS-A） 动物

- 基类和派生类
    ```cs
    using System;
    namespace InheritanceApplication
    {
       class Shape 
       {
          public void setWidth(int w)
          {
             width = w;
          }
          public void setHeight(int h)
          {
             height = h;
          }
          protected int width;
          protected int height;
       }
    
       // 派生类
       class Rectangle: Shape
       {
          public int getArea()
          { 
             return (width * height); 
          }
       }
       
       class RectangleTester
       {
          static void Main(string[] args)
          {
             Rectangle Rect = new Rectangle();
    
             Rect.setWidth(5);
             Rect.setHeight(7);
    
             // 打印对象的面积
             Console.WriteLine("总面积： {0}",  Rect.getArea());
             Console.ReadKey();
          }
       }
    }
    ```
- 基类初始化  ?  
派生类继承了基类的成员变量和成员方法。因此父类对象应在子类对象创建之前被创建。可以在成员初始化列表中进行父类的初始化。
    ```cs
    using System;
    namespace RectangleApplication
    {
       class Rectangle
       {
          // 成员变量
          protected double length;
          protected double width;
          public Rectangle(double l, double w)
          {
             length = l;
             width = w;
          }
          public double GetArea()
          {
             return length * width;
          }
          public void Display()
          {
             Console.WriteLine("长度： {0}", length);
             Console.WriteLine("宽度： {0}", width);
             Console.WriteLine("面积： {0}", GetArea());
          }
       }//end class Rectangle  
       class Tabletop : Rectangle
       {
          private double cost;
          public Tabletop(double l, double w) : base(l, w)
          { }
          public double GetCost()
          {
             double cost;
             cost = GetArea() * 70;
             return cost;
          }
          public void Display()
          {
             base.Display();
             Console.WriteLine("成本： {0}", GetCost());
          }
       }
       class ExecuteRectangle
       {
          static void Main(string[] args)
          {
             Tabletop t = new Tabletop(4.5, 7.5);
             t.Display();
             Console.ReadLine();
          }
       }
    }
    ```
- 多重继承  
C# 不支持多重继承。但是可以使用接口来实现多重继承。
    ```cs
    pass
    ```
- 为什么一个对象可以用父类声明，却用子类实例化
    - 这个实例是子类的，但是因为你声明时是用父类声明的，所以你用正常的办法访问不到子类自己的成员，只能访问到从父类继承来的成员。

    - 在子类中用 override 重写父类中用 virtual 申明的虚方法时，实例化父类调用该方法，执行时调用的是子类中重写的方法；

    - 如果子类中用 new 覆盖父类中用 virtual 申明的虚方法时，实例化父类调用该方法，执行时调用的是父类中的虚方法。
- **多态**  
    - 多态性意味着有多重形式。在面向对象编程范式中，多态性往往表现为"一个接口，多个功能"。

    - 多态性可以是静态的或动态的。在`静态多态性`中，函数的响应是在编译时发生的。在`动态多态性`中，函数的响应是在运行时发生的。
    - ***静态多态性***  
    在编译时，函数和对象的连接机制被称为早期绑定，也被称为静态绑定。
        - 函数重载
            - 可以在同一个范围内对相同的函数名有多个定义。函数的定义必须彼此不同，可以是参数列表中的参数类型不同，也可以是参数个数不同。不能重载只有返回类型不同的函数声明。
        - 运算符重载
    - ***动态多态性***  
    动态多态性是通过 抽象类 和 虚方法 实现的。
        - `abstract`  (类似纯虚函数？)  
    C# 允许您使用关键字 abstract 创建抽象类，用于提供接口的部分类的实现。当一个派生类继承自该抽象类时，实现即完成。抽象类包含抽象方法，抽象方法可被派生类实现。派生类具有更专业的功能。
        - `vitual`  
        当有一个定义在类中的函数需要在继承类中实现时，可以使用虚方法。虚方法是使用关键字 virtual 声明的。虚方法可以在不同的继承类中有不同的实现。对虚方法的调用是在运行时发生的。  
        
        ```cs
        // abstract method
        using System;
        namespace PolymorphismApplication
        {
           abstract class Shape  // 类也要用 abstract
           {
               abstract public int area();  // 函数用 abstract
           }
           class Rectangle:  Shape
           {
              private int length;
              private int width;
              public Rectangle( int a=0, int b=0)
              {
                 length = a;
                 width = b;
              }
              public override int area ()  // 需要用 override
              { 
                 Console.WriteLine("Rectangle 类的面积：");
                 return (width * length); 
              }
           }
        
           class RectangleTester
           {
              static void Main(string[] args)
              {
                 Rectangle r = new Rectangle(10, 7);
                 double a = r.area();
                 Console.WriteLine("面积： {0}",a);
                 Console.ReadKey();
              }
           }
        }
        ```
        ```cs
        // vitual method 和 C++ 类似
        using System;
        namespace PolymorphismApplication
        {
           class Shape 
           {
              protected int width, height;
              public Shape( int a=0, int b=0)
              {
                 width = a;
                 height = b;
              }
              public virtual int area() // 基类函数 + vitual
              {
                 Console.WriteLine("父类的面积：");
                 return 0;
              }
           }
           class Rectangle: Shape
           {
              public Rectangle( int a=0, int b=0): base(a, b)
              {
        
              }
              public override int area ()  // 和 C++ 不同点：子类方法 + override
              {
                 Console.WriteLine("Rectangle 类的面积：");
                 return (width * height); 
              }
           }
           class Triangle: Shape
           {
              public Triangle(int a = 0, int b = 0): base(a, b)
              {
              
              }
              public override int area()
              {
                 Console.WriteLine("Triangle 类的面积：");
                 return (width * height / 2); 
              }
           }
           class Caller
           {
              public void CallArea(Shape sh)
              {
                 int a;
                 a = sh.area();
                 Console.WriteLine("面积： {0}", a);
              }
           }  
           class Tester
           {
              
              static void Main(string[] args)
              {
                 Caller c = new Caller();
                 Rectangle r = new Rectangle(10, 7);
                 Triangle t = new Triangle(10, 5);
                 c.CallArea(r);
                 c.CallArea(t);
                 Console.ReadKey();
              }
           }
        }
        ```
## 运算符重载
- operator  
可以重定义或重载 C# 中内置的运算符。因此，程序员也可以使用用户自定义类型的运算符。重载运算符是具有特殊名称的函数，是通过关键字 `operator` 后跟运算符的符号来定义的。[[click here for more info]](http://www.runoob.com/csharp/csharp-operator-overloading.html)
    ```cs
    using System;
    
    namespace OperatorOvlApplication
    {
       class Box
       {
          private double length;      // 长度
          private double breadth;     // 宽度
          private double height;      // 高度
    
          public double getVolume()
          {
             return length * breadth * height;
          }
          public void setLength( double len )
          {
             length = len;
          }
    
          public void setBreadth( double bre )
          {
             breadth = bre;
          }
    
          public void setHeight( double hei )
          {
             height = hei;
          }
          // 重载 + 运算符来把两个 Box 对象相加
          public static Box operator+ (Box b, Box c)
          {
             Box box = new Box();
             box.length = b.length + c.length;
             box.breadth = b.breadth + c.breadth;
             box.height = b.height + c.height;
             return box;
          }
    
       }
    // 上面的函数为用户自定义的类 Box 实现了加法运算符（+）。它把两个 Box 对象的属性相加，并返回相加后的 Box 对象。
    }
    ```
## 接口
- interface  
    - 接口定义了所有类继承接口时应遵循的语法合同。接口定义了语法合同 "是什么" 部分，派生类定义了语法合同 "怎么做" 部分。

    - 接口定义了属性、方法和事件，这些都是接口的成员。接口只包含了成员的声明。成员的定义是派生类的责任。接口提供了派生类应遵循的标准结构。

    - 接口使得实现接口的类或结构在形式上保持一致。

    - 抽象类在某种程度上与接口类似，但是，它们大多只是用在当只有少数方法由基类声明由派生类实现时。

- 定义接口  
接口使用 `interface` 关键字声明，它与类的声明类似。接口声明默认是 `public` 的。下面是一个接口声明的实例：
    ```cs
    using System;
    
    interface IMyInterface
    {
        // 接口成员
        void MethodToImplement();
    }
    //以上代码定义了接口 IMyInterface。通常接口命令以 I 字母开头，这个接口只有一个方法 MethodToImplement()，没有参数和返回值，当然我们可以按照需求设置参数和返回值。
    //该方法并没有具体的实现。
    
    class InterfaceImplementer : IMyInterface
    {
        static void Main()
        {
            InterfaceImplementer iImp = new InterfaceImplementer();
            iImp.MethodToImplement();
        }
    
        public void MethodToImplement()
        {
            Console.WriteLine("MethodToImplement() called.");
        }
    }
    ```
- 接口继承  
    ```cs
         (1)通过接口可以实现多重继承，C# 接口的成员不能有 public、protected、internal、private 等修饰符。原因很简单，接口里面的方法都需要由外面接口实现去实现方法体，那么其修饰符必然是 public。C# 接口中的成员默认是 public 的，java 中是可以加 public 的。
     (2)接口成员不能有 new、static、abstract、override、virtual 修饰符。有一点要注意，当一个接口实现一个接口，这2个接口中有相同的方法时，可用 new 关键字隐藏父接口中的方法。
     (3)接口中只包含成员的签名，接口没有构造函数，所有不能直接使用 new 对接口进行实例化。接口中只能包含方法、属性、事件和索引的组合。接口一旦被实现，实现类必须实现接口中的所有成员，除非实现类本身是抽象类。
     (4)C# 是单继承，接口是解决 C# 里面类可以同时继承多个基类的问题。
    ```

## 命名空间
命名空间的设计目的是提供一种让一组名称与其他名称分隔开的方式。在一个命名空间中声明的类的名称与另一个命名空间中声明的相同的类的名称不冲突。
- namespace  
    ```cs
    using System;
    namespace first_space
    {
       class namespace_cl
       {
          public void func()
          {
             Console.WriteLine("Inside first_space");
          }
       }
    }
    namespace second_space
    {
       class namespace_cl
       {
          public void func()
          {
             Console.WriteLine("Inside second_space");
          }
       }
    }   
    class TestClass
    {
       static void Main(string[] args)
       {
          first_space.namespace_cl fc = new first_space.namespace_cl();
          second_space.namespace_cl sc = new second_space.namespace_cl();
          fc.func();
          sc.func();
          Console.ReadKey();
       }
    }
    ```
- using  
`using` 关键字表明程序使用的是给定命名空间中的名称
- 嵌套命名空间
    ```cs
    using System;
    using SomeNameSpace;
    using SomeNameSpace.Nested;
    
    namespace SomeNameSpace
    {
        public class MyClass 
        {
            static void Main() 
            {
                Console.WriteLine("In SomeNameSpace");
                Nested.NestedNameSpaceClass.SayHello();
            }
        }
    
        // 内嵌命名空间
        namespace Nested   
        {
            public class NestedNameSpaceClass 
            {
                public static void SayHello() 
                {
                    Console.WriteLine("In Nested");
                }
            }
        }
    }
    // out_put:
    //In SomeNameSpace
    //In Nested
    ```
## 预处理指令
- 特点    
    - 所有的预处理器指令都是以 #开始。且在一行上，只有空白字符可以出现在预处理器指令之前。预处理器指令不是语句，所以它们不以分号（;）结束。

    - C# 编译器没有一个单独的预处理器，但是，指令被处理时就像是有一个单独的预处理器一样。在 C# 中，预处理器指令用于在条件编译中起作用。与 C 和 C++ 不同的是，它们不是用来创建宏。一个预处理器指令必须是该行上的唯一指令。
    ```cs
    #define	//它用于定义一系列成为符号的字符。
    #undef	//它用于取消定义符号。
    #if	//它用于测试符号是否为真。
    #else	//它用于创建复合条件指令，与 #if 一起使用。
    #elif	//它用于创建复合条件指令。
    #endif	//指定一个条件指令的结束。
    #line	//它可以让您修改编译器的行数以及（可选地）输出错误和警告的文件名。
    #error	//它允许从代码的指定位置生成一个错误。
    #warning	//它允许从代码的指定位置生成一级警告。
    #region	//它可以让您在使用 Visual Studio Code Editor 的大纲特性时，指定一个可展开或折叠的代码块。
    #endregion	//它标识着 #region 块的结束。
    ```
- `#define` `#if` `#else` `#endif`
    ```cs
    #define PI 
    using System;
    namespace PreprocessorDAppl
    {
       class Program
       {
          static void Main(string[] args)
          {
             #if (PI)
                Console.WriteLine("PI is defined");
             #else
                Console.WriteLine("PI is not defined");
             #endif
             Console.ReadKey();
          }
       }
    }
    //PI is defined
    ```
## 正则表达式
与Python类似 [[More Info Here]](http://www.runoob.com/csharp/csharp-regular-expressions.html)
- Regex类
```cs
1	public bool IsMatch( string input ) 
//指示 Regex 构造函数中指定的正则表达式是否在指定的输入字符串中找到匹配项。

2	public bool IsMatch( string input, int startat ) 
//指示 Regex 构造函数中指定的正则表达式是否在指定的输入字符串中找到匹配项，从字符串中指定的开始位置开始。

3	public static bool IsMatch( string input, string pattern ) 
//指示指定的正则表达式是否在指定的输入字符串中找到匹配项。

4	public MatchCollection Matches( string input ) 
//在指定的输入字符串中搜索正则表达式的所有匹配项。

5	public string Replace( string input, string replacement ) 
//在指定的输入字符串中，把所有匹配正则表达式模式的所有匹配的字符串替换为指定的替换字符串。

6	public string[] Split( string input ) 
//把输入字符串分割为子字符串数组，根据在 Regex 构造函数中指定的正则表达式模式定义的位置进行分割。
```
- 例子
```cs
using System;
using System.Text.RegularExpressions;

public class Example
{
   public static void Main()
   {
      string input = "1851 1999 1950 1905 2003";
      string pattern = @"(?<=19)\d{2}\b";

      foreach (Match match in Regex.Matches(input, pattern))
         Console.WriteLine(match.Value);
   }
}
```
## 异常处理
[[More Info Here]](http://www.runoob.com/csharp/csharp-exception-handling.html)
- 关键词
    - `try`  
    一个 try 块标识了一个将被激活的特定的异常的代码块。后跟一个或多个 catch 块。
    - `catch`  
    程序通过异常处理程序捕获异常。catch 关键字表示异常的捕获。
    - `finally`  
    finally 块用于执行给定的语句，不管异常是否被抛出都会执行。例如，如果您打开一个文件，不管是否出现异常文件都要被关闭。
    - `throw`  
    当问题出现时，程序抛出一个异常。使用 throw 关键字来完成。
    ```cs
    try
    {
       // 引起异常的语句
    }
    catch( ExceptionName e1 )
    {
       // 错误处理代码
    }
    catch( ExceptionName e2 )
    {
       // 错误处理代码
    }
    catch( ExceptionName eN )
    {
       // 错误处理代码
    }
    finally
    {
       // 要执行的语句
    }
    
    using System;
    namespace ErrorHandlingApplication
    {
        class DivNumbers
        {
            int result;
            DivNumbers()
            {
                result = 0;
            }
            public void division(int num1, int num2)
            {
                try
                {
                    result = num1 / num2;
                }
                catch (DivideByZeroException e)
                {
                    Console.WriteLine("Exception caught: {0}", e);
                }
                finally
                {
                    Console.WriteLine("Result: {0}", result);
                }
    
            }
            static void Main(string[] args)
            {
                DivNumbers d = new DivNumbers();
                d.division(25, 0);
                Console.ReadKey();
            }
        }
    }
    ```

## 文件IO
- IO类  
System.IO命名空间有各种不同的类，用于执行各种文件操作，如创建和删除文件、读取或写入文件，关闭文件等。
    ```cs
    BinaryReader	从二进制流读取原始数据。
    BinaryWriter	以二进制格式写入原始数据。
    BufferedStream	字节流的临时存储。
    Directory	有助于操作目录结构。
    DirectoryInfo	用于对目录执行操作。
    DriveInfo	提供驱动器的信息。
    File	有助于处理文件。
    FileInfo	用于对文件执行操作。
    FileStream	用于文件中任何位置的读写。
    MemoryStream	用于随机访问存储在内存中的数据流。
    Path	对路径信息执行操作。
    StreamReader	用于从字节流中读取字符。
    StreamWriter	用于向一个流中写入字符。
    StringReader	用于读取字符串缓冲区。
    StringWriter	用于写入字符串缓冲区。
    ```
- FileStream类    
    - System.IO命名空间中的 FileStream 类有助于文件的读写与关闭。该类派生自抽象类 Stream。
    ```cs
    //创建一个 FileStream 对象 F 来读取名为 sample.txt 的文件：
    FileStream F = new FileStream("sample.txt", FileMode.Open, FileAccess.Read, FileShare.Read);
    ```
    - FileMode  
        FileMode 枚举定义了各种打开文件的方法。FileMode 枚举的成员有：
    ```cs
    Append：打开一个已有的文件，并将光标放置在文件的末尾。如果文件不存在，则创建文件。
    Create：创建一个新的文件。如果文件已存在，则删除旧文件，然后创建新文件。
    CreateNew：指定操作系统应创建一个新的文件。如果文件已存在，则抛出异常。
    Open：打开一个已有的文件。如果文件不存在，则抛出异常。
    OpenOrCreate：指定操作系统应打开一个已有的文件。如果文件不存在，则用指定的名称创建一个新的文件打开。
    Truncate：打开一个已有的文件，文件一旦打开，就将被截断为零字节大小。然后我们可以向文件写入全新的数据，但是保留文件的初始创建日期。如果文件不存在，则抛出异常。
    ```
    - FileAccess  
    ```cs
    FileAccess 枚举的成员有：Read、ReadWrite 和 Write。
    ```
    - FileShare  
        FileShare 枚举的成员有：

    ```cs

    Inheritable：允许文件句柄可由子进程继承。Win32 不直接支持此功能。
    None：谢绝共享当前文件。文件关闭前，打开该文件的任何请求（由此进程或另一进程发出的请求）都将失败。
    Read：允许随后打开文件读取。如果未指定此标志，则文件关闭前，任何打开该文件以进行读取的请求（由此进程或另一进程发出的请求）都将失败。但是，即使指定了此标志，仍可能需要附加权限才能够访问该文件。
    ReadWrite：允许随后打开文件读取或写入。如果未指定此标志，则文件关闭前，任何打开该文件以进行读取或写入的请求（由此进程或另一进程发出）都将失败。但是，即使指定了此标志，仍可能需要附加权限才能够访问该文件。
    Write：允许随后打开文件写入。如果未指定此标志，则文件关闭前，任何打开该文件以进行写入的请求（由此进程或另一进过程发出的请求）都将失败。但是，即使指定了此标志，仍可能需要附加权限才能够访问该文件。
    Delete：允许随后删除文件。
    ```
    - 例子
    ```cs
    using System;
    using System.IO;
    
    namespace FileIOApplication
    {
        class Program
        {
            static void Main(string[] args)
            {
                FileStream F = new FileStream("test.dat", 
                FileMode.OpenOrCreate, FileAccess.ReadWrite);
    
                for (int i = 1; i <= 20; i++)
                {
                    F.WriteByte((byte)i);
                }
    
                F.Position = 0;
    
                for (int i = 0; i <= 20; i++)
                {
                    Console.Write(F.ReadByte() + " ");
                }
                F.Close();
                Console.ReadKey();
            }
        }
    }
    ```
    
## VisualStudio操作
- VS中常用的快捷键
    ```cs
    　　Ctrl + k +d  //快速对齐代码
    　　Ctrl + z  //撤销
    　　Ctrl + s  //保存
    　　Ctrl + j  //快速弹出智能提示
    　　Shift + End、Shift + Home、Shift + 上下左右  //选中单行内容
    　　Ctrl + k + c //快速注释选中内容
    　　Ctrl + k + u //快速取消注选中的注释内容
    　　Alt + Shift +F10 //添加命名空间
    　　F1 //转到帮助
    　　F12 //查看类型定义
    　　#region ...#endregion  //折叠代码


    波浪线
    　　1)、如果你的代码中出现了红色的波浪线，意味着你的代码中出现了语法错误。
    　　2)、如果你的代码中出现了绿色的波浪线，说明你的代码语法并没有错误，只不过提示你有可能会出现错误，但是不一定会出现错误。警告线
        
    ```
- 注释  
    - C#引入了新的XML注释，即我们在某个函数前新起一行，输入///，VS.Net会自动增加XML格式的注释。
    - XML注释分为一级注释（Primary Tags）和二级注释（Secondary Tags），前者可以单独存在，后者必须包含在一级注释内部。
    ```cs
    I 一级注释
    1. <remarks>对类型进行描述，功能类似<summary>，据说建议使用<remarks>;
    2. <summary>对共有类型的类、方法、属性或字段进行注释；
    3. <value>主要用于属性的注释，表示属性的制的含义，可以配合<summary>使用；
    4. <param>用于对方法的参数进行说明，格式：<param name="param_name">value</param>；
    5. <returns>用于定义方法的返回值，对于一个方法，输入///后，会自动添加<summary>、<param>列表和<returns>；
    6. <exception>定义可能抛出的异常，格式：<exception cref="IDNotFoundException">；
    7. <example>用于给出如何使用某个方法、属性或者字段的使用方法；
    8. <permission>涉及方法的访问许可；
    9. <seealso>用于参考某个其它的东东:)，也可以通过cref设置属性；
    10. <include>用于指示外部的XML注释；
    II 二级注释
    1. <c> or <code>主要用于加入代码段；
    2. <para>的作用类似HTML中的<p>标记符，就是分段；
    3. <pararef>用于引用某个参数；
    4. <see>的作用类似<seealso>，可以指示其它的方法；
    5. <list>用于生成一个列表；
    另外，还可以自定义XML标签 
            
    ```
---
---
# C#进阶
## 数学计算库[..](https://docs.microsoft.com/zh-cn/dotnet/api/system.math?view=netframework-4.7.2)
```csharp
/// <summary>
/// The following class represents simple functionality of the trapezoid.
/// </summary>
using System;

namespace MathClassCS
{
	class MathTrapezoidSample
	{
		private double m_longBase;
		private double m_shortBase;
		private double m_leftLeg;
		private double m_rightLeg;

		public MathTrapezoidSample(double longbase, double shortbase, double leftLeg, double rightLeg)
		{
			m_longBase = Math.Abs(longbase);
			m_shortBase = Math.Abs(shortbase);
			m_leftLeg = Math.Abs(leftLeg);
			m_rightLeg = Math.Abs(rightLeg);
		}

		private double GetRightSmallBase()
		{
			return (Math.Pow(m_rightLeg,2.0) - Math.Pow(m_leftLeg,2.0) + Math.Pow(m_longBase,2.0) + Math.Pow(m_shortBase,2.0) - 2* m_shortBase * m_longBase)/ (2*(m_longBase - m_shortBase));
		}

		public double GetHeight()
		{
			double x = GetRightSmallBase();
			return Math.Sqrt(Math.Pow(m_rightLeg,2.0) - Math.Pow(x,2.0));
		}

		public double GetSquare()
		{
			return GetHeight() * m_longBase / 2.0;
		}

		public double GetLeftBaseRadianAngle()
		{
			double sinX = GetHeight()/m_leftLeg;
			return Math.Round(Math.Asin(sinX),2);
		}

		public double GetRightBaseRadianAngle()
		{
			double x = GetRightSmallBase();
			double cosX = (Math.Pow(m_rightLeg,2.0) + Math.Pow(x,2.0) - Math.Pow(GetHeight(),2.0))/(2*x*m_rightLeg);
			return Math.Round(Math.Acos(cosX),2);
		}

		public double GetLeftBaseDegreeAngle()
		{
			double x = GetLeftBaseRadianAngle() * 180/ Math.PI;
			return Math.Round(x,2);
		}

		public double GetRightBaseDegreeAngle()
		{
			double x = GetRightBaseRadianAngle() * 180/ Math.PI;
			return Math.Round(x,2);
		}

		static void Main(string[] args)
		{
			MathTrapezoidSample trpz = new MathTrapezoidSample(20.0, 10.0, 8.0, 6.0);
			Console.WriteLine("The trapezoid's bases are 20.0 and 10.0, the trapezoid's legs are 8.0 and 6.0");
			double h = trpz.GetHeight();
			Console.WriteLine("Trapezoid height is: " + h.ToString());
			double dxR = trpz.GetLeftBaseRadianAngle();
			Console.WriteLine("Trapezoid left base angle is: " + dxR.ToString() + " Radians");
			double dyR = trpz.GetRightBaseRadianAngle();
			Console.WriteLine("Trapezoid right base angle is: " + dyR.ToString() + " Radians");
			double dxD = trpz.GetLeftBaseDegreeAngle();
			Console.WriteLine("Trapezoid left base angle is: " + dxD.ToString() + " Degrees");
			double dyD = trpz.GetRightBaseDegreeAngle();
			Console.WriteLine("Trapezoid left base angle is: " + dyD.ToString() + " Degrees");
		}
	}
}
```

## 矩阵运算
- [一个矩阵运算库(github)](https://github.com/YanjieHe/MatrixLibrary)
## 文件路径
- 获取文件路径方式
```csharp
//1.获取模块的完整路径。 
string path1 = System.Diagnostics.Process.GetCurrentProcess().MainModule.FileName;

//2.获取和设置当前目录(该进程从中启动的目录)的完全限定目录 
string path2 = System.Environment.CurrentDirectory;

//3.获取应用程序的当前工作目录 
string path3 = System.IO.Directory.GetCurrentDirectory();

//4.获取程序的基目录 
string path4 = System.AppDomain.CurrentDomain.BaseDirectory;

//5.获取和设置包括该应用程序的目录的名称 
string path5 = System.AppDomain.CurrentDomain.SetupInformation.ApplicationBase;

//6.获取启动了应用程序的可执行文件的路径 
string path6 = System.Windows.Forms.Application.StartupPath;

//7.获取启动了应用程序的可执行文件的路径及文件名 
string path7 = System.Windows.Forms.Application.ExecutablePath; 

// 输出结果 
1. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release\XmlAndXsd.vshost.exe 
2. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release 
3. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release 
4. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release\ 
5. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release\ 
6. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release 
7. D:\work\prj\VP-VPlatform\XmlAndXsd\bin\Release\XmlAndXsd.EXE
```


## 文件读写  
[ref](http://www.runoob.com/csharp/csharp-file-io.html)  
一个 `文件` 是一个存储在磁盘中带有指定名称和目录路径的数据集合。当打开文件进行读写时，它变成一个 流。
从根本上说，流是通过通信路径传递的字节序列。有两个主要的流：`输入流` 和 `输出流`。输入流用于从文件读取数据（读操作），输出流用于向文件写入数据（写操作）。
```csharp
BinaryReader	//从二进制流读取原始数据。
BinaryWriter	//以二进制格式写入原始数据。
BufferedStream	//字节流的临时存储。
Directory	//有助于操作目录结构。
DirectoryInfo	//用于对目录执行操作。
DriveInfo	//提供驱动器的信息。
File	//有助于处理文件。
FileInfo	//用于对文件执行操作。
FileStream	//用于文件中任何位置的读写。
MemoryStream	//用于随机访问存储在内存中的数据流。
Path	//对路径信息执行操作。
StreamReader	//用于从字节流中读取字符。
StreamWriter	//用于向一个流中写入字符。
StringReader	//用于读取字符串缓冲区。
StringWriter	//用于写入字符串缓冲区。
```
- **FileStream 类**   
`FileStream F = new FileStream("sample.txt", FileMode.Open, FileAccess.Read, FileShare.Read);`
    ```csharp
    FileMode //枚举定义了各种打开文件的方法。FileMode 枚举的成员有:
    
    Append：//打开一个已有的文件，并将光标放置在文件的末尾。如果文件不存在，则创建文件。
    Create：//创建一个新的文件。如果文件已存在，则删除旧文件，然后创建新文件。
    CreateNew：//指定操作系统应创建一个新的文件。如果文件已存在，则抛出异常。
    Open：//打开一个已有的文件。如果文件不存在，则抛出异常。
    OpenOrCreate：//指定操作系统应打开一个已有的文件。如果文件不存在，则用指定的名称创建一个新的文件打开。
    Truncate：//打开一个已有的文件，文件一旦打开，就将被截断为零字节大小。然后我们可以向文件写入全新的数据，但是保留文件的初始创建日期。如果文件不存在，则抛出异常。
    
    FileAccess //枚举的成员有：
    Read ReadWrite  Write。
    
    FileShare //枚举的成员有：
    
    Inheritable：//允许文件句柄可由子进程继承。Win32 不直接支持此功能。
    None：//谢绝共享当前文件。文件关闭前，打开该文件的任何请求（由此进程或另一进程发出的请求）都将失败。
    Read：//允许随后打开文件读取。如果未指定此标志，则文件关闭前，任何打开该文件以进行读取的请求（由此进程或另一进程发出的请求）都将失败。但是，即使指定了此标志，仍可能需要附加权限才能够访问该文件。
    ReadWrite：//允许随后打开文件读取或写入。如果未指定此标志，则文件关闭前，任何打开该文件以进行读取或写入的请求（由此进程或另一进程发出）都将失败。但是，即使指定了此标志，仍可能需要附加权限才能够访问该文件。
    Write：//允许随后打开文件写入。如果未指定此标志，则文件关闭前，任何打开该文件以进行写入的请求（由此进程或另一进过程发出的请求）都将失败。但是，即使指定了此标志，仍可能需要附加权限才能够访问该文件。
    Delete：//允许随后删除文件。
    
    using System;
    using System.IO;
    
    namespace FileIOApplication
    {
        class Program
        {
            static void Main(string[] args)
            {
                FileStream F = new FileStream("test.dat", FileMode.OpenOrCreate, FileAccess.ReadWrite);
    
                for (int i = 1; i <= 20; i++)
                {
                    F.WriteByte((byte)i);
                }
    
                F.Position = 0;
    
                for (int i = 0; i <= 20; i++)
                {
                    Console.Write(F.ReadByte() + " ");
                }
                F.Close();
                Console.ReadKey();
            }
        }
    }
    ```

- **文本文件**  
`StreamReader` 和 `StreamWriter` 类用于文本文件的数据读写。这些类从抽象基类 Stream 继承，Stream 支持文件流的字节读写。
    - `StreamReader` 类继承自抽象基类 `TextReader`，表示阅读器读取一系列字符。
        ```csharp
        using System;
        using System.IO;
        
        namespace FileApplication
        {
            class Program
            {
                static void Main(string[] args)
                {
                    try
                    {
                        // 创建一个 StreamReader 的实例来读取文件 
                        // using 语句也能关闭 StreamReader
                        using (StreamReader sr = new StreamReader("c:/jamaica.txt"))
                        {
                            string line;
                           
                            // 从文件读取并显示行，直到文件的末尾 
                            while ((line = sr.ReadLine()) != null)
                            {
                                Console.WriteLine(line);
                            }
                        }
                    }
                    catch (Exception e)
                    {
                        // 向用户显示出错消息
                        Console.WriteLine("The file could not be read:");
                        Console.WriteLine(e.Message);
                    }
                    Console.ReadKey();
                }
            }
        }
        ```
    - `StreamWriter` 类继承自抽象类`TextWriter`，表示编写器写入一系列字符。  
        ```csharp
        using System;
        using System.IO;
        
        namespace FileApplication
        {
            class Program
            {
                static void Main(string[] args)
                {
        
                    string[] names = new string[] {"Zara Ali", "Nuha Ali"};
                    using (StreamWriter sw = new StreamWriter("names.txt"))
                    {
                        foreach (string s in names)
                        {
                            sw.WriteLine(s);
        
                        }
                    }
        
                    // 从文件中读取并显示每行
                    string line = "";
                    using (StreamReader sr = new StreamReader("names.txt"))
                    {
                        while ((line = sr.ReadLine()) != null)
                        {
                            Console.WriteLine(line);
                        }
                    }
                    Console.ReadKey();
                }
            }
        }
        ```
- **二进制文件**  
[ref](http://www.runoob.com/csharp/csharp-binary-files.html)
- **文件路径**
- **文件编码**  
[转utf-8](https://www.cnblogs.com/xiaofengfeng/archive/2011/12/23/2299679.html)
    ```csharp
    public static string get_uft8(string unicodeString)
        {
            UTF8Encoding utf8 = new UTF8Encoding();
            Byte[] encodedBytes = utf8.GetBytes(unicodeString);
            String decodedString = utf8.GetString(encodedBytes);
            return decodedString;
        }
    ```


# TODO list:
- [ ] 流程图
```
graph TD
    A[START] -->B(mid)
    B -->C{choose}
    C -->|1| D[100]
    C -->|2| E[90]
```
- [ ] 甘特图
```
gantt
dateFormat YYYY-MM-DD
title 计划表（demo）
section 初期
明确需求: 2018-12-14,5d
section 中期
调研+开发: 2018-12-24,14d
section 后期
收尾: 2019-01-07,5d

```
- [ ] MATH
```math
\oint_C x^3\, dx+4y^2\,dy

2 = \left(\frac{\left(3-x\right)\times 2}{3-x}\right)

\sum_{m=1}^\infty\sum_{n=1}^\infty\frac{m^2n}{3^m\left(m3^n+n3^m\right)}

\phi_n(\kappa) = \frac{1}{4\pi^2\kappa^2}\int_0^\infty\frac{\sin(\kappa R)}{\kappa R}\frac{\partial}{\partial R}\left[R^2\frac{\partial D_n(R)}{\partial R}\right]dR

```

- git problems [..](https://www.jianshu.com/p/450cd21b36a4)