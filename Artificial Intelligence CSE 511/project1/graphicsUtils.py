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

<div class="highlight"><pre><span class="c"># graphicsUtils.py</span>
<span class="c"># ----------------</span>
<span class="c"># Licensing Information: Please do not distribute or publish solutions to this</span>
<span class="c"># project. You are free to use and extend these projects for educational</span>
<span class="c"># purposes. The Pacman AI projects were developed at UC Berkeley, primarily by</span>
<span class="c"># John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).</span>
<span class="c"># For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html</span>

<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">math</span>
<span class="kn">import</span> <span class="nn">random</span>
<span class="kn">import</span> <span class="nn">string</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="kn">import</span> <span class="nn">types</span>
<span class="kn">import</span> <span class="nn">Tkinter</span>

<span class="n">_Windows</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s">&#39;win32&#39;</span>  <span class="c"># True if on Win95/98/NT</span>

<span class="n">_root_window</span> <span class="o">=</span> <span class="bp">None</span>      <span class="c"># The root window for graphics output</span>
<span class="n">_canvas</span> <span class="o">=</span> <span class="bp">None</span>      <span class="c"># The canvas which holds graphics</span>
<span class="n">_canvas_xs</span> <span class="o">=</span> <span class="bp">None</span>      <span class="c"># Size of canvas object</span>
<span class="n">_canvas_ys</span> <span class="o">=</span> <span class="bp">None</span>
<span class="n">_canvas_x</span> <span class="o">=</span> <span class="bp">None</span>      <span class="c"># Current position on canvas</span>
<span class="n">_canvas_y</span> <span class="o">=</span> <span class="bp">None</span>
<span class="n">_canvas_col</span> <span class="o">=</span> <span class="bp">None</span>      <span class="c"># Current colour (set to black below)</span>
<span class="n">_canvas_tsize</span> <span class="o">=</span> <span class="mi">12</span>
<span class="n">_canvas_tserifs</span> <span class="o">=</span> <span class="mi">0</span>

<span class="k">def</span> <span class="nf">formatColor</span><span class="p">(</span><span class="n">r</span><span class="p">,</span> <span class="n">g</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="k">return</span> <span class="s">&#39;#</span><span class="si">%02x%02x%02x</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">r</span> <span class="o">*</span> <span class="mi">255</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">g</span> <span class="o">*</span> <span class="mi">255</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">b</span> <span class="o">*</span> <span class="mi">255</span><span class="p">))</span>

<span class="k">def</span> <span class="nf">colorToVector</span><span class="p">(</span><span class="n">color</span><span class="p">):</span>
    <span class="k">return</span> <span class="nb">map</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="mi">16</span><span class="p">)</span> <span class="o">/</span> <span class="mf">256.0</span><span class="p">,</span> <span class="p">[</span><span class="n">color</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="mi">3</span><span class="p">],</span> <span class="n">color</span><span class="p">[</span><span class="mi">3</span><span class="p">:</span><span class="mi">5</span><span class="p">],</span> <span class="n">color</span><span class="p">[</span><span class="mi">5</span><span class="p">:</span><span class="mi">7</span><span class="p">]])</span>

<span class="k">if</span> <span class="n">_Windows</span><span class="p">:</span>
    <span class="n">_canvas_tfonts</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;times new roman&#39;</span><span class="p">,</span> <span class="s">&#39;lucida console&#39;</span><span class="p">]</span>
<span class="k">else</span><span class="p">:</span>
    <span class="n">_canvas_tfonts</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;times&#39;</span><span class="p">,</span> <span class="s">&#39;lucidasans-24&#39;</span><span class="p">]</span>
    <span class="k">pass</span> <span class="c"># XXX need defaults here</span>

