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

<div class="highlight"><pre><span class="c"># layout.py</span>
<span class="c"># ---------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="kn">from</span> <span class="nn">util</span> <span class="kn">import</span> <span class="n">manhattanDistance</span>
<span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Grid</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">random</span>

<span class="n">VISIBILITY_MATRIX_CACHE</span> <span class="o">=</span> <span class="p">{}</span>

<span class="k">class</span> <span class="nc">Layout</span><span class="p">:</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    A Layout manages the static information about the game board.</span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">layoutText</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">layoutText</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">layoutText</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">walls</span> <span class="o">=</span> <span class="n">Grid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">food</span> <span class="o">=</span> <span class="n">Grid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">,</span> <span class="bp">False</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">capsules</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">numGhosts</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">processLayoutText</span><span class="p">(</span><span class="n">layoutText</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">layoutText</span> <span class="o">=</span> <span class="n">layoutText</span>
        <span class="c"># self.initializeVisibilityMatrix()</span>

    <span class="k">def</span> <span class="nf">getNumGhosts</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">numGhosts</span>

    <span class="k">def</span> <span class="nf">initializeVisibilityMatrix</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">global</span> <span class="n">VISIBILITY_MATRIX_CACHE</span>
        <span class="k">if</span> <span class="nb">reduce</span><span class="p">(</span><span class="nb">str</span><span class="o">.</span><span class="n">__add__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">layoutText</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">VISIBILITY_MATRIX_CACHE</span><span class="p">:</span>
            <span class="kn">from</span> <span class="nn">game</span> <span class="kn">import</span> <span class="n">Directions</span>
            <span class="n">vecs</span> <span class="o">=</span> <span class="p">[(</span><span class="o">-</span><span class="mf">0.5</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span> <span class="p">(</span><span class="mf">0.5</span><span class="p">,</span><span class="mi">0</span><span class="p">),(</span><span class="mi">0</span><span class="p">,</span><span class="o">-</span><span class="mf">0.5</span><span class="p">),(</span><span class="mi">0</span><span class="p">,</span><span class="mf">0.5</span><span class="p">)]</span>
            <span class="n">dirs</span> <span class="o">=</span> <span class="p">[</span><span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">,</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">]</span>
            <span class="n">vis</span> <span class="o">=</span> <span class="n">Grid</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">,</span> <span class="p">{</span><span class="n">Directions</span><span class="o">.</span><span class="n">NORTH</span><span class="p">:</span><span class="nb">set</span><span class="p">(),</span> <span class="n">Directions</span><span class="o">.</span><span class="n">SOUTH</span><span class="p">:</span><span class="nb">set</span><span class="p">(),</span> <span class="n">Directions</span><span class="o">.</span><span class="n">EAST</span><span class="p">:</span><span class="nb">set</span><span class="p">(),</span> <span class="n">Directions</span><span class="o">.</span><span class="n">WEST</span><span class="p">:</span><span class="nb">set</span><span class="p">(),</span> <span class="n">Directions</span><span class="o">.</span><span class="n">STOP</span><span class="p">:</span><span class="nb">set</span><span class="p">()})</span>
            <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">):</span>
                <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">):</span>
                    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">==</span> <span class="bp">False</span><span class="p">:</span>
                        <span class="k">for</span> <span class="n">vec</span><span class="p">,</span> <span class="n">direction</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">vecs</span><span class="p">,</span> <span class="n">dirs</span><span class="p">):</span>
                            <span class="n">dx</span><span class="p">,</span> <span class="n">dy</span> <span class="o">=</span> <span class="n">vec</span>
                            <span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span> <span class="o">=</span> <span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">dy</span>
                            <span class="k">while</span> <span class="p">(</span><span class="n">nextx</span> <span class="o">+</span> <span class="n">nexty</span><span class="p">)</span> <span class="o">!=</span> <span class="nb">int</span><span class="p">(</span><span class="n">nextx</span><span class="p">)</span> <span class="o">+</span> <span class="nb">int</span><span class="p">(</span><span class="n">nexty</span><span class="p">)</span> <span class="ow">or</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">nextx</span><span class="p">)][</span><span class="nb">int</span><span class="p">(</span><span class="n">nexty</span><span class="p">)]</span> <span class="p">:</span>
                                <span class="n">vis</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">][</span><span class="n">direction</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span><span class="p">))</span>
                                <span class="n">nextx</span><span class="p">,</span> <span class="n">nexty</span> <span class="o">=</span> <span class="n">x</span> <span class="o">+</span> <span class="n">dx</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">dy</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">visibility</span> <span class="o">=</span> <span class="n">vis</span>
            <span class="n">VISIBILITY_MATRIX_CACHE</span><span class="p">[</span><span class="nb">reduce</span><span class="p">(</span><span class="nb">str</span><span class="o">.</span><span class="n">__add__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">layoutText</span><span class="p">)]</span> <span class="o">=</span> <span class="n">vis</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">visibility</span> <span class="o">=</span> <span class="n">VISIBILITY_MATRIX_CACHE</span><span class="p">[</span><span class="nb">reduce</span><span class="p">(</span><span class="nb">str</span><span class="o">.</span><span class="n">__add__</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">layoutText</span><span class="p">)]</span>

    <span class="k">def</span> <span class="nf">isWall</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pos</span><span class="p">):</span>
        <span class="n">x</span><span class="p">,</span> <span class="n">col</span> <span class="o">=</span> <span class="n">pos</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">col</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">getRandomLegalPosition</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">x</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">))</span>
        <span class="n">y</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">))</span>
        <span class="k">while</span> <span class="bp">self</span><span class="o">.</span><span class="n">isWall</span><span class="p">(</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span> <span class="p">):</span>
            <span class="n">x</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">))</span>
            <span class="n">y</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">))</span>
        <span class="k">return</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getRandomCorner</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="n">poses</span> <span class="o">=</span> <span class="p">[(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="mi">2</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)]</span>
        <span class="k">return</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">poses</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">getFurthestCorner</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">pacPos</span><span class="p">):</span>
        <span class="n">poses</span> <span class="o">=</span> <span class="p">[(</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="mi">2</span><span class="p">),</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span> <span class="o">-</span> <span class="mi">2</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="mi">2</span><span class="p">)]</span>
        <span class="n">dist</span><span class="p">,</span> <span class="n">pos</span> <span class="o">=</span> <span class="nb">max</span><span class="p">([(</span><span class="n">manhattanDistance</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">pacPos</span><span class="p">),</span> <span class="n">p</span><span class="p">)</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">poses</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">pos</span>

    <span class="k">def</span> <span class="nf">isVisibleFrom</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ghostPos</span><span class="p">,</span> <span class="n">pacPos</span><span class="p">,</span> <span class="n">pacDirection</span><span class="p">):</span>
        <span class="n">row</span><span class="p">,</span> <span class="n">col</span> <span class="o">=</span> <span class="p">[</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">pacPos</span><span class="p">]</span>
        <span class="k">return</span> <span class="n">ghostPos</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">visibility</span><span class="p">[</span><span class="n">row</span><span class="p">][</span><span class="n">col</span><span class="p">][</span><span class="n">pacDirection</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">layoutText</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">deepCopy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">Layout</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">layoutText</span><span class="p">[:])</span>

    <span class="k">def</span> <span class="nf">processLayoutText</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">layoutText</span><span class="p">):</span>
        <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">        Coordinates are flipped from the input format to the (x,y) convention here</span>

<span class="sd">        The shape of the maze.  Each character</span>
<span class="sd">        represents a different type of object.</span>
<span class="sd">         % - Wall</span>
<span class="sd">         . - Food</span>
<span class="sd">         o - Capsule</span>
<span class="sd">         G - Ghost</span>
<span class="sd">         P - Pacman</span>
<span class="sd">        Other characters are ignored.</span>
<span class="sd">        &quot;&quot;&quot;</span>
        <span class="n">maxY</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">height</span> <span class="o">-</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">y</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">height</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">width</span><span class="p">):</span>
                <span class="n">layoutChar</span> <span class="o">=</span> <span class="n">layoutText</span><span class="p">[</span><span class="n">maxY</span> <span class="o">-</span> <span class="n">y</span><span class="p">][</span><span class="n">x</span><span class="p">]</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">processLayoutChar</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">layoutChar</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span> <span class="o">=</span> <span class="p">[</span> <span class="p">(</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">0</span><span class="p">,</span> <span class="n">pos</span><span class="p">)</span> <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">pos</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">processLayoutChar</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">layoutChar</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">layoutChar</span> <span class="o">==</span> <span class="s">&#39;%&#39;</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">walls</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="k">elif</span> <span class="n">layoutChar</span> <span class="o">==</span> <span class="s">&#39;.&#39;</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">food</span><span class="p">[</span><span class="n">x</span><span class="p">][</span><span class="n">y</span><span class="p">]</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="k">elif</span> <span class="n">layoutChar</span> <span class="o">==</span> <span class="s">&#39;o&#39;</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">capsules</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">))</span>
        <span class="k">elif</span> <span class="n">layoutChar</span> <span class="o">==</span> <span class="s">&#39;P&#39;</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
        <span class="k">elif</span> <span class="n">layoutChar</span> <span class="ow">in</span> <span class="p">[</span><span class="s">&#39;G&#39;</span><span class="p">]:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span> <span class="p">)</span> <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">numGhosts</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">elif</span> <span class="n">layoutChar</span> <span class="ow">in</span>  <span class="p">[</span><span class="s">&#39;1&#39;</span><span class="p">,</span> <span class="s">&#39;2&#39;</span><span class="p">,</span> <span class="s">&#39;3&#39;</span><span class="p">,</span> <span class="s">&#39;4&#39;</span><span class="p">]:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">agentPositions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">layoutChar</span><span class="p">),</span> <span class="p">(</span><span class="n">x</span><span class="p">,</span><span class="n">y</span><span class="p">)))</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">numGhosts</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="k">def</span> <span class="nf">getLayout</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">back</span> <span class="o">=</span> <span class="mi">2</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">name</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;.lay&#39;</span><span class="p">):</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="n">tryToLoad</span><span class="p">(</span><span class="s">&#39;layouts/&#39;</span> <span class="o">+</span> <span class="n">name</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">layout</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="n">layout</span> <span class="o">=</span> <span class="n">tryToLoad</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="n">tryToLoad</span><span class="p">(</span><span class="s">&#39;layouts/&#39;</span> <span class="o">+</span> <span class="n">name</span> <span class="o">+</span> <span class="s">&#39;.lay&#39;</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">layout</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="n">layout</span> <span class="o">=</span> <span class="n">tryToLoad</span><span class="p">(</span><span class="n">name</span> <span class="o">+</span> <span class="s">&#39;.lay&#39;</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">layout</span> <span class="o">==</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">back</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">curdir</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s">&#39;.&#39;</span><span class="p">)</span>
        <span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="s">&#39;..&#39;</span><span class="p">)</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="n">getLayout</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">back</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
        <span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="n">curdir</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">layout</span>

<span class="k">def</span> <span class="nf">tryToLoad</span><span class="p">(</span><span class="n">fullname</span><span class="p">):</span>
    <span class="k">if</span><span class="p">(</span><span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">fullname</span><span class="p">)):</span> <span class="k">return</span> <span class="bp">None</span>
    <span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">fullname</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span> <span class="k">return</span> <span class="n">Layout</span><span class="p">([</span><span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">f</span><span class="p">])</span>
    <span class="k">finally</span><span class="p">:</span> <span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</pre></div>
</body>
</html>
