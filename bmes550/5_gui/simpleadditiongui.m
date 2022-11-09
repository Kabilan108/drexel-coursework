function varargout = simpleadditiongui(varargin)
% SIMPLEADDITIONGUI MATLAB code for simpleadditiongui.fig
%      SIMPLEADDITIONGUI, by itself, creates a new SIMPLEADDITIONGUI or raises the existing
%      singleton*.
%
%      H = SIMPLEADDITIONGUI returns the handle to a new SIMPLEADDITIONGUI or the handle to
%      the existing singleton*.
%
%      SIMPLEADDITIONGUI('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SIMPLEADDITIONGUI.M with the given input arguments.
%
%      SIMPLEADDITIONGUI('Property','Value',...) creates a new SIMPLEADDITIONGUI or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before simpleadditiongui_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to simpleadditiongui_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help simpleadditiongui

% Last Modified by GUIDE v2.5 17-Nov-2020 12:54:41

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @simpleadditiongui_OpeningFcn, ...
                   'gui_OutputFcn',  @simpleadditiongui_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before simpleadditiongui is made visible.
function simpleadditiongui_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to simpleadditiongui (see VARARGIN)

% Choose default command line output for simpleadditiongui
handles.output = hObject;

handles.figure1.Color = [1 1 0];


% Update handles structure
guidata(hObject, handles);

% UIWAIT makes simpleadditiongui wait for user response (see UIRESUME)
 uiwait(handles.figure1);



% --- Executes when user attempts to close figure1.
function figure1_CloseRequestFcn(hObject, eventdata, handles)
% hObject    handle to figure1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: delete(hObject) closes the figure
%delete(hObject);
if isequal(get(hObject,'waitstatus'),'waiting')
    uiresume(hObject);
else
    delete(hObject);
end


% --- Outputs from this function are returned to the command line.
function varargout = simpleadditiongui_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% Get default command line output from handles structure
%varargout{1} = handles.output;
%varargout{1} = sqrt(5);
%varargout{1} = handles.result.String;
% TODO: FIND OUT WHY handles.myresulttobereturned is not available here.
varargout{1} = handles.myresulttobereturned;
delete(handles.figure1);


function secondnumber_Callback(hObject, eventdata, handles)
% hObject    handle to secondnumber (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of secondnumber as text
%        str2double(get(hObject,'String')) returns contents of secondnumber as a double


% --- Executes during object creation, after setting all properties.
function secondnumber_CreateFcn(hObject, eventdata, handles)
% hObject    handle to secondnumber (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function firstnumber_Callback(hObject, eventdata, handles)
% hObject    handle to firstnumber (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of firstnumber as text
%        str2double(get(hObject,'String')) returns contents of firstnumber as a double


% --- Executes during object creation, after setting all properties.
function firstnumber_CreateFcn(hObject, eventdata, handles)
% hObject    handle to firstnumber (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


x=linspace(-pi,pi, 100);
plot(handles.ax2, rand(1,10),rand(1,10) );

fprintf('Big Button is clicked\n');
resultnum = str2double(handles.firstnumber.String) + str2double(handles.secondnumber.String);
handles.result.String = sprintf('%f',resultnum);
handles.myresulttobereturned = handles.result.String;
guidata(hObject, handles);


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
fprintf('Small Button is clicked\n');
guidata(hObject, handles);
