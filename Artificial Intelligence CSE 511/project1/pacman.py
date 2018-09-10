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

<div class="highlight"><pre><span class="c"># pacman.py</span>
<span class="c"># ---------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">Pacman.py holds the logic for the classic pacman game along with the main</span>
<span class="sd">code to run a game.  This file is divided into three sections:</span>

<span class="sd">  (i)  Your interface to the pacman world:</span>
<span class="sd">          Pacman is a complex environment.  You probably don&#39;t want to</span>
<span class="sd">          read through all of the code we wrote to make the game runs</span>
<span class="sd">          correctly.  This section contains the parts of the code</span>
<span class="sd">          that you will need to understand in order to complete the</span>
<span class="sd">          project.  There is also some code in game.py that you should</span>
<span class="sd">          understand.</span>

<span class="sd">  (ii)  The hidden secrets of pacman:</span>
<span class="sd">          This section contains all of the logic code that the pacman</span>
<span class="sd">          environment uses to decide who can move where, who dies when</span>
<span class="sd">          things collide, etc.  You shouldn&#39;t need to read this section</span>
<span class="sd">          of code, but you can if you want.</span>

<span class="sd">  (iii) Framework to start a game:</span>
<span class="sd">          The final section contains the code for reading the command</span>
<span class="sd">          you use to set up the game, then starting up a new game, along with</span>
<span class="sd">          linking in all the external parts (agent functions, graphics).</span>
<span class="sd">          Check this section out to see all the options available to you.</span>

<span class="sd">To play your first game, type &#39;python pacman.py&#39; from the command line.</span>
<span class="sd">The keys are &#39;a&#39;, &#39;s&#39;, &#39;d&#39;, and &#39;w&#39; to move (or arrow keys).  Have fun!</span>
<span class="sd">&quot;&quot;&quot;</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">GameStateData</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Game</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Directions</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Actions</span>
<span class="kn">from</span> <span class="nn">util</span> <span class="kn">import</span> <span class="n">nearestPoint</span>
<span class="kn">from</span> <span class="nn">util</span> <span class="kn">import</span> <span class="n">manhattanDistance</span>
<span class="kn">import</span> <span class="nn">util</span><span class="o">,</span> <span class="nn">layout</span>
<span class="kn">import</span> <span class="nn">sys</span><span class="o">,</span> <span class="nn">types</span><span class="o">,</span> <span class="nn">time</span><span class="o">,</span> <span class="nn">random</span><span class="o">,</span> <span class="nn">os</span>

<span class="c">###################################################</span>
<span class="c"># YOUR INTERFACE TO THE PACMAN WORLD: A GameState #</span>
<span class="c">###################################################</span>

<span class="k">class</span> <span class="nc">GameState</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A GameState specifies the full game state, including the food, capsules,</span>
<span class="sd">    agent configurations and score changes.</span>

<span class="sd">    GameStates are used by the Game object to capture the actual state of the game and</span>
<span class="sd">    can be used by agents to reason about the game.</span>

<span class="sd">    Much of the information in a GameState is stored in a GameStateData object.  We</span>
<span class="sd">    strongly suggest that you access that data via the accessor methods below rather</span>
<span class="sd">    than referring to the GameStateData object directly.</span>

<span class="sd">    Note that in classic Pacman, Pacman is always agent 0.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="c">####################################################</span>
    <span class="c"># Accessor methods: use these to access state data #</span>
    <span class="c">####################################################</span>

    <span class="c"># static variable keeps track of which states have had getLegalActions called</span>
    <span class="n">explored</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
    <span class="k">def</span> <span class="nf">getAndResetExplored</span><span class="p">():</span>
        <span class="n">tmp</span> <span class="o">=</span> <span class="n">GameState</span><span class="o">.</span><span class="n">explored</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
        <span class="n">GameState</span><span class="o">.</span><span class="n">explored</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">tmp</span>
    <span class="n">getAndResetExplored</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span><span class="n">getAndResetExplored</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getLegalActions</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="o">=</span><span class="mi">0</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the legal actions for the agent specified.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">GameState</span><span class="o">.</span><span class="n">explored</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">isWin</span><span class="p">()</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">isLose</span><span class="p">():</span> <span class="k">return</span> <span class="p">[]</span>

        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>  <span class="c"># Pacman is moving</span>
            <span class="k">return</span> <span class="n">PacmanRules</span><span class="o">.</span><span class="n">getLegalActions</span><span class="p">(</span> <span class="bp">self</span> <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">GhostRules</span><span class="o">.</span><span class="n">getLegalActions</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">generateSuccessor</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns the successor state after the specified agent takes the action.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="c"># Check that successors exist</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">isWin</span><span class="p">()</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">isLose</span><span class="p">():</span> <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Can</span><span class="se">\&#39;</span><span class="s">t generate a successor of a terminal state.&#39;</span><span class="p">)</span>

        <span class="c"># Copy current state</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">GameState</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span>

        <span class="c"># Let agent&#39;s logic deal with its action&#39;s effects on the board</span>
        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>  <span class="c"># Pacman is moving</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_eaten</span> <span class="o">=</span> <span class="p">[</span><span class="bp">False</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">state</span><span class="o">.</span><span class="n">getNumAgents</span><span class="p">())]</span>
            <span class="n">PacmanRules</span><span class="o">.</span><span class="n">applyAction</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">action</span> <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>                <span class="c"># A ghost is moving</span>
            <span class="n">GhostRules</span><span class="o">.</span><span class="n">applyAction</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">agentIndex</span> <span class="p">)</span>

        <span class="c"># Time passes</span>
        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">+=</span> <span class="o">-</span><span class="n">TIME_PENALTY</span> <span class="c"># Penalty for waiting around</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">GhostRules</span><span class="o">.</span><span class="n">decrementTimer</span><span class="p">(</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span> <span class="p">)</span>

        <span class="c"># Resolve multi-agent effects</span>
        <span class="n">GhostRules</span><span class="o">.</span><span class="n">checkDeath</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">agentIndex</span> <span class="p">)</span>

        <span class="c"># Book keeping</span>
        <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_agentMoved</span> <span class="o">=</span> <span class="n">agentIndex</span>
        <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">score</span> <span class="o">+=</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">scoreChange</span>
        <span class="k">return</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">getLegalPacmanActions</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">getLegalActions</span><span class="p">(</span> <span class="mi">0</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">generatePacmanSuccessor</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">action</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Generates the successor state after the specified pacman move</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span> <span class="mi">0</span><span class="p">,</span> <span class="n">action</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">getPacmanState</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns an AgentState object for pacman (in game.py)</span>

<span class="sd">        state.pos gives the current position</span>
<span class="sd">        state.direction gives the travel vector</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getPacmanPosition</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getGhostStates</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>

    <span class="k">def</span> <span class="nf">getGhostState</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span> <span class="p">):</span>
        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">agentIndex</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getNumAgents</span><span class="p">():</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;Invalid index passed to getGhostState&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">getGhostPosition</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span> <span class="p">):</span>
        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;Pacman&#39;s index passed to getGhostPosition&quot;</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getGhostPositions</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">s</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">getGhostStates</span><span class="p">()]</span>

    <span class="k">def</span> <span class="nf">getNumAgents</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">getScore</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">score</span>

    <span class="k">def</span> <span class="nf">getCapsules</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns a list of positions (x,y) of the remaining capsules.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">capsules</span>

    <span class="k">def</span> <span class="nf">getNumFood</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">getFood</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns a Grid of boolean food indicator variables.</span>

