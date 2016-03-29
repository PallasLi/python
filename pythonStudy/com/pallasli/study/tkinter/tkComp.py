'''
Created on 2016年3月24日

@author: lyt

1.Button 按钮。类似标签,但提供额外的功能,例如鼠标掠过、按下、释放以及键盘操作/事件

2.Canvas 画布。提供绘图功能(直线、椭圆、多边形、矩形) ;可以包含图形或位图

3.Checkbutton 选择按钮。一组方框,可以选择其中的任意个(类似 HTML 中的 checkbox)

4.Entry 文本框。单行文字域,用来收集键盘输入(类似 HTML 中的 text)

5.Frame 框架。包含其他组件的纯容器

6.Label 标签。用来显示文字或图片

7.Listbox 列表框。一个选项列表,用户可以从中选择

8.Menu 菜单。点下菜单按钮后弹出的一个选项列表,用户可以从中选择

9.Menubutton 菜单按钮。用来包含菜单的组件(有下拉式、层叠式等等)

10.Message 消息框。类似于标签,但可以显示多行文本

11.Radiobutton 单选按钮。一组按钮,其中只有一个可被“按下” (类似 HTML 中的 radio)

12.Scale 进度条。线性“滑块”组件,可设定起始值和结束值,会显示当前位置的精确值

13.Scrollbar 滚动条。对其支持的组件(文本域、画布、列表框、文本框)提供滚动功能

14.Text 文本域。 多行文字区域,可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)

15.Toplevel 顶级。类似框架,但提供一个独立的窗口容器。

Tkinter支持15个核心的窗口部件，这个15个核心窗口部件类列表如下：

窗口部件及说明：

Button：一个简单的按钮，用来执行一个命令或别的操作。

Canvas：组织图形。这个部件可以用来绘制图表和图，创建图形编辑器，实现定制窗口部件。

Checkbutton：代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换。

Entry：文本输入域。

Frame：一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。

Label：显示一个文本或图象。

Listbox：显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。

Menu：菜单条。用来实现下拉和弹出式菜单。

Menubutton：菜单按钮。用来实现下拉式菜单。

Message：显示一文本。类似label窗口部件，但是能够自动地调整文本到给定的宽度或比率。

Radiobutton：代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。

Scale：允许你通过滑块来设置一数字值。

Scrollbar：为配合使用canvas, entry, listbox, and text窗口部件的标准滚动条。

Text：格式化文本显示。允许你用不同的样式和属性来显示和编辑文本。同时支持内嵌图象和窗口。

Toplevel：一个容器窗口部件，作为一个单独的、最上面的窗口显示。

注意在Tkinter中窗口部件类没有分级；所有的窗口部件类在树中都是兄弟。

所有这些窗口部件提供了Misc和几何管理方法、配置管理方法和部件自己定义的另外的方法。此外，Toplevel类也提供窗口管理接口。这意味一个典型的窗口部件类提供了大约150种方法。

Button窗口部件

Button（按钮）窗口部件是一个标准的Tkinter窗口部件，用来实现各种按钮。按钮能够包含文本或图象，并且你能够将按钮与一个Python函数或方法相关联。当这个按钮被按下时，Tkinter自动调用相关联的函数或方法。

按钮仅能显示一种字体，但是这个文本可以跨行。另外，这个文本中的一个字母可以有下划线，例如标明一个快捷键。默认情况，Tab键用于将焦点移动到一个按钮部件。

一、那么什么时候用按钮部件呢？

简而言之，按钮部件用来让用户说“马上给我执行这个任务”，通常我们用显示在按钮上的文本或图象来提示。按钮通常用在工具条中或应用程序窗口中，并且用来接收或忽略输入在对话框中的数据。

关于按钮和输入的数据的配合，可以参看Checkbutton和Radiobutton部件。

二、样式

普通的按钮很容易被创建，仅仅指定按钮的内容（文本、位图、图象）和一个当按钮被按下时的回调函数即可：b = Button(master, text="OK", command=self.ok)

没有回调函数的按钮是没有用的，当你按下这个按钮时它什么也不做。你可能在开发一个应用程序的时候想实现这种按钮，比如为了不干扰你的beta版的测试者：b = Button(master, text="Help", state=DISABLED)

如 果你没有指定尺寸，按钮的大小将正好能够容纳它的内容。你可以用padx和pady选项来增加内容与按钮边框的间距。你也可以用height和width 选项来显式地设置按钮的尺寸。如果你在按钮中显示文本，那么这些选项将以文本的单位为定义按钮的尺寸。如果你替而代之显示图象，那么按钮的尺寸将是象素 （或其它的屏幕单位）。你实际上甚至能够用象素单位来定义文本按钮的尺寸，但这可能带来意外的结果。下面是指定尺寸的一段例子代码：

f = Frame(master, height=32, width=32)

f.pack_propagate(0) # don't shrink

b = Button(f, text="Sure!")

b.pack(fill=BOTH, expand=1)

按钮能够显示多行文本（但只能用一种字体）。 你可以使用多行或wraplength选项来使按钮自己调整文本。当调整文本时，使用anchor,justify,也可加上padx选项来得到你所希望的格式。一个例子如下：b = Button(master, text=longtext, anchor=W, justify=LEFT, padx=2)

为了使一个普通的按钮看起来像凹入的，例如你想去实现某种类型的工具框，你可简单地将relief的值从"RAISED"改变为"SUNKEN：b.config(relief=SUNKEN)

你也可能想改变背景。注意：一个大概更好的解决方案是使用一个Checkbutton或Radiobutton其indicatoron选项的值设置为false：b = Checkbutton(master, image=bold, variable=var, indicatoron=0)

三、方法

Button窗口部件支持标准的Tkinter窗口部件接口，加上下面的方法：

flash()：频繁重画按钮，使其在活动和普通样式下切换。

invoke() ：调用与按钮相关联的命令。

下面的方法与你实现自己的按钮绑定有关：

tkButtonDown(), tkButtonEnter(), tkButtonInvoke(), tkButtonLeave(), tkButtonUp()这些方法可以用在定制事件绑定中，所有这些方法接收0个或多个形参。

四、选项

Button窗口部件支持下面的选项：

activebackground, activeforeground

类型：颜色；

说明：当按钮被激活时所使用的颜色。

anchor

类型：常量；

说明：控制按钮上内容的位置。使用N, NE, E, SE, S, SW, W, NW, or CENTER这些值之一。默认值是CENTER。

background (bg), foreground (fg)

类型：颜色；

说明：按钮的颜色。默认值与特定平台相关。

bitmap

类型：位图；

说 明：显示在窗口部件中的位图。如果image选项被指定了，则这个选项被忽略。下面的位图在所有平台上都有 效：error, gray75, gray50, gray25, gray12, hourglass, info, questhead, question, 和 warning.

Tkinter类之窗口部件类

这 后面附加的位图仅在Macintosh上有 效：document, stationery, edition, application, accessory, folder, pfolder, trash, floppy, ramdisk, cdrom, preferences, querydoc, stop, note, 和 caution.

你也可以从一个XBM文件中装载位图。只需要在XBM文件名前加一个前缀@,例如"@sample.xbm"。

borderwidth (bd)

类型：整数；

说明：按钮边框的宽度。默认值与特定平台相关。但通常是1或2象素。

command

类型：回调；

说明：当按钮被按下时所调用的一个函数或方法。所回调的可以是一个函数、方法或别的可调用的Python对象。

cursor

类型：光标；

说明：当鼠标移动到按钮上时所显示的光标。

default

类型：常量；

说明：如果设置了，则按钮为默认按钮。注意这个语法在Tk 8.0b2中已改变。

disabledforeground

类型：颜色；

说明：当按钮无效时的颜色。

font

类型：字体；

说明：按钮所使用的字体。按钮只能包含一种字体的文本。

highlightbackground, highlightcolor

类型：颜色；

说明：控制焦点所在的高亮边框的颜色。当窗口部件获得焦点的时候，边框为highlightcolor所指定的颜色。否则边框为highlightbackground所指定的颜色。默认值由系统所定。

highlightthickness

类型：距离；

说明：控制焦点所在的高亮边框的宽度。默认值通常是1或2象素。

image

类型：图象；

说明：在部件中显示的图象。如果指定，则text和bitmap选项将被忽略。

justify

类型：常量；

说明：定义多行文本如何对齐。可取值有：LEFT, RIGHT, 或 CENTER。

padx, pady

类型：距离；

说明：指定文本或图象与按钮边框的间距。

relief

类型：常量；

说明：边框的装饰。通常按钮按下时是凹陷的，否则凸起。另外的可能取值有GROOVE, RIDGE, 和 FLAT。

state

类型：常量；

说明：按钮的状态：NORMAL, ACTIVE 或 DISABLED。默认值为NORMAL。

takefocus

类型：标志；

说明：表明用户可以Tab键来将焦点移到这个按钮上。默认值是一个空字符串，意思是如果按钮有按键绑定的话，它可以通过所绑定的按键来获得焦点。

text

类型：字符串；

说明：显示在按钮中的文本。文本可以是多行。如果bitmaps或image选项被使用，则text选项被忽略。

textvariable

类型：变量；

说明：与按钮相关的Tk变量（通常是一个字符串变量）。如果这个变量的值改变，那么按钮上的文本相应更新。

underline

类型：整数；

说明：在文本标签中哪个字符加下划线。默认值为-1，意思是没有字符加下划线。

width, height

类型：距离；

说明：按钮的尺寸。如果按钮显示文本，尺寸使用文本的单位。如果按钮显示图象，尺寸以象素为单位（或屏幕的单位）。如果尺寸没指定，它将根据按钮的内容来计算。

wraplength

类型：距离；

说明：确定一个按钮的文本何时调整为多行。它以屏幕的单位为单位。默认不调整。

Mixins

Tkinter模块提供了相应于Tk中的各种窗口部件类型的类和一定数量的mixin和别的帮助类（mixin是一个类，被设计来使用多态继承与其它的类结合）。当你使用Tkinter时，你不将直接访问mixin类。

一、实施mixins

通过root窗口和窗口部件类，Misc类被用作mixin。它提供了大量的Tk和窗口相关服务，这些服务对所有Tkinter核心窗口部件者有效。这些通过委托完成；窗口部件仅仅直接请求适当的内部对象。

Wm类通过root窗口和顶级窗口部件类被用作mixin。通过委托它提供了窗口管理服务。

使用委托像这样简化你的应用程序代码：一旦你有一窗口部件，你能够使用这个窗口部件的实例的方法访问Tkinter的所有部份。

二、Geometry(几何学)与mixins

Grid,Pack,Place这些类通过窗口部件类被用作mixins。通过委托，它们也提供了访问不同几何管理的支持。

下面是Geometry Mixins的列表及说明：

管理器及说明：

Grid：grid几何管理器允许你通过在一个二维网格中组织窗口部件来创建一个类似表的版面。

Pack：pack几何管理器通过在一个帧中把窗口部件包装到一个父部件中来创建一个版面。为了对窗口部件使用这个几何管理器，我们在这个窗口部件上使用pack方法来集成。

Place：place几何管理器让你显式将一个窗口部件放到给定的位置。要使用这个几何管理器，需使用place方法。

三、窗口部件配置管理Widget类使用 geometry mixins来混合Misc类，并通过cget和configure方法来增加配置管理，也可以通过一个局部的字典接口。

窗口部件的配置

要配置一个窗口部件的外观，你用选项比使用方法调用好。典型的选项包括text、color、size、command等等。对于处理选项，所有的核心窗口部件执行同样的配置接口：

配置接口

widgetclass(master, option=value, ...) => widget

说明：

创 建这个窗口部件的一个实例，这个实例作为给定的master的孩子，并且使用给定的选项。所有的选项都有默认值，因此在简单的情况下，你仅需要指定这个 master。如果你想的话，你也可以不指定master；Tkinter这时会使用最近创建的root窗口作为master。注意这个name选项仅能 在窗口部件被创建时设置。

cget(option) => string

说明：

返回一个选项的当前值。选项的名字和返回值都是字符串。要得到name选项，使用str(widget)代替。

configure(option=value, ...), config(option=value, ...)

说明：

设置一个或多个选项（作为关键字参数给定）。

注意一些选项的名字与Python中的保留字相同(class,from等)。要使用这些作为关键字参数，仅需要在这些选项名后添加一下划线(class_,from_)。注意你不能用此方法来设置name选项；name选项只能在窗口部件被创建时设置。

为了方便起见，窗口部件也实现一个局部的字典接口。 __setitem__ 方法映射configure，而__getitem__方法映射cget。你可以使用下面的语法来设置和查询选项：

value = widget[option]

widget[option] = value

注意每个赋值都导致一个对Tk的调用。如果你希望去改变多个选项，单独地调用(config或configure)去改变它们是一个好的主意。

这下面的字典方法也适用于窗口部件：

keys() => list

说明：

返回窗口部件中所有可以被设置的选项的一个列表。name选项不包括在这个列表中（它不能通过字典接口被查询或修改）。

向后兼容性

关键字参数在Python1.3时被引入。之前，使用原始的Python字典将选项传递给窗口构造器和configure方法。原代码类似如下：

self.button = Button(frame, {"text": "QUIT", "fg": "red", "command": frame.quit})

self.button.pack({"side": LEFT})

关键字参数语法更优雅和少容易发生错误。但是为了与存在的代码兼容，Tkinter仍支持老的语法。在新的程序中你不应再用老的语法，即使是在某些情况下是很有吸引力的。例如，如果你创建了一个定制的窗口部件，它需要沿它的父类传递配置选项，你的代码可能如下：

def __init__(self, master, **kw):

Canvas.__init__(self, master, kw) # kw 是一个字典

上面的代码在当前版本的Tkinter下工作的很好，但是它在将来的版本下可能不工作。一个通常的办法是使用apply函数：

def __init__(self, master, **kw):

apply(Canvas.__init__, (self, master), kw)

这个apply函数使用了一个函数（一个未约束的方法），一个带参数的元组（它必须包括self，因为我们调用一个未约束的方法），一个可选的，提供了关键字参数的字典。

窗口部件的样式之颜色

所有的Tkinter标准窗口部件提供了一套样式设置选项，这让你可以去修改这些窗口部件的外观如颜色、字体和其它的可视外观。

颜色

大部份窗口部件都允许你指定窗口部件和文本的颜色，这可以使用background和foreground选项。要指定颜色，你可以使用颜色名，也可以使用红、绿、蓝颜色组合。

1、颜色名Tkinter 包括一个颜色数据库，它将颜色名映射到相应的RGB值。这个数据库包括了通常的名称如Red, Green, Blue, Yellow, 和 LightBlue，也可使用外来的如Moccasin，PeachPuff等等。在X window系统上，颜色名由X server定义。你能够找到 一个名为xrgb.txt的文件，它包含了一个由颜色名和相应RGB值组成的列表。在Windows和Macintosh系统上，颜色名表内建于Tk中。

在Windows下，你可以使用Windows系统颜色（用户可以通过控制面板来改变这些颜色）：

SystemActiveBorder, SystemActiveCaption, SystemAppWorkspace, SystemBackground,

SystemButtonFace, SystemButtonHighlight, SystemButtonShadow, SystemButtonText,

SystemCaptionText, SystemDisabledText, SystemHighlight, SystemHighlightText,

SystemInactiveBorder, SystemInactiveCaption, SystemInactiveCaptionText, SystemMenu,

SystemMenuText, SystemScrollbar, SystemWindow, SystemWindowFrame, SystemWindowText。

在Macintosh上，下面的系统颜色是有效的：SystemButtonFace, SystemButtonFrame, SystemButtonText, SystemHighlight, SystemHighlightText, SystemMenu, SystemMenuActive, SystemMenuActiveText, SystemMenuDisabled, SystemMenuText, SystemWindowBody。

颜色名是大小写不敏感的。许多颜色名词与词之间有无格都有效。例如"lightblue", "light blue", 和"Light Blue"都是同一颜色。

2、RGB格式

如果你需要显式地指定颜色名，你可以使用如下格式的字符串：

#RRGGBB

RR, GG, BB 分别是red,green和blue值的十六进制表示。下面的例子演示了如何将一个颜色三元组转换为

一个Tk颜色格式：tk_rgb = "#%02x%02x%02x" % (128, 192, 200)

Tk也支持用形如"#RGB"和"rrrrggggbbbb"去分别指定16和65536程度之间的值。

你可以使用窗口部件的winfo_rgb方法来将一个代表颜色的字符串（名字或RGB格式）转换为一个三元组：

rgb = widget.winfo_rgb("red")

red, green, blue = rgb[0]/256, rgb[1]/256, rgb[2]/256

注意winfo_rgb返回16位的RGB值，范围在0~65535之间。要将它们映射到更通用的0~255范围内，你必须将每个值都除以256（或将它们向右移8位）。

窗口部件的样式之字体

字体窗口部件允许你显示文本和指定所使用的字体。所有的窗口部件都提供了合理的默认值，你很少需要去为简单元素如标签和按钮指定字体。

字体通常使用font窗口部件选项指定。Tkinter支持一定数量的不同字体描述类型：* Font descriptors

* User-defined font names

* System fonts

* X font descriptors

Tk8.0以前的版本仅X font描述被支持。

1、字体描述

从Tk8.0开始，Tkinter支持独立于平台的字体描述。你可以使用元组来指定一个字体，这个元组包含了一个字体类型名字，一个以磅为单位的高度，代表一个或多个样式的字符串。例如：

("Times", 10, "bold")

("Helvetica", 10, "bold italic")

("Symbol", 8)

要得到默认的尺寸和类型，你可以给出作为单一字符串的字体名。如果这个字体类型名字没有包括空格，你也可以给这个字符串自身增加尺寸和样式：

"Times 10 bold"

"Helvetica 10 bold italic"

"Symbol 8"

在大部份Windows平台上存在如下有效的字体类名：

Arial (相 应 于 Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys, MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), 和 Verdana：

Tkinter类之窗口部件类

注意：如果这个字体类型名包含空格，你必须使用上面所描述的元组语法。

有效的样式有normal, bold, roman, italic, underline, and overstrike。

Tk8.0自动映射Courier, Helvetica, 和Times到所有平台上相应的本地字体类型名。此外，在Tk8.0下字体格式不会引起问题，如果Tk不能找出确切的匹配，它会试着找类似的字体，如果失败，Tk就使用特定平台的默认字体。

Tk4.2在Windows下同样支持这种字体描述。这儿有几个限制，包括字体类型名必须在平台上存在，并非这所有上面样式名都存在（或它们中的一些有不同的名字）。

2、字体名此外，Tk8.0允许你去创建已命名的字体并且当为一个窗口部件指定字体时使用它们的名字。

tkFont模块提供一个Font类，这个类允许你去创建字体实例。你可以随处使用这样一个实例。你也可能使用一个字体实例来得到字体的量度，包括存在于那个字体中的字符串所站用的尺寸。

tkFont.Font(family="Times", size=10, weight=tkFont.BOLD)

tkFont.Font(family="Helvetica", size=10, weight=tkFont.BOLD,

slant=tkFont.ITALIC)

tkFont.Font(family="Symbol", size=8)

如果你修改一个已命名的字体（使用config方法），这个改变将自动影响到所有使用这个字体的窗口部件。

Font构造器支持下列的样式选项（注意常量被定义在tkFont模块中）：

样式选项及说明：

family选项

类型：字符串

说明：字体类型

size选项

类型：整型

说明：以磅为单位的字体的尺寸。要以象素为单位的话，使用负值。

weight选项

类型：常量

说明：字体的粗细。使用NORMAL或BOLD。默认为NORMAL。

slant选项

类型：常量

说明：字体倾斜。使用NORMAL或ITALIC。默认为NORMAL。

underline选项

类型：标志

说明：字体下划线。如果1(true)，字体加下划线。默认为0(false)。

overstrike选项

类型：标志

说明：字体划线。如果为1(true)，则字体上有一条线；默认为0(false)。

3、系统字体

Tk也支持特定系统的字体名。在X下，这些通常是字体别名如fixed,6x10等等。

在Windows下，这些包括ansi,ansifixed,device,oemfixed,system和systemfixed：Tkinter类之窗口部件类

在Macintosh上，系统字体名是application和system。

注意：系统字体是字体名，不是字体类型名，它们不能与尺寸或样式属性结合。为了可移植性，尽可能避免使用这些名字。

4、X字体描述

X字体描述是如下格式的字符串（星号所代表的是无关字段。具体细节可查看Tk文档或X手册）：-*-family-weight-slant-*--*-size-*-*-*-*-charset

典型的字体类别如：Times, Helvetica, Courier or Symbol。

weight可以是"Bold"或"Normal"。slant取值中R代表"roman"(正常)，I代表"italic"，o代表团"oblique"（实际上等同于italic）。

size是字体的高度，以十分之一磅为单位。一英寸72磅，但是一些低分辩率的显示器的1磅较常规的大些，以便小字体能够清晰显示。charset（字符集）通常是ISO8859-1 (ISO Latin 1), 但一些字体也使用其它的值。

下面的描述的family取值是Times，weight取值是Bold，slant取值是R，size取值是120，charset取值是ISO8859-1：-*-Times-Bold-R-*--*-120-*-*-*-*-ISO8859-1

如果你不关心charset（字符集），或你使用如Symbol的字体（这种字体类别有特定的字符集），那么你可以使用一个星号作为描述的最后部分：-*-Symbol-*-*-*--*-80-*

典 型的X server至少支持Times, Helvetica, Courier等字体，size有8, 10, 12, 14, 18, 和 24 磅，weight有normal，bold、italic(Times)或oblique(Helvetica, Courier)。大多数的服务器都有 支持随意查看字体。你可以使用如xlsfonts和xfontsel来检查你所访问的服务器的字体。

这种类型的字体描述可以用在Windows 和Macintosh上。注意：如果你使用Tk4.2，你必须牢记字体类型必须是Windows所支持的一种。
'''
