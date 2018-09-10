<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html>
<head>
  <title></title>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <style type="text/css">
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
pre { line-height: 125%; }
body .hll { background-color: #ffffcc }
body  { background: #f8f8f8; }
body .c { color: #408080; font-style: italic } /* Comment */
body .err { border: 1px solid #FF0000 } /* Error */
body .k { color: #008000; font-weight: bold } /* Keyword */
body .o { color: #666666 } /* Operator */
body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
body .cp { color: #BC7A00 } /* Comment.Preproc */
body .c1 { color: #408080; font-style: italic } /* Comment.Single */
body .cs { color: #408080; font-style: italic } /* Comment.Special */
body .gd { color: #A00000 } /* Generic.Deleted */
body .ge { font-style: italic } /* Generic.Emph */
body .gr { color: #FF0000 } /* Generic.Error */
body .gh { color: #000080; font-weight: bold } /* Generic.Heading */
body .gi { color: #00A000 } /* Generic.Inserted */
body .go { color: #888888 } /* Generic.Output */
body .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
body .gs { font-weight: bold } /* Generic.Strong */
body .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
body .gt { color: #0044DD } /* Generic.Traceback */
body .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
body .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
body .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
body .kp { color: #008000 } /* Keyword.Pseudo */
body .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
body .kt { color: #B00040 } /* Keyword.Type */
body .m { color: #666666 } /* Literal.Number */
body .s { color: #BA2121 } /* Literal.String */
body .na { color: #7D9029 } /* Name.Attribute */
body .nb { color: #008000 } /* Name.Builtin */
body .nc { color: #0000FF; font-weight: bold } /* Name.Class */
body .no { color: #880000 } /* Name.Constant */
body .nd { color: #AA22FF } /* Name.Decorator */
body .ni { color: #999999; font-weight: bold } /* Name.Entity */
body .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
body .nf { color: #0000FF } /* Name.Function */
body .nl { color: #A0A000 } /* Name.Label */
body .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
body .nt { color: #008000; font-weight: bold } /* Name.Tag */
body .nv { color: #19177C } /* Name.Variable */
body .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
body .w { color: #bbbbbb } /* Text.Whitespace */
body .mb { color: #666666 } /* Literal.Number.Bin */
body .mf { color: #666666 } /* Literal.Number.Float */
body .mh { color: #666666 } /* Literal.Number.Hex */
body .mi { color: #666666 } /* Literal.Number.Integer */
body .mo { color: #666666 } /* Literal.Number.Oct */
body .sb { color: #BA2121 } /* Literal.String.Backtick */
body .sc { color: #BA2121 } /* Literal.String.Char */
body .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
body .s2 { color: #BA2121 } /* Literal.String.Double */
body .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
body .sh { color: #BA2121 } /* Literal.String.Heredoc */
body .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
body .sx { color: #008000 } /* Literal.String.Other */
body .sr { color: #BB6688 } /* Literal.String.Regex */
body .s1 { color: #BA2121 } /* Literal.String.Single */
body .ss { color: #19177C } /* Literal.String.Symbol */
body .bp { color: #008000 } /* Name.Builtin.Pseudo */
body .vc { color: #19177C } /* Name.Variable.Class */
body .vg { color: #19177C } /* Name.Variable.Global */
body .vi { color: #19177C } /* Name.Variable.Instance */
body .il { color: #666666 } /* Literal.Number.Integer.Long */

  </style>
</head>
<body>
<h2></h2>

<div class="highlight"><pre><span class="c"># util.py</span>
<span class="c"># -------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">inspect</span>
<span class="kn">import</span> <span class="nn">heapq</span><span class="o">,</span> <span class="nn">random</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd"> Data structures useful for implementing SearchAgents</span>
<span class="sd">&quot;&quot;&quot;</span>

<span class="k">class</span> <span class="nc">Stack</span><span class="p">:</span>
    <span class="s">&quot;A container with a last-in-first-out (LIFO) queuing policy.&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">push</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">item</span><span class="p">):</span>
        <span class="s">&quot;Push &#39;item&#39; onto the stack&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">pop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="s">&quot;Pop the most recently pushed item from the stack&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">isEmpty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="s">&quot;Returns true if the stack is empty&quot;</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span>

<span class="k">class</span> <span class="nc">Queue</span><span class="p">:</span>
    <span class="s">&quot;A container with a first-in-first-out (FIFO) queuing policy.&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">push</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">item</span><span class="p">):</span>
        <span class="s">&quot;Enqueue the &#39;item&#39; into the queue&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">item</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">pop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">          Dequeue the earliest enqueued item still in the queue. This</span>
<span class="sd">          operation removes the item from the queue.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">isEmpty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="s">&quot;Returns true if the queue is empty&quot;</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span>

<span class="k">class</span> <span class="nc">PriorityQueue</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">      Implements a priority queue data structure. Each inserted item</span>
<span class="sd">      has a priority associated with it and the client is usually interested</span>
<span class="sd">      in quick retrieval of the lowest-priority item in the queue. This</span>
<span class="sd">      data structure allows O(1) access to the lowest-priority item.</span>

<span class="sd">      Note that this PriorityQueue does not allow you to change the priority</span>
<span class="sd">      of an item.  However, you may insert the same item multiple times with</span>
<span class="sd">      different priorities.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span>  <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">heap</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">push</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">,</span> <span class="n">priority</span><span class="p">):</span>
        <span class="n">pair</span> <span class="o">=</span> <span class="p">(</span><span class="n">priority</span><span class="p">,</span><span class="n">item</span><span class="p">)</span>
        <span class="n">heapq</span><span class="o">.</span><span class="n">heappush</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">heap</span><span class="p">,</span><span class="n">pair</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">pop</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="p">(</span><span class="n">priority</span><span class="p">,</span><span class="n">item</span><span class="p">)</span> <span class="o">=</span> <span class="n">heapq</span><span class="o">.</span><span class="n">heappop</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">heap</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">item</span>

    <span class="k">def</span> <span class="nf">isEmpty</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">heap</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span>

<span class="k">class</span> <span class="nc">PriorityQueueWithFunction</span><span class="p">(</span><span class="n">PriorityQueue</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Implements a priority queue with the same push/pop signature of the</span>
<span class="sd">    Queue and the Stack classes. This is designed for drop-in replacement for</span>
<span class="sd">    those two classes. The caller has to provide a priority function, which</span>
<span class="sd">    extracts each item&#39;s priority.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span>  <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">priorityFunction</span><span class="p">):</span>
        <span class="s">&quot;priorityFunction (item) -&gt; priority&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">priorityFunction</span> <span class="o">=</span> <span class="n">priorityFunction</span>      <span class="c"># store the priority function</span>
        <span class="n">PriorityQueue</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>        <span class="c"># super-class initializer</span>

    <span class="k">def</span> <span class="nf">push</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">):</span>
        <span class="s">&quot;Adds an item to the queue with priority from the priority function&quot;</span>
        <span class="n">PriorityQueue</span><span class="o">.</span><span class="n">push</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">priorityFunction</span><span class="p">(</span><span class="n">item</span><span class="p">))</span>


<span class="k">def</span> <span class="nf">manhattanDistance</span><span class="p">(</span> <span class="n">xy1</span><span class="p">,</span> <span class="n">xy2</span> <span class="p">):</span>
    <span class="s">&quot;Returns the Manhattan distance between points xy1 and xy2&quot;</span>
    <span class="k">return</span> <span class="nb">abs</span><span class="p">(</span> <span class="n">xy1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">xy2</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">)</span> <span class="o">+</span> <span class="nb">abs</span><span class="p">(</span> <span class="n">xy1</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">xy2</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="p">)</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">  Data structures and functions useful for various course projects</span>

<span class="sd">  The search project should not need anything below this line.</span>
<span class="sd">&quot;&quot;&quot;</span>

<span class="k">class</span> <span class="nc">Counter</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A counter keeps track of counts for a set of keys.</span>

<span class="sd">    The counter class is an extension of the standard python</span>
<span class="sd">    dictionary type.  It is specialized to have number values</span>
<span class="sd">    (integers or floats), and includes a handful of additional</span>
<span class="sd">    functions to ease the task of counting data.  In particular,</span>
<span class="sd">    all keys are defaulted to have value 0.  Using a dictionary:</span>

<span class="sd">    a = {}</span>
<span class="sd">    print a[&#39;test&#39;]</span>

<span class="sd">    would give an error, while the Counter class analogue:</span>

<span class="sd">    &gt;&gt;&gt; a = Counter()</span>
<span class="sd">    &gt;&gt;&gt; print a[&#39;test&#39;]</span>
<span class="sd">    0</span>

<span class="sd">    returns the default 0 value. Note that to reference a key</span>
<span class="sd">    that you know is contained in the counter,</span>
<span class="sd">    you can still use the dictionary syntax:</span>

<span class="sd">    &gt;&gt;&gt; a = Counter()</span>
<span class="sd">    &gt;&gt;&gt; a[&#39;test&#39;] = 2</span>
<span class="sd">    &gt;&gt;&gt; print a[&#39;test&#39;]</span>
<span class="sd">    2</span>

<span class="sd">    This is very useful for counting things without initializing their counts,</span>
<span class="sd">    see for example:</span>

<span class="sd">    &gt;&gt;&gt; a[&#39;blah&#39;] += 1</span>
<span class="sd">    &gt;&gt;&gt; print a[&#39;blah&#39;]</span>
<span class="sd">    1</span>

<span class="sd">    The counter also includes additional functionality useful in implementing</span>
<span class="sd">    the classifiers for this assignment.  Two counters can be added,</span>
<span class="sd">    subtracted or multiplied together.  See below for details.  They can</span>
<span class="sd">    also be normalized and their total count and arg max can be extracted.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">idx</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">idx</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">dict</span><span class="o">.</span><span class="n">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">idx</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">incrementAll</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">keys</span><span class="p">,</span> <span class="n">count</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Increments all elements of keys by the same count.</span>

<span class="sd">        &gt;&gt;&gt; a = Counter()</span>
<span class="sd">        &gt;&gt;&gt; a.incrementAll([&#39;one&#39;,&#39;two&#39;, &#39;three&#39;], 1)</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;one&#39;]</span>
<span class="sd">        1</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;two&#39;]</span>
<span class="sd">        1</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">keys</span><span class="p">:</span>
            <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">+=</span> <span class="n">count</span>

    <span class="k">def</span> <span class="nf">argMax</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the key with the highest value.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
        <span class="nb">all</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="n">values</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">all</span><span class="p">]</span>
        <span class="n">maxIndex</span> <span class="o">=</span> <span class="n">values</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">values</span><span class="p">))</span>
        <span class="k">return</span> <span class="nb">all</span><span class="p">[</span><span class="n">maxIndex</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">sortedKeys</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns a list of keys sorted by their values.  Keys</span>
<span class="sd">        with the highest values will appear first.</span>

<span class="sd">        &gt;&gt;&gt; a = Counter()</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;first&#39;] = -2</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;second&#39;] = 4</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;third&#39;] = 1</span>
<span class="sd">        &gt;&gt;&gt; a.sortedKeys()</span>
<span class="sd">        [&#39;second&#39;, &#39;third&#39;, &#39;first&#39;]</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">sortedItems</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="n">compare</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">:</span>  <span class="n">sign</span><span class="p">(</span><span class="n">y</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
        <span class="n">sortedItems</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="nb">cmp</span><span class="o">=</span><span class="n">compare</span><span class="p">)</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">sortedItems</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">totalCount</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the sum of counts for all keys.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>

    <span class="k">def</span> <span class="nf">normalize</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Edits the counter such that the total count of all</span>
<span class="sd">        keys sums to 1.  The ratio of counts for all keys</span>
<span class="sd">        will remain the same. Note that normalizing an empty</span>
<span class="sd">        Counter will result in an error.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">total</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">totalCount</span><span class="p">())</span>
        <span class="k">if</span> <span class="n">total</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
            <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">/</span> <span class="n">total</span>

    <span class="k">def</span> <span class="nf">divideAll</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">divisor</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Divides all counts by divisor</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">divisor</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">divisor</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
            <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">/=</span> <span class="n">divisor</span>

    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns a copy of the counter</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="n">Counter</span><span class="p">(</span><span class="nb">dict</span><span class="o">.</span><span class="n">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">__mul__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">y</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Multiplying two counters gives the dot product of their vectors where</span>
<span class="sd">        each unique label is a vector element.</span>

<span class="sd">        &gt;&gt;&gt; a = Counter()</span>
<span class="sd">        &gt;&gt;&gt; b = Counter()</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;first&#39;] = -2</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;second&#39;] = 4</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;first&#39;] = 3</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;second&#39;] = 5</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;third&#39;] = 1.5</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;fourth&#39;] = 2.5</span>
<span class="sd">        &gt;&gt;&gt; a * b</span>
<span class="sd">        14</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="nb">sum</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">x</span> <span class="o">=</span> <span class="bp">self</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="o">&gt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">y</span><span class="p">):</span>
            <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="n">y</span><span class="p">,</span><span class="n">x</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">x</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">y</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="nb">sum</span> <span class="o">+=</span> <span class="n">x</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">*</span> <span class="n">y</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        <span class="k">return</span> <span class="nb">sum</span>

    <span class="k">def</span> <span class="nf">__radd__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Adding another counter to a counter increments the current counter</span>
<span class="sd">        by the values stored in the second counter.</span>

<span class="sd">        &gt;&gt;&gt; a = Counter()</span>
<span class="sd">        &gt;&gt;&gt; b = Counter()</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;first&#39;] = -2</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;second&#39;] = 4</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;first&#39;] = 3</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;third&#39;] = 1</span>
<span class="sd">        &gt;&gt;&gt; a += b</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;first&#39;]</span>
<span class="sd">        1</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">y</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
            <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">+=</span> <span class="n">value</span>

    <span class="k">def</span> <span class="nf">__add__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">y</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Adding two counters gives a counter with the union of all keys and</span>
<span class="sd">        counts of the second added to counts of the first.</span>

<span class="sd">        &gt;&gt;&gt; a = Counter()</span>
<span class="sd">        &gt;&gt;&gt; b = Counter()</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;first&#39;] = -2</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;second&#39;] = 4</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;first&#39;] = 3</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;third&#39;] = 1</span>
<span class="sd">        &gt;&gt;&gt; (a + b)[&#39;first&#39;]</span>
<span class="sd">        1</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">addend</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">y</span><span class="p">:</span>
                <span class="n">addend</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">+</span> <span class="n">y</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">addend</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">y</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">addend</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">y</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">addend</span>

    <span class="k">def</span> <span class="nf">__sub__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">y</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Subtracting a counter from another gives a counter with the union of all keys and</span>
<span class="sd">        counts of the second subtracted from counts of the first.</span>

<span class="sd">        &gt;&gt;&gt; a = Counter()</span>
<span class="sd">        &gt;&gt;&gt; b = Counter()</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;first&#39;] = -2</span>
<span class="sd">        &gt;&gt;&gt; a[&#39;second&#39;] = 4</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;first&#39;] = 3</span>
<span class="sd">        &gt;&gt;&gt; b[&#39;third&#39;] = 1</span>
<span class="sd">        &gt;&gt;&gt; (a - b)[&#39;first&#39;]</span>
<span class="sd">        -5</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">addend</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">y</span><span class="p">:</span>
                <span class="n">addend</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">-</span> <span class="n">y</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">addend</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">y</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="n">addend</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span> <span class="o">*</span> <span class="n">y</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">addend</span>

<span class="k">def</span> <span class="nf">raiseNotDefined</span><span class="p">():</span>
    <span class="k">print</span> <span class="s">&quot;Method not implemented: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">inspect</span><span class="o">.</span><span class="n">stack</span><span class="p">()[</span><span class="mi">1</span><span class="p">][</span><span class="mi">3</span><span class="p">]</span>
    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">normalize</span><span class="p">(</span><span class="n">vectorOrCounter</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    normalize a vector or counter by dividing each value by the sum of all values</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">normalizedCounter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span>
    <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">vectorOrCounter</span><span class="p">)</span> <span class="o">==</span> <span class="nb">type</span><span class="p">(</span><span class="n">normalizedCounter</span><span class="p">):</span>
        <span class="n">counter</span> <span class="o">=</span> <span class="n">vectorOrCounter</span>
        <span class="n">total</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="n">counter</span><span class="o">.</span><span class="n">totalCount</span><span class="p">())</span>
        <span class="k">if</span> <span class="n">total</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="n">counter</span>
        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">counter</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
            <span class="n">value</span> <span class="o">=</span> <span class="n">counter</span><span class="p">[</span><span class="n">key</span><span class="p">]</span>
            <span class="n">normalizedCounter</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span> <span class="o">/</span> <span class="n">total</span>
        <span class="k">return</span> <span class="n">normalizedCounter</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">vector</span> <span class="o">=</span> <span class="n">vectorOrCounter</span>
        <span class="n">s</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="nb">sum</span><span class="p">(</span><span class="n">vector</span><span class="p">))</span>
        <span class="k">if</span> <span class="n">s</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="n">vector</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">el</span> <span class="o">/</span> <span class="n">s</span> <span class="k">for</span> <span class="n">el</span> <span class="ow">in</span> <span class="n">vector</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">nSample</span><span class="p">(</span><span class="n">distribution</span><span class="p">,</span> <span class="n">values</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
    <span class="k">if</span> <span class="nb">sum</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">distribution</span> <span class="o">=</span> <span class="n">normalize</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span>
    <span class="n">rand</span> <span class="o">=</span> <span class="p">[</span><span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n</span><span class="p">)]</span>
    <span class="n">rand</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
    <span class="n">samples</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">samplePos</span><span class="p">,</span> <span class="n">distPos</span><span class="p">,</span> <span class="n">cdf</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span> <span class="n">distribution</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">while</span> <span class="n">samplePos</span> <span class="o">&lt;</span> <span class="n">n</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">rand</span><span class="p">[</span><span class="n">samplePos</span><span class="p">]</span> <span class="o">&lt;</span> <span class="n">cdf</span><span class="p">:</span>
            <span class="n">samplePos</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">samples</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">values</span><span class="p">[</span><span class="n">distPos</span><span class="p">])</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">distPos</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="n">cdf</span> <span class="o">+=</span> <span class="n">distribution</span><span class="p">[</span><span class="n">distPos</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">samples</span>

<span class="k">def</span> <span class="nf">sample</span><span class="p">(</span><span class="n">distribution</span><span class="p">,</span> <span class="n">values</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
    <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span> <span class="o">==</span> <span class="n">Counter</span><span class="p">:</span>
        <span class="n">items</span> <span class="o">=</span> <span class="n">distribution</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
        <span class="n">distribution</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">items</span><span class="p">]</span>
        <span class="n">values</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">items</span><span class="p">]</span>
    <span class="k">if</span> <span class="nb">sum</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">distribution</span> <span class="o">=</span> <span class="n">normalize</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span>
    <span class="n">choice</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span>
    <span class="n">i</span><span class="p">,</span> <span class="n">total</span><span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">distribution</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
    <span class="k">while</span> <span class="n">choice</span> <span class="o">&gt;</span> <span class="n">total</span><span class="p">:</span>
        <span class="n">i</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">total</span> <span class="o">+=</span> <span class="n">distribution</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">values</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">sampleFromCounter</span><span class="p">(</span><span class="n">ctr</span><span class="p">):</span>
    <span class="n">items</span> <span class="o">=</span> <span class="n">ctr</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">sample</span><span class="p">([</span><span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="ow">in</span> <span class="n">items</span><span class="p">],</span> <span class="p">[</span><span class="n">k</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="ow">in</span> <span class="n">items</span><span class="p">])</span>

<span class="k">def</span> <span class="nf">getProbability</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">distribution</span><span class="p">,</span> <span class="n">values</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">      Gives the probability of a value under a discrete distribution</span>
<span class="sd">      defined by (distributions, values).</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">total</span> <span class="o">=</span> <span class="mf">0.0</span>
    <span class="k">for</span> <span class="n">prob</span><span class="p">,</span> <span class="n">val</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">distribution</span><span class="p">,</span> <span class="n">values</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">val</span> <span class="o">==</span> <span class="n">value</span><span class="p">:</span>
            <span class="n">total</span> <span class="o">+=</span> <span class="n">prob</span>
    <span class="k">return</span> <span class="n">total</span>

<span class="k">def</span> <span class="nf">flipCoin</span><span class="p">(</span> <span class="n">p</span> <span class="p">):</span>
    <span class="n">r</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">r</span> <span class="o">&lt;</span> <span class="n">p</span>

<span class="k">def</span> <span class="nf">chooseFromDistribution</span><span class="p">(</span> <span class="n">distribution</span> <span class="p">):</span>
    <span class="s">&quot;Takes either a counter or a list of (prob, key) pairs and samples&quot;</span>
    <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span> <span class="o">==</span> <span class="nb">dict</span> <span class="ow">or</span> <span class="nb">type</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span> <span class="o">==</span> <span class="n">Counter</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">sample</span><span class="p">(</span><span class="n">distribution</span><span class="p">)</span>
    <span class="n">r</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">random</span><span class="p">()</span>
    <span class="n">base</span> <span class="o">=</span> <span class="mf">0.0</span>
    <span class="k">for</span> <span class="n">prob</span><span class="p">,</span> <span class="n">element</span> <span class="ow">in</span> <span class="n">distribution</span><span class="p">:</span>
        <span class="n">base</span> <span class="o">+=</span> <span class="n">prob</span>
        <span class="k">if</span> <span class="n">r</span> <span class="o">&lt;=</span> <span class="n">base</span><span class="p">:</span> <span class="k">return</span> <span class="n">element</span>

<span class="k">def</span> <span class="nf">nearestPoint</span><span class="p">(</span> <span class="n">pos</span> <span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Finds the nearest grid point to a position (discretizes).</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="p">(</span> <span class="n">current_row</span><span class="p">,</span> <span class="n">current_col</span> <span class="p">)</span> <span class="o">=</span> <span class="n">pos</span>

    <span class="n">grid_row</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span> <span class="n">current_row</span> <span class="o">+</span> <span class="mf">0.5</span> <span class="p">)</span>
    <span class="n">grid_col</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span> <span class="n">current_col</span> <span class="o">+</span> <span class="mf">0.5</span> <span class="p">)</span>
    <span class="k">return</span> <span class="p">(</span> <span class="n">grid_row</span><span class="p">,</span> <span class="n">grid_col</span> <span class="p">)</span>

<span class="k">def</span> <span class="nf">sign</span><span class="p">(</span> <span class="n">x</span> <span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Returns 1 or -1 depending on the sign of x</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">if</span><span class="p">(</span> <span class="n">x</span> <span class="o">&gt;=</span> <span class="mi">0</span> <span class="p">):</span>
        <span class="k">return</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="o">-</span><span class="mi">1</span>

<span class="k">def</span> <span class="nf">arrayInvert</span><span class="p">(</span><span class="n">array</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Inverts a matrix stored as a list of lists.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">result</span> <span class="o">=</span> <span class="p">[[]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">array</span><span class="p">]</span>
    <span class="k">for</span> <span class="n">outer</span> <span class="ow">in</span> <span class="n">array</span><span class="p">:</span>
        <span class="k">for</span> <span class="n">inner</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">outer</span><span class="p">)):</span>
            <span class="n">result</span><span class="p">[</span><span class="n">inner</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">outer</span><span class="p">[</span><span class="n">inner</span><span class="p">])</span>
    <span class="k">return</span> <span class="n">result</span>

<span class="k">def</span> <span class="nf">matrixAsList</span><span class="p">(</span> <span class="n">matrix</span><span class="p">,</span> <span class="n">value</span> <span class="o">=</span> <span class="bp">True</span> <span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Turns a matrix into a list of coordinates matching the specified value</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">rows</span><span class="p">,</span> <span class="n">cols</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span> <span class="n">matrix</span> <span class="p">),</span> <span class="nb">len</span><span class="p">(</span> <span class="n">matrix</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">)</span>
    <span class="n">cells</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span> <span class="n">rows</span> <span class="p">):</span>
        <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span> <span class="n">cols</span> <span class="p">):</span>
            <span class="k">if</span> <span class="n">matrix</span><span class="p">[</span><span class="n">row</span><span class="p">][</span><span class="n">col</span><span class="p">]</span> <span class="o">==</span> <span class="n">value</span><span class="p">:</span>
                <span class="n">cells</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span> <span class="n">row</span><span class="p">,</span> <span class="n">col</span> <span class="p">)</span> <span class="p">)</span>
    <span class="k">return</span> <span class="n">cells</span>

<span class="k">def</span> <span class="nf">lookup</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">namespace</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Get a method or class from any imported module from its name.</span>
<span class="sd">    Usage: lookup(functionName, globals())</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">dots</span> <span class="o">=</span> <span class="n">name</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">dots</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">moduleName</span><span class="p">,</span> <span class="n">objName</span> <span class="o">=</span> <span class="s">&#39;.&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]),</span> <span class="n">name</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
        <span class="n">module</span> <span class="o">=</span> <span class="nb">__import__</span><span class="p">(</span><span class="n">moduleName</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">objName</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">modules</span> <span class="o">=</span> <span class="p">[</span><span class="n">obj</span> <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">namespace</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">if</span> <span class="nb">str</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">obj</span><span class="p">))</span> <span class="o">==</span> <span class="s">&quot;&lt;type &#39;module&#39;&gt;&quot;</span><span class="p">]</span>
        <span class="n">options</span> <span class="o">=</span> <span class="p">[</span><span class="nb">getattr</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span> <span class="k">for</span> <span class="n">module</span> <span class="ow">in</span> <span class="n">modules</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">module</span><span class="p">)]</span>
        <span class="n">options</span> <span class="o">+=</span> <span class="p">[</span><span class="n">obj</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">namespace</span><span class="o">.</span><span class="n">items</span><span class="p">()</span> <span class="k">if</span> <span class="n">obj</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">name</span> <span class="p">]</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">options</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span> <span class="k">return</span> <span class="n">options</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">options</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span> <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;Name conflict for </span><span class="si">%s</span><span class="s">&#39;</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;</span><span class="si">%s</span><span class="s"> not found as a method or class&#39;</span> <span class="o">%</span> <span class="n">name</span>

<span class="k">def</span> <span class="nf">pause</span><span class="p">():</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Pauses the output stream awaiting user feedback.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">print</span> <span class="s">&quot;&lt;Press enter/return to continue&gt;&quot;</span>
    <span class="nb">raw_input</span><span class="p">()</span>


<span class="c">## code to handle timeouts</span>
<span class="kn">import</span> <span class="nn">signal</span>
<span class="k">class</span> <span class="nc">TimeoutFunctionException</span><span class="p">(</span><span class="ne">Exception</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Exception to raise on a timeout&quot;&quot;&quot;</span>
    <span class="k">pass</span>

<span class="k">class</span> <span class="nc">TimeoutFunction</span><span class="p">:</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">function</span><span class="p">,</span> <span class="n">timeout</span><span class="p">):</span>
        <span class="s">&quot;timeout must be at least 1 second. WHY??&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span> <span class="o">=</span> <span class="n">timeout</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">function</span> <span class="o">=</span> <span class="n">function</span>

    <span class="k">def</span> <span class="nf">handle_timeout</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">signum</span><span class="p">,</span> <span class="n">frame</span><span class="p">):</span>
        <span class="k">raise</span> <span class="n">TimeoutFunctionException</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="s">&#39;SIGALRM&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">signal</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="n">old</span> <span class="o">=</span> <span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGALRM</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">handle_timeout</span><span class="p">)</span>
        <span class="n">signal</span><span class="o">.</span><span class="n">alarm</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">function</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGALRM</span><span class="p">,</span> <span class="n">old</span><span class="p">)</span>
        <span class="n">signal</span><span class="o">.</span><span class="n">alarm</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span>
</pre></div>
</body>
</html>
