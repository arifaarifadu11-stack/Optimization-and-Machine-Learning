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

<div class="highlight"><pre><span class="c"># game.py</span>
<span class="c"># -------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="kn">from</span> <span class="nn">util</span> <span class="kn">import</span> <span class="o">*</span>
<span class="kn">import</span> <span class="nn">time</span><span class="o">,</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">traceback</span>

<span class="c">#######################</span>
<span class="c"># Parts worth reading #</span>
<span class="c">#######################</span>

<span class="k">class</span> <span class="nc">Agent</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    An agent must define a getAction method, but may also define the</span>
<span class="sd">    following methods which will be called if they exist:</span>

<span class="sd">    def registerInitialState(self, state): # inspects the starting state</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">index</span> <span class="o">=</span> <span class="n">index</span>

    <span class="k">def</span> <span class="nf">getAction</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        The Agent will receive a GameState (from either {pacman, capture, sonar}.py) and</span>
<span class="sd">        must return an action from Directions.{North, South, East, West, Stop}</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">raiseNotDefined</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">Directions</span><span class="p">:</span>
    <span class="n">NORTH</span> <span class="o">=</span> <span class="s">&#39;North&#39;</span>
    <span class="n">SOUTH</span> <span class="o">=</span> <span class="s">&#39;South&#39;</span>
    <span class="n">EAST</span> <span class="o">=</span> <span class="s">&#39;East&#39;</span>
    <span class="n">WEST</span> <span class="o">=</span> <span class="s">&#39;West&#39;</span>
    <span class="n">STOP</span> <span class="o">=</span> <span class="s">&#39;Stop&#39;</span>

    <span class="n">LEFT</span> <span class="o">=</span>       <span class="p">{</span><span class="n">NORTH</span><span class="p">:</span> <span class="n">WEST</span><span class="p">,</span>
                   <span class="n">SOUTH</span><span class="p">:</span> <span class="n">EAST</span><span class="p">,</span>
                   <span class="n">EAST</span><span class="p">:</span>  <span class="n">NORTH</span><span class="p">,</span>
                   <span class="n">WEST</span><span class="p">:</span>  <span class="n">SOUTH</span><span class="p">,</span>
                   <span class="n">STOP</span><span class="p">:</span>  <span class="n">STOP</span><span class="p">}</span>

    <span class="n">RIGHT</span> <span class="o">=</span>      <span class="nb">dict</span><span class="p">([(</span><span class="n">y</span><span class="p">,</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="ow">in</span> <span class="n">LEFT</span><span class="o">.</span><span class="n">items</span><span class="p">()])</span>

    <span class="n">REVERSE</span> <span class="o">=</span> <span class="p">{</span><span class="n">NORTH</span><span class="p">:</span> <span class="n">SOUTH</span><span class="p">,</span>
               <span class="n">SOUTH</span><span class="p">:</span> <span class="n">NORTH</span><span class="p">,</span>
               <span class="n">EAST</span><span class="p">:</span> <span class="n">WEST</span><span class="p">,</span>
               <span class="n">WEST</span><span class="p">:</span> <span class="n">EAST</span><span class="p">,</span>
               <span class="n">STOP</span><span class="p">:</span> <span class="n">STOP</span><span class="p">}</span>

<span class="k">class</span> <span class="nc">Configuration</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A Configuration holds the (x,y) coordinate of a character, along with its</span>
<span class="sd">    traveling direction.</span>

<span class="sd">    The convention for positions, like a graph, is that (0,0) is the lower left corner, x increases</span>
<span class="sd">    horizontally and y increases vertically.  Therefore, north is the direction of increasing y, or (0,1).</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pos</span><span class="p">,</span> <span class="n">direction</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">pos</span> <span class="o">=</span> <span class="n">pos</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">direction</span> <span class="o">=</span> <span class="n">direction</span>

    <span class="k">def</span> <span class="nf">getPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pos</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getDirection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">direction</span>

    <span class="k">def</span> <span class="nf">isInteger</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pos</span>
        <span class="k">return</span> <span class="n">x</span> <span class="o">==</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="ow">and</span> <span class="n">y</span> <span class="o">==</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">other</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">return</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pos</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">pos</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">direction</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">direction</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">x</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pos</span><span class="p">)</span>
        <span class="n">y</span> <span class="o">=</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direction</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="mi">13</span> <span class="o">*</span> <span class="n">y</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s">&quot;(x,y)=&quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">pos</span><span class="p">)</span><span class="o">+</span><span class="s">&quot;, &quot;</span><span class="o">+</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">direction</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">generateSuccessor</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">vector</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Generates a new configuration reached by translating the current</span>