<span class="k">def</span> <span class="nf">sleep</span><span class="p">(</span><span class="n">secs</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_root_window</span>
    <span class="k">if</span> <span class="n">_root_window</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">secs</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">_root_window</span><span class="o">.</span><span class="n">update_idletasks</span><span class="p">()</span>
        <span class="n">_root_window</span><span class="o">.</span><span class="n">after</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="mi">1000</span> <span class="o">*</span> <span class="n">secs</span><span class="p">),</span> <span class="n">_root_window</span><span class="o">.</span><span class="n">quit</span><span class="p">)</span>
        <span class="n">_root_window</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">begin_graphics</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">640</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">480</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">formatColor</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>

    <span class="k">global</span> <span class="n">_root_window</span><span class="p">,</span> <span class="n">_canvas</span><span class="p">,</span> <span class="n">_canvas_x</span><span class="p">,</span> <span class="n">_canvas_y</span><span class="p">,</span> <span class="n">_canvas_xs</span><span class="p">,</span> <span class="n">_canvas_ys</span><span class="p">,</span> <span class="n">_bg_color</span>

    <span class="c"># Check for duplicate call</span>
    <span class="k">if</span> <span class="n">_root_window</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
        <span class="c"># Lose the window.</span>
        <span class="n">_root_window</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>

    <span class="c"># Save the canvas size parameters</span>
    <span class="n">_canvas_xs</span><span class="p">,</span> <span class="n">_canvas_ys</span> <span class="o">=</span> <span class="n">width</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">height</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="n">_canvas_x</span><span class="p">,</span> <span class="n">_canvas_y</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">_canvas_ys</span>
    <span class="n">_bg_color</span> <span class="o">=</span> <span class="n">color</span>

    <span class="c"># Create the root window</span>
    <span class="n">_root_window</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">Tk</span><span class="p">()</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">protocol</span><span class="p">(</span><span class="s">&#39;WM_DELETE_WINDOW&#39;</span><span class="p">,</span> <span class="n">_destroy_window</span><span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="n">title</span> <span class="ow">or</span> <span class="s">&#39;Graphics Window&#39;</span><span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">resizable</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>

    <span class="c"># Create the canvas object</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">_canvas</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">Canvas</span><span class="p">(</span><span class="n">_root_window</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="n">height</span><span class="p">)</span>
        <span class="n">_canvas</span><span class="o">.</span><span class="n">pack</span><span class="p">()</span>
        <span class="n">draw_background</span><span class="p">()</span>
        <span class="n">_canvas</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="n">_root_window</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="k">raise</span>

    <span class="c"># Bind to key-down and key-up events</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;KeyPress&gt;&quot;</span><span class="p">,</span> <span class="n">_keypress</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;KeyRelease&gt;&quot;</span><span class="p">,</span> <span class="n">_keyrelease</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;FocusIn&gt;&quot;</span><span class="p">,</span> <span class="n">_clear_keys</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;FocusOut&gt;&quot;</span><span class="p">,</span> <span class="n">_clear_keys</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;Button-1&gt;&quot;</span><span class="p">,</span> <span class="n">_leftclick</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;Button-2&gt;&quot;</span><span class="p">,</span> <span class="n">_rightclick</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;Button-3&gt;&quot;</span><span class="p">,</span> <span class="n">_rightclick</span> <span class="p">)</span>
    <span class="n">_root_window</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span> <span class="s">&quot;&lt;Control-Button-1&gt;&quot;</span><span class="p">,</span> <span class="n">_ctrl_leftclick</span><span class="p">)</span>
    <span class="n">_clear_keys</span><span class="p">()</span>

<span class="n">_leftclick_loc</span> <span class="o">=</span> <span class="bp">None</span>
<span class="n">_rightclick_loc</span> <span class="o">=</span> <span class="bp">None</span>
<span class="n">_ctrl_leftclick_loc</span> <span class="o">=</span> <span class="bp">None</span>

