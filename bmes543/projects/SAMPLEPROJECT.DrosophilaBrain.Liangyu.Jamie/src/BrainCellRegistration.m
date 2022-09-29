function varargout = BrainCellRegistration(varargin)
% BRAINCELLREGISTRATION MATLAB code for BrainCellRegistration.fig
%      BRAINCELLREGISTRATION, by itself, creates a new BRAINCELLREGISTRATION or raises the existing
%      singleton*.
%
%      H = BRAINCELLREGISTRATION returns the handle to a new BRAINCELLREGISTRATION or the handle to
%      the existing singleton*.
%
%      BRAINCELLREGISTRATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in BRAINCELLREGISTRATION.M with the given input arguments.
%
%      BRAINCELLREGISTRATION('Property','Value',...) creates a new BRAINCELLREGISTRATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before BrainCellRegistration_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to BrainCellRegistration_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help BrainCellRegistration

% Last Modified by GUIDE v2.5 12-Dec-2019 18:31:54

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @BrainCellRegistration_OpeningFcn, ...
                   'gui_OutputFcn',  @BrainCellRegistration_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

addpath(getenv('BMESAHMETDIR'));

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before BrainCellRegistration is made visible.
function BrainCellRegistration_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to BrainCellRegistration (see VARARGIN)

% Choose default command line output for BrainCellRegistration
handles.output = hObject;

set(handles.RegType, 'String', {'Rigid','NonRigid'});

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes BrainCellRegistration wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = BrainCellRegistration_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on slider movement.
function img1Channel_Callback(hObject, eventdata, handles)
% hObject    handle to img1Channel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
channelselect(handles,1);

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function img1Channel_CreateFcn(hObject, eventdata, handles)
% hObject    handle to img1Channel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function img2Channel_Callback(hObject, eventdata, handles)
% hObject    handle to img2Channel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
channelselect(handles,2);

% Update handles structure
guidata(hObject, handles);


% --- Executes during object creation, after setting all properties.
function img2Channel_CreateFcn(hObject, eventdata, handles)
% hObject    handle to img2Channel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on slider movement.
function imgMergeChannel_Callback(hObject, eventdata, handles)
% hObject    handle to imgMergeChannel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider
channelselect(handles,'merged');

% Update handles structure
guidata(hObject, handles);

% --- Executes during object creation, after setting all properties.
function imgMergeChannel_CreateFcn(hObject, eventdata, handles)
% hObject    handle to imgMergeChannel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in selImg1.
function selImg1_Callback(hObject, eventdata, handles)
% hObject    handle to selImg1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[handles] = imgselect(handles, 1);

% Update handles structure
guidata(hObject, handles);


% --- Executes on button press in selImg2.
function selImg2_Callback(hObject, eventdata, handles)
% hObject    handle to selImg2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

