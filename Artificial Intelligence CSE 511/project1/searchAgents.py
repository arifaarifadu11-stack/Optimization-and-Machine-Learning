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

<div class="highlight"><pre><span class="c"># searchAgents.py</span>
<span class="c"># ---------------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">This file contains all of the agents that can be selected to</span>
<span class="sd">control Pacman.  To select an agent, use the &#39;-p&#39; option</span>
<span class="sd">when running pacman.py.  Arguments can be passed to your agent</span>
<span class="sd">using &#39;-a&#39;.  For example, to load a SearchAgent that uses</span>
<span class="sd">depth first search (dfs), run the following command:</span>

<span class="sd">&gt; python pacman.py -p SearchAgent -a searchFunction=depthFirstSearch</span>

<span class="sd">Commands to invoke other search strategies can be found in the</span>
<span class="sd">project description.</span>

<span class="sd">Please only change the parts of the file you are asked to.</span>
<span class="sd">Look for the lines that say</span>

<span class="sd">&quot;*** YOUR CODE HERE ***&quot;</span>

<span class="sd">The parts you fill in start about 3/4 of the way down.  Follow the</span>
<span class="sd">project description for details.</span>

<span class="sd">Good luck and happy searching!</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Directions</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Actions</span>
<span class="kn">import</span> <span class="nn">util</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="kn">import</span> <span class="nn">search</span>

<span class="k">class</span> <span class="nc">GoWestAgent</span><span class="p">(</span><span class="n">Agent</span><span class="p">):</span>
    <span class="s">&quot;An agent that goes West until it can&#39;t.&quot;</span>

    <span class="k">def</span> <span class="nf">getAction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="s">&quot;The agent receives a GameState (defined in pacman.py).&quot;</span>
        <span class="k">if</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span> <span class="ow">in</span> <span class="n">state</span><span class="o">.</span><span class="n">getLegalPacmanActions</span><span class="p">():</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span>

<span class="c">#######################################################</span>
<span class="c"># This portion is written for you, but will only work #</span>
<span class="c">#       after you fill in parts of search.py          #</span>
<span class="c">#######################################################</span>