<span class="k">def</span> <span class="nf">_leftclick</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_leftclick_loc</span>
    <span class="n">_leftclick_loc</span> <span class="o">=</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">_rightclick</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_rightclick_loc</span>
    <span class="n">_rightclick_loc</span> <span class="o">=</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">_ctrl_leftclick</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_ctrl_leftclick_loc</span>
    <span class="n">_ctrl_leftclick_loc</span> <span class="o">=</span> <span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">x</span><span class="p">,</span> <span class="n">event</span><span class="o">.</span><span class="n">y</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">wait_for_click</span><span class="p">():</span>
    <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
        <span class="k">global</span> <span class="n">_leftclick_loc</span>
        <span class="k">global</span> <span class="n">_rightclick_loc</span>
        <span class="k">global</span> <span class="n">_ctrl_leftclick_loc</span>
        <span class="k">if</span> <span class="n">_leftclick_loc</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">val</span> <span class="o">=</span> <span class="n">_leftclick_loc</span>
            <span class="n">_leftclick_loc</span> <span class="o">=</span> <span class="bp">None</span>
            <span class="k">return</span> <span class="n">val</span><span class="p">,</span> <span class="s">&#39;left&#39;</span>
        <span class="k">if</span> <span class="n">_rightclick_loc</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">val</span> <span class="o">=</span> <span class="n">_rightclick_loc</span>
            <span class="n">_rightclick_loc</span> <span class="o">=</span> <span class="bp">None</span>
            <span class="k">return</span> <span class="n">val</span><span class="p">,</span> <span class="s">&#39;right&#39;</span>
        <span class="k">if</span> <span class="n">_ctrl_leftclick_loc</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">val</span> <span class="o">=</span> <span class="n">_ctrl_leftclick_loc</span>
            <span class="n">_ctrl_leftclick_loc</span> <span class="o">=</span> <span class="bp">None</span>
            <span class="k">return</span> <span class="n">val</span><span class="p">,</span> <span class="s">&#39;ctrl_left&#39;</span>
        <span class="n">sleep</span><span class="p">(</span><span class="mf">0.05</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">draw_background</span><span class="p">():</span>
    <span class="n">corners</span> <span class="o">=</span> <span class="p">[(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">_canvas_ys</span><span class="p">),</span> <span class="p">(</span><span class="n">_canvas_xs</span><span class="p">,</span> <span class="n">_canvas_ys</span><span class="p">),</span> <span class="p">(</span><span class="n">_canvas_xs</span><span class="p">,</span> <span class="mi">0</span><span class="p">)]</span>
    <span class="n">polygon</span><span class="p">(</span><span class="n">corners</span><span class="p">,</span> <span class="n">_bg_color</span><span class="p">,</span> <span class="n">fillColor</span><span class="o">=</span><span class="n">_bg_color</span><span class="p">,</span> <span class="n">filled</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">smoothed</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">_destroy_window</span><span class="p">(</span><span class="n">event</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="c">#    global _root_window</span>
<span class="c">#    _root_window.destroy()</span>
<span class="c">#    _root_window = None</span>
    <span class="c">#print &quot;DESTROY&quot;</span>

<span class="k">def</span> <span class="nf">end_graphics</span><span class="p">():</span>
    <span class="k">global</span> <span class="n">_root_window</span><span class="p">,</span> <span class="n">_canvas</span><span class="p">,</span> <span class="n">_mouse_enabled</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">_root_window</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
                <span class="n">_root_window</span><span class="o">.</span><span class="n">destroy</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">SystemExit</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">print</span> <span class="s">&#39;Ending graphics raised an exception:&#39;</span><span class="p">,</span> <span class="n">e</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="n">_root_window</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="n">_canvas</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="n">_mouse_enabled</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">_clear_keys</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">clear_screen</span><span class="p">(</span><span class="n">background</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_canvas_x</span><span class="p">,</span> <span class="n">_canvas_y</span>
    <span class="n">_canvas</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="s">&#39;all&#39;</span><span class="p">)</span>
    <span class="n">draw_background</span><span class="p">()</span>
    <span class="n">_canvas_x</span><span class="p">,</span> <span class="n">_canvas_y</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="n">_canvas_ys</span>

<span class="k">def</span> <span class="nf">polygon</span><span class="p">(</span><span class="n">coords</span><span class="p">,</span> <span class="n">outlineColor</span><span class="p">,</span> <span class="n">fillColor</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">filled</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">smoothed</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">behind</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">1</span><span class="p">):</span>
    <span class="n">c</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span> <span class="n">coords</span><span class="p">:</span>
        <span class="n">c</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">coord</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
        <span class="n">c</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">coord</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">fillColor</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span> <span class="n">fillColor</span> <span class="o">=</span> <span class="n">outlineColor</span>
    <span class="k">if</span> <span class="n">filled</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="n">fillColor</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>
    <span class="n">poly</span> <span class="o">=</span> <span class="n">_canvas</span><span class="o">.</span><span class="n">create_polygon</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">outline</span><span class="o">=</span><span class="n">outlineColor</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">fillColor</span><span class="p">,</span> <span class="n">smooth</span><span class="o">=</span><span class="n">smoothed</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">behind</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">_canvas</span><span class="o">.</span><span class="n">tag_lower</span><span class="p">(</span><span class="n">poly</span><span class="p">,</span> <span class="n">behind</span><span class="p">)</span> <span class="c"># Higher should be more visible</span>
    <span class="k">return</span> <span class="n">poly</span>

<span class="k">def</span> <span class="nf">square</span><span class="p">(</span><span class="n">pos</span><span class="p">,</span> <span class="n">r</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="n">filled</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">behind</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">pos</span>
    <span class="n">coords</span> <span class="o">=</span> <span class="p">[(</span><span class="n">x</span> <span class="o">-</span> <span class="n">r</span><span class="p">,</span> <span class="n">y</span> <span class="o">-</span> <span class="n">r</span><span class="p">),</span> <span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">r</span><span class="p">,</span> <span class="n">y</span> <span class="o">-</span> <span class="n">r</span><span class="p">),</span> <span class="p">(</span><span class="n">x</span> <span class="o">+</span> <span class="n">r</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">r</span><span class="p">),</span> <span class="p">(</span><span class="n">x</span> <span class="o">-</span> <span class="n">r</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">r</span><span class="p">)]</span>
    <span class="k">return</span> <span class="n">polygon</span><span class="p">(</span><span class="n">coords</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="n">filled</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">behind</span><span class="o">=</span><span class="n">behind</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">circle</span><span class="p">(</span><span class="n">pos</span><span class="p">,</span> <span class="n">r</span><span class="p">,</span> <span class="n">outlineColor</span><span class="p">,</span> <span class="n">fillColor</span><span class="p">,</span> <span class="n">endpoints</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">&#39;pieslice&#39;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">2</span><span class="p">):</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">pos</span>
    <span class="n">x0</span><span class="p">,</span> <span class="n">x1</span> <span class="o">=</span> <span class="n">x</span> <span class="o">-</span> <span class="n">r</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">x</span> <span class="o">+</span> <span class="n">r</span>
    <span class="n">y0</span><span class="p">,</span> <span class="n">y1</span> <span class="o">=</span> <span class="n">y</span> <span class="o">-</span> <span class="n">r</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">r</span>
    <span class="k">if</span> <span class="n">endpoints</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">e</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">359</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">e</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">endpoints</span><span class="p">)</span>
    <span class="k">while</span> <span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="mi">360</span>

    <span class="k">return</span> <span class="n">_canvas</span><span class="o">.</span><span class="n">create_arc</span><span class="p">(</span><span class="n">x0</span><span class="p">,</span> <span class="n">y0</span><span class="p">,</span> <span class="n">x1</span><span class="p">,</span> <span class="n">y1</span><span class="p">,</span> <span class="n">outline</span><span class="o">=</span><span class="n">outlineColor</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">fillColor</span><span class="p">,</span>
                              <span class="n">extent</span><span class="o">=</span><span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">start</span><span class="o">=</span><span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">style</span><span class="o">=</span><span class="n">style</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">image</span><span class="p">(</span><span class="n">pos</span><span class="p">,</span> <span class="nb">file</span><span class="o">=</span><span class="s">&quot;../../blueghost.gif&quot;</span><span class="p">):</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">pos</span>
    <span class="c"># img = PhotoImage(file=file)</span>
    <span class="k">return</span> <span class="n">_canvas</span><span class="o">.</span><span class="n">create_image</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">image</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">PhotoImage</span><span class="p">(</span><span class="nb">file</span><span class="o">=</span><span class="nb">file</span><span class="p">),</span> <span class="n">anchor</span> <span class="o">=</span> <span class="n">Tkinter</span><span class="o">.</span><span class="n">NW</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">refresh</span><span class="p">():</span>
    <span class="n">_canvas</span><span class="o">.</span><span class="n">update_idletasks</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">moveCircle</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">pos</span><span class="p">,</span> <span class="n">r</span><span class="p">,</span> <span class="n">endpoints</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_canvas_x</span><span class="p">,</span> <span class="n">_canvas_y</span>

    <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">pos</span>
<span class="c">#    x0, x1 = x - r, x + r + 1</span>
<span class="c">#    y0, y1 = y - r, y + r + 1</span>
    <span class="n">x0</span><span class="p">,</span> <span class="n">x1</span> <span class="o">=</span> <span class="n">x</span> <span class="o">-</span> <span class="n">r</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">x</span> <span class="o">+</span> <span class="n">r</span>
    <span class="n">y0</span><span class="p">,</span> <span class="n">y1</span> <span class="o">=</span> <span class="n">y</span> <span class="o">-</span> <span class="n">r</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">y</span> <span class="o">+</span> <span class="n">r</span>
    <span class="k">if</span> <span class="n">endpoints</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">e</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">359</span><span class="p">]</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">e</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">endpoints</span><span class="p">)</span>
    <span class="k">while</span> <span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">&gt;</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="mi">360</span>

    <span class="n">edit</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="p">(</span><span class="s">&#39;start&#39;</span><span class="p">,</span> <span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span> <span class="p">(</span><span class="s">&#39;extent&#39;</span><span class="p">,</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
    <span class="n">move_to</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">x0</span><span class="p">,</span> <span class="n">y0</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">edit</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
    <span class="n">_canvas</span><span class="o">.</span><span class="n">itemconfigure</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="o">**</span><span class="nb">dict</span><span class="p">(</span><span class="n">args</span><span class="p">))</span>

<span class="k">def</span> <span class="nf">text</span><span class="p">(</span><span class="n">pos</span><span class="p">,</span> <span class="n">color</span><span class="p">,</span> <span class="n">contents</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="s">&#39;Helvetica&#39;</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">12</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">&#39;normal&#39;</span><span class="p">,</span> <span class="n">anchor</span><span class="o">=</span><span class="s">&quot;nw&quot;</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_canvas_x</span><span class="p">,</span> <span class="n">_canvas_y</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">pos</span>
    <span class="n">font</span> <span class="o">=</span> <span class="p">(</span><span class="n">font</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">size</span><span class="p">),</span> <span class="n">style</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">_canvas</span><span class="o">.</span><span class="n">create_text</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">color</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="n">contents</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="n">font</span><span class="p">,</span> <span class="n">anchor</span><span class="o">=</span><span class="n">anchor</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">changeText</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">newText</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">12</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">&#39;normal&#39;</span><span class="p">):</span>
    <span class="n">_canvas</span><span class="o">.</span><span class="n">itemconfigure</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="n">newText</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">font</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">_canvas</span><span class="o">.</span><span class="n">itemconfigure</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="p">(</span><span class="n">font</span><span class="p">,</span> <span class="s">&#39;-</span><span class="si">%d</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">size</span><span class="p">,</span> <span class="n">style</span><span class="p">))</span>

<span class="k">def</span> <span class="nf">changeColor</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">newColor</span><span class="p">):</span>
    <span class="n">_canvas</span><span class="o">.</span><span class="n">itemconfigure</span><span class="p">(</span><span class="nb">id</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">newColor</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">line</span><span class="p">(</span><span class="n">here</span><span class="p">,</span> <span class="n">there</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="n">formatColor</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">),</span> <span class="n">width</span><span class="o">=</span><span class="mi">2</span><span class="p">):</span>
    <span class="n">x0</span><span class="p">,</span> <span class="n">y0</span> <span class="o">=</span> <span class="n">here</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">here</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="n">x1</span><span class="p">,</span> <span class="n">y1</span> <span class="o">=</span> <span class="n">there</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">there</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">_canvas</span><span class="o">.</span><span class="n">create_line</span><span class="p">(</span><span class="n">x0</span><span class="p">,</span> <span class="n">y0</span><span class="p">,</span> <span class="n">x1</span><span class="p">,</span> <span class="n">y1</span><span class="p">,</span> <span class="n">fill</span><span class="o">=</span><span class="n">color</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">)</span>

<span class="c">##############################################################################</span>
<span class="c">### Keypress handling ########################################################</span>
<span class="c">##############################################################################</span>

<span class="c"># We bind to key-down and key-up events.</span>

<span class="n">_keysdown</span> <span class="o">=</span> <span class="p">{}</span>
<span class="n">_keyswaiting</span> <span class="o">=</span> <span class="p">{}</span>
<span class="c"># This holds an unprocessed key release.  We delay key releases by up to</span>
<span class="c"># one call to keys_pressed() to get round a problem with auto repeat.</span>
<span class="n">_got_release</span> <span class="o">=</span> <span class="bp">None</span>

<span class="k">def</span> <span class="nf">_keypress</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_got_release</span>
    <span class="c">#remap_arrows(event)</span>
    <span class="n">_keysdown</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">keysym</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">_keyswaiting</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">keysym</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="c">#    print event.char, event.keycode</span>
    <span class="n">_got_release</span> <span class="o">=</span> <span class="bp">None</span>

<span class="k">def</span> <span class="nf">_keyrelease</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_got_release</span>
    <span class="c">#remap_arrows(event)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">del</span> <span class="n">_keysdown</span><span class="p">[</span><span class="n">event</span><span class="o">.</span><span class="n">keysym</span><span class="p">]</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="k">pass</span>
    <span class="n">_got_release</span> <span class="o">=</span> <span class="mi">1</span>

<span class="k">def</span> <span class="nf">remap_arrows</span><span class="p">(</span><span class="n">event</span><span class="p">):</span>
    <span class="c"># TURN ARROW PRESSES INTO LETTERS (SHOULD BE IN KEYBOARD AGENT)</span>
    <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">char</span> <span class="ow">in</span> <span class="p">[</span><span class="s">&#39;a&#39;</span><span class="p">,</span> <span class="s">&#39;s&#39;</span><span class="p">,</span> <span class="s">&#39;d&#39;</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">]:</span>
        <span class="k">return</span>
    <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">keycode</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">37</span><span class="p">,</span> <span class="mi">101</span><span class="p">]:</span> <span class="c"># LEFT ARROW (win / x)</span>
        <span class="n">event</span><span class="o">.</span><span class="n">char</span> <span class="o">=</span> <span class="s">&#39;a&#39;</span>
    <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">keycode</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">38</span><span class="p">,</span> <span class="mi">99</span><span class="p">]:</span> <span class="c"># UP ARROW</span>
        <span class="n">event</span><span class="o">.</span><span class="n">char</span> <span class="o">=</span> <span class="s">&#39;w&#39;</span>
    <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">keycode</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">39</span><span class="p">,</span> <span class="mi">102</span><span class="p">]:</span> <span class="c"># RIGHT ARROW</span>
        <span class="n">event</span><span class="o">.</span><span class="n">char</span> <span class="o">=</span> <span class="s">&#39;d&#39;</span>
    <span class="k">if</span> <span class="n">event</span><span class="o">.</span><span class="n">keycode</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">40</span><span class="p">,</span> <span class="mi">104</span><span class="p">]:</span> <span class="c"># DOWN ARROW</span>
        <span class="n">event</span><span class="o">.</span><span class="n">char</span> <span class="o">=</span> <span class="s">&#39;s&#39;</span>

<span class="k">def</span> <span class="nf">_clear_keys</span><span class="p">(</span><span class="n">event</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">_keysdown</span><span class="p">,</span> <span class="n">_got_release</span><span class="p">,</span> <span class="n">_keyswaiting</span>
    <span class="n">_keysdown</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">_keyswaiting</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">_got_release</span> <span class="o">=</span> <span class="bp">None</span>

<span class="k">def</span> <span class="nf">keys_pressed</span><span class="p">(</span><span class="n">d_o_e</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">,</span>
                 <span class="n">d_w</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">DONT_WAIT</span><span class="p">):</span>
    <span class="n">d_o_e</span><span class="p">(</span><span class="n">d_w</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">_got_release</span><span class="p">:</span>
        <span class="n">d_o_e</span><span class="p">(</span><span class="n">d_w</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">_keysdown</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">keys_waiting</span><span class="p">():</span>
    <span class="k">global</span> <span class="n">_keyswaiting</span>
    <span class="n">keys</span> <span class="o">=</span> <span class="n">_keyswaiting</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span>
    <span class="n">_keyswaiting</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="k">return</span> <span class="n">keys</span>

<span class="c"># Block for a list of keys...</span>

<span class="k">def</span> <span class="nf">wait_for_keys</span><span class="p">():</span>
    <span class="n">keys</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">while</span> <span class="n">keys</span> <span class="o">==</span> <span class="p">[]:</span>
        <span class="n">keys</span> <span class="o">=</span> <span class="n">keys_pressed</span><span class="p">()</span>
        <span class="n">sleep</span><span class="p">(</span><span class="mf">0.05</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">keys</span>

<span class="k">def</span> <span class="nf">remove_from_screen</span><span class="p">(</span><span class="n">x</span><span class="p">,</span>
                       <span class="n">d_o_e</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">,</span>
                       <span class="n">d_w</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">DONT_WAIT</span><span class="p">):</span>
    <span class="n">_canvas</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
    <span class="n">d_o_e</span><span class="p">(</span><span class="n">d_w</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">_adjust_coords</span><span class="p">(</span><span class="n">coord_list</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">coord_list</span><span class="p">),</span> <span class="mi">2</span><span class="p">):</span>
        <span class="n">coord_list</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">coord_list</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">+</span> <span class="n">x</span>
        <span class="n">coord_list</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">coord_list</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span> <span class="o">+</span> <span class="n">y</span>
    <span class="k">return</span> <span class="n">coord_list</span>

<span class="k">def</span> <span class="nf">move_to</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
            <span class="n">d_o_e</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">,</span>
            <span class="n">d_w</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">DONT_WAIT</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">y</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">x</span>
        <span class="k">except</span><span class="p">:</span> <span class="k">raise</span>  <span class="s">&#39;incomprehensible coordinates&#39;</span>

    <span class="n">horiz</span> <span class="o">=</span> <span class="bp">True</span>
    <span class="n">newCoords</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">current_x</span><span class="p">,</span> <span class="n">current_y</span> <span class="o">=</span> <span class="n">_canvas</span><span class="o">.</span><span class="n">coords</span><span class="p">(</span><span class="nb">object</span><span class="p">)[</span><span class="mi">0</span><span class="p">:</span><span class="mi">2</span><span class="p">]</span> <span class="c"># first point</span>
    <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span>  <span class="n">_canvas</span><span class="o">.</span><span class="n">coords</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">horiz</span><span class="p">:</span>
            <span class="n">inc</span> <span class="o">=</span> <span class="n">x</span> <span class="o">-</span> <span class="n">current_x</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">inc</span> <span class="o">=</span> <span class="n">y</span> <span class="o">-</span> <span class="n">current_y</span>
        <span class="n">horiz</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">horiz</span>

        <span class="n">newCoords</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">coord</span> <span class="o">+</span> <span class="n">inc</span><span class="p">)</span>

    <span class="n">_canvas</span><span class="o">.</span><span class="n">coords</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="o">*</span><span class="n">newCoords</span><span class="p">)</span>
    <span class="n">d_o_e</span><span class="p">(</span><span class="n">d_w</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">move_by</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
            <span class="n">d_o_e</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">dooneevent</span><span class="p">,</span>
            <span class="n">d_w</span><span class="o">=</span><span class="n">Tkinter</span><span class="o">.</span><span class="n">tkinter</span><span class="o">.</span><span class="n">DONT_WAIT</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">y</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">x</span>
        <span class="k">except</span><span class="p">:</span> <span class="k">raise</span> <span class="ne">Exception</span><span class="p">,</span> <span class="s">&#39;incomprehensible coordinates&#39;</span>

    <span class="n">horiz</span> <span class="o">=</span> <span class="bp">True</span>
    <span class="n">newCoords</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">coord</span> <span class="ow">in</span>  <span class="n">_canvas</span><span class="o">.</span><span class="n">coords</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">horiz</span><span class="p">:</span>
            <span class="n">inc</span> <span class="o">=</span> <span class="n">x</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">inc</span> <span class="o">=</span> <span class="n">y</span>
        <span class="n">horiz</span> <span class="o">=</span> <span class="ow">not</span> <span class="n">horiz</span>

        <span class="n">newCoords</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">coord</span> <span class="o">+</span> <span class="n">inc</span><span class="p">)</span>

    <span class="n">_canvas</span><span class="o">.</span><span class="n">coords</span><span class="p">(</span><span class="nb">object</span><span class="p">,</span> <span class="o">*</span><span class="n">newCoords</span><span class="p">)</span>
    <span class="n">d_o_e</span><span class="p">(</span><span class="n">d_w</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">writePostscript</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span>
    <span class="s">&quot;Writes the current canvas to a postscript file.&quot;</span>
    <span class="n">psfile</span> <span class="o">=</span> <span class="nb">file</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span>
    <span class="n">psfile</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">_canvas</span><span class="o">.</span><span class="n">postscript</span><span class="p">(</span><span class="n">pageanchor</span><span class="o">=</span><span class="s">&#39;sw&#39;</span><span class="p">,</span>
                     <span class="n">y</span><span class="o">=</span><span class="s">&#39;0.c&#39;</span><span class="p">,</span>
                     <span class="n">x</span><span class="o">=</span><span class="s">&#39;0.c&#39;</span><span class="p">))</span>
    <span class="n">psfile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

<span class="n">ghost_shape</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.5</span><span class="p">),</span>
    <span class="p">(</span><span class="mf">0.25</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.75</span><span class="p">),</span>
    <span class="p">(</span><span class="mf">0.5</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.5</span><span class="p">),</span>
    <span class="p">(</span><span class="mf">0.75</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.75</span><span class="p">),</span>
    <span class="p">(</span><span class="mf">0.75</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">),</span>
    <span class="p">(</span><span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.75</span><span class="p">),</span>
    <span class="p">(</span><span class="o">-</span> <span class="mf">0.5</span><span class="p">,</span> <span class="mf">0.75</span><span class="p">),</span>
    <span class="p">(</span><span class="o">-</span> <span class="mf">0.75</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">),</span>
    <span class="p">(</span><span class="o">-</span> <span class="mf">0.75</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.75</span><span class="p">),</span>
    <span class="p">(</span><span class="o">-</span> <span class="mf">0.5</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.5</span><span class="p">),</span>
    <span class="p">(</span><span class="o">-</span> <span class="mf">0.25</span><span class="p">,</span> <span class="o">-</span> <span class="mf">0.75</span><span class="p">)</span>
  <span class="p">]</span>

<span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="n">begin_graphics</span><span class="p">()</span>
    <span class="n">clear_screen</span><span class="p">()</span>
    <span class="n">ghost_shape</span> <span class="o">=</span> <span class="p">[(</span><span class="n">x</span> <span class="o">*</span> <span class="mi">10</span> <span class="o">+</span> <span class="mi">20</span><span class="p">,</span> <span class="n">y</span> <span class="o">*</span> <span class="mi">10</span> <span class="o">+</span> <span class="mi">20</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="ow">in</span> <span class="n">ghost_shape</span><span class="p">]</span>
    <span class="n">g</span> <span class="o">=</span> <span class="n">polygon</span><span class="p">(</span><span class="n">ghost_shape</span><span class="p">,</span> <span class="n">formatColor</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
    <span class="n">move_to</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="p">(</span><span class="mi">50</span><span class="p">,</span> <span class="mi">50</span><span class="p">))</span>
    <span class="n">circle</span><span class="p">((</span><span class="mi">150</span><span class="p">,</span> <span class="mi">150</span><span class="p">),</span> <span class="mi">20</span><span class="p">,</span> <span class="n">formatColor</span><span class="p">(</span><span class="mf">0.7</span><span class="p">,</span> <span class="mf">0.3</span><span class="p">,</span> <span class="mf">0.0</span><span class="p">),</span> <span class="n">endpoints</span><span class="o">=</span><span class="p">[</span><span class="mi">15</span><span class="p">,</span> <span class="o">-</span> <span class="mi">15</span><span class="p">])</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</body>
</html>
