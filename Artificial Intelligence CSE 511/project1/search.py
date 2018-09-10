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

<div class="highlight"><pre><span class="c"># search.py</span>
<span class="c"># ---------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">In search.py, you will implement generic search algorithms which are called</span>
<span class="sd">by Pacman agents (in searchAgents.py).</span>
<span class="sd">&quot;&quot;&quot;</span>

<span class="kn">import</span> <span class="nn">util</span>

<span class="k">class</span> <span class="nc">SearchProblem</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    This class outlines the structure of a search problem, but doesn&#39;t implement</span>
<span class="sd">    any of the methods (in object-oriented terminology: an abstract class).</span>

<span class="sd">    You do not need to change anything in this class, ever.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">getStartState</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the start state for the search problem</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">isGoalState</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">          state: Search state</span>

<span class="sd">        Returns True if and only if the state is a valid goal state</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getSuccessors</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">          state: Search state</span>

<span class="sd">        For a given state, this should return a list of triples,</span>
<span class="sd">        (successor, action, stepCost), where &#39;successor&#39; is a</span>
<span class="sd">        successor to the current state, &#39;action&#39; is the action</span>
<span class="sd">        required to get there, and &#39;stepCost&#39; is the incremental</span>
<span class="sd">        cost of expanding to that successor</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getCostOfActions</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">         actions: A list of actions to take</span>

<span class="sd">        This method returns the total cost of a particular sequence of actions.  The sequence must</span>
<span class="sd">        be composed of legal moves</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>


<span class="k">def</span> <span class="nf">tinyMazeSearch</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Returns a sequence of moves that solves tinyMaze.  For any other</span>
<span class="sd">    maze, the sequence of moves will be incorrect, so only use this for tinyMaze</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Directions</span>
    <span class="n">s</span> <span class="o">=</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span>
    <span class="n">w</span> <span class="o">=</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span>
    <span class="k">return</span>  <span class="p">[</span><span class="n">s</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">w</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">w</span><span class="p">,</span><span class="n">w</span><span class="p">,</span><span class="n">s</span><span class="p">,</span><span class="n">w</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">depthFirstSearch</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Search the deepest nodes in the search tree first</span>
<span class="sd">    [2nd Edition: p 75, 3rd Edition: p 87]</span>

<span class="sd">    Your search algorithm needs to return a list of actions that reaches</span>
<span class="sd">    the goal.  Make sure to implement a graph search algorithm</span>
<span class="sd">    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].</span>

<span class="sd">    To get started, you might want to try some of these simple commands to</span>
<span class="sd">    understand the search problem that is being passed in:</span>

<span class="sd">    print &quot;Start:&quot;, problem.getStartState()</span>
<span class="sd">    print &quot;Is the start a goal?&quot;, problem.isGoalState(problem.getStartState())</span>
<span class="sd">    print &quot;Start&#39;s successors:&quot;, problem.getSuccessors(problem.getStartState())</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
    <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">breadthFirstSearch</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Search the shallowest nodes in the search tree first.</span>
<span class="sd">    [2nd Edition: p 73, 3rd Edition: p 82]</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
    <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">uniformCostSearch</span><span class="p">(</span><span class="n">problem</span><span class="p">):</span>
    <span class="s">&quot;Search the node of least total cost first. &quot;</span>
    <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
    <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">nullHeuristic</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">problem</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A heuristic function estimates the cost from the current state to the nearest</span>
<span class="sd">    goal in the provided SearchProblem.  This heuristic is trivial.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">return</span> <span class="mi">0</span>

<span class="k">def</span> <span class="nf">aStarSearch</span><span class="p">(</span><span class="n">problem</span><span class="p">,</span> <span class="n">heuristic</span><span class="o">=</span><span class="n">nullHeuristic</span><span class="p">):</span>
    <span class="s">&quot;Search the node that has the lowest combined cost and heuristic first.&quot;</span>
    <span class="s">&quot;*** YOUR CODE HERE ***&quot;</span>
    <span class="n">util</span><span class="o">.</span><span class="n">raiseNotDefined</span><span class="p">()</span>


<span class="c"># Abbreviations</span>
<span class="n">bfs</span> <span class="o">=</span> <span class="n">breadthFirstSearch</span>
<span class="n">dfs</span> <span class="o">=</span> <span class="n">depthFirstSearch</span>
<span class="n">astar</span> <span class="o">=</span> <span class="n">aStarSearch</span>
<span class="n">ucs</span> <span class="o">=</span> <span class="n">uniformCostSearch</span>
</pre></div>
</body>
</html>