<span class="sd">        configuration by the action vector.  This is a low-level call and does</span>
<span class="sd">        not attempt to respect the legality of the movement.</span>

<span class="sd">        Actions are movement vectors.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">pos</span>
        <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">vector</span>
        <span class="n">direction</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">vectorToDirection</span><span class="p">(</span><span class="n">vector</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">direction</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span><span class="p">:</span>
            <span class="n">direction</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">direction</span> <span class="c"># There is no stop direction</span>
        <span class="k">return</span> <span class="n">Configuration</span><span class="p">((</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">,</span> <span class="n">y</span><span class="o">+</span><span class="n">dy</span><span class="p">),</span> <span class="n">direction</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">AgentState</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    AgentStates hold the state of an agent (configuration, speed, scared, etc).</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">startConfiguration</span><span class="p">,</span> <span class="n">isPacman</span> <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">start</span> <span class="o">=</span> <span class="n">startConfiguration</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span> <span class="o">=</span> <span class="n">startConfiguration</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">isPacman</span> <span class="o">=</span> <span class="n">isPacman</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">isPacman</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&quot;Pacman: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span> <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&quot;Ghost: &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">other</span> <span class="p">):</span>
        <span class="k">if</span> <span class="n">other</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">False</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">configuration</span> <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">scaredTimer</span>

    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">configuration</span><span class="p">)</span> <span class="o">+</span> <span class="mi">13</span> <span class="o">*</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">scaredTimer</span><span class="p">))</span>

    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">AgentState</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">start</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">isPacman</span> <span class="p">)</span>
        <span class="n">state</span><span class="o">.</span><span class="n">configuration</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span>
        <span class="n">state</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">scaredTimer</span>
        <span class="k">return</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">getPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getDirection</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">getDirection</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">Grid</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A 2-dimensional array of objects backed by a list of lists.  Data is accessed</span>
<span class="sd">    via grid[x][y] where (x,y) are positions on a Pacman map with x horizontal,</span>
<span class="sd">    y vertical and the origin (0,0) in the bottom left corner.</span>