<span class="sd">        Grids can be accessed via list notation, so to check</span>
<span class="sd">        if there is food at (x,y), just call</span>

<span class="sd">        currentFood = state.getFood()</span>
<span class="sd">        if currentFood[x][y] == True: ...</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span>

    <span class="k">def</span> <span class="nf">getWalls</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns a Grid of boolean wall indicator variables.</span>

<span class="sd">        Grids can be accessed via list notation, so to check</span>
<span class="sd">        if there is food at (x,y), just call</span>

<span class="sd">        walls = state.getWalls()</span>
<span class="sd">        if walls[x][y] == True: ...</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">walls</span>

    <span class="k">def</span> <span class="nf">hasFood</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">hasWall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">isLose</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_lose</span>

    <span class="k">def</span> <span class="nf">isWin</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_win</span>

    <span class="c">#############################################</span>
    <span class="c">#             Helper methods:               #</span>
    <span class="c"># You shouldn&#39;t need to call these directly #</span>
    <span class="c">#############################################</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">prevState</span> <span class="o">=</span> <span class="bp">None</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Generates a new state by copying information from its predecessor.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="n">prevState</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span> <span class="c"># Initial state</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">GameStateData</span><span class="p">(</span><span class="n">prevState</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">GameStateData</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">deepCopy</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">GameState</span><span class="p">(</span> <span class="bp">self</span> <span class="p">)</span>
        <span class="n">state</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">state</span>

    <span class="k">def</span> <span class="nf">__eq__</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">other</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Allows two states to be compared.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">==</span> <span class="n">other</span><span class="o">.</span><span class="n">data</span>

    <span class="k">def</span> <span class="nf">__hash__</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Allows states to be keys of dictionaries.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="nb">hash</span><span class="p">(</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span> <span class="bp">self</span> <span class="p">):</span>

        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">initialize</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">layout</span><span class="p">,</span> <span class="n">numGhostAgents</span><span class="o">=</span><span class="mi">1000</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Creates an initial game state from a layout array (see layout.py).</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">initialize</span><span class="p">(</span><span class="n">layout</span><span class="p">,</span> <span class="n">numGhostAgents</span><span class="p">)</span>

<span class="c">############################################################################</span>
<span class="c">#                     THE HIDDEN SECRETS OF PACMAN                         #</span>
<span class="c">#                                                                          #</span>
<span class="c"># You shouldn&#39;t need to look through the code in this section of the file. #</span>
<span class="c">############################################################################</span>

<span class="n">SCARED_TIME</span> <span class="o">=</span> <span class="mi">40</span>    <span class="c"># Moves ghosts are scared</span>
<span class="n">COLLISION_TOLERANCE</span> <span class="o">=</span> <span class="mf">0.7</span> <span class="c"># How close ghosts must be to Pacman to kill</span>
<span class="n">TIME_PENALTY</span> <span class="o">=</span> <span class="mi">1</span> <span class="c"># Number of points lost each round</span>