<span class="k">class</span> <span class="nc">SearchAgent</span><span class="p">(</span><span class="n">Agent</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    This very general search agent finds a path using a supplied search algorithm for a</span>
<span class="sd">    supplied search problem, then returns actions to follow that path.</span>

<span class="sd">    As a default, this agent runs DFS on a PositionSearchProblem to find location (1,1)</span>

<span class="sd">    Options for fn include:</span>
<span class="sd">      depthFirstSearch or dfs</span>
<span class="sd">      breadthFirstSearch or bfs</span>


<span class="sd">    Note: You should NOT change any code in SearchAgent</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fn</span><span class="o">=</span><span class="s">&#39;depthFirstSearch&#39;</span><span class="p">,</span> <span class="n">prob</span><span class="o">=</span><span class="s">&#39;PositionSearchProblem&#39;</span><span class="p">,</span> <span class="n">heuristic</span><span class="o">=</span><span class="s">&#39;nullHeuristic&#39;</span><span class="p">):</span>
        <span class="c"># Warning: some advanced Python magic is employed below to find the right functions and problems</span>

        <span class="c"># Get the search function from the name and heuristic</span>
        <span class="k">if</span> <span class="n">fn</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">search</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">,</span> <span class="n">fn</span> <span class="o">+</span> <span class="s">&#39; is not a search function in search.py.&#39;</span>
        <span class="n">func</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">search</span><span class="p">,</span> <span class="n">fn</span><span class="p">)</span>
        <span class="k">if</span> <span class="s">&#39;heuristic&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">func</span><span class="o">.</span><span class="n">func_code</span><span class="o">.</span><span class="n">co_varnames</span><span class="p">:</span>
            <span class="k">print</span><span class="p">(</span><span class="s">&#39;[SearchAgent] using function &#39;</span> <span class="o">+</span> <span class="n">fn</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">=</span> <span class="n">func</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">heuristic</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">()</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span>
                <span class="n">heur</span> <span class="o">=</span> <span class="nb">globals</span><span class="p">()[</span><span class="n">heuristic</span><span class="p">]</span>
            <span class="k">elif</span> <span class="n">heuristic</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">search</span><span class="p">):</span>
                <span class="n">heur</span> <span class="o">=</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">search</span><span class="p">,</span> <span class="n">heuristic</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">,</span> <span class="n">heuristic</span> <span class="o">+</span> <span class="s">&#39; is not a function in searchAgents.py or search.py.&#39;</span>
            <span class="k">print</span><span class="p">(</span><span class="s">&#39;[SearchAgent] using function </span><span class="si">%s</span><span class="s"> and heuristic </span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">fn</span><span class="p">,</span> <span class="n">heuristic</span><span class="p">))</span>
            <span class="c"># Note: this bit of Python trickery combines the search algorithm and the heuristic</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="n">func</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">heuristic</span><span class="o">=</span><span class="n">heur</span><span class="p">)</span>

        <span class="c"># Get the search problem type from the name</span>
        <span class="k">if</span> <span class="n">prob</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">()</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">prob</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;Problem&#39;</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">,</span> <span class="n">prob</span> <span class="o">+</span> <span class="s">&#39; is not a search problem type in SearchAgents.py.&#39;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchType</span> <span class="o">=</span> <span class="nb">globals</span><span class="p">()[</span><span class="n">prob</span><span class="p">]</span>
        <span class="k">print</span><span class="p">(</span><span class="s">&#39;[SearchAgent] using problem type &#39;</span> <span class="o">+</span> <span class="n">prob</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">registerInitialState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        This is the first time that the agent sees the layout of the game board. Here, we</span>
<span class="sd">        choose a path to the goal.  In this phase, the agent should compute the path to the</span>
<span class="sd">        goal and store it in a local variable.  All of the work is done in this method!</span>

<span class="sd">        state: a GameState object (pacman.py)</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&quot;No search function provided for SearchAgent&quot;</span>
        <span class="n">starttime</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
        <span class="n">problem</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">searchType</span><span class="p">(</span><span class="n">state</span><span class="p">)</span> <span class="c"># Makes a new search problem</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">actions</span>  <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span><span class="p">(</span><span class="n">problem</span><span class="p">)</span> <span class="c"># Find a path</span>
        <span class="n">totalCost</span> <span class="o">=</span> <span class="n">problem</span><span class="o">.</span><span class="n">getCostOfActions</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">actions</span><span class="p">)</span>
        <span class="k">print</span><span class="p">(</span><span class="s">&#39;Path found with total cost of </span><span class="si">%d</span><span class="s"> in </span><span class="si">%.1f</span><span class="s"> seconds&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">totalCost</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">starttime</span><span class="p">))</span>
        <span class="k">if</span> <span class="s">&#39;_expanded&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span> <span class="k">print</span><span class="p">(</span><span class="s">&#39;Search nodes expanded: </span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">problem</span><span class="o">.</span><span class="n">_expanded</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getAction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the next action in the path chosen earlier (in registerInitialState).  Return</span>
<span class="sd">        Directions.STOP if there is no further action to take.</span>

<span class="sd">        state: a GameState object (pacman.py)</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="s">&#39;actionIndex&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span> <span class="bp">self</span><span class="o">.</span><span class="n">actionIndex</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">i</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">actionIndex</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">actionIndex</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">actions</span><span class="p">):</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">actions</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span>

<span class="k">class</span> <span class="nc">PositionSearchProblem</span><span class="p">(</span><span class="n">search</span><span class="o">.</span><span class="n">SearchProblem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A search problem defines the state space, start state, goal test,</span>
<span class="sd">    successor function and cost function.  This search problem can be</span>
<span class="sd">    used to find paths to a particular point on the pacman board.</span>

<span class="sd">    The state space consists of (x,y) positions in a pacman game.</span>

<span class="sd">    Note: this search problem is fully specified; you should NOT change it.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">gameState</span><span class="p">,</span> <span class="n">costFn</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="n">goal</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="n">start</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">warn</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Stores the start and goal.</span>

<span class="sd">        gameState: A GameState object (pacman.py)</span>
<span class="sd">        costFn: A function from a search state (tuple) to a non-negative number</span>
<span class="sd">        goal: A position in the gameState</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getWalls</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">startState</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">start</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">startState</span> <span class="o">=</span> <span class="n">start</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">goal</span> <span class="o">=</span> <span class="n">goal</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">costFn</span> <span class="o">=</span> <span class="n">costFn</span>
        <span class="k">if</span> <span class="n">warn</span> <span class="ow">and</span> <span class="p">(</span><span class="n">gameState</span><span class="o">.</span><span class="n">getNumFood</span><span class="p">()</span> <span class="o">!=</span> <span class="mi">1</span> <span class="ow">or</span> <span class="ow">not</span> <span class="n">gameState</span><span class="o">.</span><span class="n">hasFood</span><span class="p">(</span><span class="o">*</span><span class="n">goal</span><span class="p">)):</span>
            <span class="k">print</span> <span class="s">&#39;Warning: this does not look like a regular search maze&#39;</span>

        <span class="c"># For display purposes</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_visited</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_visitedlist</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">=</span> <span class="p">{},</span> <span class="p">[],</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">getStartState</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">startState</span>

    <span class="k">def</span> <span class="nf">isGoalState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="n">isGoal</span> <span class="o">=</span> <span class="n">state</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">goal</span>

        <span class="c"># For display purposes only</span>
        <span class="k">if</span> <span class="n">isGoal</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_visitedlist</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
            <span class="kn">import</span> <span class="nn">__main__</span>
            <span class="k">if</span> <span class="s">&#39;_display&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">__main__</span><span class="p">):</span>
                <span class="k">if</span> <span class="s">&#39;drawExpandedCells&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">__main__</span><span class="o">.</span><span class="n">_display</span><span class="p">):</span> <span class="c">#@UndefinedVariable</span>
                    <span class="n">__main__</span><span class="o">.</span><span class="n">_display</span><span class="o">.</span><span class="n">drawExpandedCells</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_visitedlist</span><span class="p">)</span> <span class="c">#@UndefinedVariable</span>

        <span class="k">return</span> <span class="n">isGoal</span>

    <span class="k">def</span> <span class="nf">getSuccessors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns successor states, the actions they require, and a cost of 1.</span>

<span class="sd">         As noted in search.py:</span>
<span class="sd">             For a given state, this should return a list of triples,</span>
<span class="sd">         (successor, action, stepCost), where &#39;successor&#39; is a</span>
<span class="sd">         successor to the current state, &#39;action&#39; is the action</span>
<span class="sd">         required to get there, and &#39;stepCost&#39; is the incremental</span>
<span class="sd">         cost of expanding to that successor</span>
<span class="sd">        &quot;&quot;&quot;</span>

        <span class="n">successors</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="p">[</span><span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">]:</span>
            <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="n">state</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span><span class="n">action</span><span class="p">)</span>
            <span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="n">dy</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">nextx</span><span class="p">][</span><span class="n">nexty</span><span class="p">]:</span>
                <span class="n">nextState</span> <span class="o">=</span> <span class="p">(</span><span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span><span class="p">)</span>
                <span class="n">cost</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">costFn</span><span class="p">(</span><span class="n">nextState</span><span class="p">)</span>
                <span class="n">successors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span> <span class="n">nextState</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">cost</span><span class="p">)</span> <span class="p">)</span>

        <span class="c"># Bookkeeping for display purposes</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="n">state</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_visited</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_visited</span><span class="p">[</span><span class="n">state</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_visitedlist</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">successors</span>

    <span class="k">def</span> <span class="nf">getCostOfActions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the cost of a particular sequence of actions.  If those actions</span>
<span class="sd">        include an illegal move, return 999999</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="n">actions</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="mi">999999</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getStartState</span><span class="p">()</span>
        <span class="n">cost</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span>
            <span class="c"># Check figure out the next state and see whether its&#39; legal</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span><span class="n">action</span><span class="p">)</span>
            <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="n">dy</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]:</span> <span class="k">return</span> <span class="mi">999999</span>
            <span class="n">cost</span> <span class="o">+=</span> <span class="bp">self</span><span class="o">.</span><span class="n">costFn</span><span class="p">((</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">cost</span>

<span class="k">class</span> <span class="nc">StayEastSearchAgent</span><span class="p">(</span><span class="n">SearchAgent</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    An agent for position search with a cost function that penalizes being in</span>
<span class="sd">    positions on the West side of the board.</span>

<span class="sd">    The cost function for stepping into a position (x,y) is 1/2^x.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">=</span> <span class="n">search</span><span class="o">.</span><span class="n">uniformCostSearch</span>
        <span class="n">costFn</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">pos</span><span class="p">:</span> <span class="o">.</span><span class="mi">5</span> <span class="o">**</span> <span class="n">pos</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchType</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">state</span><span class="p">:</span> <span class="n">PositionSearchProblem</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">costFn</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">StayWestSearchAgent</span><span class="p">(</span><span class="n">SearchAgent</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    An agent for position search with a cost function that penalizes being in</span>
<span class="sd">    positions on the East side of the board.</span>

<span class="sd">    The cost function for stepping into a position (x,y) is 2^x.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">=</span> <span class="n">search</span><span class="o">.</span><span class="n">uniformCostSearch</span>
        <span class="n">costFn</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">pos</span><span class="p">:</span> <span class="mi">2</span> <span class="o">**</span> <span class="n">pos</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchType</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">state</span><span class="p">:</span> <span class="n">PositionSearchProblem</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">costFn</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">manhattanHeuristic</span><span class="p">(</span><span class="n">position</span><span class="p">,</span> <span class="n">problem</span><span class="p">,</span> <span class="n">info</span><span class="o">=</span><span class="p">{}):</span>
    <span class="s">&quot;The Manhattan distance heuristic for a PositionSearchProblem&quot;</span>
    <span class="n">xy1</span> <span class="o">=</span> <span class="n">position</span>
    <span class="n">xy2</span> <span class="o">=</span> <span class="n">problem</span><span class="o">.</span><span class="n">goal</span>
    <span class="k">return</span> <span class="nb">abs</span><span class="p">(</span><span class="n">xy1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">xy2</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">+</span> <span class="nb">abs</span><span class="p">(</span><span class="n">xy1</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">xy2</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>

<span class="k">def</span> <span class="nf">euclideanHeuristic</span><span class="p">(</span><span class="n">position</span><span class="p">,</span> <span class="n">problem</span><span class="p">,</span> <span class="n">info</span><span class="o">=</span><span class="p">{}):</span>
    <span class="s">&quot;The Euclidean distance heuristic for a PositionSearchProblem&quot;</span>
    <span class="n">xy1</span> <span class="o">=</span> <span class="n">position</span>
    <span class="n">xy2</span> <span class="o">=</span> <span class="n">problem</span><span class="o">.</span><span class="n">goal</span>
    <span class="k">return</span> <span class="p">(</span> <span class="p">(</span><span class="n">xy1</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">xy2</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span> <span class="o">**</span> <span class="mi">2</span> <span class="o">+</span> <span class="p">(</span><span class="n">xy1</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">xy2</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span> <span class="o">**</span> <span class="mi">2</span> <span class="p">)</span> <span class="o">**</span> <span class="mf">0.5</span>

<span class="c">#####################################################</span>
<span class="c"># This portion is incomplete.  Time to write code!  #</span>
<span class="c">#####################################################</span>

<span class="k">class</span> <span class="nc">CornersProblem</span><span class="p">(</span><span class="n">search</span><span class="o">.</span><span class="n">SearchProblem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    This search problem finds paths through all four corners of a layout.</span>

<span class="sd">    You must select a suitable state space and successor function</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingGameState</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Stores the walls, pacman&#39;s starting position and corners.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">startingGameState</span><span class="o">.</span><span class="n">getWalls</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">startingPosition</span> <span class="o">=</span> <span class="n">startingGameState</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">()</span>
        <span class="n">top</span><span class="p">,</span> <span class="n">right</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="o">.</span><span class="n">height</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="o">.</span><span class="n">width</span><span class="o">-</span><span class="mi">2</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">corners</span> <span class="o">=</span> <span class="p">((</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">top</span><span class="p">),</span> <span class="p">(</span><span class="n">right</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="n">right</span><span class="p">,</span> <span class="n">top</span><span class="p">))</span>
        <span class="k">for</span> <span class="n">corner</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">corners</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">startingGameState</span><span class="o">.</span><span class="n">hasFood</span><span class="p">(</span><span class="o">*</span><span class="n">corner</span><span class="p">):</span>
                <span class="k">print</span> <span class="s">&#39;Warning: no food in corner &#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">corner</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">=</span> <span class="mi">0</span> <span class="c"># Number of search nodes expanded</span>

        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>

    <span class="k">def</span> <span class="nf">getStartState</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="s">&quot;Returns the start state (in your state space, not the full Pacman state space)&quot;</span>
        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">isGoalState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="s">&quot;Returns whether this search state is a goal state of the problem&quot;</span>
        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getSuccessors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns successor states, the actions they require, and a cost of 1.</span>

<span class="sd">         As noted in search.py:</span>
<span class="sd">             For a given state, this should return a list of triples,</span>
<span class="sd">         (successor, action, stepCost), where &#39;successor&#39; is a</span>
<span class="sd">         successor to the current state, &#39;action&#39; is the action</span>
<span class="sd">         required to get there, and &#39;stepCost&#39; is the incremental</span>
<span class="sd">         cost of expanding to that successor</span>
<span class="sd">        &quot;&quot;&quot;</span>

        <span class="n">successors</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="p">[</span><span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">]:</span>
            <span class="c"># Add a successor state to the successor list if the action is legal</span>
            <span class="c"># Here&#39;s a code snippet for figuring out whether a new position hits a wall:</span>
            <span class="c">#   x,y = currentPosition</span>
            <span class="c">#   dx, dy = Actions.directionToVector(action)</span>
            <span class="c">#   nextx, nexty = int(x + dx), int(y + dy)</span>
            <span class="c">#   hitsWall = self.walls[nextx][nexty]</span>

            <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">successors</span>

    <span class="k">def</span> <span class="nf">getCostOfActions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the cost of a particular sequence of actions.  If those actions</span>
<span class="sd">        include an illegal move, return 999999.  This is implemented for you.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="n">actions</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="mi">999999</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">startingPosition</span>
        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span><span class="n">action</span><span class="p">)</span>
            <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="n">dy</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]:</span> <span class="k">return</span> <span class="mi">999999</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">actions</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">cornersHeuristic</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">problem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A heuristic for the CornersProblem that you defined.</span>

<span class="sd">      state:   The current search state</span>
<span class="sd">               (a data structure you chose in your search problem)</span>

<span class="sd">      problem: The CornersProblem instance for this layout.</span>

<span class="sd">    This function should always return a number that is a lower bound</span>
<span class="sd">    on the shortest path from the state to a goal of the problem; i.e.</span>
<span class="sd">    it should be admissible (as well as consistent).</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">corners</span> <span class="o">=</span> <span class="n">problem</span><span class="o">.</span><span class="n">corners</span> <span class="c"># These are the corner coordinates</span>
    <span class="n">walls</span> <span class="o">=</span> <span class="n">problem</span><span class="o">.</span><span class="n">walls</span> <span class="c"># These are the walls of the maze, as a Grid (game.py)</span>

    <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
    <span class="k">return</span> <span class="mi">0</span> <span class="c"># Default to trivial solution</span>

<span class="k">class</span> <span class="nc">AStarCornersAgent</span><span class="p">(</span><span class="n">SearchAgent</span><span class="p">):</span>
    <span class="s">&quot;A SearchAgent for FoodSearchProblem using A* and your foodHeuristic&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">prob</span><span class="p">:</span> <span class="n">search</span><span class="o">.</span><span class="n">aStarSearch</span><span class="p">(</span><span class="n">prob</span><span class="p">,</span> <span class="n">cornersHeuristic</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchType</span> <span class="o">=</span> <span class="n">CornersProblem</span>

<span class="k">class</span> <span class="nc">FoodSearchProblem</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A search problem associated with finding the a path that collects all of the</span>
<span class="sd">    food (dots) in a Pacman game.</span>

<span class="sd">    A search state in this problem is a tuple ( pacmanPosition, foodGrid ) where</span>
<span class="sd">      pacmanPosition: a tuple (x,y) of integers specifying Pacman&#39;s position</span>
<span class="sd">      foodGrid:       a Grid (see game.py) of either True or False, specifying remaining food</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">startingGameState</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">start</span> <span class="o">=</span> <span class="p">(</span><span class="n">startingGameState</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">(),</span> <span class="n">startingGameState</span><span class="o">.</span><span class="n">getFood</span><span class="p">())</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">startingGameState</span><span class="o">.</span><span class="n">getWalls</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">startingGameState</span> <span class="o">=</span> <span class="n">startingGameState</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">heuristicInfo</span> <span class="o">=</span> <span class="p">{}</span> <span class="c"># A dictionary for the heuristic to store information</span>

    <span class="k">def</span> <span class="nf">getStartState</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">start</span>

    <span class="k">def</span> <span class="nf">isGoalState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">state</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">()</span> <span class="o">==</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">getSuccessors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="s">&quot;Returns successor states, the actions they require, and a cost of 1.&quot;</span>
        <span class="n">successors</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">direction</span> <span class="ow">in</span> <span class="p">[</span><span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">]:</span>
            <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="n">state</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span><span class="n">direction</span><span class="p">)</span>
            <span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="n">dy</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">nextx</span><span class="p">][</span><span class="n">nexty</span><span class="p">]:</span>
                <span class="n">nextFood</span> <span class="o">=</span> <span class="n">state</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
                <span class="n">nextFood</span><span class="p">[</span><span class="n">nextx</span><span class="p">][</span><span class="n">nexty</span><span class="p">]</span> <span class="o">=</span> <span class="bp">False</span>
                <span class="n">successors</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span> <span class="p">((</span><span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span><span class="p">),</span> <span class="n">nextFood</span><span class="p">),</span> <span class="n">direction</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span> <span class="p">)</span>
        <span class="k">return</span> <span class="n">successors</span>

    <span class="k">def</span> <span class="nf">getCostOfActions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;Returns the cost of a particular sequence of actions.  If those actions</span>
<span class="sd">        include an illegal move, return 999999&quot;&quot;&quot;</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getStartState</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">cost</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span>
            <span class="c"># figure out the next state and see whether it&#39;s legal</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span><span class="n">action</span><span class="p">)</span>
            <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="n">dy</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]:</span>
                <span class="k">return</span> <span class="mi">999999</span>
            <span class="n">cost</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">return</span> <span class="n">cost</span>

<span class="k">class</span> <span class="nc">AStarFoodSearchAgent</span><span class="p">(</span><span class="n">SearchAgent</span><span class="p">):</span>
    <span class="s">&quot;A SearchAgent for FoodSearchProblem using A* and your foodHeuristic&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchFunction</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">prob</span><span class="p">:</span> <span class="n">search</span><span class="o">.</span><span class="n">aStarSearch</span><span class="p">(</span><span class="n">prob</span><span class="p">,</span> <span class="n">foodHeuristic</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">searchType</span> <span class="o">=</span> <span class="n">FoodSearchProblem</span>

<span class="k">def</span> <span class="nf">foodHeuristic</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">problem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Your heuristic for the FoodSearchProblem goes here.</span>

<span class="sd">    This heuristic must be consistent to ensure correctness.  First, try to come up</span>
<span class="sd">    with an admissible heuristic; almost all admissible heuristics will be consistent</span>
<span class="sd">    as well.</span>

<span class="sd">    If using A* ever finds a solution that is worse uniform cost search finds,</span>
<span class="sd">    your heuristic is *not* consistent, and probably not admissible!  On the other hand,</span>
<span class="sd">    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.</span>

<span class="sd">    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a</span>
<span class="sd">    Grid (see game.py) of either True or False. You can call foodGrid.asList()</span>
<span class="sd">    to get a list of food coordinates instead.</span>

<span class="sd">    If you want access to info like walls, capsules, etc., you can query the problem.</span>
<span class="sd">    For example, problem.walls gives you a Grid of where the walls are.</span>

<span class="sd">    If you want to *store* information to be reused in other calls to the heuristic,</span>
<span class="sd">    there is a dictionary called problem.heuristicInfo that you can use. For example,</span>
<span class="sd">    if you only want to count the walls once and store that value, try:</span>
<span class="sd">      problem.heuristicInfo[&#39;wallCount&#39;] = problem.walls.count()</span>
<span class="sd">    Subsequent calls to this heuristic can access problem.heuristicInfo[&#39;wallCount&#39;]</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">position</span><span class="p">,</span> <span class="n">foodGrid</span> <span class="o">=</span> <span class="n">state</span>
    <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
    <span class="k">return</span> <span class="mi">0</span>

<span class="k">class</span> <span class="nc">ClosestDotSearchAgent</span><span class="p">(</span><span class="n">SearchAgent</span><span class="p">):</span>
    <span class="s">&quot;Search for all food using a sequence of searches&quot;</span>
    <span class="k">def</span> <span class="nf">registerInitialState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">actions</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">currentState</span> <span class="o">=</span> <span class="n">state</span>
        <span class="k">while</span><span class="p">(</span><span class="n">currentState</span><span class="o">.</span><span class="n">getFood</span><span class="p">()</span><span class="o">.</span><span class="n">count</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">):</span>
            <span class="n">nextPathSegment</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">findPathToClosestDot</span><span class="p">(</span><span class="n">currentState</span><span class="p">)</span> <span class="c"># The missing piece</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">actions</span> <span class="o">+=</span> <span class="n">nextPathSegment</span>
            <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">nextPathSegment</span><span class="p">:</span>
                <span class="n">legal</span> <span class="o">=</span> <span class="n">currentState</span><span class="o">.</span><span class="n">getLegalActions</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">action</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">legal</span><span class="p">:</span>
                    <span class="n">t</span> <span class="o">=</span> <span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">action</span><span class="p">),</span> <span class="nb">str</span><span class="p">(</span><span class="n">currentState</span><span class="p">))</span>
                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;findPathToClosestDot returned an illegal move: </span><span class="si">%s</span><span class="s">!</span><span class="se">\n</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">t</span>
                <span class="n">currentState</span> <span class="o">=</span> <span class="n">currentState</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">action</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">actionIndex</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">print</span> <span class="s">&#39;Path found with cost </span><span class="si">%d</span><span class="s">.&#39;</span> <span class="o">%</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">actions</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">findPathToClosestDot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">gameState</span><span class="p">):</span>
        <span class="s">&quot;Returns a path (a list of actions) to the closest dot, starting from gameState&quot;</span>
        <span class="c"># Here are some useful elements of the startState</span>
        <span class="n">startPosition</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">()</span>
        <span class="n">food</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getFood</span><span class="p">()</span>
        <span class="n">walls</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getWalls</span><span class="p">()</span>
        <span class="n">problem</span> <span class="o">=</span> <span class="n">AnyFoodSearchProblem</span><span class="p">(</span><span class="n">gameState</span><span class="p">)</span>

        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">AnyFoodSearchProblem</span><span class="p">(</span><span class="n">PositionSearchProblem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">      A search problem for finding a path to any food.</span>

<span class="sd">      This search problem is just like the PositionSearchProblem, but</span>
<span class="sd">      has a different goal test, which you need to fill in below.  The</span>
<span class="sd">      state space and successor function do not need to be changed.</span>

<span class="sd">      The class definition above, AnyFoodSearchProblem(PositionSearchProblem),</span>
<span class="sd">      inherits the methods of the PositionSearchProblem.</span>

<span class="sd">      You can use this search problem to help you fill in</span>
<span class="sd">      the findPathToClosestDot method.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">gameState</span><span class="p">):</span>
        <span class="s">&quot;Stores information from the gameState.  You don&#39;t need to change this.&quot;</span>
        <span class="c"># Store the food for later reference</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getFood</span><span class="p">()</span>

        <span class="c"># Store info for the PositionSearchProblem (no need to change this)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getWalls</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">startState</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">costFn</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="mi">1</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_visited</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_visitedlist</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">_expanded</span> <span class="o">=</span> <span class="p">{},</span> <span class="p">[],</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">isGoalState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        The state is Pacman&#39;s position. Fill this in with a goal test</span>
<span class="sd">        that will complete the problem definition.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="n">state</span>

        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="c">##################</span>
<span class="c"># Mini-contest 1 #</span>
<span class="c">##################</span>

<span class="k">class</span> <span class="nc">ApproximateSearchAgent</span><span class="p">(</span><span class="n">Agent</span><span class="p">):</span>
    <span class="s">&quot;Implement your contest entry here.  Change anything but the class name.&quot;</span>

    <span class="k">def</span> <span class="nf">registerInitialState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="s">&quot;This method is called before any moves are made.&quot;</span>
        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>

    <span class="k">def</span> <span class="nf">getAction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        From game.py:</span>
<span class="sd">        The Agent will receive a GameState and must return an action from</span>
<span class="sd">        Directions.{North, South, East, West, Stop}</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">mazeDistance</span><span class="p">(</span><span class="n">point1</span><span class="p">,</span> <span class="n">point2</span><span class="p">,</span> <span class="n">gameState</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Returns the maze distance between any two points, using the search functions</span>
<span class="sd">    you have already built.  The gameState can be any game state -- Pacman&#39;s position</span>
<span class="sd">    in that state is ignored.</span>

<span class="sd">    Example usage: mazeDistance( (2,4), (5,6), gameState)</span>

<span class="sd">    This might be a useful helper function for your ApproximateSearchAgent.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">x1</span><span class="p">,</span> <span class="n">y1</span> <span class="o">=</span> <span class="n">point1</span>
    <span class="n">x2</span><span class="p">,</span> <span class="n">y2</span> <span class="o">=</span> <span class="n">point2</span>
    <span class="n">walls</span> <span class="o">=</span> <span class="n">gameState</span><span class="o">.</span><span class="n">getWalls</span><span class="p">()</span>
    <span class="k">assert</span> <span class="ow">not</span> <span class="n">walls</span><span class="p">[</span><span class="n">x1</span><span class="p">][</span><span class="n">y1</span><span class="p">],</span> <span class="s">&#39;point1 is a wall: &#39;</span> <span class="o">+</span> <span class="n">point1</span>
    <span class="k">assert</span> <span class="ow">not</span> <span class="n">walls</span><span class="p">[</span><span class="n">x2</span><span class="p">][</span><span class="n">y2</span><span class="p">],</span> <span class="s">&#39;point2 is a wall: &#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">point2</span><span class="p">)</span>
    <span class="n">prob</span> <span class="o">=</span> <span class="n">PositionSearchProblem</span><span class="p">(</span><span class="n">gameState</span><span class="p">,</span> <span class="n">start</span><span class="o">=</span><span class="n">point1</span><span class="p">,</span> <span class="n">goal</span><span class="o">=</span><span class="n">point2</span><span class="p">,</span> <span class="n">warn</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="n">search</span><span class="o">.</span><span class="n">bfs</span><span class="p">(</span><span class="n">prob</span><span class="p">))</span>
</pre></div>
</body>
</html>