<span class="sd">    The __str__ method constructs an output that is oriented like a pacman board.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">initialValue</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">bitRepresentation</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">initialValue</span> <span class="ow">not</span> <span class="ow">in</span> <span class="p">[</span><span class="bp">False</span><span class="p">,</span> <span class="bp">True</span><span class="p">]:</span> <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Grids can only contain booleans&#39;</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">CELLS_PER_INT</span> <span class="o">=</span> <span class="mi">30</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">=</span> <span class="n">width</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">=</span> <span class="n">height</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="p">[[</span><span class="n">initialValue</span> <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">height</span><span class="p">)]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">width</span><span class="p">)]</span>
        <span class="k">if</span> <span class="n">bitRepresentation</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_unpackBits</span><span class="p">(</span><span class="n">bitRepresentation</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">i</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">__setitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">item</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">item</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">out</span> <span class="o">=</span> <span class="p">[[</span><span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">)]</span> <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">)]</span>
        <span class="n">out</span><span class="o">.</span><span class="n">reverse</span><span class="p">()</span>
        <span class="k">return</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">out</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">other</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">data</span>

    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="c"># return hash(str(self))</span>
        <span class="n">base</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="n">h</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">l</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">i</span><span class="p">:</span>
                    <span class="n">h</span> <span class="o">+=</span> <span class="n">base</span>
                <span class="n">base</span> <span class="o">*=</span> <span class="mi">2</span>
        <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span><span class="n">h</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">copy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">g</span> <span class="o">=</span> <span class="n">Grid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">)</span>
        <span class="n">g</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span><span class="p">[:]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">g</span>

    <span class="k">def</span> <span class="nf">deepCopy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">shallowCopy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">g</span> <span class="o">=</span> <span class="n">Grid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">)</span>
        <span class="n">g</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span>
        <span class="k">return</span> <span class="n">g</span>

    <span class="k">def</span> <span class="nf">count</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">item</span> <span class="o">=</span><span class="bp">True</span> <span class="p">):</span>
        <span class="k">return</span> <span class="nb">sum</span><span class="p">([</span><span class="n">x</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">asList</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span> <span class="o">=</span> <span class="bp">True</span><span class="p">):</span>
        <span class="nb">list</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">):</span>
                <span class="k">if</span> <span class="bp">self</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">==</span> <span class="n">key</span><span class="p">:</span> <span class="nb">list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span> <span class="p">)</span>
        <span class="k">return</span> <span class="nb">list</span>

    <span class="k">def</span> <span class="nf">packBits</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns an efficient int list representation</span>

<span class="sd">        (width, height, bitPackedInts...)</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">bits</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">]</span>
        <span class="n">currentInt</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">):</span>
            <span class="n">bit</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">CELLS_PER_INT</span> <span class="o">-</span> <span class="p">(</span><span class="n">i</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">CELLS_PER_INT</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
            <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cellIndexToPosition</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]:</span>
                <span class="n">currentInt</span> <span class="o">+=</span> <span class="mi">2</span> <span class="o">**</span> <span class="n">bit</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">CELLS_PER_INT</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">bits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentInt</span><span class="p">)</span>
                <span class="n">currentInt</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">bits</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">currentInt</span><span class="p">)</span>
        <span class="k">return</span> <span class="nb">tuple</span><span class="p">(</span><span class="n">bits</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_cellIndexToPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">index</span><span class="p">):</span>
        <span class="n">x</span> <span class="o">=</span> <span class="n">index</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span>
        <span class="n">y</span> <span class="o">=</span> <span class="n">index</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span>
        <span class="k">return</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span>

    <span class="k">def</span> <span class="nf">_unpackBits</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">bits</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Fills in data from a bit-level representation</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">cell</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">packed</span> <span class="ow">in</span> <span class="n">bits</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">bit</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_unpackInt</span><span class="p">(</span><span class="n">packed</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">CELLS_PER_INT</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">cell</span> <span class="o">==</span> <span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">:</span> <span class="k">break</span>
                <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_cellIndexToPosition</span><span class="p">(</span><span class="n">cell</span><span class="p">)</span>
                <span class="bp">self</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="n">bit</span>
                <span class="n">cell</span> <span class="o">+=</span> <span class="mi">1</span>

    <span class="k">def</span> <span class="nf">_unpackInt</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">packed</span><span class="p">,</span> <span class="n">size</span><span class="p">):</span>
        <span class="n">bools</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">if</span> <span class="n">packed</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span> <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="s">&quot;must be a positive integer&quot;</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">size</span><span class="p">):</span>
            <span class="n">n</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">**</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">CELLS_PER_INT</span> <span class="o">-</span> <span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">packed</span> <span class="o">&gt;=</span> <span class="n">n</span><span class="p">:</span>
                <span class="n">bools</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span>
                <span class="n">packed</span> <span class="o">-=</span> <span class="n">n</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">bools</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">False</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">bools</span>

<span class="k">def</span> <span class="nf">reconstituteGrid</span><span class="p">(</span><span class="n">bitRep</span><span class="p">):</span>
    <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">bitRep</span><span class="p">)</span> <span class="ow">is</span> <span class="ow">not</span> <span class="nb">type</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)):</span>
        <span class="k">return</span> <span class="n">bitRep</span>
    <span class="n">width</span><span class="p">,</span> <span class="n">height</span> <span class="o">=</span> <span class="n">bitRep</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">Grid</span><span class="p">(</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">,</span> <span class="n">bitRepresentation</span><span class="o">=</span> <span class="n">bitRep</span><span class="p">[</span><span class="mi">2</span><span class="p">:])</span>

<span class="c">####################################</span>
<span class="c"># Parts you shouldn&#39;t have to read #</span>
<span class="c">####################################</span>