<span class="k">class</span> <span class="nc">ClassicGameRules</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    These game rules manage the control flow of a game, deciding when</span>
<span class="sd">    and how the game starts and ends.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span> <span class="o">=</span> <span class="n">timeout</span>

    <span class="k">def</span> <span class="nf">newGame</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">layout</span><span class="p">,</span> <span class="n">pacmanAgent</span><span class="p">,</span> <span class="n">ghostAgents</span><span class="p">,</span> <span class="n">display</span><span class="p">,</span> <span class="n">quiet</span> <span class="o">=</span> <span class="bp">False</span><span class="p">,</span> <span class="n">catchExceptions</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
        <span class="n">agents</span> <span class="o">=</span> <span class="p">[</span><span class="n">pacmanAgent</span><span class="p">]</span> <span class="o">+</span> <span class="n">ghostAgents</span><span class="p">[:</span><span class="n">layout</span><span class="o">.</span><span class="n">getNumGhosts</span><span class="p">()]</span>
        <span class="n">initState</span> <span class="o">=</span> <span class="n">GameState</span><span class="p">()</span>
        <span class="n">initState</span><span class="o">.</span><span class="n">initialize</span><span class="p">(</span> <span class="n">layout</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">ghostAgents</span><span class="p">)</span> <span class="p">)</span>
        <span class="n">game</span> <span class="o">=</span> <span class="n">Game</span><span class="p">(</span><span class="n">agents</span><span class="p">,</span> <span class="n">display</span><span class="p">,</span> <span class="bp">self</span><span class="p">,</span> <span class="n">catchExceptions</span><span class="o">=</span><span class="n">catchExceptions</span><span class="p">)</span>
        <span class="n">game</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">initState</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">initialState</span> <span class="o">=</span> <span class="n">initState</span><span class="o">.</span><span class="n">deepCopy</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">quiet</span> <span class="o">=</span> <span class="n">quiet</span>
        <span class="k">return</span> <span class="n">game</span>

    <span class="k">def</span> <span class="nf">process</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">,</span> <span class="n">game</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Checks to see whether it is time to end the game.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">if</span> <span class="n">state</span><span class="o">.</span><span class="n">isWin</span><span class="p">():</span> <span class="bp">self</span><span class="o">.</span><span class="n">win</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">game</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">state</span><span class="o">.</span><span class="n">isLose</span><span class="p">():</span> <span class="bp">self</span><span class="o">.</span><span class="n">lose</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">game</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">win</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">,</span> <span class="n">game</span> <span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span> <span class="k">print</span> <span class="s">&quot;Pacman emerges victorious! Score: </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">score</span>
        <span class="n">game</span><span class="o">.</span><span class="n">gameOver</span> <span class="o">=</span> <span class="bp">True</span>

    <span class="k">def</span> <span class="nf">lose</span><span class="p">(</span> <span class="bp">self</span><span class="p">,</span> <span class="n">state</span><span class="p">,</span> <span class="n">game</span> <span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span> <span class="k">print</span> <span class="s">&quot;Pacman died! Score: </span><span class="si">%d</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">score</span>
        <span class="n">game</span><span class="o">.</span><span class="n">gameOver</span> <span class="o">=</span> <span class="bp">True</span>

    <span class="k">def</span> <span class="nf">getProgress</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">game</span><span class="p">):</span>
        <span class="k">return</span> <span class="nb">float</span><span class="p">(</span><span class="n">game</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">getNumFood</span><span class="p">())</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">initialState</span><span class="o">.</span><span class="n">getNumFood</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">agentCrash</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">game</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">print</span> <span class="s">&quot;Pacman crashed&quot;</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">print</span> <span class="s">&quot;A ghost crashed&quot;</span>

    <span class="k">def</span> <span class="nf">getMaxTotalTime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span>

    <span class="k">def</span> <span class="nf">getMaxStartupTime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span>

    <span class="k">def</span> <span class="nf">getMoveWarningTime</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span>

    <span class="k">def</span> <span class="nf">getMoveTimeout</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span>

    <span class="k">def</span> <span class="nf">getMaxTimeWarnings</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">return</span> <span class="mi">0</span>

<span class="k">class</span> <span class="nc">PacmanRules</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    These functions govern how pacman interacts with his environment under</span>
<span class="sd">    the classic game rules.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">PACMAN_SPEED</span><span class="o">=</span><span class="mi">1</span>

    <span class="k">def</span> <span class="nf">getLegalActions</span><span class="p">(</span> <span class="n">state</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Returns a list of possible actions.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="k">return</span> <span class="n">Actions</span><span class="o">.</span><span class="n">getPossibleActions</span><span class="p">(</span> <span class="n">state</span><span class="o">.</span><span class="n">getPacmanState</span><span class="p">()</span><span class="o">.</span><span class="n">configuration</span><span class="p">,</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">walls</span> <span class="p">)</span>
    <span class="n">getLegalActions</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">getLegalActions</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">applyAction</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">action</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Edits the state to reflect the results of the action.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">legal</span> <span class="o">=</span> <span class="n">PacmanRules</span><span class="o">.</span><span class="n">getLegalActions</span><span class="p">(</span> <span class="n">state</span> <span class="p">)</span>
        <span class="k">if</span> <span class="n">action</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">legal</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;Illegal action &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">action</span><span class="p">))</span>

        <span class="n">pacmanState</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>

        <span class="c"># Update Configuration</span>
        <span class="n">vector</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span> <span class="n">action</span><span class="p">,</span> <span class="n">PacmanRules</span><span class="o">.</span><span class="n">PACMAN_SPEED</span> <span class="p">)</span>
        <span class="n">pacmanState</span><span class="o">.</span><span class="n">configuration</span> <span class="o">=</span> <span class="n">pacmanState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span> <span class="n">vector</span> <span class="p">)</span>

        <span class="c"># Eat</span>
        <span class="nb">next</span> <span class="o">=</span> <span class="n">pacmanState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span>
        <span class="n">nearest</span> <span class="o">=</span> <span class="n">nearestPoint</span><span class="p">(</span> <span class="nb">next</span> <span class="p">)</span>
        <span class="k">if</span> <span class="n">manhattanDistance</span><span class="p">(</span> <span class="n">nearest</span><span class="p">,</span> <span class="nb">next</span> <span class="p">)</span> <span class="o">&lt;=</span> <span class="mf">0.5</span> <span class="p">:</span>
            <span class="c"># Remove food</span>
            <span class="n">PacmanRules</span><span class="o">.</span><span class="n">consume</span><span class="p">(</span> <span class="n">nearest</span><span class="p">,</span> <span class="n">state</span> <span class="p">)</span>
    <span class="n">applyAction</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">applyAction</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">consume</span><span class="p">(</span> <span class="n">position</span><span class="p">,</span> <span class="n">state</span> <span class="p">):</span>
        <span class="n">x</span><span class="p">,</span><span class="n">y</span> <span class="o">=</span> <span class="n">position</span>
        <span class="c"># Eat food</span>
        <span class="k">if</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]:</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">+=</span> <span class="mi">10</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">food</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="bp">False</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_foodEaten</span> <span class="o">=</span> <span class="n">position</span>
            <span class="c"># TODO: cache numFood?</span>
            <span class="n">numFood</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">getNumFood</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">numFood</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_lose</span><span class="p">:</span>
                <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">+=</span> <span class="mi">500</span>
                <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_win</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="c"># Eat capsule</span>
        <span class="k">if</span><span class="p">(</span> <span class="n">position</span> <span class="ow">in</span> <span class="n">state</span><span class="o">.</span><span class="n">getCapsules</span><span class="p">()</span> <span class="p">):</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">capsules</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span> <span class="n">position</span> <span class="p">)</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_capsuleEaten</span> <span class="o">=</span> <span class="n">position</span>
            <span class="c"># Reset all ghosts&#39; scared timers</span>
            <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span> <span class="p">)</span> <span class="p">):</span>
                <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">=</span> <span class="n">SCARED_TIME</span>
    <span class="n">consume</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">consume</span> <span class="p">)</span>