[handles] = imgselect(handles, 2);

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in savedatabase.
function savedatabase_Callback(hObject, eventdata, handles)
% hObject    handle to savedatabase (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

handles = savedatabase(handles);

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in RunDetection.
function RunDetection_Callback(hObject, eventdata, handles)
% hObject    handle to RunDetection (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
int_thres = str2double(get(handles.int_thres,'String'));
min_size = str2double(get(handles.min_size,'String'));
[handles, num1, num2, nOverlap] = celldetect(handles, int_thres, min_size);

handles.num_cells1.String = ['# of cells: ' num2str(num1)];
handles.num_cells2.String = ['# of cells: ' num2str(num2)];
handles.num_cells3.String = ['# of overlaps: ' num2str(nOverlap)];

handles.cells.i1 = num1;
handles.cells.i2 = num2;
handles.cells.iOverlap = nOverlap;

% Update handles structure
guidata(hObject, handles);


function int_thres_Callback(hObject, eventdata, handles)
% hObject    handle to int_thres (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of int_thres as text
%        str2double(get(hObject,'String')) returns contents of int_thres as a double


% --- Executes during object creation, after setting all properties.
function int_thres_CreateFcn(hObject, eventdata, handles)
% hObject    handle to int_thres (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function min_size_Callback(hObject, eventdata, handles)
% hObject    handle to min_size (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of min_size as text
%        str2double(get(hObject,'String')) returns contents of min_size as a double


% --- Executes during object creation, after setting all properties.
function min_size_CreateFcn(hObject, eventdata, handles)
% hObject    handle to min_size (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in listbox2.
function listbox2_Callback(hObject, eventdata, handles)
% hObject    handle to listbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns listbox2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox2


% --- Executes during object creation, after setting all properties.
function listbox2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function TLCorner_Callback(hObject, eventdata, handles)
% hObject    handle to TLCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of TLCorner as text
%        str2double(get(hObject,'String')) returns contents of TLCorner as a double


% --- Executes during object creation, after setting all properties.
function TLCorner_CreateFcn(hObject, eventdata, handles)
% hObject    handle to TLCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function BLCorner_Callback(hObject, eventdata, handles)
% hObject    handle to BLCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of BLCorner as text
%        str2double(get(hObject,'String')) returns contents of BLCorner as a double


% --- Executes during object creation, after setting all properties.
function BLCorner_CreateFcn(hObject, eventdata, handles)
% hObject    handle to BLCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function TRCorner_Callback(hObject, eventdata, handles)
% hObject    handle to TRCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of TRCorner as text
%        str2double(get(hObject,'String')) returns contents of TRCorner as a double


% --- Executes during object creation, after setting all properties.
function TRCorner_CreateFcn(hObject, eventdata, handles)
% hObject    handle to TRCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function BRCorner_Callback(hObject, eventdata, handles)
% hObject    handle to BRCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of BRCorner as text
%        str2double(get(hObject,'String')) returns contents of BRCorner as a double


% --- Executes during object creation, after setting all properties.
function BRCorner_CreateFcn(hObject, eventdata, handles)
% hObject    handle to BRCorner (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function regThresh_Callback(hObject, eventdata, handles)
% hObject    handle to regThresh (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of regThresh as text
%        str2double(get(hObject,'String')) returns contents of regThresh as a double


% --- Executes during object creation, after setting all properties.
function regThresh_CreateFcn(hObject, eventdata, handles)
% hObject    handle to regThresh (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in previewOptions.
function previewOptions_Callback(hObject, eventdata, handles)
% hObject    handle to previewOptions (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[handles] = preimgreg(handles);

% Update handles structure
guidata(hObject, handles);

% --- Executes on button press in RunReg.
function RunReg_Callback(hObject, eventdata, handles)
% hObject    handle to RunReg (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
[handles] = runimgreg(handles);

img2Channel_Callback(hObject, eventdata, handles);
imgMergeChannel_Callback(hObject, eventdata, handles);

% Update handles structure
guidata(hObject, handles);

% --- Executes on selection change in RegType.
function RegType_Callback(hObject, eventdata, handles)
% hObject    handle to RegType (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns RegType contents as cell array
%        contents{get(hObject,'Value')} returns selected item from RegType


% --- Executes during object creation, after setting all properties.
function RegType_CreateFcn(hObject, eventdata, handles)
% hObject    handle to RegType (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in rotProcess.
function rotProcess_Callback(hObject, eventdata, handles)
% hObject    handle to rotProcess (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

[handles] = preprocess(handles);

% update images
img1Channel_Callback(hObject, eventdata, handles)
img2Channel_Callback(hObject, eventdata, handles)
imgMergeChannel_Callback(hObject, eventdata, handles)
% Update handles structure
guidata(hObject, handles);

function editdate_Callback(hObject, eventdata, handles)
% hObject    handle to editdate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of editdate as text
%        str2double(get(hObject,'String')) returns contents of editdate as a double


% --- Executes during object creation, after setting all properties.
function editdate_CreateFcn(hObject, eventdata, handles)
% hObject    handle to editdate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