<span class="k">class</span> <span class="nc">Actions</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A collection of static methods for manipulating move actions.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="c"># Directions</span>
    <span class="n">_directions</span> <span class="o">=</span> <span class="p">{</span><span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">:</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span>
                   <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">:</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">),</span>
                   <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">:</span>  <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
                   <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">:</span>  <span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span>
                   <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span><span class="p">:</span>  <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)}</span>

    <span class="n">_directionsAsList</span> <span class="o">=</span> <span class="n">_directions</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>

    <span class="n">TOLERANCE</span> <span class="o">=</span> <span class="o">.</span><span class="mo">001</span>

    <span class="k">def</span> <span class="nf">reverseDirection</span><span class="p">(</span><span class="n">action</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span>
        <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span>
        <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span>
        <span class="k">if</span> <span class="n">action</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span>
        <span class="k">return</span> <span class="n">action</span>
    <span class="n">reverseDirection</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">reverseDirection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">vectorToDirection</span><span class="p">(</span><span class="n">vector</span><span class="p">):</span>
        <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">vector</span>
        <span class="k">if</span> <span class="n">dy</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span>
        <span class="k">if</span> <span class="n">dy</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span>
        <span class="k">if</span> <span class="n">dx</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span>
        <span class="k">if</span> <span class="n">dx</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span>
        <span class="k">return</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span>
    <span class="n">vectorToDirection</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">vectorToDirection</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">directionToVector</span><span class="p">(</span><span class="n">direction</span><span class="p">,</span> <span class="n">speed</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">):</span>
        <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span>  <span class="n">Actions</span><span class="o">.</span><span class="n">_directions</span><span class="p">[</span><span class="n">direction</span><span class="p">]</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">dx</span> <span class="o">*</span> <span class="n">speed</span><span class="p">,</span> <span class="n">dy</span> <span class="o">*</span> <span class="n">speed</span><span class="p">)</span>
    <span class="n">directionToVector</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">directionToVector</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getPossibleActions</span><span class="p">(</span><span class="n">config</span><span class="p">,</span> <span class="n">walls</span><span class="p">):</span>
        <span class="n">possible</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">pos</span>
        <span class="n">x_int</span><span class="p">,</span> <span class="n">y_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="mf">0.5</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="mf">0.5</span><span class="p">)</span>

        <span class="c"># In between grid points, all agents must continue straight</span>
        <span class="k">if</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">x</span> <span class="o">-</span> <span class="n">x_int</span><span class="p">)</span> <span class="o">+</span> <span class="nb">abs</span><span class="p">(</span><span class="n">y</span> <span class="o">-</span> <span class="n">y_int</span><span class="p">)</span>  <span class="o">&gt;</span> <span class="n">Actions</span><span class="o">.</span><span class="n">TOLERANCE</span><span class="p">):</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">config</span><span class="o">.</span><span class="n">getDirection</span><span class="p">()]</span>

        <span class="k">for</span> <span class="nb">dir</span><span class="p">,</span> <span class="n">vec</span> <span class="ow">in</span> <span class="n">Actions</span><span class="o">.</span><span class="n">_directionsAsList</span><span class="p">:</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">vec</span>
            <span class="n">next_y</span> <span class="o">=</span> <span class="n">y_int</span> <span class="o">+</span> <span class="n">dy</span>
            <span class="n">next_x</span> <span class="o">=</span> <span class="n">x_int</span> <span class="o">+</span> <span class="n">dx</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">walls</span><span class="p">[</span><span class="n">next_x</span><span class="p">][</span><span class="n">next_y</span><span class="p">]:</span> <span class="n">possible</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">dir</span><span class="p">)</span>

        <span class="k">return</span> <span class="n">possible</span>

    <span class="n">getPossibleActions</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">getPossibleActions</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getLegalNeighbors</span><span class="p">(</span><span class="n">position</span><span class="p">,</span> <span class="n">walls</span><span class="p">):</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="n">position</span>
        <span class="n">x_int</span><span class="p">,</span> <span class="n">y_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="mf">0.5</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span> <span class="o">+</span> <span class="mf">0.5</span><span class="p">)</span>
        <span class="n">neighbors</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="nb">dir</span><span class="p">,</span> <span class="n">vec</span> <span class="ow">in</span> <span class="n">Actions</span><span class="o">.</span><span class="n">_directionsAsList</span><span class="p">:</span>
            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">vec</span>
            <span class="n">next_x</span> <span class="o">=</span> <span class="n">x_int</span> <span class="o">+</span> <span class="n">dx</span>
            <span class="k">if</span> <span class="n">next_x</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">next_x</span> <span class="o">==</span> <span class="n">walls</span><span class="o">.</span><span class="n">width</span><span class="p">:</span> <span class="k">continue</span>
            <span class="n">next_y</span> <span class="o">=</span> <span class="n">y_int</span> <span class="o">+</span> <span class="n">dy</span>
            <span class="k">if</span> <span class="n">next_y</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">next_y</span> <span class="o">==</span> <span class="n">walls</span><span class="o">.</span><span class="n">height</span><span class="p">:</span> <span class="k">continue</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">walls</span><span class="p">[</span><span class="n">next_x</span><span class="p">][</span><span class="n">next_y</span><span class="p">]:</span> <span class="n">neighbors</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">next_x</span><span class="p">,</span> <span class="n">next_y</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">neighbors</span>
    <span class="n">getLegalNeighbors</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">getLegalNeighbors</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getSuccessor</span><span class="p">(</span><span class="n">position</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span>
        <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span><span class="n">action</span><span class="p">)</span>
        <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">position</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">dy</span><span class="p">)</span>
    <span class="n">getSuccessor</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">getSuccessor</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">GameStateData</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>