<span class="k">class</span> <span class="nc">GhostRules</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    These functions dictate how ghosts interact with their environment.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">GHOST_SPEED</span><span class="o">=</span><span class="mf">1.0</span>
    <span class="k">def</span> <span class="nf">getLegalActions</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">ghostIndex</span> <span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Ghosts cannot stop, and cannot turn around unless they</span>
<span class="sd">        reach a dead end, but can turn 90 degrees at intersections.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">conf</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">getGhostState</span><span class="p">(</span> <span class="n">ghostIndex</span> <span class="p">)</span><span class="o">.</span><span class="n">configuration</span>
        <span class="n">possibleActions</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">getPossibleActions</span><span class="p">(</span> <span class="n">conf</span><span class="p">,</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">layout</span><span class="o">.</span><span class="n">walls</span> <span class="p">)</span>
        <span class="n">reverse</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">reverseDirection</span><span class="p">(</span> <span class="n">conf</span><span class="o">.</span><span class="n">direction</span> <span class="p">)</span>
        <span class="k">if</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span> <span class="ow">in</span> <span class="n">possibleActions</span><span class="p">:</span>
            <span class="n">possibleActions</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span> <span class="p">)</span>
        <span class="k">if</span> <span class="n">reverse</span> <span class="ow">in</span> <span class="n">possibleActions</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span> <span class="n">possibleActions</span> <span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">possibleActions</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span> <span class="n">reverse</span> <span class="p">)</span>
        <span class="k">return</span> <span class="n">possibleActions</span>
    <span class="n">getLegalActions</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">getLegalActions</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">applyAction</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">action</span><span class="p">,</span> <span class="n">ghostIndex</span><span class="p">):</span>

        <span class="n">legal</span> <span class="o">=</span> <span class="n">GhostRules</span><span class="o">.</span><span class="n">getLegalActions</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">ghostIndex</span> <span class="p">)</span>
        <span class="k">if</span> <span class="n">action</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">legal</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;Illegal ghost action &quot;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">action</span><span class="p">))</span>

        <span class="n">ghostState</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">ghostIndex</span><span class="p">]</span>
        <span class="n">speed</span> <span class="o">=</span> <span class="n">GhostRules</span><span class="o">.</span><span class="n">GHOST_SPEED</span>
        <span class="k">if</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span> <span class="n">speed</span> <span class="o">/=</span> <span class="mf">2.0</span>
        <span class="n">vector</span> <span class="o">=</span> <span class="n">Actions</span><span class="o">.</span><span class="n">directionToVector</span><span class="p">(</span> <span class="n">action</span><span class="p">,</span> <span class="n">speed</span> <span class="p">)</span>
        <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span> <span class="o">=</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span> <span class="n">vector</span> <span class="p">)</span>
    <span class="n">applyAction</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">applyAction</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">decrementTimer</span><span class="p">(</span> <span class="n">ghostState</span><span class="p">):</span>
        <span class="n">timer</span> <span class="o">=</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">scaredTimer</span>
        <span class="k">if</span> <span class="n">timer</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">pos</span> <span class="o">=</span> <span class="n">nearestPoint</span><span class="p">(</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">pos</span> <span class="p">)</span>
        <span class="n">ghostState</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span> <span class="mi">0</span><span class="p">,</span> <span class="n">timer</span> <span class="o">-</span> <span class="mi">1</span> <span class="p">)</span>
    <span class="n">decrementTimer</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">decrementTimer</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">checkDeath</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="n">pacmanPosition</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">getPacmanPosition</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">agentIndex</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c"># Pacman just moved; Anyone can kill him</span>
            <span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span> <span class="p">)</span> <span class="p">):</span>
                <span class="n">ghostState</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">index</span><span class="p">]</span>
                <span class="n">ghostPosition</span> <span class="o">=</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span>
                <span class="k">if</span> <span class="n">GhostRules</span><span class="o">.</span><span class="n">canKill</span><span class="p">(</span> <span class="n">pacmanPosition</span><span class="p">,</span> <span class="n">ghostPosition</span> <span class="p">):</span>
                    <span class="n">GhostRules</span><span class="o">.</span><span class="n">collide</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">ghostState</span><span class="p">,</span> <span class="n">index</span> <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">ghostState</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">agentStates</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span>
            <span class="n">ghostPosition</span> <span class="o">=</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span><span class="o">.</span><span class="n">getPosition</span><span class="p">()</span>
            <span class="k">if</span> <span class="n">GhostRules</span><span class="o">.</span><span class="n">canKill</span><span class="p">(</span> <span class="n">pacmanPosition</span><span class="p">,</span> <span class="n">ghostPosition</span> <span class="p">):</span>
                <span class="n">GhostRules</span><span class="o">.</span><span class="n">collide</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">ghostState</span><span class="p">,</span> <span class="n">agentIndex</span> <span class="p">)</span>
    <span class="n">checkDeath</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">checkDeath</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">collide</span><span class="p">(</span> <span class="n">state</span><span class="p">,</span> <span class="n">ghostState</span><span class="p">,</span> <span class="n">agentIndex</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">+=</span> <span class="mi">200</span>
            <span class="n">GhostRules</span><span class="o">.</span><span class="n">placeGhost</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">ghostState</span><span class="p">)</span>
            <span class="n">ghostState</span><span class="o">.</span><span class="n">scaredTimer</span> <span class="o">=</span> <span class="mi">0</span>
            <span class="c"># Added for first-person</span>
            <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_eaten</span><span class="p">[</span><span class="n">agentIndex</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_win</span><span class="p">:</span>
                <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">scoreChange</span> <span class="o">-=</span> <span class="mi">500</span>
                <span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">_lose</span> <span class="o">=</span> <span class="bp">True</span>
    <span class="n">collide</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">collide</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">canKill</span><span class="p">(</span> <span class="n">pacmanPosition</span><span class="p">,</span> <span class="n">ghostPosition</span> <span class="p">):</span>
        <span class="k">return</span> <span class="n">manhattanDistance</span><span class="p">(</span> <span class="n">ghostPosition</span><span class="p">,</span> <span class="n">pacmanPosition</span> <span class="p">)</span> <span class="o">&lt;=</span> <span class="n">COLLISION_TOLERANCE</span>
    <span class="n">canKill</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">canKill</span> <span class="p">)</span>

    <span class="k">def</span> <span class="nf">placeGhost</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">ghostState</span><span class="p">):</span>
        <span class="n">ghostState</span><span class="o">.</span><span class="n">configuration</span> <span class="o">=</span> <span class="n">ghostState</span><span class="o">.</span><span class="n">start</span>
    <span class="n">placeGhost</span> <span class="o">=</span> <span class="nb">staticmethod</span><span class="p">(</span> <span class="n">placeGhost</span> <span class="p">)</span>

<span class="c">#############################</span>
<span class="c"># FRAMEWORK TO START A GAME #</span>
<span class="c">#############################</span>

<span class="k">def</span> <span class="nf">default</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">str</span> <span class="o">+</span> <span class="s">&#39; [Default: </span><span class="si">%d</span><span class="s">efault]&#39;</span>

<span class="k">def</span> <span class="nf">parseAgentArgs</span><span class="p">(</span><span class="nb">str</span><span class="p">):</span>
    <span class="k">if</span> <span class="nb">str</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span> <span class="p">{}</span>
    <span class="n">pieces</span> <span class="o">=</span> <span class="nb">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;,&#39;</span><span class="p">)</span>
    <span class="n">opts</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">pieces</span><span class="p">:</span>
        <span class="k">if</span> <span class="s">&#39;=&#39;</span> <span class="ow">in</span> <span class="n">p</span><span class="p">:</span>
            <span class="n">key</span><span class="p">,</span> <span class="n">val</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">key</span><span class="p">,</span><span class="n">val</span> <span class="o">=</span> <span class="n">p</span><span class="p">,</span> <span class="mi">1</span>
        <span class="n">opts</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">val</span>
    <span class="k">return</span> <span class="n">opts</span>

<span class="k">def</span> <span class="nf">readCommand</span><span class="p">(</span> <span class="n">argv</span> <span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Processes the command used to run pacman from the command line.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="kn">from</span> <span class="nn">optparse</span> <span class="kn">import</span> <span class="n">OptionParser</span>
    <span class="n">usageStr</span> <span class="o">=</span> <span class="s">&quot;&quot;&quot;</span>
<span class="s">    USAGE:      python pacman.py &lt;options&gt;</span>
<span class="s">    EXAMPLES:   (1) python pacman.py</span>
<span class="s">                    - starts an interactive game</span>
<span class="s">                (2) python pacman.py --layout smallClassic --zoom 2</span>
<span class="s">                OR  python pacman.py -l smallClassic -z 2</span>
<span class="s">                    - starts an interactive game on a smaller board, zoomed in</span>
<span class="s">    &quot;&quot;&quot;</span>
    <span class="n">parser</span> <span class="o">=</span> <span class="n">OptionParser</span><span class="p">(</span><span class="n">usageStr</span><span class="p">)</span>

    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-n&#39;</span><span class="p">,</span> <span class="s">&#39;--numGames&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;numGames&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;int&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;the number of GAMES to play&#39;</span><span class="p">),</span> <span class="n">metavar</span><span class="o">=</span><span class="s">&#39;GAMES&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-l&#39;</span><span class="p">,</span> <span class="s">&#39;--layout&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;layout&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;the LAYOUT_FILE from which to load the map layout&#39;</span><span class="p">),</span>
                      <span class="n">metavar</span><span class="o">=</span><span class="s">&#39;LAYOUT_FILE&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s">&#39;mediumClassic&#39;</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-p&#39;</span><span class="p">,</span> <span class="s">&#39;--pacman&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;pacman&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;the agent TYPE in the pacmanAgents module to use&#39;</span><span class="p">),</span>
                      <span class="n">metavar</span><span class="o">=</span><span class="s">&#39;TYPE&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s">&#39;KeyboardAgent&#39;</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-t&#39;</span><span class="p">,</span> <span class="s">&#39;--textGraphics&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;textGraphics&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;Display output as text only&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-q&#39;</span><span class="p">,</span> <span class="s">&#39;--quietTextGraphics&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;quietGraphics&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;Generate minimal output and no graphics&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-g&#39;</span><span class="p">,</span> <span class="s">&#39;--ghosts&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;ghost&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;the ghost agent TYPE in the ghostAgents module to use&#39;</span><span class="p">),</span>
                      <span class="n">metavar</span> <span class="o">=</span> <span class="s">&#39;TYPE&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="s">&#39;RandomGhost&#39;</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-k&#39;</span><span class="p">,</span> <span class="s">&#39;--numghosts&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;int&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;numGhosts&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;The maximum number of ghosts to use&#39;</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-z&#39;</span><span class="p">,</span> <span class="s">&#39;--zoom&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;float&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;zoom&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;Zoom the size of the graphics window&#39;</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="mf">1.0</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-f&#39;</span><span class="p">,</span> <span class="s">&#39;--fixRandomSeed&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;fixRandomSeed&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;Fixes the random seed to always play the same game&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-r&#39;</span><span class="p">,</span> <span class="s">&#39;--recordActions&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;record&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;Writes game histories to a file (named by the time they were played)&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;--replay&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;gameToReplay&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;A recorded game file (pickle) to replay&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-a&#39;</span><span class="p">,</span><span class="s">&#39;--agentArgs&#39;</span><span class="p">,</span><span class="n">dest</span><span class="o">=</span><span class="s">&#39;agentArgs&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;Comma separated values sent to agent. e.g. &quot;opt1=val1,opt2,opt3=val3&quot;&#39;</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-x&#39;</span><span class="p">,</span> <span class="s">&#39;--numTraining&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;numTraining&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;int&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;How many episodes are training (suppresses output)&#39;</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;--frameTime&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;frameTime&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;float&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;Time to delay between frames; &lt;0 means keyboard&#39;</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="mf">0.1</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;-c&#39;</span><span class="p">,</span> <span class="s">&#39;--catchExceptions&#39;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s">&#39;store_true&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;catchExceptions&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="s">&#39;Turns on exception handling and timeouts during games&#39;</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
    <span class="n">parser</span><span class="o">.</span><span class="n">add_option</span><span class="p">(</span><span class="s">&#39;--timeout&#39;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s">&#39;timeout&#39;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="s">&#39;int&#39;</span><span class="p">,</span>
                      <span class="n">help</span><span class="o">=</span><span class="n">default</span><span class="p">(</span><span class="s">&#39;Maximum length of time an agent can spend computing in a single game&#39;</span><span class="p">),</span> <span class="n">default</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>

    <span class="n">options</span><span class="p">,</span> <span class="n">otherjunk</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">(</span><span class="n">argv</span><span class="p">)</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">otherjunk</span><span class="p">)</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Command line input not understood: &#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">otherjunk</span><span class="p">))</span>
    <span class="n">args</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span>

    <span class="c"># Fix the random seed</span>
    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">fixRandomSeed</span><span class="p">:</span> <span class="n">random</span><span class="o">.</span><span class="n">seed</span><span class="p">(</span><span class="s">&#39;cs188&#39;</span><span class="p">)</span>

    <span class="c"># Choose a layout</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;layout&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">layout</span><span class="o">.</span><span class="n">getLayout</span><span class="p">(</span> <span class="n">options</span><span class="o">.</span><span class="n">layout</span> <span class="p">)</span>
    <span class="k">if</span> <span class="n">args</span><span class="p">[</span><span class="s">&#39;layout&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&quot;The layout &quot;</span> <span class="o">+</span> <span class="n">options</span><span class="o">.</span><span class="n">layout</span> <span class="o">+</span> <span class="s">&quot; cannot be found&quot;</span><span class="p">)</span>

    <span class="c"># Choose a Pacman agent</span>
    <span class="n">noKeyboard</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">gameToReplay</span> <span class="o">==</span> <span class="bp">None</span> <span class="ow">and</span> <span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">textGraphics</span> <span class="ow">or</span> <span class="n">options</span><span class="o">.</span><span class="n">quietGraphics</span><span class="p">)</span>
    <span class="n">pacmanType</span> <span class="o">=</span> <span class="n">loadAgent</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">pacman</span><span class="p">,</span> <span class="n">noKeyboard</span><span class="p">)</span>
    <span class="n">agentOpts</span> <span class="o">=</span> <span class="n">parseAgentArgs</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">agentArgs</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">numTraining</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">args</span><span class="p">[</span><span class="s">&#39;numTraining&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">numTraining</span>
        <span class="k">if</span> <span class="s">&#39;numTraining&#39;</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">agentOpts</span><span class="p">:</span> <span class="n">agentOpts</span><span class="p">[</span><span class="s">&#39;numTraining&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">numTraining</span>
    <span class="n">pacman</span> <span class="o">=</span> <span class="n">pacmanType</span><span class="p">(</span><span class="o">**</span><span class="n">agentOpts</span><span class="p">)</span> <span class="c"># Instantiate Pacman with agentArgs</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;pacman&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pacman</span>

    <span class="c"># Don&#39;t display training games</span>
    <span class="k">if</span> <span class="s">&#39;numTrain&#39;</span> <span class="ow">in</span> <span class="n">agentOpts</span><span class="p">:</span>
        <span class="n">options</span><span class="o">.</span><span class="n">numQuiet</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">agentOpts</span><span class="p">[</span><span class="s">&#39;numTrain&#39;</span><span class="p">])</span>
        <span class="n">options</span><span class="o">.</span><span class="n">numIgnore</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">agentOpts</span><span class="p">[</span><span class="s">&#39;numTrain&#39;</span><span class="p">])</span>

    <span class="c"># Choose a ghost agent</span>
    <span class="n">ghostType</span> <span class="o">=</span> <span class="n">loadAgent</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">ghost</span><span class="p">,</span> <span class="n">noKeyboard</span><span class="p">)</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;ghosts&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">ghostType</span><span class="p">(</span> <span class="n">i</span><span class="o">+</span><span class="mi">1</span> <span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span> <span class="n">options</span><span class="o">.</span><span class="n">numGhosts</span> <span class="p">)]</span>

    <span class="c"># Choose a display format</span>
    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">quietGraphics</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">textDisplay</span>
        <span class="n">args</span><span class="p">[</span><span class="s">&#39;display&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">textDisplay</span><span class="o">.</span><span class="n">NullGraphics</span><span class="p">()</span>
    <span class="k">elif</span> <span class="n">options</span><span class="o">.</span><span class="n">textGraphics</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">textDisplay</span>
        <span class="n">textDisplay</span><span class="o">.</span><span class="n">SLEEP_TIME</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">frameTime</span>
        <span class="n">args</span><span class="p">[</span><span class="s">&#39;display&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">textDisplay</span><span class="o">.</span><span class="n">PacmanGraphics</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="kn">import</span> <span class="nn">graphicsDisplay</span>
        <span class="n">args</span><span class="p">[</span><span class="s">&#39;display&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">graphicsDisplay</span><span class="o">.</span><span class="n">PacmanGraphics</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">zoom</span><span class="p">,</span> <span class="n">frameTime</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">frameTime</span><span class="p">)</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;numGames&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">numGames</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;record&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">record</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;catchExceptions&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">catchExceptions</span>
    <span class="n">args</span><span class="p">[</span><span class="s">&#39;timeout&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">options</span><span class="o">.</span><span class="n">timeout</span>

    <span class="c"># Special case: recorded games don&#39;t use the runGames method or args structure</span>
    <span class="k">if</span> <span class="n">options</span><span class="o">.</span><span class="n">gameToReplay</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
        <span class="k">print</span> <span class="s">&#39;Replaying recorded game </span><span class="si">%s</span><span class="s">.&#39;</span> <span class="o">%</span> <span class="n">options</span><span class="o">.</span><span class="n">gameToReplay</span>
        <span class="kn">import</span> <span class="nn">cPickle</span>
        <span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">options</span><span class="o">.</span><span class="n">gameToReplay</span><span class="p">)</span>
        <span class="k">try</span><span class="p">:</span> <span class="n">recorded</span> <span class="o">=</span> <span class="n">cPickle</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
        <span class="k">finally</span><span class="p">:</span> <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="n">recorded</span><span class="p">[</span><span class="s">&#39;display&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">args</span><span class="p">[</span><span class="s">&#39;display&#39;</span><span class="p">]</span>
        <span class="n">replayGame</span><span class="p">(</span><span class="o">**</span><span class="n">recorded</span><span class="p">)</span>
        <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">args</span>

<span class="k">def</span> <span class="nf">loadAgent</span><span class="p">(</span><span class="n">pacman</span><span class="p">,</span> <span class="n">nographics</span><span class="p">):</span>
    <span class="c"># Looks through all pythonPath Directories for the right module,</span>
    <span class="n">pythonPathStr</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">expandvars</span><span class="p">(</span><span class="s">&quot;$PYTHONPATH&quot;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">pythonPathStr</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">:</span>
        <span class="n">pythonPathDirs</span> <span class="o">=</span> <span class="n">pythonPathStr</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;:&#39;</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">pythonPathDirs</span> <span class="o">=</span> <span class="n">pythonPathStr</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)</span>
    <span class="n">pythonPathDirs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">moduleDir</span> <span class="ow">in</span> <span class="n">pythonPathDirs</span><span class="p">:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="n">moduleDir</span><span class="p">):</span> <span class="k">continue</span>
        <span class="n">moduleNames</span> <span class="o">=</span> <span class="p">[</span><span class="n">f</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="n">moduleDir</span><span class="p">)</span> <span class="k">if</span> <span class="n">f</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;gents.py&#39;</span><span class="p">)]</span>
        <span class="k">for</span> <span class="n">modulename</span> <span class="ow">in</span> <span class="n">moduleNames</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">module</span> <span class="o">=</span> <span class="nb">__import__</span><span class="p">(</span><span class="n">modulename</span><span class="p">[:</span><span class="o">-</span><span class="mi">3</span><span class="p">])</span>
            <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span>
                <span class="k">continue</span>
            <span class="k">if</span> <span class="n">pacman</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">module</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">nographics</span> <span class="ow">and</span> <span class="n">modulename</span> <span class="o">==</span> <span class="s">&#39;keyboardAgents.py&#39;</span><span class="p">:</span>
                    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;Using the keyboard requires graphics (not text display)&#39;</span><span class="p">)</span>
                <span class="k">return</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">module</span><span class="p">,</span> <span class="n">pacman</span><span class="p">)</span>
    <span class="k">raise</span> <span class="ne">Exception</span><span class="p">(</span><span class="s">&#39;The agent &#39;</span> <span class="o">+</span> <span class="n">pacman</span> <span class="o">+</span> <span class="s">&#39; is not specified in any *Agents.py.&#39;</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">replayGame</span><span class="p">(</span> <span class="n">layout</span><span class="p">,</span> <span class="n">actions</span><span class="p">,</span> <span class="n">display</span> <span class="p">):</span>
    <span class="kn">import</span> <span class="nn">pacmanAgents</span><span class="o">,</span> <span class="nn">ghostAgents</span>
    <span class="n">rules</span> <span class="o">=</span> <span class="n">ClassicGameRules</span><span class="p">()</span>
    <span class="n">agents</span> <span class="o">=</span> <span class="p">[</span><span class="n">pacmanAgents</span><span class="o">.</span><span class="n">GreedyAgent</span><span class="p">()]</span> <span class="o">+</span> <span class="p">[</span><span class="n">ghostAgents</span><span class="o">.</span><span class="n">RandomGhost</span><span class="p">(</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">layout</span><span class="o">.</span><span class="n">getNumGhosts</span><span class="p">())]</span>
    <span class="n">game</span> <span class="o">=</span> <span class="n">rules</span><span class="o">.</span><span class="n">newGame</span><span class="p">(</span> <span class="n">layout</span><span class="p">,</span> <span class="n">agents</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">agents</span><span class="p">[</span><span class="mi">1</span><span class="p">:],</span> <span class="n">display</span> <span class="p">)</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">game</span><span class="o">.</span><span class="n">state</span>
    <span class="n">display</span><span class="o">.</span><span class="n">initialize</span><span class="p">(</span><span class="n">state</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>

    <span class="k">for</span> <span class="n">action</span> <span class="ow">in</span> <span class="n">actions</span><span class="p">:</span>
            <span class="c"># Execute the action</span>
        <span class="n">state</span> <span class="o">=</span> <span class="n">state</span><span class="o">.</span><span class="n">generateSuccessor</span><span class="p">(</span> <span class="o">*</span><span class="n">action</span> <span class="p">)</span>
        <span class="c"># Change the display</span>
        <span class="n">display</span><span class="o">.</span><span class="n">update</span><span class="p">(</span> <span class="n">state</span><span class="o">.</span><span class="n">data</span> <span class="p">)</span>
        <span class="c"># Allow for game specific conditions (winning, losing, etc.)</span>
        <span class="n">rules</span><span class="o">.</span><span class="n">process</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">game</span><span class="p">)</span>

    <span class="n">display</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">runGames</span><span class="p">(</span> <span class="n">layout</span><span class="p">,</span> <span class="n">pacman</span><span class="p">,</span> <span class="n">ghosts</span><span class="p">,</span> <span class="n">display</span><span class="p">,</span> <span class="n">numGames</span><span class="p">,</span> <span class="n">record</span><span class="p">,</span> <span class="n">numTraining</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">catchExceptions</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">30</span> <span class="p">):</span>
    <span class="kn">import</span> <span class="nn">__main__</span>
    <span class="n">__main__</span><span class="o">.</span><span class="n">__dict__</span><span class="p">[</span><span class="s">&#39;_display&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">display</span>

    <span class="n">rules</span> <span class="o">=</span> <span class="n">ClassicGameRules</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
    <span class="n">games</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span> <span class="n">numGames</span> <span class="p">):</span>
        <span class="n">beQuiet</span> <span class="o">=</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">numTraining</span>
        <span class="k">if</span> <span class="n">beQuiet</span><span class="p">:</span>
                <span class="c"># Suppress output and graphics</span>
            <span class="kn">import</span> <span class="nn">textDisplay</span>
            <span class="n">gameDisplay</span> <span class="o">=</span> <span class="n">textDisplay</span><span class="o">.</span><span class="n">NullGraphics</span><span class="p">()</span>
            <span class="n">rules</span><span class="o">.</span><span class="n">quiet</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">gameDisplay</span> <span class="o">=</span> <span class="n">display</span>
            <span class="n">rules</span><span class="o">.</span><span class="n">quiet</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="n">game</span> <span class="o">=</span> <span class="n">rules</span><span class="o">.</span><span class="n">newGame</span><span class="p">(</span> <span class="n">layout</span><span class="p">,</span> <span class="n">pacman</span><span class="p">,</span> <span class="n">ghosts</span><span class="p">,</span> <span class="n">gameDisplay</span><span class="p">,</span> <span class="n">beQuiet</span><span class="p">,</span> <span class="n">catchExceptions</span><span class="p">)</span>
        <span class="n">game</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">beQuiet</span><span class="p">:</span> <span class="n">games</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">game</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">record</span><span class="p">:</span>
            <span class="kn">import</span> <span class="nn">time</span><span class="o">,</span> <span class="nn">cPickle</span>
            <span class="n">fname</span> <span class="o">=</span> <span class="p">(</span><span class="s">&#39;recorded-game-</span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">))</span> <span class="o">+</span>  <span class="s">&#39;-&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">t</span><span class="p">)</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">time</span><span class="o">.</span><span class="n">localtime</span><span class="p">()[</span><span class="mi">1</span><span class="p">:</span><span class="mi">6</span><span class="p">]])</span>
            <span class="n">f</span> <span class="o">=</span> <span class="nb">file</span><span class="p">(</span><span class="n">fname</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span>
            <span class="n">components</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;layout&#39;</span><span class="p">:</span> <span class="n">layout</span><span class="p">,</span> <span class="s">&#39;actions&#39;</span><span class="p">:</span> <span class="n">game</span><span class="o">.</span><span class="n">moveHistory</span><span class="p">}</span>
            <span class="n">cPickle</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">components</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span>
            <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="k">if</span> <span class="p">(</span><span class="n">numGames</span><span class="o">-</span><span class="n">numTraining</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">scores</span> <span class="o">=</span> <span class="p">[</span><span class="n">game</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">getScore</span><span class="p">()</span> <span class="k">for</span> <span class="n">game</span> <span class="ow">in</span> <span class="n">games</span><span class="p">]</span>
        <span class="n">wins</span> <span class="o">=</span> <span class="p">[</span><span class="n">game</span><span class="o">.</span><span class="n">state</span><span class="o">.</span><span class="n">isWin</span><span class="p">()</span> <span class="k">for</span> <span class="n">game</span> <span class="ow">in</span> <span class="n">games</span><span class="p">]</span>
        <span class="n">winRate</span> <span class="o">=</span> <span class="n">wins</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="bp">True</span><span class="p">)</span><span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">wins</span><span class="p">))</span>
        <span class="k">print</span> <span class="s">&#39;Average Score:&#39;</span><span class="p">,</span> <span class="nb">sum</span><span class="p">(</span><span class="n">scores</span><span class="p">)</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">scores</span><span class="p">))</span>
        <span class="k">print</span> <span class="s">&#39;Scores:       &#39;</span><span class="p">,</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">score</span><span class="p">)</span> <span class="k">for</span> <span class="n">score</span> <span class="ow">in</span> <span class="n">scores</span><span class="p">])</span>
        <span class="k">print</span> <span class="s">&#39;Win Rate:      </span><span class="si">%d</span><span class="s">/</span><span class="si">%d</span><span class="s"> (</span><span class="si">%.2f</span><span class="s">)&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">wins</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="bp">True</span><span class="p">),</span> <span class="nb">len</span><span class="p">(</span><span class="n">wins</span><span class="p">),</span> <span class="n">winRate</span><span class="p">)</span>
        <span class="k">print</span> <span class="s">&#39;Record:       &#39;</span><span class="p">,</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">([</span> <span class="p">[</span><span class="s">&#39;Loss&#39;</span><span class="p">,</span> <span class="s">&#39;Win&#39;</span><span class="p">][</span><span class="nb">int</span><span class="p">(</span><span class="n">w</span><span class="p">)]</span> <span class="k">for</span> <span class="n">w</span> <span class="ow">in</span> <span class="n">wins</span><span class="p">])</span>

    <span class="k">return</span> <span class="n">games</span>

<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    The main function called when pacman.py is run</span>
<span class="sd">    from the command line:</span>

<span class="sd">    &gt; python pacman.py</span>

<span class="sd">    See the usage string for more details.</span>

<span class="sd">    &gt; python pacman.py --help</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">args</span> <span class="o">=</span> <span class="n">readCommand</span><span class="p">(</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span> <span class="p">)</span> <span class="c"># Get game components based on input</span>
    <span class="n">runGames</span><span class="p">(</span> <span class="o">**</span><span class="n">args</span> <span class="p">)</span>

    <span class="c"># import cProfile</span>
    <span class="c"># cProfile.run(&quot;runGames( **args )&quot;)</span>
    <span class="k">pass</span>
</pre></div>
</body>
</html>