<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">prevState</span> <span class="o">=</span> <span class="bp">None</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Generates a new data packet by copying information from its predecessor.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="n">prevState</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="n">prevState</span><span class="o">.</span><span class="n">food</span><span class="o">.</span><span class="n">shallowCopy</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">capsules</span> <span class="o">=</span> <span class="n">prevState</span><span class="o">.</span><span class="n">capsules</span><span class="p">[:]</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">copyAgentStates</span><span class="p">(</span> <span class="n">prevState</span><span class="o">.</span><span class="n">agentStates</span> <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">layout</span> <span class="o">=</span> <span class="n">prevState</span><span class="o">.</span><span class="n">layout</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_eaten</span> <span class="o">=</span> <span class="n">prevState</span><span class="o">.</span><span class="n">_eaten</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="n">prevState</span><span class="o">.</span><span class="n">score</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_foodEaten</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_capsuleEaten</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_agentMoved</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_lose</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_win</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">deepCopy</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">GameStateData</span><span class="p">(</span> <span class="bp">self</span> <span class="p">)</span>
        <span class="n">state</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">food</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">()</span>
        <span class="n">state</span><span class="o">.</span><span class="n">layout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">()</span>
        <span class="n">state</span><span class="o">.</span><span class="n">_agentMoved</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_agentMoved</span>
        <span class="n">state</span><span class="o">.</span><span class="n">_foodEaten</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_foodEaten</span>
        <span class="n">state</span><span class="o">.</span><span class="n">_capsuleEaten</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_capsuleEaten</span>
        <span class="k">return</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">copyAgentStates</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentStates</span> <span class="p">):</span>
        <span class="n">copiedStates</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">agentState</span> <span class="ow">in</span> <span class="n">agentStates</span><span class="p">:</span>
            <span class="n">copiedStates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">agentState</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="p">)</span>
        <span class="k">return</span> <span class="n">copiedStates</span>

    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">other</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Allows two states to be compared.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="n">other</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="c"># TODO Check for type of other</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">agentStates</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">food</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">food</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">capsules</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">capsules</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">score</span><span class="p">:</span> <span class="k">return</span> <span class="bp">False</span>
        <span class="k">return</span> <span class="bp">True</span>

    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Allows states to be keys of dictionaries.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">state</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span> <span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="nb">int</span><span class="p">(</span><span class="nb">hash</span><span class="p">(</span><span class="n">state</span><span class="p">))</span>
            <span class="k">except</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">print</span> <span class="n">e</span>
                <span class="c">#hash(state)</span>
        <span class="k">return</span> <span class="nb">int</span><span class="p">((</span><span class="nb">hash</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span><span class="p">))</span> <span class="o">+</span> <span class="mi">13</span><span class="o">*</span><span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">food</span><span class="p">)</span> <span class="o">+</span> <span class="mi">113</span><span class="o">*</span> <span class="nb">hash</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">capsules</span><span class="p">))</span> <span class="o">+</span> <span class="mi">7</span> <span class="o">*</span> <span class="nb">hash</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">score</span><span class="p">))</span> <span class="o">%</span> <span class="mi">1048575</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="n">width</span><span class="p">,</span> <span class="n">height</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">height</span>
        <span class="nb">map</span> <span class="o">=</span> <span class="n">Grid</span><span class="p">(</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">food</span><span class="p">)</span> <span class="o">==</span> <span class="nb">type</span><span class="p">((</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="n">reconstituteGrid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">food</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">width</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">height</span><span class="p">):</span>
                <span class="n">food</span><span class="p">,</span> <span class="n">walls</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">food</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">walls</span>
                <span class="nb">map</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_foodWallStr</span><span class="p">(</span><span class="n">food</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">],</span> <span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">])</span>

        <span class="k">for</span> <span class="n">agentState</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">agentState</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">continue</span>
            <span class="k">if</span> <span class="n">agentState</span><span class="o">.</span><span class="n">configuration</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">continue</span>
            <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span> <span class="n">i</span> <span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">nearestPoint</span><span class="p">(</span> <span class="n">agentState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">pos</span> <span class="p">)]</span>
            <span class="n">agent_dir</span> <span class="o">=</span> <span class="n">agentState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">direction</span>
            <span class="k">if</span> <span class="n">agentState</span><span class="o">.</span><span class="n">isPacman</span><span class="p">:</span>
                <span class="nb">map</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_pacStr</span><span class="p">(</span> <span class="n">agent_dir</span> <span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="nb">map</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_ghostStr</span><span class="p">(</span> <span class="n">agent_dir</span> <span class="p">)</span>

        <span class="k">for</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">capsules</span><span class="p">:</span>
            <span class="nb">map</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;o&#39;</span>

        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="nb">map</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="s">&quot;</span><span class="se">\n</span><span class="s">Score: </span><span class="si">%d</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">score</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_foodWallStr</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">hasFood</span><span class="p">,</span> <span class="n">hasWall</span> <span class="p">):</span>
        <span class="k">if</span> <span class="n">hasFood</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;.&#39;</span>
        <span class="k">elif</span> <span class="n">hasWall</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;%&#39;</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39; &#39;</span>

    <span class="k">def</span> <span class="nf">_pacStr</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="nb">dir</span> <span class="p">):</span>
        <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;v&#39;</span>
        <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;^&#39;</span>
        <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;&gt;&#39;</span>
        <span class="k">return</span> <span class="s">&#39;&lt;&#39;</span>

    <span class="k">def</span> <span class="nf">_ghostStr</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="nb">dir</span> <span class="p">):</span>
        <span class="k">return</span> <span class="s">&#39;G&#39;</span>
        <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;M&#39;</span>
        <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;W&#39;</span>
        <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">:</span>
            <span class="k">return</span> <span class="s">&#39;3&#39;</span>
        <span class="k">return</span> <span class="s">&#39;E&#39;</span>

    <span class="k">def</span> <span class="nf">initialize</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">layout</span><span class="p">,</span> <span class="n">numGhostAgents</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Creates an initial game state from a layout array (see layout.py).</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="n">layout</span><span class="o">.</span><span class="n">food</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">capsules</span> <span class="o">=</span> <span class="n">layout</span><span class="o">.</span><span class="n">capsules</span><span class="p">[:]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">layout</span> <span class="o">=</span> <span class="n">layout</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">score</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">numGhosts</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="k">for</span> <span class="n">isPacman</span><span class="p">,</span> <span class="n">pos</span> <span class="ow">in</span> <span class="n">layout</span><span class="o">.</span><span class="n">agentPositions</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">isPacman</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">numGhosts</span> <span class="o">==</span> <span class="n">numGhostAgents</span><span class="p">:</span> <span class="k">continue</span> <span class="c"># Max ghosts reached already</span>
                <span class="k">else</span><span class="p">:</span> <span class="n">numGhosts</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="n">AgentState</span><span class="p">(</span> <span class="n">Configuration</span><span class="p">(</span> <span class="n">pos</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span><span class="p">),</span> <span class="n">isPacman</span><span class="p">)</span> <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_eaten</span> <span class="o">=</span> <span class="p">[</span><span class="bp">False</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentStates</span><span class="p">]</span>

<span class="k">try</span><span class="p">:</span>
    <span class="kn">import</span> <span class="nn">boinc</span>
    <span class="n">_BOINC_ENABLED</span> <span class="o">=</span> <span class="bp">True</span>
<span class="k">except</span><span class="p">:</span>
    <span class="n">_BOINC_ENABLED</span> <span class="o">=</span> <span class="bp">False</span>

<span class="k">class</span> <span class="nc">Game</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    The Game manages the control flow, soliciting actions from agents.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agents</span><span class="p">,</span> <span class="n">display</span><span class="p">,</span> <span class="n">rules</span><span class="p">,</span> <span class="n">startingIndex</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">muteAgents</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">catchExceptions</span><span class="o">=</span><span class="bp">False</span> <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentCrashed</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agents</span> <span class="o">=</span> <span class="n">agents</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">display</span> <span class="o">=</span> <span class="n">display</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">rules</span> <span class="o">=</span> <span class="n">rules</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">startingIndex</span> <span class="o">=</span> <span class="n">startingIndex</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">gameOver</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">muteAgents</span> <span class="o">=</span> <span class="n">muteAgents</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">catchExceptions</span> <span class="o">=</span> <span class="n">catchExceptions</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">moveHistory</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span> <span class="k">for</span> <span class="n">agent</span> <span class="ow">in</span> <span class="n">agents</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimeWarnings</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span> <span class="k">for</span> <span class="n">agent</span> <span class="ow">in</span> <span class="n">agents</span><span class="p">]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentTimeout</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="kn">import</span> <span class="nn">cStringIO</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentOutput</span> <span class="o">=</span> <span class="p">[</span><span class="n">cStringIO</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span> <span class="k">for</span> <span class="n">agent</span> <span class="ow">in</span> <span class="n">agents</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">getProgress</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">gameOver</span><span class="p">:</span>
            <span class="k">return</span> <span class="mf">1.0</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getProgress</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_agentCrash</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
        <span class="s">&quot;Helper method for handling agent crashes&quot;</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">quiet</span><span class="p">:</span> <span class="n">traceback</span><span class="o">.</span><span class="n">print_exc</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">gameOver</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentCrashed</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">agentCrash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">)</span>

    <span class="n">OLD_STDOUT</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">OLD_STDERR</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">mute</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">muteAgents</span><span class="p">:</span> <span class="k">return</span>
        <span class="k">global</span> <span class="n">OLD_STDOUT</span><span class="p">,</span> <span class="n">OLD_STDERR</span>
        <span class="kn">import</span> <span class="nn">cStringIO</span>
        <span class="n">OLD_STDOUT</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span>
        <span class="n">OLD_STDERR</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span>
        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentOutput</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span>
        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentOutput</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">unmute</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">muteAgents</span><span class="p">:</span> <span class="k">return</span>
        <span class="k">global</span> <span class="n">OLD_STDOUT</span><span class="p">,</span> <span class="n">OLD_STDERR</span>
        <span class="c"># Revert stdout/stderr to originals</span>
        <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span> <span class="o">=</span> <span class="n">OLD_STDOUT</span>
        <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span> <span class="o">=</span> <span class="n">OLD_STDERR</span>


    <span class="k">def</span> <span class="nf">run</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Main control loop for game play.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">initialize</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">numMoves</span> <span class="o">=</span> <span class="mi">0</span>

        <span class="c">###self.display.initialize(self.state.makeObservation(1).data)</span>
        <span class="c"># inform learning agents of the game start</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">)):</span>
            <span class="n">agent</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">[</span><span class="n">i</span><span class="p">]</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">agent</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">mute</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
                <span class="c"># this is a null agent, meaning it failed to load</span>
                <span class="c"># the other team wins</span>
                <span class="k">print</span> <span class="s">&quot;Agent </span><span class="si">%d</span><span class="s"> failed to load&quot;</span> <span class="o">%</span> <span class="n">i</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
                <span class="k">return</span>
            <span class="k">if</span> <span class="p">(</span><span class="s">&quot;registerInitialState&quot;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">agent</span><span class="p">)):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">mute</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">catchExceptions</span><span class="p">:</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">timed_func</span> <span class="o">=</span> <span class="n">TimeoutFunction</span><span class="p">(</span><span class="n">agent</span><span class="o">.</span><span class="n">registerInitialState</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getMaxStartupTime</span><span class="p">(</span><span class="n">i</span><span class="p">)))</span>
                        <span class="k">try</span><span class="p">:</span>
                            <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
                            <span class="n">timed_func</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">())</span>
                            <span class="n">time_taken</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimes</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+=</span> <span class="n">time_taken</span>
                        <span class="k">except</span> <span class="n">TimeoutFunctionException</span><span class="p">:</span>
                            <span class="k">print</span> <span class="s">&quot;Agent </span><span class="si">%d</span><span class="s"> ran out of time on startup!&quot;</span> <span class="o">%</span> <span class="n">i</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">agentTimeout</span> <span class="o">=</span> <span class="bp">True</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
                            <span class="k">return</span>
                    <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span><span class="n">data</span><span class="p">:</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                        <span class="k">return</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">agent</span><span class="o">.</span><span class="n">registerInitialState</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">())</span>
                <span class="c">## TODO: could this exceed the total time</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>

        <span class="n">agentIndex</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">startingIndex</span>
        <span class="n">numAgents</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">agents</span> <span class="p">)</span>

        <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">gameOver</span><span class="p">:</span>
            <span class="c"># Fetch the next agent</span>
            <span class="n">agent</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span>
            <span class="n">move_time</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="n">skip_action</span> <span class="o">=</span> <span class="bp">False</span>
            <span class="c"># Generate an observation of the state</span>
            <span class="k">if</span> <span class="s">&#39;observationFunction&#39;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span> <span class="n">agent</span> <span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">mute</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">catchExceptions</span><span class="p">:</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">timed_func</span> <span class="o">=</span> <span class="n">TimeoutFunction</span><span class="p">(</span><span class="n">agent</span><span class="o">.</span><span class="n">observationFunction</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getMoveTimeout</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)))</span>
                        <span class="k">try</span><span class="p">:</span>
                            <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
                            <span class="n">observation</span> <span class="o">=</span> <span class="n">timed_func</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">())</span>
                        <span class="k">except</span> <span class="n">TimeoutFunctionException</span><span class="p">:</span>
                            <span class="n">skip_action</span> <span class="o">=</span> <span class="bp">True</span>
                        <span class="n">move_time</span> <span class="o">+=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                    <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span><span class="n">data</span><span class="p">:</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                        <span class="k">return</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">observation</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">observationFunction</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">())</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">observation</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">()</span>

            <span class="c"># Solicit an action</span>
            <span class="n">action</span> <span class="o">=</span> <span class="bp">None</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">mute</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">catchExceptions</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="n">timed_func</span> <span class="o">=</span> <span class="n">TimeoutFunction</span><span class="p">(</span><span class="n">agent</span><span class="o">.</span><span class="n">getAction</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getMoveTimeout</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">))</span> <span class="o">-</span> <span class="nb">int</span><span class="p">(</span><span class="n">move_time</span><span class="p">))</span>
                    <span class="k">try</span><span class="p">:</span>
                        <span class="n">start_time</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
                        <span class="k">if</span> <span class="n">skip_action</span><span class="p">:</span>
                            <span class="k">raise</span> <span class="n">TimeoutFunctionException</span><span class="p">()</span>
                        <span class="n">action</span> <span class="o">=</span> <span class="n">timed_func</span><span class="p">(</span> <span class="n">observation</span> <span class="p">)</span>
                    <span class="k">except</span> <span class="n">TimeoutFunctionException</span><span class="p">:</span>
                        <span class="k">print</span> <span class="s">&quot;Agent </span><span class="si">%d</span><span class="s"> timed out on a single move!&quot;</span> <span class="o">%</span> <span class="n">agentIndex</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">agentTimeout</span> <span class="o">=</span> <span class="bp">True</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                        <span class="k">return</span>

                    <span class="n">move_time</span> <span class="o">+=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">start_time</span>

                    <span class="k">if</span> <span class="n">move_time</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getMoveWarningTime</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">):</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimeWarnings</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
                        <span class="k">print</span> <span class="s">&quot;Agent </span><span class="si">%d</span><span class="s"> took too long to make a move! This is warning </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimeWarnings</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">])</span>
                        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimeWarnings</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getMaxTimeWarnings</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">):</span>
                            <span class="k">print</span> <span class="s">&quot;Agent </span><span class="si">%d</span><span class="s"> exceeded the maximum number of warnings: </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimeWarnings</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">])</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">agentTimeout</span> <span class="o">=</span> <span class="bp">True</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
                            <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>

                    <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimes</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span> <span class="o">+=</span> <span class="n">move_time</span>
                    <span class="c">#print &quot;Agent: %d, time: %f, total: %f&quot; % (agentIndex, move_time, self.totalAgentTimes[agentIndex])</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimes</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span> <span class="o">&gt;</span> <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">getMaxTotalTime</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">):</span>
                        <span class="k">print</span> <span class="s">&quot;Agent </span><span class="si">%d</span><span class="s"> ran out of time! (time: </span><span class="si">%1.2f</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">totalAgentTimes</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">])</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">agentTimeout</span> <span class="o">=</span> <span class="bp">True</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="n">quiet</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
                        <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                        <span class="k">return</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span><span class="n">data</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                    <span class="k">return</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">action</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">getAction</span><span class="p">(</span><span class="n">observation</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>

            <span class="c"># Execute the action</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">moveHistory</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="n">agentIndex</span><span class="p">,</span> <span class="n">action</span><span class="p">)</span> <span class="p">)</span>
            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">catchExceptions</span><span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span> <span class="n">agentIndex</span><span class="p">,</span> <span class="n">action</span> <span class="p">)</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span><span class="n">data</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">mute</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                    <span class="k">return</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span> <span class="n">agentIndex</span><span class="p">,</span> <span class="n">action</span> <span class="p">)</span>

            <span class="c"># Change the display</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">update</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">data</span> <span class="p">)</span>
            <span class="c">###idx = agentIndex - agentIndex % 2 + 1</span>
            <span class="c">###self.display.update( self.state.makeObservation(idx).data )</span>

            <span class="c"># Allow for game specific conditions (winning, losing, etc.)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">rules</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span>
            <span class="c"># Track progress</span>
            <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="n">numAgents</span> <span class="o">+</span> <span class="mi">1</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">numMoves</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="c"># Next agent</span>
            <span class="n">agentIndex</span> <span class="o">=</span> <span class="p">(</span> <span class="n">agentIndex</span> <span class="o">+</span> <span class="mi">1</span> <span class="p">)</span> <span class="o">%</span> <span class="n">numAgents</span>

            <span class="k">if</span> <span class="n">_BOINC_ENABLED</span><span class="p">:</span>
                <span class="n">boinc</span><span class="o">.</span><span class="n">set_fraction_done</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">getProgress</span><span class="p">())</span>

        <span class="c"># inform a learning agent of the game result</span>
        <span class="k">for</span> <span class="n">agentIndex</span><span class="p">,</span> <span class="n">agent</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">agents</span><span class="p">):</span>
            <span class="k">if</span> <span class="s">&quot;final&quot;</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span> <span class="n">agent</span> <span class="p">)</span> <span class="p">:</span>
                <span class="k">try</span><span class="p">:</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">mute</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
                    <span class="n">agent</span><span class="o">.</span><span class="n">final</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                <span class="k">except</span> <span class="ne">Exception</span><span class="p">,</span><span class="n">data</span><span class="p">:</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">catchExceptions</span><span class="p">:</span> <span class="k">raise</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">_agentCrash</span><span class="p">(</span><span class="n">agentIndex</span><span class="p">)</span>
                    <span class="bp">self</span><span class="o">.</span><span class="n">unmute</span><span class="p">()</span>
                    <span class="k">return</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">display</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span>
</pre></div>
</body>
</html>
